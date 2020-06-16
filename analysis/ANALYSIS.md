# State and Country COVID-19 Analysis #
## Updated: 2020-06-16 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  94   |   31197|     1603.66|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  98   |   12986|     1462.07|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  88   |    7897|     1136.31|   1.007/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  91   |    6626|      522.87|   1.010/ 67|   1.008/ 88|   1.007/ 95|   1.007/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  89   |    6483|      506.37|   1.007/ 93|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  89   |    6165|      617.33|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 104   |    5335|      135.03|   1.013/ 52|   1.012/ 59|   1.011/ 61|   1.011/ 63 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  89   |    4321|     1211.86|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  94   |    3088|      664.27|   1.005/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  89   |    3069|      507.58|   1.010/ 69|   1.008/ 88|   1.007/ 95|   1.007/ ** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 108   |  120711|      366.30|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  91   |   48142|      227.72|   1.027/ 26|   1.022/ 31|   1.021/ 33|   1.020/ 35 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  97   |   42828|      644.66|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 116   |   35005|      581.11|   1.001/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 122   |   30162|      449.67|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 105   |   27218|      577.88|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  89   |   19072|      150.67|   1.037/ 19|   1.033/ 21|   1.032/ 21|   1.031/ 22 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  97   |    9856|        7.24|   1.039/ 17|   1.038/ 18|   1.038/ 18|   1.038/ 18 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  97   |    9795|      849.95|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 117   |    8859|      106.25|   1.008/ 82|   1.009/ 81|   1.009/ 81|   1.009/ 81 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  83   |     799|      162.95|   1.015/ 47|   1.013/ 52|   1.013/ 53|   1.013/ 54 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  83   |      11|       15.30|   1.010/ 68|   1.013/ 52|   1.014/ 48|   1.015/ 46 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  87   |    1229|      168.91|   1.018/ 38|   1.017/ 40|   1.017/ 41|   1.016/ 42 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  84   |     184|       60.81|   1.021/ 32|   1.022/ 32|   1.022/ 32|   1.022/ 32 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 104   |    5335|      135.03|   1.013/ 52|   1.012/ 59|   1.011/ 61|   1.011/ 63 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  94   |    1680|      291.72|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  89   |    4321|     1211.86|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  82   |     439|      450.44|   1.010/ 72|   1.007/ 94|   1.007/ **|   1.006/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 100   |    3041|      141.58|   1.012/ 59|   1.010/ 67|   1.010/ 69|   1.010/ 71 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  96   |    2519|      237.26|   1.014/ 51|   1.013/ 54|   1.013/ 54|   1.013/ 55 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  77   |      17|       12.01|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  82   |      88|       49.08|   1.004/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  91   |    6626|      522.87|   1.010/ 67|   1.008/ 88|   1.007/ 95|   1.007/ ** |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  92   |    2518|      373.96|   1.008/ 85|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  83   |     709|      224.64|   1.013/ 53|   1.008/ 85|   1.007/ **|   1.006/ ** |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  95   |     250|       85.70|   1.007/ 95|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  92   |     521|      116.73|   1.010/ 66|   1.009/ 77|   1.009/ 80|   1.008/ 83 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  94   |    3088|      664.27|   1.005/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  81   |     107|       79.50|   1.009/ 81|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  89   |    3069|      507.58|   1.010/ 69|   1.008/ 88|   1.007/ 95|   1.007/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  88   |    7897|     1136.31|   1.007/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  89   |    6165|      617.33|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  87   |    1408|      249.63|   1.017/ 41|   1.014/ 48|   1.014/ 51|   1.013/ 53 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  89   |     954|      320.45|   1.014/ 50|   1.011/ 63|   1.010/ 67|   1.010/ 73 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  89   |     919|      149.66|   1.010/ 66|   1.009/ 81|   1.008/ 86|   1.008/ 91 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  81   |      19|       17.42|   1.007/ **|   1.007/ 94|   1.008/ 91|   1.008/ 89 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  80   |     222|      114.75|   1.018/ 38|   1.017/ 41|   1.016/ 42|   1.016/ 43 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  92   |     477|      154.90|   1.007/ 96|   1.006/ **|   1.005/ **|   1.005/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  85   |     337|      248.06|   1.018/ 38|   1.015/ 45|   1.015/ 47|   1.014/ 49 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  98   |   12986|     1462.07|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  83   |     452|      215.63|   1.014/ 50|   1.011/ 60|   1.011/ 63|   1.010/ 67 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  94   |   31197|     1603.66|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  83   |    1195|      113.90|   1.014/ 49|   1.012/ 58|   1.011/ 61|   1.011/ 65 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  81   |      80|      105.08|   1.012/ 58|   1.008/ 86|   1.007/ 99|   1.006/ ** |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  88   |    2694|      230.49|   1.011/ 63|   1.008/ 83|   1.008/ 90|   1.007/ 98 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  89   |     370|       93.45|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  93   |     176|       41.70|   1.009/ 81|   1.009/ 81|   1.009/ 81|   1.009/ 81 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  89   |    6483|      506.37|   1.007/ 93|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  87   |     149|       46.70|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  80   |     892|      841.97|   1.012/ 58|   1.008/ 82|   1.008/ 92|   1.007/ ** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  92   |     620|      120.50|   1.014/ 48|   1.013/ 52|   1.013/ 52|   1.013/ 53 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  97   |      79|       88.75|   1.016/ 43|   1.014/ 49|   1.014/ 51|   1.013/ 53 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  87   |     481|       70.33|   1.018/ 39|   1.018/ 38|   1.018/ 38|   1.018/ 38 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  91   |    2063|       71.15|   1.011/ 62|   1.009/ 74|   1.009/ 77|   1.008/ 82 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  86   |     144|       44.91|   1.017/ 41|   1.016/ 44|   1.015/ 45|   1.015/ 46 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  88   |      55|       88.75|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  94   |    1668|      195.36|   1.009/ 78|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 108   |    1239|      162.72|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  78   |      90|       50.09|   1.009/ 75|   1.008/ 82|   1.008/ 84|   1.008/ 85 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  88   |     727|      124.84|   1.012/ 57|   1.011/ 66|   1.010/ 69|   1.010/ 72 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  64   |      19|       33.00|   1.009/ 75|   1.002/ **|   1.000/ --|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  86   |     475|       14.74|   1.040/ 17|   1.042/ 16|   1.042/ 16|   1.042/ 16 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  97   |      35|       12.45|   1.007/ **|   1.008/ 89|   1.008/ 86|   1.008/ 83 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  96   |     779|       18.12|   1.012/ 59|   1.012/ 59|   1.012/ 60|   1.012/ 60 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  79   |       5|        0.17|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 100   |     844|       18.79|   1.030/ 23|   1.031/ 22|   1.031/ 22|   1.031/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  82   |     307|      103.91|   1.051/ 14|   1.049/ 14|   1.048/ 14|   1.047/ 14 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 107   |     103|        4.03|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  96   |     686|       77.06|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  95   |     122|       12.12|   1.044/ 16|   1.046/ 15|   1.046/ 15|   1.046/ 15 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  92   |      38|       24.48|   1.064/ 11|   1.073/  9|   1.075/  9|   1.077/  9 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  90   |    1268|        7.53|   1.043/ 16|   1.041/ 17|   1.040/ 17|   1.040/ 17 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  77   |     319|       33.91|   1.019/ 35|   1.018/ 38|   1.018/ 39|   1.017/ 40 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  97   |    9795|      849.95|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  71   |       5|        0.39|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  79   |     646|       56.36|   1.042/ 16|   1.041/ 17|   1.040/ 17|   1.040/ 17 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  87   |     169|       51.21|   1.003/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  77   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  91   |   48142|      227.72|   1.027/ 26|   1.022/ 31|   1.021/ 33|   1.020/ 35 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  97   |     183|       26.32|   1.014/ 50|   1.012/ 58|   1.011/ 60|   1.011/ 63 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  90   |      54|        2.57|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  64   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  83   |     237|        8.94|   1.008/ 90|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  99   |    8703|      229.04|   1.008/ 90|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  24   |       7|        1.34|   1.045/ 15|   1.072/ 10|   1.079/  9|   1.087/  8 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  49   |      74|        4.54|   1.008/ 92|   1.007/ **|   1.007/ **|   1.006/ ** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  86   |    3284|      171.85|   1.066/ 10|   1.067/ 10|   1.068/ 10|   1.068/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  97   |    4638|        3.31|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  86   |    1733|       35.09|   1.043/ 16|   1.045/ 15|   1.045/ 15|   1.046/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  89   |      12|        2.33|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  89   |     108|       26.53|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  90   |      85|        7.55|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  94   |     603|      103.64|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  91   |     590|       56.93|   1.012/ 56|   1.013/ 55|   1.013/ 54|   1.013/ 54 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  94   |    4079|      233.52|   1.009/ 76|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 100   |    1582|       15.78|   1.036/ 19|   1.038/ 18|   1.038/ 18|   1.038/ 18 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  77   |      75|       11.60|   1.036/ 19|   1.036/ 19|   1.036/ 19|   1.036/ 19 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  55   |      12|        8.85|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  72   |      59|        0.60|   1.134/  5|   1.153/  4|   1.158/  4|   1.163/  4 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  87   |     331|       59.91|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 122   |   30162|      449.67|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  88   |      26|       12.08|   1.012/ 56|   1.009/ 74|   1.009/ 81|   1.008/ 89 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  85   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  73   |      14|        3.67|   1.009/ 76|   1.011/ 60|   1.012/ 57|   1.013/ 55 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  99   |    8961|      107.77|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  87   |      53|        1.74|   1.024/ 29|   1.025/ 28|   1.025/ 28|   1.025/ 27 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  97   |     188|       17.53|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  92   |     440|       26.50|   1.074/  9|   1.074/  9|   1.074/  9|   1.074/  9 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  62   |      25|        2.05|   1.010/ 66|   1.010/ 67|   1.010/ 66|   1.011/ 65 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  51   |      16|        9.81|   1.040/ 17|   1.044/ 16|   1.045/ 15|   1.046/ 15 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  72   |      76|        6.53|   1.044/ 16|   1.041/ 17|   1.041/ 17|   1.040/ 17 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  82   |     327|       35.71|   1.028/ 25|   1.027/ 25|   1.027/ 25|   1.027/ 26 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  93   |     579|       59.28|   1.005/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  97   |    9856|        7.24|   1.039/ 17|   1.038/ 18|   1.038/ 18|   1.038/ 18 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  97   |    2206|        8.27|   1.021/ 32|   1.021/ 33|   1.021/ 33|   1.021/ 33 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 117   |    8859|      106.25|   1.008/ 82|   1.009/ 81|   1.009/ 81|   1.009/ 81 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 104   |     490|       12.53|   1.077/  9|   1.086/  8|   1.088/  8|   1.090/  8 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  97   |    1735|      352.62|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  87   |     304|       33.09|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 116   |   35005|      581.11|   1.001/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  89   |      10|        3.72|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 124   |    1048|        8.32|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  81   |       9|        0.84|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  83   |      73|        3.92|   1.044/ 16|   1.051/ 13|   1.053/ 13|   1.055/ 12 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  82   |     105|        2.22|   1.032/ 21|   1.033/ 21|   1.033/ 21|   1.033/ 21 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  82   |      32|       17.62|   1.006/ **|   1.007/ 95|   1.008/ 90|   1.008/ 86 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  73   |     324|       73.38|   1.024/ 29|   1.017/ 42|   1.015/ 47|   1.013/ 54 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  74   |      28|        4.31|   1.032/ 22|   1.034/ 20|   1.035/ 20|   1.036/ 19 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  74   |      28|       14.62|   1.012/ 58|   1.012/ 56|   1.012/ 56|   1.013/ 55 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  98   |      31|        4.51|   1.012/ 59|   1.014/ 50|   1.015/ 48|   1.015/ 46 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  73   |      33|        7.37|   1.011/ 62|   1.010/ 70|   1.010/ 72|   1.009/ 75 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  75   |       7|        1.06|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  87   |      78|       27.79|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  30   |      11|        0.40|   1.052/ 13|   1.014/ 50|   1.003/ **|   1.000/ -- |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  91   |     119|        3.65|   1.003/ **|   1.003/ **|   1.003/ **|   1.004/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  79   |     109|        5.37|   1.021/ 33|   1.019/ 37|   1.018/ 38|   1.017/ 40 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  78   |     129|       31.59|   1.088/  8|   1.079/  9|   1.077/  9|   1.074/  9 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  89   |   19072|      150.67|   1.037/ 19|   1.033/ 21|   1.032/ 21|   1.031/ 22 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  90   |     416|      154.95|   1.022/ 31|   1.022/ 32|   1.021/ 32|   1.021/ 32 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  98   |     215|        5.99|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  22   |       2|        0.07|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  31   |      19|        0.65|   1.068/ 10|   1.053/ 13|   1.050/ 14|   1.048/ 14 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 102   |    6179|      353.98|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  79   |      22|        4.47|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  81   |      72|       11.14|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  83   |      68|        3.05|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  85   |     440|        2.14|   1.027/ 26|   1.025/ 28|   1.024/ 28|   1.024/ 29 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  86   |     184|       88.77|   1.026/ 27|   1.027/ 25|   1.028/ 25|   1.028/ 24 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  94   |     242|       45.16|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  77   |     113|       24.14|   1.051/ 14|   1.048/ 14|   1.048/ 14|   1.047/ 14 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  89   |    2792|       12.73|   1.044/ 16|   1.045/ 15|   1.045/ 15|   1.045/ 15 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  97   |     444|      105.16|   1.017/ 40|   1.018/ 39|   1.018/ 39|   1.018/ 39 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  87   |      11|        1.56|   1.001/ **|   1.001/ **|   1.001/ **|   1.002/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  88   |    7042|      219.16|   1.028/ 25|   1.025/ 27|   1.025/ 28|   1.024/ 29 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 135   |    1145|       10.55|   1.008/ 88|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  96   |    1271|       33.12|   1.010/ 71|   1.009/ 76|   1.009/ 78|   1.009/ 79 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  91   |    1565|      152.28|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  80   |      84|       30.50|   1.050/ 14|   1.044/ 15|   1.043/ 16|   1.042/ 17 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  86   |    1430|       73.68|   1.007/ 96|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  89   |    7633|       52.01|   1.029/ 24|   1.025/ 27|   1.024/ 28|   1.023/ 30 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  17   |       2|        0.16|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  84   |     989|       28.90|   1.047/ 15|   1.050/ 14|   1.050/ 14|   1.051/ 13 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  76   |      61|        3.79|   1.029/ 24|   1.029/ 24|   1.029/ 24|   1.029/ 24 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  88   |     256|       36.76|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  54   |      52|        6.55|   1.008/ 90|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  87   |      26|        4.54|   1.007/ **|   1.007/ 98|   1.007/ 97|   1.007/ 96 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  80   |      28|        5.14|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  94   |     110|       52.76|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  69   |      91|        5.75|   1.011/ 61|   1.008/ 88|   1.007/ 99|   1.006/ ** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  81   |    1620|       27.56|   1.058/ 12|   1.056/ 12|   1.055/ 12|   1.055/ 12 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 105   |   27218|      577.88|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  80   |      11|        0.53|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  95   |     553|       13.03|   1.038/ 18|   1.033/ 21|   1.031/ 22|   1.030/ 23 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  97   |    5086|      491.92|   1.007/ 97|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 103   |    1950|      226.65|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  79   |       7|        0.39|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  77   |      21|        0.38|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 107   |      58|        0.88|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  81   |      13|        1.77|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  83   |       8|        5.87|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  89   |      50|        4.24|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  91   |    4900|       58.93|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 108   |  120711|      366.30|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  95   |     948|       22.63|   1.016/ 43|   1.013/ 52|   1.013/ 54|   1.012/ 57 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  88   |     299|       30.24|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  97   |   42828|      644.66|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  79   |      24|        6.73|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  81   |      20|        0.58|   1.017/ 41|   1.016/ 42|   1.016/ 43|   1.016/ 43 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  81   |      27|        0.85|   1.026/ 27|   1.029/ 24|   1.029/ 23|   1.030/ 23 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  75   |      10|        0.56|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  85   |       4|        0.26|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |

