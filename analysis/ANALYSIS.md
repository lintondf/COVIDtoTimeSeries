# State and Country COVID-19 Analysis #
## Updated: 2020-05-20 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  67   |   29170|     1499.46|   1.009/ 81|   1.006/ **|   1.005/ **|   1.005/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  71   |   11251|     1266.71|   1.018/ 38|   1.012/ 58|   1.010/ 67|   1.009/ 78 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  61   |    6259|      900.62|   1.025/ 28|   1.017/ 40|   1.016/ 44|   1.014/ 50 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  62   |    5156|      516.32|   1.013/ 55|   1.008/ 90|   1.006/ **|   1.005/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  62   |    5054|      394.77|   1.030/ 23|   1.019/ 37|   1.016/ 44|   1.013/ 53 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  64   |    4595|      362.61|   1.031/ 22|   1.026/ 27|   1.024/ 28|   1.023/ 30 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  62   |    3617|     1014.60|   1.021/ 33|   1.016/ 43|   1.015/ 46|   1.014/ 50 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  77   |    3567|       90.28|   1.025/ 28|   1.019/ 36|   1.018/ 38|   1.017/ 41 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  67   |    2636|      566.92|   1.014/ 48|   1.011/ 62|   1.010/ 67|   1.010/ 72 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  62   |    2191|      362.45|   1.030/ 23|   1.023/ 30|   1.021/ 32|   1.020/ 35 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  81   |   97992|      297.36|   1.017/ 41|   1.011/ 62|   1.010/ 71|   1.008/ 83 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  70   |   37763|      568.41|   1.013/ 53|   1.009/ 80|   1.008/ 91|   1.007/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  89   |   33250|      551.97|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  95   |   29744|      443.43|   1.005/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  78   |   28586|      606.92|   1.006/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  64   |   18838|       89.10|   1.058/ 12|   1.052/ 13|   1.050/ 14|   1.049/ 14 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  70   |    9451|      820.07|   1.008/ 85|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  72   |    8430|      101.39|   1.009/ 81|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  90   |    7280|       87.32|   1.008/ 87|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  72   |    6699|      176.31|   1.027/ 25|   1.018/ 38|   1.016/ 44|   1.013/ 52 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  56   |     538|      109.80|   1.031/ 22|   1.024/ 29|   1.022/ 32|   1.020/ 35 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  56   |      10|       14.02|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  60   |     763|      104.81|   1.041/ 17|   1.035/ 20|   1.033/ 21|   1.031/ 22 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  57   |     108|       35.83|   1.018/ 39|   1.006/ **|   1.002/ **|   1.000/ -- |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  77   |    3567|       90.28|   1.025/ 28|   1.019/ 36|   1.018/ 38|   1.017/ 41 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  67   |    1260|      218.85|   1.025/ 27|   1.024/ 29|   1.023/ 30|   1.023/ 30 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  62   |    3617|     1014.60|   1.021/ 33|   1.016/ 43|   1.015/ 46|   1.014/ 50 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  55   |     311|      319.11|   1.037/ 19|   1.033/ 21|   1.032/ 21|   1.031/ 22 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  73   |    2164|      100.74|   1.023/ 30|   1.018/ 39|   1.017/ 42|   1.015/ 45 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  69   |    1740|      163.90|   1.019/ 35|   1.015/ 47|   1.014/ 51|   1.012/ 55 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  50   |      17|       12.08|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  55   |      75|       41.78|   1.010/ 70|   1.008/ 82|   1.008/ 85|   1.008/ 88 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  64   |    4595|      362.61|   1.031/ 22|   1.026/ 27|   1.024/ 28|   1.023/ 30 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  65   |    1943|      288.66|   1.027/ 26|   1.018/ 38|   1.016/ 43|   1.014/ 50 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  56   |     393|      124.63|   1.043/ 16|   1.035/ 20|   1.033/ 21|   1.031/ 23 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  68   |     210|       72.06|   1.018/ 39|   1.013/ 51|   1.012/ 56|   1.011/ 62 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  65   |     366|       81.82|   1.019/ 37|   1.015/ 47|   1.014/ 50|   1.013/ 54 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  67   |    2636|      566.92|   1.014/ 48|   1.011/ 62|   1.010/ 67|   1.010/ 72 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  54   |      73|       54.38|   1.014/ 48|   1.012/ 59|   1.011/ 62|   1.010/ 66 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  62   |    2191|      362.45|   1.030/ 23|   1.023/ 30|   1.021/ 32|   1.020/ 35 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  61   |    6259|      900.62|   1.025/ 28|   1.017/ 40|   1.016/ 44|   1.014/ 50 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  62   |    5156|      516.32|   1.013/ 55|   1.008/ 90|   1.006/ **|   1.005/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  60   |     817|      144.84|   1.038/ 18|   1.028/ 25|   1.026/ 27|   1.023/ 30 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  62   |     582|      195.64|   1.033/ 21|   1.027/ 25|   1.026/ 27|   1.024/ 28 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  62   |     657|      107.06|   1.029/ 23|   1.025/ 28|   1.023/ 29|   1.022/ 31 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  54   |      16|       15.02|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  53   |     128|       66.04|   1.035/ 20|   1.032/ 21|   1.032/ 22|   1.031/ 22 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  65   |     375|      121.87|   1.020/ 35|   1.015/ 46|   1.014/ 50|   1.013/ 54 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  58   |     192|      141.48|   1.045/ 15|   1.035/ 20|   1.032/ 21|   1.030/ 23 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  71   |   11251|     1266.71|   1.018/ 38|   1.012/ 58|   1.010/ 67|   1.009/ 78 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  56   |     293|      139.80|   1.041/ 17|   1.034/ 20|   1.032/ 22|   1.030/ 23 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  67   |   29170|     1499.46|   1.009/ 81|   1.006/ **|   1.005/ **|   1.005/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  56   |     738|       70.33|   1.029/ 24|   1.023/ 30|   1.021/ 32|   1.020/ 35 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  54   |      48|       63.41|   1.036/ 19|   1.025/ 28|   1.022/ 32|   1.019/ 37 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  61   |    1786|      152.83|   1.029/ 23|   1.023/ 30|   1.021/ 33|   1.019/ 36 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  62   |     305|       77.02|   1.012/ 58|   1.006/ **|   1.005/ **|   1.003/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  66   |     147|       34.86|   1.014/ 49|   1.009/ 76|   1.008/ 88|   1.007/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  62   |    5054|      394.77|   1.030/ 23|   1.019/ 37|   1.016/ 44|   1.013/ 53 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  60   |     128|       40.15|   1.016/ 42|   1.014/ 51|   1.013/ 54|   1.012/ 57 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  53   |     546|      515.41|   1.030/ 23|   1.021/ 33|   1.019/ 37|   1.016/ 43 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  65   |     431|       83.76|   1.023/ 30|   1.014/ 48|   1.012/ 56|   1.010/ 67 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  70   |      56|       63.47|   1.035/ 20|   1.029/ 24|   1.028/ 25|   1.026/ 26 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  60   |     312|       45.69|   1.022/ 31|   1.021/ 33|   1.021/ 33|   1.020/ 34 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  64   |    1433|       49.41|   1.029/ 24|   1.026/ 26|   1.025/ 27|   1.025/ 28 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  59   |      88|       27.47|   1.031/ 22|   1.027/ 25|   1.026/ 26|   1.025/ 27 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  61   |      55|       87.60|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  67   |    1131|      132.48|   1.029/ 24|   1.020/ 34|   1.018/ 38|   1.016/ 43 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  81   |    1055|      138.59|   1.011/ 62|   1.009/ 79|   1.008/ 85|   1.007/ 92 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  51   |      69|       38.44|   1.026/ 26|   1.026/ 26|   1.026/ 26|   1.026/ 26 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  61   |     481|       82.56|   1.020/ 35|   1.016/ 43|   1.015/ 45|   1.014/ 48 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  37   |       7|       12.09|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  59   |     187|        5.80|   1.050/ 14|   1.044/ 16|   1.043/ 16|   1.041/ 17 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  70   |      32|       11.14|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  69   |     561|       13.04|   1.012/ 57|   1.012/ 57|   1.012/ 57|   1.012/ 57 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  52   |       2|        0.06|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  73   |     406|        9.03|   1.029/ 24|   1.025/ 27|   1.025/ 28|   1.024/ 29 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  55   |      62|       20.83|   1.038/ 18|   1.042/ 16|   1.043/ 16|   1.044/ 16 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  80   |     105|        4.10|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  69   |     646|       72.51|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  68   |      40|        4.02|   1.031/ 22|   1.034/ 20|   1.034/ 20|   1.035/ 20 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  65   |      11|        7.39|   1.031/ 22|   1.041/ 17|   1.044/ 16|   1.046/ 15 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  63   |     347|        2.06|   1.048/ 14|   1.055/ 12|   1.057/ 12|   1.058/ 12 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  50   |     179|       19.01|   1.036/ 19|   1.032/ 21|   1.031/ 22|   1.031/ 23 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  70   |    9451|      820.07|   1.008/ 85|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  44   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  52   |     196|       17.07|   1.057/ 12|   1.048/ 14|   1.046/ 15|   1.044/ 16 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  60   |     147|       44.38|   1.035/ 20|   1.030/ 23|   1.029/ 24|   1.027/ 25 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  50   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  64   |   18838|       89.10|   1.058/ 12|   1.052/ 13|   1.050/ 14|   1.049/ 14 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  70   |     116|       16.75|   1.026/ 26|   1.023/ 31|   1.022/ 32|   1.021/ 33 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  63   |      53|        2.53|   1.006/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  37   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  56   |     165|        6.21|   1.022/ 31|   1.020/ 34|   1.020/ 35|   1.019/ 36 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  72   |    6699|      176.31|   1.027/ 25|   1.018/ 38|   1.016/ 44|   1.013/ 52 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  22   |      57|        3.51|   1.094/  7|   1.051/ 13|   1.040/ 17|   1.029/ 24 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  59   |     468|       24.50|   1.047/ 14|   1.054/ 13|   1.055/ 12|   1.057/ 12 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  70   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  59   |     635|       12.85|   1.036/ 19|   1.031/ 22|   1.029/ 23|   1.028/ 25 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  62   |      10|        1.88|   1.043/ 16|   1.055/ 13|   1.058/ 12|   1.061/ 11 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  62   |     103|       25.18|   1.012/ 57|   1.002/ **|   1.000/ **|   1.000/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  63   |      84|        7.52|   1.009/ 74|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  67   |     570|       97.87|   1.008/ 88|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  64   |     458|       44.21|   1.017/ 41|   1.013/ 55|   1.012/ 60|   1.011/ 66 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  67   |    3281|      187.84|   1.045/ 15|   1.040/ 17|   1.038/ 18|   1.037/ 19 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  73   |     679|        6.77|   1.027/ 25|   1.024/ 29|   1.023/ 30|   1.022/ 31 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  50   |      31|        4.80|   1.066/ 10|   1.068/ 10|   1.069/ 10|   1.070/ 10 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  28   |       8|        5.80|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  45   |       5|        0.05|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  60   |     312|       56.44|   1.016/ 42|   1.012/ 60|   1.010/ 67|   1.009/ 76 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  95   |   29744|      443.43|   1.005/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  61   |      13|        5.93|   1.040/ 17|   1.032/ 21|   1.032/ 21|   1.029/ 23 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  58   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  46   |      13|        3.43|   1.024/ 29|   1.014/ 48|   1.012/ 59|   1.009/ 77 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  72   |    8430|      101.39|   1.009/ 81|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  60   |      31|        1.01|   1.039/ 18|   1.042/ 16|   1.043/ 16|   1.044/ 16 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  70   |     165|       15.43|   1.009/ 76|   1.008/ 83|   1.008/ 84|   1.008/ 85 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  65   |      38|        2.29|   1.045/ 15|   1.048/ 14|   1.048/ 14|   1.049/ 14 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  35   |      18|        1.45|   1.044/ 16|   1.049/ 14|   1.050/ 14|   1.050/ 14 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  24   |       5|        2.93|   1.070/ 10|   1.094/  7|   1.117/  6|   1.139/  5 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  45   |      23|        2.01|   1.053/ 13|   1.034/ 20|   1.029/ 24|   1.023/ 29 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  55   |     155|       16.97|   1.037/ 19|   1.030/ 23|   1.028/ 24|   1.027/ 26 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  66   |     490|       50.10|   1.018/ 38|   1.013/ 55|   1.011/ 62|   1.010/ 72 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  70   |    3546|        2.60|   1.052/ 13|   1.046/ 15|   1.045/ 15|   1.043/ 16 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  70   |    1188|        4.45|   1.023/ 30|   1.024/ 29|   1.024/ 29|   1.024/ 28 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  90   |    7280|       87.32|   1.008/ 87|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  77   |     126|        3.23|   1.019/ 36|   1.021/ 33|   1.021/ 32|   1.022/ 32 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  70   |    1662|      337.67|   1.010/ 68|   1.004/ **|   1.003/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  60   |     281|       30.61|   1.012/ 59|   1.010/ 70|   1.009/ 73|   1.009/ 77 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  89   |   33250|      551.97|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  62   |       9|        3.46|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  97   |     909|        7.21|   1.026/ 26|   1.018/ 38|   1.016/ 43|   1.014/ 49 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  54   |       9|        0.86|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  56   |      36|        1.91|   1.015/ 45|   1.013/ 55|   1.012/ 58|   1.011/ 61 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  55   |      54|        1.14|   1.056/ 12|   1.057/ 12|   1.057/ 12|   1.057/ 12 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  55   |      31|       17.45|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  46   |     130|       29.49|   1.087/  8|   1.087/  8|   1.087/  8|   1.086/  8 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  47   |      14|        2.20|   1.024/ 29|   1.015/ 46|   1.013/ 52|   1.012/ 58 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  47   |      20|       10.47|   1.012/ 58|   1.009/ 76|   1.009/ 81|   1.008/ 87 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  71   |      27|        3.91|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  46   |      22|        4.82|   1.010/ 66|   1.011/ 64|   1.011/ 61|   1.012/ 57 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  48   |       3|        0.44|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  60   |      58|       20.75|   1.017/ 40|   1.020/ 35|   1.020/ 34|   1.021/ 33 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  64   |     115|        3.50|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  52   |      55|        2.70|   1.042/ 16|   1.042/ 16|   1.042/ 16|   1.042/ 16 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  51   |       1|        0.25|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  62   |    5980|       47.24|   1.059/ 12|   1.054/ 13|   1.052/ 13|   1.051/ 14 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  63   |     230|       85.71|   1.035/ 20|   1.031/ 22|   1.030/ 23|   1.030/ 23 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  71   |     198|        5.53|   1.005/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  75   |    5975|      342.28|   1.007/ 94|   1.004/ **|   1.003/ **|   1.002/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  52   |      21|        4.27|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  54   |       9|        1.45|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  56   |      57|        2.56|   1.027/ 25|   1.023/ 30|   1.022/ 31|   1.021/ 32 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  58   |     224|        1.08|   1.053/ 13|   1.032/ 21|   1.027/ 25|   1.022/ 32 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  59   |     105|       50.54|   1.016/ 44|   1.012/ 56|   1.012/ 59|   1.011/ 62 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  67   |     236|       44.02|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  50   |      25|        5.26|   1.052/ 13|   1.060/ 11|   1.062/ 11|   1.065/ 11 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  62   |    1004|        4.58|   1.044/ 15|   1.036/ 19|   1.033/ 21|   1.031/ 22 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  70   |     295|       69.92|   1.021/ 33|   1.017/ 41|   1.016/ 43|   1.015/ 46 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  60   |      11|        1.55|   1.007/ 93|   1.007/ 98|   1.007/ 98|   1.007/ 99 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  61   |    3019|       93.96|   1.053/ 13|   1.046/ 15|   1.044/ 16|   1.043/ 16 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 108   |     944|        8.70|   1.018/ 38|   1.014/ 48|   1.014/ 51|   1.013/ 55 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  69   |     992|       25.85|   1.020/ 35|   1.015/ 48|   1.013/ 52|   1.012/ 58 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  64   |    1264|      123.03|   1.011/ 64|   1.008/ 87|   1.007/ 95|   1.007/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  53   |      15|        5.62|   1.016/ 42|   1.015/ 47|   1.014/ 49|   1.014/ 51 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  59   |    1182|       60.91|   1.022/ 31|   1.017/ 40|   1.016/ 43|   1.015/ 46 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  62   |    3030|       20.65|   1.050/ 14|   1.040/ 17|   1.038/ 18|   1.036/ 19 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  57   |     339|        9.90|   1.036/ 19|   1.033/ 21|   1.032/ 21|   1.032/ 22 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  49   |      31|        1.89|   1.066/ 10|   1.059/ 12|   1.057/ 12|   1.054/ 13 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  61   |     247|       35.50|   1.012/ 58|   1.010/ 69|   1.009/ 73|   1.009/ 78 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  27   |      35|        4.46|   1.078/  9|   1.071/ 10|   1.066/ 10|   1.061/ 11 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  60   |      23|        4.11|   1.015/ 47|   1.006/ **|   1.004/ **|   1.001/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  53   |      29|        5.23|   1.010/ 70|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  67   |     108|       51.48|   1.006/ **|   1.002/ **|   1.001/ **|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  42   |      61|        3.81|   1.033/ 21|   1.015/ 46|   1.011/ 65|   1.006/ ** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  54   |     307|        5.22|   1.054/ 13|   1.050/ 14|   1.050/ 14|   1.049/ 14 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  78   |   28586|      606.92|   1.006/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  53   |       9|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  68   |     126|        2.96|   1.066/ 10|   1.053/ 13|   1.050/ 14|   1.046/ 15 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  70   |    3943|      381.41|   1.019/ 37|   1.014/ 49|   1.013/ 53|   1.012/ 58 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  76   |    1950|      226.59|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  52   |       3|        0.17|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  50   |      23|        0.40|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  80   |      58|        0.87|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  54   |      12|        1.61|   1.014/ 48|   1.016/ 43|   1.016/ 43|   1.016/ 42 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  56   |       8|        5.87|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  62   |      47|        3.99|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  64   |    4339|       52.18|   1.013/ 52|   1.009/ 77|   1.008/ 87|   1.007/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  81   |   97992|      297.36|   1.017/ 41|   1.011/ 62|   1.010/ 71|   1.008/ 83 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  68   |     563|       13.44|   1.040/ 17|   1.038/ 18|   1.038/ 18|   1.037/ 19 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  61   |     257|       26.02|   1.034/ 21|   1.017/ 42|   1.012/ 57|   1.008/ 89 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  70   |   37763|      568.41|   1.013/ 53|   1.009/ 80|   1.008/ 91|   1.007/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  52   |      20|        5.74|   1.012/ 60|   1.011/ 65|   1.011/ 66|   1.010/ 67 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  54   |      12|        0.36|   1.023/ 30|   1.030/ 23|   1.032/ 22|   1.034/ 20 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  54   |      10|        0.31|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  48   |       8|        0.47|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  58   |       4|        0.26|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |

