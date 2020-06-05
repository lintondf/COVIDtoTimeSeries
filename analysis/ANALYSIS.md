# State and Country COVID-19 Analysis #
## Updated: 2020-06-05 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  83   |   30616|     1573.81|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  87   |   12419|     1398.23|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  77   |    7385|     1062.62|   1.012/ 59|   1.009/ 77|   1.008/ 82|   1.008/ 89 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  78   |    6046|      472.29|   1.013/ 55|   1.009/ 80|   1.008/ 89|   1.007/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  80   |    5967|      470.86|   1.016/ 43|   1.012/ 57|   1.011/ 61|   1.010/ 66 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  78   |    5700|      570.76|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  93   |    4636|      117.33|   1.016/ 42|   1.014/ 50|   1.013/ 53|   1.012/ 56 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  78   |    4174|     1170.60|   1.008/ 83|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  83   |    2939|      632.23|   1.007/ 99|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  78   |    2772|      458.47|   1.015/ 46|   1.012/ 58|   1.011/ 63|   1.010/ 68 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  97   |  112932|      342.69|   1.009/ 75|   1.007/ **|   1.006/ **|   1.005/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  86   |   40629|      611.55|   1.008/ 92|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  80   |   36189|      171.18|   1.039/ 18|   1.034/ 20|   1.032/ 21|   1.031/ 22 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 105   |   34551|      573.57|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 111   |   30068|      448.27|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  94   |   27899|      592.33|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  78   |   12577|       99.36|   1.047/ 15|   1.043/ 16|   1.043/ 16|   1.042/ 16 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  86   |    9727|      844.02|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  88   |    8822|      106.10|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 106   |    8113|       97.31|   1.007/ 93|   1.007/ 99|   1.007/ **|   1.007/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  72   |     682|      139.03|   1.016/ 44|   1.013/ 55|   1.012/ 58|   1.011/ 62 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  72   |      10|       13.69|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  76   |    1026|      140.97|   1.020/ 34|   1.016/ 43|   1.015/ 46|   1.014/ 49 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  73   |     144|       47.67|   1.021/ 33|   1.022/ 31|   1.023/ 30|   1.023/ 30 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  93   |    4636|      117.33|   1.016/ 42|   1.014/ 50|   1.013/ 53|   1.012/ 56 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  83   |    1581|      274.59|   1.012/ 56|   1.009/ 74|   1.009/ 81|   1.008/ 89 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  78   |    4174|     1170.60|   1.008/ 83|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  71   |     398|      408.78|   1.015/ 46|   1.010/ 66|   1.009/ 74|   1.008/ 84 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  89   |    2688|      125.14|   1.014/ 49|   1.012/ 60|   1.011/ 63|   1.010/ 67 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  85   |    2203|      207.49|   1.015/ 47|   1.013/ 52|   1.013/ 54|   1.012/ 56 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  66   |      17|       12.01|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  71   |      85|       47.66|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  80   |    5967|      470.86|   1.016/ 43|   1.012/ 57|   1.011/ 61|   1.010/ 66 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  81   |    2320|      344.58|   1.012/ 58|   1.009/ 81|   1.008/ 90|   1.007/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  72   |     620|      196.57|   1.026/ 26|   1.021/ 33|   1.020/ 35|   1.019/ 37 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  84   |     231|       79.15|   1.008/ 91|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  81   |     463|      103.71|   1.015/ 47|   1.013/ 52|   1.013/ 53|   1.013/ 55 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  83   |    2939|      632.23|   1.007/ 99|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  70   |      94|       70.11|   1.019/ 37|   1.021/ 33|   1.021/ 32|   1.022/ 32 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  78   |    2772|      458.47|   1.015/ 46|   1.012/ 58|   1.011/ 63|   1.010/ 68 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  77   |    7385|     1062.62|   1.012/ 59|   1.009/ 77|   1.008/ 82|   1.008/ 89 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  78   |    5700|      570.76|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  76   |    1170|      207.44|   1.023/ 30|   1.020/ 35|   1.019/ 37|   1.018/ 39 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  78   |     820|      275.40|   1.023/ 30|   1.021/ 33|   1.020/ 34|   1.020/ 35 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  78   |     831|      135.40|   1.014/ 48|   1.011/ 63|   1.010/ 68|   1.009/ 75 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  70   |      17|       16.00|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  69   |     188|       97.02|   1.020/ 34|   1.015/ 45|   1.014/ 49|   1.013/ 54 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  81   |     444|      144.19|   1.010/ 70|   1.007/ 95|   1.007/ **|   1.006/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  74   |     280|      205.84|   1.025/ 27|   1.021/ 32|   1.020/ 34|   1.019/ 36 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  87   |   12419|     1398.23|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  72   |     398|      189.69|   1.019/ 36|   1.015/ 47|   1.013/ 51|   1.012/ 56 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  83   |   30616|     1573.81|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  72   |    1021|       97.38|   1.022/ 32|   1.020/ 34|   1.020/ 35|   1.020/ 35 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  70   |      68|       89.33|   1.023/ 30|   1.021/ 34|   1.020/ 35|   1.019/ 36 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  77   |    2415|      206.63|   1.018/ 38|   1.015/ 45|   1.015/ 47|   1.014/ 50 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  78   |     348|       87.87|   1.009/ 77|   1.008/ 85|   1.008/ 88|   1.008/ 90 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  82   |     162|       38.32|   1.007/ 95|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  78   |    6046|      472.29|   1.013/ 55|   1.009/ 80|   1.008/ 89|   1.007/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  76   |     141|       44.13|   1.008/ 87|   1.007/ **|   1.007/ **|   1.006/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  69   |     782|      738.40|   1.021/ 32|   1.019/ 36|   1.019/ 37|   1.018/ 38 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  81   |     525|      102.05|   1.014/ 51|   1.011/ 62|   1.010/ 66|   1.010/ 70 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  86   |      69|       78.01|   1.018/ 38|   1.014/ 49|   1.013/ 53|   1.012/ 58 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  76   |     399|       58.45|   1.016/ 42|   1.015/ 45|   1.015/ 46|   1.015/ 47 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  80   |    1839|       63.43|   1.015/ 46|   1.012/ 58|   1.011/ 62|   1.010/ 67 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  75   |     123|       38.45|   1.019/ 37|   1.015/ 47|   1.014/ 50|   1.013/ 53 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  77   |      55|       88.51|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  83   |    1520|      178.03|   1.018/ 38|   1.015/ 47|   1.014/ 50|   1.013/ 53 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  97   |    1175|      154.32|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  67   |      80|       44.84|   1.010/ 71|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  77   |     628|      107.92|   1.018/ 39|   1.017/ 40|   1.017/ 40|   1.017/ 40 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  53   |      18|       31.87|   1.031/ 22|   1.028/ 24|   1.027/ 25|   1.026/ 26 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  75   |     305|        9.45|   1.032/ 21|   1.029/ 24|   1.028/ 24|   1.027/ 25 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  86   |      33|       11.64|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  85   |     686|       15.95|   1.012/ 57|   1.012/ 58|   1.012/ 58|   1.012/ 59 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  68   |       4|        0.14|   1.022/ 31|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  89   |     612|       13.61|   1.026/ 26|   1.025/ 28|   1.025/ 28|   1.024/ 28 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  71   |     165|       55.67|   1.069/ 10|   1.078/  9|   1.081/  8|   1.083/  8 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  96   |     105|        4.07|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  85   |     673|       75.56|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  84   |      73|        7.30|   1.042/ 16|   1.045/ 15|   1.046/ 15|   1.047/ 15 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  81   |      20|       12.91|   1.037/ 19|   1.040/ 17|   1.041/ 17|   1.042/ 16 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  79   |     792|        4.70|   1.049/ 14|   1.048/ 14|   1.048/ 14|   1.048/ 14 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  66   |     260|       27.59|   1.023/ 30|   1.020/ 34|   1.019/ 36|   1.019/ 37 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  86   |    9727|      844.02|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  60   |       3|        0.28|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  68   |     411|       35.83|   1.050/ 14|   1.049/ 14|   1.049/ 14|   1.049/ 14 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  76   |     168|       50.91|   1.009/ 77|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  66   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  80   |   36189|      171.18|   1.039/ 18|   1.034/ 20|   1.032/ 21|   1.031/ 22 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  86   |     155|       22.32|   1.016/ 44|   1.013/ 54|   1.012/ 57|   1.011/ 61 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  79   |      54|        2.58|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  53   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  72   |     209|        7.86|   1.021/ 33|   1.019/ 36|   1.019/ 36|   1.019/ 37 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  88   |    8043|      211.68|   1.013/ 51|   1.010/ 70|   1.009/ 76|   1.008/ 84 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  13   |       4|        0.76|   1.000/ --|   1.587/  1|   1.260/  2|   1.000/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  38   |      67|        4.15|   1.011/ 65|   1.004/ **|   1.003/ **|   1.001/ ** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  75   |    1340|       70.12|   1.063/ 11|   1.065/ 10|   1.066/ 10|   1.066/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  86   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  75   |    1067|       21.60|   1.037/ 19|   1.038/ 18|   1.039/ 18|   1.039/ 18 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  78   |      11|        2.18|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  78   |     106|       25.96|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  79   |      85|        7.55|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  83   |     587|      100.86|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  80   |     526|       50.75|   1.011/ 66|   1.009/ 73|   1.009/ 75|   1.009/ 77 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  83   |    3876|      221.87|   1.013/ 54|   1.006/ **|   1.004/ **|   1.003/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  89   |    1070|       10.67|   1.034/ 20|   1.036/ 19|   1.037/ 19|   1.037/ 18 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  66   |      53|        8.23|   1.037/ 19|   1.033/ 21|   1.032/ 21|   1.032/ 22 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  44   |      13|        9.45|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  61   |       9|        0.09|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  76   |     329|       59.53|   1.004/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 111   |   30068|      448.27|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  77   |      20|        9.06|   1.055/ 12|   1.062/ 11|   1.063/ 11|   1.065/ 11 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  74   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  62   |      13|        3.38|   1.005/ **|   1.005/ **|   1.005/ **|   1.006/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  88   |    8822|      106.10|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  76   |      40|        1.32|   1.017/ 39|   1.013/ 52|   1.012/ 57|   1.011/ 62 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  86   |     183|       17.07|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  81   |     135|        8.12|   1.086/  8|   1.095/  7|   1.097/  7|   1.100/  7 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  51   |      24|        1.98|   1.018/ 39|   1.010/ 69|   1.008/ 86|   1.006/ ** |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  40   |       9|        5.32|   1.029/ 23|   1.008/ 90|   1.002/ **|   1.000/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  61   |      50|        4.33|   1.054/ 13|   1.056/ 12|   1.057/ 12|   1.058/ 12 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  71   |     241|       26.28|   1.030/ 23|   1.030/ 23|   1.030/ 23|   1.029/ 23 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  82   |     554|       56.67|   1.009/ 80|   1.006/ **|   1.006/ **|   1.005/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  86   |    6500|        4.78|   1.041/ 17|   1.039/ 18|   1.039/ 18|   1.038/ 18 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  86   |    1755|        6.57|   1.023/ 30|   1.022/ 31|   1.022/ 31|   1.022/ 31 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 106   |    8113|       97.31|   1.007/ 93|   1.007/ 99|   1.007/ **|   1.007/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  93   |     216|        5.52|   1.045/ 15|   1.051/ 13|   1.053/ 13|   1.054/ 13 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  86   |    1707|      346.83|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  76   |     294|       32.04|   1.004/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 105   |   34551|      573.57|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  78   |       9|        3.39|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 113   |    1042|        8.27|   1.009/ 78|   1.004/ **|   1.003/ **|   1.001/ ** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  70   |       9|        0.84|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  72   |      43|        2.28|   1.027/ 26|   1.034/ 20|   1.036/ 19|   1.038/ 18 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  71   |      74|        1.56|   1.032/ 22|   1.031/ 22|   1.031/ 22|   1.031/ 22 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  71   |      30|       16.89|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  62   |     255|       57.65|   1.042/ 16|   1.033/ 21|   1.030/ 23|   1.028/ 25 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  63   |      18|        2.77|   1.024/ 29|   1.029/ 23|   1.031/ 22|   1.032/ 21 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  63   |      25|       13.24|   1.011/ 65|   1.008/ 81|   1.008/ 88|   1.007/ 95 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  87   |      27|        3.94|   1.003/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  62   |      29|        6.53|   1.013/ 54|   1.010/ 70|   1.009/ 77|   1.008/ 86 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  64   |       5|        0.75|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  76   |      74|       26.43|   1.012/ 56|   1.011/ 64|   1.010/ 67|   1.010/ 70 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  19   |       6|        0.23|   1.261/  2|   1.121/  6|   1.027/ 26|   1.000/ -- |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  80   |     117|        3.57|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  68   |      87|        4.32|   1.025/ 28|   1.019/ 36|   1.018/ 39|   1.016/ 42 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  67   |      39|        9.57|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  78   |   12577|       99.36|   1.047/ 15|   1.043/ 16|   1.043/ 16|   1.042/ 16 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  79   |     332|      123.93|   1.022/ 32|   1.018/ 38|   1.017/ 40|   1.016/ 42 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  87   |     209|        5.82|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  11   |       2|        0.07|   1.260/  2|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  20   |      10|        0.33|   1.126/  5|   1.095/  7|   1.075/  9|   1.055/ 12 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  91   |    6137|      351.55|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  68   |      22|        4.43|   1.003/ **|   1.003/ **|   1.004/ **|   1.004/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  70   |      53|        8.22|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  72   |      69|        3.11|   1.008/ 81|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  74   |     331|        1.61|   1.032/ 22|   1.029/ 24|   1.029/ 24|   1.028/ 25 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  75   |     143|       68.87|   1.023/ 30|   1.025/ 27|   1.026/ 27|   1.026/ 26 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  83   |     241|       44.81|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  66   |      63|       13.48|   1.067/ 10|   1.072/  9|   1.074/  9|   1.075/  9 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  78   |    1722|        7.85|   1.040/ 17|   1.040/ 17|   1.041/ 17|   1.041/ 17 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  86   |     365|       86.50|   1.015/ 45|   1.014/ 48|   1.014/ 49|   1.014/ 50 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  76   |      11|        1.56|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  77   |    5293|      164.73|   1.034/ 20|   1.030/ 23|   1.029/ 24|   1.028/ 25 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 124   |    1070|        9.86|   1.009/ 75|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  85   |    1147|       29.90|   1.010/ 68|   1.008/ 87|   1.007/ 94|   1.007/ ** |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  80   |    1469|      142.91|   1.010/ 72|   1.009/ 75|   1.009/ 76|   1.009/ 77 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  69   |      47|       16.94|   1.066/ 10|   1.073/  9|   1.075/  9|   1.076/  9 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  75   |    1340|       69.03|   1.009/ 80|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  78   |    5559|       37.88|   1.040/ 17|   1.037/ 18|   1.037/ 19|   1.036/ 19 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  73   |     578|       16.90|   1.039/ 17|   1.042/ 17|   1.042/ 16|   1.043/ 16 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  65   |      48|        2.98|   1.028/ 25|   1.019/ 36|   1.017/ 40|   1.015/ 45 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  77   |     250|       35.91|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  43   |      49|        6.19|   1.020/ 35|   1.006/ **|   1.002/ **|   1.000/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  76   |      24|        4.26|   1.005/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  69   |      28|        5.19|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  83   |     110|       52.69|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  58   |      81|        5.12|   1.021/ 33|   1.021/ 33|   1.021/ 33|   1.021/ 33 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  70   |     865|       14.71|   1.062/ 11|   1.062/ 11|   1.061/ 11|   1.061/ 11 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  94   |   27899|      592.33|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  69   |      11|        0.49|   1.012/ 58|   1.016/ 44|   1.017/ 41|   1.018/ 39 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  84   |     337|        7.94|   1.062/ 11|   1.060/ 11|   1.059/ 12|   1.059/ 12 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  86   |    4709|      455.52|   1.011/ 61|   1.009/ 74|   1.009/ 79|   1.008/ 83 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  92   |    1951|      226.74|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  68   |       5|        0.31|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  66   |      21|        0.38|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  96   |      58|        0.87|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  70   |      14|        1.80|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  72   |       8|        5.87|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  78   |      49|        4.20|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  80   |    4720|       56.76|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  97   |  112932|      342.69|   1.009/ 75|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  84   |     812|       19.39|   1.021/ 34|   1.016/ 44|   1.015/ 47|   1.013/ 51 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  77   |     285|       28.80|   1.009/ 75|   1.004/ **|   1.003/ **|   1.001/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  86   |   40629|      611.55|   1.008/ 92|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  68   |      23|        6.65|   1.008/ 85|   1.007/ 95|   1.007/ 99|   1.007/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  70   |      16|        0.47|   1.017/ 41|   1.017/ 41|   1.017/ 41|   1.017/ 41 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  70   |      11|        0.34|   1.047/ 14|   1.063/ 11|   1.067/ 10|   1.072/ 10 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  64   |       7|        0.39|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  74   |       4|        0.26|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |

