# State and Country COVID-19 Analysis #
## Updated: 2020-06-23 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 101   |   31454|    1616.868|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 105   |   13289|    1496.120|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  95   |    8101|    1165.728|   1.005/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  98   |    6959|     549.174|   1.008/ 86|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  96   |    6676|     521.445|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  96   |    6282|     629.050|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 111   |    5764|     145.885|   1.012/ 58|   1.011/ 66|   1.010/ 68|   1.010/ 70 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  96   |    4374|    1226.702|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 107   |    3261|     151.840|   1.011/ 64|   1.010/ 71|   1.010/ 73|   1.009/ 75 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 101   |    3163|     680.400|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 115   |  124569|     378.003|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  98   |   55488|     262.465|   1.023/ 30|   1.019/ 36|   1.018/ 38|   1.017/ 40 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 104   |   43803|     659.336|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 123   |   35183|     584.068|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 129   |   30189|     450.068|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 112   |   27508|     584.035|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  96   |   23705|     187.274|   1.034/ 20|   1.031/ 22|   1.030/ 23|   1.029/ 23 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 104   |   14007|      10.290|   1.034/ 20|   1.033/ 21|   1.032/ 21|   1.032/ 22 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 124   |    9521|     114.194|   1.010/ 67|   1.011/ 64|   1.011/ 64|   1.011/ 63 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 104   |    9814|     851.605|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  90   |     866|     176.704|   1.013/ 54|   1.012/ 59|   1.012/ 60|   1.011/ 62 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  90   |      12|      16.663|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  94   |    1388|     190.652|   1.018/ 39|   1.017/ 40|   1.017/ 41|   1.017/ 41 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  91   |     222|      73.643|   1.027/ 25|   1.029/ 24|   1.030/ 23|   1.030/ 23 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 111   |    5764|     145.885|   1.012/ 58|   1.011/ 66|   1.010/ 68|   1.010/ 70 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 101   |    1715|     297.832|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  96   |    4374|    1226.702|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  89   |     453|     465.396|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 107   |    3261|     151.840|   1.011/ 64|   1.010/ 71|   1.010/ 73|   1.009/ 75 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 103   |    2739|     257.971|   1.012/ 60|   1.011/ 65|   1.010/ 67|   1.010/ 68 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  84   |      17|      12.007|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  89   |      90|      50.342|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  98   |    6959|     549.174|   1.008/ 86|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  99   |    2621|     389.392|   1.007/ **|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  90   |     737|     233.612|   1.008/ 91|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 102   |     261|      89.537|   1.007/ 98|   1.007/ **|   1.007/ **|   1.006/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  99   |     548|     122.735|   1.008/ 88|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 101   |    3163|     680.400|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  88   |     108|      80.405|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  96   |    3205|     530.062|   1.007/ 96|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  95   |    8101|    1165.728|   1.005/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  96   |    6282|     629.050|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  94   |    1512|     268.066|   1.012/ 59|   1.009/ 79|   1.008/ 86|   1.007/ 95 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  96   |    1016|     341.385|   1.010/ 70|   1.007/ 96|   1.007/ **|   1.006/ ** |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  96   |     987|     160.747|   1.011/ 63|   1.010/ 68|   1.010/ 69|   1.010/ 70 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  88   |      20|      18.841|   1.010/ 69|   1.011/ 61|   1.012/ 59|   1.012/ 58 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  87   |     253|     130.952|   1.018/ 39|   1.017/ 41|   1.017/ 41|   1.017/ 42 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  99   |     497|     161.218|   1.007/ **|   1.006/ **|   1.006/ **|   1.005/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  92   |     364|     267.884|   1.012/ 57|   1.009/ 77|   1.008/ 85|   1.007/ 94 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 105   |   13289|    1496.120|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  90   |     488|     232.525|   1.011/ 61|   1.010/ 72|   1.009/ 75|   1.009/ 79 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 101   |   31454|    1616.868|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  90   |    1290|     122.996|   1.012/ 56|   1.011/ 65|   1.010/ 68|   1.010/ 70 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  88   |      82|     107.391|   1.007/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  95   |    2818|     241.103|   1.008/ 86|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  96   |     378|      95.637|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 100   |     190|      45.040|   1.010/ 69|   1.010/ 67|   1.010/ 67|   1.010/ 66 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  96   |    6676|     521.445|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  94   |     152|      47.591|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  87   |     941|     888.052|   1.009/ 77|   1.006/ **|   1.006/ **|   1.005/ ** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  99   |     673|     130.672|   1.013/ 54|   1.012/ 58|   1.012/ 59|   1.012/ 60 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 104   |      86|      96.899|   1.013/ 54|   1.011/ 61|   1.011/ 64|   1.010/ 66 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  94   |     540|      79.089|   1.016/ 42|   1.016/ 43|   1.016/ 43|   1.016/ 43 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  98   |    2241|      77.291|   1.012/ 57|   1.011/ 60|   1.011/ 61|   1.011/ 62 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  93   |     161|      50.323|   1.016/ 43|   1.015/ 45|   1.015/ 46|   1.015/ 46 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  95   |      56|      89.431|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 101   |    1713|     200.671|   1.006/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 115   |    1285|     168.733|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  85   |      92|      51.392|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  95   |     773|     132.747|   1.010/ 67|   1.009/ 77|   1.009/ 80|   1.008/ 83 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  71   |      20|      34.331|   1.010/ 67|   1.009/ 76|   1.009/ 77|   1.009/ 78 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  93   |     616|      19.119|   1.037/ 18|   1.037/ 19|   1.037/ 19|   1.037/ 19 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 104   |      39|      13.654|   1.017/ 42|   1.020/ 35|   1.020/ 34|   1.021/ 33 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 103   |     850|      19.771|   1.013/ 55|   1.013/ 54|   1.013/ 54|   1.013/ 54 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  86   |       7|       0.223|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 107   |    1044|      23.237|   1.030/ 23|   1.030/ 23|   1.030/ 23|   1.030/ 23 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  89   |     398|     134.677|   1.041/ 17|   1.037/ 19|   1.036/ 19|   1.035/ 20 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 114   |     103|       4.006|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 103   |     694|      78.001|   1.002/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 102   |     163|      16.153|   1.042/ 16|   1.042/ 16|   1.042/ 16|   1.042/ 16 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  99   |      62|      40.107|   1.067/ 10|   1.072/ 10|   1.073/  9|   1.074/  9 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  97   |    1621|       9.623|   1.036/ 19|   1.033/ 21|   1.033/ 21|   1.032/ 22 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  84   |     359|      38.178|   1.018/ 39|   1.016/ 42|   1.016/ 43|   1.016/ 44 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 104   |    9814|     851.605|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  78   |      11|       0.975|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  86   |     835|      72.820|   1.038/ 18|   1.036/ 19|   1.036/ 19|   1.035/ 19 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  94   |     173|      52.391|   1.004/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  84   |       1|       0.428|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  98   |   55488|     262.465|   1.023/ 30|   1.019/ 36|   1.018/ 38|   1.017/ 40 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 104   |     204|      29.353|   1.017/ 41|   1.016/ 42|   1.016/ 42|   1.016/ 42 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  97   |      53|       2.555|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  71   |       1|       0.091|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  90   |     293|      11.052|   1.013/ 51|   1.013/ 53|   1.013/ 54|   1.013/ 54 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 106   |    8949|     235.516|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  31   |      30|       5.376|   1.086/  8|   1.094/  7|   1.096/  7|   1.098/  7 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  56   |      75|       4.647|   1.004/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  93   |    5127|     268.308|   1.055/ 12|   1.053/ 13|   1.053/ 13|   1.052/ 13 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 104   |    4638|       3.308|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  93   |    2341|      47.393|   1.045/ 15|   1.047/ 15|   1.047/ 15|   1.048/ 14 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  96   |      12|       2.447|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  96   |     109|      26.715|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  97   |      85|       7.605|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 101   |     609|     104.536|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  98   |     658|      63.514|   1.015/ 47|   1.015/ 45|   1.016/ 44|   1.016/ 44 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 101   |    4296|     245.916|   1.009/ 75|   1.008/ 85|   1.008/ 88|   1.008/ 91 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 107   |    2147|      21.410|   1.043/ 16|   1.045/ 15|   1.046/ 15|   1.046/ 15 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  84   |      98|      15.043|   1.042/ 16|   1.045/ 15|   1.045/ 15|   1.046/ 15 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  62   |      32|      23.507|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  79   |     103|       1.047|   1.064/ 11|   1.056/ 12|   1.053/ 13|   1.050/ 14 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  94   |     331|      59.893|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 129   |   30189|     450.068|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  95   |      35|      16.139|   1.035/ 20|   1.036/ 19|   1.036/ 19|   1.037/ 19 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  92   |       1|       0.426|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  80   |      14|       3.840|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 106   |    9029|     108.586|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  94   |      72|       2.370|   1.052/ 13|   1.059/ 12|   1.061/ 11|   1.063/ 11 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 104   |     192|      17.866|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  99   |     693|      41.714|   1.058/ 12|   1.055/ 13|   1.054/ 13|   1.053/ 13 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  69   |      27|       2.219|   1.010/ 68|   1.011/ 63|   1.011/ 62|   1.011/ 61 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  58   |      19|      11.610|   1.028/ 24|   1.033/ 21|   1.034/ 20|   1.035/ 20 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  79   |      97|       8.358|   1.034/ 20|   1.030/ 23|   1.029/ 24|   1.028/ 25 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  89   |     388|      42.366|   1.026/ 27|   1.025/ 28|   1.024/ 28|   1.024/ 28 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|       0.267|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 100   |     589|      60.242|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 104   |   14007|      10.290|   1.034/ 20|   1.033/ 21|   1.032/ 21|   1.032/ 22 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 104   |    2543|       9.526|   1.020/ 34|   1.020/ 35|   1.020/ 35|   1.020/ 35 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 124   |    9521|     114.194|   1.010/ 67|   1.011/ 64|   1.011/ 64|   1.011/ 63 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 111   |     944|      24.127|   1.088/  8|   1.096/  7|   1.098/  7|   1.100/  7 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 104   |    1745|     354.592|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  94   |     309|      33.609|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 123   |   35183|     584.068|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  96   |      10|       3.768|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 131   |    1036|       8.228|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  88   |       9|       0.844|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  90   |     113|       6.062|   1.060/ 11|   1.067/ 10|   1.069/ 10|   1.071/ 10 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  89   |     129|       2.715|   1.030/ 23|   1.029/ 23|   1.029/ 23|   1.029/ 24 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  89   |      34|      18.711|   1.007/ 94|   1.009/ 80|   1.009/ 77|   1.009/ 75 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  80   |     351|      79.430|   1.016/ 43|   1.010/ 67|   1.009/ 77|   1.008/ 91 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  81   |      37|       5.658|   1.043/ 16|   1.047/ 15|   1.048/ 14|   1.049/ 14 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  81   |      30|      15.987|   1.011/ 62|   1.011/ 62|   1.011/ 62|   1.011/ 62 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 105   |      33|       4.804|   1.007/ 99|   1.007/ 96|   1.007/ 96|   1.007/ 95 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  80   |      35|       7.751|   1.008/ 85|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  82   |      11|       1.574|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  94   |      79|      28.282|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  37   |      15|       0.554|   1.035/ 19|   1.041/ 17|   1.042/ 16|   1.043/ 16 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  98   |     122|       3.711|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  86   |     118|       5.822|   1.013/ 52|   1.010/ 70|   1.009/ 76|   1.008/ 84 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  85   |     166|      40.758|   1.042/ 16|   1.037/ 19|   1.035/ 19|   1.034/ 20 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  96   |   23705|     187.274|   1.034/ 20|   1.031/ 22|   1.030/ 23|   1.029/ 23 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  97   |     484|     180.475|   1.022/ 31|   1.022/ 31|   1.022/ 32|   1.022/ 32 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 105   |     217|       6.043|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  29   |       5|       0.168|   1.078/  9|   1.065/ 11|   1.060/ 11|   1.054/ 13 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  38   |      24|       0.802|   1.040/ 17|   1.029/ 24|   1.026/ 26|   1.023/ 30 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 109   |    6186|     354.358|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  86   |      22|       4.451|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  88   |      78|      12.057|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  90   |      68|       3.047|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  92   |     535|       2.593|   1.028/ 25|   1.027/ 25|   1.027/ 25|   1.027/ 25 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  93   |     233|     111.943|   1.032/ 22|   1.035/ 20|   1.035/ 19|   1.036/ 19 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 101   |     245|      45.649|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  84   |     149|      31.858|   1.041/ 17|   1.037/ 19|   1.036/ 19|   1.035/ 20 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  96   |    3777|      17.219|   1.043/ 16|   1.043/ 16|   1.043/ 16|   1.043/ 16 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 104   |     508|     120.431|   1.019/ 36|   1.020/ 35|   1.020/ 35|   1.020/ 34 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  94   |      12|       1.743|   1.003/ **|   1.003/ **|   1.003/ **|   1.004/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  95   |    8402|     261.502|   1.027/ 26|   1.025/ 28|   1.024/ 28|   1.024/ 29 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 142   |    1208|      11.129|   1.008/ 86|   1.007/ 98|   1.007/ **|   1.007/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 103   |    1367|      35.628|   1.011/ 65|   1.011/ 66|   1.010/ 66|   1.010/ 66 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  98   |    1586|     154.338|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  87   |     107|      39.078|   1.042/ 17|   1.036/ 19|   1.035/ 20|   1.033/ 21 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  93   |    1516|      78.121|   1.009/ 80|   1.009/ 80|   1.009/ 80|   1.009/ 80 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  96   |    8879|      60.504|   1.023/ 29|   1.020/ 35|   1.019/ 36|   1.018/ 38 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  24   |       2|       0.162|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  91   |    1346|      39.348|   1.044/ 16|   1.044/ 16|   1.044/ 16|   1.044/ 16 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  83   |      82|       5.086|   1.038/ 18|   1.041/ 17|   1.042/ 16|   1.043/ 16 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  95   |     261|      37.548|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  61   |      54|       6.852|   1.009/ 80|   1.009/ 74|   1.010/ 72|   1.010/ 70 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  94   |      27|       4.663|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  87   |      28|       5.132|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 101   |     110|      52.544|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  76   |      93|       5.852|   1.005/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  88   |    2218|      37.741|   1.046/ 15|   1.041/ 17|   1.040/ 17|   1.039/ 18 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|       1.044|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 112   |   27508|     584.035|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  87   |      11|       0.523|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 102   |     655|      15.433|   1.026/ 26|   1.020/ 35|   1.018/ 38|   1.016/ 42 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 104   |    5276|     510.380|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 110   |    1962|     227.982|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  86   |       7|       0.426|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  84   |      21|       0.376|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 114   |      59|       0.880|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  88   |      13|       1.746|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  90   |       8|       5.865|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  96   |      50|       4.280|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  98   |    5010|      60.244|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 115   |  124569|     378.003|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 102   |    1053|      25.146|   1.016/ 44|   1.014/ 49|   1.014/ 50|   1.013/ 51 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  95   |     309|      31.215|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 104   |   43803|     659.336|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  86   |      25|       6.987|   1.006/ **|   1.007/ 96|   1.007/ 93|   1.008/ 90 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  88   |      21|       0.604|   1.007/ 93|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  88   |      34|       1.060|   1.037/ 19|   1.040/ 17|   1.041/ 17|   1.042/ 17 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  82   |      12|       0.662|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  92   |       4|       0.264|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |

