# State and Country COVID-19 Analysis #
## Updated: 2020-06-07 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  85   |   30731|     1579.73|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  89   |   12522|     1409.79|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  79   |    7502|     1079.48|   1.010/ 66|   1.008/ 87|   1.007/ 95|   1.007/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  80   |    6152|      480.52|   1.012/ 58|   1.009/ 79|   1.008/ 86|   1.007/ 95 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  82   |    6107|      481.97|   1.015/ 45|   1.012/ 58|   1.011/ 62|   1.010/ 66 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  80   |    5746|      575.39|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  95   |    4768|      120.67|   1.016/ 43|   1.014/ 50|   1.013/ 52|   1.013/ 55 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  80   |    4210|     1180.76|   1.007/ 94|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  85   |    2973|      639.44|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  80   |    2834|      468.84|   1.014/ 48|   1.011/ 61|   1.011/ 65|   1.010/ 70 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  99   |  114465|      347.34|   1.009/ 80|   1.006/ **|   1.006/ **|   1.005/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  88   |   41107|      618.74|   1.007/ 96|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  82   |   38537|      182.29|   1.038/ 18|   1.033/ 21|   1.032/ 22|   1.031/ 23 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 107   |   34644|      575.11|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 113   |   30088|      448.57|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  96   |   27734|      588.82|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  80   |   13782|      108.88|   1.049/ 14|   1.047/ 15|   1.047/ 15|   1.046/ 15 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  88   |    9746|      845.70|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  90   |    8855|      106.50|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 108   |    8234|       98.75|   1.007/ 93|   1.007/ 96|   1.007/ 97|   1.007/ 98 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  74   |     700|      142.83|   1.015/ 45|   1.013/ 55|   1.012/ 57|   1.011/ 60 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  74   |      10|       13.68|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  78   |    1062|      145.88|   1.020/ 34|   1.017/ 40|   1.016/ 42|   1.016/ 44 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  75   |     151|       50.11|   1.024/ 29|   1.026/ 27|   1.026/ 26|   1.027/ 26 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  95   |    4768|      120.67|   1.016/ 43|   1.014/ 50|   1.013/ 52|   1.013/ 55 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  85   |    1606|      278.81|   1.011/ 61|   1.008/ 84|   1.008/ 92|   1.007/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  80   |    4210|     1180.76|   1.007/ 94|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  73   |     406|      416.50|   1.014/ 49|   1.010/ 69|   1.009/ 76|   1.008/ 85 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  91   |    2755|      128.29|   1.014/ 49|   1.012/ 57|   1.012/ 60|   1.011/ 62 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  87   |    2255|      212.37|   1.014/ 50|   1.012/ 57|   1.012/ 59|   1.011/ 61 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  68   |      17|       12.01|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  73   |      85|       47.84|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  82   |    6107|      481.97|   1.015/ 45|   1.012/ 58|   1.011/ 62|   1.010/ 66 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  83   |    2359|      350.48|   1.011/ 61|   1.008/ 82|   1.008/ 90|   1.007/ 99 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  74   |     642|      203.48|   1.024/ 29|   1.019/ 37|   1.017/ 40|   1.016/ 43 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  86   |     234|       80.41|   1.008/ 84|   1.007/ **|   1.007/ **|   1.006/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  83   |     476|      106.58|   1.015/ 47|   1.014/ 51|   1.013/ 51|   1.013/ 52 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  85   |    2973|      639.44|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  72   |      98|       72.87|   1.018/ 38|   1.019/ 36|   1.019/ 35|   1.020/ 35 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  80   |    2834|      468.84|   1.014/ 48|   1.011/ 61|   1.011/ 65|   1.010/ 70 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  79   |    7502|     1079.48|   1.010/ 66|   1.008/ 87|   1.007/ 95|   1.007/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  80   |    5746|      575.39|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  78   |    1218|      215.89|   1.023/ 30|   1.020/ 35|   1.019/ 36|   1.019/ 37 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  80   |     848|      284.84|   1.021/ 33|   1.019/ 37|   1.018/ 38|   1.017/ 40 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  80   |     847|      138.07|   1.013/ 53|   1.010/ 71|   1.009/ 78|   1.008/ 86 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  72   |      17|       16.35|   1.006/ **|   1.008/ 92|   1.008/ 88|   1.008/ 83 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  71   |     194|      100.25|   1.022/ 32|   1.019/ 37|   1.018/ 39|   1.017/ 40 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  83   |     451|      146.27|   1.009/ 73|   1.007/ 97|   1.007/ **|   1.006/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  76   |     292|      214.42|   1.025/ 28|   1.022/ 32|   1.021/ 33|   1.020/ 34 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  89   |   12522|     1409.79|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  74   |     409|      194.87|   1.018/ 38|   1.014/ 49|   1.013/ 53|   1.012/ 57 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  85   |   30731|     1579.73|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  74   |    1058|      100.84|   1.020/ 34|   1.018/ 38|   1.018/ 39|   1.018/ 39 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  72   |      72|       93.91|   1.024/ 29|   1.023/ 30|   1.022/ 31|   1.022/ 31 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  79   |    2478|      212.02|   1.017/ 41|   1.014/ 50|   1.013/ 53|   1.012/ 56 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  80   |     353|       89.10|   1.008/ 83|   1.007/ 93|   1.007/ 96|   1.007/ 99 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  84   |     164|       38.77|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  80   |    6152|      480.52|   1.012/ 58|   1.009/ 79|   1.008/ 86|   1.007/ 95 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  78   |     143|       44.73|   1.007/ 92|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  71   |     808|      762.58|   1.020/ 34|   1.018/ 39|   1.017/ 41|   1.016/ 43 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  83   |     543|      105.44|   1.015/ 45|   1.014/ 50|   1.013/ 52|   1.013/ 53 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  88   |      70|       79.62|   1.017/ 41|   1.013/ 53|   1.012/ 57|   1.011/ 62 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  78   |     414|       60.54|   1.018/ 39|   1.017/ 40|   1.017/ 40|   1.017/ 40 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  82   |    1886|       65.05|   1.015/ 46|   1.012/ 56|   1.012/ 59|   1.011/ 62 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  77   |     127|       39.50|   1.017/ 40|   1.014/ 49|   1.013/ 52|   1.012/ 56 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  79   |      55|       88.64|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  85   |    1556|      182.35|   1.016/ 43|   1.013/ 54|   1.012/ 58|   1.011/ 63 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  99   |    1186|      155.78|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  69   |      83|       46.12|   1.012/ 58|   1.010/ 66|   1.010/ 68|   1.010/ 69 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  79   |     649|      111.55|   1.017/ 40|   1.017/ 41|   1.017/ 41|   1.017/ 42 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  55   |      19|       32.37|   1.025/ 28|   1.017/ 42|   1.014/ 49|   1.012/ 59 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  77   |     324|       10.07|   1.034/ 21|   1.031/ 22|   1.031/ 22|   1.030/ 23 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  88   |      33|       11.74|   1.003/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  87   |     702|       16.32|   1.012/ 58|   1.012/ 59|   1.012/ 59|   1.012/ 59 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  70   |       4|        0.14|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  91   |     646|       14.38|   1.028/ 25|   1.027/ 25|   1.027/ 26|   1.027/ 26 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  73   |     188|       63.71|   1.067/ 10|   1.073/  9|   1.075/  9|   1.076/  9 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  98   |     104|        4.06|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  87   |     677|       75.99|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  86   |      80|        7.99|   1.043/ 16|   1.045/ 15|   1.046/ 15|   1.047/ 15 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  83   |      22|       14.17|   1.041/ 17|   1.046/ 15|   1.047/ 15|   1.048/ 14 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  81   |     866|        5.14|   1.048/ 14|   1.047/ 15|   1.047/ 15|   1.046/ 15 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  68   |     270|       28.65|   1.022/ 31|   1.020/ 35|   1.019/ 36|   1.018/ 38 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  88   |    9746|      845.70|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  62   |       3|        0.28|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  70   |     451|       39.34|   1.049/ 14|   1.048/ 14|   1.047/ 14|   1.047/ 14 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  78   |     169|       51.06|   1.007/ 93|   1.003/ **|   1.001/ **|   1.000/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  68   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  82   |   38537|      182.29|   1.038/ 18|   1.033/ 21|   1.032/ 22|   1.031/ 23 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  88   |     161|       23.17|   1.018/ 39|   1.016/ 43|   1.016/ 44|   1.015/ 45 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  81   |      54|        2.58|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  55   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  74   |     215|        8.11|   1.019/ 36|   1.018/ 39|   1.017/ 40|   1.017/ 41 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  90   |    8206|      215.96|   1.013/ 54|   1.010/ 71|   1.009/ 77|   1.008/ 83 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  15   |       5|        0.85|   1.239/  3|   1.126/  5|   1.066/ 10|   1.011/ 63 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  40   |      69|        4.22|   1.009/ 73|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  77   |    1520|       79.55|   1.064/ 11|   1.066/ 10|   1.066/ 10|   1.066/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  88   |    4638|        3.31|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  77   |    1161|       23.51|   1.040/ 17|   1.042/ 16|   1.043/ 16|   1.043/ 16 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  80   |      11|        2.15|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  80   |     106|       26.01|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  81   |      85|        7.54|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  85   |     590|      101.40|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  82   |     536|       51.76|   1.010/ 67|   1.009/ 73|   1.009/ 75|   1.009/ 76 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  85   |    3902|      223.39|   1.011/ 61|   1.006/ **|   1.004/ **|   1.003/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  91   |    1152|       11.48|   1.035/ 20|   1.037/ 19|   1.037/ 18|   1.038/ 18 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  68   |      56|        8.69|   1.033/ 21|   1.029/ 24|   1.028/ 25|   1.027/ 26 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  46   |      13|        9.23|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  63   |      17|        0.17|   1.114/  6|   1.139/  5|   1.145/  5|   1.151/  4 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  78   |     330|       59.67|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 113   |   30088|      448.57|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  79   |      21|        9.75|   1.058/ 12|   1.064/ 11|   1.066/ 10|   1.067/ 10 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  76   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  64   |      13|        3.44|   1.004/ **|   1.004/ **|   1.004/ **|   1.005/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  90   |    8855|      106.50|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  78   |      42|        1.39|   1.021/ 33|   1.019/ 36|   1.019/ 37|   1.018/ 37 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  88   |     184|       17.18|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  83   |     167|       10.07|   1.094/  7|   1.104/  6|   1.107/  6|   1.109/  6 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  53   |      24|        1.99|   1.013/ 53|   1.005/ **|   1.003/ **|   1.001/ ** |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  42   |      10|        6.36|   1.041/ 17|   1.059/ 12|   1.064/ 11|   1.069/ 10 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  63   |      54|        4.69|   1.049/ 14|   1.048/ 14|   1.048/ 14|   1.047/ 14 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  73   |     254|       27.78|   1.030/ 23|   1.029/ 24|   1.029/ 24|   1.029/ 24 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  84   |     560|       57.34|   1.008/ 87|   1.006/ **|   1.006/ **|   1.005/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  88   |    7030|        5.16|   1.042/ 17|   1.040/ 17|   1.040/ 17|   1.039/ 17 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  88   |    1831|        6.86|   1.022/ 31|   1.022/ 32|   1.022/ 32|   1.021/ 32 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 108   |    8234|       98.75|   1.007/ 93|   1.007/ 96|   1.007/ 97|   1.007/ 98 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  95   |     230|        5.89|   1.051/ 13|   1.058/ 12|   1.060/ 11|   1.062/ 11 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  88   |    1713|      348.09|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  78   |     296|       32.20|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 107   |   34644|      575.11|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  80   |       9|        3.48|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 115   |    1048|        8.32|   1.007/ 95|   1.002/ **|   1.001/ **|   1.000/ ** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  72   |       9|        0.84|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  74   |      47|        2.50|   1.032/ 22|   1.040/ 17|   1.042/ 16|   1.044/ 16 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  73   |      79|        1.67|   1.033/ 21|   1.033/ 21|   1.034/ 20|   1.034/ 20 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  73   |      30|       16.89|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  64   |     270|       61.00|   1.039/ 18|   1.030/ 23|   1.028/ 24|   1.026/ 26 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  65   |      20|        3.04|   1.032/ 21|   1.040/ 17|   1.042/ 16|   1.045/ 15 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  65   |      26|       13.44|   1.011/ 64|   1.009/ 76|   1.009/ 80|   1.008/ 84 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  89   |      27|        4.00|   1.006/ **|   1.007/ 98|   1.007/ 93|   1.008/ 88 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  64   |      30|        6.73|   1.014/ 49|   1.012/ 56|   1.012/ 59|   1.011/ 61 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  66   |       5|        0.79|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  78   |      75|       26.76|   1.010/ 71|   1.007/ 94|   1.007/ **|   1.006/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  21   |       8|        0.29|   1.067/ 10|   1.050/ 14|   1.065/ 11|   1.081/  8 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  82   |     117|        3.57|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  70   |      92|        4.52|   1.027/ 26|   1.023/ 30|   1.023/ 31|   1.022/ 32 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  69   |      49|       12.03|   1.212/  3|   1.240/  3|   1.247/  3|   1.253/  3 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  80   |   13782|      108.88|   1.049/ 14|   1.047/ 15|   1.047/ 15|   1.046/ 15 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  81   |     344|      128.25|   1.021/ 34|   1.017/ 40|   1.017/ 42|   1.016/ 44 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  89   |     210|        5.86|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  13   |       2|        0.07|   1.145/  5|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  22   |      12|        0.41|   1.127/  5|   1.101/  7|   1.104/  7|   1.108/  6 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  93   |    6148|      352.18|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  70   |      22|        4.45|   1.002/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  72   |      58|        9.05|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  74   |      69|        3.11|   1.006/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  76   |     350|        1.70|   1.030/ 23|   1.028/ 25|   1.027/ 25|   1.027/ 26 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  77   |     150|       72.08|   1.022/ 31|   1.024/ 29|   1.024/ 29|   1.024/ 28 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  85   |     241|       44.81|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  68   |      71|       15.32|   1.064/ 11|   1.066/ 10|   1.067/ 10|   1.068/ 10 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  80   |    1874|        8.54|   1.041/ 17|   1.042/ 16|   1.042/ 16|   1.043/ 16 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  88   |     378|       89.49|   1.016/ 42|   1.016/ 44|   1.016/ 44|   1.016/ 44 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  78   |      11|        1.56|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  79   |    5596|      174.17|   1.033/ 21|   1.029/ 24|   1.028/ 25|   1.027/ 26 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 126   |    1083|        9.98|   1.008/ 83|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  87   |    1169|       30.45|   1.010/ 68|   1.008/ 82|   1.008/ 87|   1.008/ 92 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  82   |    1493|      145.26|   1.009/ 77|   1.008/ 82|   1.008/ 83|   1.008/ 85 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  71   |      53|       19.12|   1.063/ 11|   1.066/ 10|   1.067/ 10|   1.067/ 10 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  77   |    1354|       69.79|   1.008/ 87|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  80   |    5950|       40.55|   1.038/ 18|   1.035/ 19|   1.035/ 20|   1.034/ 20 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  75   |     634|       18.54|   1.042/ 16|   1.046/ 15|   1.047/ 15|   1.047/ 14 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  67   |      50|        3.07|   1.024/ 29|   1.016/ 42|   1.014/ 48|   1.013/ 55 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  79   |     251|       36.03|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  45   |      49|        6.21|   1.015/ 45|   1.004/ **|   1.001/ **|   1.000/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  78   |      25|        4.30|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  71   |      28|        5.17|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  85   |     110|       52.76|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  60   |      84|        5.27|   1.018/ 38|   1.016/ 43|   1.016/ 44|   1.015/ 46 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  72   |     973|       16.56|   1.062/ 11|   1.061/ 11|   1.061/ 11|   1.061/ 11 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  96   |   27734|      588.82|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  71   |      11|        0.51|   1.010/ 71|   1.012/ 59|   1.012/ 57|   1.013/ 55 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  86   |     380|        8.94|   1.055/ 12|   1.052/ 13|   1.051/ 13|   1.050/ 14 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  88   |    4797|      463.98|   1.011/ 63|   1.009/ 77|   1.009/ 81|   1.008/ 85 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  94   |    1949|      226.54|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  70   |       6|        0.34|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  68   |      21|        0.38|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  98   |      58|        0.87|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  72   |      14|        1.80|   1.003/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  74   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  80   |      49|        4.21|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  82   |    4757|       57.21|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  99   |  114465|      347.34|   1.009/ 80|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  86   |     836|       19.97|   1.019/ 36|   1.015/ 47|   1.014/ 50|   1.013/ 55 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  79   |     287|       29.04|   1.008/ 85|   1.004/ **|   1.002/ **|   1.001/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  88   |   41107|      618.74|   1.007/ 96|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  70   |      24|        6.71|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  72   |      16|        0.48|   1.018/ 39|   1.018/ 38|   1.018/ 38|   1.018/ 38 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  72   |      19|        0.59|   1.047/ 15|   1.060/ 11|   1.063/ 11|   1.066/ 10 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  66   |       7|        0.39|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  76   |       4|        0.26|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |

