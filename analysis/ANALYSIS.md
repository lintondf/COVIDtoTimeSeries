# State and Country COVID-19 Analysis #
## Updated: 2020-05-14 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  61   |   28113|     1445.12|   1.012/ 57|   1.008/ 86|   1.007/ 98|   1.006/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  65   |   10377|     1168.28|   1.026/ 27|   1.017/ 40|   1.015/ 46|   1.013/ 54 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  55   |    5598|      805.55|   1.035/ 20|   1.023/ 30|   1.020/ 34|   1.017/ 39 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  56   |    4913|      491.98|   1.019/ 36|   1.012/ 59|   1.010/ 70|   1.008/ 86 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  56   |    4412|      344.62|   1.042/ 16|   1.033/ 21|   1.030/ 23|   1.027/ 25 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  58   |    3880|      306.19|   1.038/ 18|   1.032/ 21|   1.031/ 22|   1.030/ 23 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  56   |    3283|      920.82|   1.027/ 26|   1.017/ 40|   1.015/ 46|   1.013/ 54 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  71   |    3147|       79.65|   1.030/ 23|   1.021/ 32|   1.019/ 36|   1.017/ 40 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  61   |    2465|      530.23|   1.018/ 38|   1.012/ 56|   1.011/ 62|   1.010/ 71 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  67   |    1926|       89.69|   1.029/ 23|   1.023/ 30|   1.022/ 32|   1.020/ 35 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  75   |   90709|      275.25|   1.022/ 31|   1.013/ 53|   1.011/ 64|   1.009/ 79 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  64   |   36015|      542.11|   1.020/ 34|   1.013/ 54|   1.011/ 63|   1.009/ 76 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  83   |   32346|      536.97|   1.008/ 84|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  72   |   27895|      592.24|   1.008/ 82|   1.006/ **|   1.005/ **|   1.004/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  89   |   29345|      437.49|   1.006/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  58   |   13714|       64.87|   1.067/ 10|   1.060/ 11|   1.059/ 12|   1.057/ 12 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  64   |    9177|      796.27|   1.013/ 54|   1.008/ 92|   1.006/ **|   1.005/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  66   |    8201|       98.62|   1.014/ 48|   1.008/ 83|   1.007/ **|   1.005/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  84   |    6995|       83.90|   1.009/ 74|   1.007/ 95|   1.007/ **|   1.006/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  69   |    5816|      333.16|   1.012/ 59|   1.007/ **|   1.006/ **|   1.004/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  50   |     452|       92.20|   1.041/ 17|   1.040/ 17|   1.039/ 18|   1.039/ 18 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  50   |      10|       13.89|   1.003/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  54   |     602|       82.74|   1.049/ 14|   1.049/ 14|   1.049/ 14|   1.049/ 14 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  51   |     104|       34.54|   1.035/ 20|   1.024/ 28|   1.022/ 32|   1.019/ 37 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  71   |    3147|       79.65|   1.030/ 23|   1.021/ 32|   1.019/ 36|   1.017/ 40 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  61   |    1099|      190.91|   1.023/ 29|   1.013/ 52|   1.011/ 64|   1.008/ 82 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  56   |    3283|      920.82|   1.027/ 26|   1.017/ 40|   1.015/ 46|   1.013/ 54 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  49   |     254|      260.36|   1.040/ 17|   1.029/ 24|   1.026/ 27|   1.023/ 30 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  67   |    1926|       89.69|   1.029/ 23|   1.023/ 30|   1.022/ 32|   1.020/ 35 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  63   |    1584|      149.17|   1.025/ 27|   1.019/ 36|   1.018/ 39|   1.016/ 43 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  44   |      17|       12.25|   1.007/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  49   |      71|       39.47|   1.012/ 60|   1.008/ 90|   1.007/ **|   1.006/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  58   |    3880|      306.19|   1.038/ 18|   1.032/ 21|   1.031/ 22|   1.030/ 23 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  59   |    1730|      257.03|   1.038/ 18|   1.030/ 23|   1.028/ 24|   1.026/ 26 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  50   |     312|       98.84|   1.054/ 13|   1.047/ 15|   1.045/ 15|   1.043/ 16 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  62   |     192|       65.92|   1.025/ 28|   1.022/ 32|   1.021/ 33|   1.020/ 34 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  59   |     335|       75.05|   1.025/ 28|   1.019/ 36|   1.018/ 39|   1.016/ 42 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  61   |    2465|      530.23|   1.018/ 38|   1.012/ 56|   1.011/ 62|   1.010/ 71 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  48   |      68|       50.44|   1.017/ 41|   1.011/ 61|   1.010/ 69|   1.009/ 81 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  56   |    1897|      313.73|   1.040/ 17|   1.030/ 23|   1.028/ 25|   1.026/ 27 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  55   |    5598|      805.55|   1.035/ 20|   1.023/ 30|   1.020/ 34|   1.017/ 39 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  56   |    4913|      491.98|   1.019/ 36|   1.012/ 59|   1.010/ 70|   1.008/ 86 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  54   |     685|      121.38|   1.051/ 13|   1.037/ 18|   1.034/ 20|   1.031/ 22 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  56   |     489|      164.31|   1.043/ 16|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  56   |     561|       91.46|   1.037/ 19|   1.032/ 21|   1.031/ 22|   1.030/ 23 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  48   |      16|       15.23|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  47   |     105|       54.20|   1.039/ 18|   1.031/ 22|   1.029/ 24|   1.028/ 25 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  59   |     341|      110.80|   1.026/ 27|   1.021/ 33|   1.019/ 36|   1.018/ 38 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  52   |     154|      112.99|   1.059/ 12|   1.057/ 12|   1.057/ 12|   1.056/ 12 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  65   |   10377|     1168.28|   1.026/ 27|   1.017/ 40|   1.015/ 46|   1.013/ 54 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  50   |     235|      111.99|   1.051/ 13|   1.044/ 16|   1.042/ 16|   1.040/ 17 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  61   |   28113|     1445.12|   1.012/ 57|   1.008/ 86|   1.007/ 98|   1.006/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  50   |     632|       60.22|   1.037/ 19|   1.032/ 22|   1.031/ 22|   1.029/ 23 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  48   |      41|       53.84|   1.052/ 13|   1.047/ 15|   1.046/ 15|   1.044/ 16 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  55   |    1547|      132.32|   1.037/ 18|   1.029/ 24|   1.026/ 26|   1.024/ 29 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  56   |     292|       73.80|   1.020/ 35|   1.013/ 53|   1.011/ 61|   1.010/ 72 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  60   |     137|       32.55|   1.022/ 32|   1.018/ 38|   1.018/ 39|   1.017/ 41 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  56   |    4412|      344.62|   1.042/ 16|   1.033/ 21|   1.030/ 23|   1.027/ 25 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  54   |     118|       36.81|   1.021/ 34|   1.017/ 42|   1.016/ 44|   1.015/ 46 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  47   |     483|      455.60|   1.042/ 16|   1.034/ 20|   1.031/ 22|   1.029/ 24 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  59   |     396|       76.97|   1.037/ 19|   1.026/ 26|   1.024/ 29|   1.021/ 33 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  64   |      44|       49.50|   1.046/ 15|   1.045/ 15|   1.045/ 15|   1.045/ 15 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  54   |     270|       39.53|   1.024/ 29|   1.023/ 30|   1.023/ 30|   1.023/ 30 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  58   |    1213|       41.84|   1.033/ 21|   1.028/ 25|   1.027/ 26|   1.026/ 27 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  53   |      75|       23.33|   1.038/ 18|   1.037/ 18|   1.037/ 18|   1.037/ 18 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  55   |      55|       88.15|   1.007/ 98|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  61   |     984|      115.23|   1.041/ 17|   1.031/ 22|   1.029/ 24|   1.026/ 26 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  75   |     994|      130.56|   1.015/ 46|   1.012/ 56|   1.012/ 60|   1.011/ 63 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  45   |      59|       32.87|   1.028/ 24|   1.018/ 38|   1.016/ 44|   1.013/ 51 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  55   |     432|       74.22|   1.024/ 28|   1.022/ 32|   1.021/ 33|   1.020/ 34 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  31   |       7|       12.09|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  53   |     143|        4.44|   1.055/ 12|   1.045/ 15|   1.043/ 16|   1.040/ 17 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  64   |      32|       11.31|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  63   |     521|       12.12|   1.012/ 58|   1.011/ 63|   1.011/ 65|   1.011/ 66 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  46   |       2|        0.06|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  67   |     346|        7.71|   1.032/ 22|   1.026/ 26|   1.025/ 28|   1.024/ 29 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  49   |      50|       16.80|   1.031/ 22|   1.027/ 25|   1.026/ 26|   1.025/ 28 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  74   |     106|        4.13|   1.009/ 78|   1.003/ **|   1.001/ **|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  63   |     645|       72.42|   1.007/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  62   |      34|        3.34|   1.029/ 24|   1.031/ 22|   1.032/ 22|   1.033/ 21 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  59   |       8|        5.46|   1.007/ 98|   1.009/ 76|   1.010/ 71|   1.010/ 66 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  57   |     252|        1.50|   1.038/ 18|   1.039/ 18|   1.039/ 17|   1.040/ 17 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  44   |     147|       15.67|   1.041/ 17|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  64   |    9177|      796.27|   1.013/ 54|   1.008/ 92|   1.006/ **|   1.005/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  38   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  46   |     142|       12.39|   1.064/ 11|   1.061/ 11|   1.060/ 11|   1.059/ 12 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  54   |     119|       36.16|   1.046/ 15|   1.051/ 14|   1.052/ 13|   1.053/ 13 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  44   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  58   |   13714|       64.87|   1.067/ 10|   1.060/ 11|   1.059/ 12|   1.057/ 12 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  64   |     102|       14.65|   1.031/ 22|   1.026/ 27|   1.025/ 28|   1.024/ 29 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  57   |      51|        2.46|   1.013/ 55|   1.012/ 57|   1.012/ 58|   1.012/ 59 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  31   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  50   |     137|        5.15|   1.040/ 17|   1.045/ 15|   1.047/ 15|   1.048/ 14 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  66   |    5936|      156.20|   1.040/ 17|   1.029/ 24|   1.026/ 27|   1.023/ 30 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  16   |      41|        2.54|   1.190/  3|   1.072/  9|   1.083/  8|   1.100/  7 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  53   |     351|       18.39|   1.034/ 20|   1.029/ 24|   1.028/ 25|   1.026/ 26 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  64   |    4637|        3.31|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  53   |     526|       10.66|   1.043/ 16|   1.040/ 17|   1.039/ 17|   1.038/ 18 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  56   |       7|        1.35|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  56   |     100|       24.48|   1.026/ 27|   1.015/ 45|   1.013/ 54|   1.010/ 69 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  57   |      83|        7.43|   1.022/ 31|   1.011/ 61|   1.009/ 79|   1.006/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  61   |     557|       95.65|   1.013/ 53|   1.009/ 81|   1.007/ 94|   1.006/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  58   |     420|       40.53|   1.022/ 31|   1.020/ 35|   1.019/ 37|   1.018/ 38 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  61   |    2576|      147.46|   1.069/ 10|   1.066/ 10|   1.065/ 11|   1.064/ 11 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  67   |     591|        5.89|   1.030/ 23|   1.024/ 29|   1.022/ 31|   1.021/ 34 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  44   |      21|        3.21|   1.058/ 12|   1.053/ 13|   1.052/ 13|   1.050/ 14 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  22   |       6|        4.42|   1.250/  3|   1.037/ 18|   1.055/ 12|   1.075/  9 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  39   |       5|        0.05|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  54   |     291|       52.62|   1.023/ 30|   1.017/ 41|   1.015/ 45|   1.014/ 50 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  89   |   29345|      437.49|   1.006/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  55   |      11|        5.08|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  52   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  40   |      12|        3.10|   1.037/ 19|   1.030/ 23|   1.029/ 24|   1.027/ 25 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  66   |    8201|       98.62|   1.014/ 48|   1.008/ 83|   1.007/ **|   1.005/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  54   |      24|        0.80|   1.032/ 22|   1.028/ 24|   1.028/ 25|   1.028/ 25 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  64   |     158|       14.71|   1.008/ 89|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  59   |      30|        1.78|   1.047/ 15|   1.038/ 18|   1.036/ 19|   1.035/ 20 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  29   |      13|        1.02|   1.055/ 13|   1.021/ 33|   1.013/ 54|   1.005/ ** |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  18   |       2|        1.25|   1.267/  2|   1.098/  7|   1.048/ 14|   1.000/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  39   |      18|        1.57|   1.077/  9|   1.076/  9|   1.076/  9|   1.076/  9 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  49   |     128|       14.01|   1.045/ 15|   1.040/ 17|   1.039/ 18|   1.037/ 18 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  60   |     454|       46.42|   1.027/ 26|   1.019/ 36|   1.018/ 39|   1.016/ 44 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  64   |    2690|        1.98|   1.062/ 11|   1.058/ 12|   1.057/ 12|   1.056/ 12 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  64   |    1049|        3.93|   1.020/ 34|   1.016/ 42|   1.015/ 45|   1.015/ 47 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  84   |    6995|       83.90|   1.009/ 74|   1.007/ 95|   1.007/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  71   |     113|        2.88|   1.016/ 43|   1.018/ 39|   1.018/ 39|   1.018/ 38 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  64   |    1653|      335.89|   1.018/ 39|   1.006/ **|   1.004/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  54   |     266|       28.90|   1.015/ 46|   1.013/ 52|   1.013/ 54|   1.012/ 55 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  83   |   32346|      536.97|   1.008/ 84|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  56   |      10|        3.56|   1.013/ 53|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  91   |     811|        6.44|   1.036/ 19|   1.027/ 25|   1.025/ 28|   1.023/ 31 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  48   |       9|        0.88|   1.009/ 80|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  50   |      33|        1.77|   1.018/ 38|   1.016/ 44|   1.015/ 46|   1.014/ 49 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  49   |      39|        0.82|   1.055/ 12|   1.059/ 12|   1.060/ 11|   1.060/ 11 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  49   |      33|       18.34|   1.010/ 70|   1.014/ 50|   1.015/ 47|   1.016/ 44 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  40   |      76|       17.13|   1.086/  8|   1.100/  7|   1.104/  7|   1.108/  6 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  41   |      13|        2.00|   1.029/ 24|   1.015/ 46|   1.010/ 67|   1.005/ ** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  41   |      19|        9.97|   1.020/ 35|   1.008/ 82|   1.006/ **|   1.003/ ** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  65   |      27|        3.90|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  40   |      21|        4.68|   1.021/ 32|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  42   |       3|        0.46|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  54   |      52|       18.67|   1.013/ 55|   1.011/ 62|   1.011/ 64|   1.011/ 65 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  58   |     111|        3.40|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  46   |      42|        2.10|   1.040/ 17|   1.044/ 16|   1.045/ 15|   1.046/ 15 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  45   |       1|        0.25|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  56   |    4316|       34.10|   1.067/ 10|   1.061/ 11|   1.060/ 11|   1.059/ 12 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  57   |     188|       70.27|   1.040/ 17|   1.037/ 19|   1.036/ 19|   1.036/ 19 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  65   |     195|        5.43|   1.009/ 80|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  69   |    5816|      333.16|   1.012/ 59|   1.007/ **|   1.006/ **|   1.004/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  46   |      21|        4.32|   1.007/ **|   1.002/ **|   1.000/ **|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  48   |       7|        1.08|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  50   |      50|        2.24|   1.032/ 21|   1.027/ 25|   1.026/ 27|   1.024/ 28 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  52   |     182|        0.88|   1.084/  8|   1.071/ 10|   1.067/ 10|   1.064/ 11 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  53   |      99|       47.71|   1.019/ 36|   1.008/ 84|   1.005/ **|   1.003/ ** |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  61   |     229|       42.61|   1.007/ 93|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  44   |      18|        3.92|   1.038/ 18|   1.035/ 20|   1.034/ 21|   1.032/ 21 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  56   |     809|        3.69|   1.058/ 12|   1.051/ 14|   1.049/ 14|   1.047/ 15 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  64   |     266|       63.01|   1.027/ 26|   1.023/ 30|   1.022/ 31|   1.021/ 33 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  54   |      10|        1.46|   1.007/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  55   |    2319|       72.18|   1.061/ 11|   1.050/ 14|   1.047/ 15|   1.044/ 16 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 102   |     874|        8.05|   1.022/ 31|   1.017/ 40|   1.016/ 43|   1.015/ 46 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  63   |     900|       23.44|   1.026/ 27|   1.018/ 39|   1.015/ 45|   1.013/ 52 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  58   |    1209|      117.68|   1.014/ 48|   1.009/ 76|   1.008/ 89|   1.006/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  47   |      14|        5.17|   1.022/ 32|   1.023/ 30|   1.024/ 29|   1.024/ 29 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  53   |    1057|       54.46|   1.029/ 24|   1.025/ 28|   1.023/ 29|   1.022/ 31 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  56   |    2376|       16.19|   1.063/ 11|   1.050/ 14|   1.047/ 15|   1.043/ 16 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  51   |     277|        8.10|   1.041/ 17|   1.039/ 18|   1.039/ 18|   1.038/ 18 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  43   |      21|        1.27|   1.070/ 10|   1.090/  8|   1.095/  7|   1.100/  7 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  55   |     242|       34.73|   1.014/ 48|   1.016/ 42|   1.017/ 41|   1.017/ 40 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  21   |      23|        2.88|   1.154/  4|   1.070/ 10|   1.055/ 12|   1.044/ 16 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  54   |      23|        3.97|   1.027/ 25|   1.019/ 36|   1.017/ 41|   1.015/ 47 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  47   |      28|        5.12|   1.017/ 40|   1.005/ **|   1.002/ **|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  61   |     107|       50.95|   1.011/ 64|   1.007/ **|   1.005/ **|   1.004/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  36   |      57|        3.56|   1.057/ 12|   1.044/ 16|   1.040/ 17|   1.035/ 19 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  48   |     227|        3.87|   1.057/ 12|   1.053/ 13|   1.052/ 13|   1.050/ 14 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  72   |   27895|      592.24|   1.008/ 82|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  47   |      10|        0.44|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  62   |      92|        2.16|   1.091/  7|   1.088/  8|   1.087/  8|   1.086/  8 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  64   |    3577|      345.97|   1.024/ 29|   1.017/ 41|   1.015/ 45|   1.014/ 50 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  70   |    1940|      225.46|   1.007/ **|   1.003/ **|   1.001/ **|   1.000/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  46   |       3|        0.17|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  44   |      22|        0.40|   1.021/ 33|   1.029/ 24|   1.031/ 22|   1.033/ 21 |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  74   |      58|        0.87|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  48   |      12|        1.53|   1.022/ 31|   1.026/ 26|   1.028/ 25|   1.029/ 24 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  50   |       8|        5.87|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  56   |      46|        3.94|   1.008/ 83|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  58   |    4107|       49.40|   1.019/ 37|   1.011/ 61|   1.010/ 73|   1.008/ 89 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  75   |   90709|      275.25|   1.022/ 31|   1.013/ 53|   1.011/ 64|   1.009/ 79 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  62   |     449|       10.72|   1.043/ 16|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  55   |     235|       23.73|   1.059/ 12|   1.045/ 15|   1.042/ 16|   1.038/ 18 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  64   |   36015|      542.11|   1.020/ 34|   1.013/ 54|   1.011/ 63|   1.009/ 76 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  46   |      19|        5.49|   1.016/ 43|   1.012/ 60|   1.011/ 64|   1.010/ 69 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  48   |      11|        0.31|   1.013/ 52|   1.005/ **|   1.003/ **|   1.001/ ** |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  48   |      10|        0.31|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  42   |       7|        0.41|   1.098/  7|   1.141/  5|   1.151/  4|   1.161/  4 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  52   |       4|        0.26|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |

