# State and Country COVID-19 Analysis #
## Updated: 2020-06-01 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  79   |   30366|     1560.97|   1.004/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  83   |   12221|     1375.90|   1.009/ 81|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  73   |    7107|     1022.68|   1.012/ 55|   1.008/ 83|   1.007/ 94|   1.006/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  74   |    5851|      457.04|   1.015/ 46|   1.010/ 68|   1.009/ 78|   1.008/ 90 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  74   |    5581|      558.83|   1.008/ 88|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  76   |    5691|      449.11|   1.019/ 37|   1.014/ 48|   1.013/ 52|   1.012/ 56 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  89   |    4389|      111.09|   1.018/ 38|   1.015/ 45|   1.015/ 48|   1.014/ 50 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  74   |    4082|     1144.94|   1.011/ 62|   1.008/ 87|   1.007/ 97|   1.006/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  79   |    2880|      619.58|   1.008/ 89|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  74   |    2645|      437.57|   1.018/ 39|   1.014/ 51|   1.013/ 55|   1.012/ 60 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  93   |  109783|      333.14|   1.011/ 65|   1.008/ 90|   1.007/ 99|   1.006/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  82   |   39770|      598.63|   1.008/ 90|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 101   |   34346|      570.17|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  76   |   31760|      150.23|   1.044/ 15|   1.039/ 18|   1.038/ 18|   1.036/ 19 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 107   |   30023|      447.60|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  90   |   28306|      600.96|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  74   |   10664|       84.25|   1.049/ 14|   1.045/ 15|   1.043/ 16|   1.042/ 16 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  82   |    9683|      840.25|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  84   |    8751|      105.25|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 102   |    7885|       94.57|   1.007/ 97|   1.006/ **|   1.006/ **|   1.006/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  68   |     647|      131.87|   1.019/ 37|   1.014/ 48|   1.014/ 51|   1.013/ 55 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  68   |      10|       13.73|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  72   |     966|      132.76|   1.022/ 31|   1.016/ 43|   1.014/ 48|   1.013/ 53 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  69   |     132|       43.85|   1.021/ 33|   1.022/ 32|   1.022/ 31|   1.023/ 31 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  89   |    4389|      111.09|   1.018/ 38|   1.015/ 45|   1.015/ 48|   1.014/ 50 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  79   |    1525|      264.90|   1.016/ 44|   1.013/ 55|   1.012/ 58|   1.011/ 62 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  74   |    4082|     1144.94|   1.011/ 62|   1.008/ 87|   1.007/ 97|   1.006/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  67   |     382|      392.23|   1.019/ 36|   1.014/ 50|   1.012/ 56|   1.011/ 62 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  85   |    2569|      119.63|   1.016/ 44|   1.013/ 55|   1.012/ 59|   1.011/ 63 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  81   |    2086|      196.46|   1.016/ 43|   1.014/ 49|   1.014/ 50|   1.013/ 52 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  62   |      17|       12.01|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  67   |      84|       46.90|   1.008/ 84|   1.007/ 97|   1.007/ **|   1.007/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  76   |    5691|      449.11|   1.019/ 37|   1.014/ 48|   1.013/ 52|   1.012/ 56 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  77   |    2245|      333.45|   1.014/ 49|   1.010/ 72|   1.009/ 81|   1.007/ 92 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  68   |     570|      180.64|   1.032/ 22|   1.027/ 26|   1.026/ 27|   1.025/ 28 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  80   |     226|       77.53|   1.007/ 96|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  77   |     439|       98.32|   1.016/ 44|   1.014/ 49|   1.014/ 51|   1.013/ 52 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  79   |    2880|      619.58|   1.008/ 89|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  66   |      87|       64.73|   1.017/ 40|   1.019/ 36|   1.020/ 35|   1.020/ 34 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  74   |    2645|      437.57|   1.018/ 39|   1.014/ 51|   1.013/ 55|   1.012/ 60 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  73   |    7107|     1022.68|   1.012/ 55|   1.008/ 83|   1.007/ 94|   1.006/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  74   |    5581|      558.83|   1.008/ 88|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  72   |    1082|      191.87|   1.027/ 25|   1.024/ 29|   1.023/ 30|   1.022/ 31 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  74   |     760|      255.20|   1.025/ 28|   1.022/ 31|   1.022/ 32|   1.021/ 33 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  74   |     794|      129.30|   1.018/ 38|   1.015/ 47|   1.014/ 50|   1.013/ 53 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  66   |      17|       15.74|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  65   |     177|       91.38|   1.027/ 26|   1.023/ 30|   1.022/ 31|   1.021/ 32 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  77   |     432|      140.18|   1.012/ 57|   1.009/ 76|   1.008/ 83|   1.008/ 91 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  70   |     259|      190.81|   1.027/ 25|   1.021/ 32|   1.020/ 34|   1.019/ 37 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  83   |   12221|     1375.90|   1.009/ 81|   1.005/ **|   1.004/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  68   |     375|      179.00|   1.023/ 30|   1.017/ 41|   1.015/ 45|   1.014/ 50 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  79   |   30366|     1560.97|   1.004/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  68   |     942|       89.79|   1.025/ 28|   1.024/ 29|   1.024/ 29|   1.024/ 29 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  66   |      63|       82.87|   1.024/ 29|   1.020/ 35|   1.019/ 37|   1.018/ 39 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  73   |    2277|      194.81|   1.020/ 34|   1.016/ 42|   1.015/ 45|   1.014/ 48 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  74   |     337|       85.16|   1.010/ 69|   1.009/ 76|   1.009/ 77|   1.009/ 79 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  78   |     158|       37.53|   1.007/ 98|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  74   |    5851|      457.04|   1.015/ 46|   1.010/ 68|   1.009/ 78|   1.008/ 90 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  72   |     137|       42.96|   1.008/ 91|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  65   |     726|      685.09|   1.026/ 26|   1.026/ 27|   1.025/ 27|   1.025/ 27 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  77   |     501|       97.36|   1.018/ 39|   1.016/ 44|   1.015/ 45|   1.015/ 46 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  82   |      66|       74.24|   1.027/ 26|   1.024/ 28|   1.024/ 29|   1.023/ 30 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  72   |     378|       55.27|   1.016/ 43|   1.014/ 49|   1.014/ 51|   1.013/ 53 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  76   |    1756|       60.55|   1.017/ 40|   1.013/ 52|   1.012/ 56|   1.011/ 61 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  71   |     116|       36.23|   1.023/ 29|   1.020/ 34|   1.020/ 35|   1.019/ 36 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  73   |      55|       88.07|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  79   |    1429|      167.41|   1.023/ 30|   1.020/ 35|   1.019/ 36|   1.018/ 38 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  93   |    1152|      151.22|   1.008/ 87|   1.006/ **|   1.006/ **|   1.006/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  63   |      79|       43.84|   1.011/ 64|   1.005/ **|   1.004/ **|   1.002/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  73   |     586|      100.61|   1.020/ 35|   1.020/ 35|   1.020/ 35|   1.020/ 35 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  49   |      17|       28.82|   1.036/ 19|   1.042/ 16|   1.043/ 16|   1.045/ 15 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  71   |     273|        8.47|   1.033/ 21|   1.027/ 25|   1.026/ 27|   1.024/ 28 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  82   |      33|       11.47|   1.004/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  81   |     654|       15.21|   1.013/ 54|   1.013/ 54|   1.013/ 54|   1.013/ 54 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  64   |       2|        0.06|   1.045/ 15|   1.010/ 70|   1.001/ **|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  85   |     554|       12.33|   1.026/ 26|   1.025/ 28|   1.025/ 28|   1.024/ 28 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  67   |     122|       41.11|   1.062/ 11|   1.071/ 10|   1.074/  9|   1.076/  9 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  92   |     105|        4.09|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  81   |     663|       74.49|   1.004/ **|   1.004/ **|   1.004/ **|   1.005/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  80   |      62|        6.13|   1.035/ 19|   1.037/ 19|   1.037/ 18|   1.038/ 18 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  77   |      17|       10.93|   1.033/ 21|   1.038/ 18|   1.039/ 18|   1.040/ 17 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  75   |     657|        3.90|   1.050/ 14|   1.050/ 14|   1.050/ 14|   1.049/ 14 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  62   |     240|       25.46|   1.026/ 27|   1.023/ 30|   1.022/ 31|   1.021/ 33 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  82   |    9683|      840.25|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  56   |       3|        0.28|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  64   |     341|       29.73|   1.044/ 15|   1.038/ 18|   1.037/ 19|   1.035/ 20 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  72   |     166|       50.39|   1.013/ 55|   1.005/ **|   1.003/ **|   1.002/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  62   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  76   |   31760|      150.23|   1.044/ 15|   1.039/ 18|   1.038/ 18|   1.036/ 19 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  82   |     148|       21.25|   1.018/ 38|   1.015/ 45|   1.015/ 47|   1.014/ 50 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  75   |      54|        2.58|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  49   |       1|        0.09|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  68   |     194|        7.32|   1.022/ 31|   1.021/ 33|   1.021/ 33|   1.021/ 34 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  84   |    7711|      202.91|   1.015/ 45|   1.010/ 66|   1.009/ 74|   1.008/ 84 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  34   |      66|        4.09|   1.017/ 40|   1.011/ 65|   1.009/ 76|   1.008/ 92 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  71   |    1044|       54.66|   1.062/ 11|   1.066/ 10|   1.067/ 10|   1.068/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  82   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  71   |     918|       18.59|   1.033/ 21|   1.032/ 21|   1.032/ 21|   1.032/ 22 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  74   |      11|        2.22|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  74   |     105|       25.81|   1.006/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  75   |      85|        7.54|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  79   |     582|      100.03|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  76   |     507|       48.91|   1.011/ 63|   1.009/ 76|   1.009/ 79|   1.008/ 83 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  79   |    3834|      219.48|   1.018/ 39|   1.010/ 69|   1.008/ 87|   1.006/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  85   |     927|        9.24|   1.029/ 24|   1.029/ 23|   1.029/ 23|   1.030/ 23 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  62   |      47|        7.24|   1.042/ 16|   1.037/ 19|   1.036/ 19|   1.035/ 20 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  40   |      13|        9.88|   1.040/ 17|   1.013/ 52|   1.005/ **|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  57   |       7|        0.07|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  72   |     327|       59.12|   1.005/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 107   |   30023|      447.60|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  73   |      17|        7.68|   1.025/ 27|   1.021/ 33|   1.020/ 34|   1.019/ 36 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  70   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  58   |      12|        3.30|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  84   |    8751|      105.25|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  72   |      38|        1.25|   1.019/ 36|   1.013/ 53|   1.012/ 59|   1.010/ 69 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  82   |     179|       16.73|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  77   |      92|        5.56|   1.081/  8|   1.092/  7|   1.094/  7|   1.097/  7 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  47   |      23|        1.91|   1.027/ 25|   1.022/ 31|   1.021/ 33|   1.020/ 35 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  36   |       8|        5.26|   1.052/ 13|   1.031/ 22|   1.027/ 26|   1.023/ 30 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  57   |      40|        3.45|   1.055/ 12|   1.061/ 11|   1.063/ 11|   1.065/ 11 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  67   |     215|       23.45|   1.028/ 25|   1.025/ 28|   1.024/ 29|   1.023/ 30 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  78   |     539|       55.20|   1.011/ 65|   1.008/ 85|   1.008/ 92|   1.007/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  82   |    5589|        4.11|   1.042/ 16|   1.039/ 18|   1.038/ 18|   1.037/ 19 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  82   |    1605|        6.01|   1.024/ 28|   1.025/ 28|   1.025/ 28|   1.025/ 28 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 102   |    7885|       94.57|   1.007/ 97|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  89   |     187|        4.78|   1.034/ 20|   1.038/ 18|   1.039/ 18|   1.040/ 17 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  82   |    1697|      344.85|   1.005/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  72   |     292|       31.79|   1.004/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 101   |   34346|      570.17|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  74   |       9|        3.32|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 109   |    1022|        8.11|   1.013/ 53|   1.008/ 91|   1.006/ **|   1.005/ ** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  66   |       9|        0.84|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  68   |      38|        2.06|   1.010/ 70|   1.009/ 73|   1.009/ 74|   1.009/ 74 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  67   |      65|        1.37|   1.028/ 25|   1.022/ 32|   1.020/ 34|   1.019/ 36 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  67   |      30|       16.87|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  58   |     224|       50.66|   1.052/ 13|   1.040/ 17|   1.038/ 18|   1.035/ 20 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  59   |      16|        2.52|   1.013/ 52|   1.012/ 60|   1.011/ 62|   1.011/ 65 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  59   |      24|       12.83|   1.015/ 47|   1.015/ 46|   1.015/ 47|   1.015/ 47 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  83   |      26|        3.87|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  58   |      28|        6.31|   1.016/ 44|   1.015/ 47|   1.014/ 48|   1.014/ 50 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  60   |       4|        0.62|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  72   |      71|       25.30|   1.016/ 43|   1.016/ 43|   1.016/ 43|   1.016/ 43 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  15   |       7|        0.26|   1.000/ --|   1.299/  2|   1.399/  2|   1.482/  1 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  76   |     117|        3.58|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  64   |      81|        4.00|   1.031/ 22|   1.026/ 26|   1.025/ 28|   1.024/ 29 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  63   |      24|        5.80|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  74   |   10664|       84.25|   1.049/ 14|   1.045/ 15|   1.043/ 16|   1.042/ 16 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  75   |     308|      115.01|   1.026/ 27|   1.023/ 31|   1.022/ 32|   1.021/ 33 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  83   |     206|        5.75|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  16   |       8|        0.25|   1.111/  6|   1.136/  5|   1.152/  4|   1.167/  4 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  87   |    6112|      350.14|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  64   |      22|        4.37|   1.004/ **|   1.005/ **|   1.006/ **|   1.006/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  66   |      40|        6.14|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  68   |      68|        3.07|   1.013/ 53|   1.008/ 89|   1.006/ **|   1.005/ ** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  70   |     295|        1.43|   1.031/ 22|   1.024/ 28|   1.023/ 30|   1.021/ 33 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  71   |     129|       62.11|   1.020/ 35|   1.022/ 32|   1.022/ 31|   1.023/ 30 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  79   |     241|       44.81|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  62   |      49|       10.40|   1.048/ 14|   1.043/ 16|   1.041/ 17|   1.040/ 17 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  74   |    1470|        6.70|   1.036/ 19|   1.033/ 21|   1.032/ 21|   1.032/ 22 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  82   |     345|       81.66|   1.014/ 48|   1.012/ 58|   1.011/ 61|   1.011/ 64 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  72   |      11|        1.57|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  73   |    4698|      146.20|   1.039/ 18|   1.034/ 20|   1.033/ 21|   1.032/ 22 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 120   |    1039|        9.58|   1.012/ 60|   1.009/ 79|   1.008/ 85|   1.007/ 93 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  81   |    1112|       28.97|   1.011/ 63|   1.008/ 90|   1.007/ **|   1.006/ ** |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  76   |    1415|      137.72|   1.010/ 68|   1.010/ 71|   1.010/ 72|   1.009/ 73 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  65   |      35|       12.81|   1.070/ 10|   1.086/  8|   1.090/  8|   1.094/  7 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  71   |    1309|       67.44|   1.010/ 66|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  74   |    4798|       32.70|   1.043/ 16|   1.040/ 17|   1.040/ 17|   1.039/ 17 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  69   |     492|       14.38|   1.034/ 20|   1.034/ 20|   1.034/ 20|   1.034/ 20 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  61   |      45|        2.79|   1.037/ 19|   1.027/ 26|   1.024/ 28|   1.022/ 32 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  73   |     249|       35.71|   1.004/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  39   |      48|        6.13|   1.032/ 21|   1.019/ 36|   1.015/ 45|   1.012/ 59 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  72   |      24|        4.19|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  65   |      28|        5.22|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  79   |     110|       52.40|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  54   |      75|        4.70|   1.023/ 30|   1.025/ 27|   1.026/ 27|   1.027/ 26 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  66   |     683|       11.63|   1.065/ 10|   1.068/ 10|   1.068/ 10|   1.069/ 10 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  90   |   28306|      600.96|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  65   |      10|        0.46|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  80   |     255|        6.01|   1.070/ 10|   1.070/ 10|   1.071/ 10|   1.071/ 10 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  82   |    4538|      438.93|   1.014/ 50|   1.012/ 60|   1.011/ 63|   1.011/ 66 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  88   |    1953|      227.00|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  64   |       4|        0.25|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  62   |      21|        0.38|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  92   |      57|        0.86|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  66   |      13|        1.79|   1.009/ 79|   1.007/ 99|   1.007/ **|   1.006/ ** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  68   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  74   |      49|        4.17|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  76   |    4637|       55.76|   1.007/ 98|   1.005/ **|   1.005/ **|   1.004/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  93   |  109783|      333.14|   1.011/ 65|   1.008/ 90|   1.007/ 99|   1.006/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  80   |     761|       18.17|   1.025/ 28|   1.020/ 35|   1.019/ 37|   1.017/ 40 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  73   |     280|       28.29|   1.012/ 58|   1.004/ **|   1.002/ **|   1.001/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  82   |   39770|      598.63|   1.008/ 90|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  64   |      23|        6.44|   1.007/ 95|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  66   |      15|        0.44|   1.015/ 47|   1.013/ 52|   1.013/ 53|   1.013/ 55 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  66   |      11|        0.33|   1.012/ 57|   1.018/ 39|   1.019/ 36|   1.021/ 33 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  60   |       7|        0.40|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  70   |       4|        0.26|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |

