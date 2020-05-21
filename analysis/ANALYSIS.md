# State and Country COVID-19 Analysis #
## Updated: 2020-05-21 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# Notes #

- Expect discontinuities in the US around 4/14/2020 as the [CDC](CDC "https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html")  expanded the definition of a COVID-19 death.  
- There is also some weekly pattern to reporting with lower values on the weekend followed by higher values subsequently, at least in some places.
- The Y axis upper limit for DDGR charts was lowered from 2.0 to 1.5 on 4/28 to better show current lower values.  

# Ten US States with Highest Death Tolls #

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. One per million is 0.0001%.  1% is 10,000 per million.

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDeathRates.png)

Daily Death Growth Rate (DDGR) in the 10 US States with the highest death tolls.

DDGR is the cube root of Arnold Kling's [Three Day Death Reproduction Rate (3DDRR)](http://www.arnoldkling.com/blog/the-3ddrr/).  The 3DDRR is calculated by dividing the cumulative total number of deaths on a given day by the  cumulative total number of deaths three days previously.  Taking the cube root converts this to the geometric mean for the three days.  These values are LOWESS filtered to generate a local-error minimizing non-parametric trend.

If deaths remain constant over the three days, the DDGR equals one.  A value of 2 would indicate that the number of deaths doubles every day.

![US States with Highest Death Toll - Daily Death Growth Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  68   |   29328|     1507.59|   1.008/ 86|   1.006/ **|   1.005/ **|   1.004/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  72   |   11396|     1283.00|   1.017/ 40|   1.011/ 62|   1.010/ 71|   1.008/ 84 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  62   |    6367|      916.25|   1.023/ 30|   1.016/ 42|   1.015/ 47|   1.013/ 53 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  63   |    5187|      519.39|   1.012/ 57|   1.008/ 91|   1.007/ **|   1.005/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  63   |    5122|      400.07|   1.028/ 25|   1.017/ 40|   1.015/ 47|   1.012/ 58 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  65   |    4703|      371.14|   1.030/ 23|   1.025/ 27|   1.024/ 29|   1.023/ 30 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  63   |    3660|     1026.50|   1.020/ 35|   1.015/ 47|   1.014/ 51|   1.012/ 56 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  78   |    3650|       92.38|   1.025/ 28|   1.020/ 35|   1.019/ 37|   1.017/ 40 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  68   |    2666|      573.54|   1.014/ 48|   1.012/ 60|   1.011/ 63|   1.010/ 67 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  63   |    2232|      369.13|   1.029/ 24|   1.022/ 32|   1.020/ 34|   1.018/ 37 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  82   |   99398|      301.62|   1.017/ 42|   1.011/ 62|   1.010/ 70|   1.009/ 80 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  71   |   37876|      570.11|   1.012/ 56|   1.008/ 86|   1.007/ **|   1.006/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  90   |   33415|      554.70|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  96   |   29857|      445.13|   1.005/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  79   |   28641|      608.09|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  65   |   19742|       93.38|   1.057/ 12|   1.051/ 13|   1.050/ 14|   1.048/ 14 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  71   |    9469|      821.62|   1.007/ 94|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  73   |    8449|      101.62|   1.008/ 85|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  91   |    7324|       87.84|   1.008/ 87|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  73   |    6774|      178.28|   1.025/ 27|   1.016/ 43|   1.014/ 50|   1.011/ 61 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  57   |     549|      111.87|   1.030/ 23|   1.022/ 31|   1.021/ 34|   1.019/ 37 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  57   |      10|       13.99|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  61   |     787|      108.10|   1.039/ 18|   1.033/ 21|   1.032/ 22|   1.030/ 23 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  58   |     110|       36.36|   1.017/ 40|   1.007/ 97|   1.005/ **|   1.002/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  78   |    3650|       92.38|   1.025/ 28|   1.020/ 35|   1.019/ 37|   1.017/ 40 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  68   |    1294|      224.73|   1.025/ 27|   1.024/ 29|   1.024/ 29|   1.024/ 29 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  63   |    3660|     1026.50|   1.020/ 35|   1.015/ 47|   1.014/ 51|   1.012/ 56 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  56   |     320|      328.44|   1.035/ 20|   1.031/ 22|   1.030/ 23|   1.030/ 23 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  74   |    2205|      102.66|   1.022/ 31|   1.018/ 39|   1.016/ 42|   1.015/ 46 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  70   |    1767|      166.42|   1.019/ 36|   1.015/ 47|   1.014/ 51|   1.013/ 55 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  51   |      17|       12.06|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  56   |      76|       42.37|   1.010/ 66|   1.010/ 69|   1.010/ 69|   1.010/ 70 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  65   |    4703|      371.14|   1.030/ 23|   1.025/ 27|   1.024/ 29|   1.023/ 30 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  66   |    1980|      294.13|   1.025/ 27|   1.017/ 40|   1.015/ 46|   1.013/ 53 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  57   |     406|      128.63|   1.042/ 16|   1.034/ 20|   1.032/ 21|   1.030/ 23 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  69   |     212|       72.77|   1.017/ 41|   1.013/ 55|   1.011/ 60|   1.010/ 67 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  66   |     374|       83.68|   1.020/ 34|   1.018/ 39|   1.017/ 40|   1.017/ 42 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  68   |    2666|      573.54|   1.014/ 48|   1.012/ 60|   1.011/ 63|   1.010/ 67 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  55   |      74|       54.94|   1.014/ 49|   1.012/ 59|   1.011/ 61|   1.011/ 64 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  63   |    2232|      369.13|   1.029/ 24|   1.022/ 32|   1.020/ 34|   1.018/ 37 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  62   |    6367|      916.25|   1.023/ 30|   1.016/ 42|   1.015/ 47|   1.013/ 53 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  63   |    5187|      519.39|   1.012/ 57|   1.008/ 91|   1.007/ **|   1.005/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  61   |     835|      148.01|   1.036/ 19|   1.026/ 26|   1.024/ 29|   1.021/ 32 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  63   |     597|      200.53|   1.033/ 21|   1.027/ 25|   1.026/ 27|   1.024/ 29 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  63   |     670|      109.20|   1.028/ 24|   1.024/ 29|   1.022/ 31|   1.021/ 33 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  55   |      16|       15.00|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  54   |     133|       68.93|   1.035/ 20|   1.034/ 20|   1.034/ 21|   1.033/ 21 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  66   |     383|      124.27|   1.020/ 35|   1.016/ 43|   1.015/ 46|   1.014/ 50 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  59   |     199|      146.14|   1.043/ 16|   1.033/ 21|   1.031/ 22|   1.028/ 24 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  72   |   11396|     1283.00|   1.017/ 40|   1.011/ 62|   1.010/ 71|   1.008/ 84 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  57   |     301|      143.32|   1.039/ 18|   1.031/ 22|   1.029/ 24|   1.027/ 26 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  68   |   29328|     1507.59|   1.008/ 86|   1.006/ **|   1.005/ **|   1.004/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  57   |     752|       71.70|   1.027/ 25|   1.022/ 32|   1.020/ 34|   1.018/ 37 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  55   |      50|       65.26|   1.036/ 19|   1.027/ 26|   1.024/ 28|   1.022/ 32 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  62   |    1833|      156.80|   1.029/ 24|   1.023/ 30|   1.022/ 32|   1.020/ 34 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  63   |     307|       77.46|   1.011/ 61|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  67   |     148|       35.18|   1.014/ 50|   1.010/ 73|   1.008/ 82|   1.007/ 95 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  63   |    5122|      400.07|   1.028/ 25|   1.017/ 40|   1.015/ 47|   1.012/ 58 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  61   |     129|       40.50|   1.015/ 46|   1.012/ 58|   1.011/ 62|   1.010/ 67 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  54   |     558|      526.56|   1.029/ 24|   1.020/ 34|   1.018/ 38|   1.016/ 42 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  66   |     438|       85.00|   1.022/ 32|   1.014/ 48|   1.013/ 55|   1.011/ 64 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  71   |      57|       64.42|   1.032/ 21|   1.026/ 27|   1.024/ 28|   1.022/ 31 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  61   |     317|       46.39|   1.021/ 33|   1.019/ 37|   1.018/ 38|   1.018/ 39 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  65   |    1466|       50.56|   1.028/ 24|   1.025/ 28|   1.024/ 29|   1.023/ 30 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  60   |      91|       28.33|   1.032/ 22|   1.029/ 24|   1.028/ 25|   1.027/ 26 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  62   |      55|       87.70|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  68   |    1155|      135.27|   1.028/ 25|   1.019/ 36|   1.017/ 40|   1.015/ 46 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  82   |    1066|      140.00|   1.011/ 62|   1.009/ 78|   1.008/ 83|   1.008/ 89 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  52   |      70|       39.25|   1.025/ 28|   1.024/ 29|   1.024/ 29|   1.024/ 29 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  62   |     489|       84.03|   1.019/ 36|   1.016/ 42|   1.015/ 45|   1.015/ 47 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  38   |       9|       16.39|   1.011/ 62|   1.027/ 25|   1.032/ 22|   1.037/ 19 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  60   |     195|        6.05|   1.048/ 14|   1.042/ 16|   1.040/ 17|   1.039/ 18 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  71   |      32|       11.10|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  70   |     568|       13.20|   1.012/ 57|   1.012/ 57|   1.012/ 57|   1.012/ 57 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  53   |       2|        0.06|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  74   |     417|        9.27|   1.028/ 24|   1.025/ 27|   1.024/ 28|   1.024/ 29 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  56   |      64|       21.78|   1.038/ 18|   1.042/ 17|   1.043/ 16|   1.044/ 16 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  81   |     105|        4.08|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  70   |     646|       72.61|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  69   |      42|        4.16|   1.032/ 22|   1.034/ 20|   1.035/ 20|   1.035/ 20 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  66   |      12|        7.62|   1.026/ 26|   1.034/ 20|   1.036/ 19|   1.038/ 18 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  64   |     367|        2.18|   1.050/ 14|   1.057/ 12|   1.058/ 12|   1.060/ 11 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  51   |     184|       19.53|   1.035/ 20|   1.031/ 22|   1.030/ 23|   1.029/ 24 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  71   |    9469|      821.62|   1.007/ 94|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  45   |       2|        0.17|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  53   |     205|       17.86|   1.056/ 12|   1.049/ 14|   1.047/ 15|   1.045/ 15 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  61   |     149|       45.29|   1.032/ 22|   1.026/ 27|   1.024/ 29|   1.022/ 31 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  51   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  65   |   19742|       93.38|   1.057/ 12|   1.051/ 13|   1.050/ 14|   1.048/ 14 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  71   |     119|       17.11|   1.026/ 27|   1.022/ 31|   1.021/ 32|   1.020/ 34 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  64   |      53|        2.54|   1.006/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  38   |       1|        0.09|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  57   |     166|        6.26|   1.021/ 33|   1.019/ 36|   1.018/ 38|   1.018/ 39 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  73   |    6774|      178.28|   1.025/ 27|   1.016/ 43|   1.014/ 50|   1.011/ 61 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  23   |      58|        3.58|   1.087/  8|   1.043/ 16|   1.031/ 22|   1.019/ 36 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  60   |     497|       26.03|   1.050/ 14|   1.057/ 12|   1.059/ 12|   1.061/ 11 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  71   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  60   |     654|       13.24|   1.035/ 20|   1.030/ 23|   1.029/ 24|   1.027/ 25 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  63   |      10|        1.96|   1.046/ 15|   1.059/ 12|   1.062/ 11|   1.065/ 10 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  63   |     102|       25.09|   1.011/ 66|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  64   |      84|        7.52|   1.008/ 87|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  68   |     572|       98.27|   1.007/ 96|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  65   |     462|       44.65|   1.016/ 43|   1.012/ 57|   1.011/ 62|   1.010/ 68 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  68   |    3376|      193.29|   1.042/ 17|   1.035/ 20|   1.033/ 21|   1.032/ 22 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  74   |     696|        6.94|   1.027/ 25|   1.024/ 29|   1.023/ 30|   1.022/ 31 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  51   |      33|        5.03|   1.062/ 11|   1.060/ 11|   1.059/ 12|   1.059/ 12 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  29   |       8|        5.69|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  46   |       5|        0.05|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  61   |     314|       56.83|   1.015/ 46|   1.010/ 68|   1.009/ 78|   1.008/ 90 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  96   |   29857|      445.13|   1.005/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  62   |      13|        6.12|   1.046/ 15|   1.032/ 22|   1.028/ 25|   1.024/ 28 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  59   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  47   |      13|        3.43|   1.021/ 33|   1.010/ 67|   1.007/ 94|   1.004/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  73   |    8449|      101.62|   1.008/ 85|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  61   |      32|        1.04|   1.037/ 19|   1.039/ 18|   1.040/ 17|   1.040/ 17 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  71   |     167|       15.54|   1.009/ 79|   1.008/ 87|   1.008/ 89|   1.008/ 90 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  66   |      41|        2.44|   1.053/ 13|   1.058/ 12|   1.059/ 12|   1.060/ 11 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  36   |      18|        1.51|   1.043/ 16|   1.047/ 15|   1.047/ 15|   1.046/ 15 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  25   |       6|        3.57|   1.107/  6|   1.116/  6|   1.131/  5|   1.147/  5 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  46   |      24|        2.06|   1.049/ 14|   1.031/ 22|   1.026/ 26|   1.021/ 33 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  56   |     159|       17.34|   1.034/ 20|   1.026/ 27|   1.024/ 29|   1.022/ 32 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  67   |     494|       50.52|   1.017/ 40|   1.012/ 58|   1.011/ 66|   1.009/ 75 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  71   |    3689|        2.71|   1.051/ 13|   1.045/ 15|   1.043/ 16|   1.042/ 17 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  71   |    1217|        4.56|   1.024/ 29|   1.024/ 28|   1.025/ 28|   1.025/ 28 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  91   |    7324|       87.84|   1.008/ 87|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  78   |     129|        3.30|   1.020/ 34|   1.022/ 31|   1.023/ 30|   1.023/ 30 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  71   |    1657|      336.73|   1.009/ 74|   1.004/ **|   1.002/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  61   |     283|       30.84|   1.011/ 62|   1.009/ 73|   1.009/ 77|   1.009/ 80 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  90   |   33415|      554.70|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  63   |       9|        3.43|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  98   |     925|        7.35|   1.024/ 29|   1.016/ 44|   1.014/ 50|   1.012/ 58 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  55   |       9|        0.85|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  57   |      36|        1.92|   1.015/ 48|   1.012/ 59|   1.011/ 62|   1.010/ 66 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  56   |      56|        1.18|   1.050/ 14|   1.044/ 16|   1.042/ 16|   1.040/ 17 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  56   |      31|       17.40|   1.006/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  47   |     138|       31.26|   1.082/  8|   1.077/  9|   1.075/  9|   1.073/  9 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  48   |      15|        2.22|   1.020/ 34|   1.012/ 59|   1.010/ 69|   1.008/ 82 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  48   |      20|       10.69|   1.014/ 50|   1.014/ 49|   1.014/ 48|   1.015/ 47 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  72   |      27|        3.91|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  47   |      22|        4.93|   1.013/ 51|   1.017/ 40|   1.019/ 37|   1.020/ 34 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  49   |       3|        0.44|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  61   |      59|       21.16|   1.018/ 38|   1.021/ 33|   1.021/ 32|   1.022/ 31 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  65   |     115|        3.51|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  53   |      57|        2.79|   1.040/ 17|   1.038/ 18|   1.037/ 18|   1.037/ 19 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  52   |       1|        0.25|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  63   |    6292|       49.71|   1.058/ 12|   1.053/ 13|   1.052/ 13|   1.050/ 14 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  64   |     237|       88.22|   1.034/ 20|   1.030/ 23|   1.029/ 23|   1.028/ 24 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  72   |     199|        5.54|   1.005/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  76   |    6001|      343.76|   1.007/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  53   |      21|        4.26|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  55   |      10|        1.53|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  57   |      58|        2.62|   1.026/ 26|   1.023/ 30|   1.022/ 31|   1.021/ 32 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  59   |     227|        1.10|   1.049/ 14|   1.030/ 23|   1.025/ 28|   1.020/ 34 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  60   |     107|       51.62|   1.017/ 41|   1.015/ 45|   1.015/ 45|   1.015/ 46 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  68   |     237|       44.20|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  51   |      27|        5.69|   1.058/ 12|   1.070/ 10|   1.073/  9|   1.077/  9 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  63   |    1035|        4.72|   1.043/ 16|   1.035/ 19|   1.033/ 21|   1.031/ 22 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  71   |     299|       70.88|   1.020/ 35|   1.016/ 43|   1.015/ 46|   1.014/ 49 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  61   |      11|        1.56|   1.007/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  62   |    3157|       98.26|   1.052/ 13|   1.045/ 15|   1.044/ 16|   1.042/ 16 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 109   |     950|        8.75|   1.017/ 41|   1.013/ 53|   1.012/ 57|   1.011/ 62 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  70   |    1007|       26.25|   1.019/ 36|   1.014/ 50|   1.013/ 54|   1.012/ 60 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  65   |    1274|      124.00|   1.011/ 64|   1.008/ 84|   1.008/ 90|   1.007/ 98 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  54   |      16|        5.74|   1.017/ 41|   1.016/ 44|   1.015/ 45|   1.015/ 46 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  60   |    1200|       61.82|   1.021/ 33|   1.016/ 43|   1.015/ 47|   1.013/ 52 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  63   |    3137|       21.38|   1.048/ 14|   1.039/ 18|   1.037/ 19|   1.035/ 20 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  58   |     349|       10.20|   1.035/ 20|   1.032/ 22|   1.031/ 22|   1.030/ 23 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  50   |      32|        1.99|   1.065/ 10|   1.057/ 12|   1.054/ 13|   1.051/ 13 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  62   |     248|       35.66|   1.011/ 62|   1.009/ 79|   1.008/ 85|   1.007/ 93 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  28   |      36|        4.59|   1.078/  9|   1.056/ 12|   1.047/ 15|   1.036/ 19 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  61   |      23|        4.10|   1.013/ 55|   1.004/ **|   1.002/ **|   1.000/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  54   |      29|        5.25|   1.009/ 81|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  68   |     108|       51.60|   1.005/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  43   |      61|        3.86|   1.031/ 22|   1.016/ 43|   1.013/ 54|   1.009/ 73 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  55   |     326|        5.54|   1.056/ 12|   1.056/ 12|   1.056/ 12|   1.056/ 12 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  79   |   28641|      608.09|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  54   |       9|        0.43|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  69   |     130|        3.06|   1.063/ 11|   1.051/ 14|   1.047/ 14|   1.044/ 16 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  71   |    3990|      385.92|   1.018/ 38|   1.013/ 51|   1.012/ 56|   1.011/ 61 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  77   |    1947|      226.32|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  53   |       3|        0.17|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  51   |      22|        0.40|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  81   |      57|        0.86|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  55   |      12|        1.63|   1.016/ 44|   1.019/ 37|   1.019/ 36|   1.020/ 35 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  57   |       8|        5.87|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  63   |      47|        4.01|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  65   |    4363|       52.46|   1.012/ 56|   1.008/ 86|   1.007/ 98|   1.006/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  82   |   99398|      301.62|   1.017/ 42|   1.011/ 62|   1.010/ 70|   1.009/ 80 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  69   |     582|       13.89|   1.039/ 17|   1.037/ 19|   1.036/ 19|   1.036/ 19 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  62   |     261|       26.40|   1.031/ 22|   1.015/ 48|   1.010/ 67|   1.006/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  71   |   37876|      570.11|   1.012/ 56|   1.008/ 86|   1.007/ **|   1.006/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  53   |      20|        5.78|   1.010/ 66|   1.009/ 79|   1.008/ 83|   1.008/ 87 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  55   |      13|        0.37|   1.024/ 29|   1.030/ 23|   1.032/ 22|   1.034/ 20 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  55   |      10|        0.31|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  49   |       8|        0.47|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  59   |       4|        0.26|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |

