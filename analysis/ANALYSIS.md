# State and Country COVID-19 Analysis #
## Updated: at 2020-09-17 for data as of 2020-09-16 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.3% of deaths and 39.0% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.3% of deaths and 56.6% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 169   |   33055|    1699.197|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 169   |   16038|    1805.671|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 169   |   14994|     517.095|   0.8%/ 86|   0.7%/105|   0.6%/111|   0.6%/118 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 169   |   14827|     375.254|   0.7%/ 99|   0.6%/110|   0.6%/113|   0.6%/116 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 169   |   13037|     607.015|   0.8%/ 87|   0.7%/ 99|   0.7%/103|   0.7%/106 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 169   |    9250|    1331.018|   0.1%/526|   0.1%/556|   0.1%/564|   0.1%/572 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 169   |    8596|     678.361|   0.2%/281|   0.2%/282|   0.2%/282|   0.2%/283 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 169   |    7889|     616.242|   0.2%/433|   0.2%/461|   0.1%/469|   0.1%/477 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 169   |    6945|     695.441|   0.1%/463|   0.1%/476|   0.1%/480|   0.1%/483 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 169   |    6586|     620.313|   0.8%/ 88|   0.7%/105|   0.6%/110|   0.6%/116 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 169   |  197252|     598.561|   0.4%/171|   0.4%/184|   0.4%/187|   0.4%/191 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 169   |  134881|     638.001|   0.6%/120|   0.5%/132|   0.5%/135|   0.5%/139 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 169   |   83354|      61.235|   1.5%/ 48|   1.4%/ 50|   1.4%/ 50|   1.4%/ 51 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 169   |   72728|     574.569|   0.7%/105|   0.6%/115|   0.6%/118|   0.6%/121 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 169   |   41752|     628.454|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 169   |   35636|     591.585|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 169   |   30965|     461.644|   0.1%/830|   0.1%/740|   0.1%/720|   0.1%/701 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 169   |   31273|     973.288|   0.4%/156|   0.4%/177|   0.4%/183|   0.4%/189 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 169   |   29919|     635.223|   0.2%/374|   0.2%/339|   0.2%/331|   0.2%/324 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 169   |   23599|     283.040|   0.5%/127|   0.5%/131|   0.5%/132|   0.5%/133 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 169   |    2422|     494.054|   0.6%/112|   0.6%/124|   0.5%/128|   0.5%/132 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 169   |      47|      63.940|   0.8%/ 89|   0.7%/104|   0.6%/109|   0.6%/114 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 169   |    5452|     748.968|   0.4%/190|   0.3%/266|   0.2%/296|   0.2%/332 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 169   |    1053|     349.085|   1.5%/ 45|   1.4%/ 49|   1.4%/ 50|   1.4%/ 51 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 169   |   14827|     375.254|   0.7%/ 99|   0.6%/110|   0.6%/113|   0.6%/116 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 169   |    2002|     347.563|   0.2%/417|   0.2%/431|   0.2%/435|   0.2%/439 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 169   |    4483|    1257.363|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 169   |     617|     633.422|   0.1%/468|   0.2%/432|   0.2%/422|   0.2%/413 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 169   |   13037|     607.015|   0.8%/ 87|   0.7%/ 99|   0.7%/103|   0.7%/106 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 169   |    6586|     620.313|   0.8%/ 88|   0.7%/105|   0.6%/110|   0.6%/116 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 169   |     113|      79.851|   2.5%/ 28|   2.2%/ 31|   2.1%/ 32|   2.0%/ 34 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 169   |     442|     247.527|   0.9%/ 73|   0.7%/ 95|   0.7%/102|   0.6%/111 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 169   |    8596|     678.361|   0.2%/281|   0.2%/282|   0.2%/282|   0.2%/283 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 169   |    3473|     515.867|   0.3%/234|   0.3%/244|   0.3%/246|   0.3%/249 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 169   |    1257|     398.537|   0.7%/106|   0.6%/116|   0.6%/118|   0.6%/121 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 169   |     533|     182.999|   1.4%/ 49|   1.6%/ 43|   1.7%/ 42|   1.7%/ 41 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 169   |    1088|     243.469|   0.9%/ 81|   0.8%/ 83|   0.8%/ 83|   0.8%/ 84 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 169   |    5329|    1146.411|   0.4%/168|   0.4%/193|   0.3%/200|   0.3%/208 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 169   |     137|     101.760|   0.2%/289|   0.2%/283|   0.2%/281|   0.2%/278 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 169   |    3865|     639.227|   0.2%/433|   0.1%/475|   0.1%/487|   0.1%/500 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 169   |    9250|    1331.018|   0.1%/526|   0.1%/556|   0.1%/564|   0.1%/572 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 169   |    6945|     695.441|   0.1%/463|   0.1%/476|   0.1%/480|   0.1%/483 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 169   |    1986|     352.096|   0.4%/185|   0.4%/189|   0.4%/190|   0.4%/191 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 169   |    2794|     938.719|   0.7%/104|   0.6%/122|   0.5%/127|   0.5%/133 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 169   |    1784|     290.620|   0.7%/102|   0.7%/106|   0.6%/108|   0.6%/109 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 169   |     141|     131.535|   1.9%/ 36|   2.0%/ 35|   2.0%/ 34|   2.0%/ 34 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 169   |     439|     226.937|   0.6%/123|   0.6%/124|   0.6%/124|   0.6%/124 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 169   |    1516|     492.139|   0.7%/ 92|   0.6%/112|   0.6%/119|   0.6%/125 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 169   |     437|     321.359|   0.1%/762|   0.1%/770|   0.1%/767|   0.1%/763 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 169   |   16038|    1805.671|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 169   |     839|     400.052|   0.4%/176|   0.3%/200|   0.3%/207|   0.3%/215 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 169   |   33055|    1699.197|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 169   |    3152|     300.526|   0.9%/ 80|   0.8%/ 83|   0.8%/ 83|   0.8%/ 84 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 169   |     173|     226.449|   1.2%/ 57|   1.3%/ 54|   1.3%/ 53|   1.3%/ 53 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 169   |    4502|     385.128|   0.5%/128|   0.5%/126|   0.6%/126|   0.6%/125 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 169   |     936|     236.548|   0.8%/ 83|   0.7%/ 94|   0.7%/ 98|   0.7%/101 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 169   |     525|     124.543|   0.8%/ 86|   0.7%/ 94|   0.7%/ 96|   0.7%/ 98 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 169   |    7889|     616.242|   0.2%/433|   0.2%/461|   0.1%/469|   0.1%/477 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 169   |     563|     176.160|   1.6%/ 43|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 169   |    1077|    1017.065|   0.2%/352|   0.2%/333|   0.2%/328|   0.2%/323 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 169   |    3171|     615.822|   0.8%/ 84|   0.7%/ 95|   0.7%/ 98|   0.7%/102 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 169   |     185|     209.194|   0.8%/ 90|   0.8%/ 84|   0.8%/ 82|   0.9%/ 80 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 169   |    2159|     316.017|   1.3%/ 55|   1.2%/ 58|   1.2%/ 58|   1.2%/ 59 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 169   |   14994|     517.095|   0.8%/ 86|   0.7%/105|   0.6%/111|   0.6%/118 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 169   |  197252|     598.561|   0.4%/171|   0.4%/184|   0.4%/187|   0.4%/191 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 169   |     443|     138.311|   0.4%/172|   0.3%/220|   0.3%/236|   0.3%/254 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 169   |      58|      92.950|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 169   |    2814|     329.645|   0.4%/159|   0.4%/173|   0.4%/177|   0.4%/181 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 169   |    2027|     266.180|   0.3%/226|   0.3%/261|   0.3%/270|   0.2%/281 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 169   |     294|     164.014|   1.8%/ 39|   1.7%/ 41|   1.7%/ 41|   1.6%/ 42 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 169   |    1229|     211.040|   0.5%/136|   0.5%/140|   0.5%/141|   0.5%/143 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 157   |      45|      77.279|   0.1%/961|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 169   |    1431|      44.398|   0.1%/639|   0.1%/719|   0.1%/739|   0.1%/758 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 169   |     353|     124.193|   1.1%/ 60|   1.0%/ 69|   1.0%/ 72|   0.9%/ 74 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 169   |    1645|      38.257|   0.5%/132|   0.5%/138|   0.5%/140|   0.5%/141 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 169   |     140|       4.506|   1.6%/ 43|   1.6%/ 42|   1.6%/ 42|   1.6%/ 42 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 169   |   12486|     277.835|   2.0%/ 34|   1.8%/ 37|   1.8%/ 38|   1.8%/ 39 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 169   |     928|     313.659|   0.3%/226|   0.3%/254|   0.3%/262|   0.3%/271 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 169   |     985|      38.364|   1.1%/ 61|   0.7%/102|   0.6%/124|   0.4%/156 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 169   |     755|      84.763|   0.1%/504|   0.2%/429|   0.2%/412|   0.2%/396 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 169   |     569|      56.504|   0.4%/175|   0.4%/174|   0.4%/174|   0.4%/174 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 169   |     214|     138.866|   0.7%/ 92|   0.8%/ 90|   0.8%/ 89|   0.8%/ 88 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 169   |    4879|      28.963|   0.8%/ 91|   0.7%/ 99|   0.7%/101|   0.7%/104 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 169   |     766|      81.411|   0.8%/ 91|   0.8%/ 90|   0.8%/ 90|   0.8%/ 90 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 169   |    9929|     861.567|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 164   |      40|       3.432|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 169   |    7624|     664.689|   0.9%/ 78|   0.7%/ 95|   0.7%/100|   0.7%/106 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 169   |     739|     223.821|   1.1%/ 63|   1.0%/ 69|   1.0%/ 71|   0.9%/ 73 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 169   |      13|       5.434|   5.5%/ 12|   5.4%/ 13|   5.4%/ 13|   5.3%/ 13 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 169   |  134881|     638.001|   0.6%/120|   0.5%/132|   0.5%/135|   0.5%/139 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 169   |     760|     109.300|   1.0%/ 66|   0.9%/ 75|   0.9%/ 77|   0.9%/ 80 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 169   |      56|       2.686|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 157   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 169   |     417|      15.721|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 169   |    9244|     243.282|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 117   |      62|      11.316|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 142   |      81|       4.962|   0.2%/374|   0.3%/276|   0.3%/258|   0.3%/242 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 169   |   12122|     634.443|   0.4%/160|   0.4%/168|   0.4%/170|   0.4%/172 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 169   |    4745|       3.384|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 169   |   24206|     490.043|   1.1%/ 63|   0.9%/ 74|   0.9%/ 78|   0.8%/ 82 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 169   |     646|     127.639|   2.5%/ 27|   2.5%/ 27|   2.5%/ 27|   2.5%/ 27 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 169   |     225|      55.234|   1.5%/ 46|   1.7%/ 41|   1.8%/ 39|   1.8%/ 38 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 169   |     109|       9.768|   0.8%/ 91|   0.8%/ 83|   0.8%/ 82|   0.9%/ 80 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 169   |     632|     108.502|   0.1%/759|   0.1%/661|   0.1%/640|   0.1%/620 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 169   |    2047|     197.577|   1.0%/ 72|   0.9%/ 77|   0.9%/ 79|   0.9%/ 80 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 169   |    7094|     406.099|   0.4%/161|   0.4%/169|   0.4%/171|   0.4%/173 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 169   |    5705|      56.898|   0.3%/220|   0.3%/225|   0.3%/227|   0.3%/228 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 169   |     814|     125.437|   0.6%/114|   0.5%/145|   0.4%/156|   0.4%/168 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 148   |      83|      61.107|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 165   |    1099|      11.134|   1.5%/ 46|   1.2%/ 58|   1.1%/ 62|   1.0%/ 66 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 169   |     338|      61.122|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 169   |   30965|     461.644|   0.1%/830|   0.1%/740|   0.1%/720|   0.1%/701 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 169   |      53|      24.455|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 169   |     106|      45.174|   0.3%/206|   1.0%/ 70|   1.0%/ 71|   1.3%/ 54 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 166   |      19|       5.218|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 169   |    9371|     112.698|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 169   |     297|       9.800|   0.4%/174|   0.3%/234|   0.3%/254|   0.3%/277 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 169   |     317|      29.520|   1.1%/ 64|   1.1%/ 62|   1.1%/ 62|   1.1%/ 62 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 169   |    3044|     183.344|   0.5%/135|   0.4%/169|   0.4%/180|   0.4%/192 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 155   |      65|       5.315|   0.4%/188|   0.2%/358|   0.1%/467|   0.1%/674 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 144   |      40|      24.942|   0.4%/197|   0.3%/202|   0.3%/204|   0.3%/206 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 165   |     222|      19.146|   0.5%/148|   0.5%/146|   0.5%/146|   0.5%/146 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 169   |    2174|     237.369|   0.7%/ 96|   0.6%/118|   0.5%/126|   0.5%/136 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 169   |     635|      65.004|   0.3%/229|   0.4%/193|   0.4%/185|   0.4%/178 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 169   |   83354|      61.235|   1.5%/ 48|   1.4%/ 50|   1.4%/ 50|   1.4%/ 51 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 169   |    9103|      34.103|   1.3%/ 54|   1.3%/ 54|   1.3%/ 55|   1.3%/ 55 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 169   |   23599|     283.040|   0.5%/127|   0.5%/131|   0.5%/132|   0.5%/133 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 169   |    8321|     212.652|   1.0%/ 71|   0.9%/ 76|   0.9%/ 77|   0.9%/ 78 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 169   |    1783|     362.368|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 169   |    1181|     128.560|   1.4%/ 51|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 169   |   35636|     591.585|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 169   |      48|      17.542|   4.6%/ 15|   4.7%/ 15|   4.7%/ 15|   4.7%/ 15 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 169   |    1497|      11.885|   0.8%/ 85|   0.8%/ 92|   0.7%/ 94|   0.7%/ 96 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 169   |      21|       2.008|   4.0%/ 17|   4.5%/ 15|   4.6%/ 15|   4.7%/ 14 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 169   |    1700|      90.999|   0.4%/156|   0.3%/206|   0.3%/224|   0.3%/245 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 169   |     642|      13.504|   0.5%/129|   0.4%/172|   0.4%/187|   0.3%/204 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 169   |     509|     283.235|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 166   |     568|     128.491|   0.4%/157|   0.5%/152|   0.5%/151|   0.5%/149 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 167   |    1022|     156.463|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 167   |      35|      18.615|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 169   |     265|      38.755|   2.9%/ 24|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 166   |      82|      18.324|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 168   |     395|      57.460|   2.9%/ 24|   2.8%/ 25|   2.7%/ 25|   2.7%/ 25 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 169   |      87|      31.284|   0.1%/648|   0.1%/985|   0.1%/ ***|   0.1%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 123   |     217|       8.253|   0.7%/ 97|   0.6%/107|   0.6%/110|   0.6%/114 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 169   |     129|       3.930|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 169   |     128|       6.328|   0.1%/681|   0.1%/629|   0.1%/619|   0.1%/609 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 169   |     161|      39.593|   0.1%/897|   0.1%/939|   0.1%/955|   0.1%/973 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 169   |   72728|     574.569|   0.7%/105|   0.6%/115|   0.6%/118|   0.6%/121 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 169   |    1156|     431.134|   0.8%/ 82|   0.8%/ 82|   0.8%/ 82|   0.8%/ 82 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 169   |    1821|      50.770|   2.4%/ 29|   2.0%/ 34|   2.0%/ 35|   1.9%/ 37 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 115   |      37|       1.241|   3.2%/ 21|   3.7%/ 19|   3.8%/ 18|   3.9%/ 17 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  69   |     107|      43.623|   1.9%/ 37|   2.1%/ 34|   2.1%/ 33|   2.2%/ 32 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 124   |     394|      13.136|   3.2%/ 21|   2.6%/ 26|   2.5%/ 28|   2.3%/ 30 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 169   |    6307|     361.263|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 169   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 169   |     147|      22.755|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 169   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 169   |    1094|       5.309|   0.4%/192|   0.4%/193|   0.4%/193|   0.4%/193 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 169   |     663|     319.199|   0.7%/102|   0.7%/100|   0.7%/100|   0.7%/ 99 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 169   |     265|      49.405|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 169   |     806|     172.808|   1.1%/ 65|   1.0%/ 66|   1.0%/ 66|   1.0%/ 66 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 169   |    6412|      29.236|   0.1%/763|   0.1%/891|   0.1%/930|   0.1%/973 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 169   |    2219|     525.967|   0.6%/125|   0.5%/143|   0.5%/148|   0.5%/153 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  52   |       6|       0.685|   1.6%/ 43|   5.7%/ 12|   6.9%/ 10|   8.0%/  9 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 169   |     647|      90.439|   3.4%/ 20|   2.8%/ 25|   2.6%/ 27|   2.4%/ 29 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 169   |   31273|     973.288|   0.4%/156|   0.4%/177|   0.4%/183|   0.4%/189 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 169   |    4647|      42.827|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 169   |    2235|      58.227|   0.5%/128|   0.5%/129|   0.5%/130|   0.5%/130 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 169   |    1874|     182.353|   0.2%/355|   0.2%/338|   0.2%/334|   0.2%/330 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 169   |     208|      75.788|   0.3%/222|   0.3%/213|   0.3%/211|   0.3%/209 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 169   |    4343|     223.813|   1.0%/ 68|   0.9%/ 74|   0.9%/ 76|   0.9%/ 78 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 169   |   18853|     128.478|   0.6%/120|   0.6%/122|   0.6%/122|   0.6%/123 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 110   |      23|       1.889|   5.0%/ 14|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 169   |    4392|     128.356|   0.7%/ 99|   0.7%/106|   0.6%/108|   0.6%/110 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 169   |     303|      18.708|   0.3%/220|   0.2%/338|   0.2%/389|   0.2%/458 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 169   |     741|     106.360|   0.2%/410|   0.1%/596|   0.1%/670|   0.1%/763 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 147   |      72|       9.174|   0.1%/486|   0.1%/568|   0.1%/598|   0.1%/635 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 169   |      27|       4.734|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 169   |      39|       7.092|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 169   |     136|      64.989|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 162   |      99|       6.209|   0.1%/774|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 169   |   16057|     273.190|   0.6%/116|   0.4%/156|   0.4%/170|   0.4%/188 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 169   |   29919|     635.223|   0.2%/374|   0.2%/339|   0.2%/331|   0.2%/324 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 169   |      12|       0.573|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 169   |     840|      19.786|   0.1%/891|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 169   |    5854|     566.286|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 169   |    2026|     235.462|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 169   |     173|       9.864|   2.2%/ 31|   2.0%/ 34|   1.9%/ 36|   1.9%/ 37 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 169   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 169   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 169   |      39|       5.159|   2.3%/ 30|   2.8%/ 25|   2.9%/ 24|   3.0%/ 23 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 169   |      62|      45.645|   6.2%/ 11|   6.2%/ 11|   6.2%/ 11|   6.2%/ 11 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 169   |     114|       9.732|   2.9%/ 24|   3.3%/ 21|   3.4%/ 20|   3.5%/ 20 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 169   |    7145|      85.927|   0.8%/ 85|   0.9%/ 78|   0.9%/ 76|   0.9%/ 74 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 169   |  197252|     598.561|   0.4%/171|   0.4%/184|   0.4%/187|   0.4%/191 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  55   |      60|       1.495|   4.5%/ 15|   3.6%/ 19|   3.5%/ 20|   3.4%/ 20 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 169   |    3387|      80.878|   1.6%/ 42|   1.7%/ 42|   1.7%/ 41|   1.7%/ 41 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 169   |     403|      40.723|   0.3%/242|   0.3%/256|   0.3%/259|   0.3%/263 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 169   |   41752|     628.454|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 169   |      46|      13.115|   0.1%/634|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 169   |     413|      12.111|   1.6%/ 44|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 169   |     515|      15.994|   1.8%/ 39|   1.7%/ 41|   1.7%/ 42|   1.6%/ 42 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  48   |      35|       0.364|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 168   |     318|      17.769|   0.8%/ 89|   0.9%/ 81|   0.9%/ 79|   0.9%/ 77 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 169   |     243|      16.032|   0.8%/ 87|   0.3%/218|   0.2%/352|   0.1%/906 |

