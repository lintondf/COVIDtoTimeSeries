# State and Country COVID-19 Analysis #
## Updated: at 2020-08-13 for data as of 2020-08-12 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 37.2% of deaths and 40.2% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 134   |   32817|    1686.965|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 134   |   15899|    1789.979|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 134   |   10803|     273.422|   1.3%/ 51|   1.3%/ 53|   1.3%/ 53|   1.3%/ 54 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 134   |   10199|     351.739|   2.2%/ 31|   1.7%/ 40|   1.6%/ 43|   1.5%/ 46 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 134   |    8866|     412.796|   2.2%/ 32|   2.1%/ 33|   2.1%/ 34|   2.0%/ 34 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 134   |    8772|    1262.264|   0.2%/451|   0.1%/483|   0.1%/492|   0.1%/501 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 134   |    7889|     622.569|   0.2%/332|   0.2%/338|   0.2%/340|   0.2%/342 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 134   |    7361|     574.993|   0.2%/374|   0.2%/385|   0.2%/387|   0.2%/389 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 134   |    6542|     655.038|   0.1%/593|   0.1%/581|   0.1%/579|   0.1%/577 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 134   |    4387|     413.174|   1.4%/ 49|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 134   |  166308|     504.660|   0.7%/102|   0.7%/103|   0.7%/104|   0.7%/104 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 134   |  104774|     495.590|   1.0%/ 67|   1.0%/ 72|   0.9%/ 74|   0.9%/ 75 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 134   |   54666|     431.876|   1.3%/ 52|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 134   |   47423|      34.839|   2.2%/ 32|   2.1%/ 33|   2.1%/ 33|   2.0%/ 34 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 134   |   46820|     704.742|   0.1%/671|   0.1%/797|   0.1%/838|   0.1%/886 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 134   |   35227|     584.790|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 134   |   30357|     452.570|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 134   |   28547|     606.086|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 134   |   22821|     710.244|   1.0%/ 66|   1.0%/ 70|   1.0%/ 71|   1.0%/ 72 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 134   |   19561|     234.603|   1.1%/ 63|   1.0%/ 71|   0.9%/ 73|   0.9%/ 75 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 134   |    1872|     381.844|   1.4%/ 48|   1.4%/ 51|   1.4%/ 51|   1.3%/ 52 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 134   |      28|      37.844|   1.2%/ 55|   1.4%/ 49|   1.5%/ 48|   1.5%/ 46 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 134   |    4427|     608.155|   1.5%/ 47|   1.1%/ 61|   1.0%/ 66|   1.0%/ 72 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 134   |     576|     190.853|   2.0%/ 34|   2.1%/ 33|   2.1%/ 33|   2.1%/ 33 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 134   |   10803|     273.422|   1.3%/ 51|   1.3%/ 53|   1.3%/ 53|   1.3%/ 54 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 134   |    1881|     326.718|   0.2%/311|   0.2%/377|   0.2%/399|   0.2%/425 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 134   |    4450|    1248.204|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 134   |     602|     618.082|   0.1%/542|   0.1%/606|   0.1%/624|   0.1%/644 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 134   |    8866|     412.796|   2.2%/ 32|   2.1%/ 33|   2.1%/ 34|   2.0%/ 34 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 134   |    4387|     413.174|   1.4%/ 49|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 134   |      28|      19.970|   1.7%/ 41|   2.2%/ 31|   2.3%/ 29|   2.5%/ 28 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 134   |     267|     149.308|   2.4%/ 28|   2.3%/ 30|   2.2%/ 31|   2.2%/ 32 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 134   |    7889|     622.569|   0.2%/332|   0.2%/338|   0.2%/340|   0.2%/342 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 134   |    3079|     457.285|   0.3%/203|   0.3%/209|   0.3%/210|   0.3%/211 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 134   |     951|     301.454|   0.8%/ 89|   0.8%/ 87|   0.8%/ 86|   0.8%/ 86 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 134   |     398|     136.548|   0.9%/ 75|   0.9%/ 75|   0.9%/ 76|   0.9%/ 76 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 134   |     792|     177.220|   0.6%/108|   0.6%/119|   0.6%/122|   0.6%/125 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 134   |    4360|     937.841|   0.8%/ 81|   0.9%/ 80|   0.9%/ 80|   0.9%/ 80 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 134   |     127|      94.131|   0.3%/243|   0.2%/284|   0.2%/297|   0.2%/311 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 134   |    3614|     597.742|   0.3%/245|   0.3%/246|   0.3%/246|   0.3%/247 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 134   |    8772|    1262.264|   0.2%/451|   0.1%/483|   0.1%/492|   0.1%/501 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 134   |    6542|     655.038|   0.1%/593|   0.1%/581|   0.1%/579|   0.1%/577 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 134   |    1713|     303.731|   0.4%/184|   0.4%/172|   0.4%/169|   0.4%/167 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 134   |    1994|     670.064|   1.6%/ 44|   1.6%/ 44|   1.6%/ 45|   1.5%/ 45 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 134   |    1364|     222.241|   0.6%/107|   0.6%/117|   0.6%/121|   0.6%/124 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 134   |      82|      76.445|   2.8%/ 25|   2.5%/ 27|   2.5%/ 28|   2.4%/ 28 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 134   |     353|     182.561|   0.6%/110|   0.6%/109|   0.6%/108|   0.6%/108 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 134   |    1002|     325.415|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 134   |     423|     311.082|   0.1%/527|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 134   |   15899|    1789.979|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 134   |     702|     334.973|   0.7%/ 94|   0.7%/104|   0.6%/107|   0.6%/110 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 134   |   32817|    1686.965|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 134   |    2285|     217.885|   1.3%/ 54|   1.3%/ 55|   1.3%/ 55|   1.3%/ 55 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 134   |     116|     152.682|   1.1%/ 62|   1.2%/ 57|   1.2%/ 56|   1.3%/ 54 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 134   |    3760|     321.694|   0.6%/111|   0.6%/123|   0.5%/127|   0.5%/131 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 134   |     633|     159.845|   1.2%/ 57|   1.1%/ 60|   1.1%/ 62|   1.1%/ 63 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 134   |     375|      88.891|   1.4%/ 50|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 134   |    7361|     574.993|   0.2%/374|   0.2%/385|   0.2%/387|   0.2%/389 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 134   |     291|      91.136|   2.1%/ 32|   2.3%/ 30|   2.3%/ 30|   2.3%/ 29 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 134   |    1018|     961.066|   0.1%/855|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 134   |    2220|     431.199|   2.1%/ 33|   1.7%/ 41|   1.6%/ 43|   1.5%/ 46 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 134   |     149|     168.658|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70|   1.0%/ 70 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 134   |    1294|     189.339|   1.7%/ 41|   1.6%/ 43|   1.6%/ 43|   1.6%/ 44 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 134   |   10199|     351.739|   2.2%/ 31|   1.7%/ 40|   1.6%/ 43|   1.5%/ 46 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 134   |  166308|     504.660|   0.7%/102|   0.7%/103|   0.7%/104|   0.7%/104 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 134   |     358|     111.621|   1.4%/ 51|   1.2%/ 57|   1.2%/ 59|   1.1%/ 61 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 134   |      58|      93.218|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 134   |    2372|     277.912|   0.7%/105|   0.7%/103|   0.7%/103|   0.7%/103 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 134   |    1726|     226.604|   0.8%/ 91|   0.8%/ 88|   0.8%/ 87|   0.8%/ 87 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 134   |     138|      77.079|   2.4%/ 29|   2.9%/ 24|   3.1%/ 23|   3.2%/ 22 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 134   |    1020|     175.239|   0.7%/ 98|   0.7%/104|   0.7%/106|   0.6%/108 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 122   |      29|      49.612|   0.9%/ 81|   1.0%/ 72|   1.0%/ 70|   1.0%/ 68 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 134   |    1347|      41.784|   0.5%/150|   0.4%/188|   0.3%/198|   0.3%/209 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 134   |     215|      75.522|   2.4%/ 29|   2.2%/ 32|   2.1%/ 33|   2.1%/ 34 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 134   |    1339|      31.130|   0.8%/ 83|   0.8%/ 87|   0.8%/ 89|   0.8%/ 90 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 134   |      84|       2.691|   4.2%/ 16|   4.2%/ 16|   4.2%/ 16|   4.2%/ 16 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 134   |    5159|     114.809|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 134   |     816|     275.995|   0.8%/ 91|   0.6%/116|   0.6%/124|   0.5%/133 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 134   |     359|      13.983|   5.1%/ 14|   5.5%/ 12|   5.6%/ 12|   5.7%/ 12 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 134   |     723|      81.267|   0.1%/782|   0.1%/711|   0.1%/696|   0.1%/682 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 134   |     516|      51.282|   1.0%/ 71|   0.6%/111|   0.5%/129|   0.4%/155 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 134   |     167|     108.246|   1.1%/ 64|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 134   |    3536|      20.989|   1.1%/ 64|   1.0%/ 72|   0.9%/ 74|   0.9%/ 76 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 134   |     603|      64.127|   0.6%/118|   0.5%/152|   0.4%/165|   0.4%/179 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 134   |    9886|     857.795|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 129   |      39|       3.334|   0.3%/247|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 134   |    3953|     344.612|   2.2%/ 31|   2.0%/ 34|   2.0%/ 35|   1.9%/ 36 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 134   |     448|     135.861|   2.2%/ 32|   2.2%/ 31|   2.2%/ 31|   2.2%/ 31 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 134   |       2|       1.011|   1.6%/ 44|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 134   |  104774|     495.590|   1.0%/ 67|   1.0%/ 72|   0.9%/ 74|   0.9%/ 75 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 134   |     481|      69.131|   2.0%/ 35|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 134   |      54|       2.591|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 122   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 134   |     398|      15.007|   0.2%/372|   0.1%/481|   0.1%/510|   0.1%/539 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 134   |    9051|     238.198|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  82   |      60|      10.983|   0.2%/315|   0.5%/143|   0.6%/124|   0.6%/109 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 107   |      76|       4.682|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 134   |   10342|     541.257|   0.7%/101|   0.6%/116|   0.6%/121|   0.6%/126 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 134   |    4691|       3.345|   0.1%/ ***|   0.1%/965|   0.1%/932|   0.1%/902 |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 134   |   14189|     287.258|   2.8%/ 25|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 134   |     290|      57.284|   5.3%/ 13|   4.6%/ 15|   4.4%/ 16|   4.2%/ 16 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 134   |     164|      40.339|   0.9%/ 77|   0.7%/ 95|   0.7%/102|   0.6%/109 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 134   |      88|       7.857|   0.1%/ ***|   0.1%/954|   0.1%/919|   0.1%/890 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 134   |     620|     106.409|   0.1%/789|   0.1%/652|   0.1%/624|   0.1%/597 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 134   |    1362|     131.457|   1.5%/ 46|   1.5%/ 45|   1.5%/ 45|   1.6%/ 44 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 134   |    6026|     344.981|   0.4%/161|   0.4%/189|   0.3%/199|   0.3%/209 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 134   |    5143|      51.294|   0.5%/131|   0.4%/183|   0.3%/203|   0.3%/227 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 134   |     586|      90.405|   2.2%/ 31|   2.1%/ 33|   2.1%/ 34|   2.0%/ 34 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 113   |      94|      68.937|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 130   |     468|       4.747|   4.2%/ 16|   4.1%/ 17|   4.1%/ 17|   4.1%/ 17 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 134   |     332|      60.105|   0.1%/715|   0.1%/549|   0.1%/518|   0.1%/489 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 134   |   30357|     452.570|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 134   |      52|      23.874|   0.2%/290|   0.1%/496|   0.1%/616|   0.1%/819 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 134   |      33|      14.056|  21.1%/  3|   6.6%/ 10|  19.0%/  3|  12.8%/  5 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 131   |      17|       4.652|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 134   |    9213|     110.803|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 134   |     222|       7.329|   1.7%/ 40|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 134   |     215|      20.048|   0.4%/181|   0.4%/173|   0.4%/171|   0.4%/169 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 134   |    2337|     140.761|   1.5%/ 46|   1.2%/ 55|   1.2%/ 58|   1.1%/ 62 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 120   |      51|       4.204|   0.8%/ 92|   0.5%/129|   0.5%/143|   0.4%/162 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 109   |      29|      18.026|   0.8%/ 89|   1.0%/ 68|   1.1%/ 65|   1.1%/ 61 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 130   |     185|      15.963|   1.1%/ 64|   1.2%/ 58|   1.2%/ 57|   1.2%/ 55 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 134   |    1628|     177.752|   1.6%/ 44|   1.0%/ 67|   0.9%/ 77|   0.8%/ 91 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 134   |     603|      61.728|   0.1%/613|   0.2%/457|   0.2%/429|   0.2%/404 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 134   |   47423|      34.839|   2.2%/ 32|   2.1%/ 33|   2.1%/ 33|   2.0%/ 34 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 134   |    5991|      22.445|   1.2%/ 57|   1.0%/ 67|   1.0%/ 70|   0.9%/ 74 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 134   |   19561|     234.603|   1.1%/ 63|   1.0%/ 71|   0.9%/ 73|   0.9%/ 75 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 134   |    5669|     144.881|   1.4%/ 48|   1.3%/ 54|   1.2%/ 56|   1.2%/ 58 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 134   |    1773|     360.247|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 134   |     640|      69.616|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.7%/ 40 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 134   |   35227|     584.790|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 134   |      14|       5.116|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 134   |    1055|       8.378|   0.4%/168|   0.5%/139|   0.5%/134|   0.5%/128 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 134   |      11|       1.033|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 134   |    1277|      68.335|   0.9%/ 80|   1.3%/ 53|   1.4%/ 49|   1.5%/ 45 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 134   |     467|       9.820|   2.4%/ 28|   2.2%/ 32|   2.1%/ 33|   2.0%/ 35 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 134   |     364|     202.449|   3.7%/ 18|   3.6%/ 19|   3.5%/ 20|   3.4%/ 20 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 131   |     490|     110.916|   0.7%/ 96|   0.7%/100|   0.7%/101|   0.7%/102 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 132   |    1509|     231.002|   0.8%/ 91|   0.1%/817|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 132   |      32|      16.909|   0.1%/559|   0.1%/672|   0.1%/724|   0.1%/793 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 134   |      86|      12.654|   3.5%/ 20|   3.8%/ 18|   3.9%/ 18|   4.0%/ 17 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 131   |      82|      18.249|   0.7%/ 97|   0.8%/ 92|   0.8%/ 91|   0.8%/ 90 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 133   |     135|      19.657|   4.8%/ 14|   5.0%/ 14|   5.3%/ 13|   3.5%/ 20 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 134   |      81|      29.009|   0.1%/886|   0.1%/794|   0.1%/771|   0.1%/750 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  88   |     161|       6.126|   3.6%/ 19|   2.9%/ 23|   2.8%/ 25|   2.6%/ 26 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 134   |     126|       3.832|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 134   |     125|       6.187|   0.1%/840|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 134   |     158|      38.653|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 134   |   54666|     431.876|   1.3%/ 52|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 134   |     871|     324.959|   0.9%/ 78|   0.8%/ 85|   0.8%/ 86|   0.8%/ 88 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 134   |     540|      15.063|   3.3%/ 21|   3.8%/ 18|   3.9%/ 18|   3.9%/ 17 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  80   |      18|       0.602|   3.0%/ 23|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  34   |      21|       8.693|   6.9%/ 10|   6.9%/ 10|   5.8%/ 12|   4.7%/ 15 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  89   |      85|       2.834|   4.2%/ 16|   5.1%/ 13|   5.3%/ 13|   5.6%/ 12 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 134   |    6181|     354.049|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 134   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 134   |     128|      19.885|   0.8%/ 85|   0.7%/ 96|   0.7%/ 99|   0.7%/103 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 134   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 134   |     968|       4.694|   0.7%/102|   0.6%/117|   0.6%/121|   0.6%/125 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 134   |     542|     261.175|   0.8%/ 89|   0.6%/114|   0.6%/123|   0.5%/134 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 134   |     256|      47.724|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 134   |     547|     117.185|   1.9%/ 36|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 134   |    6160|      28.083|   0.3%/250|   0.2%/348|   0.2%/384|   0.2%/427 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 134   |    1740|     412.473|   1.6%/ 44|   1.3%/ 51|   1.3%/ 54|   1.2%/ 56 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  17   |       3|       0.336|  14.5%/  5|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 134   |      86|      12.025|   5.1%/ 13|   5.6%/ 12|   5.8%/ 12|   5.9%/ 12 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 134   |   22821|     710.244|   1.0%/ 66|   1.0%/ 70|   1.0%/ 71|   1.0%/ 72 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 134   |    2332|      21.486|   1.3%/ 52|   1.5%/ 46|   1.6%/ 44|   1.6%/ 43 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 134   |    1827|      47.616|   0.5%/128|   0.6%/122|   0.6%/121|   0.6%/119 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 134   |    1764|     171.650|   0.2%/422|   0.2%/452|   0.2%/458|   0.1%/465 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 134   |     189|      68.734|   0.8%/ 83|   0.9%/ 79|   0.9%/ 79|   0.9%/ 78 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 134   |    2792|     143.859|   1.5%/ 46|   1.6%/ 43|   1.6%/ 43|   1.6%/ 42 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 134   |   15326|     104.441|   0.8%/ 88|   0.7%/ 98|   0.7%/101|   0.7%/104 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  75   |       5|       0.404|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 134   |    3269|      95.529|   1.1%/ 64|   1.0%/ 66|   1.0%/ 67|   1.0%/ 67 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 134   |     243|      15.000|   1.4%/ 48|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 134   |     670|      96.166|   1.2%/ 58|   1.0%/ 69|   1.0%/ 72|   0.9%/ 76 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 112   |      69|       8.694|   0.3%/232|   0.4%/182|   0.4%/172|   0.4%/162 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 134   |      27|       4.734|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 134   |      28|       5.132|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 134   |     129|      61.605|   0.6%/107|   0.7%/ 95|   0.8%/ 92|   0.8%/ 90 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 127   |      93|       5.852|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 134   |   11439|     194.630|   2.8%/ 24|   2.6%/ 27|   2.5%/ 27|   2.4%/ 28 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 134   |   28547|     606.086|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 134   |      11|       0.505|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 134   |     792|      18.673|   0.5%/133|   0.5%/147|   0.5%/152|   0.4%/156 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 134   |    5789|     559.974|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 134   |    1989|     231.219|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 134   |      56|       3.198|   2.0%/ 34|   1.4%/ 51|   1.2%/ 58|   1.0%/ 66 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 134   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 134   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 134   |      25|       3.308|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 134   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 134   |      52|       4.395|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 134   |    5896|      70.908|   0.3%/246|   0.3%/255|   0.3%/257|   0.3%/259 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 134   |  166308|     504.660|   0.7%/102|   0.7%/103|   0.7%/104|   0.7%/104 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  20   |       9|       0.229|   4.8%/ 14|  13.7%/  5|  12.8%/  5|   9.4%/  7 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 134   |    1987|      47.454|   1.3%/ 54|   1.4%/ 51|   1.4%/ 50|   1.4%/ 50 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 134   |     359|      36.309|   0.2%/314|   0.2%/338|   0.2%/345|   0.2%/353 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 134   |   46820|     704.742|   0.1%/671|   0.1%/797|   0.1%/838|   0.1%/886 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 134   |      38|      10.717|   0.4%/195|   0.2%/315|   0.2%/375|   0.1%/467 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 134   |     217|       6.369|   3.5%/ 20|   3.2%/ 21|   3.2%/ 22|   3.1%/ 22 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 134   |     244|       7.580|   3.4%/ 21|   3.4%/ 20|   3.4%/ 20|   3.5%/ 20 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  13   |      18|       0.187|  12.6%/  5|  14.5%/  5|  17.0%/  4|  11.5%/  6 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 133   |     239|      13.367|   5.0%/ 14|   5.7%/ 12|   5.9%/ 12|   6.1%/ 11 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 134   |     131|       8.620|   1.6%/ 42|   0.6%/107|   0.6%/107|   5.5%/ 13 |

