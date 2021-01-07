# State and Country COVID-19 Analysis #
## Updated: 2021-01-07 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 299   |   36904|    1897.026|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 296   |   28259|     974.575|   1.007/ 99|   1.007/ 97|   1.007/ 97|   1.007/ 96 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 309   |   24467|     619.233|   1.008/ 88|   1.008/ 83|   1.008/ 82|   1.009/ 81 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 305   |   22237|    1035.350|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 303   |   18545|    2087.920|   1.003/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 296   |   17992|    1419.867|   1.011/ 64|   1.011/ 61|   1.011/ 60|   1.012/ 60 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 294   |   14746|    1151.873|   1.013/ 54|   1.014/ 50|   1.014/ 50|   1.014/ 49 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 294   |   12947|    1296.447|   1.010/ 67|   1.011/ 63|   1.011/ 62|   1.011/ 62 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 293   |   12160|    1749.796|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 301   |   11339|    1067.948|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 313   |  340122|    1032.099|   1.008/ 90|   1.008/ 86|   1.008/ 85|   1.008/ 84 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 296   |  197347|     933.472|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 302   |  160897|     118.201|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 294   |  129002|    1019.155|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 321   |   74134|    1230.673|   1.012/ 58|   1.012/ 55|   1.013/ 55|   1.013/ 55 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 302   |   73726|    1109.732|   1.009/ 79|   1.009/ 75|   1.009/ 75|   1.009/ 74 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 327   |   67501|    1006.332|   1.009/ 80|   1.009/ 77|   1.009/ 76|   1.009/ 76 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 294   |   59483|     405.350|   1.012/ 57|   1.012/ 56|   1.012/ 56|   1.012/ 56 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 322   |   62382|     748.184|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 310   |   53433|    1134.453|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 288   |    4867|     992.654|   1.008/ 83|   1.009/ 80|   1.009/ 80|   1.009/ 80 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 288   |     227|     310.973|   1.010/ 69|   1.010/ 67|   1.010/ 67|   1.010/ 67 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 292   |    8427|    1157.814|   1.009/ 80|   1.009/ 74|   1.009/ 74|   1.009/ 73 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 289   |    3849|    1275.512|   1.011/ 62|   1.011/ 62|   1.011/ 62|   1.011/ 62 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 309   |   24467|     619.233|   1.008/ 88|   1.008/ 83|   1.008/ 82|   1.009/ 81 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 299   |    4699|     816.019|   1.012/ 58|   1.013/ 55|   1.013/ 55|   1.013/ 54 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 294   |    5802|    1627.376|   1.006/ **|   1.007/ **|   1.007/ **|   1.007/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 287   |     912|     936.228|   1.005/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 305   |   22237|    1035.350|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 301   |   11339|    1067.948|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 282   |     319|     225.057|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 287   |    1534|     858.291|   1.013/ 53|   1.013/ 52|   1.013/ 52|   1.013/ 52 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 296   |   17992|    1419.867|   1.011/ 64|   1.011/ 61|   1.011/ 60|   1.012/ 60 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 297   |    8330|    1237.276|   1.013/ 55|   1.013/ 53|   1.013/ 53|   1.013/ 52 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 288   |    4017|    1273.205|   1.011/ 62|   1.011/ 61|   1.011/ 61|   1.011/ 61 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 300   |    2943|    1010.036|   1.015/ 47|   1.015/ 46|   1.015/ 46|   1.015/ 46 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 297   |    2722|     609.331|   1.010/ 66|   1.011/ 65|   1.011/ 64|   1.011/ 64 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 299   |    7414|    1594.764|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 286   |     325|     241.794|   1.014/ 48|   1.016/ 45|   1.016/ 44|   1.016/ 44 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 294   |    5693|     941.633|   1.008/ 91|   1.008/ 85|   1.008/ 84|   1.008/ 83 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 293   |   12160|    1749.796|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 294   |   12947|    1296.447|   1.010/ 67|   1.011/ 63|   1.011/ 62|   1.011/ 62 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 292   |    5551|     984.251|   1.013/ 52|   1.014/ 50|   1.014/ 50|   1.014/ 50 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 294   |    4768|    1602.090|   1.007/ 99|   1.007/ 95|   1.007/ 95|   1.007/ 94 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 294   |    6025|     981.628|   1.011/ 63|   1.011/ 62|   1.011/ 62|   1.011/ 62 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 286   |    1234|    1154.260|   1.012/ 59|   1.011/ 64|   1.011/ 65|   1.011/ 66 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 285   |    1797|     928.857|   1.014/ 50|   1.014/ 50|   1.014/ 50|   1.014/ 50 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 297   |    3009|     976.795|   1.011/ 62|   1.012/ 59|   1.012/ 58|   1.012/ 58 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 290   |     684|     503.342|   1.011/ 62|   1.012/ 57|   1.012/ 57|   1.012/ 56 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 303   |   18545|    2087.920|   1.003/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 288   |    2514|    1199.001|   1.016/ 42|   1.017/ 40|   1.017/ 40|   1.017/ 40 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 299   |   36904|    1897.026|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 288   |    6963|     663.905|   1.007/ 93|   1.007/ 93|   1.007/ 93|   1.007/ 92 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 286   |    1703|    2235.014|   1.009/ 81|   1.007/ 99|   1.007/ **|   1.007/ ** |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 293   |    8771|     750.320|   1.010/ 67|   1.011/ 64|   1.011/ 63|   1.011/ 63 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 294   |    2569|     649.245|   1.011/ 64|   1.011/ 63|   1.011/ 63|   1.011/ 63 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 298   |    1480|     350.853|   1.014/ 50|   1.014/ 48|   1.015/ 47|   1.015/ 47 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 294   |   14746|    1151.873|   1.013/ 54|   1.014/ 50|   1.014/ 50|   1.014/ 49 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 292   |    1573|     492.632|   1.009/ 75|   1.009/ 75|   1.009/ 75|   1.009/ 74 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 285   |    1741|    1643.439|   1.009/ 75|   1.010/ 70|   1.010/ 69|   1.010/ 69 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 297   |    5360|    1041.002|   1.006/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 302   |    1880|    2124.885|   1.015/ 46|   1.014/ 48|   1.014/ 48|   1.014/ 48 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 292   |    7186|    1051.602|   1.013/ 52|   1.013/ 51|   1.014/ 51|   1.014/ 51 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 296   |   28259|     974.575|   1.007/ 99|   1.007/ 97|   1.007/ 97|   1.007/ 96 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 291   |    1336|     416.879|   1.013/ 55|   1.013/ 54|   1.013/ 53|   1.013/ 53 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 293   |      63|     100.787|   1.017/ 40|   1.019/ 37|   1.019/ 36|   1.019/ 36 |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 299   |    5020|     588.115|   1.006/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 313   |    3350|     439.966|   1.005/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 283   |    1393|     777.093|   1.019/ 36|   1.020/ 34|   1.020/ 34|   1.020/ 34 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 293   |    6010|    1032.157|   1.014/ 49|   1.014/ 49|   1.014/ 49|   1.014/ 49 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 269   |     527|     910.609|   1.024/ 29|   1.024/ 29|   1.024/ 29|   1.024/ 29 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 291   |    2177|      67.543|   1.007/ 93|   1.008/ 88|   1.008/ 87|   1.008/ 86 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 302   |    1284|     451.190|   1.013/ 53|   1.013/ 53|   1.013/ 53|   1.013/ 53 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 301   |    2889|      67.182|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 284   |     455|      14.616|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 305   |   53452|    1189.433|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 287   |    3212|    1085.892|   1.011/ 65|   1.010/ 66|   1.010/ 67|   1.010/ 67 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 312   |     929|      36.153|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 301   |    6982|     784.264|   1.027/ 25|   1.029/ 24|   1.029/ 24|   1.029/ 24 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 300   |    2686|     266.855|   1.024/ 28|   1.025/ 27|   1.026/ 27|   1.026/ 27 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 297   |     381|     246.730|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 295   |    7750|      46.003|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 282   |    1453|     154.414|   1.007/ **|   1.007/ **|   1.007/ **|   1.007/ ** |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 302   |   20936|    1816.633|   1.006/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 276   |      45|       3.813|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 284   |    9377|     817.559|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 292   |    4856|    1471.000|   1.016/ 42|   1.016/ 43|   1.016/ 43|   1.016/ 43 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 282   |      46|      19.690|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 296   |  197347|     933.472|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 302   |    9216|    1325.810|   1.026/ 26|   1.027/ 26|   1.027/ 26|   1.027/ 26 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 295   |      79|       3.788|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 269   |       1|       0.091|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 288   |     451|      16.995|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 304   |   15214|     400.383|   1.009/ 74|   1.010/ 70|   1.010/ 69|   1.010/ 68 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 229   |      63|      11.513|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 254   |     106|       6.532|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 291   |   17006|     890.034|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 302   |    4767|       3.400|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 291   |   44790|     906.750|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 294   |    2432|     480.777|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 294   |    4902|    1202.593|   1.031/ 22|   1.031/ 22|   1.031/ 22|   1.031/ 22 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 295   |     145|      12.957|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 299   |     989|     169.889|   1.011/ 61|   1.012/ 57|   1.012/ 56|   1.012/ 56 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 296   |    2436|     235.194|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 299   |   14606|     836.141|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 305   |    7480|      74.592|   1.004/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 282   |    1355|     208.893|   1.006/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 260   |      86|      63.311|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Eritrea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Eritrea.png)|  16   |       1|       0.286|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 277   |    2030|      20.575|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 292   |     512|      92.538|   1.008/ 86|   1.009/ 79|   1.009/ 78|   1.009/ 77 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 327   |   67501|    1006.332|   1.009/ 80|   1.009/ 77|   1.009/ 76|   1.009/ 76 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 293   |      65|      29.955|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 290   |     125|      53.397|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 278   |    4666|    1253.132|   1.023/ 29|   1.023/ 30|   1.023/ 30|   1.023/ 30 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 304   |   29480|     354.537|   1.026/ 27|   1.028/ 25|   1.028/ 25|   1.028/ 24 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 292   |     338|      11.153|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 302   |    6177|     575.938|   1.019/ 37|   1.019/ 36|   1.019/ 36|   1.019/ 36 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 297   |    4935|     297.223|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 267   |      82|       6.744|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 256   |      46|      28.395|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 277   |     236|      20.375|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 287   |    3231|     352.780|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|       0.267|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 298   |   12425|    1271.353|   1.027/ 25|   1.027/ 25|   1.027/ 25|   1.027/ 25 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 302   |  160897|     118.201|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 302   |   22950|      85.983|   1.008/ 91|   1.008/ 91|   1.008/ 91|   1.008/ 91 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 322   |   62382|     748.184|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 309   |   13802|     352.746|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 302   |    2246|     456.292|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 293   |    3692|     401.857|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 321   |   74134|    1230.673|   1.012/ 58|   1.012/ 55|   1.013/ 55|   1.013/ 55 |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 294   |     376|     137.785|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 329   |    3006|      23.866|   1.013/ 52|   1.014/ 49|   1.014/ 48|   1.014/ 48 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 286   |   10058|     943.414|   1.009/ 81|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 287   |    2768|     148.130|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 287   |    1954|      41.081|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 287   |    1407|     783.697|   1.010/ 69|   1.010/ 68|   1.010/ 68|   1.010/ 68 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 278   |    1005|     227.325|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 279   |    1389|     212.581|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 279   |     699|     366.321|   1.041/ 17|   1.043/ 16|   1.043/ 16|   1.044/ 16 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 303   |    1728|     253.110|   1.010/ 68|   1.009/ 75|   1.009/ 76|   1.009/ 77 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 278   |      83|      18.583|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 280   |    1673|     243.476|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 292   |    1589|     568.762|   1.044/ 16|   1.046/ 15|   1.046/ 15|   1.046/ 15 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 235   |     264|      10.065|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 296   |     523|      15.970|   1.010/ 67|   1.011/ 65|   1.011/ 65|   1.011/ 64 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 284   |     236|      11.666|   1.014/ 50|   1.015/ 45|   1.015/ 45|   1.016/ 44 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 283   |     288|      70.629|   1.009/ 77|   1.010/ 70|   1.010/ 69|   1.010/ 68 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 294   |  129002|    1019.155|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 295   |    3180|    1185.702|   1.008/ 87|   1.008/ 89|   1.008/ 89|   1.008/ 89 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 303   |    9074|     252.960|   1.007/ **|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 227   |     179|       5.949|   1.007/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)| 181   |     201|      81.655|   1.013/ 55|   1.014/ 49|   1.014/ 48|   1.015/ 47 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 236   |    2201|      73.372|   1.005/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 307   |   11761|     673.740|   1.008/ 88|   1.008/ 85|   1.008/ 84|   1.008/ 84 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 284   |      25|       5.026|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 286   |     166|      25.733|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 288   |      83|       3.704|   1.007/ 94|   1.008/ 84|   1.008/ 83|   1.008/ 82 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 290   |    1261|       6.119|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 291   |    2816|    1355.722|   1.014/ 50|   1.014/ 50|   1.014/ 50|   1.014/ 50 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 299   |     435|      80.987|   1.007/ 98|   1.008/ 91|   1.008/ 90|   1.008/ 89 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 282   |    1644|     352.498|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 294   |    9971|      45.461|   1.008/ 89|   1.008/ 83|   1.008/ 82|   1.008/ 82 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 302   |    3915|     928.032|   1.008/ 83|   1.009/ 78|   1.009/ 78|   1.009/ 77 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)| 164   |       9|       1.023|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 292   |    2550|     356.525|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 293   |   38149|    1187.268|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 340   |   10498|      96.747|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 301   |   39248|    1022.641|   1.020/ 35|   1.019/ 36|   1.019/ 36|   1.019/ 36 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 296   |    7412|     721.259|   1.017/ 40|   1.018/ 38|   1.018/ 38|   1.018/ 38 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 285   |     249|      90.594|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 291   |   17775|     915.980|   1.012/ 59|   1.011/ 60|   1.011/ 61|   1.011/ 61 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 294   |   59483|     405.350|   1.012/ 57|   1.012/ 56|   1.012/ 56|   1.012/ 56 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 222   |      81|       6.530|   1.021/ 32|   1.023/ 29|   1.024/ 29|   1.024/ 29 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 289   |    6474|     189.185|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 281   |     386|      23.802|   1.006/ **|   1.007/ **|   1.007/ **|   1.007/ ** |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 293   |    3177|     456.193|   1.025/ 27|   1.027/ 26|   1.027/ 26|   1.027/ 25 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 259   |      76|       9.602|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 292   |      29|       5.138|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 285   |    2705|     495.662|   1.038/ 18|   1.039/ 17|   1.040/ 17|   1.040/ 17 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 299   |    3585|    1711.786|   1.021/ 33|   1.021/ 32|   1.021/ 32|   1.021/ 32 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 274   |     130|       8.207|   1.001/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 286   |   27437|     466.810|   1.009/ 76|   1.010/ 71|   1.010/ 71|   1.010/ 70 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|       1.044|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 310   |   53433|    1134.453|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 285   |     265|      12.174|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 300   |    1555|      36.631|   1.005/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 302   |    8251|     798.075|   1.008/ 88|   1.008/ 81|   1.009/ 81|   1.009/ 80 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 308   |    8008|     930.732|   1.019/ 37|   1.019/ 35|   1.020/ 35|   1.020/ 35 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 284   |     736|      42.070|   1.012/ 56|   1.012/ 56|   1.012/ 56|   1.012/ 56 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 282   |      21|       0.376|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 312   |      61|       0.911|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 286   |      73|       9.718|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 288   |     140|     102.566|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 294   |    8806|     751.246|   1.011/ 60|   1.009/ 73|   1.009/ 76|   1.009/ 78 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 296   |   20878|     251.070|   1.014/ 51|   1.014/ 49|   1.014/ 48|   1.014/ 48 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 313   |  340122|    1032.099|   1.008/ 90|   1.008/ 86|   1.008/ 85|   1.008/ 84 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)| 167   |     289|       7.182|   1.008/ 89|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 300   |   22988|     548.910|   1.013/ 52|   1.013/ 54|   1.013/ 54|   1.013/ 55 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 293   |     690|      69.793|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 302   |   73726|    1109.732|   1.009/ 79|   1.009/ 75|   1.009/ 75|   1.009/ 74 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 284   |     107|      30.306|   1.026/ 27|   1.028/ 25|   1.028/ 24|   1.028/ 24 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 286   |     656|      19.226|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 286   |    1089|      33.800|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)| 160   |      35|       0.364|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 280   |     387|      21.635|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 290   |     355|      23.392|   1.008/ 83|   1.009/ 77|   1.009/ 77|   1.009/ 76 |

