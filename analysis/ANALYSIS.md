# State and Country COVID-19 Analysis #
## Updated: 2020-06-12 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  90   |   30993|     1593.19|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  94   |   12781|     1438.94|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  84   |    7744|     1114.29|   1.008/ 87|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  87   |    6404|      505.34|   1.012/ 56|   1.010/ 72|   1.009/ 78|   1.008/ 84 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  85   |    6341|      495.31|   1.009/ 78|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  85   |    6043|      605.06|   1.007/ 98|   1.006/ **|   1.006/ **|   1.006/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 100   |    5081|      128.59|   1.014/ 48|   1.013/ 55|   1.012/ 57|   1.012/ 59 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  85   |    4273|     1198.41|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  90   |    3044|      654.76|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  85   |    2969|      491.16|   1.012/ 58|   1.009/ 74|   1.009/ 79|   1.008/ 84 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 104   |  118139|      358.49|   1.007/ 94|   1.006/ **|   1.005/ **|   1.005/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  93   |   42112|      633.88|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  87   |   43911|      207.70|   1.031/ 22|   1.026/ 26|   1.025/ 27|   1.024/ 29 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 112   |   34867|      578.82|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 118   |   30151|      449.50|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 101   |   27389|      581.50|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  85   |   16666|      131.67|   1.042/ 16|   1.039/ 18|   1.038/ 18|   1.037/ 19 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  93   |    9778|      848.44|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  95   |    8918|      107.25|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 113   |    8561|      102.67|   1.008/ 87|   1.008/ 88|   1.008/ 89|   1.008/ 89 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  79   |     755|      154.05|   1.017/ 41|   1.016/ 43|   1.016/ 44|   1.016/ 44 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  79   |      10|       14.02|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  83   |    1147|      157.54|   1.018/ 38|   1.016/ 43|   1.015/ 45|   1.015/ 46 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  80   |     168|       55.69|   1.022/ 31|   1.023/ 30|   1.023/ 30|   1.023/ 30 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 100   |    5081|      128.59|   1.014/ 48|   1.013/ 55|   1.012/ 57|   1.012/ 59 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  90   |    1653|      287.03|   1.008/ 85|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  85   |    4273|     1198.41|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  78   |     426|      437.70|   1.012/ 56|   1.010/ 70|   1.009/ 74|   1.009/ 78 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  96   |    2913|      135.64|   1.013/ 55|   1.011/ 63|   1.011/ 65|   1.010/ 68 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  92   |    2389|      225.03|   1.014/ 50|   1.013/ 54|   1.013/ 55|   1.012/ 56 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  73   |      17|       12.01|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  78   |      86|       48.31|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  87   |    6404|      505.34|   1.012/ 56|   1.010/ 72|   1.009/ 78|   1.008/ 84 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  88   |    2454|      364.46|   1.010/ 73|   1.007/ 94|   1.007/ **|   1.006/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  79   |     685|      216.98|   1.018/ 39|   1.013/ 54|   1.011/ 60|   1.010/ 68 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  91   |     243|       83.36|   1.008/ 86|   1.007/ 95|   1.007/ 97|   1.007/ 99 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  88   |     503|      112.48|   1.012/ 57|   1.011/ 64|   1.010/ 66|   1.010/ 68 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  90   |    3044|      654.76|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  77   |     105|       77.77|   1.013/ 52|   1.012/ 57|   1.012/ 59|   1.011/ 61 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  85   |    2969|      491.16|   1.012/ 58|   1.009/ 74|   1.009/ 79|   1.008/ 84 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  84   |    7744|     1114.29|   1.008/ 87|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  85   |    6043|      605.06|   1.007/ 98|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  83   |    1327|      235.26|   1.020/ 35|   1.017/ 40|   1.017/ 41|   1.016/ 43 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  85   |     911|      306.11|   1.018/ 39|   1.015/ 46|   1.014/ 48|   1.014/ 50 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  85   |     885|      144.15|   1.012/ 60|   1.009/ 74|   1.009/ 79|   1.008/ 84 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  77   |      18|       16.94|   1.001/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  76   |     207|      106.87|   1.016/ 42|   1.013/ 52|   1.012/ 55|   1.012/ 59 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  88   |     465|      151.10|   1.008/ 85|   1.006/ **|   1.006/ **|   1.006/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  81   |     316|      232.62|   1.020/ 35|   1.017/ 41|   1.016/ 43|   1.015/ 46 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  94   |   12781|     1438.94|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  79   |     432|      206.06|   1.015/ 47|   1.011/ 61|   1.010/ 66|   1.010/ 72 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  90   |   30993|     1593.19|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  79   |    1137|      108.42|   1.017/ 40|   1.015/ 46|   1.015/ 47|   1.014/ 49 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  77   |      77|      101.67|   1.018/ 39|   1.015/ 46|   1.014/ 49|   1.013/ 51 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  84   |    2605|      222.83|   1.013/ 55|   1.009/ 73|   1.009/ 80|   1.008/ 88 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  85   |     363|       91.81|   1.007/ 95|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  89   |     170|       40.24|   1.008/ 82|   1.008/ 85|   1.008/ 85|   1.008/ 86 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  85   |    6341|      495.31|   1.009/ 78|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  83   |     146|       45.77|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  76   |     861|      812.49|   1.016/ 44|   1.013/ 54|   1.012/ 58|   1.011/ 62 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  88   |     587|      114.05|   1.016/ 42|   1.016/ 43|   1.016/ 44|   1.016/ 44 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  93   |      74|       83.76|   1.016/ 43|   1.013/ 52|   1.013/ 55|   1.012/ 58 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  83   |     446|       65.33|   1.016/ 43|   1.016/ 44|   1.016/ 44|   1.015/ 45 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  87   |    1983|       68.40|   1.012/ 56|   1.010/ 69|   1.009/ 73|   1.009/ 78 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  82   |     135|       42.02|   1.016/ 44|   1.013/ 53|   1.012/ 56|   1.012/ 59 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  84   |      55|       88.78|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  90   |    1628|      190.78|   1.012/ 58|   1.008/ 83|   1.007/ 93|   1.007/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 104   |    1213|      159.34|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  74   |      87|       48.34|   1.009/ 73|   1.008/ 83|   1.008/ 85|   1.008/ 88 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  84   |     695|      119.40|   1.015/ 47|   1.014/ 50|   1.014/ 51|   1.013/ 52 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  60   |      19|       32.84|   1.015/ 46|   1.006/ **|   1.004/ **|   1.002/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  82   |     401|       12.45|   1.041/ 17|   1.043/ 16|   1.044/ 16|   1.044/ 16 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  93   |      34|       12.04|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  92   |     744|       17.29|   1.012/ 58|   1.012/ 59|   1.012/ 60|   1.012/ 60 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  75   |       5|        0.16|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  96   |     748|       16.64|   1.030/ 23|   1.030/ 23|   1.030/ 23|   1.030/ 23 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  78   |     252|       85.09|   1.056/ 12|   1.056/ 12|   1.056/ 12|   1.056/ 12 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 103   |     104|        4.04|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  92   |     683|       76.67|   1.002/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  91   |     102|       10.11|   1.046/ 15|   1.049/ 14|   1.049/ 14|   1.050/ 14 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  88   |      29|       18.76|   1.055/ 12|   1.062/ 11|   1.064/ 11|   1.066/ 10 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  86   |    1078|        6.40|   1.046/ 15|   1.044/ 15|   1.044/ 16|   1.044/ 16 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  73   |     297|       31.55|   1.021/ 32|   1.020/ 35|   1.019/ 35|   1.019/ 36 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  93   |    9778|      848.44|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  67   |       4|        0.32|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  75   |     551|       48.03|   1.042/ 16|   1.039/ 18|   1.038/ 18|   1.038/ 18 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  83   |     168|       51.00|   1.004/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  73   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  87   |   43911|      207.70|   1.031/ 22|   1.026/ 26|   1.025/ 27|   1.024/ 29 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  93   |     174|       25.01|   1.016/ 43|   1.015/ 47|   1.014/ 48|   1.014/ 50 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  86   |      54|        2.57|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  60   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  79   |     227|        8.54|   1.013/ 54|   1.010/ 73|   1.009/ 80|   1.008/ 89 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  95   |    8510|      223.95|   1.010/ 73|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  20   |       5|        0.94|   1.162/  4|   1.030/ 23|   1.009/ 80|   1.000/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  45   |      72|        4.42|   1.009/ 73|   1.010/ 68|   1.010/ 67|   1.011/ 65 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  82   |    2163|      113.20|   1.063/ 11|   1.063/ 11|   1.063/ 11|   1.063/ 11 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  93   |    4638|        3.31|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  82   |    1454|       29.43|   1.042/ 16|   1.044/ 15|   1.045/ 15|   1.045/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  85   |      11|        2.22|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  85   |     107|       26.26|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  86   |      84|        7.54|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  90   |     598|      102.78|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  87   |     561|       54.18|   1.010/ 70|   1.009/ 75|   1.009/ 76|   1.009/ 77 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  90   |    3986|      228.17|   1.009/ 77|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  96   |    1369|       13.66|   1.034/ 20|   1.035/ 20|   1.035/ 20|   1.035/ 20 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  73   |      65|       10.07|   1.036/ 19|   1.035/ 20|   1.035/ 20|   1.035/ 20 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  51   |      12|        8.90|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  68   |      34|        0.35|   1.134/  5|   1.159/  4|   1.165/  4|   1.171/  4 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  83   |     331|       59.82|   1.002/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 118   |   30151|      449.50|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  84   |      24|       11.02|   1.012/ 60|   1.007/ 92|   1.006/ **|   1.005/ ** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  81   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  69   |      13|        3.53|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  95   |    8918|      107.25|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  83   |      48|        1.58|   1.024/ 28|   1.025/ 28|   1.025/ 28|   1.025/ 27 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  93   |     187|       17.42|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  88   |     306|       18.46|   1.103/  7|   1.111/  6|   1.113/  6|   1.115/  6 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  58   |      24|        1.97|   1.005/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  47   |      13|        8.03|   1.014/ 48|   1.005/ **|   1.003/ **|   1.001/ ** |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  68   |      65|        5.58|   1.043/ 16|   1.039/ 18|   1.038/ 18|   1.037/ 19 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  78   |     292|       31.94|   1.030/ 23|   1.030/ 23|   1.029/ 23|   1.029/ 23 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  89   |     572|       58.51|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  93   |    8501|        6.24|   1.040/ 17|   1.039/ 18|   1.038/ 18|   1.038/ 18 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  93   |    2032|        7.61|   1.022/ 32|   1.021/ 33|   1.021/ 33|   1.021/ 33 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 113   |    8561|      102.67|   1.008/ 87|   1.008/ 88|   1.008/ 89|   1.008/ 89 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 100   |     357|        9.12|   1.065/ 10|   1.073/  9|   1.075/  9|   1.078/  9 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  93   |    1726|      350.72|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  83   |     301|       32.77|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 112   |   34867|      578.82|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  85   |      10|        3.64|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 120   |    1054|        8.37|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  77   |       9|        0.84|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  79   |      60|        3.19|   1.041/ 17|   1.049/ 14|   1.051/ 13|   1.054/ 13 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  78   |      93|        1.95|   1.030/ 23|   1.030/ 23|   1.031/ 23|   1.031/ 22 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  78   |      31|       17.17|   1.003/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  69   |     304|       68.75|   1.030/ 23|   1.023/ 30|   1.021/ 33|   1.019/ 36 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  70   |      25|        3.76|   1.036/ 19|   1.043/ 16|   1.045/ 15|   1.046/ 15 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  70   |      27|       13.94|   1.009/ 78|   1.007/ 95|   1.007/ **|   1.007/ ** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  94   |      29|        4.26|   1.010/ 71|   1.012/ 59|   1.012/ 56|   1.013/ 54 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  69   |      32|        7.07|   1.012/ 57|   1.010/ 67|   1.010/ 70|   1.010/ 73 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  71   |       6|        0.83|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  83   |      76|       27.30|   1.008/ 92|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  26   |      10|        0.40|   1.058/ 12|   1.055/ 12|   1.050/ 14|   1.044/ 16 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  87   |     118|        3.60|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  75   |     101|        4.97|   1.022/ 31|   1.019/ 36|   1.018/ 38|   1.017/ 40 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  74   |      85|       20.90|   1.122/  6|   1.123/  5|   1.123/  5|   1.123/  5 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  85   |   16666|      131.67|   1.042/ 16|   1.039/ 18|   1.038/ 18|   1.037/ 19 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  86   |     382|      142.28|   1.022/ 31|   1.021/ 33|   1.021/ 33|   1.021/ 34 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  94   |     213|        5.93|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  18   |       2|        0.07|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  27   |      16|        0.55|   1.093/  7|   1.060/ 11|   1.049/ 14|   1.037/ 19 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  98   |    6170|      353.44|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  75   |      22|        4.47|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  77   |      68|       10.56|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  79   |      68|        3.07|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  81   |     399|        1.93|   1.028/ 24|   1.026/ 26|   1.026/ 27|   1.025/ 27 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  82   |     166|       80.06|   1.021/ 33|   1.022/ 32|   1.022/ 31|   1.022/ 31 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  90   |     241|       44.94|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  73   |      93|       19.89|   1.052/ 13|   1.050/ 14|   1.050/ 14|   1.049/ 14 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  85   |    2349|       10.71|   1.044/ 15|   1.046/ 15|   1.046/ 15|   1.047/ 15 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  93   |     414|       98.04|   1.018/ 39|   1.018/ 39|   1.018/ 39|   1.018/ 38 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  83   |      11|        1.55|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  84   |    6380|      198.55|   1.030/ 23|   1.026/ 27|   1.025/ 27|   1.024/ 28 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 131   |    1113|       10.25|   1.007/ 98|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  92   |    1225|       31.91|   1.010/ 68|   1.009/ 75|   1.009/ 77|   1.009/ 79 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  87   |    1540|      149.83|   1.007/ 99|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  76   |      70|       25.54|   1.063/ 11|   1.063/ 11|   1.063/ 11|   1.063/ 11 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  82   |    1393|       71.79|   1.007/ 99|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  85   |    6897|       47.00|   1.033/ 21|   1.030/ 23|   1.029/ 24|   1.028/ 25 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  13   |       2|        0.16|   1.145/  5|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  80   |     813|       23.76|   1.047/ 15|   1.051/ 14|   1.052/ 13|   1.053/ 13 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  72   |      55|        3.40|   1.025/ 28|   1.021/ 32|   1.021/ 33|   1.020/ 34 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  84   |     254|       36.44|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  50   |      50|        6.39|   1.010/ 68|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  83   |      25|        4.42|   1.005/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  76   |      28|        5.15|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  90   |     111|       52.82|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  65   |      89|        5.59|   1.015/ 47|   1.012/ 60|   1.011/ 64|   1.010/ 70 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  77   |    1302|       22.15|   1.062/ 11|   1.061/ 11|   1.060/ 11|   1.060/ 11 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 101   |   27389|      581.50|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  76   |      11|        0.52|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  91   |     477|       11.24|   1.043/ 16|   1.038/ 18|   1.036/ 19|   1.035/ 20 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  93   |    4968|      480.49|   1.009/ 79|   1.007/ **|   1.007/ **|   1.006/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  99   |    1948|      226.44|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  75   |       7|        0.38|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  73   |      21|        0.38|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 103   |      58|        0.88|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  77   |      13|        1.78|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  79   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  85   |      50|        4.24|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  87   |    4841|       58.21|   1.005/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 104   |  118139|      358.49|   1.007/ 94|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  91   |     895|       21.37|   1.017/ 41|   1.014/ 51|   1.013/ 54|   1.012/ 58 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  84   |     294|       29.74|   1.007/ 97|   1.004/ **|   1.004/ **|   1.003/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  93   |   42112|      633.88|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  75   |      24|        6.75|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  77   |      18|        0.54|   1.022/ 32|   1.024/ 29|   1.024/ 29|   1.025/ 28 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  77   |      24|        0.75|   1.029/ 24|   1.033/ 21|   1.034/ 20|   1.035/ 19 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  71   |       8|        0.47|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  81   |       4|        0.26|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |

