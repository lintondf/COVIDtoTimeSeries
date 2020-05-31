# State and Country COVID-19 Analysis #
## Updated: 2020-05-31 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  78   |   30320|     1558.58|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  82   |   12184|     1371.77|   1.009/ 78|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  72   |    7063|     1016.30|   1.013/ 53|   1.009/ 78|   1.008/ 89|   1.007/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  73   |    5785|      451.89|   1.016/ 43|   1.010/ 67|   1.009/ 76|   1.008/ 89 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  73   |    5543|      555.03|   1.008/ 86|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  75   |    5607|      442.45|   1.020/ 35|   1.015/ 45|   1.014/ 48|   1.013/ 52 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  88   |    4334|      109.68|   1.019/ 37|   1.016/ 44|   1.015/ 46|   1.014/ 48 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  73   |    4046|     1134.93|   1.012/ 60|   1.008/ 86|   1.007/ 96|   1.006/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  78   |    2869|      617.24|   1.008/ 85|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  73   |    2608|      431.35|   1.018/ 37|   1.014/ 49|   1.013/ 53|   1.012/ 58 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  92   |  109141|      331.19|   1.011/ 62|   1.008/ 85|   1.007/ 94|   1.007/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  81   |   39545|      595.24|   1.008/ 86|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 100   |   34312|      569.60|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  75   |   30599|      144.73|   1.046/ 15|   1.041/ 17|   1.040/ 17|   1.039/ 18 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 106   |   30054|      448.06|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  89   |   28392|      602.81|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  73   |   10231|       80.82|   1.051/ 13|   1.047/ 15|   1.046/ 15|   1.045/ 15 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  81   |    9661|      838.34|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  83   |    8721|      104.89|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 101   |    7829|       93.90|   1.007/ 97|   1.006/ **|   1.006/ **|   1.006/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  67   |     636|      129.74|   1.019/ 37|   1.014/ 50|   1.013/ 54|   1.012/ 59 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  67   |      10|       13.73|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  71   |     951|      130.63|   1.023/ 30|   1.017/ 41|   1.015/ 46|   1.014/ 51 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  68   |     130|       43.02|   1.021/ 34|   1.022/ 32|   1.022/ 31|   1.023/ 31 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  88   |    4334|      109.68|   1.019/ 37|   1.016/ 44|   1.015/ 46|   1.014/ 48 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  78   |    1511|      262.37|   1.017/ 41|   1.014/ 49|   1.014/ 51|   1.013/ 54 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  73   |    4046|     1134.93|   1.012/ 60|   1.008/ 86|   1.007/ 96|   1.006/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  66   |     378|      388.08|   1.019/ 36|   1.014/ 51|   1.012/ 57|   1.011/ 64 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  84   |    2544|      118.46|   1.016/ 43|   1.013/ 53|   1.012/ 56|   1.012/ 60 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  80   |    2058|      193.79|   1.016/ 42|   1.015/ 48|   1.014/ 49|   1.014/ 50 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  61   |      17|       12.01|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  66   |      83|       46.65|   1.009/ 75|   1.009/ 81|   1.008/ 83|   1.008/ 85 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  75   |    5607|      442.45|   1.020/ 35|   1.015/ 45|   1.014/ 48|   1.013/ 52 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  76   |    2231|      331.40|   1.015/ 47|   1.010/ 68|   1.009/ 76|   1.008/ 87 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  67   |     556|      176.24|   1.033/ 21|   1.029/ 24|   1.028/ 25|   1.027/ 26 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  79   |     225|       77.20|   1.008/ 85|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  76   |     434|       97.11|   1.016/ 45|   1.014/ 50|   1.013/ 52|   1.013/ 54 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  78   |    2869|      617.24|   1.008/ 85|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  65   |      85|       63.48|   1.017/ 41|   1.019/ 37|   1.019/ 36|   1.020/ 35 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  73   |    2608|      431.35|   1.018/ 37|   1.014/ 49|   1.013/ 53|   1.012/ 58 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  72   |    7063|     1016.30|   1.013/ 53|   1.009/ 78|   1.008/ 89|   1.007/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  73   |    5543|      555.03|   1.008/ 86|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  71   |    1056|      187.28|   1.028/ 25|   1.024/ 29|   1.023/ 30|   1.022/ 31 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  73   |     743|      249.70|   1.025/ 27|   1.023/ 30|   1.022/ 31|   1.021/ 32 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  73   |     780|      127.13|   1.017/ 40|   1.013/ 54|   1.012/ 59|   1.011/ 65 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  65   |      17|       15.65|   1.004/ **|   1.005/ **|   1.005/ **|   1.006/ ** |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  64   |     174|       89.70|   1.028/ 24|   1.025/ 27|   1.025/ 28|   1.024/ 29 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  76   |     429|      139.19|   1.013/ 55|   1.010/ 72|   1.009/ 78|   1.008/ 85 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  69   |     254|      186.75|   1.029/ 24|   1.023/ 31|   1.021/ 33|   1.020/ 35 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  82   |   12184|     1371.77|   1.009/ 78|   1.005/ **|   1.004/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  67   |     369|      175.91|   1.024/ 29|   1.017/ 40|   1.016/ 44|   1.014/ 49 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  78   |   30320|     1558.58|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  67   |     920|       87.76|   1.025/ 28|   1.024/ 29|   1.024/ 29|   1.024/ 29 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  65   |      62|       81.24|   1.024/ 28|   1.020/ 35|   1.018/ 38|   1.017/ 40 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  72   |    2249|      192.42|   1.022/ 32|   1.018/ 38|   1.017/ 40|   1.016/ 42 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  73   |     334|       84.37|   1.010/ 68|   1.009/ 77|   1.009/ 79|   1.009/ 81 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  77   |     158|       37.35|   1.008/ 91|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  73   |    5785|      451.89|   1.016/ 43|   1.010/ 67|   1.009/ 76|   1.008/ 89 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  71   |     136|       42.62|   1.007/ 93|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  64   |     709|      669.38|   1.027/ 26|   1.027/ 26|   1.027/ 26|   1.027/ 26 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  76   |     495|       96.09|   1.018/ 39|   1.016/ 43|   1.015/ 45|   1.015/ 46 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  81   |      64|       72.54|   1.024/ 28|   1.020/ 34|   1.019/ 36|   1.018/ 38 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  71   |     373|       54.56|   1.017/ 40|   1.015/ 45|   1.015/ 46|   1.015/ 47 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  75   |    1731|       59.71|   1.018/ 38|   1.014/ 49|   1.013/ 53|   1.012/ 57 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  70   |     114|       35.56|   1.024/ 29|   1.021/ 33|   1.020/ 34|   1.019/ 36 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  72   |      55|       87.95|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  78   |    1406|      164.74|   1.024/ 28|   1.022/ 32|   1.021/ 33|   1.020/ 34 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  92   |    1146|      150.45|   1.008/ 82|   1.007/ 98|   1.007/ **|   1.006/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  62   |      78|       43.77|   1.012/ 57|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  72   |     575|       98.70|   1.019/ 36|   1.019/ 37|   1.019/ 37|   1.019/ 37 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  48   |      16|       27.94|   1.037/ 19|   1.046/ 15|   1.048/ 14|   1.051/ 14 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  70   |     267|        8.29|   1.033/ 21|   1.028/ 25|   1.026/ 26|   1.025/ 28 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  81   |      33|       11.42|   1.004/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  80   |     646|       15.02|   1.013/ 54|   1.013/ 54|   1.013/ 53|   1.013/ 53 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  63   |       2|        0.06|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  84   |     541|       12.05|   1.027/ 25|   1.026/ 27|   1.026/ 27|   1.025/ 27 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  66   |     112|       37.71|   1.062/ 11|   1.073/  9|   1.076/  9|   1.078/  9 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  91   |     105|        4.09|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  80   |     660|       74.18|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  79   |      59|        5.91|   1.035/ 20|   1.036/ 19|   1.036/ 19|   1.037/ 19 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  76   |      16|       10.39|   1.029/ 24|   1.032/ 22|   1.033/ 21|   1.033/ 21 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  74   |     625|        3.71|   1.049/ 14|   1.049/ 14|   1.049/ 14|   1.049/ 14 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  61   |     234|       24.88|   1.026/ 26|   1.023/ 30|   1.022/ 31|   1.021/ 32 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  81   |    9661|      838.34|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  55   |       2|        0.17|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  63   |     329|       28.68|   1.047/ 15|   1.042/ 16|   1.041/ 17|   1.039/ 18 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  71   |     165|       50.08|   1.015/ 47|   1.007/ 93|   1.006/ **|   1.004/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  61   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  75   |   30599|      144.73|   1.046/ 15|   1.041/ 17|   1.040/ 17|   1.039/ 18 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  81   |     145|       20.93|   1.019/ 36|   1.016/ 43|   1.015/ 45|   1.014/ 48 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  74   |      54|        2.58|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  48   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  67   |     191|        7.18|   1.022/ 32|   1.020/ 34|   1.020/ 35|   1.019/ 36 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  83   |    7599|      199.97|   1.015/ 45|   1.010/ 69|   1.009/ 79|   1.007/ 92 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  33   |      66|        4.07|   1.019/ 36|   1.014/ 50|   1.013/ 54|   1.012/ 59 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  70   |     979|       51.21|   1.062/ 11|   1.067/ 10|   1.068/ 10|   1.069/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  81   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  70   |     890|       18.02|   1.033/ 21|   1.032/ 21|   1.032/ 21|   1.032/ 22 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  73   |      11|        2.23|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  73   |     105|       25.70|   1.006/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  74   |      85|        7.54|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  78   |     582|       99.97|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  75   |     501|       48.38|   1.011/ 63|   1.009/ 78|   1.008/ 82|   1.008/ 87 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  78   |    3839|      219.76|   1.020/ 35|   1.012/ 57|   1.010/ 68|   1.008/ 85 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  84   |     898|        8.96|   1.028/ 25|   1.028/ 25|   1.028/ 25|   1.028/ 25 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  61   |      45|        6.98|   1.041/ 17|   1.034/ 20|   1.033/ 21|   1.031/ 22 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  39   |      13|        9.89|   1.046/ 15|   1.023/ 30|   1.016/ 44|   1.008/ 88 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  56   |       6|        0.07|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  71   |     326|       58.89|   1.006/ **|   1.002/ **|   1.001/ **|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 106   |   30054|      448.06|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  72   |      16|        7.45|   1.025/ 28|   1.020/ 35|   1.019/ 37|   1.017/ 39 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  69   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  57   |      12|        3.30|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  83   |    8721|      104.89|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  71   |      37|        1.24|   1.020/ 35|   1.014/ 50|   1.012/ 56|   1.011/ 64 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  81   |     179|       16.66|   1.007/ **|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  76   |      84|        5.05|   1.078/  9|   1.088/  8|   1.090/  8|   1.093/  7 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  46   |      23|        1.88|   1.029/ 24|   1.024/ 28|   1.023/ 30|   1.022/ 31 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  35   |       8|        5.15|   1.061/ 11|   1.039/ 18|   1.035/ 20|   1.031/ 22 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  56   |      37|        3.22|   1.051/ 13|   1.054/ 13|   1.055/ 12|   1.056/ 12 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  66   |     209|       22.85|   1.028/ 24|   1.025/ 28|   1.024/ 28|   1.023/ 29 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  77   |     534|       54.68|   1.011/ 64|   1.008/ 87|   1.007/ 95|   1.007/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  81   |    5369|        3.94|   1.042/ 16|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  81   |    1566|        5.87|   1.024/ 29|   1.025/ 28|   1.025/ 28|   1.025/ 28 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 101   |    7829|       93.90|   1.007/ 97|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  88   |     180|        4.59|   1.032/ 22|   1.036/ 19|   1.037/ 19|   1.038/ 18 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  81   |    1692|      343.85|   1.005/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  71   |     292|       31.73|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 100   |   34312|      569.60|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  73   |       9|        3.32|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 108   |    1019|        8.09|   1.014/ 49|   1.009/ 80|   1.007/ 94|   1.006/ ** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  65   |       9|        0.84|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  67   |      38|        2.03|   1.008/ 84|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  66   |      64|        1.34|   1.028/ 25|   1.020/ 34|   1.019/ 37|   1.017/ 40 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  66   |      30|       16.89|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  57   |     215|       48.58|   1.054/ 13|   1.041/ 17|   1.038/ 18|   1.035/ 20 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  58   |      16|        2.50|   1.015/ 47|   1.014/ 50|   1.014/ 50|   1.014/ 51 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  58   |      24|       12.68|   1.016/ 42|   1.018/ 39|   1.018/ 39|   1.018/ 38 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  82   |      26|        3.86|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  57   |      28|        6.26|   1.018/ 39|   1.018/ 37|   1.018/ 37|   1.018/ 38 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  59   |       3|        0.44|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  71   |      70|       24.94|   1.017/ 41|   1.017/ 40|   1.017/ 40|   1.017/ 40 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  14   |       2|        0.08|   1.000/ --|   1.000/ --|   1.297/  2|   1.466/  1 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  75   |     117|        3.58|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  63   |      79|        3.90|   1.032/ 21|   1.028/ 25|   1.027/ 26|   1.025/ 27 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  62   |      20|        4.99|   1.186/  4|   1.179/  4|   1.179/  4|   1.179/  4 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  73   |   10231|       80.82|   1.051/ 13|   1.047/ 15|   1.046/ 15|   1.045/ 15 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  74   |     303|      112.81|   1.027/ 25|   1.024/ 28|   1.024/ 29|   1.023/ 30 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  82   |     206|        5.73|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  15   |       6|        0.21|   1.123/  5|   1.120/  6|   1.134/  5|   1.149/  5 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  86   |    6110|      349.99|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  63   |      22|        4.34|   1.004/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  65   |      37|        5.76|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  67   |      68|        3.05|   1.015/ 46|   1.010/ 69|   1.009/ 79|   1.008/ 92 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  69   |     286|        1.39|   1.031/ 22|   1.023/ 30|   1.021/ 33|   1.019/ 36 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  70   |     126|       60.71|   1.018/ 38|   1.020/ 35|   1.020/ 34|   1.021/ 34 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  78   |     241|       44.84|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  61   |      46|        9.86|   1.046/ 15|   1.040/ 17|   1.038/ 18|   1.036/ 19 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  73   |    1413|        6.44|   1.034/ 20|   1.030/ 23|   1.029/ 23|   1.028/ 24 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  81   |     340|       80.57|   1.014/ 48|   1.012/ 59|   1.011/ 62|   1.010/ 66 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  71   |      11|        1.57|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  72   |    4550|      141.60|   1.040/ 17|   1.035/ 20|   1.034/ 20|   1.033/ 21 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 119   |    1028|        9.48|   1.011/ 60|   1.009/ 81|   1.008/ 89|   1.007/ 98 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  80   |    1106|       28.81|   1.011/ 60|   1.008/ 85|   1.007/ 94|   1.007/ ** |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  75   |    1401|      136.36|   1.010/ 68|   1.010/ 72|   1.009/ 73|   1.009/ 74 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  64   |      32|       11.73|   1.071/ 10|   1.089/  8|   1.093/  7|   1.098/  7 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  70   |    1303|       67.13|   1.011/ 63|   1.007/ 96|   1.006/ **|   1.005/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  73   |    4610|       31.41|   1.043/ 16|   1.040/ 17|   1.039/ 17|   1.039/ 18 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  68   |     475|       13.88|   1.033/ 21|   1.032/ 21|   1.032/ 21|   1.032/ 22 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  60   |      44|        2.74|   1.039/ 18|   1.029/ 24|   1.026/ 27|   1.023/ 29 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  72   |     249|       35.72|   1.004/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  38   |      48|        6.08|   1.036/ 19|   1.024/ 29|   1.020/ 34|   1.017/ 40 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  71   |      24|        4.19|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  64   |      29|        5.23|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  78   |     110|       52.41|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  53   |      72|        4.55|   1.022/ 31|   1.024/ 29|   1.024/ 28|   1.025/ 28 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  65   |     642|       10.92|   1.066/ 10|   1.069/ 10|   1.070/ 10|   1.070/ 10 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  89   |   28392|      602.81|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  64   |      10|        0.45|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  79   |     235|        5.53|   1.065/ 11|   1.062/ 11|   1.062/ 11|   1.061/ 11 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  81   |    4486|      433.95|   1.014/ 48|   1.012/ 57|   1.012/ 60|   1.011/ 63 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  87   |    1952|      226.87|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  63   |       4|        0.24|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  61   |      21|        0.38|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  91   |      57|        0.86|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  65   |      13|        1.78|   1.010/ 68|   1.009/ 79|   1.008/ 82|   1.008/ 86 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  67   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  73   |      49|        4.16|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  75   |    4610|       55.44|   1.007/ 95|   1.005/ **|   1.005/ **|   1.004/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  92   |  109141|      331.19|   1.011/ 62|   1.008/ 85|   1.007/ 94|   1.007/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  79   |     746|       17.81|   1.026/ 27|   1.021/ 33|   1.020/ 35|   1.018/ 37 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  72   |     280|       28.27|   1.013/ 53|   1.005/ **|   1.003/ **|   1.001/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  81   |   39545|      595.24|   1.008/ 86|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  63   |      23|        6.42|   1.008/ 83|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  65   |      15|        0.43|   1.014/ 50|   1.012/ 57|   1.012/ 59|   1.011/ 62 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  65   |      11|        0.33|   1.011/ 66|   1.016/ 44|   1.017/ 41|   1.018/ 38 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  59   |       7|        0.40|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  69   |       4|        0.26|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |

