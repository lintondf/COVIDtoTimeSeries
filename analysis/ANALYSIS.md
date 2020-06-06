# State and Country COVID-19 Analysis #
## Updated: 2020-06-06 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  84   |   30694|     1577.82|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  88   |   12491|     1406.27|   1.007/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  78   |    7454|     1072.57|   1.011/ 62|   1.009/ 81|   1.008/ 87|   1.007/ 94 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  79   |    6090|      475.67|   1.012/ 56|   1.009/ 79|   1.008/ 88|   1.007/ 99 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  81   |    6027|      475.66|   1.016/ 44|   1.012/ 57|   1.011/ 61|   1.010/ 66 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  79   |    5722|      572.96|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  94   |    4707|      119.12|   1.016/ 43|   1.014/ 50|   1.013/ 53|   1.013/ 55 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  79   |    4187|     1174.51|   1.008/ 89|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  84   |    2959|      636.45|   1.007/ 98|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  79   |    2799|      462.93|   1.015/ 47|   1.012/ 60|   1.011/ 64|   1.010/ 69 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  98   |  113867|      345.53|   1.009/ 77|   1.007/ **|   1.006/ **|   1.006/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  87   |   40835|      614.65|   1.007/ 94|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  81   |   37183|      175.88|   1.038/ 18|   1.032/ 21|   1.031/ 22|   1.030/ 23 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 106   |   34623|      574.76|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 112   |   30113|      448.93|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  95   |   27785|      589.90|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  79   |   13169|      104.04|   1.049/ 14|   1.047/ 15|   1.046/ 15|   1.046/ 15 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  87   |    9730|      844.26|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  89   |    8832|      106.22|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 107   |    8170|       97.98|   1.007/ 93|   1.007/ 98|   1.007/ 99|   1.007/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  73   |     690|      140.67|   1.015/ 45|   1.012/ 57|   1.011/ 61|   1.011/ 66 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  73   |      10|       13.68|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  77   |    1041|      142.99|   1.020/ 34|   1.017/ 41|   1.016/ 43|   1.015/ 46 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  74   |     148|       48.89|   1.023/ 30|   1.025/ 27|   1.026/ 27|   1.026/ 26 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  94   |    4707|      119.12|   1.016/ 43|   1.014/ 50|   1.013/ 53|   1.013/ 55 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  84   |    1596|      277.15|   1.012/ 58|   1.009/ 77|   1.008/ 84|   1.007/ 93 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  79   |    4187|     1174.51|   1.008/ 89|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  72   |     403|      413.62|   1.014/ 48|   1.010/ 68|   1.009/ 75|   1.008/ 85 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  90   |    2726|      126.90|   1.014/ 49|   1.012/ 58|   1.011/ 61|   1.011/ 64 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  86   |    2232|      210.21|   1.014/ 48|   1.013/ 54|   1.012/ 55|   1.012/ 57 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  67   |      17|       12.01|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  72   |      85|       47.79|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  81   |    6027|      475.66|   1.016/ 44|   1.012/ 57|   1.011/ 61|   1.010/ 66 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  82   |    2343|      347.98|   1.011/ 60|   1.008/ 83|   1.008/ 92|   1.007/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  73   |     630|      199.81|   1.025/ 27|   1.020/ 34|   1.019/ 37|   1.018/ 39 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  85   |     232|       79.69|   1.008/ 85|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  82   |     470|      105.24|   1.015/ 47|   1.014/ 50|   1.013/ 51|   1.013/ 52 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  84   |    2959|      636.45|   1.007/ 98|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  71   |      96|       71.62|   1.019/ 37|   1.020/ 34|   1.021/ 34|   1.021/ 33 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  79   |    2799|      462.93|   1.015/ 47|   1.012/ 60|   1.011/ 64|   1.010/ 69 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  78   |    7454|     1072.57|   1.011/ 62|   1.009/ 81|   1.008/ 87|   1.007/ 94 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  79   |    5722|      572.96|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  77   |    1192|      211.39|   1.023/ 30|   1.020/ 35|   1.019/ 37|   1.018/ 38 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  79   |     833|      279.87|   1.022/ 31|   1.020/ 35|   1.019/ 36|   1.019/ 37 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  79   |     838|      136.51|   1.014/ 51|   1.010/ 69|   1.009/ 75|   1.008/ 82 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  71   |      17|       16.19|   1.002/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  70   |     191|       98.92|   1.021/ 33|   1.017/ 41|   1.016/ 43|   1.015/ 46 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  82   |     448|      145.46|   1.010/ 68|   1.008/ 88|   1.007/ 94|   1.007/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  75   |     285|      209.71|   1.025/ 27|   1.022/ 32|   1.021/ 33|   1.020/ 34 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  88   |   12491|     1406.27|   1.007/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  73   |     402|      191.94|   1.019/ 37|   1.014/ 48|   1.013/ 52|   1.012/ 56 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  84   |   30694|     1577.82|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  73   |    1039|       99.08|   1.021/ 33|   1.020/ 35|   1.019/ 35|   1.019/ 36 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  71   |      70|       91.56|   1.023/ 29|   1.022/ 32|   1.021/ 33|   1.021/ 33 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  78   |    2451|      209.69|   1.018/ 39|   1.015/ 47|   1.014/ 49|   1.013/ 52 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  79   |     350|       88.46|   1.009/ 81|   1.008/ 90|   1.007/ 93|   1.007/ 95 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  83   |     162|       38.52|   1.007/ 96|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  79   |    6090|      475.67|   1.012/ 56|   1.009/ 79|   1.008/ 88|   1.007/ 99 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  77   |     142|       44.39|   1.008/ 89|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  70   |     796|      751.83|   1.021/ 33|   1.019/ 37|   1.018/ 38|   1.017/ 40 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  82   |     535|      103.95|   1.014/ 48|   1.013/ 55|   1.012/ 57|   1.012/ 60 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  87   |      69|       78.50|   1.017/ 40|   1.013/ 53|   1.012/ 57|   1.011/ 63 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  77   |     406|       59.43|   1.017/ 41|   1.016/ 43|   1.016/ 43|   1.016/ 43 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  81   |    1860|       64.16|   1.015/ 46|   1.012/ 56|   1.012/ 60|   1.011/ 64 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  76   |     125|       39.04|   1.018/ 38|   1.015/ 46|   1.014/ 49|   1.013/ 52 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  78   |      55|       88.59|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  84   |    1541|      180.55|   1.017/ 40|   1.014/ 49|   1.013/ 52|   1.012/ 56 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  98   |    1182|      155.19|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  68   |      82|       45.59|   1.011/ 65|   1.008/ 83|   1.008/ 88|   1.007/ 94 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  78   |     639|      109.73|   1.017/ 40|   1.017/ 40|   1.017/ 41|   1.017/ 41 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  54   |      19|       32.28|   1.029/ 24|   1.022/ 32|   1.020/ 35|   1.018/ 39 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  76   |     314|        9.75|   1.033/ 21|   1.031/ 22|   1.030/ 23|   1.030/ 23 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  87   |      33|       11.67|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  86   |     694|       16.13|   1.012/ 58|   1.012/ 59|   1.012/ 59|   1.012/ 60 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  69   |       4|        0.14|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  90   |     629|       14.00|   1.027/ 26|   1.026/ 26|   1.026/ 27|   1.026/ 27 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  72   |     176|       59.51|   1.069/ 10|   1.076/  9|   1.078/  9|   1.080/  8 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  97   |     104|        4.06|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  86   |     675|       75.79|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  85   |      77|        7.65|   1.043/ 16|   1.046/ 15|   1.047/ 15|   1.048/ 14 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  82   |      21|       13.47|   1.038/ 18|   1.042/ 16|   1.043/ 16|   1.044/ 16 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  80   |     828|        4.92|   1.049/ 14|   1.048/ 14|   1.047/ 14|   1.047/ 15 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  67   |     264|       28.10|   1.023/ 31|   1.020/ 35|   1.019/ 36|   1.019/ 37 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  87   |    9730|      844.26|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  61   |       3|        0.28|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  69   |     430|       37.46|   1.049/ 14|   1.048/ 14|   1.048/ 14|   1.048/ 14 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  77   |     168|       50.86|   1.008/ 85|   1.003/ **|   1.002/ **|   1.000/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  67   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  81   |   37183|      175.88|   1.038/ 18|   1.032/ 21|   1.031/ 22|   1.030/ 23 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  87   |     158|       22.74|   1.017/ 41|   1.014/ 48|   1.014/ 50|   1.013/ 52 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  80   |      54|        2.58|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  54   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  73   |     211|        7.96|   1.019/ 36|   1.018/ 39|   1.017/ 40|   1.017/ 41 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  89   |    8110|      213.43|   1.013/ 53|   1.010/ 71|   1.009/ 77|   1.008/ 85 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  14   |      64|       11.64|   1.089/  8|   1.313/  2|   1.126/  5|   1.000/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  39   |      68|        4.17|   1.010/ 71|   1.005/ **|   1.004/ **|   1.002/ ** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  76   |    1425|       74.57|   1.064/ 11|   1.065/ 10|   1.066/ 10|   1.066/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  87   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  76   |    1112|       22.51|   1.039/ 18|   1.041/ 17|   1.042/ 16|   1.042/ 16 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  79   |      11|        2.16|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  79   |     106|       25.95|   1.003/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  80   |      85|        7.55|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  84   |     589|      101.20|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  81   |     530|       51.17|   1.010/ 69|   1.009/ 77|   1.009/ 80|   1.008/ 82 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  84   |    3902|      223.37|   1.012/ 58|   1.005/ **|   1.004/ **|   1.002/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  90   |    1110|       11.07|   1.035/ 20|   1.037/ 19|   1.037/ 18|   1.038/ 18 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  67   |      55|        8.46|   1.036/ 19|   1.032/ 22|   1.031/ 22|   1.030/ 23 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  45   |      13|        9.28|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  62   |      14|        0.14|   1.106/  6|   1.130/  5|   1.136/  5|   1.142/  5 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  77   |     329|       59.56|   1.004/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 112   |   30113|      448.93|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  78   |      20|        9.43|   1.056/ 12|   1.063/ 11|   1.064/ 11|   1.066/ 10 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  75   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  63   |      13|        3.41|   1.004/ **|   1.004/ **|   1.004/ **|   1.005/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  89   |    8832|      106.22|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  77   |      41|        1.35|   1.019/ 37|   1.015/ 45|   1.014/ 48|   1.014/ 50 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  87   |     184|       17.12|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  82   |     148|        8.94|   1.089/  8|   1.098/  7|   1.100/  7|   1.102/  7 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  52   |      24|        1.99|   1.015/ 45|   1.007/ 95|   1.005/ **|   1.003/ ** |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  41   |       9|        5.73|   1.024/ 28|   1.008/ 88|   1.003/ **|   1.000/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  62   |      52|        4.51|   1.052/ 13|   1.054/ 13|   1.054/ 13|   1.055/ 13 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  72   |     248|       27.07|   1.031/ 22|   1.030/ 23|   1.030/ 23|   1.030/ 23 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  83   |     556|       56.94|   1.008/ 84|   1.006/ **|   1.006/ **|   1.005/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  87   |    6747|        4.96|   1.041/ 17|   1.039/ 17|   1.039/ 18|   1.039/ 18 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  87   |    1794|        6.72|   1.023/ 31|   1.022/ 31|   1.022/ 31|   1.022/ 31 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 107   |    8170|       97.98|   1.007/ 93|   1.007/ 98|   1.007/ 99|   1.007/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  94   |     222|        5.68|   1.048/ 14|   1.055/ 13|   1.056/ 12|   1.058/ 12 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  87   |    1708|      347.13|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  77   |     295|       32.07|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 106   |   34623|      574.76|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  79   |       9|        3.44|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 114   |    1049|        8.33|   1.008/ 85|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  71   |       9|        0.84|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  73   |      45|        2.39|   1.030/ 23|   1.039/ 18|   1.041/ 17|   1.043/ 16 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  72   |      77|        1.61|   1.032/ 21|   1.032/ 21|   1.032/ 21|   1.033/ 21 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  72   |      30|       16.90|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  63   |     261|       59.08|   1.040/ 17|   1.031/ 23|   1.028/ 24|   1.026/ 27 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  64   |      19|        2.90|   1.031/ 22|   1.040/ 17|   1.043/ 16|   1.045/ 15 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  64   |      25|       13.35|   1.011/ 65|   1.009/ 80|   1.008/ 85|   1.008/ 91 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  88   |      27|        3.96|   1.004/ **|   1.005/ **|   1.005/ **|   1.006/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  63   |      30|        6.63|   1.014/ 51|   1.011/ 61|   1.011/ 65|   1.010/ 69 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  65   |       5|        0.78|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  77   |      74|       26.60|   1.011/ 63|   1.009/ 76|   1.009/ 81|   1.008/ 86 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  20   |       7|        0.26|   1.256/  3|   1.059/ 12|   1.029/ 24|   1.009/ 81 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  81   |     117|        3.57|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  69   |      89|        4.41|   1.025/ 27|   1.021/ 33|   1.020/ 35|   1.019/ 37 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  68   |      43|       10.55|   1.077/  9|   1.139/  5|   1.192/  3|   1.115/  6 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  79   |   13169|      104.04|   1.049/ 14|   1.047/ 15|   1.046/ 15|   1.046/ 15 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  80   |     338|      126.20|   1.021/ 33|   1.017/ 40|   1.016/ 42|   1.016/ 44 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  88   |     210|        5.84|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  12   |       2|        0.07|   1.200/  3|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  21   |      11|        0.36|   1.130/  5|   1.094/  7|   1.085/  8|   1.078/  9 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  92   |    6148|      352.16|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  69   |      22|        4.44|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  71   |      56|        8.65|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  73   |      69|        3.10|   1.007/ 95|   1.002/ **|   1.001/ **|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  75   |     340|        1.65|   1.031/ 22|   1.028/ 25|   1.027/ 26|   1.026/ 26 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  76   |     146|       70.45|   1.023/ 30|   1.025/ 28|   1.025/ 27|   1.026/ 27 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  84   |     241|       44.84|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  67   |      67|       14.46|   1.067/ 10|   1.072/  9|   1.074/  9|   1.075/  9 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  79   |    1794|        8.18|   1.041/ 17|   1.041/ 17|   1.041/ 17|   1.041/ 17 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  87   |     370|       87.76|   1.015/ 45|   1.014/ 48|   1.014/ 48|   1.014/ 49 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  77   |      11|        1.56|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  78   |    5453|      169.72|   1.034/ 20|   1.030/ 23|   1.029/ 24|   1.028/ 25 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 125   |    1074|        9.90|   1.009/ 79|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  86   |    1159|       30.20|   1.010/ 67|   1.008/ 83|   1.008/ 88|   1.007/ 93 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  81   |    1481|      144.08|   1.009/ 74|   1.009/ 78|   1.009/ 79|   1.009/ 81 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  70   |      49|       17.96|   1.064/ 11|   1.069/ 10|   1.070/ 10|   1.071/ 10 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  76   |    1349|       69.51|   1.008/ 83|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  79   |    5747|       39.16|   1.039/ 18|   1.036/ 19|   1.036/ 19|   1.035/ 20 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  74   |     605|       17.68|   1.041/ 17|   1.044/ 16|   1.045/ 15|   1.046/ 15 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  66   |      49|        3.03|   1.026/ 27|   1.018/ 39|   1.016/ 44|   1.014/ 50 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  78   |     251|       35.99|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  44   |      49|        6.21|   1.017/ 40|   1.004/ **|   1.001/ **|   1.000/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  77   |      24|        4.26|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  70   |      28|        5.18|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  84   |     110|       52.76|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  59   |      82|        5.19|   1.019/ 36|   1.018/ 39|   1.017/ 40|   1.017/ 42 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  71   |     919|       15.63|   1.062/ 11|   1.062/ 11|   1.061/ 11|   1.061/ 11 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  95   |   27785|      589.90|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  70   |      11|        0.50|   1.011/ 64|   1.014/ 50|   1.014/ 48|   1.015/ 45 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  85   |     358|        8.44|   1.058/ 12|   1.055/ 13|   1.054/ 13|   1.053/ 13 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  87   |    4750|      459.50|   1.011/ 61|   1.009/ 74|   1.009/ 78|   1.008/ 82 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  93   |    1949|      226.53|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  69   |       6|        0.33|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  67   |      21|        0.38|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  97   |      58|        0.87|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  71   |      14|        1.80|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  73   |       8|        5.87|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  79   |      49|        4.21|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  81   |    4735|       56.94|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  98   |  113867|      345.53|   1.009/ 77|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  85   |     823|       19.64|   1.020/ 35|   1.015/ 46|   1.014/ 49|   1.013/ 54 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  78   |     287|       28.99|   1.009/ 79|   1.004/ **|   1.003/ **|   1.002/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  87   |   40835|      614.65|   1.007/ 94|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  69   |      24|        6.68|   1.007/ 96|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  71   |      16|        0.47|   1.017/ 40|   1.018/ 39|   1.018/ 39|   1.018/ 39 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  71   |      12|        0.36|   1.048/ 14|   1.063/ 11|   1.067/ 10|   1.071/ 10 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  65   |       7|        0.39|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  75   |       4|        0.26|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |

