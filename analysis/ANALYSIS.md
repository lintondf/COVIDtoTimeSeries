# State and Country COVID-19 Analysis #
## Updated: 2020-06-04 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# Notes #

- Expect discontinuities in the US around 4/14/2020 as the [CDC](CDC "https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html")  expanded the definition of a COVID-19 death.  
- There is also some weekly pattern to reporting with lower values on the weekend followed by higher values subsequently, at least in some places.
- The Y axis upper limit for DDGR charts was lowered from 2.0 to 1.5 on 4/28 and then to 1.25 on 5/26/20 to better show current lower values.  

# Ten US States with Highest Death Tolls #

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. One per million is 0.0001%.  1% is 10,000 per million.

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDeathRates.png)

Daily Death Growth Rate (DDGR) in the 10 US States with the highest death tolls.

DDGR is the cube root of Arnold Kling's [Three Day Death Reproduction Rate (3DDRR)](http://www.arnoldkling.com/blog/the-3ddrr/).  The 3DDRR is calculated by dividing the cumulative total number of deaths on a given day by the  cumulative total number of deaths three days previously.  Taking the cube root converts this to the geometric mean for the three days.  These values are LOWESS filtered to generate a local-error minimizing non-parametric trend.

If deaths remain constant over the three days, the DDGR equals one.  A value of 2 would indicate that the number of deaths doubles every day.

![US States with Highest Death Toll - Daily Death Growth Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  82   |   30571|     1571.49|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  86   |   12388|     1394.69|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  76   |    7329|     1054.63|   1.012/ 56|   1.010/ 72|   1.009/ 77|   1.008/ 83 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  77   |    5980|      467.10|   1.012/ 55|   1.008/ 86|   1.007/ 99|   1.006/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  79   |    5883|      464.24|   1.016/ 43|   1.012/ 58|   1.011/ 64|   1.010/ 71 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  77   |    5669|      567.60|   1.007/ 99|   1.005/ **|   1.005/ **|   1.005/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  92   |    4579|      115.89|   1.016/ 42|   1.014/ 50|   1.013/ 53|   1.012/ 56 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  77   |    4149|     1163.86|   1.009/ 76|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  82   |    2926|      629.41|   1.007/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  77   |    2736|      452.53|   1.015/ 45|   1.012/ 59|   1.011/ 63|   1.010/ 69 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  96   |  112303|      340.78|   1.009/ 73|   1.007/ **|   1.006/ **|   1.006/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  85   |   40353|      607.41|   1.008/ 91|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 104   |   34529|      573.20|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  79   |   34952|      165.32|   1.039/ 18|   1.033/ 21|   1.032/ 22|   1.031/ 23 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 110   |   30091|      448.61|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  93   |   27956|      593.54|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  77   |   11977|       94.63|   1.045/ 15|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  85   |    9708|      842.40|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  87   |    8797|      105.79|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 105   |    8052|       96.57|   1.007/ 94|   1.007/ **|   1.007/ **|   1.007/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  71   |     674|      137.40|   1.017/ 40|   1.014/ 49|   1.013/ 51|   1.013/ 54 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  71   |      10|       13.69|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  75   |    1007|      138.28|   1.020/ 35|   1.015/ 47|   1.014/ 51|   1.012/ 56 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  72   |     140|       46.37|   1.019/ 37|   1.019/ 36|   1.019/ 36|   1.019/ 36 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  92   |    4579|      115.89|   1.016/ 42|   1.014/ 50|   1.013/ 53|   1.012/ 56 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  82   |    1569|      272.45|   1.013/ 54|   1.010/ 72|   1.009/ 79|   1.008/ 88 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  77   |    4149|     1163.86|   1.009/ 76|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  70   |     394|      404.98|   1.015/ 45|   1.010/ 67|   1.009/ 76|   1.008/ 88 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  88   |    2660|      123.85|   1.014/ 50|   1.011/ 63|   1.010/ 67|   1.010/ 72 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  84   |    2177|      205.02|   1.015/ 45|   1.014/ 49|   1.014/ 50|   1.013/ 52 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  65   |      17|       12.01|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  70   |      85|       47.53|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  79   |    5883|      464.24|   1.016/ 43|   1.012/ 58|   1.011/ 64|   1.010/ 71 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  80   |    2305|      342.45|   1.012/ 57|   1.008/ 82|   1.008/ 92|   1.007/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  71   |     608|      192.55|   1.028/ 25|   1.023/ 30|   1.022/ 32|   1.020/ 34 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  83   |     229|       78.55|   1.007/ 98|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  80   |     457|      102.37|   1.015/ 47|   1.013/ 52|   1.013/ 53|   1.013/ 55 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  82   |    2926|      629.41|   1.007/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  69   |      93|       68.86|   1.018/ 38|   1.020/ 34|   1.021/ 34|   1.021/ 33 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  77   |    2736|      452.53|   1.015/ 45|   1.012/ 59|   1.011/ 63|   1.010/ 69 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  76   |    7329|     1054.63|   1.012/ 56|   1.010/ 72|   1.009/ 77|   1.008/ 83 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  77   |    5669|      567.60|   1.007/ 99|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  75   |    1146|      203.22|   1.024/ 29|   1.020/ 35|   1.019/ 37|   1.018/ 38 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  77   |     803|      269.86|   1.023/ 30|   1.020/ 34|   1.020/ 35|   1.019/ 36 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  77   |     821|      133.83|   1.015/ 45|   1.012/ 58|   1.011/ 63|   1.010/ 68 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  69   |      17|       15.96|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  68   |     184|       95.09|   1.020/ 35|   1.014/ 51|   1.012/ 57|   1.010/ 66 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  80   |     442|      143.36|   1.010/ 68|   1.007/ 95|   1.007/ **|   1.006/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  73   |     273|      201.01|   1.024/ 28|   1.019/ 35|   1.018/ 38|   1.017/ 40 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  86   |   12388|     1394.69|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  71   |     391|      186.53|   1.020/ 35|   1.015/ 47|   1.013/ 51|   1.012/ 57 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  82   |   30571|     1571.49|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  71   |    1001|       95.41|   1.022/ 32|   1.020/ 34|   1.020/ 35|   1.020/ 35 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  69   |      67|       87.67|   1.023/ 30|   1.020/ 35|   1.019/ 36|   1.018/ 38 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  76   |    2382|      203.82|   1.018/ 37|   1.015/ 45|   1.014/ 48|   1.014/ 51 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  77   |     345|       87.13|   1.009/ 78|   1.008/ 89|   1.008/ 91|   1.007/ 94 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  81   |     161|       38.07|   1.007/ 98|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  77   |    5980|      467.10|   1.012/ 55|   1.008/ 86|   1.007/ 99|   1.006/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  75   |     140|       43.80|   1.008/ 87|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  68   |     769|      725.79|   1.022/ 31|   1.020/ 34|   1.020/ 35|   1.019/ 36 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  80   |     521|      101.27|   1.015/ 46|   1.013/ 53|   1.012/ 56|   1.012/ 58 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  85   |      68|       76.73|   1.020/ 35|   1.015/ 45|   1.014/ 48|   1.013/ 52 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  75   |     392|       57.38|   1.015/ 46|   1.013/ 53|   1.013/ 55|   1.012/ 57 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  79   |    1815|       62.58|   1.015/ 45|   1.012/ 59|   1.011/ 64|   1.010/ 69 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  74   |     122|       37.99|   1.020/ 35|   1.016/ 43|   1.015/ 46|   1.014/ 49 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  76   |      55|       88.43|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  82   |    1500|      175.78|   1.019/ 36|   1.016/ 44|   1.015/ 47|   1.014/ 49 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  96   |    1171|      153.74|   1.007/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  66   |      80|       44.63|   1.010/ 71|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  76   |     618|      106.11|   1.018/ 38|   1.018/ 39|   1.017/ 39|   1.017/ 40 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  52   |      18|       31.47|   1.034/ 20|   1.034/ 20|   1.034/ 20|   1.034/ 20 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  74   |     296|        9.19|   1.032/ 22|   1.028/ 25|   1.027/ 26|   1.026/ 27 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  85   |      33|       11.60|   1.003/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  84   |     678|       15.76|   1.012/ 56|   1.012/ 57|   1.012/ 57|   1.012/ 57 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  67   |       4|        0.14|   1.029/ 24|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  88   |     596|       13.26|   1.026/ 27|   1.025/ 28|   1.024/ 28|   1.024/ 29 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  70   |     152|       51.38|   1.067/ 10|   1.076/  9|   1.079/  9|   1.081/  8 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  95   |     105|        4.07|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  84   |     671|       75.34|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  83   |      70|        6.98|   1.041/ 17|   1.044/ 16|   1.045/ 15|   1.046/ 15 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  80   |      19|       12.36|   1.037/ 19|   1.041/ 17|   1.042/ 16|   1.043/ 16 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  78   |     755|        4.48|   1.049/ 14|   1.048/ 14|   1.048/ 14|   1.048/ 14 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  65   |     254|       27.04|   1.024/ 29|   1.021/ 33|   1.020/ 34|   1.019/ 36 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  85   |    9708|      842.40|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  59   |       3|        0.28|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  67   |     391|       34.08|   1.048/ 14|   1.046/ 15|   1.046/ 15|   1.045/ 15 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  75   |     167|       50.62|   1.009/ 74|   1.003/ **|   1.002/ **|   1.000/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  65   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  79   |   34952|      165.32|   1.039/ 18|   1.033/ 21|   1.032/ 22|   1.031/ 23 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  85   |     153|       22.03|   1.016/ 43|   1.013/ 53|   1.012/ 57|   1.011/ 61 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  78   |      54|        2.58|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  52   |       1|        0.09|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  71   |     205|        7.72|   1.022/ 31|   1.021/ 32|   1.021/ 32|   1.021/ 33 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  87   |    7940|      208.94|   1.014/ 50|   1.010/ 71|   1.009/ 78|   1.008/ 88 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  12   |       4|        0.73|   1.000/ --|   1.587/  1|   1.587/  1|   1.260/  2 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  37   |      67|        4.14|   1.012/ 57|   1.006/ **|   1.005/ **|   1.003/ ** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  74   |    1256|       65.71|   1.062/ 11|   1.065/ 11|   1.065/ 10|   1.066/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  85   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  74   |    1026|       20.78|   1.036/ 19|   1.037/ 19|   1.037/ 18|   1.037/ 18 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  77   |      11|        2.19|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  77   |     106|       25.91|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  78   |      85|        7.55|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  82   |     587|      100.73|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  79   |     521|       50.25|   1.010/ 66|   1.009/ 76|   1.009/ 79|   1.008/ 82 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  82   |    3884|      222.35|   1.014/ 51|   1.006/ **|   1.005/ **|   1.003/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  88   |    1031|       10.29|   1.034/ 20|   1.036/ 19|   1.036/ 19|   1.037/ 19 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  65   |      52|        7.96|   1.037/ 18|   1.032/ 21|   1.031/ 22|   1.030/ 23 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  43   |      13|        9.51|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  60   |       8|        0.08|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  75   |     328|       59.38|   1.004/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 110   |   30091|      448.61|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  76   |      19|        8.67|   1.051/ 13|   1.056/ 12|   1.057/ 12|   1.059/ 12 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  73   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  61   |      12|        3.35|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  87   |    8797|      105.79|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  75   |      39|        1.30|   1.018/ 38|   1.014/ 51|   1.012/ 56|   1.011/ 61 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  85   |     182|       16.99|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  80   |     122|        7.33|   1.083/  8|   1.091/  7|   1.094/  7|   1.096/  7 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  50   |      24|        1.98|   1.020/ 34|   1.013/ 53|   1.011/ 61|   1.010/ 71 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  39   |       9|        5.32|   1.033/ 21|   1.013/ 54|   1.008/ 91|   1.002/ ** |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  60   |      47|        4.10|   1.055/ 12|   1.060/ 11|   1.061/ 11|   1.062/ 11 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  70   |     233|       25.49|   1.029/ 23|   1.028/ 24|   1.028/ 24|   1.028/ 25 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  81   |     550|       56.24|   1.009/ 78|   1.006/ **|   1.006/ **|   1.005/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  85   |    6243|        4.59|   1.041/ 17|   1.038/ 18|   1.038/ 18|   1.037/ 18 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  85   |    1719|        6.44|   1.023/ 29|   1.023/ 29|   1.023/ 29|   1.023/ 29 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 105   |    8052|       96.57|   1.007/ 94|   1.007/ **|   1.007/ **|   1.007/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  92   |     208|        5.32|   1.041/ 17|   1.047/ 15|   1.048/ 14|   1.050/ 14 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  85   |    1703|      345.98|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  75   |     294|       31.95|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 104   |   34529|      573.20|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  77   |       9|        3.35|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 112   |    1042|        8.27|   1.010/ 71|   1.005/ **|   1.003/ **|   1.002/ ** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  69   |       9|        0.84|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  71   |      41|        2.20|   1.020/ 34|   1.025/ 27|   1.026/ 26|   1.028/ 25 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  70   |      72|        1.50|   1.031/ 22|   1.029/ 24|   1.029/ 24|   1.029/ 24 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  70   |      30|       16.90|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  61   |     247|       55.84|   1.045/ 15|   1.035/ 20|   1.033/ 21|   1.030/ 23 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  62   |      17|        2.67|   1.018/ 39|   1.020/ 35|   1.020/ 34|   1.021/ 33 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  62   |      25|       13.10|   1.011/ 65|   1.008/ 86|   1.007/ 95|   1.007/ ** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  86   |      27|        3.91|   1.002/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  61   |      29|        6.49|   1.013/ 52|   1.011/ 65|   1.010/ 70|   1.009/ 77 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  63   |       5|        0.73|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  75   |      73|       26.19|   1.013/ 52|   1.012/ 57|   1.012/ 59|   1.011/ 60 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  18   |       2|        0.08|   1.175/  4|   1.200/  3|   1.071/ 10|   1.000/ -- |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  79   |     117|        3.57|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  67   |      85|        4.22|   1.025/ 27|   1.019/ 36|   1.017/ 40|   1.016/ 44 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  66   |      34|        8.34|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  77   |   11977|       94.63|   1.045/ 15|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  78   |     327|      122.05|   1.023/ 30|   1.020/ 35|   1.019/ 37|   1.018/ 38 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  86   |     208|        5.80|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  10   |       2|        0.07|   1.260/  2|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  19   |       9|        0.31|   1.116/  6|   1.107/  6|   1.085/  8|   1.061/ 11 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  90   |    6137|      351.55|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  67   |      22|        4.42|   1.003/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  69   |      50|        7.70|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  71   |      69|        3.10|   1.010/ 70|   1.005/ **|   1.003/ **|   1.002/ ** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  73   |     321|        1.56|   1.033/ 21|   1.030/ 23|   1.029/ 24|   1.028/ 24 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  74   |     139|       67.14|   1.023/ 30|   1.026/ 27|   1.027/ 26|   1.027/ 25 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  82   |     241|       44.82|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  65   |      59|       12.59|   1.062/ 11|   1.065/ 10|   1.066/ 10|   1.067/ 10 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  77   |    1651|        7.53|   1.039/ 17|   1.039/ 18|   1.039/ 18|   1.039/ 18 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  85   |     359|       85.14|   1.015/ 45|   1.014/ 50|   1.014/ 51|   1.013/ 52 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  75   |      11|        1.57|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  76   |    5149|      160.24|   1.035/ 19|   1.031/ 22|   1.030/ 23|   1.029/ 24 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 123   |    1060|        9.77|   1.009/ 73|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  84   |    1140|       29.69|   1.010/ 68|   1.008/ 90|   1.007/ 98|   1.006/ ** |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  79   |    1456|      141.66|   1.010/ 70|   1.009/ 73|   1.009/ 74|   1.009/ 74 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  68   |      44|       15.90|   1.068/ 10|   1.078/  9|   1.080/  9|   1.082/  8 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  74   |    1334|       68.74|   1.009/ 76|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  77   |    5359|       36.52|   1.040/ 17|   1.038/ 18|   1.037/ 18|   1.037/ 19 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  72   |     554|       16.18|   1.038/ 18|   1.040/ 17|   1.040/ 17|   1.041/ 17 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  64   |      48|        2.95|   1.029/ 24|   1.020/ 35|   1.017/ 40|   1.015/ 46 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  76   |     250|       35.89|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  42   |      49|        6.20|   1.022/ 31|   1.008/ 88|   1.004/ **|   1.000/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  75   |      24|        4.24|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  68   |      28|        5.20|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  82   |     110|       52.67|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  57   |      80|        5.05|   1.023/ 30|   1.024/ 28|   1.025/ 28|   1.025/ 27 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  69   |     816|       13.88|   1.062/ 11|   1.062/ 11|   1.061/ 11|   1.061/ 11 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  93   |   27956|      593.54|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  68   |      11|        0.49|   1.015/ 47|   1.020/ 35|   1.021/ 33|   1.023/ 31 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  83   |     316|        7.44|   1.066/ 10|   1.066/ 10|   1.066/ 10|   1.066/ 10 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  85   |    4662|      450.98|   1.012/ 60|   1.009/ 75|   1.009/ 79|   1.008/ 85 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  91   |    1950|      226.69|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  67   |       5|        0.29|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  65   |      21|        0.38|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  95   |      58|        0.87|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  69   |      14|        1.80|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  71   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  77   |      49|        4.18|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  79   |    4696|       56.47|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  96   |  112303|      340.78|   1.009/ 73|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  83   |     799|       19.07|   1.022/ 32|   1.017/ 40|   1.016/ 43|   1.015/ 47 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  76   |     284|       28.74|   1.010/ 71|   1.004/ **|   1.003/ **|   1.001/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  85   |   40353|      607.41|   1.008/ 91|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  67   |      23|        6.61|   1.009/ 76|   1.009/ 80|   1.008/ 82|   1.008/ 83 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  69   |      16|        0.46|   1.017/ 42|   1.016/ 42|   1.016/ 42|   1.016/ 42 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  69   |      11|        0.34|   1.049/ 14|   1.066/ 10|   1.071/ 10|   1.075/  9 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  63   |       7|        0.39|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  73   |       4|        0.26|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |

