# State and Country COVID-19 Analysis #
## Updated: 2020-05-30 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  77   |   30226|     1553.74|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  81   |   12097|     1361.99|   1.009/ 74|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  71   |    6995|     1006.53|   1.014/ 50|   1.009/ 76|   1.008/ 88|   1.007/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  72   |    5740|      448.40|   1.016/ 42|   1.010/ 67|   1.009/ 78|   1.007/ 93 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  72   |    5512|      551.97|   1.008/ 84|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  74   |    5539|      437.09|   1.021/ 33|   1.016/ 43|   1.015/ 46|   1.014/ 50 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  87   |    4261|      107.83|   1.019/ 37|   1.016/ 44|   1.015/ 47|   1.014/ 50 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  72   |    4020|     1127.56|   1.012/ 57|   1.008/ 81|   1.008/ 91|   1.007/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  77   |    2851|      613.27|   1.008/ 82|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  72   |    2577|      426.21|   1.019/ 36|   1.014/ 48|   1.013/ 52|   1.012/ 57 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  91   |  108076|      327.96|   1.011/ 60|   1.008/ 85|   1.007/ 95|   1.006/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  80   |   39465|      594.04|   1.008/ 84|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  99   |   34217|      568.03|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 105   |   29997|      447.21|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  74   |   29487|      139.48|   1.047/ 15|   1.042/ 16|   1.041/ 17|   1.040/ 17 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  88   |   28542|      605.97|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  80   |    9656|      837.83|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  72   |    9800|       77.43|   1.052/ 13|   1.048/ 14|   1.047/ 14|   1.046/ 15 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  82   |    8705|      104.69|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 100   |    7782|       93.33|   1.007/ 96|   1.006/ **|   1.006/ **|   1.006/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  66   |     629|      128.21|   1.019/ 36|   1.014/ 50|   1.012/ 56|   1.011/ 62 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  66   |      10|       13.76|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  70   |     939|      128.95|   1.023/ 29|   1.016/ 43|   1.014/ 48|   1.012/ 55 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  67   |     127|       42.02|   1.019/ 37|   1.019/ 37|   1.019/ 37|   1.019/ 37 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  87   |    4261|      107.83|   1.019/ 37|   1.016/ 44|   1.015/ 47|   1.014/ 50 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  77   |    1492|      259.05|   1.018/ 39|   1.015/ 46|   1.014/ 48|   1.014/ 50 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  72   |    4020|     1127.56|   1.012/ 57|   1.008/ 81|   1.008/ 91|   1.007/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  65   |     372|      382.44|   1.020/ 34|   1.014/ 48|   1.013/ 54|   1.011/ 61 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  83   |    2508|      116.75|   1.016/ 42|   1.013/ 54|   1.012/ 57|   1.011/ 62 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  79   |    2028|      191.02|   1.017/ 41|   1.015/ 46|   1.015/ 48|   1.014/ 49 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  60   |      17|       12.01|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  65   |      83|       46.34|   1.010/ 71|   1.009/ 73|   1.009/ 74|   1.009/ 75 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  74   |    5539|      437.09|   1.021/ 33|   1.016/ 43|   1.015/ 46|   1.014/ 50 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  75   |    2205|      327.59|   1.015/ 46|   1.010/ 69|   1.009/ 79|   1.007/ 93 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  66   |     542|      171.92|   1.035/ 20|   1.031/ 22|   1.030/ 23|   1.029/ 24 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  78   |     224|       77.05|   1.009/ 77|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  75   |     427|       95.53|   1.015/ 47|   1.012/ 56|   1.012/ 59|   1.011/ 63 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  77   |    2851|      613.27|   1.008/ 82|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  64   |      83|       62.08|   1.015/ 45|   1.016/ 42|   1.017/ 42|   1.017/ 41 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  72   |    2577|      426.21|   1.019/ 36|   1.014/ 48|   1.013/ 52|   1.012/ 57 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  71   |    6995|     1006.53|   1.014/ 50|   1.009/ 76|   1.008/ 88|   1.007/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  72   |    5512|      551.97|   1.008/ 84|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  70   |    1033|      183.09|   1.028/ 25|   1.023/ 30|   1.022/ 31|   1.021/ 33 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  72   |     729|      244.93|   1.026/ 27|   1.023/ 30|   1.022/ 31|   1.021/ 32 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  72   |     768|      125.15|   1.016/ 43|   1.010/ 67|   1.009/ 78|   1.007/ 94 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  64   |      17|       15.53|   1.005/ **|   1.008/ 91|   1.008/ 84|   1.009/ 77 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  63   |     169|       87.52|   1.028/ 25|   1.024/ 28|   1.023/ 29|   1.022/ 31 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  75   |     424|      137.61|   1.013/ 53|   1.010/ 71|   1.009/ 78|   1.008/ 86 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  68   |     250|      183.88|   1.030/ 23|   1.023/ 29|   1.022/ 32|   1.020/ 34 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  81   |   12097|     1361.99|   1.009/ 74|   1.005/ **|   1.004/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  66   |     364|      173.42|   1.025/ 28|   1.018/ 39|   1.016/ 43|   1.014/ 48 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  77   |   30226|     1553.74|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  66   |     899|       85.72|   1.024/ 28|   1.023/ 30|   1.022/ 31|   1.022/ 31 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  64   |      61|       79.88|   1.025/ 28|   1.020/ 35|   1.018/ 37|   1.017/ 40 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  71   |    2211|      189.16|   1.022/ 31|   1.019/ 37|   1.018/ 39|   1.017/ 41 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  72   |     331|       83.59|   1.010/ 69|   1.009/ 80|   1.008/ 82|   1.008/ 85 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  76   |     157|       37.23|   1.008/ 92|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  72   |    5740|      448.40|   1.016/ 42|   1.010/ 67|   1.009/ 78|   1.007/ 93 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  70   |     136|       42.48|   1.008/ 92|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  63   |     690|      651.62|   1.027/ 26|   1.026/ 27|   1.026/ 27|   1.026/ 27 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  75   |     486|       94.48|   1.018/ 38|   1.016/ 43|   1.016/ 44|   1.015/ 46 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  80   |      63|       71.45|   1.022/ 32|   1.016/ 43|   1.015/ 47|   1.013/ 52 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  70   |     368|       53.82|   1.018/ 38|   1.017/ 42|   1.016/ 43|   1.016/ 44 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  74   |    1711|       59.02|   1.019/ 37|   1.015/ 47|   1.014/ 50|   1.013/ 54 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  69   |     111|       34.75|   1.024/ 28|   1.021/ 33|   1.020/ 34|   1.020/ 35 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  71   |      55|       87.75|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  77   |    1375|      161.13|   1.025/ 28|   1.022/ 32|   1.021/ 33|   1.020/ 34 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  91   |    1137|      149.31|   1.009/ 79|   1.007/ 95|   1.007/ **|   1.007/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  61   |      78|       43.50|   1.013/ 52|   1.008/ 85|   1.007/ **|   1.005/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  71   |     562|       96.55|   1.018/ 39|   1.017/ 41|   1.017/ 41|   1.016/ 42 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  47   |      15|       26.75|   1.035/ 20|   1.046/ 15|   1.048/ 14|   1.051/ 14 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  69   |     260|        8.07|   1.034/ 20|   1.028/ 25|   1.026/ 26|   1.025/ 28 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  80   |      32|       11.37|   1.004/ **|   1.005/ **|   1.006/ **|   1.006/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  79   |     638|       14.83|   1.013/ 54|   1.013/ 53|   1.013/ 53|   1.013/ 53 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  62   |       2|        0.06|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  83   |     528|       11.75|   1.028/ 25|   1.027/ 26|   1.027/ 26|   1.026/ 26 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  65   |     104|       35.12|   1.058/ 12|   1.067/ 10|   1.069/ 10|   1.072/  9 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  90   |     105|        4.09|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  79   |     657|       73.78|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  78   |      57|        5.69|   1.034/ 20|   1.035/ 20|   1.035/ 19|   1.036/ 19 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  75   |      15|       10.01|   1.028/ 25|   1.030/ 23|   1.031/ 22|   1.031/ 22 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  73   |     598|        3.55|   1.051/ 14|   1.052/ 13|   1.052/ 13|   1.052/ 13 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  60   |     229|       24.37|   1.027/ 26|   1.023/ 29|   1.023/ 31|   1.022/ 32 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  80   |    9656|      837.83|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  54   |       2|        0.17|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  62   |     317|       27.66|   1.049/ 14|   1.044/ 16|   1.043/ 16|   1.042/ 17 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  70   |     165|       49.96|   1.016/ 42|   1.009/ 76|   1.007/ 95|   1.006/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  60   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  74   |   29487|      139.48|   1.047/ 15|   1.042/ 16|   1.041/ 17|   1.040/ 17 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  80   |     143|       20.63|   1.020/ 35|   1.017/ 41|   1.016/ 43|   1.015/ 46 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  73   |      54|        2.57|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  47   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  66   |     187|        7.06|   1.021/ 33|   1.019/ 37|   1.018/ 38|   1.017/ 40 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  82   |    7540|      198.43|   1.016/ 43|   1.011/ 66|   1.009/ 76|   1.008/ 89 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  32   |      66|        4.04|   1.020/ 34|   1.017/ 42|   1.016/ 44|   1.015/ 45 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  69   |     921|       48.19|   1.062/ 11|   1.068/ 10|   1.069/ 10|   1.070/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  80   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  69   |     861|       17.43|   1.033/ 21|   1.032/ 22|   1.031/ 22|   1.031/ 22 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  72   |      11|        2.23|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  72   |     105|       25.65|   1.006/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  73   |      84|        7.53|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  77   |     581|       99.74|   1.003/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  74   |     497|       47.96|   1.011/ 65|   1.008/ 85|   1.007/ 92|   1.007/ ** |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  77   |    3801|      217.60|   1.022/ 31|   1.014/ 48|   1.013/ 55|   1.011/ 65 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  83   |     871|        8.69|   1.027/ 26|   1.026/ 26|   1.026/ 27|   1.026/ 27 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  60   |      43|        6.70|   1.040/ 17|   1.031/ 22|   1.029/ 24|   1.027/ 26 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  38   |      13|        9.88|   1.052/ 13|   1.033/ 21|   1.027/ 26|   1.019/ 36 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  55   |       6|        0.06|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  70   |     325|       58.84|   1.006/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 105   |   29997|      447.21|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  71   |      16|        7.14|   1.026/ 27|   1.021/ 33|   1.020/ 35|   1.019/ 37 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  68   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  56   |      12|        3.32|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  82   |    8705|      104.69|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  70   |      37|        1.22|   1.021/ 32|   1.016/ 44|   1.014/ 49|   1.013/ 55 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  80   |     178|       16.58|   1.007/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  75   |      77|        4.62|   1.070/ 10|   1.078/  9|   1.080/  9|   1.082/  8 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  45   |      22|        1.83|   1.028/ 24|   1.019/ 36|   1.017/ 40|   1.015/ 46 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  34   |       8|        5.05|   1.067/ 10|   1.039/ 18|   1.033/ 21|   1.028/ 24 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  55   |      35|        3.01|   1.049/ 14|   1.050/ 14|   1.051/ 13|   1.052/ 13 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  65   |     205|       22.34|   1.030/ 23|   1.027/ 25|   1.027/ 26|   1.026/ 26 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  76   |     531|       54.29|   1.011/ 63|   1.008/ 89|   1.007/ 98|   1.006/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  80   |    5181|        3.81|   1.042/ 16|   1.037/ 18|   1.036/ 19|   1.035/ 20 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  80   |    1527|        5.72|   1.024/ 28|   1.025/ 28|   1.025/ 28|   1.025/ 27 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 100   |    7782|       93.33|   1.007/ 96|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  87   |     173|        4.43|   1.031/ 22|   1.035/ 20|   1.036/ 19|   1.037/ 19 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  80   |    1690|      343.42|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  70   |     292|       31.73|   1.005/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  99   |   34217|      568.03|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  72   |       9|        3.33|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 107   |    1006|        7.99|   1.015/ 47|   1.009/ 78|   1.007/ 94|   1.006/ ** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  64   |       9|        0.84|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  66   |      38|        2.01|   1.008/ 83|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  65   |      62|        1.31|   1.026/ 26|   1.017/ 41|   1.015/ 47|   1.012/ 56 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  65   |      30|       16.85|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  56   |     207|       46.87|   1.055/ 12|   1.041/ 17|   1.037/ 19|   1.034/ 20 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  57   |      16|        2.48|   1.016/ 42|   1.016/ 42|   1.016/ 42|   1.017/ 42 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  57   |      24|       12.51|   1.016/ 42|   1.018/ 38|   1.018/ 38|   1.019/ 37 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  81   |      26|        3.86|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  56   |      28|        6.17|   1.019/ 36|   1.022/ 32|   1.022/ 31|   1.023/ 30 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  58   |       3|        0.44|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  70   |      68|       24.50|   1.016/ 42|   1.017/ 42|   1.017/ 41|   1.017/ 41 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  13   |       2|        0.08|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  74   |     117|        3.58|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  62   |      77|        3.81|   1.033/ 21|   1.029/ 24|   1.027/ 25|   1.026/ 26 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  61   |      18|        4.32|   1.145/  5|   1.387/  2|   1.283/  2|   1.154/  4 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  72   |    9800|       77.43|   1.052/ 13|   1.048/ 14|   1.047/ 14|   1.046/ 15 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  73   |     296|      110.23|   1.028/ 25|   1.025/ 27|   1.025/ 28|   1.024/ 29 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  81   |     205|        5.71|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  14   |       6|        0.19|   1.145/  5|   1.101/  7|   1.101/  7|   1.101/  7 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  85   |    6092|      348.99|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  62   |      22|        4.32|   1.004/ **|   1.006/ **|   1.007/ **|   1.007/ 96 |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  64   |      34|        5.26|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  66   |      68|        3.03|   1.016/ 42|   1.012/ 59|   1.010/ 66|   1.009/ 75 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  68   |     280|        1.36|   1.032/ 21|   1.024/ 29|   1.022/ 31|   1.020/ 34 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  69   |     123|       59.33|   1.017/ 42|   1.017/ 40|   1.017/ 40|   1.018/ 39 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  77   |     241|       44.82|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  60   |      45|        9.55|   1.049/ 14|   1.044/ 16|   1.043/ 16|   1.041/ 17 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  72   |    1370|        6.25|   1.034/ 20|   1.029/ 24|   1.028/ 25|   1.027/ 26 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  80   |     336|       79.72|   1.015/ 47|   1.012/ 59|   1.011/ 63|   1.010/ 67 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  70   |      11|        1.58|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  71   |    4388|      136.58|   1.041/ 17|   1.036/ 19|   1.035/ 20|   1.034/ 20 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 118   |    1022|        9.42|   1.011/ 61|   1.008/ 84|   1.007/ 92|   1.007/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  79   |    1096|       28.55|   1.012/ 58|   1.008/ 84|   1.007/ 94|   1.007/ ** |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  74   |    1388|      135.10|   1.010/ 68|   1.010/ 72|   1.010/ 73|   1.009/ 74 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  63   |      30|       10.75|   1.070/ 10|   1.089/  8|   1.094/  7|   1.099/  7 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  69   |    1292|       66.58|   1.012/ 59|   1.008/ 92|   1.007/ **|   1.005/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  72   |    4434|       30.21|   1.043/ 16|   1.039/ 17|   1.039/ 18|   1.038/ 18 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  67   |     459|       13.40|   1.032/ 21|   1.031/ 22|   1.031/ 22|   1.030/ 23 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  59   |      43|        2.66|   1.040/ 17|   1.029/ 24|   1.026/ 26|   1.023/ 30 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  71   |     248|       35.64|   1.005/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  37   |      47|        5.98|   1.040/ 17|   1.029/ 24|   1.026/ 26|   1.023/ 29 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  70   |      24|        4.20|   1.005/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  63   |      29|        5.23|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  77   |     110|       52.31|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  52   |      71|        4.45|   1.021/ 33|   1.022/ 31|   1.023/ 30|   1.023/ 30 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  64   |     601|       10.22|   1.067/ 10|   1.071/ 10|   1.072/  9|   1.073/  9 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  88   |   28542|      605.97|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  63   |      10|        0.45|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  78   |     218|        5.13|   1.058/ 12|   1.053/ 13|   1.052/ 13|   1.050/ 14 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  80   |    4437|      429.16|   1.015/ 47|   1.012/ 57|   1.012/ 59|   1.011/ 62 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  86   |    1954|      227.05|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  62   |       4|        0.24|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  60   |      21|        0.38|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  90   |      57|        0.86|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  64   |      13|        1.77|   1.012/ 59|   1.011/ 65|   1.010/ 67|   1.010/ 68 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  66   |       8|        5.87|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  72   |      49|        4.16|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  74   |    4592|       55.22|   1.008/ 91|   1.005/ **|   1.005/ **|   1.004/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  91   |  108076|      327.96|   1.011/ 60|   1.008/ 85|   1.007/ 95|   1.006/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  78   |     733|       17.50|   1.027/ 26|   1.022/ 31|   1.021/ 33|   1.020/ 35 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  71   |     277|       28.03|   1.014/ 49|   1.005/ **|   1.003/ **|   1.001/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  80   |   39465|      594.04|   1.008/ 84|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  62   |      22|        6.38|   1.009/ 74|   1.008/ 83|   1.008/ 85|   1.008/ 88 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  64   |      14|        0.42|   1.016/ 44|   1.015/ 47|   1.014/ 48|   1.014/ 49 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  64   |      10|        0.32|   1.009/ 77|   1.014/ 50|   1.015/ 46|   1.016/ 42 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  58   |       7|        0.41|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  68   |       4|        0.26|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |

