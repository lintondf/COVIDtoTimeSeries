# State and Country COVID-19 Analysis #
## Updated: at 2020-07-30 for data as of 2020-07-29 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 35.9% of deaths and 40.0% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 69.1% of deaths and 56.4% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 120   |   32683|    1680.062|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 120   |   15861|    1785.685|   0.1%/712|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 120   |    8821|     223.246|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 120   |    8575|    1233.916|   0.2%/399|   0.2%/430|   0.2%/437|   0.2%/445 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 120   |    7661|     604.580|   0.2%/333|   0.2%/384|   0.2%/397|   0.2%/409 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 120   |    7183|     561.117|   0.2%/328|   0.2%/381|   0.2%/397|   0.2%/415 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 120   |    6432|     644.054|   0.1%/716|   0.1%/968|   0.1%/ ***|   0.1%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 120   |    6276|     292.188|   2.3%/ 30|   2.4%/ 29|   2.4%/ 29|   2.4%/ 28 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 120   |    5573|     192.207|   4.2%/ 16|   4.8%/ 14|   5.0%/ 14|   5.2%/ 13 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 120   |    4431|    1242.796|   0.1%/906|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 120   |  149814|     454.610|   0.6%/107|   0.7%/100|   0.7%/ 99|   0.7%/ 97 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 120   |   90605|     428.573|   1.3%/ 55|   1.2%/ 60|   1.1%/ 61|   1.1%/ 62 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 120   |   46058|     693.267|   0.1%/494|   0.1%/543|   0.1%/556|   0.1%/570 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 120   |   45698|     361.028|   1.5%/ 46|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 120   |   35145|     583.431|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 120   |   35083|      25.773|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 120   |   30255|     451.050|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 120   |   28440|     603.821|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 120   |   19275|     599.887|   1.3%/ 51|   1.3%/ 54|   1.2%/ 55|   1.2%/ 56 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 120   |   16397|     196.665|   1.4%/ 48|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 120   |    1546|     315.385|   1.8%/ 39|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 120   |      21|      28.634|   2.5%/ 27|   3.1%/ 22|   3.2%/ 21|   3.4%/ 21 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 120   |    3575|     491.179|   2.5%/ 27|   2.3%/ 30|   2.2%/ 31|   2.2%/ 32 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 120   |     427|     141.522|   1.8%/ 39|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 120   |    8821|     223.246|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 120   |    1812|     314.687|   0.3%/225|   0.3%/207|   0.3%/203|   0.3%/199 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 120   |    4431|    1242.796|   0.1%/906|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 120   |     576|     591.126|   0.2%/461|   0.1%/476|   0.1%/482|   0.1%/488 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 120   |    6276|     292.188|   2.3%/ 30|   2.4%/ 29|   2.4%/ 29|   2.4%/ 28 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 120   |    3592|     338.344|   1.1%/ 61|   1.3%/ 54|   1.3%/ 53|   1.3%/ 52 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 120   |      27|      19.161|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 120   |     159|      88.744|   2.0%/ 34|   2.3%/ 30|   2.4%/ 29|   2.4%/ 28 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 120   |    7661|     604.580|   0.2%/333|   0.2%/384|   0.2%/397|   0.2%/409 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 120   |    2932|     435.499|   0.4%/196|   0.4%/193|   0.4%/192|   0.4%/191 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 120   |     851|     269.642|   0.7%/102|   0.7%/102|   0.7%/102|   0.7%/102 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 120   |     340|     116.622|   0.9%/ 74|   1.1%/ 64|   1.1%/ 62|   1.1%/ 60 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 120   |     721|     161.488|   0.9%/ 81|   0.9%/ 81|   0.9%/ 80|   0.9%/ 80 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 120   |    3831|     824.166|   0.8%/ 92|   0.9%/ 80|   0.9%/ 78|   0.9%/ 75 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 120   |     121|      90.081|   0.4%/179|   0.3%/208|   0.3%/217|   0.3%/225 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 120   |    3470|     573.912|   0.3%/256|   0.3%/259|   0.3%/259|   0.3%/259 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 120   |    8575|    1233.916|   0.2%/399|   0.2%/430|   0.2%/437|   0.2%/445 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 120   |    6432|     644.054|   0.1%/716|   0.1%/968|   0.1%/ ***|   0.1%/ *** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 120   |    1630|     289.001|   0.3%/227|   0.3%/241|   0.3%/246|   0.3%/250 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 120   |    1554|     522.223|   1.3%/ 52|   1.4%/ 51|   1.4%/ 51|   1.4%/ 51 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 120   |    1232|     200.764|   0.8%/ 90|   0.9%/ 81|   0.9%/ 79|   0.9%/ 77 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 120   |      52|      48.879|   3.3%/ 21|   3.6%/ 19|   3.7%/ 18|   3.8%/ 18 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 120   |     325|     167.862|   0.6%/108|   0.7%/106|   0.6%/107|   0.6%/107 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 120   |     772|     250.663|   1.5%/ 47|   1.5%/ 46|   1.5%/ 45|   1.5%/ 45 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 120   |     412|     302.717|   0.3%/233|   0.3%/243|   0.3%/246|   0.3%/248 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 120   |   15861|    1785.685|   0.1%/712|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 120   |     629|     299.782|   0.9%/ 76|   1.0%/ 72|   1.0%/ 71|   1.0%/ 70 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 120   |   32683|    1680.062|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 120   |    1887|     179.906|   1.2%/ 55|   1.3%/ 54|   1.3%/ 53|   1.3%/ 53 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 120   |     102|     133.614|   0.9%/ 75|   0.9%/ 75|   0.9%/ 76|   0.9%/ 76 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 120   |    3388|     289.809|   0.7%/100|   0.8%/ 91|   0.8%/ 89|   0.8%/ 87 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 120   |     512|     129.385|   1.2%/ 55|   1.4%/ 50|   1.4%/ 49|   1.5%/ 48 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 120   |     302|      71.551|   1.6%/ 43|   1.7%/ 40|   1.8%/ 39|   1.8%/ 38 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 120   |    7183|     561.117|   0.2%/328|   0.2%/381|   0.2%/397|   0.2%/415 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 120   |     207|      64.764|   1.5%/ 46|   1.7%/ 41|   1.7%/ 40|   1.8%/ 38 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 120   |    1009|     952.321|   0.2%/454|   0.1%/562|   0.1%/597|   0.1%/637 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 120   |    1598|     310.289|   3.2%/ 22|   3.4%/ 20|   3.5%/ 20|   3.5%/ 19 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 120   |     128|     144.285|   0.9%/ 81|   0.7%/102|   0.6%/110|   0.6%/118 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 120   |    1022|     149.559|   1.8%/ 37|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 120   |    5573|     192.207|   4.2%/ 16|   4.8%/ 14|   5.0%/ 14|   5.2%/ 13 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 120   |  149814|     454.610|   0.6%/107|   0.7%/100|   0.7%/ 99|   0.7%/ 97 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 120   |     293|      91.442|   1.7%/ 40|   1.7%/ 42|   1.6%/ 42|   1.6%/ 43 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 120   |      56|      89.745|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 120   |    2115|     247.742|   0.4%/170|   0.3%/203|   0.3%/213|   0.3%/222 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 120   |    1530|     200.876|   0.6%/108|   0.7%/104|   0.7%/103|   0.7%/102 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 120   |     106|      59.195|   0.7%/ 97|   0.9%/ 81|   0.9%/ 77|   0.9%/ 74 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 120   |     905|     155.484|   0.6%/107|   0.7%/ 94|   0.8%/ 91|   0.8%/ 89 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 108   |      26|      45.493|   0.8%/ 91|   0.6%/108|   0.6%/115|   0.6%/122 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 120   |    1321|      41.000|   1.2%/ 57|   0.8%/ 84|   0.7%/ 95|   0.6%/111 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 120   |     150|      52.587|   3.1%/ 22|   3.2%/ 22|   3.2%/ 21|   3.2%/ 21 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 120   |    1186|      27.584|   0.9%/ 74|   0.9%/ 73|   0.9%/ 73|   0.9%/ 73 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 120   |      44|       1.398|   4.3%/ 16|   5.6%/ 12|   6.0%/ 11|   6.4%/ 11 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 120   |    3262|      72.583|   3.4%/ 20|   3.6%/ 19|   3.6%/ 19|   3.7%/ 19 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 120   |     744|     251.529|   1.4%/ 49|   1.1%/ 61|   1.1%/ 65|   1.0%/ 70 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 120   |     143|       5.570|   3.6%/ 19|   4.6%/ 15|   4.9%/ 14|   5.2%/ 13 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 120   |     714|      80.184|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 120   |     445|      44.194|   2.1%/ 33|   1.9%/ 36|   1.9%/ 37|   1.8%/ 38 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 120   |     147|      95.353|   1.5%/ 46|   1.3%/ 53|   1.3%/ 55|   1.2%/ 57 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 120   |    3063|      18.180|   1.5%/ 46|   1.4%/ 49|   1.4%/ 49|   1.4%/ 50 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 120   |     551|      58.526|   1.0%/ 72|   0.9%/ 78|   0.9%/ 80|   0.8%/ 82 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 120   |    9831|     853.032|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 115   |      37|       3.188|   3.1%/ 22|   1.0%/ 71|   1.0%/ 71|   0.9%/ 73 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 120   |    2811|     245.097|   2.6%/ 26|   2.5%/ 28|   2.5%/ 28|   2.4%/ 28 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 120   |     303|      91.895|   1.8%/ 38|   1.8%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 120   |       1|       0.428|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 120   |   90605|     428.573|   1.3%/ 55|   1.2%/ 60|   1.1%/ 61|   1.1%/ 62 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 120   |     361|      51.882|   1.7%/ 40|   1.8%/ 39|   1.8%/ 38|   1.8%/ 38 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 120   |      53|       2.540|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 108   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 120   |     395|      14.872|   0.5%/139|   0.5%/129|   0.5%/127|   0.5%/126 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 120   |    8968|     235.994|   0.1%/827|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  68   |      60|      10.932|   0.9%/ 74|   0.5%/130|   0.4%/168|   0.3%/250 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  93   |      75|       4.619|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 120   |    9683|     506.750|   1.0%/ 72|   0.8%/ 82|   0.8%/ 84|   0.8%/ 87 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 120   |    4652|       3.318|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 120   |    9370|     189.695|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21|   3.2%/ 21 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 120   |     134|      26.490|   8.2%/  8|   8.7%/  8|   8.8%/  8|   8.9%/  8 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 120   |     137|      33.556|   1.3%/ 54|   1.6%/ 43|   1.7%/ 41|   1.8%/ 39 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 120   |      87|       7.774|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 120   |     614|     105.382|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 120   |    1113|     107.459|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49|   1.4%/ 48 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 120   |    5642|     323.012|   0.6%/115|   0.5%/130|   0.5%/134|   0.5%/139 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 120   |    4823|      48.103|   1.1%/ 61|   0.9%/ 81|   0.8%/ 88|   0.7%/ 96 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 120   |     438|      67.566|   2.8%/ 25|   2.6%/ 26|   2.6%/ 27|   2.5%/ 27 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  99   |      51|      37.548|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 116   |     246|       2.495|   4.0%/ 17|   4.4%/ 16|   4.5%/ 15|   4.5%/ 15 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 120   |     329|      59.454|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 120   |   30255|     451.050|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 120   |      49|      22.498|   0.4%/162|   0.5%/134|   0.5%/127|   0.6%/121 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 120   |       7|       3.170|   7.3%/  9|   9.2%/  7|   9.6%/  7|  10.1%/  7 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 117   |      16|       4.397|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 120   |    9136|     109.870|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 120   |     171|       5.659|   1.5%/ 47|   1.6%/ 44|   1.6%/ 43|   1.6%/ 43 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 120   |     203|      18.922|   0.3%/248|   0.3%/200|   0.4%/191|   0.4%/183 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 120   |    1880|     113.198|   2.3%/ 30|   1.9%/ 36|   1.8%/ 38|   1.7%/ 40 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 106   |      45|       3.707|   1.5%/ 48|   1.7%/ 40|   1.8%/ 38|   1.9%/ 36 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  95   |      26|      16.207|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 116   |     163|      14.055|   0.8%/ 83|   0.5%/153|   0.4%/190|   0.3%/250 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 120   |    1223|     133.519|   3.0%/ 23|   3.2%/ 21|   3.3%/ 21|   3.4%/ 20 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 120   |     597|      61.085|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 120   |   35083|      25.773|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 120   |    5055|      18.940|   1.9%/ 37|   1.8%/ 38|   1.8%/ 38|   1.8%/ 39 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 120   |   16397|     196.665|   1.4%/ 48|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 120   |    4722|     120.685|   2.2%/ 32|   1.8%/ 38|   1.7%/ 40|   1.6%/ 42 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 120   |    1766|     358.840|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 120   |     490|      53.365|   1.9%/ 37|   2.0%/ 34|   2.1%/ 33|   2.1%/ 33 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 120   |   35145|     583.431|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 120   |      10|       3.667|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 120   |     999|       7.933|   0.1%/565|   0.2%/462|   0.2%/440|   0.2%/421 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 120   |      11|       1.055|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 120   |     764|      40.899|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 120   |     310|       6.509|   2.8%/ 25|   2.8%/ 25|   2.8%/ 25|   2.8%/ 25 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 120   |     199|     110.646|   4.2%/ 16|   4.0%/ 17|   4.0%/ 17|   4.0%/ 17 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 117   |     442|     100.042|   0.8%/ 85|   0.9%/ 79|   0.9%/ 77|   0.9%/ 76 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 118   |     321|      49.167|   3.5%/ 20|   2.6%/ 26|   2.4%/ 29|   2.2%/ 32 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 118   |      31|      16.358|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 120   |      47|       6.832|   2.5%/ 28|   3.2%/ 22|   3.4%/ 21|   3.5%/ 19 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 117   |      79|      17.631|   0.6%/110|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 119   |      68|       9.898|   3.8%/ 18|   4.5%/ 15|   4.7%/ 15|   4.9%/ 14 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 120   |      80|      28.725|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  74   |      99|       3.764|   5.4%/ 13|   5.5%/ 12|   5.6%/ 12|   5.7%/ 12 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 120   |     124|       3.786|   0.1%/562|   0.1%/502|   0.1%/489|   0.1%/476 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 120   |     124|       6.118|   0.2%/373|   0.2%/342|   0.2%/333|   0.2%/324 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 120   |     159|      39.099|   0.3%/226|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 120   |   45698|     361.028|   1.5%/ 46|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 120   |     762|     284.128|   1.0%/ 69|   1.0%/ 73|   0.9%/ 73|   0.9%/ 74 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 120   |     318|       8.874|   1.8%/ 38|   2.1%/ 33|   2.2%/ 32|   2.3%/ 30 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  66   |      11|       0.372|   1.7%/ 41|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  20   |       9|       3.660|  18.1%/  4|   4.6%/ 15|   4.6%/ 15|   4.0%/ 17 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  75   |      49|       1.631|   1.8%/ 38|   2.6%/ 26|   2.8%/ 24|   3.0%/ 23 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 120   |    6162|     352.971|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 120   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 120   |     115|      17.736|   1.2%/ 57|   1.2%/ 56|   1.2%/ 56|   1.2%/ 56 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 120   |      69|       3.103|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 120   |     886|       4.300|   1.0%/ 67|   0.8%/ 82|   0.8%/ 86|   0.8%/ 91 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 120   |     482|     231.991|   1.3%/ 53|   1.2%/ 58|   1.2%/ 60|   1.1%/ 61 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 120   |     256|      47.658|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 120   |     417|      89.411|   2.8%/ 25|   2.7%/ 26|   2.6%/ 26|   2.6%/ 26 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 120   |    5991|      27.315|   0.6%/113|   0.4%/182|   0.3%/214|   0.3%/260 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 120   |    1401|     332.027|   2.4%/ 29|   2.2%/ 31|   2.2%/ 31|   2.1%/ 32 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 120   |      47|       6.510|   3.7%/ 18|   4.1%/ 17|   4.2%/ 17|   4.2%/ 16 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 120   |   19275|     599.887|   1.3%/ 51|   1.3%/ 54|   1.2%/ 55|   1.2%/ 56 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 120   |    2013|      18.550|   0.9%/ 77|   0.9%/ 81|   0.8%/ 82|   0.8%/ 83 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 120   |    1693|      44.117|   0.4%/165|   0.4%/175|   0.4%/177|   0.4%/180 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 120   |    1731|     168.408|   0.2%/310|   0.2%/388|   0.2%/413|   0.2%/441 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 120   |     171|      62.148|   0.7%/ 94|   0.5%/145|   0.4%/167|   0.4%/196 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 120   |    2260|     116.485|   1.1%/ 65|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 120   |   13753|      93.721|   1.1%/ 65|   0.9%/ 74|   0.9%/ 77|   0.9%/ 80 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  61   |       5|       0.404|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 120   |    2866|      83.748|   1.4%/ 50|   1.2%/ 60|   1.1%/ 63|   1.0%/ 66 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 120   |     200|      12.339|   1.9%/ 37|   1.9%/ 36|   2.0%/ 35|   2.0%/ 35 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 120   |     576|      82.738|   2.0%/ 35|   1.6%/ 43|   1.5%/ 46|   1.4%/ 48 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  98   |      67|       8.456|   0.2%/281|   0.1%/470|   0.1%/581|   0.1%/768 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 120   |      27|       4.775|   0.1%/828|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 120   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 120   |     117|      55.748|   0.2%/300|   0.3%/223|   0.3%/209|   0.4%/197 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 113   |      93|       5.860|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 120   |    7508|     127.735|   3.6%/ 19|   3.7%/ 18|   3.7%/ 18|   3.8%/ 18 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 120   |   28440|     603.821|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 120   |      11|       0.505|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 120   |     734|      17.287|   0.6%/113|   0.5%/131|   0.5%/137|   0.5%/143 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 120   |    5739|     555.106|   0.2%/384|   0.1%/474|   0.1%/505|   0.1%/541 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 120   |    1978|     229.949|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 120   |      45|       2.550|   6.5%/ 11|   4.6%/ 15|   3.6%/ 19|   1.7%/ 40 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 120   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 120   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 120   |      18|       2.335|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 120   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 120   |      50|       4.265|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 120   |    5670|      68.183|   0.3%/220|   0.3%/235|   0.3%/239|   0.3%/243 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 120   |  149814|     454.610|   0.6%/107|   0.7%/100|   0.7%/ 99|   0.7%/ 97 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 120   |    1677|      40.047|   1.0%/ 66|   1.0%/ 72|   0.9%/ 73|   0.9%/ 75 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 120   |     348|      35.149|   0.3%/274|   0.2%/319|   0.2%/332|   0.2%/345 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 120   |   46058|     693.267|   0.1%/494|   0.1%/543|   0.1%/556|   0.1%/570 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 120   |      36|      10.092|   0.8%/ 83|   0.7%/ 94|   0.7%/ 97|   0.7%/101 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 120   |     136|       3.987|   4.5%/ 15|   3.7%/ 18|   3.5%/ 19|   3.4%/ 20 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 120   |     158|       4.896|   3.3%/ 21|   3.0%/ 23|   3.0%/ 23|   2.9%/ 24 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 119   |     182|      10.182|   1.5%/ 45|   1.0%/ 71|   0.7%/ 97|   1.7%/ 42 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 120   |      40|       2.666|   5.5%/ 12|   4.3%/ 16|   4.1%/ 17|   3.8%/ 18 |

