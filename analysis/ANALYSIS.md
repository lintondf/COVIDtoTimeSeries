# State and Country COVID-19 Analysis #
## Updated: at 2020-08-07 for data as of 2020-08-06 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 36.9% of deaths and 40.0% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 68.5% of deaths and 55.6% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 128   |   32775|    1684.763|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 128   |   15880|    1787.861|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 128   |    9936|     251.477|   1.5%/ 47|   1.5%/ 46|   1.5%/ 45|   1.5%/ 45 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 128   |    8690|    1250.472|   0.2%/421|   0.2%/437|   0.2%/442|   0.2%/446 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 128   |    8141|     280.777|   3.3%/ 21|   3.2%/ 21|   3.2%/ 22|   3.2%/ 22 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 128   |    7782|     614.101|   0.2%/323|   0.2%/319|   0.2%/317|   0.2%/316 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 128   |    7776|     362.057|   2.5%/ 28|   2.5%/ 27|   2.5%/ 27|   2.5%/ 27 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 128   |    7283|     568.924|   0.2%/372|   0.2%/407|   0.2%/417|   0.2%/428 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 128   |    6488|     649.701|   0.1%/615|   0.1%/597|   0.1%/592|   0.1%/586 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 128   |    4444|    1246.539|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 128   |  159214|     483.134|   0.7%/ 96|   0.8%/ 92|   0.8%/ 91|   0.8%/ 90 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 128   |   98848|     467.561|   1.1%/ 60|   1.1%/ 64|   1.1%/ 66|   1.0%/ 67 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 128   |   50623|     399.938|   1.3%/ 51|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 128   |   46533|     700.426|   0.1%/528|   0.1%/558|   0.1%/566|   0.1%/574 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 128   |   41858|      30.751|   2.3%/ 30|   2.2%/ 31|   2.2%/ 31|   2.2%/ 32 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 128   |   35191|     584.201|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 128   |   30309|     451.859|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 128   |   28480|     604.660|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 128   |   21307|     663.111|   1.1%/ 62|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 128   |   18165|     217.865|   1.3%/ 53|   1.2%/ 56|   1.2%/ 57|   1.2%/ 58 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 128   |    1735|     353.887|   1.5%/ 46|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 128   |      26|      35.193|   2.7%/ 25|   3.3%/ 21|   3.4%/ 20|   3.6%/ 19 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 128   |    4129|     567.268|   1.9%/ 36|   1.6%/ 44|   1.5%/ 47|   1.4%/ 50 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 128   |     506|     167.756|   2.1%/ 33|   2.3%/ 30|   2.3%/ 30|   2.4%/ 29 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 128   |    9936|     251.477|   1.5%/ 47|   1.5%/ 46|   1.5%/ 45|   1.5%/ 45 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 128   |    1862|     323.315|   0.3%/242|   0.3%/254|   0.3%/258|   0.3%/263 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 128   |    4444|    1246.539|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 128   |     602|     617.977|   0.1%/480|   0.1%/517|   0.1%/528|   0.1%/540 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 128   |    7776|     362.057|   2.5%/ 28|   2.5%/ 27|   2.5%/ 27|   2.5%/ 27 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 128   |    4020|     378.612|   1.3%/ 53|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 128   |      28|      19.461|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 128   |     223|     124.888|   3.0%/ 23|   3.3%/ 21|   3.4%/ 20|   3.4%/ 20 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 128   |    7782|     614.101|   0.2%/323|   0.2%/319|   0.2%/317|   0.2%/316 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 128   |    3019|     448.487|   0.4%/195|   0.3%/198|   0.3%/200|   0.3%/201 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 128   |     906|     287.034|   0.7%/ 93|   0.8%/ 91|   0.8%/ 90|   0.8%/ 90 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 128   |     377|     129.320|   1.0%/ 69|   1.0%/ 66|   1.1%/ 66|   1.1%/ 65 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 128   |     764|     171.108|   0.7%/ 98|   0.6%/107|   0.6%/109|   0.6%/112 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 128   |    4128|     887.879|   0.8%/ 85|   0.9%/ 78|   0.9%/ 77|   0.9%/ 76 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 128   |     125|      92.821|   0.3%/210|   0.3%/242|   0.3%/252|   0.3%/263 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 128   |    3551|     587.339|   0.3%/253|   0.3%/253|   0.3%/253|   0.3%/253 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 128   |    8690|    1250.472|   0.2%/421|   0.2%/437|   0.2%/442|   0.2%/446 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 128   |    6488|     649.701|   0.1%/615|   0.1%/597|   0.1%/592|   0.1%/586 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 128   |    1673|     296.659|   0.3%/209|   0.3%/206|   0.3%/205|   0.3%/204 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 128   |    1806|     606.960|   1.7%/ 40|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 128   |    1313|     213.981|   0.7%/ 97|   0.7%/100|   0.7%/101|   0.7%/102 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 128   |      69|      64.237|   2.8%/ 24|   2.7%/ 26|   2.6%/ 26|   2.6%/ 27 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 128   |     340|     175.957|   0.6%/116|   0.6%/126|   0.5%/129|   0.5%/131 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 128   |     898|     291.469|   1.8%/ 39|   1.8%/ 38|   1.9%/ 37|   1.9%/ 37 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 128   |     421|     309.799|   0.3%/264|   0.2%/300|   0.2%/312|   0.2%/326 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 128   |   15880|    1787.861|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 128   |     674|     321.451|   0.8%/ 83|   0.8%/ 86|   0.8%/ 87|   0.8%/ 88 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 128   |   32775|    1684.763|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 128   |    2110|     201.175|   1.4%/ 50|   1.4%/ 48|   1.4%/ 48|   1.5%/ 48 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 128   |     109|     143.025|   0.9%/ 75|   0.9%/ 76|   0.9%/ 77|   0.9%/ 77 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 128   |    3624|     309.990|   0.8%/ 92|   0.8%/ 89|   0.8%/ 88|   0.8%/ 88 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 128   |     584|     147.657|   1.5%/ 45|   1.7%/ 41|   1.7%/ 40|   1.7%/ 40 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 128   |     345|      81.894|   1.4%/ 50|   1.3%/ 53|   1.3%/ 54|   1.3%/ 54 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 128   |    7283|     568.924|   0.2%/372|   0.2%/407|   0.2%/417|   0.2%/428 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 128   |     244|      76.273|   2.0%/ 35|   2.2%/ 31|   2.3%/ 31|   2.3%/ 30 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 128   |    1014|     957.594|   0.1%/658|   0.1%/818|   0.1%/869|   0.1%/925 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 128   |    1998|     388.099|   2.7%/ 26|   2.5%/ 28|   2.5%/ 28|   2.4%/ 29 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 128   |     139|     156.962|   1.0%/ 67|   1.1%/ 64|   1.1%/ 63|   1.1%/ 62 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 128   |    1170|     171.220|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39|   1.7%/ 39 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 128   |    8141|     280.777|   3.3%/ 21|   3.2%/ 21|   3.2%/ 22|   3.2%/ 22 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 128   |  159214|     483.134|   0.7%/ 96|   0.8%/ 92|   0.8%/ 91|   0.8%/ 90 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 128   |     334|     104.063|   1.6%/ 42|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 128   |      57|      91.578|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 128   |    2262|     264.960|   0.8%/ 91|   0.9%/ 77|   0.9%/ 74|   1.0%/ 71 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 128   |    1637|     215.023|   0.7%/ 96|   0.8%/ 89|   0.8%/ 87|   0.8%/ 86 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 128   |     122|      68.185|   1.5%/ 46|   1.8%/ 38|   1.9%/ 36|   2.0%/ 34 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 128   |     974|     167.356|   0.8%/ 84|   0.9%/ 78|   0.9%/ 76|   0.9%/ 75 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 116   |      27|      46.939|   0.6%/109|   0.6%/117|   0.6%/119|   0.6%/120 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 128   |    1332|      41.328|   0.5%/148|   0.1%/642|   0.0%/ ***|   0.0%/ -- |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 128   |     187|      65.819|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 128   |    1276|      29.678|   0.9%/ 77|   0.9%/ 79|   0.9%/ 80|   0.9%/ 80 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 128   |      65|       2.091|   3.4%/ 20|   3.0%/ 23|   4.1%/ 17|   3.3%/ 21 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 128   |    4261|      94.820|   3.4%/ 20|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 128   |     791|     267.392|   1.0%/ 71|   0.7%/ 95|   0.7%/103|   0.6%/113 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 128   |     258|      10.039|   4.6%/ 15|   5.2%/ 13|   5.4%/ 13|   5.6%/ 12 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 128   |     720|      80.822|   0.1%/991|   0.1%/919|   0.1%/904|   0.1%/890 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 128   |     496|      49.313|   1.5%/ 45|   1.2%/ 56|   1.2%/ 59|   1.1%/ 63 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 128   |     157|     101.984|   1.1%/ 63|   0.9%/ 77|   0.8%/ 82|   0.8%/ 87 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 128   |    3346|      19.864|   1.2%/ 57|   1.1%/ 64|   1.0%/ 66|   1.0%/ 68 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 128   |     587|      62.338|   0.8%/ 86|   0.7%/ 96|   0.7%/ 98|   0.7%/102 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 128   |    9860|     855.571|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 123   |      39|       3.302|   0.4%/161|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 128   |    3484|     303.745|   2.7%/ 26|   2.7%/ 26|   2.7%/ 26|   2.7%/ 26 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 128   |     384|     116.436|   2.3%/ 30|   2.4%/ 28|   2.5%/ 28|   2.5%/ 27 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 128   |       1|       0.428|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 128   |   98848|     467.561|   1.1%/ 60|   1.1%/ 64|   1.1%/ 66|   1.0%/ 67 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 128   |     426|      61.334|   2.1%/ 33|   2.3%/ 31|   2.3%/ 30|   2.3%/ 29 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 128   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 116   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 128   |     397|      14.943|   0.2%/398|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 128   |    9018|     237.335|   0.1%/921|   0.1%/983|   0.1%/999|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  76   |      59|      10.753|   0.2%/413|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 101   |      75|       4.626|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 128   |   10118|     529.512|   0.8%/ 86|   0.7%/ 95|   0.7%/ 97|   0.7%/100 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 128   |    4674|       3.333|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 128   |   12110|     245.162|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22|   3.1%/ 23 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 128   |     222|      43.828|   6.6%/ 10|   5.8%/ 12|   5.5%/ 12|   5.3%/ 13 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 128   |     156|      38.344|   1.4%/ 51|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 128   |      87|       7.803|   0.1%/710|   0.1%/481|   0.2%/442|   0.2%/407 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 128   |     617|     105.890|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 128   |    1245|     120.151|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 128   |    5886|     336.930|   0.6%/123|   0.5%/131|   0.5%/132|   0.5%/134 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 128   |    5044|      50.301|   0.7%/ 95|   0.5%/134|   0.5%/149|   0.4%/167 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 128   |     519|      80.090|   2.3%/ 29|   2.1%/ 33|   2.0%/ 34|   2.0%/ 35 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 107   |      86|      63.075|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 124   |     364|       3.692|   4.7%/ 14|   5.1%/ 14|   5.1%/ 13|   5.2%/ 13 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 128   |     330|      59.721|   0.1%/ ***|   0.1%/727|   0.1%/674|   0.1%/627 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 128   |   30309|     451.859|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 128   |      51|      23.593|   0.5%/130|   0.6%/118|   0.6%/116|   0.6%/114 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 128   |      14|       6.012|   9.5%/  7|  11.1%/  6|  11.6%/  6|  12.0%/  6 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 125   |      17|       4.653|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 128   |    9174|     110.335|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 128   |     198|       6.538|   1.7%/ 40|   1.9%/ 37|   1.9%/ 37|   1.9%/ 36 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 128   |     210|      19.627|   0.4%/182|   0.4%/165|   0.4%/161|   0.4%/158 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 128   |    2154|     129.701|   1.9%/ 37|   1.6%/ 42|   1.6%/ 44|   1.5%/ 45 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 114   |      49|       4.020|   1.2%/ 59|   1.2%/ 59|   1.2%/ 59|   1.2%/ 59 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 103   |      27|      16.821|   0.3%/232|   0.4%/162|   0.5%/150|   0.5%/140 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 124   |     171|      14.733|   0.8%/ 88|   0.8%/ 92|   0.7%/ 93|   0.7%/ 93 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 128   |    1518|     165.769|   2.4%/ 29|   2.1%/ 32|   2.1%/ 33|   2.0%/ 35 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 128   |     598|      61.190|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 128   |   41858|      30.751|   2.3%/ 30|   2.2%/ 31|   2.2%/ 31|   2.2%/ 32 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 128   |    5641|      21.134|   1.5%/ 47|   1.3%/ 55|   1.2%/ 57|   1.2%/ 60 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 128   |   18165|     217.865|   1.3%/ 53|   1.2%/ 56|   1.2%/ 57|   1.2%/ 58 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 128   |    5267|     134.606|   1.6%/ 42|   1.4%/ 50|   1.3%/ 53|   1.2%/ 55 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 128   |    1767|     359.136|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 128   |     577|      62.801|   2.0%/ 35|   2.0%/ 34|   2.0%/ 34|   2.1%/ 34 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 128   |   35191|     584.201|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 128   |      10|       3.667|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 128   |    1024|       8.129|   0.3%/243|   0.4%/192|   0.4%/182|   0.4%/173 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 128   |      11|       1.046|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 128   |    1062|      56.856|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 128   |     407|       8.556|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 128   |     292|     162.422|   4.7%/ 15|   5.0%/ 14|   5.1%/ 13|   5.2%/ 13 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 125   |     471|     106.588|   0.8%/ 87|   0.8%/ 86|   0.8%/ 86|   0.8%/ 86 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 126   |    1706|     261.155|   1.6%/ 42|   0.7%/103|   0.4%/162|   0.2%/373 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 126   |      32|      16.774|   0.2%/318|   0.3%/267|   0.3%/255|   0.3%/244 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 128   |      70|      10.189|   2.9%/ 24|   3.2%/ 22|   3.3%/ 21|   3.3%/ 21 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 125   |      81|      18.135|   0.7%/ 93|   0.8%/ 84|   0.9%/ 81|   0.9%/ 79 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 127   |     100|      14.614|   4.4%/ 15|   4.7%/ 15|   4.7%/ 14|   4.8%/ 14 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 128   |      80|      28.812|   0.1%/825|   0.1%/722|   0.1%/694|   0.1%/665 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  82   |     135|       5.131|   4.5%/ 15|   3.9%/ 18|   3.7%/ 19|   3.5%/ 19 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 128   |     125|       3.827|   0.1%/665|   0.1%/725|   0.1%/746|   0.1%/770 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 128   |     125|       6.157|   0.1%/847|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 128   |     158|      38.850|   0.1%/789|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 128   |   50623|     399.938|   1.3%/ 51|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 128   |     827|     308.407|   1.0%/ 66|   1.1%/ 65|   1.1%/ 65|   1.1%/ 64 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 128   |     386|      10.763|   3.1%/ 22|   3.7%/ 19|   3.8%/ 18|   4.0%/ 17 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  74   |      15|       0.498|   2.6%/ 27|   4.9%/ 14|   5.5%/ 12|   6.2%/ 11 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  28   |      14|       5.752|   6.7%/ 10|   4.3%/ 16|   5.1%/ 13|   6.0%/ 11 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  83   |      63|       2.104|   2.7%/ 25|   2.8%/ 25|   2.8%/ 25|   2.8%/ 25 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 128   |    6172|     353.534|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 128   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 128   |     124|      19.127|   1.1%/ 61|   1.2%/ 60|   1.2%/ 60|   1.2%/ 59 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 128   |      69|       3.096|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 128   |     932|       4.519|   0.8%/ 82|   0.8%/ 90|   0.8%/ 92|   0.7%/ 94 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 128   |     521|     250.906|   1.1%/ 64|   1.0%/ 72|   0.9%/ 74|   0.9%/ 77 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 128   |     256|      47.673|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 128   |     483|     103.614|   2.0%/ 34|   1.7%/ 40|   1.6%/ 42|   1.6%/ 44 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 128   |    6098|      27.801|   0.4%/193|   0.2%/321|   0.2%/382|   0.1%/472 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 128   |    1609|     381.440|   1.9%/ 36|   1.7%/ 41|   1.6%/ 42|   1.6%/ 44 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  11   |       3|       0.336|  26.0%/  2|   0.0%/ --|   0.0%/ --|  14.5%/  5 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 128   |      63|       8.870|   4.1%/ 17|   4.2%/ 16|   4.2%/ 16|   4.3%/ 16 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 128   |   21307|     663.111|   1.1%/ 62|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 128   |    2170|      19.995|   1.0%/ 69|   1.0%/ 66|   1.1%/ 65|   1.1%/ 65 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 128   |    1761|      45.879|   0.5%/145|   0.5%/138|   0.5%/137|   0.5%/135 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 128   |    1750|     170.263|   0.2%/456|   0.1%/617|   0.1%/678|   0.1%/753 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 128   |     180|      65.644|   0.7%/100|   0.6%/114|   0.6%/118|   0.6%/122 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 128   |    2525|     130.127|   1.4%/ 51|   1.5%/ 47|   1.5%/ 46|   1.5%/ 45 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 128   |   14686|     100.079|   0.9%/ 77|   0.8%/ 86|   0.8%/ 88|   0.8%/ 91 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  69   |       5|       0.404|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 128   |    3078|      89.942|   1.1%/ 64|   0.9%/ 73|   0.9%/ 76|   0.9%/ 79 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 128   |     225|      13.878|   1.5%/ 46|   1.4%/ 50|   1.3%/ 52|   1.3%/ 54 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 128   |     632|      90.745|   1.5%/ 47|   1.2%/ 56|   1.2%/ 58|   1.1%/ 61 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 106   |      67|       8.519|   0.1%/572|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 128   |      27|       4.743|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 128   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 128   |     123|      58.733|   0.6%/112|   0.8%/ 89|   0.8%/ 84|   0.9%/ 80 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 121   |      93|       5.852|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 128   |    9723|     165.425|   3.3%/ 21|   3.2%/ 21|   3.2%/ 22|   3.2%/ 22 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 128   |   28480|     604.660|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 128   |      11|       0.505|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 128   |     769|      18.123|   0.6%/113|   0.6%/120|   0.6%/121|   0.6%/123 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 128   |    5782|     559.240|   0.1%/604|   0.1%/892|   0.1%/ ***|   0.1%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 128   |    1984|     230.648|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 128   |      52|       2.985|   2.4%/ 28|   2.3%/ 30|   2.9%/ 23|   1.4%/ 48 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 128   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 128   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 128   |      21|       2.722|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 128   |       8|       5.865|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 128   |      51|       4.337|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 128   |    5800|      69.751|   0.3%/229|   0.3%/234|   0.3%/236|   0.3%/237 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 128   |  159214|     483.134|   0.7%/ 96|   0.8%/ 92|   0.8%/ 91|   0.8%/ 90 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  14   |       5|       0.124|  14.5%/  5|   7.7%/  9|   7.7%/  9|   0.0%/ -- |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 128   |    1829|      43.683|   1.1%/ 62|   1.1%/ 60|   1.2%/ 60|   1.2%/ 60 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 128   |     354|      35.816|   0.2%/305|   0.2%/331|   0.2%/338|   0.2%/346 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 128   |   46533|     700.426|   0.1%/528|   0.1%/558|   0.1%/566|   0.1%/574 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 128   |      37|      10.520|   0.7%/ 94|   0.7%/ 96|   0.7%/ 96|   0.7%/ 96 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 128   |     179|       5.257|   4.0%/ 17|   3.7%/ 19|   3.6%/ 19|   3.6%/ 19 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 128   |     200|       6.196|   3.2%/ 21|   3.2%/ 21|   3.2%/ 21|   3.2%/ 21 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 127   |     188|      10.536|   3.3%/ 21|   1.6%/ 43|   1.2%/ 59|   0.7%/ 94 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 128   |      87|       5.745|   7.8%/  9|   8.3%/  8|   8.5%/  8|   8.6%/  8 |

