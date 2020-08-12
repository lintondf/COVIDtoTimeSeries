# State and Country COVID-19 Analysis #
## Updated: at 2020-08-12 for data as of 2020-08-11 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 37.1% of deaths and 40.1% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 68.0% of deaths and 55.3% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 133   |   32812|    1686.659|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 133   |   15896|    1789.659|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 133   |   10662|     269.848|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52|   1.3%/ 52 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 133   |    9928|     342.384|   2.4%/ 29|   2.0%/ 35|   1.9%/ 37|   1.7%/ 40 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 133   |    8762|    1260.762|   0.2%/424|   0.2%/437|   0.2%/441|   0.2%/444 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 133   |    8683|     404.270|   2.2%/ 32|   2.1%/ 33|   2.0%/ 34|   2.0%/ 34 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 133   |    7873|     621.310|   0.2%/322|   0.2%/323|   0.2%/324|   0.2%/324 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 133   |    7344|     573.692|   0.2%/399|   0.2%/433|   0.2%/443|   0.2%/452 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 133   |    6534|     654.296|   0.1%/587|   0.1%/570|   0.1%/566|   0.1%/562 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 133   |    4449|    1247.778|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 133   |  165173|     501.216|   0.7%/100|   0.7%/101|   0.7%/101|   0.7%/101 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 133   |  103612|     490.094|   1.0%/ 69|   0.9%/ 77|   0.9%/ 79|   0.8%/ 82 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 133   |   53961|     426.311|   1.3%/ 53|   1.3%/ 55|   1.2%/ 55|   1.2%/ 56 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 133   |   46772|     704.020|   0.1%/654|   0.1%/775|   0.1%/814|   0.1%/860 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 133   |   46487|      34.151|   2.2%/ 31|   2.1%/ 32|   2.1%/ 33|   2.1%/ 33 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 133   |   35221|     584.687|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 133   |   30345|     452.393|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 133   |   28533|     605.785|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 133   |   22650|     704.919|   1.1%/ 65|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 133   |   19333|     231.877|   1.1%/ 62|   1.0%/ 70|   1.0%/ 72|   0.9%/ 74 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 133   |    1845|     376.294|   1.4%/ 50|   1.3%/ 55|   1.2%/ 56|   1.2%/ 57 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 133   |      27|      37.452|   1.2%/ 55|   1.5%/ 47|   1.5%/ 46|   1.6%/ 44 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 133   |    4381|     601.872|   1.5%/ 46|   1.1%/ 62|   1.0%/ 68|   0.9%/ 74 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 133   |     565|     187.125|   2.1%/ 33|   2.1%/ 32|   2.2%/ 32|   2.2%/ 32 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 133   |   10662|     269.848|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52|   1.3%/ 52 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 133   |    1878|     326.174|   0.2%/315|   0.2%/392|   0.2%/420|   0.2%/453 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 133   |    4449|    1247.778|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 133   |     603|     618.868|   0.1%/509|   0.1%/550|   0.1%/561|   0.1%/572 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 133   |    8683|     404.270|   2.2%/ 32|   2.1%/ 33|   2.0%/ 34|   2.0%/ 34 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 133   |    4316|     406.477|   1.3%/ 51|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 133   |      28|      19.939|   1.6%/ 44|   2.0%/ 35|   2.1%/ 33|   2.2%/ 31 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 133   |     259|     144.824|   2.6%/ 27|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 133   |    7873|     621.310|   0.2%/322|   0.2%/323|   0.2%/324|   0.2%/324 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 133   |    3067|     455.559|   0.3%/211|   0.3%/223|   0.3%/226|   0.3%/229 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 133   |     943|     298.969|   0.8%/ 89|   0.8%/ 87|   0.8%/ 86|   0.8%/ 86 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 133   |     394|     135.254|   0.9%/ 79|   0.8%/ 82|   0.8%/ 83|   0.8%/ 84 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 133   |     787|     176.150|   0.6%/109|   0.6%/121|   0.6%/125|   0.5%/129 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 133   |    4322|     929.775|   0.9%/ 80|   0.9%/ 77|   0.9%/ 77|   0.9%/ 77 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 133   |     126|      93.926|   0.3%/238|   0.3%/277|   0.2%/290|   0.2%/304 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 133   |    3604|     596.081|   0.3%/242|   0.3%/241|   0.3%/241|   0.3%/240 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 133   |    8762|    1260.762|   0.2%/424|   0.2%/437|   0.2%/441|   0.2%/444 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 133   |    6534|     654.296|   0.1%/587|   0.1%/570|   0.1%/566|   0.1%/562 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 133   |    1705|     302.276|   0.4%/192|   0.4%/183|   0.4%/180|   0.4%/178 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 133   |    1962|     659.207|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44|   1.6%/ 45 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 133   |    1357|     221.063|   0.7%/103|   0.6%/111|   0.6%/113|   0.6%/116 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 133   |      80|      74.484|   2.9%/ 23|   2.8%/ 25|   2.7%/ 25|   2.7%/ 26 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 133   |     351|     181.213|   0.6%/118|   0.6%/123|   0.6%/124|   0.6%/125 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 133   |     986|     320.031|   1.8%/ 39|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 133   |     423|     311.015|   0.1%/474|   0.1%/970|   0.1%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 133   |   15896|    1789.659|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 133   |     698|     333.079|   0.8%/ 90|   0.7%/ 97|   0.7%/ 99|   0.7%/101 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 133   |   32812|    1686.659|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 133   |    2256|     215.067|   1.3%/ 54|   1.3%/ 55|   1.3%/ 55|   1.2%/ 55 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 133   |     115|     150.423|   1.0%/ 69|   1.0%/ 67|   1.0%/ 66|   1.1%/ 65 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 133   |    3740|     319.957|   0.6%/109|   0.6%/120|   0.6%/123|   0.5%/127 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 133   |     625|     157.972|   1.2%/ 57|   1.1%/ 61|   1.1%/ 62|   1.1%/ 64 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 133   |     370|      87.614|   1.3%/ 51|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 133   |    7344|     573.692|   0.2%/399|   0.2%/433|   0.2%/443|   0.2%/452 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 133   |     283|      88.608|   2.3%/ 30|   2.5%/ 28|   2.5%/ 27|   2.6%/ 27 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 133   |    1017|     960.346|   0.1%/893|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 133   |    2190|     425.425|   2.1%/ 32|   1.8%/ 39|   1.7%/ 41|   1.6%/ 44 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 133   |     148|     167.190|   1.1%/ 63|   1.1%/ 61|   1.1%/ 61|   1.1%/ 60 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 133   |    1273|     186.311|   1.7%/ 41|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 133   |    9928|     342.384|   2.4%/ 29|   2.0%/ 35|   1.9%/ 37|   1.7%/ 40 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 133   |  165173|     501.216|   0.7%/100|   0.7%/101|   0.7%/101|   0.7%/101 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 133   |     354|     110.494|   1.4%/ 51|   1.2%/ 58|   1.2%/ 60|   1.1%/ 62 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 133   |      58|      93.045|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 133   |    2357|     276.165|   0.7%/ 99|   0.7%/ 94|   0.7%/ 93|   0.7%/ 92 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 133   |    1712|     224.819|   0.8%/ 90|   0.8%/ 86|   0.8%/ 85|   0.8%/ 84 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 133   |     135|      75.330|   2.2%/ 31|   2.8%/ 25|   2.9%/ 24|   3.0%/ 23 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 133   |    1014|     174.168|   0.7%/ 93|   0.7%/ 95|   0.7%/ 96|   0.7%/ 97 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 121   |      28|      49.096|   0.8%/ 86|   0.9%/ 78|   0.9%/ 76|   0.9%/ 74 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 133   |    1341|      41.609|   0.4%/169|   0.3%/272|   0.2%/316|   0.2%/372 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 133   |     211|      74.050|   2.5%/ 27|   2.3%/ 30|   2.3%/ 30|   2.2%/ 31 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 133   |    1328|      30.894|   0.8%/ 82|   0.8%/ 86|   0.8%/ 87|   0.8%/ 89 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 133   |      81|       2.598|   4.2%/ 16|   4.2%/ 16|   4.2%/ 16|   4.2%/ 16 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 133   |    4987|     110.963|   3.3%/ 21|   3.2%/ 22|   3.2%/ 22|   3.1%/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 133   |     812|     274.660|   0.8%/ 88|   0.6%/114|   0.6%/122|   0.5%/132 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 133   |     341|      13.289|   5.1%/ 14|   5.6%/ 12|   5.7%/ 12|   5.8%/ 12 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 133   |     723|      81.183|   0.1%/839|   0.1%/772|   0.1%/759|   0.1%/747 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 133   |     514|      51.103|   1.1%/ 65|   0.7%/ 97|   0.6%/110|   0.5%/128 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 133   |     166|     107.259|   1.1%/ 63|   1.0%/ 67|   1.0%/ 68|   1.0%/ 69 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 133   |    3504|      20.797|   1.1%/ 64|   1.0%/ 72|   0.9%/ 74|   0.9%/ 77 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 133   |     601|      63.894|   0.6%/113|   0.5%/143|   0.4%/154|   0.4%/167 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 133   |    9880|     857.322|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 128   |      39|       3.337|   0.3%/202|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 133   |    3883|     338.533|   2.3%/ 30|   2.1%/ 33|   2.1%/ 33|   2.0%/ 34 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 133   |     435|     131.911|   2.1%/ 32|   2.2%/ 32|   2.2%/ 32|   2.2%/ 31 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 133   |       2|       1.019|   2.0%/ 35|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 133   |  103612|     490.094|   1.0%/ 69|   0.9%/ 77|   0.9%/ 79|   0.8%/ 82 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 133   |     471|      67.723|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 133   |      54|       2.588|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 121   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 133   |     397|      14.973|   0.2%/435|   0.1%/785|   0.1%/957|   0.1%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 133   |    9045|     238.031|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  81   |      60|      10.909|   0.2%/411|   0.4%/167|   0.5%/143|   0.6%/125 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 106   |      76|       4.677|   0.1%/ ***|   0.1%/795|   0.1%/736|   0.1%/685 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 133   |   10308|     539.471|   0.7%/ 96|   0.6%/108|   0.6%/112|   0.6%/115 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 133   |    4689|       3.344|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 133   |   13850|     280.383|   2.8%/ 24|   2.7%/ 26|   2.6%/ 26|   2.6%/ 27 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 133   |     279|      55.215|   5.6%/ 12|   4.8%/ 14|   4.7%/ 15|   4.5%/ 15 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 133   |     163|      40.106|   1.0%/ 72|   0.8%/ 85|   0.8%/ 90|   0.7%/ 95 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 133   |      88|       7.851|   0.1%/ ***|   0.1%/828|   0.1%/788|   0.1%/754 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 133   |     619|     106.286|   0.1%/951|   0.1%/819|   0.1%/791|   0.1%/764 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 133   |    1340|     129.405|   1.5%/ 46|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 133   |    6006|     343.828|   0.4%/156|   0.4%/182|   0.4%/190|   0.3%/200 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 133   |    5128|      51.138|   0.5%/127|   0.4%/182|   0.3%/204|   0.3%/232 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 133   |     576|      88.746|   2.3%/ 30|   2.2%/ 32|   2.1%/ 32|   2.1%/ 33 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 112   |      93|      68.824|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 129   |     449|       4.553|   4.2%/ 16|   4.1%/ 17|   4.1%/ 17|   4.1%/ 17 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 133   |     332|      60.029|   0.1%/839|   0.1%/645|   0.1%/609|   0.1%/576 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 133   |   30345|     452.393|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 133   |      52|      23.868|   0.3%/249|   0.2%/353|   0.2%/400|   0.1%/465 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 133   |      32|      13.630|  21.1%/  3|  12.9%/  5|   6.6%/ 10|  19.0%/  3 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 130   |      17|       4.658|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 133   |    9208|     110.735|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 133   |     218|       7.191|   1.8%/ 39|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 133   |     214|      19.958|   0.4%/194|   0.4%/189|   0.4%/189|   0.4%/188 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 133   |    2313|     139.276|   1.6%/ 43|   1.4%/ 51|   1.3%/ 53|   1.2%/ 56 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 119   |      51|       4.188|   0.9%/ 81|   0.7%/101|   0.6%/108|   0.6%/116 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 108   |      29|      17.849|   0.8%/ 82|   1.2%/ 58|   1.3%/ 54|   1.4%/ 50 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 129   |     182|      15.755|   1.1%/ 62|   1.2%/ 56|   1.3%/ 54|   1.3%/ 53 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 133   |    1617|     176.565|   1.7%/ 41|   1.2%/ 58|   1.1%/ 65|   0.9%/ 74 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 133   |     602|      61.631|   0.1%/671|   0.1%/495|   0.1%/463|   0.2%/435 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 133   |   46487|      34.151|   2.2%/ 31|   2.1%/ 32|   2.1%/ 33|   2.1%/ 33 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 133   |    5938|      22.246|   1.3%/ 55|   1.1%/ 66|   1.0%/ 69|   1.0%/ 72 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 133   |   19333|     231.877|   1.1%/ 62|   1.0%/ 70|   1.0%/ 72|   0.9%/ 74 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 133   |    5604|     143.230|   1.5%/ 47|   1.3%/ 53|   1.3%/ 55|   1.2%/ 56 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 133   |    1772|     360.076|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 133   |     628|      68.377|   1.8%/ 39|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 133   |   35221|     584.687|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 133   |      14|       5.009|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 133   |    1049|       8.330|   0.4%/180|   0.5%/149|   0.5%/143|   0.5%/137 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 133   |      11|       1.035|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 133   |    1231|      65.904|   0.3%/266|   0.4%/174|   0.4%/159|   0.5%/147 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 133   |     457|       9.614|   2.4%/ 28|   2.1%/ 32|   2.0%/ 34|   2.0%/ 35 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 133   |     353|     196.603|   3.7%/ 19|   3.5%/ 20|   3.4%/ 20|   3.4%/ 21 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 130   |     487|     110.181|   0.7%/ 96|   0.7%/100|   0.7%/102|   0.7%/103 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 131   |    1504|     230.222|   0.9%/ 80|   0.1%/523|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 131   |      32|      16.902|   0.1%/505|   0.1%/548|   0.1%/569|   0.1%/596 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 133   |      83|      12.114|   3.4%/ 20|   3.6%/ 19|   3.7%/ 19|   3.8%/ 18 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 130   |      81|      18.135|   0.7%/106|   0.7%/104|   0.7%/104|   0.7%/105 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 132   |     129|      18.805|   4.7%/ 15|   4.9%/ 14|   5.0%/ 14|   5.1%/ 14 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 133   |      81|      28.985|   0.1%/819|   0.1%/719|   0.1%/693|   0.1%/668 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  87   |     157|       5.971|   3.8%/ 18|   3.3%/ 21|   3.1%/ 22|   3.0%/ 23 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 133   |     126|       3.832|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 133   |     125|       6.185|   0.1%/730|   0.1%/944|   0.1%/ ***|   0.1%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 133   |     158|      38.685|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 133   |   53961|     426.311|   1.3%/ 53|   1.3%/ 55|   1.2%/ 55|   1.2%/ 56 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 133   |     865|     322.502|   0.9%/ 76|   0.9%/ 81|   0.8%/ 82|   0.8%/ 84 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 133   |     521|      14.528|   3.3%/ 21|   3.7%/ 19|   3.8%/ 18|   3.9%/ 18 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  79   |      17|       0.573|   2.6%/ 26|   2.6%/ 26|   2.6%/ 27|   2.5%/ 28 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  33   |      20|       8.022|   5.3%/ 13|   7.9%/  9|   6.8%/ 10|   5.6%/ 12 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  88   |      80|       2.680|   3.9%/ 18|   4.6%/ 15|   4.7%/ 14|   4.9%/ 14 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 133   |    6179|     353.959|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 133   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 133   |     128|      19.737|   0.8%/ 91|   0.6%/109|   0.6%/115|   0.6%/122 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 133   |      69|       3.093|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 133   |     963|       4.672|   0.7%/ 96|   0.6%/108|   0.6%/111|   0.6%/115 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 133   |     540|     260.017|   0.9%/ 81|   0.7%/ 99|   0.7%/104|   0.6%/111 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 133   |     256|      47.718|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 133   |     537|     115.115|   1.9%/ 35|   1.8%/ 39|   1.7%/ 40|   1.7%/ 41 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 133   |    6149|      28.037|   0.3%/242|   0.2%/350|   0.2%/392|   0.2%/445 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 133   |    1720|     407.724|   1.6%/ 42|   1.4%/ 50|   1.3%/ 52|   1.3%/ 54 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  16   |       3|       0.336|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 133   |      81|      11.355|   4.8%/ 14|   5.2%/ 13|   5.3%/ 13|   5.5%/ 13 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 133   |   22650|     704.919|   1.1%/ 65|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 133   |    2297|      21.167|   1.2%/ 55|   1.4%/ 50|   1.4%/ 48|   1.5%/ 47 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 133   |    1817|      47.337|   0.5%/126|   0.6%/118|   0.6%/116|   0.6%/115 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 133   |    1761|     171.398|   0.2%/417|   0.2%/450|   0.2%/458|   0.1%/466 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 133   |     187|      68.139|   0.8%/ 86|   0.8%/ 84|   0.8%/ 83|   0.8%/ 83 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 133   |    2746|     141.517|   1.5%/ 46|   1.6%/ 42|   1.7%/ 42|   1.7%/ 41 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 133   |   15223|     103.735|   0.8%/ 86|   0.7%/ 96|   0.7%/ 99|   0.7%/102 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  74   |       5|       0.404|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 133   |    3235|      94.554|   1.1%/ 64|   1.0%/ 67|   1.0%/ 68|   1.0%/ 68 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 133   |     240|      14.809|   1.4%/ 48|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 133   |     664|      95.327|   1.2%/ 55|   1.1%/ 66|   1.0%/ 69|   1.0%/ 72 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 111   |      68|       8.664|   0.3%/256|   0.3%/205|   0.4%/194|   0.4%/184 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 133   |      27|       4.734|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 133   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 133   |     128|      61.182|   0.7%/105|   0.8%/ 91|   0.8%/ 88|   0.8%/ 86 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 126   |      93|       5.852|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 133   |   11185|     190.308|   3.0%/ 23|   2.8%/ 25|   2.7%/ 25|   2.7%/ 26 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 133   |   28533|     605.785|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 133   |      11|       0.505|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 133   |     789|      18.600|   0.6%/125|   0.5%/134|   0.5%/136|   0.5%/138 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 133   |    5788|     559.898|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 133   |    1988|     231.098|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 133   |      55|       3.171|   2.9%/ 23|   2.7%/ 25|   2.7%/ 25|   2.0%/ 35 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 133   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 133   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 133   |      24|       3.187|   2.7%/ 26|   3.1%/ 22|   3.3%/ 21|   3.4%/ 20 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 133   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 133   |      51|       4.378|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 133   |    5881|      70.718|   0.3%/244|   0.3%/253|   0.3%/255|   0.3%/257 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 133   |  165173|     501.216|   0.7%/100|   0.7%/101|   0.7%/101|   0.7%/101 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  19   |       9|       0.230|   5.9%/ 12|  11.0%/  6|  13.7%/  5|  14.8%/  5 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 133   |    1960|      46.804|   1.3%/ 54|   1.4%/ 51|   1.4%/ 50|   1.4%/ 50 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 133   |     358|      36.245|   0.2%/294|   0.2%/306|   0.2%/309|   0.2%/312 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 133   |   46772|     704.020|   0.1%/654|   0.1%/775|   0.1%/814|   0.1%/860 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 133   |      38|      10.703|   0.4%/171|   0.3%/246|   0.2%/278|   0.2%/319 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 133   |     211|       6.182|   3.6%/ 19|   3.3%/ 21|   3.3%/ 21|   3.2%/ 22 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 133   |     236|       7.321|   3.3%/ 21|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  12   |      16|       0.166|  14.5%/  5|   9.1%/  7|  14.5%/  5|  17.0%/  4 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 132   |     230|      12.836|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 133   |     123|       8.136|   5.0%/ 14|   7.4%/  9|   0.6%/107|   0.6%/107 |

