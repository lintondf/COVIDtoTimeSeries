# State and Country COVID-19 Analysis #
## Updated: 2020-06-10 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  88   |   30901|     1588.44|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  92   |   12682|     1427.85|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  82   |    7657|     1101.75|   1.009/ 79|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  85   |    6280|      495.57|   1.013/ 54|   1.010/ 71|   1.009/ 78|   1.008/ 85 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  83   |    6264|      489.28|   1.010/ 72|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  83   |    5961|      596.88|   1.008/ 86|   1.008/ 91|   1.008/ 92|   1.007/ 93 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  98   |    4951|      125.31|   1.014/ 48|   1.012/ 57|   1.012/ 60|   1.011/ 63 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  83   |    4247|     1191.24|   1.006/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  88   |    3018|      649.16|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  83   |    2914|      481.96|   1.012/ 56|   1.010/ 72|   1.009/ 78|   1.008/ 84 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 102   |  116762|      354.31|   1.008/ 90|   1.006/ **|   1.005/ **|   1.005/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  91   |   41680|      627.37|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  85   |   41697|      197.23|   1.032/ 21|   1.027/ 25|   1.026/ 27|   1.025/ 28 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 110   |   34791|      577.55|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 116   |   30138|      449.31|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  99   |   27490|      583.64|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  83   |   15447|      122.04|   1.042/ 16|   1.039/ 18|   1.038/ 18|   1.037/ 18 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  91   |    9764|      847.28|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  93   |    8890|      106.92|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 111   |    8424|      101.03|   1.008/ 90|   1.008/ 92|   1.007/ 92|   1.007/ 93 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  77   |     731|      149.07|   1.016/ 43|   1.015/ 47|   1.014/ 48|   1.014/ 49 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  77   |      10|       13.74|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  81   |    1109|      152.36|   1.018/ 39|   1.015/ 46|   1.014/ 48|   1.014/ 50 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  78   |     161|       53.20|   1.020/ 34|   1.021/ 33|   1.021/ 33|   1.021/ 33 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  98   |    4951|      125.31|   1.014/ 48|   1.012/ 57|   1.012/ 60|   1.011/ 63 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  88   |    1635|      283.89|   1.009/ 80|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  83   |    4247|     1191.24|   1.006/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  76   |     418|      429.48|   1.013/ 55|   1.010/ 72|   1.009/ 78|   1.008/ 84 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  94   |    2849|      132.66|   1.013/ 55|   1.011/ 65|   1.010/ 68|   1.010/ 72 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  90   |    2327|      219.18|   1.012/ 57|   1.010/ 66|   1.010/ 69|   1.010/ 72 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  71   |      17|       12.01|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  76   |      86|       48.08|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  85   |    6280|      495.57|   1.013/ 54|   1.010/ 71|   1.009/ 78|   1.008/ 85 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  86   |    2418|      359.16|   1.010/ 68|   1.008/ 89|   1.007/ 96|   1.007/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  77   |     668|      211.87|   1.020/ 35|   1.015/ 47|   1.013/ 52|   1.012/ 58 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  89   |     239|       82.04|   1.008/ 90|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  86   |     492|      110.09|   1.012/ 56|   1.011/ 64|   1.010/ 66|   1.010/ 68 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  88   |    3018|      649.16|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  75   |     102|       76.18|   1.016/ 44|   1.015/ 45|   1.015/ 45|   1.015/ 45 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  83   |    2914|      481.96|   1.012/ 56|   1.010/ 72|   1.009/ 78|   1.008/ 84 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  82   |    7657|     1101.75|   1.009/ 79|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  83   |    5961|      596.88|   1.008/ 86|   1.008/ 91|   1.008/ 92|   1.007/ 93 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  81   |    1281|      227.16|   1.020/ 34|   1.018/ 39|   1.017/ 41|   1.016/ 43 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  83   |     885|      297.47|   1.018/ 38|   1.016/ 44|   1.015/ 46|   1.014/ 48 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  83   |     868|      141.48|   1.011/ 61|   1.008/ 82|   1.008/ 90|   1.007/ 99 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  75   |      18|       16.76|   1.006/ **|   1.007/ 93|   1.008/ 89|   1.008/ 86 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  74   |     201|      103.66|   1.016/ 44|   1.011/ 62|   1.010/ 69|   1.009/ 78 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  86   |     459|      149.07|   1.008/ 86|   1.006/ **|   1.005/ **|   1.005/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  79   |     305|      224.50|   1.020/ 34|   1.016/ 42|   1.016/ 44|   1.015/ 47 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  92   |   12682|     1427.85|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  77   |     422|      201.34|   1.015/ 45|   1.012/ 60|   1.011/ 65|   1.010/ 72 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  88   |   30901|     1588.44|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  77   |    1104|      105.23|   1.017/ 41|   1.015/ 47|   1.014/ 49|   1.013/ 52 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  75   |      75|       98.92|   1.021/ 34|   1.018/ 38|   1.018/ 39|   1.017/ 40 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  82   |    2557|      218.71|   1.014/ 51|   1.010/ 68|   1.009/ 75|   1.008/ 82 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  83   |     359|       90.68|   1.007/ 96|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  87   |     167|       39.57|   1.007/ 93|   1.007/ **|   1.007/ **|   1.006/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  83   |    6264|      489.28|   1.010/ 72|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  81   |     145|       45.36|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  74   |     841|      793.93|   1.017/ 40|   1.014/ 50|   1.013/ 53|   1.012/ 56 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  86   |     569|      110.50|   1.016/ 43|   1.015/ 45|   1.015/ 45|   1.015/ 46 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  91   |      72|       81.48|   1.014/ 49|   1.010/ 68|   1.009/ 75|   1.008/ 84 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  81   |     433|       63.42|   1.016/ 42|   1.016/ 44|   1.016/ 44|   1.016/ 44 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  85   |    1942|       66.99|   1.013/ 54|   1.010/ 69|   1.009/ 74|   1.009/ 80 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  80   |     131|       40.98|   1.016/ 44|   1.012/ 56|   1.012/ 60|   1.011/ 64 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  82   |      55|       88.75|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  88   |    1603|      187.75|   1.013/ 53|   1.009/ 73|   1.009/ 81|   1.008/ 91 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 102   |    1202|      157.90|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  72   |      85|       47.51|   1.010/ 67|   1.009/ 76|   1.009/ 78|   1.009/ 80 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  82   |     677|      116.23|   1.015/ 46|   1.014/ 50|   1.014/ 51|   1.013/ 52 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  58   |      19|       32.49|   1.016/ 44|   1.005/ **|   1.002/ **|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  80   |     367|       11.40|   1.040/ 17|   1.041/ 17|   1.041/ 17|   1.042/ 17 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  91   |      34|       11.91|   1.004/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  90   |     727|       16.90|   1.012/ 58|   1.012/ 59|   1.012/ 59|   1.012/ 59 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  73   |       4|        0.13|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  94   |     704|       15.67|   1.029/ 24|   1.029/ 24|   1.029/ 24|   1.029/ 24 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  76   |     225|       76.13|   1.060/ 11|   1.062/ 11|   1.062/ 11|   1.063/ 11 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 101   |     104|        4.05|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  90   |     681|       76.44|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  89   |      92|        9.19|   1.044/ 16|   1.047/ 15|   1.047/ 14|   1.048/ 14 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  86   |      26|       16.65|   1.050/ 14|   1.057/ 12|   1.058/ 12|   1.060/ 11 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  84   |     990|        5.88|   1.047/ 15|   1.046/ 15|   1.045/ 15|   1.045/ 15 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  71   |     285|       30.34|   1.022/ 32|   1.020/ 35|   1.019/ 36|   1.019/ 37 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  91   |    9764|      847.28|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  65   |       3|        0.30|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  73   |     510|       44.45|   1.044/ 16|   1.041/ 17|   1.041/ 17|   1.040/ 17 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  81   |     168|       50.97|   1.005/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  71   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  85   |   41697|      197.23|   1.032/ 21|   1.027/ 25|   1.026/ 27|   1.025/ 28 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  91   |     169|       24.31|   1.018/ 39|   1.016/ 43|   1.016/ 44|   1.015/ 45 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  84   |      54|        2.58|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  58   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  77   |     223|        8.41|   1.016/ 43|   1.014/ 51|   1.013/ 53|   1.012/ 56 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  93   |    8392|      220.85|   1.011/ 66|   1.008/ 92|   1.007/ **|   1.006/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  18   |       5|        0.95|   1.260/  3|   1.070/ 10|   1.048/ 14|   1.023/ 30 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  43   |      70|        4.33|   1.009/ 75|   1.009/ 80|   1.009/ 80|   1.009/ 79 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  80   |    1828|       95.69|   1.064/ 11|   1.065/ 10|   1.066/ 10|   1.066/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  91   |    4638|        3.31|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  80   |    1329|       26.91|   1.042/ 16|   1.045/ 15|   1.045/ 15|   1.046/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  83   |      11|        2.15|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  83   |     107|       26.13|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  84   |      84|        7.54|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  88   |     596|      102.32|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  85   |     551|       53.15|   1.010/ 71|   1.009/ 77|   1.009/ 79|   1.009/ 80 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  88   |    3958|      226.60|   1.010/ 69|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  94   |    1280|       12.77|   1.034/ 20|   1.036/ 19|   1.036/ 19|   1.037/ 19 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  71   |      61|        9.33|   1.030/ 23|   1.026/ 27|   1.024/ 28|   1.023/ 29 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  49   |      12|        8.97|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  66   |      26|        0.26|   1.127/  5|   1.154/  4|   1.161/  4|   1.167/  4 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  81   |     330|       59.75|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 116   |   30138|      449.31|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  82   |      23|       10.50|   1.011/ 62|   1.006/ **|   1.005/ **|   1.003/ ** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  79   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  67   |      13|        3.50|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  93   |    8890|      106.92|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  81   |      46|        1.51|   1.026/ 27|   1.027/ 26|   1.027/ 25|   1.027/ 25 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  91   |     186|       17.33|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  86   |     244|       14.69|   1.104/  6|   1.114/  6|   1.117/  6|   1.119/  6 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  56   |      24|        1.98|   1.008/ 87|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  45   |      12|        7.61|   1.047/ 15|   1.055/ 12|   1.057/ 12|   1.060/ 11 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  66   |      60|        5.17|   1.042/ 16|   1.037/ 18|   1.036/ 19|   1.034/ 20 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  76   |     275|       30.03|   1.028/ 25|   1.027/ 26|   1.026/ 26|   1.026/ 27 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  87   |     568|       58.09|   1.007/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  91   |    7882|        5.79|   1.041/ 17|   1.040/ 17|   1.039/ 17|   1.039/ 18 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  91   |    1951|        7.31|   1.022/ 31|   1.022/ 32|   1.022/ 32|   1.021/ 32 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 111   |    8424|      101.03|   1.008/ 90|   1.008/ 92|   1.007/ 92|   1.007/ 93 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  98   |     304|        7.78|   1.061/ 11|   1.070/ 10|   1.072/  9|   1.074/  9 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  91   |    1720|      349.44|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  81   |     299|       32.56|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 110   |   34791|      577.55|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  83   |      10|        3.59|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 118   |    1055|        8.37|   1.005/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  75   |       9|        0.84|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  77   |      54|        2.88|   1.034/ 20|   1.041/ 17|   1.043/ 16|   1.045/ 15 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  76   |      87|        1.84|   1.031/ 22|   1.032/ 22|   1.032/ 22|   1.032/ 21 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  76   |      31|       17.04|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  67   |     292|       66.02|   1.035/ 19|   1.028/ 24|   1.027/ 26|   1.025/ 28 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  68   |      22|        3.44|   1.032/ 22|   1.038/ 18|   1.039/ 18|   1.041/ 17 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  68   |      26|       13.76|   1.010/ 70|   1.008/ 84|   1.008/ 88|   1.007/ 92 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  92   |      28|        4.16|   1.010/ 71|   1.012/ 57|   1.013/ 54|   1.013/ 51 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  67   |      31|        6.94|   1.013/ 54|   1.011/ 64|   1.010/ 66|   1.010/ 69 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  69   |       6|        0.82|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  81   |      75|       27.02|   1.007/ 99|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  24   |       9|        0.36|   1.037/ 19|   1.070/ 10|   1.076/  9|   1.080/  8 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  85   |     117|        3.58|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  73   |      97|        4.79|   1.023/ 29|   1.020/ 35|   1.019/ 36|   1.018/ 38 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  72   |      70|       17.15|   1.127/  5|   1.121/  6|   1.120/  6|   1.118/  6 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  83   |   15447|      122.04|   1.042/ 16|   1.039/ 18|   1.038/ 18|   1.037/ 18 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  84   |     366|      136.54|   1.022/ 31|   1.020/ 34|   1.020/ 34|   1.020/ 35 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  92   |     212|        5.90|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  16   |       2|        0.07|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  25   |      15|        0.51|   1.099/  7|   1.085/  8|   1.082/  8|   1.077/  9 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  96   |    6163|      353.05|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  73   |      22|        4.47|   1.002/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  75   |      64|        9.98|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  77   |      69|        3.08|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  79   |     378|        1.84|   1.029/ 24|   1.027/ 26|   1.026/ 26|   1.026/ 27 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  80   |     159|       76.51|   1.020/ 34|   1.021/ 33|   1.021/ 33|   1.021/ 33 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  88   |     241|       44.86|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  71   |      84|       18.11|   1.057/ 12|   1.057/ 12|   1.057/ 12|   1.057/ 12 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  83   |    2149|        9.80|   1.044/ 16|   1.046/ 15|   1.046/ 15|   1.047/ 15 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  91   |     399|       94.49|   1.018/ 39|   1.018/ 39|   1.018/ 39|   1.018/ 38 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  81   |      11|        1.55|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  82   |    6063|      188.70|   1.031/ 22|   1.027/ 26|   1.026/ 27|   1.025/ 28 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 129   |    1100|       10.14|   1.007/ 93|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  90   |    1201|       31.28|   1.010/ 71|   1.008/ 83|   1.008/ 87|   1.008/ 91 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  85   |    1523|      148.18|   1.008/ 89|   1.007/ **|   1.007/ **|   1.006/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  74   |      62|       22.70|   1.062/ 11|   1.063/ 11|   1.063/ 11|   1.063/ 11 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  80   |    1378|       71.02|   1.007/ 95|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  83   |    6511|       44.37|   1.034/ 20|   1.031/ 22|   1.030/ 23|   1.030/ 23 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  11   |       2|        0.16|   1.260/  2|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  78   |     735|       21.49|   1.046/ 15|   1.050/ 14|   1.051/ 13|   1.052/ 13 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  70   |      53|        3.26|   1.024/ 28|   1.020/ 35|   1.018/ 37|   1.017/ 40 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  82   |     253|       36.29|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  48   |      50|        6.32|   1.011/ 60|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  81   |      25|        4.38|   1.006/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  74   |      28|        5.16|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  88   |     111|       52.83|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  63   |      87|        5.49|   1.017/ 40|   1.015/ 45|   1.015/ 47|   1.014/ 49 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  75   |    1160|       19.74|   1.062/ 11|   1.061/ 11|   1.061/ 11|   1.060/ 11 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  99   |   27490|      583.64|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  74   |      11|        0.52|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  89   |     439|       10.33|   1.045/ 15|   1.040/ 17|   1.039/ 18|   1.037/ 18 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  91   |    4896|      473.60|   1.009/ 76|   1.007/ 98|   1.007/ **|   1.006/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  97   |    1947|      226.30|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  73   |       6|        0.37|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  71   |      21|        0.38|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 101   |      58|        0.88|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  75   |      13|        1.79|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  77   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  83   |      50|        4.23|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  85   |    4808|       57.81|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 102   |  116762|      354.31|   1.008/ 90|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  89   |     869|       20.75|   1.017/ 40|   1.013/ 53|   1.012/ 57|   1.011/ 62 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  82   |     291|       29.47|   1.007/ 93|   1.004/ **|   1.003/ **|   1.003/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  91   |   41680|      627.37|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  73   |      24|        6.75|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  75   |      18|        0.51|   1.020/ 35|   1.021/ 32|   1.022/ 32|   1.022/ 31 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  75   |      23|        0.71|   1.039/ 18|   1.047/ 15|   1.048/ 14|   1.050/ 14 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  69   |       7|        0.42|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  79   |       4|        0.26|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |

