# State and Country COVID-19 Analysis #
## Updated: 2020-06-13 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  91   |   31036|     1595.39|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  95   |   12815|     1442.75|   1.005/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  85   |    7777|     1119.05|   1.008/ 91|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  88   |    6476|      511.05|   1.012/ 57|   1.010/ 71|   1.009/ 76|   1.008/ 82 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  86   |    6388|      498.97|   1.009/ 80|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  86   |    6080|      608.76|   1.007/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 101   |    5140|      130.08|   1.014/ 48|   1.013/ 55|   1.012/ 56|   1.012/ 58 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  86   |    4289|     1203.12|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  91   |    3054|      656.96|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  86   |    3000|      496.22|   1.012/ 60|   1.009/ 75|   1.009/ 79|   1.008/ 85 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 105   |  118698|      360.19|   1.007/ 96|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  88   |   45111|      213.38|   1.031/ 22|   1.026/ 26|   1.025/ 28|   1.024/ 29 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  94   |   42335|      637.24|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 113   |   34883|      579.09|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 119   |   30132|      449.22|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 102   |   27353|      580.73|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  86   |   17311|      136.76|   1.041/ 17|   1.038/ 18|   1.038/ 18|   1.037/ 19 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  94   |    9788|      849.34|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  96   |    8936|      107.46|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 114   |    8633|      103.54|   1.008/ 86|   1.008/ 86|   1.008/ 86|   1.008/ 87 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  80   |     768|      156.72|   1.017/ 41|   1.016/ 42|   1.016/ 42|   1.016/ 43 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  80   |      10|       14.17|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  84   |    1169|      160.55|   1.019/ 37|   1.017/ 41|   1.017/ 42|   1.016/ 43 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  81   |     172|       57.10|   1.023/ 30|   1.024/ 29|   1.024/ 29|   1.024/ 28 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 101   |    5140|      130.08|   1.014/ 48|   1.013/ 55|   1.012/ 56|   1.012/ 58 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  91   |    1658|      287.89|   1.008/ 90|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  86   |    4289|     1203.12|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  79   |     429|      440.32|   1.011/ 61|   1.009/ 79|   1.008/ 85|   1.008/ 92 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  97   |    2943|      137.03|   1.012/ 55|   1.011/ 63|   1.011/ 65|   1.010/ 67 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  93   |    2422|      228.09|   1.014/ 49|   1.013/ 52|   1.013/ 53|   1.013/ 53 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  74   |      17|       12.01|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  79   |      87|       48.51|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  88   |    6476|      511.05|   1.012/ 57|   1.010/ 71|   1.009/ 76|   1.008/ 82 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  89   |    2468|      366.58|   1.009/ 75|   1.007/ 98|   1.007/ **|   1.006/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  80   |     693|      219.60|   1.017/ 42|   1.012/ 60|   1.010/ 68|   1.009/ 77 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  92   |     245|       84.04|   1.008/ 85|   1.008/ 92|   1.007/ 93|   1.007/ 95 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  89   |     508|      113.62|   1.012/ 57|   1.011/ 63|   1.011/ 65|   1.010/ 67 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  91   |    3054|      656.96|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  78   |     105|       78.35|   1.012/ 58|   1.010/ 68|   1.010/ 72|   1.009/ 76 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  86   |    3000|      496.22|   1.012/ 60|   1.009/ 75|   1.009/ 79|   1.008/ 85 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  85   |    7777|     1119.05|   1.008/ 91|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  86   |    6080|      608.76|   1.007/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  84   |    1351|      239.47|   1.020/ 35|   1.017/ 40|   1.017/ 41|   1.016/ 43 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  86   |     924|      310.47|   1.017/ 41|   1.014/ 48|   1.014/ 50|   1.013/ 52 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  86   |     896|      145.91|   1.012/ 59|   1.010/ 71|   1.009/ 75|   1.009/ 79 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  78   |      18|       17.01|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  77   |     211|      109.01|   1.019/ 37|   1.017/ 41|   1.016/ 42|   1.016/ 43 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  89   |     468|      152.04|   1.008/ 84|   1.007/ **|   1.006/ **|   1.006/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  82   |     323|      237.25|   1.021/ 33|   1.018/ 38|   1.018/ 39|   1.017/ 40 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  95   |   12815|     1442.75|   1.005/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  80   |     437|      208.54|   1.014/ 48|   1.011/ 62|   1.010/ 66|   1.010/ 71 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  91   |   31036|     1595.39|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  80   |    1154|      110.05|   1.017/ 41|   1.015/ 46|   1.014/ 48|   1.014/ 49 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  78   |      78|      102.91|   1.017/ 41|   1.014/ 50|   1.013/ 53|   1.012/ 57 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  85   |    2624|      224.48|   1.012/ 57|   1.009/ 75|   1.009/ 81|   1.008/ 89 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  86   |     366|       92.39|   1.007/ 98|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  90   |     171|       40.63|   1.008/ 82|   1.008/ 84|   1.008/ 84|   1.008/ 84 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  86   |    6388|      498.97|   1.009/ 80|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  84   |     147|       46.05|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  77   |     869|      820.60|   1.015/ 46|   1.012/ 58|   1.011/ 62|   1.010/ 67 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  89   |     596|      115.79|   1.016/ 43|   1.016/ 44|   1.016/ 44|   1.016/ 44 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  94   |      75|       85.31|   1.017/ 40|   1.015/ 46|   1.015/ 47|   1.014/ 49 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  84   |     456|       66.66|   1.017/ 41|   1.017/ 42|   1.017/ 42|   1.017/ 42 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  88   |    2007|       69.22|   1.012/ 56|   1.010/ 67|   1.010/ 70|   1.009/ 73 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  83   |     137|       42.79|   1.017/ 42|   1.015/ 47|   1.014/ 49|   1.014/ 50 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  85   |      55|       88.77|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  91   |    1638|      191.88|   1.011/ 62|   1.008/ 89|   1.007/ **|   1.006/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 105   |    1219|      160.10|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  75   |      88|       48.84|   1.010/ 69|   1.009/ 75|   1.009/ 76|   1.009/ 77 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  85   |     704|      120.93|   1.015/ 47|   1.014/ 51|   1.013/ 52|   1.013/ 53 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  61   |      19|       32.85|   1.015/ 46|   1.007/ 96|   1.005/ **|   1.003/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  83   |     420|       13.03|   1.042/ 16|   1.044/ 15|   1.045/ 15|   1.046/ 15 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  94   |      35|       12.15|   1.006/ **|   1.007/ **|   1.007/ **|   1.007/ 98 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  93   |     752|       17.50|   1.012/ 58|   1.012/ 59|   1.012/ 59|   1.012/ 60 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  76   |       5|        0.16|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  97   |     770|       17.14|   1.030/ 23|   1.030/ 23|   1.030/ 23|   1.030/ 23 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  79   |     266|       90.08|   1.056/ 12|   1.056/ 12|   1.056/ 12|   1.056/ 12 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 104   |     104|        4.04|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  93   |     683|       76.77|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  92   |     107|       10.60|   1.046/ 15|   1.049/ 14|   1.050/ 14|   1.050/ 14 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  89   |      31|       20.04|   1.058/ 12|   1.065/ 10|   1.067/ 10|   1.069/ 10 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  87   |    1124|        6.67|   1.045/ 15|   1.044/ 16|   1.043/ 16|   1.043/ 16 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  74   |     303|       32.17|   1.021/ 33|   1.020/ 35|   1.019/ 36|   1.019/ 37 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  94   |    9788|      849.34|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  68   |       4|        0.34|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  76   |     574|       50.01|   1.042/ 16|   1.040/ 17|   1.039/ 17|   1.039/ 18 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  84   |     169|       51.15|   1.004/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  74   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  88   |   45111|      213.38|   1.031/ 22|   1.026/ 26|   1.025/ 28|   1.024/ 29 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  94   |     177|       25.39|   1.016/ 45|   1.014/ 50|   1.013/ 51|   1.013/ 53 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  87   |      54|        2.57|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  61   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  80   |     228|        8.59|   1.011/ 61|   1.008/ 90|   1.007/ **|   1.006/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  96   |    8576|      225.68|   1.009/ 76|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  21   |       6|        1.01|   1.059/ 12|   1.044/ 16|   1.045/ 15|   1.048/ 14 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  46   |      72|        4.46|   1.009/ 76|   1.009/ 73|   1.010/ 71|   1.010/ 70 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  83   |    2515|      131.64|   1.065/ 11|   1.066/ 10|   1.066/ 10|   1.066/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  94   |    4638|        3.31|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  83   |    1521|       30.79|   1.042/ 16|   1.045/ 15|   1.045/ 15|   1.046/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  86   |      11|        2.26|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  86   |     107|       26.36|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  87   |      85|        7.54|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  91   |     600|      102.96|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  88   |     567|       54.78|   1.010/ 67|   1.010/ 70|   1.010/ 70|   1.010/ 71 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  91   |    3997|      228.81|   1.009/ 77|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  97   |    1416|       14.12|   1.033/ 21|   1.034/ 20|   1.034/ 20|   1.035/ 20 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  74   |      68|       10.43|   1.037/ 19|   1.037/ 19|   1.037/ 19|   1.037/ 18 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  52   |      12|        8.90|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  69   |      40|        0.41|   1.117/  6|   1.137/  5|   1.142/  5|   1.147/  5 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  84   |     331|       59.89|   1.002/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 119   |   30132|      449.22|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  85   |      24|       11.27|   1.016/ 42|   1.013/ 53|   1.012/ 56|   1.012/ 60 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  82   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  70   |      13|        3.54|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  96   |    8936|      107.46|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  84   |      49|        1.61|   1.023/ 31|   1.022/ 31|   1.022/ 31|   1.022/ 31 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  94   |     187|       17.46|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  89   |     341|       20.51|   1.091/  7|   1.095/  7|   1.096/  7|   1.097/  7 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  59   |      24|        1.97|   1.005/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  48   |      14|        8.59|   1.026/ 27|   1.026/ 26|   1.027/ 26|   1.027/ 26 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  69   |      67|        5.77|   1.043/ 16|   1.039/ 17|   1.038/ 18|   1.037/ 18 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  79   |     302|       32.94|   1.031/ 22|   1.031/ 22|   1.031/ 22|   1.031/ 22 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  90   |     574|       58.75|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  94   |    8814|        6.48|   1.039/ 17|   1.038/ 18|   1.038/ 18|   1.037/ 18 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  94   |    2074|        7.77|   1.021/ 32|   1.021/ 33|   1.021/ 33|   1.020/ 34 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 114   |    8633|      103.54|   1.008/ 86|   1.008/ 86|   1.008/ 86|   1.008/ 87 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 101   |     386|        9.87|   1.067/ 10|   1.076/  9|   1.078/  9|   1.080/  9 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  94   |    1730|      351.53|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  84   |     302|       32.87|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 113   |   34883|      579.09|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  86   |      10|        3.66|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 121   |    1050|        8.34|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  78   |       9|        0.84|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  80   |      62|        3.34|   1.042/ 16|   1.051/ 14|   1.053/ 13|   1.055/ 12 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  79   |      96|        2.01|   1.030/ 23|   1.030/ 23|   1.030/ 23|   1.031/ 23 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  79   |      31|       17.22|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  70   |     310|       70.18|   1.028/ 24|   1.021/ 33|   1.019/ 37|   1.017/ 41 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  71   |      26|        3.91|   1.036/ 19|   1.042/ 17|   1.043/ 16|   1.044/ 15 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  71   |      27|       14.07|   1.009/ 76|   1.008/ 88|   1.008/ 92|   1.007/ 95 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  95   |      30|        4.33|   1.010/ 69|   1.012/ 58|   1.013/ 55|   1.013/ 53 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  70   |      32|        7.16|   1.012/ 59|   1.010/ 69|   1.010/ 71|   1.009/ 74 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  72   |       6|        0.85|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  84   |      77|       27.44|   1.007/ 94|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  27   |      11|        0.40|   1.060/ 11|   1.049/ 14|   1.043/ 16|   1.036/ 19 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  88   |     118|        3.61|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  76   |     103|        5.08|   1.022/ 31|   1.019/ 36|   1.019/ 37|   1.018/ 38 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  75   |      95|       23.22|   1.109/  6|   1.111/  6|   1.112/  6|   1.112/  6 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  86   |   17311|      136.76|   1.041/ 17|   1.038/ 18|   1.038/ 18|   1.037/ 19 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  87   |     389|      145.10|   1.022/ 32|   1.021/ 34|   1.020/ 34|   1.020/ 35 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  95   |     213|        5.95|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  19   |       2|        0.07|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  28   |      17|        0.56|   1.088/  8|   1.047/ 15|   1.033/ 21|   1.019/ 36 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  99   |    6169|      353.41|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  76   |      22|        4.47|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  78   |      70|       10.84|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  80   |      68|        3.06|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  82   |     409|        1.99|   1.028/ 24|   1.027/ 26|   1.026/ 26|   1.026/ 27 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  83   |     170|       81.86|   1.022/ 31|   1.023/ 30|   1.023/ 30|   1.023/ 30 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  91   |     241|       44.99|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  74   |      98|       20.94|   1.052/ 13|   1.050/ 14|   1.049/ 14|   1.049/ 14 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  86   |    2449|       11.17|   1.043/ 16|   1.045/ 15|   1.045/ 15|   1.045/ 15 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  94   |     421|       99.74|   1.018/ 39|   1.018/ 39|   1.018/ 39|   1.018/ 39 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  84   |      11|        1.55|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  85   |    6514|      202.72|   1.028/ 24|   1.025/ 28|   1.024/ 29|   1.023/ 30 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 132   |    1121|       10.33|   1.007/ 98|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  93   |    1235|       32.18|   1.010/ 68|   1.009/ 75|   1.009/ 76|   1.009/ 78 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  88   |    1547|      150.55|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  77   |      74|       26.91|   1.061/ 11|   1.060/ 11|   1.060/ 11|   1.059/ 11 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  83   |    1400|       72.14|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  86   |    7100|       48.38|   1.032/ 21|   1.029/ 24|   1.028/ 24|   1.028/ 25 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  14   |       2|        0.16|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  81   |     856|       25.02|   1.047/ 15|   1.051/ 14|   1.051/ 13|   1.052/ 13 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  73   |      56|        3.47|   1.024/ 28|   1.022/ 32|   1.021/ 33|   1.020/ 34 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  85   |     254|       36.49|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  51   |      51|        6.44|   1.010/ 72|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  84   |      25|        4.44|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  77   |      28|        5.15|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  91   |     111|       52.80|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  66   |      89|        5.63|   1.013/ 53|   1.009/ 76|   1.008/ 86|   1.007/ 98 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  78   |    1378|       23.45|   1.060/ 11|   1.059/ 12|   1.059/ 12|   1.059/ 12 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 102   |   27353|      580.73|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  77   |      11|        0.53|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  92   |     497|       11.71|   1.042/ 16|   1.037/ 19|   1.035/ 20|   1.034/ 20 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  94   |    5006|      484.23|   1.009/ 80|   1.007/ 99|   1.007/ **|   1.006/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 100   |    1950|      226.59|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  76   |       7|        0.38|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  74   |      21|        0.38|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 104   |      58|        0.88|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  78   |      13|        1.78|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  80   |       8|        5.87|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  86   |      50|        4.24|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  88   |    4859|       58.44|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 105   |  118698|      360.19|   1.007/ 96|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  92   |     910|       21.74|   1.017/ 40|   1.014/ 48|   1.014/ 51|   1.013/ 54 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  85   |     295|       29.84|   1.007/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  94   |   42335|      637.24|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  76   |      24|        6.76|   1.003/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  78   |      19|        0.55|   1.022/ 32|   1.023/ 29|   1.024/ 29|   1.024/ 28 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  78   |      25|        0.77|   1.027/ 26|   1.030/ 23|   1.031/ 22|   1.031/ 22 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  72   |       9|        0.50|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  82   |       4|        0.26|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |

