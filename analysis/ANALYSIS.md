# State and Country COVID-19 Analysis #
## Updated: 2020-05-16 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  63   |   28503|     1465.20|   1.011/ 64|   1.007/ 95|   1.006/ **|   1.006/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  67   |   10713|     1206.14|   1.024/ 29|   1.016/ 42|   1.015/ 47|   1.013/ 54 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  57   |    5840|      840.37|   1.031/ 22|   1.022/ 31|   1.020/ 35|   1.018/ 39 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  58   |    5007|      501.34|   1.017/ 41|   1.011/ 66|   1.009/ 77|   1.007/ 92 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  58   |    4678|      365.40|   1.041/ 17|   1.032/ 21|   1.030/ 23|   1.028/ 25 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  60   |    4144|      327.06|   1.038/ 18|   1.034/ 20|   1.033/ 21|   1.033/ 21 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  58   |    3399|      953.23|   1.025/ 28|   1.018/ 38|   1.016/ 42|   1.015/ 47 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  73   |    3292|       83.31|   1.029/ 24|   1.022/ 31|   1.020/ 34|   1.019/ 37 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  63   |    2522|      542.46|   1.017/ 41|   1.012/ 58|   1.011/ 64|   1.010/ 71 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  69   |    2011|       93.64|   1.028/ 25|   1.023/ 31|   1.021/ 33|   1.020/ 35 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  77   |   93308|      283.14|   1.021/ 33|   1.013/ 52|   1.011/ 60|   1.010/ 71 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  66   |   36723|      552.76|   1.018/ 39|   1.011/ 61|   1.010/ 71|   1.008/ 85 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  85   |   32678|      542.48|   1.008/ 91|   1.005/ **|   1.004/ **|   1.004/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  91   |   29468|      439.32|   1.005/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  74   |   28177|      598.23|   1.008/ 90|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  60   |   15371|       72.71|   1.065/ 11|   1.060/ 11|   1.058/ 12|   1.057/ 12 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  66   |    9287|      805.84|   1.011/ 62|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  68   |    8300|       99.82|   1.013/ 55|   1.007/ 96|   1.006/ **|   1.005/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  86   |    7095|       85.09|   1.009/ 78|   1.007/ 99|   1.007/ **|   1.006/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  68   |    6227|      163.88|   1.036/ 19|   1.026/ 27|   1.023/ 30|   1.021/ 33 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  52   |     489|       99.82|   1.042/ 16|   1.041/ 17|   1.041/ 17|   1.040/ 17 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  52   |      10|       13.99|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  56   |     661|       90.87|   1.049/ 14|   1.049/ 14|   1.049/ 14|   1.049/ 14 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  53   |     107|       35.35|   1.029/ 24|   1.017/ 41|   1.014/ 50|   1.011/ 65 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  73   |    3292|       83.31|   1.029/ 24|   1.022/ 31|   1.020/ 34|   1.019/ 37 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  63   |    1144|      198.73|   1.025/ 28|   1.019/ 37|   1.017/ 40|   1.016/ 43 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  58   |    3399|      953.23|   1.025/ 28|   1.018/ 38|   1.016/ 42|   1.015/ 47 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  51   |     271|      278.69|   1.040/ 17|   1.033/ 21|   1.032/ 22|   1.030/ 23 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  69   |    2011|       93.64|   1.028/ 25|   1.023/ 31|   1.021/ 33|   1.020/ 35 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  65   |    1641|      154.53|   1.024/ 29|   1.018/ 37|   1.017/ 40|   1.016/ 43 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  46   |      17|       12.18|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  51   |      72|       40.33|   1.011/ 63|   1.009/ 81|   1.008/ 86|   1.008/ 92 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  60   |    4144|      327.06|   1.038/ 18|   1.034/ 20|   1.033/ 21|   1.033/ 21 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  61   |    1809|      268.68|   1.034/ 20|   1.026/ 27|   1.024/ 29|   1.021/ 32 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  52   |     341|      108.18|   1.053/ 13|   1.048/ 14|   1.046/ 15|   1.045/ 15 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  64   |     199|       68.32|   1.023/ 30|   1.020/ 35|   1.019/ 36|   1.018/ 38 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  61   |     346|       77.39|   1.022/ 31|   1.017/ 41|   1.015/ 45|   1.014/ 49 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  63   |    2522|      542.46|   1.017/ 41|   1.012/ 58|   1.011/ 64|   1.010/ 71 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  50   |      70|       51.91|   1.017/ 42|   1.013/ 51|   1.013/ 54|   1.012/ 58 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  58   |    2002|      331.14|   1.037/ 19|   1.029/ 23|   1.027/ 25|   1.026/ 27 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  57   |    5840|      840.37|   1.031/ 22|   1.022/ 31|   1.020/ 35|   1.018/ 39 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  58   |    5007|      501.34|   1.017/ 41|   1.011/ 66|   1.009/ 77|   1.007/ 92 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  56   |     732|      129.85|   1.047/ 14|   1.037/ 19|   1.034/ 20|   1.031/ 22 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  58   |     522|      175.31|   1.040/ 17|   1.035/ 20|   1.034/ 20|   1.032/ 21 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  58   |     596|       97.11|   1.035/ 20|   1.032/ 22|   1.031/ 22|   1.030/ 23 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  50   |      16|       15.14|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  49   |     111|       57.39|   1.036/ 19|   1.030/ 23|   1.028/ 24|   1.027/ 26 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  61   |     354|      114.83|   1.024/ 28|   1.020/ 35|   1.019/ 37|   1.018/ 39 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  54   |     166|      122.22|   1.053/ 13|   1.047/ 14|   1.046/ 15|   1.044/ 16 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  67   |   10713|     1206.14|   1.024/ 29|   1.016/ 42|   1.015/ 47|   1.013/ 54 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  52   |     256|      122.17|   1.050/ 14|   1.045/ 15|   1.044/ 16|   1.043/ 16 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  63   |   28503|     1465.20|   1.011/ 64|   1.007/ 95|   1.006/ **|   1.006/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  52   |     673|       64.12|   1.036/ 19|   1.033/ 21|   1.032/ 22|   1.031/ 22 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  50   |      44|       57.73|   1.048/ 14|   1.041/ 17|   1.039/ 18|   1.037/ 19 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  57   |    1634|      139.80|   1.036/ 19|   1.029/ 23|   1.028/ 25|   1.026/ 26 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  58   |     298|       75.21|   1.017/ 41|   1.011/ 64|   1.009/ 75|   1.008/ 89 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  62   |     142|       33.62|   1.021/ 34|   1.017/ 40|   1.017/ 42|   1.016/ 44 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  58   |    4678|      365.40|   1.041/ 17|   1.032/ 21|   1.030/ 23|   1.028/ 25 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  56   |     122|       38.07|   1.019/ 36|   1.017/ 42|   1.016/ 43|   1.015/ 45 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  49   |     506|      477.36|   1.038/ 18|   1.029/ 24|   1.026/ 26|   1.024/ 29 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  61   |     411|       79.91|   1.032/ 22|   1.022/ 31|   1.020/ 35|   1.017/ 40 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  66   |      49|       55.49|   1.049/ 14|   1.048/ 14|   1.048/ 14|   1.048/ 14 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  56   |     286|       41.88|   1.026/ 26|   1.028/ 25|   1.028/ 24|   1.029/ 24 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  60   |    1289|       44.44|   1.032/ 21|   1.029/ 23|   1.029/ 24|   1.028/ 25 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  55   |      79|       24.80|   1.036/ 19|   1.034/ 20|   1.034/ 20|   1.033/ 21 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  57   |      55|       87.73|   1.005/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  63   |    1040|      121.86|   1.038/ 18|   1.030/ 23|   1.028/ 24|   1.026/ 26 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  77   |    1017|      133.61|   1.014/ 49|   1.012/ 60|   1.011/ 63|   1.010/ 67 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  47   |      62|       34.63|   1.028/ 25|   1.023/ 30|   1.022/ 32|   1.021/ 33 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  57   |     450|       77.31|   1.023/ 30|   1.021/ 34|   1.020/ 35|   1.019/ 36 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  33   |       7|       12.09|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  55   |     155|        4.82|   1.053/ 13|   1.044/ 16|   1.041/ 17|   1.039/ 18 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  66   |      32|       11.26|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  65   |     534|       12.42|   1.012/ 57|   1.012/ 59|   1.012/ 59|   1.012/ 59 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  48   |       2|        0.06|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  69   |     367|        8.17|   1.032/ 21|   1.028/ 24|   1.027/ 25|   1.026/ 26 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  51   |      52|       17.67|   1.030/ 23|   1.026/ 26|   1.025/ 27|   1.024/ 28 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  76   |     106|        4.12|   1.006/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  65   |     645|       72.50|   1.005/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  64   |      36|        3.55|   1.030/ 23|   1.032/ 22|   1.032/ 21|   1.033/ 21 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  61   |       9|        5.81|   1.024/ 29|   1.036/ 19|   1.039/ 18|   1.042/ 16 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  59   |     279|        1.65|   1.043/ 16|   1.047/ 15|   1.049/ 14|   1.050/ 14 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  46   |     158|       16.80|   1.040/ 17|   1.036/ 19|   1.036/ 19|   1.035/ 20 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  66   |    9287|      805.84|   1.011/ 62|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  40   |       2|        0.17|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  48   |     162|       14.13|   1.067/ 10|   1.067/ 10|   1.067/ 10|   1.067/ 10 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  56   |     130|       39.26|   1.043/ 16|   1.045/ 15|   1.045/ 15|   1.045/ 15 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  46   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  60   |   15371|       72.71|   1.065/ 11|   1.060/ 11|   1.058/ 12|   1.057/ 12 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  66   |     107|       15.33|   1.028/ 24|   1.024/ 29|   1.022/ 31|   1.021/ 33 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  59   |      52|        2.50|   1.011/ 64|   1.009/ 74|   1.009/ 77|   1.009/ 80 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  33   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  52   |     151|        5.68|   1.032/ 22|   1.037/ 19|   1.038/ 18|   1.040/ 17 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  68   |    6227|      163.88|   1.036/ 19|   1.026/ 27|   1.023/ 30|   1.021/ 33 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  18   |      49|        3.04|   1.148/  5|   1.093/  7|   1.099/  7|   1.103/  7 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  55   |     379|       19.85|   1.036/ 19|   1.034/ 20|   1.034/ 20|   1.034/ 20 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  66   |    4637|        3.31|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  55   |     563|       11.41|   1.041/ 17|   1.037/ 19|   1.036/ 19|   1.034/ 20 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  58   |       7|        1.48|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  58   |     102|       24.92|   1.022/ 32|   1.012/ 60|   1.009/ 77|   1.006/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  59   |      84|        7.52|   1.018/ 39|   1.008/ 89|   1.005/ **|   1.003/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  63   |     562|       96.50|   1.011/ 65|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  60   |     436|       42.04|   1.022/ 32|   1.019/ 36|   1.019/ 37|   1.018/ 38 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  63   |    2828|      161.89|   1.058/ 12|   1.052/ 13|   1.050/ 14|   1.048/ 14 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  69   |     617|        6.15|   1.028/ 24|   1.023/ 30|   1.021/ 32|   1.020/ 35 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  46   |      24|        3.69|   1.061/ 11|   1.061/ 11|   1.061/ 11|   1.061/ 11 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  24   |       7|        5.24|   1.110/  6|   1.178/  4|   1.192/  3|   1.207/  3 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  41   |       5|        0.06|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  56   |     299|       54.10|   1.021/ 32|   1.017/ 41|   1.016/ 44|   1.015/ 47 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  91   |   29468|      439.32|   1.005/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  57   |      11|        5.12|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  54   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  42   |      12|        3.29|   1.033/ 21|   1.029/ 23|   1.029/ 24|   1.028/ 25 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  68   |    8300|       99.82|   1.013/ 55|   1.007/ 96|   1.006/ **|   1.005/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  56   |      26|        0.86|   1.036/ 19|   1.038/ 18|   1.038/ 18|   1.039/ 18 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  66   |     160|       14.91|   1.008/ 84|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  61   |      32|        1.90|   1.044/ 16|   1.037/ 19|   1.035/ 19|   1.034/ 20 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  31   |      14|        1.19|   1.047/ 15|   1.063/ 11|   1.070/ 10|   1.078/  9 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  20   |       3|        1.94|   1.145/  5|   1.043/ 16|   1.010/ 71|   1.000/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  41   |      21|        1.78|   1.074/  9|   1.068/ 10|   1.067/ 10|   1.066/ 10 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  51   |     138|       15.11|   1.043/ 16|   1.039/ 18|   1.038/ 18|   1.036/ 19 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  62   |     467|       47.77|   1.023/ 30|   1.016/ 43|   1.014/ 48|   1.013/ 54 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  66   |    2969|        2.18|   1.059/ 12|   1.054/ 13|   1.052/ 13|   1.051/ 14 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  66   |    1085|        4.06|   1.020/ 35|   1.017/ 41|   1.016/ 43|   1.016/ 44 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  86   |    7095|       85.09|   1.009/ 78|   1.007/ 99|   1.007/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  73   |     116|        2.98|   1.016/ 43|   1.017/ 40|   1.018/ 39|   1.018/ 39 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  66   |    1657|      336.63|   1.014/ 48|   1.005/ **|   1.003/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  56   |     271|       29.49|   1.014/ 51|   1.011/ 61|   1.011/ 64|   1.010/ 67 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  85   |   32678|      542.48|   1.008/ 91|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  58   |      10|        3.53|   1.009/ 77|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  93   |     847|        6.73|   1.033/ 21|   1.025/ 28|   1.022/ 31|   1.020/ 34 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  50   |       9|        0.87|   1.006/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  52   |      34|        1.82|   1.016/ 42|   1.014/ 51|   1.013/ 54|   1.012/ 58 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  51   |      44|        0.93|   1.060/ 11|   1.066/ 10|   1.068/ 10|   1.069/ 10 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  51   |      33|       18.16|   1.010/ 69|   1.013/ 53|   1.014/ 50|   1.014/ 48 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  42   |      92|       20.91|   1.090/  8|   1.102/  7|   1.106/  6|   1.109/  6 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  43   |      13|        2.06|   1.027/ 26|   1.013/ 51|   1.010/ 72|   1.006/ ** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  43   |      19|       10.14|   1.017/ 41|   1.011/ 65|   1.009/ 75|   1.008/ 88 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  67   |      27|        3.91|   1.005/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  42   |      21|        4.62|   1.013/ 51|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  44   |       3|        0.45|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  56   |      54|       19.25|   1.015/ 46|   1.016/ 43|   1.016/ 42|   1.017/ 41 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  60   |     113|        3.44|   1.007/ **|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  48   |      46|        2.30|   1.043/ 16|   1.048/ 14|   1.049/ 14|   1.050/ 14 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  47   |       1|        0.25|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  58   |    4855|       38.36|   1.067/ 10|   1.064/ 11|   1.064/ 11|   1.063/ 11 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  59   |     203|       75.61|   1.039/ 18|   1.036/ 19|   1.036/ 19|   1.035/ 20 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  67   |     196|        5.47|   1.007/ 96|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  71   |    5882|      336.96|   1.010/ 66|   1.006/ **|   1.005/ **|   1.004/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  48   |      21|        4.30|   1.005/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  50   |       8|        1.25|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  52   |      53|        2.35|   1.031/ 22|   1.027/ 26|   1.026/ 27|   1.025/ 28 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  54   |     199|        0.97|   1.072/  9|   1.054/ 13|   1.049/ 14|   1.044/ 16 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  55   |     100|       48.25|   1.017/ 42|   1.008/ 89|   1.006/ **|   1.004/ ** |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  63   |     232|       43.22|   1.008/ 92|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  46   |      20|        4.21|   1.037/ 19|   1.034/ 20|   1.033/ 21|   1.031/ 22 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  58   |     877|        4.00|   1.053/ 13|   1.044/ 16|   1.042/ 16|   1.040/ 17 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  66   |     276|       65.46|   1.025/ 28|   1.020/ 34|   1.019/ 36|   1.018/ 38 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  56   |      11|        1.50|   1.011/ 61|   1.013/ 52|   1.014/ 49|   1.015/ 47 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  57   |    2529|       78.71|   1.058/ 12|   1.047/ 15|   1.044/ 15|   1.042/ 16 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 104   |     899|        8.28|   1.022/ 31|   1.018/ 38|   1.017/ 40|   1.016/ 42 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  65   |     934|       24.33|   1.025/ 28|   1.018/ 37|   1.017/ 41|   1.015/ 45 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  60   |    1227|      119.38|   1.013/ 54|   1.008/ 85|   1.007/ 98|   1.006/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  49   |      15|        5.29|   1.018/ 39|   1.015/ 47|   1.014/ 49|   1.013/ 53 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  55   |    1102|       56.81|   1.027/ 25|   1.023/ 30|   1.022/ 31|   1.021/ 33 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  58   |    2588|       17.64|   1.058/ 12|   1.046/ 15|   1.043/ 16|   1.040/ 17 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  53   |     298|        8.69|   1.039/ 17|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  45   |      25|        1.52|   1.075/  9|   1.090/  8|   1.093/  7|   1.096/  7 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  57   |     245|       35.15|   1.014/ 51|   1.014/ 49|   1.014/ 49|   1.014/ 50 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  23   |      27|        3.46|   1.110/  6|   1.093/  7|   1.103/  7|   1.115/  6 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  56   |      23|        4.02|   1.021/ 33|   1.010/ 69|   1.007/ 97|   1.004/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  49   |      28|        5.13|   1.013/ 52|   1.004/ **|   1.002/ **|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  63   |     107|       51.25|   1.009/ 78|   1.005/ **|   1.003/ **|   1.002/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  38   |      58|        3.65|   1.049/ 14|   1.025/ 28|   1.018/ 39|   1.010/ 68 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  50   |     252|        4.28|   1.056/ 12|   1.053/ 13|   1.052/ 13|   1.051/ 14 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  74   |   28177|      598.23|   1.008/ 90|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  49   |      10|        0.44|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  64   |     104|        2.44|   1.085/  8|   1.079/  9|   1.078/  9|   1.076/  9 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  66   |    3718|      359.67|   1.024/ 28|   1.020/ 35|   1.019/ 37|   1.017/ 39 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  72   |    1945|      226.11|   1.006/ **|   1.002/ **|   1.001/ **|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  48   |       3|        0.17|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  46   |      23|        0.41|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  76   |      58|        0.87|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  50   |      12|        1.56|   1.015/ 45|   1.017/ 42|   1.017/ 41|   1.017/ 41 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  52   |       8|        5.87|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  58   |      46|        3.95|   1.006/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  60   |    4191|       50.40|   1.017/ 41|   1.011/ 64|   1.009/ 74|   1.008/ 86 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  77   |   93308|      283.14|   1.021/ 33|   1.013/ 52|   1.011/ 60|   1.010/ 71 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  64   |     484|       11.56|   1.042/ 16|   1.039/ 18|   1.038/ 18|   1.037/ 18 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  57   |     247|       24.93|   1.048/ 14|   1.031/ 22|   1.026/ 26|   1.022/ 32 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  66   |   36723|      552.76|   1.018/ 39|   1.011/ 61|   1.010/ 71|   1.008/ 85 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  48   |      20|        5.55|   1.012/ 56|   1.007/ 92|   1.006/ **|   1.005/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  50   |      11|        0.32|   1.016/ 44|   1.014/ 50|   1.013/ 52|   1.013/ 52 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  50   |      10|        0.31|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  44   |       8|        0.45|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  54   |       4|        0.26|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |

