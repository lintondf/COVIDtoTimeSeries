# State and Country COVID-19 Analysis #
## Updated: 2020-06-14 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  92   |   31103|     1598.86|   1.002/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  96   |   12883|     1450.46|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  86   |    7824|     1125.79|   1.007/ 95|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  89   |    6525|      514.95|   1.012/ 59|   1.009/ 74|   1.009/ 78|   1.008/ 84 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  87   |    6419|      501.39|   1.008/ 83|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  87   |    6111|      611.95|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 102   |    5213|      131.94|   1.014/ 48|   1.013/ 54|   1.012/ 56|   1.012/ 58 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  87   |    4298|     1205.47|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  92   |    3067|      659.84|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  87   |    3023|      500.01|   1.011/ 62|   1.009/ 77|   1.008/ 82|   1.008/ 88 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 106   |  119514|      362.66|   1.007/ 98|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  89   |   46097|      218.04|   1.030/ 23|   1.025/ 27|   1.024/ 29|   1.023/ 30 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  95   |   42502|      639.74|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 114   |   34938|      580.00|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 120   |   30160|      449.64|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 103   |   27291|      579.42|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  87   |   17902|      141.43|   1.040/ 17|   1.037/ 19|   1.036/ 19|   1.036/ 19 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  95   |    9788|      849.30|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  95   |    9133|        6.71|   1.040/ 17|   1.039/ 18|   1.038/ 18|   1.038/ 18 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  97   |    8942|      107.54|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  81   |     780|      159.02|   1.017/ 42|   1.016/ 43|   1.016/ 44|   1.016/ 44 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  81   |      11|       14.60|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  85   |    1190|      163.46|   1.019/ 36|   1.018/ 39|   1.018/ 39|   1.017/ 40 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  82   |     176|       58.37|   1.023/ 30|   1.024/ 29|   1.024/ 28|   1.024/ 28 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 102   |    5213|      131.94|   1.014/ 48|   1.013/ 54|   1.012/ 56|   1.012/ 58 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  92   |    1668|      289.60|   1.007/ 96|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  87   |    4298|     1205.47|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  80   |     433|      444.32|   1.011/ 65|   1.008/ 86|   1.007/ 93|   1.007/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  98   |    2981|      138.77|   1.013/ 55|   1.011/ 61|   1.011/ 63|   1.011/ 65 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  94   |    2457|      231.37|   1.014/ 48|   1.014/ 51|   1.014/ 51|   1.013/ 52 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  75   |      17|       12.01|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  80   |      87|       48.75|   1.004/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  89   |    6525|      514.95|   1.012/ 59|   1.009/ 74|   1.009/ 78|   1.008/ 84 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  90   |    2487|      369.42|   1.009/ 77|   1.007/ 98|   1.007/ **|   1.006/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  81   |     698|      221.22|   1.016/ 44|   1.011/ 66|   1.009/ 75|   1.008/ 86 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  93   |     247|       84.61|   1.008/ 87|   1.007/ 93|   1.007/ 95|   1.007/ 97 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  90   |     513|      114.78|   1.012/ 58|   1.011/ 65|   1.010/ 67|   1.010/ 68 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  92   |    3067|      659.84|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  79   |     106|       78.81|   1.011/ 65|   1.008/ 81|   1.008/ 88|   1.007/ 95 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  87   |    3023|      500.01|   1.011/ 62|   1.009/ 77|   1.008/ 82|   1.008/ 88 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  86   |    7824|     1125.79|   1.007/ 95|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  87   |    6111|      611.95|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  85   |    1370|      242.91|   1.019/ 37|   1.016/ 42|   1.016/ 44|   1.015/ 45 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  87   |     934|      313.97|   1.016/ 43|   1.013/ 52|   1.013/ 55|   1.012/ 58 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  87   |     904|      147.22|   1.012/ 59|   1.010/ 70|   1.009/ 74|   1.009/ 77 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  79   |      18|       17.08|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  78   |     215|      111.15|   1.021/ 33|   1.020/ 34|   1.020/ 35|   1.020/ 35 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  90   |     472|      153.17|   1.008/ 84|   1.007/ **|   1.007/ **|   1.006/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  83   |     328|      241.03|   1.020/ 34|   1.018/ 38|   1.017/ 40|   1.017/ 41 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  96   |   12883|     1450.46|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  81   |     442|      210.75|   1.014/ 49|   1.011/ 60|   1.011/ 64|   1.010/ 68 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  92   |   31103|     1598.86|   1.002/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  81   |    1169|      111.41|   1.016/ 43|   1.014/ 49|   1.014/ 50|   1.013/ 52 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  79   |      79|      103.76|   1.015/ 45|   1.012/ 58|   1.011/ 62|   1.010/ 67 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  86   |    2652|      226.90|   1.012/ 58|   1.009/ 75|   1.009/ 81|   1.008/ 88 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  87   |     367|       92.79|   1.007/ **|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  91   |     173|       40.95|   1.008/ 82|   1.008/ 84|   1.008/ 84|   1.008/ 84 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  87   |    6419|      501.39|   1.008/ 83|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  85   |     148|       46.26|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  78   |     878|      828.93|   1.014/ 49|   1.011/ 64|   1.010/ 69|   1.009/ 76 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  90   |     605|      117.54|   1.016/ 43|   1.016/ 44|   1.015/ 45|   1.015/ 45 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  95   |      77|       86.47|   1.018/ 38|   1.016/ 42|   1.016/ 43|   1.016/ 44 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  85   |     464|       67.93|   1.018/ 39|   1.018/ 39|   1.018/ 39|   1.018/ 39 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  89   |    2025|       69.84|   1.012/ 57|   1.010/ 68|   1.010/ 71|   1.009/ 75 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  84   |     140|       43.56|   1.017/ 40|   1.016/ 43|   1.016/ 44|   1.015/ 45 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  86   |      55|       88.78|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  92   |    1650|      193.36|   1.010/ 66|   1.007/ 98|   1.006/ **|   1.005/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 106   |    1227|      161.09|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  76   |      88|       49.34|   1.010/ 68|   1.010/ 71|   1.010/ 71|   1.010/ 72 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  86   |     713|      122.39|   1.014/ 49|   1.013/ 53|   1.013/ 54|   1.012/ 56 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  62   |      19|       33.00|   1.013/ 54|   1.005/ **|   1.003/ **|   1.001/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  84   |     438|       13.59|   1.042/ 16|   1.044/ 16|   1.045/ 15|   1.045/ 15 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  95   |      35|       12.26|   1.007/ 99|   1.008/ 85|   1.008/ 82|   1.009/ 79 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  94   |     761|       17.71|   1.012/ 58|   1.012/ 59|   1.012/ 59|   1.012/ 59 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  77   |       5|        0.17|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  98   |     795|       17.69|   1.030/ 23|   1.031/ 22|   1.031/ 22|   1.031/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  80   |     280|       94.68|   1.055/ 12|   1.055/ 12|   1.055/ 13|   1.054/ 13 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 105   |     104|        4.03|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  94   |     684|       76.88|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  93   |     112|       11.11|   1.046/ 15|   1.049/ 14|   1.049/ 14|   1.050/ 14 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  90   |      33|       21.30|   1.059/ 12|   1.066/ 10|   1.068/ 10|   1.070/ 10 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  88   |    1173|        6.96|   1.044/ 15|   1.043/ 16|   1.042/ 16|   1.042/ 16 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  75   |     308|       32.75|   1.020/ 34|   1.019/ 36|   1.019/ 37|   1.018/ 38 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  95   |    9788|      849.30|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  69   |       4|        0.35|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  77   |     597|       52.02|   1.042/ 16|   1.040/ 17|   1.040/ 17|   1.039/ 17 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  85   |     169|       51.09|   1.004/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  75   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  89   |   46097|      218.04|   1.030/ 23|   1.025/ 27|   1.024/ 29|   1.023/ 30 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  95   |     179|       25.69|   1.015/ 46|   1.013/ 52|   1.013/ 54|   1.012/ 56 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  88   |      54|        2.57|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  62   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  81   |     229|        8.62|   1.010/ 69|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  97   |    8615|      226.71|   1.009/ 81|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  22   |       7|        1.20|   1.052/ 13|   1.064/ 11|   1.079/  9|   1.097/  7 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  47   |      73|        4.48|   1.008/ 83|   1.008/ 88|   1.008/ 89|   1.008/ 90 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  84   |    2778|      145.38|   1.066/ 10|   1.067/ 10|   1.068/ 10|   1.068/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  95   |    4638|        3.31|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  84   |    1587|       32.13|   1.043/ 16|   1.045/ 15|   1.045/ 15|   1.046/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  87   |      12|        2.28|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  87   |     108|       26.42|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  88   |      85|        7.55|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  92   |     601|      103.22|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  89   |     574|       55.38|   1.011/ 64|   1.011/ 66|   1.011/ 66|   1.010/ 66 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  92   |    4032|      230.83|   1.009/ 76|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  98   |    1465|       14.61|   1.033/ 21|   1.034/ 20|   1.034/ 20|   1.035/ 20 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  75   |      70|       10.83|   1.037/ 18|   1.038/ 18|   1.038/ 18|   1.038/ 18 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  53   |      12|        8.87|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  70   |      46|        0.47|   1.126/  5|   1.146/  5|   1.151/  4|   1.156/  4 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  85   |     331|       59.86|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 120   |   30160|      449.64|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  86   |      25|       11.49|   1.017/ 40|   1.014/ 48|   1.014/ 51|   1.013/ 54 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  83   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  71   |      13|        3.59|   1.003/ **|   1.003/ **|   1.003/ **|   1.004/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  97   |    8942|      107.54|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  85   |      50|        1.64|   1.021/ 34|   1.020/ 35|   1.020/ 35|   1.019/ 35 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  95   |     187|       17.48|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  90   |     372|       22.41|   1.081/  8|   1.084/  8|   1.084/  8|   1.085/  8 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  60   |      24|        2.00|   1.007/ 99|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  49   |      15|        9.09|   1.038/ 18|   1.044/ 16|   1.045/ 15|   1.047/ 15 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  70   |      70|        6.03|   1.044/ 15|   1.042/ 16|   1.041/ 17|   1.040/ 17 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  80   |     311|       33.91|   1.030/ 23|   1.030/ 23|   1.030/ 23|   1.030/ 23 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  91   |     576|       58.89|   1.005/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  95   |    9133|        6.71|   1.040/ 17|   1.039/ 18|   1.038/ 18|   1.038/ 18 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  95   |    2117|        7.93|   1.021/ 32|   1.021/ 33|   1.021/ 33|   1.021/ 34 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 115   |    8703|      104.38|   1.008/ 85|   1.008/ 86|   1.008/ 86|   1.008/ 86 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 102   |     417|       10.65|   1.070/ 10|   1.079/  9|   1.081/  8|   1.083/  8 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  95   |    1732|      351.85|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  85   |     303|       32.94|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 114   |   34938|      580.00|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  87   |      10|        3.68|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 122   |    1052|        8.35|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  79   |       9|        0.84|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  81   |      66|        3.53|   1.042/ 16|   1.049/ 14|   1.051/ 13|   1.053/ 13 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  80   |      99|        2.08|   1.031/ 22|   1.032/ 21|   1.032/ 21|   1.033/ 21 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  80   |      31|       17.34|   1.004/ **|   1.004/ **|   1.004/ **|   1.005/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  71   |     315|       71.19|   1.027/ 26|   1.019/ 36|   1.017/ 40|   1.015/ 46 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  72   |      26|        4.05|   1.034/ 20|   1.039/ 18|   1.040/ 17|   1.041/ 17 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  72   |      27|       14.28|   1.010/ 66|   1.010/ 69|   1.010/ 70|   1.010/ 70 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  96   |      30|        4.39|   1.011/ 60|   1.014/ 50|   1.014/ 48|   1.015/ 46 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  71   |      32|        7.22|   1.012/ 60|   1.010/ 69|   1.010/ 72|   1.009/ 74 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  73   |       6|        0.90|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  85   |      77|       27.54|   1.007/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  28   |      11|        0.41|   1.062/ 11|   1.034/ 20|   1.024/ 29|   1.013/ 54 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  89   |     118|        3.62|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  77   |     105|        5.18|   1.022/ 31|   1.020/ 35|   1.019/ 36|   1.019/ 37 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  76   |     106|       25.91|   1.104/  7|   1.107/  6|   1.107/  6|   1.107/  6 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  87   |   17902|      141.43|   1.040/ 17|   1.037/ 19|   1.036/ 19|   1.036/ 19 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  88   |     398|      148.49|   1.022/ 31|   1.021/ 33|   1.021/ 33|   1.020/ 34 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  96   |     214|        5.96|   1.003/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  20   |       2|        0.07|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  29   |      18|        0.59|   1.082/  8|   1.046/ 15|   1.036/ 19|   1.026/ 26 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 100   |    6175|      353.75|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  77   |      22|        4.47|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  79   |      71|       10.95|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  81   |      68|        3.05|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  83   |     419|        2.03|   1.028/ 25|   1.026/ 27|   1.025/ 27|   1.025/ 28 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  84   |     174|       83.90|   1.023/ 30|   1.024/ 29|   1.024/ 29|   1.024/ 29 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  92   |     242|       45.06|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  75   |     102|       21.97|   1.052/ 13|   1.050/ 14|   1.050/ 14|   1.049/ 14 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  87   |    2554|       11.64|   1.043/ 16|   1.045/ 15|   1.045/ 15|   1.045/ 15 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  95   |     428|      101.45|   1.017/ 40|   1.017/ 40|   1.017/ 40|   1.017/ 40 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  85   |      11|        1.54|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  86   |    6677|      207.79|   1.027/ 25|   1.024/ 29|   1.023/ 30|   1.022/ 31 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 133   |    1128|       10.39|   1.007/ 96|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  94   |    1248|       32.51|   1.010/ 69|   1.009/ 75|   1.009/ 77|   1.009/ 78 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  89   |    1553|      151.15|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  78   |      77|       28.07|   1.057/ 12|   1.054/ 13|   1.053/ 13|   1.052/ 13 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  84   |    1410|       72.64|   1.007/ **|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  87   |    7278|       49.60|   1.031/ 22|   1.028/ 24|   1.027/ 25|   1.026/ 26 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  15   |       2|        0.16|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  82   |     898|       26.25|   1.047/ 14|   1.051/ 14|   1.051/ 13|   1.052/ 13 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  74   |      58|        3.58|   1.026/ 26|   1.025/ 27|   1.025/ 28|   1.025/ 28 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  86   |     255|       36.58|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  52   |      51|        6.49|   1.009/ 77|   1.007/ 99|   1.007/ **|   1.006/ ** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  85   |      26|        4.48|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  78   |      28|        5.14|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  92   |     111|       52.80|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  67   |      90|        5.67|   1.012/ 57|   1.008/ 83|   1.007/ 95|   1.006/ ** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  79   |    1456|       24.78|   1.060/ 11|   1.059/ 12|   1.058/ 12|   1.058/ 12 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 103   |   27291|      579.42|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  78   |      11|        0.53|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  93   |     516|       12.16|   1.041/ 17|   1.036/ 19|   1.034/ 20|   1.033/ 21 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  95   |    5033|      486.87|   1.008/ 84|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 101   |    1949|      226.56|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  77   |       7|        0.39|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  75   |      21|        0.38|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 105   |      58|        0.88|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  79   |      13|        1.77|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  81   |       8|        5.87|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  87   |      50|        4.24|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  89   |    4871|       58.58|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 106   |  119514|      362.66|   1.007/ 98|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  93   |     922|       22.02|   1.017/ 40|   1.014/ 48|   1.014/ 50|   1.013/ 53 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  86   |     297|       30.00|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  95   |   42502|      639.74|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  77   |      24|        6.75|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  79   |      19|        0.56|   1.020/ 35|   1.021/ 33|   1.021/ 33|   1.021/ 32 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  79   |      26|        0.80|   1.024/ 28|   1.027/ 26|   1.027/ 25|   1.028/ 25 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  73   |       9|        0.52|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  83   |       4|        0.26|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |

