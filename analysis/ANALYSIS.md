# State and Country COVID-19 Analysis #
## Updated: 2020-05-15 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  62   |   28348|     1457.20|   1.011/ 60|   1.008/ 89|   1.007/ **|   1.006/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  66   |   10573|     1190.37|   1.025/ 28|   1.017/ 41|   1.015/ 46|   1.013/ 53 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  56   |    5738|      825.70|   1.033/ 21|   1.022/ 31|   1.020/ 35|   1.018/ 39 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  57   |    4952|      495.80|   1.018/ 38|   1.011/ 62|   1.010/ 72|   1.008/ 87 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  57   |    4538|      354.50|   1.041/ 17|   1.032/ 21|   1.030/ 23|   1.027/ 25 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  59   |    4005|      316.08|   1.038/ 18|   1.033/ 21|   1.032/ 21|   1.031/ 22 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  57   |    3332|      934.46|   1.026/ 27|   1.017/ 40|   1.015/ 46|   1.013/ 53 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  72   |    3229|       81.71|   1.029/ 23|   1.022/ 31|   1.020/ 34|   1.019/ 37 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  62   |    2498|      537.34|   1.017/ 40|   1.012/ 56|   1.011/ 62|   1.010/ 70 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  68   |    1972|       91.83|   1.029/ 24|   1.023/ 30|   1.022/ 32|   1.020/ 34 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  76   |   92323|      280.15|   1.022/ 32|   1.014/ 51|   1.012/ 60|   1.010/ 71 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  65   |   36300|      546.40|   1.019/ 36|   1.012/ 57|   1.010/ 66|   1.009/ 79 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  84   |   32551|      540.38|   1.008/ 88|   1.005/ **|   1.004/ **|   1.004/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  90   |   29514|      440.00|   1.006/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  73   |   28010|      594.68|   1.008/ 86|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  59   |   14485|       68.52|   1.066/ 10|   1.060/ 11|   1.058/ 12|   1.057/ 12 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  65   |    9217|      799.80|   1.012/ 59|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  67   |    8237|       99.07|   1.014/ 51|   1.008/ 90|   1.006/ **|   1.005/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  85   |    7038|       84.41|   1.009/ 76|   1.007/ 98|   1.007/ **|   1.006/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  70   |    5859|      335.64|   1.011/ 62|   1.007/ **|   1.005/ **|   1.004/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  51   |     471|       96.14|   1.043/ 16|   1.042/ 16|   1.042/ 16|   1.042/ 16 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  51   |      10|       13.96|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  55   |     632|       86.83|   1.049/ 14|   1.049/ 14|   1.049/ 14|   1.049/ 14 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  52   |     106|       35.11|   1.032/ 21|   1.020/ 34|   1.017/ 40|   1.014/ 50 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  72   |    3229|       81.71|   1.029/ 23|   1.022/ 31|   1.020/ 34|   1.019/ 37 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  62   |    1122|      194.87|   1.023/ 29|   1.015/ 45|   1.014/ 51|   1.012/ 58 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  57   |    3332|      934.46|   1.026/ 27|   1.017/ 40|   1.015/ 46|   1.013/ 53 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  50   |     263|      269.83|   1.040/ 17|   1.031/ 22|   1.029/ 23|   1.027/ 25 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  68   |    1972|       91.83|   1.029/ 24|   1.023/ 30|   1.022/ 32|   1.020/ 34 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  64   |    1614|      152.01|   1.025/ 28|   1.019/ 36|   1.018/ 39|   1.016/ 42 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  45   |      17|       12.19|   1.005/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  50   |      71|       39.98|   1.011/ 63|   1.008/ 89|   1.007/ 99|   1.006/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  59   |    4005|      316.08|   1.038/ 18|   1.033/ 21|   1.032/ 21|   1.031/ 22 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  60   |    1773|      263.40|   1.036/ 19|   1.028/ 25|   1.026/ 27|   1.023/ 30 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  51   |     325|      103.16|   1.053/ 13|   1.047/ 14|   1.046/ 15|   1.045/ 15 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  63   |     195|       67.04|   1.024/ 29|   1.020/ 34|   1.020/ 35|   1.019/ 37 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  60   |     341|       76.39|   1.024/ 29|   1.019/ 37|   1.017/ 40|   1.016/ 43 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  62   |    2498|      537.34|   1.017/ 40|   1.012/ 56|   1.011/ 62|   1.010/ 70 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  49   |      69|       51.21|   1.017/ 41|   1.012/ 56|   1.011/ 62|   1.010/ 69 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  57   |    1945|      321.71|   1.038/ 18|   1.030/ 23|   1.028/ 25|   1.026/ 27 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  56   |    5738|      825.70|   1.033/ 21|   1.022/ 31|   1.020/ 35|   1.018/ 39 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  57   |    4952|      495.80|   1.018/ 38|   1.011/ 62|   1.010/ 72|   1.008/ 87 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  55   |     706|      125.23|   1.049/ 14|   1.037/ 19|   1.034/ 20|   1.031/ 22 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  57   |     506|      169.91|   1.041/ 17|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  57   |     578|       94.17|   1.036/ 19|   1.032/ 22|   1.031/ 22|   1.030/ 23 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  49   |      16|       15.16|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  48   |     107|       55.46|   1.036/ 19|   1.028/ 25|   1.026/ 27|   1.024/ 29 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  60   |     348|      112.87|   1.025/ 27|   1.020/ 34|   1.019/ 36|   1.018/ 39 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  53   |     161|      118.07|   1.057/ 12|   1.054/ 13|   1.053/ 13|   1.052/ 13 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  66   |   10573|     1190.37|   1.025/ 28|   1.017/ 41|   1.015/ 46|   1.013/ 53 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  51   |     245|      116.78|   1.051/ 14|   1.044/ 15|   1.043/ 16|   1.041/ 17 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  62   |   28348|     1457.20|   1.011/ 60|   1.008/ 89|   1.007/ **|   1.006/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  51   |     650|       62.02|   1.037/ 19|   1.032/ 21|   1.031/ 22|   1.030/ 23 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  49   |      42|       55.68|   1.050/ 14|   1.044/ 16|   1.042/ 16|   1.041/ 17 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  56   |    1593|      136.31|   1.037/ 19|   1.030/ 23|   1.028/ 25|   1.026/ 26 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  57   |     295|       74.44|   1.018/ 38|   1.012/ 58|   1.010/ 67|   1.009/ 79 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  61   |     140|       33.11|   1.021/ 33|   1.018/ 39|   1.017/ 41|   1.016/ 43 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  57   |    4538|      354.50|   1.041/ 17|   1.032/ 21|   1.030/ 23|   1.027/ 25 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  55   |     119|       37.28|   1.019/ 36|   1.015/ 45|   1.015/ 48|   1.014/ 51 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  48   |     495|      467.54|   1.040/ 17|   1.031/ 22|   1.029/ 24|   1.026/ 27 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  60   |     405|       78.71|   1.034/ 20|   1.024/ 29|   1.021/ 33|   1.018/ 38 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  65   |      47|       52.63|   1.052/ 13|   1.052/ 13|   1.052/ 13|   1.053/ 13 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  55   |     278|       40.74|   1.026/ 27|   1.027/ 25|   1.027/ 25|   1.028/ 25 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  59   |    1248|       43.05|   1.032/ 21|   1.028/ 24|   1.027/ 25|   1.026/ 26 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  54   |      77|       24.07|   1.038/ 18|   1.037/ 18|   1.037/ 18|   1.037/ 19 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  56   |      55|       88.10|   1.006/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  62   |    1015|      118.91|   1.040/ 17|   1.032/ 22|   1.029/ 23|   1.027/ 25 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  76   |    1007|      132.29|   1.015/ 47|   1.012/ 57|   1.012/ 60|   1.011/ 63 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  46   |      60|       33.64|   1.028/ 25|   1.021/ 33|   1.019/ 36|   1.018/ 38 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  56   |     441|       75.78|   1.024/ 29|   1.021/ 33|   1.020/ 34|   1.019/ 35 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  32   |       7|       12.09|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  54   |     148|        4.60|   1.052/ 13|   1.042/ 16|   1.039/ 18|   1.036/ 19 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  65   |      32|       11.27|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  64   |     528|       12.27|   1.012/ 57|   1.012/ 60|   1.011/ 60|   1.011/ 61 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  47   |       2|        0.06|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  68   |     358|        7.96|   1.032/ 21|   1.027/ 25|   1.026/ 26|   1.025/ 27 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  50   |      51|       17.18|   1.030/ 23|   1.025/ 27|   1.024/ 29|   1.023/ 30 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  75   |     106|        4.12|   1.008/ 89|   1.002/ **|   1.000/ **|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  64   |     646|       72.58|   1.006/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  63   |      35|        3.45|   1.029/ 24|   1.031/ 22|   1.032/ 21|   1.033/ 21 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  60   |       9|        5.69|   1.014/ 49|   1.021/ 33|   1.023/ 30|   1.025/ 27 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  58   |     265|        1.57|   1.040/ 17|   1.044/ 16|   1.045/ 15|   1.046/ 15 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  45   |     153|       16.22|   1.041/ 17|   1.037/ 18|   1.037/ 19|   1.036/ 19 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  65   |    9217|      799.80|   1.012/ 59|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  39   |       2|        0.17|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  47   |     152|       13.22|   1.065/ 11|   1.064/ 11|   1.063/ 11|   1.063/ 11 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  55   |     124|       37.70|   1.044/ 15|   1.048/ 14|   1.048/ 14|   1.049/ 14 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  45   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  59   |   14485|       68.52|   1.066/ 10|   1.060/ 11|   1.058/ 12|   1.057/ 12 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  65   |     104|       14.97|   1.029/ 24|   1.025/ 28|   1.023/ 30|   1.022/ 31 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  58   |      52|        2.48|   1.012/ 58|   1.011/ 61|   1.011/ 62|   1.011/ 63 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  32   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  51   |     145|        5.44|   1.036/ 19|   1.040/ 17|   1.041/ 17|   1.042/ 16 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  67   |    6065|      159.61|   1.038/ 18|   1.027/ 25|   1.025/ 28|   1.022/ 31 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  17   |      46|        2.84|   1.177/  4|   1.088/  8|   1.110/  6|   1.134/  5 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  54   |     364|       19.06|   1.035/ 20|   1.031/ 22|   1.030/ 23|   1.029/ 23 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  65   |    4637|        3.31|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  54   |     545|       11.03|   1.042/ 16|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  57   |       7|        1.41|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  57   |     101|       24.66|   1.023/ 30|   1.013/ 52|   1.011/ 65|   1.008/ 87 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  58   |      84|        7.51|   1.020/ 35|   1.010/ 70|   1.007/ 93|   1.005/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  62   |     560|       96.25|   1.012/ 60|   1.007/ **|   1.006/ **|   1.004/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  59   |     428|       41.33|   1.022/ 31|   1.020/ 35|   1.019/ 36|   1.019/ 37 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  62   |    2692|      154.10|   1.063/ 11|   1.057/ 12|   1.055/ 12|   1.053/ 13 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  68   |     604|        6.03|   1.029/ 24|   1.023/ 30|   1.021/ 32|   1.020/ 35 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  45   |      22|        3.43|   1.060/ 11|   1.059/ 12|   1.058/ 12|   1.058/ 12 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  23   |       7|        4.99|   1.074/  9|   1.142/  5|   1.161/  4|   1.181/  4 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  40   |       5|        0.05|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  55   |     294|       53.21|   1.022/ 31|   1.016/ 42|   1.015/ 46|   1.014/ 50 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  90   |   29514|      440.00|   1.006/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  56   |      11|        4.94|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  53   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  41   |      12|        3.20|   1.035/ 20|   1.030/ 23|   1.029/ 24|   1.028/ 25 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  67   |    8237|       99.07|   1.014/ 51|   1.008/ 90|   1.006/ **|   1.005/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  55   |      25|        0.82|   1.031/ 22|   1.029/ 24|   1.028/ 24|   1.028/ 25 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  65   |     158|       14.76|   1.008/ 90|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  60   |      31|        1.85|   1.045/ 15|   1.038/ 18|   1.036/ 19|   1.035/ 20 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  30   |      14|        1.12|   1.052/ 13|   1.044/ 16|   1.045/ 15|   1.048/ 14 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  19   |       3|        1.93|   1.208/  3|   1.060/ 11|   1.017/ 41|   1.000/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  40   |      20|        1.69|   1.077/  9|   1.076/  9|   1.076/  9|   1.077/  9 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  50   |     134|       14.62|   1.044/ 15|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  61   |     459|       47.01|   1.025/ 28|   1.017/ 40|   1.015/ 45|   1.014/ 50 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  65   |    2828|        2.08|   1.061/ 11|   1.056/ 12|   1.055/ 12|   1.054/ 13 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  65   |    1064|        3.99|   1.019/ 35|   1.016/ 43|   1.015/ 45|   1.014/ 48 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  85   |    7038|       84.41|   1.009/ 76|   1.007/ 98|   1.007/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  72   |     114|        2.93|   1.016/ 43|   1.017/ 40|   1.018/ 39|   1.018/ 38 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  65   |    1646|      334.54|   1.016/ 44|   1.006/ **|   1.003/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  55   |     268|       29.20|   1.014/ 48|   1.012/ 56|   1.012/ 58|   1.011/ 61 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  84   |   32551|      540.38|   1.008/ 88|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  57   |      10|        3.54|   1.011/ 63|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  92   |     833|        6.61|   1.035/ 20|   1.026/ 27|   1.024/ 29|   1.021/ 32 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  49   |       9|        0.87|   1.007/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  51   |      33|        1.79|   1.016/ 42|   1.013/ 55|   1.011/ 60|   1.010/ 67 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  50   |      41|        0.87|   1.058/ 12|   1.063/ 11|   1.064/ 11|   1.065/ 11 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  50   |      33|       18.42|   1.010/ 68|   1.014/ 51|   1.014/ 48|   1.015/ 46 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  41   |      84|       18.96|   1.090/  8|   1.103/  7|   1.107/  6|   1.111/  6 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  42   |      13|        2.00|   1.027/ 26|   1.008/ 88|   1.002/ **|   1.000/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  42   |      19|       10.09|   1.018/ 39|   1.010/ 71|   1.008/ 89|   1.006/ ** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  66   |      27|        3.91|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  41   |      21|        4.63|   1.018/ 39|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  43   |       3|        0.46|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  55   |      53|       18.98|   1.014/ 50|   1.014/ 51|   1.014/ 51|   1.014/ 51 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  59   |     112|        3.42|   1.007/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  47   |      45|        2.21|   1.042/ 16|   1.047/ 15|   1.048/ 14|   1.049/ 14 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  46   |       1|        0.25|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  57   |    4564|       36.06|   1.067/ 10|   1.064/ 11|   1.063/ 11|   1.062/ 11 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  58   |     196|       72.95|   1.040/ 17|   1.037/ 19|   1.036/ 19|   1.035/ 19 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  66   |     196|        5.46|   1.008/ 88|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  70   |    5859|      335.64|   1.011/ 62|   1.007/ **|   1.005/ **|   1.004/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  47   |      21|        4.31|   1.006/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  49   |       8|        1.18|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  51   |      51|        2.30|   1.031/ 22|   1.027/ 26|   1.026/ 27|   1.024/ 28 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  53   |     190|        0.92|   1.078/  9|   1.063/ 11|   1.059/ 12|   1.055/ 13 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  54   |     100|       48.07|   1.017/ 40|   1.007/ 95|   1.005/ **|   1.002/ ** |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  62   |     231|       42.99|   1.008/ 89|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  45   |      19|        4.03|   1.035/ 19|   1.030/ 23|   1.029/ 24|   1.027/ 26 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  57   |     839|        3.83|   1.055/ 12|   1.046/ 15|   1.044/ 16|   1.042/ 17 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  65   |     271|       64.13|   1.025/ 27|   1.021/ 33|   1.020/ 34|   1.019/ 36 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  55   |      11|        1.48|   1.009/ 78|   1.009/ 78|   1.009/ 77|   1.009/ 76 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  56   |    2428|       75.57|   1.059/ 12|   1.048/ 14|   1.045/ 15|   1.042/ 16 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 103   |     882|        8.13|   1.022/ 31|   1.018/ 39|   1.017/ 41|   1.016/ 44 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  64   |     919|       23.94|   1.025/ 27|   1.018/ 38|   1.016/ 42|   1.015/ 47 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  59   |    1217|      118.39|   1.014/ 51|   1.009/ 79|   1.008/ 91|   1.006/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  48   |      14|        5.24|   1.020/ 34|   1.018/ 37|   1.018/ 38|   1.018/ 39 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  54   |    1082|       55.73|   1.028/ 24|   1.024/ 29|   1.023/ 30|   1.022/ 32 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  57   |    2472|       16.85|   1.060/ 11|   1.048/ 14|   1.045/ 15|   1.042/ 17 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  52   |     287|        8.40|   1.040/ 17|   1.038/ 18|   1.038/ 18|   1.038/ 18 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  44   |      22|        1.38|   1.071/ 10|   1.087/  8|   1.091/  7|   1.094/  7 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  56   |     244|       35.05|   1.014/ 49|   1.015/ 45|   1.015/ 45|   1.015/ 45 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  22   |      25|        3.19|   1.139/  5|   1.080/  8|   1.085/  8|   1.093/  7 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  55   |      23|        3.99|   1.024/ 29|   1.015/ 47|   1.012/ 57|   1.010/ 72 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  48   |      28|        5.15|   1.016/ 44|   1.006/ **|   1.004/ **|   1.002/ ** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  62   |     107|       51.19|   1.010/ 70|   1.006/ **|   1.004/ **|   1.003/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  37   |      57|        3.61|   1.052/ 13|   1.034/ 20|   1.029/ 24|   1.023/ 30 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  49   |     240|        4.08|   1.056/ 12|   1.051/ 13|   1.050/ 14|   1.049/ 14 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  73   |   28010|      594.68|   1.008/ 86|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  48   |      10|        0.44|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  63   |      98|        2.30|   1.088/  8|   1.084/  8|   1.082/  8|   1.081/  8 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  65   |    3635|      351.59|   1.024/ 29|   1.018/ 39|   1.016/ 43|   1.015/ 47 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  71   |    1939|      225.42|   1.006/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  47   |       3|        0.17|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  45   |      23|        0.40|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  75   |      58|        0.87|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  49   |      12|        1.54|   1.018/ 39|   1.021/ 33|   1.022/ 31|   1.023/ 30 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  51   |       8|        5.87|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  57   |      46|        3.95|   1.007/ 94|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  59   |    4140|       49.79|   1.018/ 39|   1.011/ 64|   1.009/ 75|   1.008/ 90 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  76   |   92323|      280.15|   1.022/ 32|   1.014/ 51|   1.012/ 60|   1.010/ 71 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  63   |     465|       11.11|   1.043/ 16|   1.039/ 18|   1.038/ 18|   1.037/ 18 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  56   |     242|       24.52|   1.054/ 13|   1.037/ 18|   1.033/ 21|   1.029/ 24 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  65   |   36300|      546.40|   1.019/ 36|   1.012/ 57|   1.010/ 66|   1.009/ 79 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  47   |      19|        5.52|   1.014/ 48|   1.009/ 76|   1.008/ 86|   1.007/ 99 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  49   |      11|        0.32|   1.014/ 48|   1.009/ 75|   1.008/ 86|   1.007/ ** |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  49   |      10|        0.31|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  43   |       8|        0.43|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  53   |       4|        0.26|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |

