# State and Country COVID-19 Analysis #
## Updated: 2020-06-21 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  99   |   31378|    1612.966|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 103   |   13216|    1487.941|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  93   |    8048|    1158.050|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  96   |    6877|     542.690|   1.009/ 77|   1.007/ 99|   1.007/ **|   1.006/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  94   |    6634|     518.195|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  94   |    6259|     626.727|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 109   |    5645|     142.858|   1.013/ 55|   1.011/ 61|   1.011/ 63|   1.011/ 65 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  94   |    4362|    1223.540|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 105   |    3199|     148.938|   1.011/ 61|   1.010/ 68|   1.010/ 69|   1.010/ 71 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  99   |    3142|     675.891|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 113   |  123533|     374.861|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  96   |   53460|     252.872|   1.024/ 28|   1.021/ 33|   1.020/ 35|   1.019/ 37 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 102   |   43573|     655.864|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 121   |   35132|     583.221|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 127   |   30181|     449.946|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 110   |   27329|     580.236|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  94   |   22286|     176.066|   1.034/ 20|   1.031/ 22|   1.030/ 23|   1.029/ 23 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 102   |   12794|       9.399|   1.037/ 19|   1.035/ 19|   1.035/ 20|   1.035/ 20 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 102   |    9812|     851.386|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 122   |    9316|     111.728|   1.010/ 70|   1.010/ 68|   1.010/ 67|   1.010/ 67 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  88   |     848|     172.910|   1.014/ 50|   1.013/ 54|   1.013/ 55|   1.012/ 56 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  88   |      12|      16.398|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  92   |    1344|     184.622|   1.019/ 37|   1.018/ 37|   1.018/ 38|   1.018/ 38 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  89   |     210|      69.614|   1.028/ 25|   1.030/ 23|   1.031/ 23|   1.031/ 22 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 109   |    5645|     142.858|   1.013/ 55|   1.011/ 61|   1.011/ 63|   1.011/ 65 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  99   |    1707|     296.430|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  94   |    4362|    1223.540|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  87   |     450|     461.946|   1.007/ 94|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 105   |    3199|     148.938|   1.011/ 61|   1.010/ 68|   1.010/ 69|   1.010/ 71 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 101   |    2685|     252.903|   1.013/ 53|   1.013/ 55|   1.012/ 56|   1.012/ 56 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  82   |      17|      12.007|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  87   |      89|      50.053|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  96   |    6877|     542.690|   1.009/ 77|   1.007/ 99|   1.007/ **|   1.006/ ** |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  97   |    2593|     385.211|   1.007/ 95|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  88   |     732|     231.952|   1.009/ 73|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 100   |     257|      88.385|   1.007/ 98|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  97   |     542|     121.287|   1.009/ 76|   1.008/ 90|   1.007/ 94|   1.007/ 98 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  99   |    3142|     675.891|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  86   |     108|      80.429|   1.005/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  94   |    3172|     524.708|   1.008/ 87|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  93   |    8048|    1158.050|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  94   |    6259|     626.727|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  92   |    1487|     263.644|   1.013/ 52|   1.010/ 66|   1.010/ 71|   1.009/ 77 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  94   |    1001|     336.314|   1.011/ 62|   1.008/ 82|   1.008/ 90|   1.007/ 99 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  94   |     967|     157.615|   1.012/ 58|   1.011/ 60|   1.011/ 61|   1.011/ 62 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  86   |      20|      18.417|   1.010/ 69|   1.011/ 60|   1.012/ 58|   1.012/ 56 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  85   |     245|     126.814|   1.020/ 35|   1.020/ 35|   1.020/ 35|   1.020/ 35 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  97   |     491|     159.323|   1.007/ **|   1.006/ **|   1.005/ **|   1.005/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  90   |     358|     263.565|   1.014/ 49|   1.011/ 62|   1.010/ 66|   1.010/ 71 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 103   |   13216|    1487.941|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  88   |     479|     228.317|   1.013/ 55|   1.011/ 63|   1.011/ 66|   1.010/ 68 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  99   |   31378|    1612.966|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  88   |    1262|     120.304|   1.012/ 55|   1.010/ 66|   1.010/ 69|   1.009/ 73 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  86   |      81|     106.828|   1.008/ 92|   1.004/ **|   1.002/ **|   1.001/ ** |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  93   |    2786|     238.300|   1.009/ 78|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  94   |     376|      95.140|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  98   |     186|      44.138|   1.011/ 65|   1.011/ 61|   1.011/ 60|   1.012/ 59 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  94   |    6634|     518.195|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  92   |     151|      47.346|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  85   |     929|     877.209|   1.011/ 65|   1.008/ 86|   1.007/ 93|   1.007/ ** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  97   |     657|     127.640|   1.013/ 54|   1.012/ 58|   1.012/ 59|   1.011/ 60 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 102   |      84|      94.896|   1.014/ 48|   1.013/ 53|   1.013/ 55|   1.012/ 57 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  92   |     524|      76.734|   1.017/ 40|   1.017/ 40|   1.018/ 39|   1.018/ 39 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  96   |    2192|      75.586|   1.013/ 54|   1.012/ 57|   1.012/ 57|   1.012/ 58 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  91   |     157|      48.819|   1.017/ 40|   1.017/ 41|   1.017/ 41|   1.017/ 42 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  93   |      56|      89.175|   1.001/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  99   |    1702|     199.409|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 113   |    1271|     166.896|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  83   |      92|      51.115|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  93   |     760|     130.582|   1.011/ 63|   1.010/ 72|   1.009/ 75|   1.009/ 78 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  69   |      19|      33.629|   1.009/ 78|   1.006/ **|   1.005/ **|   1.005/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  91   |     575|      17.833|   1.039/ 17|   1.040/ 17|   1.040/ 17|   1.040/ 17 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 102   |      37|      13.099|   1.014/ 50|   1.016/ 42|   1.017/ 41|   1.018/ 39 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 101   |     829|      19.279|   1.013/ 55|   1.013/ 54|   1.013/ 54|   1.013/ 54 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  84   |       7|       0.213|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 105   |     985|      21.924|   1.031/ 22|   1.032/ 22|   1.032/ 22|   1.032/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  87   |     372|     125.930|   1.041/ 17|   1.037/ 18|   1.036/ 19|   1.035/ 19 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 112   |     103|       4.011|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 101   |     692|      77.758|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 100   |     150|      14.901|   1.042/ 16|   1.043/ 16|   1.043/ 16|   1.043/ 16 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  97   |      54|      35.085|   1.068/ 10|   1.075/  9|   1.077/  9|   1.078/  9 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  95   |    1520|       9.020|   1.038/ 18|   1.036/ 19|   1.035/ 20|   1.035/ 20 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  82   |     348|      36.985|   1.019/ 37|   1.018/ 39|   1.017/ 40|   1.017/ 41 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 102   |    9812|     851.386|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  76   |       9|       0.780|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  84   |     777|      67.758|   1.038/ 18|   1.036/ 19|   1.035/ 20|   1.035/ 20 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  92   |     172|      52.041|   1.004/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  82   |       1|       0.428|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  96   |   53460|     252.872|   1.024/ 28|   1.021/ 33|   1.020/ 35|   1.019/ 37 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 102   |     197|      28.393|   1.016/ 43|   1.016/ 44|   1.016/ 44|   1.015/ 45 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  95   |      53|       2.557|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  69   |       1|       0.091|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  88   |     277|      10.419|   1.008/ 92|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 104   |    8893|     234.032|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  29   |      23|       4.121|   1.087/  8|   1.069/ 10|   1.065/ 10|   1.061/ 11 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  54   |      75|       4.640|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  91   |    4574|     239.398|   1.059/ 12|   1.057/ 12|   1.057/ 12|   1.057/ 12 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 102   |    4638|       3.308|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  91   |    2132|      43.158|   1.042/ 16|   1.043/ 16|   1.043/ 16|   1.043/ 16 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  94   |      12|       2.423|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  94   |     109|      26.694|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  95   |      85|       7.589|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  99   |     608|     104.334|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  96   |     638|      61.593|   1.015/ 47|   1.016/ 44|   1.016/ 43|   1.016/ 43 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  99   |    4225|     241.873|   1.009/ 73|   1.008/ 84|   1.008/ 87|   1.008/ 90 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 105   |    1964|      19.590|   1.042/ 16|   1.045/ 15|   1.045/ 15|   1.046/ 15 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  82   |      89|      13.763|   1.036/ 19|   1.037/ 19|   1.037/ 19|   1.037/ 19 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  60   |      25|      18.692|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  77   |      92|       0.932|   1.092/  7|   1.088/  8|   1.087/  8|   1.085/  8 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  92   |     331|      59.917|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 127   |   30181|     449.946|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  93   |      32|      14.849|   1.035/ 20|   1.036/ 19|   1.036/ 19|   1.036/ 19 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  90   |       1|       0.426|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  78   |      14|       3.810|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 104   |    9014|     108.410|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  92   |      64|       2.111|   1.044/ 15|   1.051/ 14|   1.052/ 13|   1.054/ 13 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 102   |     191|      17.770|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  97   |     619|      37.294|   1.061/ 11|   1.058/ 12|   1.057/ 12|   1.056/ 12 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  67   |      27|       2.174|   1.011/ 64|   1.012/ 59|   1.012/ 57|   1.012/ 56 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  56   |      18|      10.990|   1.023/ 30|   1.028/ 25|   1.029/ 24|   1.030/ 23 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  77   |      92|       7.924|   1.040/ 17|   1.037/ 18|   1.037/ 19|   1.036/ 19 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  87   |     369|      40.259|   1.025/ 27|   1.024/ 29|   1.023/ 29|   1.023/ 30 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|       0.267|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  98   |     587|      60.053|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 102   |   12794|       9.399|   1.037/ 19|   1.035/ 19|   1.035/ 20|   1.035/ 20 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 102   |    2445|       9.161|   1.021/ 33|   1.021/ 33|   1.021/ 33|   1.021/ 34 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 122   |    9316|     111.728|   1.010/ 70|   1.010/ 68|   1.010/ 67|   1.010/ 67 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 109   |     781|      19.957|   1.086/  8|   1.095/  7|   1.097/  7|   1.099/  7 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 102   |    1744|     354.296|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  92   |     307|      33.455|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 121   |   35132|     583.221|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  94   |      10|       3.760|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 129   |    1038|       8.243|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  86   |       9|       0.844|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  88   |      99|       5.307|   1.059/ 12|   1.068/ 10|   1.070/ 10|   1.072/  9 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  87   |     122|       2.574|   1.033/ 21|   1.033/ 21|   1.033/ 21|   1.033/ 21 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  87   |      33|      18.283|   1.006/ **|   1.006/ **|   1.007/ **|   1.007/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  78   |     344|      77.765|   1.017/ 41|   1.010/ 67|   1.009/ 80|   1.007/ 99 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  79   |      34|       5.145|   1.034/ 20|   1.036/ 19|   1.036/ 19|   1.037/ 19 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  79   |      30|      15.672|   1.013/ 52|   1.014/ 49|   1.014/ 48|   1.015/ 47 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 103   |      32|       4.744|   1.008/ 83|   1.009/ 76|   1.009/ 75|   1.009/ 74 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  78   |      34|       7.641|   1.008/ 86|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  80   |      10|       1.473|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  92   |      79|      28.221|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  35   |      13|       0.503|   1.037/ 19|   1.040/ 17|   1.042/ 16|   1.044/ 16 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  96   |     121|       3.697|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  84   |     116|       5.718|   1.015/ 46|   1.012/ 58|   1.011/ 63|   1.010/ 68 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  83   |     164|      40.320|   1.044/ 16|   1.038/ 18|   1.036/ 19|   1.035/ 20 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  94   |   22286|     176.066|   1.034/ 20|   1.031/ 22|   1.030/ 23|   1.029/ 23 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  95   |     463|     172.815|   1.022/ 31|   1.022/ 31|   1.022/ 31|   1.022/ 32 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 103   |     216|       6.028|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  27   |       4|       0.147|   1.070/ 10|   1.059/ 12|   1.051/ 13|   1.041/ 17 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  36   |      23|       0.765|   1.046/ 15|   1.040/ 17|   1.039/ 18|   1.037/ 19 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 107   |    6184|     354.258|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  84   |      22|       4.457|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  86   |      77|      11.962|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  88   |      68|       3.048|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  90   |     507|       2.459|   1.028/ 24|   1.028/ 25|   1.027/ 25|   1.027/ 25 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  91   |     217|     104.478|   1.031/ 22|   1.033/ 21|   1.034/ 20|   1.035/ 20 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  99   |     244|      45.459|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  82   |     139|      29.699|   1.044/ 16|   1.040/ 17|   1.039/ 17|   1.038/ 18 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  94   |    3482|      15.875|   1.045/ 15|   1.045/ 15|   1.046/ 15|   1.046/ 15 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 102   |     488|     115.725|   1.019/ 37|   1.019/ 36|   1.019/ 36|   1.019/ 35 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  92   |      12|       1.689|   1.003/ **|   1.004/ **|   1.004/ **|   1.005/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  93   |    8003|     249.084|   1.027/ 25|   1.025/ 27|   1.025/ 28|   1.024/ 29 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 140   |    1188|      10.947|   1.007/ 93|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 101   |    1339|      34.892|   1.011/ 63|   1.011/ 63|   1.011/ 63|   1.011/ 63 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  96   |    1583|     153.998|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  85   |     101|      36.715|   1.045/ 15|   1.040/ 17|   1.039/ 18|   1.037/ 18 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  91   |    1489|      76.749|   1.008/ 82|   1.008/ 82|   1.008/ 83|   1.008/ 83 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  94   |    8545|      58.227|   1.026/ 27|   1.022/ 31|   1.021/ 32|   1.020/ 34 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  22   |       2|       0.162|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  89   |    1240|      36.246|   1.045/ 15|   1.046/ 15|   1.046/ 15|   1.047/ 15 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  81   |      76|       4.683|   1.039/ 18|   1.042/ 16|   1.044/ 16|   1.045/ 15 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  93   |     260|      37.297|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  59   |      53|       6.695|   1.007/ **|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  92   |      26|       4.640|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  85   |      28|       5.133|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  99   |     110|      52.607|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  74   |      93|       5.825|   1.006/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  86   |    2048|      34.838|   1.050/ 14|   1.046/ 15|   1.045/ 15|   1.044/ 16 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|       1.044|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 110   |   27329|     580.236|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  85   |      11|       0.525|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 100   |     631|      14.861|   1.029/ 24|   1.023/ 31|   1.021/ 33|   1.019/ 36 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 102   |    5232|     506.095|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 108   |    1959|     227.700|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  84   |       7|       0.418|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  82   |      21|       0.376|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 112   |      59|       0.880|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  86   |      13|       1.752|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  88   |       8|       5.865|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  94   |      50|       4.270|   1.002/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  96   |    4976|      59.843|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 113   |  123533|     374.861|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 100   |    1024|      24.444|   1.017/ 42|   1.015/ 45|   1.015/ 46|   1.015/ 47 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  93   |     306|      30.941|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 102   |   43573|     655.864|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  84   |      24|       6.891|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  86   |      20|       0.600|   1.010/ 71|   1.007/ 99|   1.006/ **|   1.005/ ** |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  86   |      32|       0.988|   1.032/ 21|   1.035/ 20|   1.036/ 19|   1.037/ 19 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  80   |      12|       0.643|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  90   |       4|       0.264|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |

