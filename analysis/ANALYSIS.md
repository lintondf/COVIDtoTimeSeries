# State and Country COVID-19 Analysis #
## Updated: 2021-01-06 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# Notes #

- Expect discontinuities in the US around 4/14/2020 as the [CDC](CDC "https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html")  expanded the definition of a COVID-19 death.  
- There is also some weekly pattern to reporting with lower values on the weekend followed by higher values subsequently, at least in some places.

# Ten US States with Highest Death Tolls #

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. One per million is 0.0001%.  1% is 10,000 per million.

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDeathRates.png)

Daily Death Growth Rate (DDGR) in the 10 US States with the highest death tolls.

DDGR is the cube root of Arnold Kling's [Three Day Death Reproduction Rate (3DDRR)](http://www.arnoldkling.com/blog/the-3ddrr/).  The 3DDRR is calculated by dividing the cumulative total number of deaths on a given day by the  cumulative total number of deaths three days previously.  Taking the cube root converts this to the geometric mean for the three days.  These values are LOWESS filtered to generate a local-error minimizing non-parametric trend.

If deaths remain constant over the three days, the DDGR equals one.  A value of 2 would indicate that the number of deaths doubles every day.

![US States with Highest Death Toll - Daily Death Growth Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 298   |   36610|    1881.906|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 295   |   28051|     967.404|   1.007/ **|   1.007/ 99|   1.007/ 98|   1.007/ 98 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 308   |   24235|     613.343|   1.008/ 92|   1.008/ 89|   1.008/ 86|   1.008/ 85 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 304   |   22146|    1031.112|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 302   |   18469|    2079.298|   1.003/ **|   1.003/ **|   1.003/ **|   1.004/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 295   |   17815|    1405.864|   1.011/ 63|   1.011/ 61|   1.012/ 60|   1.012/ 59 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 293   |   14577|    1138.678|   1.013/ 55|   1.013/ 52|   1.014/ 50|   1.014/ 50 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 293   |   12822|    1283.881|   1.010/ 66|   1.011/ 64|   1.011/ 62|   1.011/ 61 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 292   |   12099|    1740.935|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 300   |   11294|    1063.749|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |


- Days - Number of days since first death
- Deaths - Total deaths to date
- Deaths/1M - Deaths per million in population
- DDGR - **Smoothed** Daily Deaths Growth Rate [n:m] total deaths n days ago over m days ago followed by the DDGR expressed as the number of days to double the total deaths count if that rate holds

# Ten Countries with Highest Death Tolls #

Deaths in the 10 countries with the highest death tolls expressed as deaths per 1 million population. 

![Countries with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/Countries10WorstDeathRates.png)

Daily Death Growth Rate (DDGR) in the 10 countries with the highest death tolls.

![Countries with Highest Death Toll - Daily Death Growth Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/Countries10WorstDDGR.png)

|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 312   |  337247|    1023.375|   1.008/ 91|   1.008/ 88|   1.008/ 86|   1.008/ 85 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 295   |  196641|     930.134|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 301   |  160611|     117.990|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 293   |  128303|    1013.631|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 320   |   73271|    1216.349|   1.012/ 58|   1.012/ 56|   1.013/ 54|   1.013/ 54 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 301   |   73122|    1100.650|   1.009/ 80|   1.009/ 78|   1.009/ 75|   1.009/ 75 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 326   |   66920|     997.671|   1.009/ 80|   1.009/ 78|   1.009/ 76|   1.009/ 76 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 293   |   58837|     400.947|   1.012/ 56|   1.012/ 56|   1.013/ 55|   1.013/ 55 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 321   |   62082|     744.588|   1.006/ **|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 309   |   53225|    1130.040|   1.004/ **|   1.005/ **|   1.005/ **|   1.005/ ** |


# US and Selected States #

For each country and each US state, deaths per million in population is plotted on the left logarithmic axis and the raw and smoothed DDGR is plotted on the linear right axis.

For the US and each US state a second chart is included below showing the various estimates of total deaths from the [IHME Projections](https://covid19.healthdata.org/united-states-of-america) website.  Historical data is from [here](http://www.healthdata.org/covid/data-downloads).  Above the date on which the estimate is issued a vertical line is plotted from the lower to the upper final total estimated deaths with a dot indicating the mean estimate.  A shaded region showing the growth to these final estimate is plotted for each IHME projection with a correspondingly colored solid line connecting the mean estimates.  The actual deaths to date are plotted as a solid black line.

## United States ##
![United States](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)

## Florida ##
![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)

## Maryland ##
![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)

## Maine ##
![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)

# US States #

Click on the link in the first column to view the DDGR and IHME charts for a specific state.

|State|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 287   |    4827|     984.366|   1.008/ 83|   1.008/ 82|   1.009/ 80|   1.009/ 80 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 287   |     224|     306.615|   1.010/ 68|   1.010/ 67|   1.010/ 66|   1.010/ 66 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 291   |    8347|    1146.800|   1.008/ 83|   1.009/ 80|   1.009/ 77|   1.009/ 76 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 288   |    3809|    1262.199|   1.011/ 63|   1.011/ 63|   1.011/ 63|   1.011/ 62 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 308   |   24235|     613.343|   1.008/ 92|   1.008/ 89|   1.008/ 86|   1.008/ 85 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 298   |    4626|     803.349|   1.012/ 57|   1.012/ 55|   1.013/ 54|   1.013/ 53 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 293   |    5757|    1614.688|   1.006/ **|   1.006/ **|   1.006/ **|   1.007/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 286   |     906|     930.483|   1.005/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 304   |   22146|    1031.112|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 300   |   11294|    1063.749|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 281   |     317|     224.146|   1.002/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 286   |    1515|     847.545|   1.013/ 52|   1.013/ 52|   1.013/ 51|   1.013/ 51 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 295   |   17815|    1405.864|   1.011/ 63|   1.011/ 61|   1.012/ 60|   1.012/ 59 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 296   |    8224|    1221.597|   1.013/ 55|   1.013/ 54|   1.013/ 52|   1.013/ 52 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 287   |    3966|    1256.911|   1.011/ 62|   1.011/ 61|   1.011/ 61|   1.011/ 61 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 299   |    2894|     993.245|   1.015/ 47|   1.015/ 47|   1.015/ 47|   1.015/ 46 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 296   |    2693|     602.765|   1.010/ 66|   1.011/ 65|   1.011/ 64|   1.011/ 64 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 298   |    7377|    1586.920|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 285   |     318|     236.515|   1.014/ 48|   1.015/ 46|   1.016/ 44|   1.016/ 43 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 293   |    5647|     934.098|   1.008/ 92|   1.008/ 88|   1.008/ 84|   1.008/ 84 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 292   |   12099|    1740.935|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 293   |   12822|    1283.881|   1.010/ 66|   1.011/ 64|   1.011/ 62|   1.011/ 61 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 291   |    5487|     973.009|   1.014/ 51|   1.014/ 50|   1.014/ 49|   1.014/ 49 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 293   |    4733|    1590.425|   1.007/ **|   1.007/ 99|   1.007/ 97|   1.007/ 96 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 293   |    5962|     971.415|   1.011/ 64|   1.011/ 63|   1.011/ 63|   1.011/ 63 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 285   |    1221|    1142.277|   1.012/ 58|   1.011/ 61|   1.011/ 65|   1.011/ 66 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 284   |    1772|     916.045|   1.014/ 49|   1.014/ 49|   1.014/ 48|   1.014/ 48 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 296   |    2972|     964.951|   1.011/ 63|   1.011/ 61|   1.012/ 59|   1.012/ 58 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 289   |     685|     503.830|   1.011/ 64|   1.011/ 61|   1.012/ 58|   1.012/ 57 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 302   |   18469|    2079.298|   1.003/ **|   1.003/ **|   1.003/ **|   1.004/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 287   |    2478|    1181.597|   1.017/ 42|   1.017/ 40|   1.018/ 39|   1.018/ 39 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 298   |   36610|    1881.906|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 287   |    6909|     658.772|   1.007/ 94|   1.007/ 94|   1.007/ 93|   1.007/ 93 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 285   |    1689|    2216.728|   1.009/ 77|   1.008/ 86|   1.007/ 97|   1.007/ ** |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 292   |    8675|     742.125|   1.010/ 68|   1.011/ 66|   1.011/ 64|   1.011/ 63 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 293   |    2542|     642.286|   1.011/ 65|   1.011/ 64|   1.011/ 63|   1.011/ 63 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 297   |    1460|     346.054|   1.014/ 50|   1.014/ 49|   1.015/ 47|   1.015/ 47 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 293   |   14577|    1138.678|   1.013/ 55|   1.013/ 52|   1.014/ 50|   1.014/ 50 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 291   |    1559|     488.080|   1.009/ 74|   1.009/ 74|   1.009/ 73|   1.009/ 73 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 284   |    1724|    1627.293|   1.009/ 77|   1.009/ 74|   1.010/ 71|   1.010/ 70 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 296   |    5326|    1034.434|   1.005/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 301   |    1854|    2095.905|   1.016/ 44|   1.015/ 45|   1.015/ 45|   1.015/ 46 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 291   |    7096|    1038.452|   1.013/ 53|   1.013/ 53|   1.013/ 52|   1.013/ 52 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 295   |   28051|     967.404|   1.007/ **|   1.007/ 99|   1.007/ 98|   1.007/ 98 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 290   |    1320|     411.790|   1.013/ 54|   1.013/ 53|   1.013/ 52|   1.013/ 52 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 292   |      62|     100.007|   1.017/ 42|   1.017/ 40|   1.018/ 38|   1.019/ 37 |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 298   |    4988|     584.337|   1.006/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 312   |    3325|     436.580|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 282   |    1365|     761.730|   1.019/ 36|   1.019/ 36|   1.020/ 35|   1.020/ 35 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 292   |    5932|    1018.819|   1.014/ 49|   1.014/ 48|   1.014/ 48|   1.014/ 48 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 268   |     516|     892.053|   1.024/ 28|   1.024/ 28|   1.025/ 28|   1.025/ 28 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 290   |    2161|      67.061|   1.007/ 94|   1.008/ 91|   1.008/ 88|   1.008/ 87 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 301   |    1270|     446.308|   1.013/ 52|   1.013/ 52|   1.013/ 51|   1.013/ 51 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 300   |    2876|      66.894|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 283   |     453|      14.564|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 304   |   53628|    1193.354|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 286   |    3182|    1075.865|   1.011/ 63|   1.011/ 64|   1.011/ 65|   1.011/ 65 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 311   |     929|      36.167|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 300   |    6861|     770.677|   1.027/ 25|   1.028/ 24|   1.029/ 24|   1.029/ 23 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 299   |    2634|     261.631|   1.025/ 28|   1.025/ 27|   1.026/ 26|   1.026/ 26 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 296   |     381|     247.056|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 294   |    7723|      45.843|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 281   |    1443|     153.386|   1.007/ **|   1.007/ **|   1.007/ **|   1.007/ ** |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 301   |   20817|    1806.290|   1.006/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 275   |      45|       3.812|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 283   |    9369|     816.851|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 291   |    4793|    1451.963|   1.017/ 41|   1.017/ 41|   1.017/ 41|   1.017/ 41 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 281   |      46|      19.530|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 295   |  196641|     930.134|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 301   |    9037|    1299.970|   1.027/ 25|   1.027/ 25|   1.028/ 25|   1.028/ 25 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 294   |      79|       3.769|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 268   |       1|       0.091|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 287   |     451|      16.987|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 303   |   15086|     396.998|   1.009/ 75|   1.010/ 73|   1.010/ 70|   1.010/ 69 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 228   |      63|      11.513|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 253   |     106|       6.526|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 290   |   16971|     888.204|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 301   |    4766|       3.399|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 290   |   44559|     902.086|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 293   |    2416|     477.751|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 293   |    4788|    1174.563|   1.031/ 22|   1.032/ 22|   1.032/ 22|   1.032/ 22 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 294   |     145|      12.928|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 298   |     982|     168.576|   1.012/ 59|   1.012/ 57|   1.013/ 54|   1.013/ 54 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 295   |    2434|     234.973|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 298   |   14612|     836.477|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 304   |    7441|      74.212|   1.004/ **|   1.004/ **|   1.005/ **|   1.005/ ** |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 281   |    1347|     207.692|   1.006/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 259   |      86|      63.287|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Eritrea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Eritrea.png)|  15   |       1|       0.286|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 276   |    2024|      20.514|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 291   |     446|      80.700|   1.008/ 87|   1.008/ 83|   1.009/ 79|   1.009/ 78 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 326   |   66920|     997.671|   1.009/ 80|   1.009/ 78|   1.009/ 76|   1.009/ 76 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 292   |      65|      29.857|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 289   |     125|      53.367|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 277   |    4572|    1227.951|   1.024/ 28|   1.024/ 29|   1.024/ 29|   1.024/ 29 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 303   |   28732|     345.552|   1.025/ 27|   1.026/ 26|   1.028/ 25|   1.028/ 25 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 291   |     337|      11.145|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 301   |    6050|     564.097|   1.020/ 35|   1.020/ 35|   1.020/ 35|   1.020/ 35 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 296   |    4916|     296.064|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 266   |      82|       6.737|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 255   |      46|      28.374|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 276   |     236|      20.373|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 286   |    3225|     352.177|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|       0.267|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 297   |   12170|    1245.342|   1.028/ 24|   1.028/ 24|   1.028/ 24|   1.028/ 24 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 301   |  160611|     117.990|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 301   |   22758|      85.265|   1.008/ 91|   1.008/ 92|   1.008/ 92|   1.008/ 92 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 321   |   62082|     744.588|   1.006/ **|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 308   |   13801|     352.728|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 301   |    2239|     454.882|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 292   |    3684|     400.921|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 320   |   73271|    1216.349|   1.012/ 58|   1.012/ 56|   1.013/ 54|   1.013/ 54 |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 293   |     375|     137.442|   1.004/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 328   |    2962|      23.517|   1.013/ 53|   1.014/ 51|   1.014/ 49|   1.014/ 49 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 285   |    9770|     916.330|   1.009/ 75|   1.008/ 91|   1.006/ **|   1.006/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 286   |    2758|     147.604|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 286   |    1947|      40.925|   1.005/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 286   |    1394|     776.446|   1.010/ 67|   1.010/ 66|   1.011/ 66|   1.011/ 65 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 277   |    1004|     227.060|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 278   |    1386|     212.155|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 278   |     670|     351.212|   1.041/ 17|   1.043/ 16|   1.044/ 16|   1.044/ 16 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 302   |    1713|     250.937|   1.010/ 68|   1.010/ 72|   1.009/ 76|   1.009/ 77 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 277   |      83|      18.581|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 279   |    1662|     241.833|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 291   |    1528|     547.100|   1.043/ 16|   1.045/ 15|   1.046/ 15|   1.046/ 15 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 234   |     264|      10.059|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 295   |     519|      15.847|   1.010/ 68|   1.010/ 67|   1.011/ 66|   1.011/ 65 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 283   |     232|      11.464|   1.014/ 49|   1.015/ 47|   1.016/ 44|   1.016/ 44 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 282   |     281|      68.953|   1.008/ 85|   1.009/ 80|   1.009/ 76|   1.009/ 75 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 293   |  128303|    1013.631|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 294   |    3156|    1176.687|   1.008/ 86|   1.008/ 87|   1.008/ 88|   1.008/ 88 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 302   |    9030|     251.718|   1.007/ 98|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 226   |     178|       5.911|   1.007/ 98|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)| 180   |     199|      80.770|   1.012/ 59|   1.013/ 55|   1.013/ 52|   1.014/ 51 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 235   |    2191|      73.047|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 306   |   11665|     668.204|   1.008/ 90|   1.008/ 88|   1.008/ 86|   1.008/ 86 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 283   |      25|       5.026|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 285   |     166|      25.710|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 287   |      83|       3.699|   1.007/ 97|   1.008/ 91|   1.008/ 86|   1.008/ 84 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 289   |    1257|       6.096|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 290   |    2782|    1339.268|   1.014/ 49|   1.014/ 48|   1.014/ 48|   1.014/ 48 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 298   |     431|      80.304|   1.007/ 99|   1.007/ 95|   1.008/ 91|   1.008/ 90 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 281   |    1643|     352.162|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 293   |    9898|      45.128|   1.008/ 89|   1.008/ 85|   1.008/ 82|   1.009/ 81 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 301   |    3881|     919.810|   1.008/ 84|   1.008/ 82|   1.009/ 80|   1.009/ 79 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)| 163   |       9|       1.017|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 291   |    2534|     354.283|   1.004/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 292   |   38107|    1185.982|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 339   |   10475|      96.533|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 300   |   38444|    1001.683|   1.020/ 34|   1.020/ 34|   1.020/ 34|   1.020/ 35 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 295   |    7311|     711.407|   1.018/ 39|   1.018/ 38|   1.019/ 37|   1.019/ 36 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 284   |     249|      90.563|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 290   |   17584|     906.168|   1.012/ 58|   1.012/ 58|   1.012/ 59|   1.012/ 59 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 293   |   58837|     400.947|   1.012/ 56|   1.012/ 56|   1.013/ 55|   1.013/ 55 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 221   |      79|       6.386|   1.020/ 34|   1.021/ 33|   1.022/ 31|   1.023/ 30 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 288   |    6468|     189.026|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 280   |     383|      23.615|   1.006/ **|   1.006/ **|   1.006/ **|   1.007/ ** |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 292   |    3095|     444.390|   1.026/ 27|   1.027/ 26|   1.027/ 25|   1.028/ 25 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 258   |      76|       9.597|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 291   |      29|       5.136|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 284   |    2620|     480.214|   1.037/ 19|   1.038/ 18|   1.039/ 18|   1.039/ 18 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 298   |    3500|    1671.535|   1.021/ 32|   1.022/ 32|   1.022/ 31|   1.022/ 31 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 273   |     130|       8.181|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 285   |   27150|     461.930|   1.009/ 80|   1.009/ 77|   1.009/ 75|   1.009/ 74 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|       1.044|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 309   |   53225|    1130.040|   1.004/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 284   |     261|      11.966|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 299   |    1548|      36.470|   1.005/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 301   |    8186|     791.821|   1.008/ 92|   1.008/ 88|   1.008/ 84|   1.008/ 83 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 307   |    7903|     918.529|   1.019/ 37|   1.019/ 36|   1.020/ 35|   1.020/ 35 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 283   |     725|      41.452|   1.013/ 54|   1.013/ 54|   1.013/ 54|   1.013/ 54 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 281   |      21|       0.376|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 311   |      61|       0.910|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 285   |      73|       9.697|   1.002/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 287   |     140|     102.516|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 293   |    8727|     744.465|   1.012/ 59|   1.010/ 66|   1.009/ 74|   1.009/ 76 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 295   |   20606|     247.799|   1.014/ 51|   1.014/ 49|   1.014/ 48|   1.014/ 48 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 312   |  337247|    1023.375|   1.008/ 91|   1.008/ 88|   1.008/ 86|   1.008/ 85 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)| 166   |     286|       7.106|   1.007/ 99|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 299   |   22696|     541.926|   1.014/ 51|   1.013/ 52|   1.013/ 53|   1.013/ 53 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 292   |     687|      69.445|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 301   |   73122|    1100.650|   1.009/ 80|   1.009/ 78|   1.009/ 75|   1.009/ 75 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 283   |     106|      29.992|   1.025/ 27|   1.027/ 26|   1.028/ 25|   1.028/ 24 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 285   |     656|      19.231|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 285   |    1085|      33.686|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)| 159   |      35|       0.364|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 279   |     385|      21.536|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 289   |     350|      23.089|   1.008/ 85|   1.009/ 81|   1.009/ 78|   1.009/ 77 |

