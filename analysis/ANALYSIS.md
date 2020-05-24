# State and Country COVID-19 Analysis #
## Updated: 2020-05-24 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  71   |   29667|     1525.03|   1.007/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  75   |   11691|     1316.21|   1.015/ 47|   1.009/ 74|   1.008/ 86|   1.007/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  65   |    6610|      951.20|   1.020/ 35|   1.014/ 50|   1.012/ 56|   1.011/ 63 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  66   |    5320|      532.65|   1.011/ 62|   1.008/ 85|   1.007/ 93|   1.007/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  66   |    5389|      420.95|   1.025/ 28|   1.017/ 42|   1.015/ 47|   1.013/ 54 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  68   |    5031|      397.03|   1.028/ 25|   1.023/ 30|   1.022/ 32|   1.021/ 33 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  81   |    3875|       98.07|   1.024/ 29|   1.020/ 34|   1.020/ 35|   1.019/ 37 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  66   |    3808|     1068.03|   1.017/ 40|   1.013/ 52|   1.012/ 56|   1.011/ 62 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  71   |    2743|      590.06|   1.012/ 55|   1.010/ 70|   1.009/ 74|   1.009/ 80 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  66   |    2361|      390.57|   1.025/ 28|   1.019/ 36|   1.018/ 39|   1.016/ 43 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  85   |  102542|      311.16|   1.015/ 46|   1.011/ 65|   1.010/ 72|   1.009/ 81 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  74   |   38587|      580.82|   1.011/ 63|   1.008/ 86|   1.007/ 94|   1.007/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  93   |   33727|      559.89|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  82   |   29020|      616.14|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  99   |   29876|      445.41|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  68   |   22916|      108.40|   1.055/ 12|   1.051/ 13|   1.050/ 14|   1.049/ 14 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  74   |    9553|      828.95|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  76   |    8555|      102.89|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  94   |    7481|       89.72|   1.008/ 89|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  66   |    7417|       58.60|   1.059/ 11|   1.056/ 12|   1.056/ 12|   1.055/ 12 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  60   |     579|      118.04|   1.026/ 26|   1.019/ 36|   1.018/ 39|   1.016/ 43 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  60   |      10|       13.92|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  64   |     853|      117.19|   1.035/ 20|   1.028/ 24|   1.027/ 26|   1.025/ 28 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  61   |     115|       37.97|   1.019/ 36|   1.015/ 47|   1.014/ 50|   1.013/ 52 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  81   |    3875|       98.07|   1.024/ 29|   1.020/ 34|   1.020/ 35|   1.019/ 37 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  71   |    1374|      238.54|   1.023/ 30|   1.021/ 33|   1.021/ 33|   1.020/ 34 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  66   |    3808|     1068.03|   1.017/ 40|   1.013/ 52|   1.012/ 56|   1.011/ 62 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  59   |     342|      351.61|   1.030/ 23|   1.025/ 28|   1.023/ 30|   1.022/ 32 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  77   |    2319|      107.95|   1.021/ 32|   1.018/ 39|   1.017/ 42|   1.016/ 44 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  73   |    1859|      175.05|   1.020/ 35|   1.017/ 40|   1.017/ 42|   1.016/ 43 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  54   |      17|       12.03|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  59   |      79|       44.00|   1.012/ 60|   1.012/ 57|   1.012/ 56|   1.013/ 55 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  68   |    5031|      397.03|   1.028/ 25|   1.023/ 30|   1.022/ 32|   1.021/ 33 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  69   |    2071|      307.68|   1.023/ 31|   1.016/ 43|   1.015/ 47|   1.013/ 53 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  60   |     452|      143.39|   1.042/ 16|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  72   |     218|       74.70|   1.013/ 51|   1.009/ 76|   1.008/ 87|   1.007/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  69   |     397|       88.80|   1.021/ 33|   1.020/ 35|   1.019/ 36|   1.019/ 36 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  71   |    2743|      590.06|   1.012/ 55|   1.010/ 70|   1.009/ 74|   1.009/ 80 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  58   |      76|       56.89|   1.013/ 53|   1.012/ 60|   1.011/ 61|   1.011/ 63 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  66   |    2361|      390.57|   1.025/ 28|   1.019/ 36|   1.018/ 39|   1.016/ 43 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  65   |    6610|      951.20|   1.020/ 35|   1.014/ 50|   1.012/ 56|   1.011/ 63 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  66   |    5320|      532.65|   1.011/ 62|   1.008/ 85|   1.007/ 93|   1.007/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  64   |     905|      160.40|   1.034/ 20|   1.027/ 25|   1.026/ 27|   1.024/ 29 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  66   |     642|      215.68|   1.030/ 23|   1.025/ 28|   1.023/ 29|   1.022/ 31 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  66   |     716|      116.63|   1.026/ 26|   1.022/ 31|   1.021/ 32|   1.020/ 34 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  58   |      16|       14.98|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  57   |     149|       76.78|   1.037/ 19|   1.037/ 19|   1.037/ 19|   1.037/ 18 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  69   |     400|      130.01|   1.019/ 37|   1.016/ 44|   1.015/ 46|   1.014/ 48 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  62   |     220|      161.60|   1.041/ 17|   1.035/ 20|   1.033/ 21|   1.031/ 22 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  75   |   11691|     1316.21|   1.015/ 47|   1.009/ 74|   1.008/ 86|   1.007/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  60   |     324|      154.73|   1.034/ 20|   1.027/ 26|   1.025/ 28|   1.023/ 30 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  71   |   29667|     1525.03|   1.007/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  60   |     800|       76.30|   1.026/ 27|   1.022/ 32|   1.020/ 34|   1.019/ 36 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  58   |      54|       71.25|   1.035/ 20|   1.029/ 24|   1.028/ 25|   1.027/ 26 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  65   |    1970|      168.53|   1.029/ 24|   1.025/ 27|   1.024/ 28|   1.023/ 29 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  66   |     315|       79.61|   1.012/ 60|   1.009/ 80|   1.008/ 87|   1.007/ 95 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  70   |     153|       36.17|   1.013/ 54|   1.009/ 74|   1.009/ 81|   1.008/ 90 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  66   |    5389|      420.95|   1.025/ 28|   1.017/ 42|   1.015/ 47|   1.013/ 54 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  64   |     132|       41.41|   1.012/ 58|   1.008/ 84|   1.007/ 96|   1.006/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  57   |     597|      563.54|   1.028/ 25|   1.023/ 29|   1.023/ 31|   1.022/ 32 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  69   |     450|       87.37|   1.019/ 36|   1.014/ 51|   1.012/ 57|   1.011/ 64 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  74   |      60|       67.84|   1.030/ 23|   1.024/ 28|   1.023/ 30|   1.021/ 32 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  64   |     333|       48.71|   1.019/ 36|   1.017/ 41|   1.016/ 42|   1.016/ 44 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  68   |    1561|       53.83|   1.025/ 28|   1.021/ 32|   1.020/ 34|   1.020/ 35 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  63   |      98|       30.68|   1.031/ 23|   1.028/ 25|   1.027/ 25|   1.027/ 26 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  65   |      55|       87.52|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  71   |    1219|      142.80|   1.026/ 27|   1.019/ 36|   1.018/ 39|   1.016/ 43 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  85   |    1090|      143.13|   1.010/ 70|   1.008/ 90|   1.007/ 96|   1.007/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  55   |      74|       41.47|   1.022/ 31|   1.020/ 35|   1.019/ 36|   1.019/ 37 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  65   |     513|       88.10|   1.019/ 37|   1.016/ 42|   1.016/ 43|   1.015/ 45 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  41   |      12|       21.12|   1.026/ 27|   1.045/ 15|   1.050/ 14|   1.055/ 13 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  63   |     219|        6.81|   1.046/ 15|   1.041/ 17|   1.040/ 17|   1.039/ 17 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  74   |      31|       11.04|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  73   |     589|       13.71|   1.012/ 56|   1.013/ 55|   1.013/ 55|   1.013/ 55 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  56   |       2|        0.06|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  77   |     450|       10.02|   1.029/ 24|   1.027/ 26|   1.026/ 26|   1.026/ 27 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  59   |      74|       25.07|   1.042/ 16|   1.046/ 15|   1.047/ 14|   1.049/ 14 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  84   |     105|        4.09|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  73   |     646|       72.59|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  72   |      47|        4.63|   1.034/ 20|   1.037/ 19|   1.037/ 18|   1.038/ 18 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  69   |      13|        8.29|   1.021/ 33|   1.025/ 28|   1.025/ 27|   1.026/ 27 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  67   |     436|        2.59|   1.053/ 13|   1.058/ 12|   1.059/ 12|   1.061/ 11 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  54   |     199|       21.19|   1.032/ 22|   1.028/ 25|   1.027/ 26|   1.026/ 27 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  74   |    9553|      828.95|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  48   |       2|        0.17|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  56   |     241|       21.02|   1.058/ 12|   1.056/ 12|   1.055/ 12|   1.055/ 12 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  64   |     156|       47.36|   1.026/ 27|   1.018/ 39|   1.016/ 44|   1.013/ 52 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  54   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  68   |   22916|      108.40|   1.055/ 12|   1.051/ 13|   1.050/ 14|   1.049/ 14 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  74   |     128|       18.44|   1.027/ 26|   1.024/ 28|   1.024/ 29|   1.024/ 29 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  67   |      53|        2.56|   1.005/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  41   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  60   |     174|        6.57|   1.025/ 28|   1.025/ 27|   1.025/ 27|   1.025/ 27 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  76   |    7065|      185.92|   1.021/ 32|   1.013/ 51|   1.011/ 60|   1.010/ 73 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  26   |      61|        3.75|   1.051/ 13|   1.024/ 29|   1.018/ 38|   1.012/ 55 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  63   |     610|       31.92|   1.058/ 12|   1.068/ 10|   1.070/ 10|   1.073/  9 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  74   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  63   |     714|       14.46|   1.034/ 20|   1.031/ 23|   1.030/ 23|   1.029/ 24 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  66   |      11|        2.12|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  66   |     103|       25.28|   1.008/ 83|   1.002/ **|   1.000/ **|   1.000/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  67   |      84|        7.50|   1.006/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  71   |     577|       99.03|   1.006/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  68   |     476|       45.93|   1.013/ 51|   1.010/ 72|   1.009/ 80|   1.008/ 90 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  71   |    3566|      204.16|   1.035/ 20|   1.026/ 27|   1.024/ 29|   1.021/ 33 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  77   |     746|        7.44|   1.026/ 27|   1.023/ 29|   1.023/ 30|   1.022/ 31 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  54   |      37|        5.67|   1.052/ 13|   1.044/ 16|   1.042/ 17|   1.039/ 18 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  32   |      11|        7.80|   1.072/ 10|   1.098/  7|   1.108/  6|   1.120/  6 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  49   |       5|        0.05|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  64   |     320|       57.91|   1.011/ 62|   1.006/ **|   1.005/ **|   1.004/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  99   |   29876|      445.41|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  65   |      14|        6.47|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  62   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  50   |      13|        3.42|   1.013/ 52|   1.002/ **|   1.000/ --|   1.000/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  76   |    8555|      102.89|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  64   |      34|        1.11|   1.030/ 23|   1.027/ 26|   1.026/ 27|   1.025/ 28 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  74   |     171|       15.94|   1.009/ 80|   1.008/ 84|   1.008/ 84|   1.008/ 85 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  69   |      50|        3.01|   1.061/ 11|   1.068/ 10|   1.070/ 10|   1.071/ 10 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  39   |      20|        1.66|   1.042/ 17|   1.036/ 19|   1.034/ 20|   1.032/ 22 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  28   |       7|        4.19|   1.086/  8|   1.080/  8|   1.072/  9|   1.061/ 11 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  49   |      27|        2.30|   1.048/ 14|   1.040/ 17|   1.038/ 18|   1.036/ 19 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  59   |     172|       18.74|   1.033/ 21|   1.028/ 25|   1.027/ 26|   1.026/ 27 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  70   |     507|       51.86|   1.014/ 50|   1.009/ 81|   1.007/ 96|   1.006/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  74   |    4159|        3.06|   1.047/ 15|   1.041/ 17|   1.039/ 18|   1.037/ 18 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  74   |    1319|        4.94|   1.025/ 28|   1.027/ 26|   1.027/ 26|   1.027/ 25 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  94   |    7481|       89.72|   1.008/ 89|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  81   |     140|        3.59|   1.025/ 27|   1.029/ 24|   1.030/ 23|   1.030/ 23 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  74   |    1671|      339.59|   1.008/ 86|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  64   |     288|       31.34|   1.008/ 83|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  93   |   33727|      559.89|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  66   |       9|        3.39|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 101   |     952|        7.56|   1.019/ 35|   1.012/ 57|   1.010/ 67|   1.008/ 82 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  58   |       9|        0.85|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  60   |      36|        1.95|   1.010/ 71|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  59   |      59|        1.23|   1.034/ 20|   1.021/ 33|   1.017/ 40|   1.013/ 52 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  59   |      30|       16.87|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  50   |     160|       36.26|   1.072/ 10|   1.058/ 12|   1.053/ 13|   1.049/ 14 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  51   |      15|        2.24|   1.013/ 54|   1.005/ **|   1.003/ **|   1.001/ ** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  51   |      22|       11.44|   1.017/ 40|   1.021/ 34|   1.022/ 32|   1.023/ 31 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  75   |      27|        3.89|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  50   |      24|        5.33|   1.017/ 40|   1.024/ 28|   1.026/ 26|   1.029/ 24 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  52   |       3|        0.44|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  64   |      62|       22.32|   1.017/ 41|   1.018/ 38|   1.018/ 37|   1.019/ 37 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  68   |     116|        3.55|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  56   |      64|        3.16|   1.042/ 16|   1.042/ 16|   1.042/ 16|   1.042/ 16 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  55   |       1|        0.25|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  66   |    7417|       58.60|   1.059/ 11|   1.056/ 12|   1.056/ 12|   1.055/ 12 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  67   |     255|       94.91|   1.030/ 23|   1.026/ 27|   1.025/ 28|   1.024/ 29 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  75   |     201|        5.59|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  79   |    6036|      345.76|   1.005/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  56   |      21|        4.24|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  58   |      17|        2.63|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  60   |      63|        2.80|   1.025/ 27|   1.023/ 30|   1.022/ 31|   1.021/ 32 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  62   |     245|        1.19|   1.042/ 16|   1.028/ 25|   1.024/ 29|   1.021/ 33 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  63   |     113|       54.24|   1.017/ 41|   1.016/ 42|   1.016/ 42|   1.016/ 42 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  71   |     239|       44.58|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  54   |      33|        7.16|   1.064/ 11|   1.076/  9|   1.079/  9|   1.082/  8 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  66   |    1147|        5.23|   1.041/ 17|   1.035/ 20|   1.033/ 21|   1.032/ 21 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  74   |     312|       73.95|   1.018/ 39|   1.014/ 49|   1.013/ 52|   1.012/ 56 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  64   |      11|        1.58|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  65   |    3544|      110.29|   1.047/ 15|   1.041/ 17|   1.039/ 18|   1.038/ 18 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 112   |     977|        9.01|   1.014/ 50|   1.010/ 71|   1.009/ 78|   1.008/ 88 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  73   |    1040|       27.11|   1.016/ 43|   1.012/ 59|   1.011/ 65|   1.009/ 73 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  68   |    1311|      127.59|   1.011/ 65|   1.009/ 75|   1.009/ 78|   1.009/ 81 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  57   |      18|        6.46|   1.031/ 22|   1.040/ 17|   1.042/ 16|   1.045/ 15 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  63   |    1237|       63.72|   1.017/ 41|   1.011/ 61|   1.010/ 69|   1.009/ 80 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  66   |    3527|       24.04|   1.046/ 15|   1.039/ 17|   1.038/ 18|   1.036/ 19 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  61   |     382|       11.18|   1.034/ 20|   1.032/ 22|   1.031/ 22|   1.030/ 23 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  53   |      37|        2.27|   1.060/ 11|   1.050/ 14|   1.047/ 15|   1.044/ 16 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  65   |     248|       35.60|   1.009/ 77|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  31   |      40|        5.01|   1.068/ 10|   1.040/ 17|   1.032/ 21|   1.026/ 27 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  64   |      24|        4.18|   1.011/ 61|   1.006/ **|   1.005/ **|   1.003/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  57   |      29|        5.26|   1.005/ **|   1.002/ **|   1.001/ **|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  71   |     108|       51.77|   1.004/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  46   |      63|        3.99|   1.022/ 31|   1.012/ 59|   1.009/ 73|   1.007/ 96 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  58   |     397|        6.76|   1.062/ 11|   1.067/ 10|   1.068/ 10|   1.069/ 10 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  82   |   29020|      616.14|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  57   |       9|        0.42|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  72   |     152|        3.57|   1.058/ 12|   1.046/ 15|   1.043/ 16|   1.039/ 17 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  74   |    4146|      401.03|   1.017/ 42|   1.013/ 54|   1.012/ 58|   1.011/ 62 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  80   |    1951|      226.80|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  56   |       3|        0.17|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  54   |      22|        0.39|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  84   |      57|        0.86|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  58   |      13|        1.66|   1.011/ 63|   1.010/ 73|   1.009/ 76|   1.009/ 80 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  60   |       8|        5.87|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  66   |      48|        4.07|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  68   |    4449|       53.50|   1.010/ 69|   1.006/ **|   1.006/ **|   1.005/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  85   |  102542|      311.16|   1.015/ 46|   1.011/ 65|   1.010/ 72|   1.009/ 81 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  72   |     638|       15.23|   1.035/ 20|   1.032/ 22|   1.031/ 22|   1.030/ 23 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  65   |     267|       27.01|   1.024/ 29|   1.011/ 66|   1.007/ 97|   1.004/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  74   |   38587|      580.82|   1.011/ 63|   1.008/ 86|   1.007/ 94|   1.007/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  56   |      21|        5.94|   1.010/ 68|   1.010/ 72|   1.010/ 73|   1.009/ 74 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  58   |      13|        0.39|   1.018/ 38|   1.019/ 36|   1.019/ 36|   1.020/ 35 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  58   |      10|        0.31|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  52   |       8|        0.45|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  62   |       4|        0.26|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |

