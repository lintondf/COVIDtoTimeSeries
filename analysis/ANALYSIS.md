# State and Country COVID-19 Analysis #
## Updated: 2020-05-19 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  66   |   29042|     1492.90|   1.009/ 76|   1.006/ **|   1.006/ **|   1.005/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  70   |   11157|     1256.06|   1.020/ 35|   1.013/ 52|   1.012/ 59|   1.010/ 68 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  60   |    6181|      889.39|   1.027/ 26|   1.019/ 36|   1.017/ 40|   1.016/ 44 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  61   |    5107|      511.39|   1.013/ 52|   1.008/ 87|   1.007/ **|   1.005/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  61   |    4965|      387.81|   1.033/ 21|   1.022/ 31|   1.020/ 35|   1.017/ 40 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  63   |    4480|      353.57|   1.033/ 21|   1.028/ 25|   1.026/ 26|   1.025/ 27 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  61   |    3563|      999.30|   1.022/ 31|   1.017/ 41|   1.016/ 44|   1.014/ 48 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  76   |    3505|       88.70|   1.026/ 27|   1.020/ 34|   1.019/ 37|   1.017/ 40 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  66   |    2610|      561.40|   1.015/ 46|   1.011/ 61|   1.010/ 66|   1.010/ 72 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  61   |    2141|      354.11|   1.032/ 22|   1.024/ 28|   1.023/ 31|   1.021/ 33 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  80   |   97144|      294.78|   1.018/ 38|   1.012/ 57|   1.011/ 65|   1.009/ 75 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  69   |   37414|      563.16|   1.014/ 50|   1.009/ 75|   1.008/ 85|   1.007/ 99 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  88   |   33157|      550.42|   1.007/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  94   |   29777|      443.92|   1.005/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  77   |   28472|      604.49|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  63   |   17893|       84.64|   1.059/ 11|   1.053/ 13|   1.052/ 13|   1.050/ 14 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  69   |    9405|      816.06|   1.009/ 79|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  71   |    8385|      100.84|   1.009/ 75|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  89   |    7226|       86.67|   1.008/ 86|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  71   |    6579|      173.14|   1.030/ 23|   1.020/ 34|   1.018/ 39|   1.015/ 45 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  55   |     528|      107.61|   1.034/ 20|   1.027/ 25|   1.026/ 27|   1.024/ 29 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  55   |      10|       14.03|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  59   |     741|      101.84|   1.044/ 16|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  56   |     108|       35.84|   1.019/ 36|   1.006/ **|   1.003/ **|   1.000/ -- |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  76   |    3505|       88.70|   1.026/ 27|   1.020/ 34|   1.019/ 37|   1.017/ 40 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  66   |    1234|      214.30|   1.026/ 26|   1.025/ 28|   1.025/ 28|   1.025/ 28 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  61   |    3563|      999.30|   1.022/ 31|   1.017/ 41|   1.016/ 44|   1.014/ 48 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  54   |     302|      310.02|   1.038/ 18|   1.036/ 19|   1.035/ 20|   1.035/ 20 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  72   |    2131|       99.20|   1.024/ 28|   1.019/ 36|   1.018/ 38|   1.017/ 41 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  68   |    1718|      161.83|   1.020/ 34|   1.015/ 45|   1.014/ 49|   1.013/ 53 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  49   |      17|       12.09|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  54   |      74|       41.49|   1.010/ 66|   1.009/ 74|   1.009/ 76|   1.009/ 78 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  63   |    4480|      353.57|   1.033/ 21|   1.028/ 25|   1.026/ 26|   1.025/ 27 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  64   |    1916|      284.58|   1.028/ 24|   1.020/ 35|   1.018/ 39|   1.016/ 44 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  55   |     381|      120.81|   1.046/ 15|   1.039/ 18|   1.037/ 19|   1.035/ 20 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  67   |     207|       71.21|   1.019/ 36|   1.015/ 46|   1.014/ 49|   1.013/ 53 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  64   |     359|       80.32|   1.018/ 38|   1.013/ 53|   1.012/ 59|   1.010/ 67 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  66   |    2610|      561.40|   1.015/ 46|   1.011/ 61|   1.010/ 66|   1.010/ 72 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  53   |      72|       53.61|   1.015/ 47|   1.012/ 60|   1.011/ 64|   1.010/ 68 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  61   |    2141|      354.11|   1.032/ 22|   1.024/ 28|   1.023/ 31|   1.021/ 33 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  60   |    6181|      889.39|   1.027/ 26|   1.019/ 36|   1.017/ 40|   1.016/ 44 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  61   |    5107|      511.39|   1.013/ 52|   1.008/ 87|   1.007/ **|   1.005/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  59   |     796|      141.07|   1.040/ 17|   1.030/ 23|   1.028/ 25|   1.025/ 27 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  61   |     566|      190.25|   1.035/ 20|   1.029/ 24|   1.028/ 25|   1.026/ 27 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  61   |     641|      104.49|   1.031/ 23|   1.026/ 26|   1.025/ 28|   1.024/ 29 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  53   |      16|       15.03|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  52   |     125|       64.52|   1.038/ 18|   1.039/ 18|   1.039/ 18|   1.039/ 18 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  64   |     371|      120.54|   1.021/ 33|   1.017/ 42|   1.015/ 45|   1.014/ 48 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  57   |     187|      137.78|   1.049/ 14|   1.043/ 16|   1.041/ 17|   1.039/ 17 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  70   |   11157|     1256.06|   1.020/ 35|   1.013/ 52|   1.012/ 59|   1.010/ 68 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  55   |     284|      135.64|   1.044/ 16|   1.037/ 19|   1.035/ 19|   1.034/ 20 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  66   |   29042|     1492.90|   1.009/ 76|   1.006/ **|   1.006/ **|   1.005/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  55   |     724|       69.06|   1.031/ 22|   1.026/ 26|   1.025/ 27|   1.024/ 29 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  53   |      47|       62.02|   1.039/ 18|   1.028/ 25|   1.025/ 28|   1.022/ 32 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  60   |    1751|      149.80|   1.031/ 22|   1.024/ 29|   1.022/ 31|   1.020/ 34 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  61   |     303|       76.48|   1.013/ 53|   1.007/ 97|   1.006/ **|   1.004/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  65   |     146|       34.55|   1.015/ 46|   1.010/ 67|   1.009/ 76|   1.008/ 87 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  61   |    4965|      387.81|   1.033/ 21|   1.022/ 31|   1.020/ 35|   1.017/ 40 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  59   |     127|       39.70|   1.017/ 39|   1.015/ 46|   1.015/ 48|   1.014/ 50 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  52   |     536|      505.75|   1.031/ 22|   1.021/ 33|   1.018/ 38|   1.016/ 44 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  64   |     428|       83.19|   1.024/ 28|   1.015/ 45|   1.013/ 53|   1.011/ 64 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  69   |      55|       61.80|   1.039/ 18|   1.034/ 20|   1.033/ 21|   1.032/ 21 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  59   |     306|       44.84|   1.024/ 29|   1.023/ 30|   1.023/ 30|   1.023/ 30 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  63   |    1398|       48.20|   1.031/ 22|   1.028/ 25|   1.027/ 25|   1.027/ 26 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  58   |      85|       26.61|   1.030/ 23|   1.025/ 27|   1.024/ 29|   1.023/ 30 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  60   |      55|       87.71|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  66   |    1114|      130.48|   1.032/ 22|   1.023/ 30|   1.021/ 33|   1.019/ 37 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  80   |    1046|      137.39|   1.012/ 60|   1.009/ 78|   1.008/ 84|   1.008/ 91 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  50   |      67|       37.65|   1.027/ 25|   1.027/ 25|   1.027/ 25|   1.028/ 25 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  60   |     474|       81.42|   1.021/ 33|   1.018/ 39|   1.017/ 41|   1.016/ 43 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  36   |       7|       12.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  58   |     180|        5.59|   1.054/ 13|   1.050/ 14|   1.049/ 14|   1.048/ 14 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  69   |      32|       11.16|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  68   |     554|       12.89|   1.012/ 57|   1.012/ 57|   1.012/ 57|   1.012/ 57 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  51   |       2|        0.06|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  72   |     397|        8.82|   1.029/ 23|   1.026/ 27|   1.025/ 28|   1.024/ 29 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  54   |      59|       19.94|   1.036/ 19|   1.039/ 18|   1.039/ 17|   1.040/ 17 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  79   |     105|        4.09|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  68   |     646|       72.60|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  67   |      39|        3.89|   1.030/ 23|   1.032/ 22|   1.032/ 22|   1.032/ 21 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  64   |      11|        7.06|   1.034/ 20|   1.048/ 14|   1.051/ 13|   1.055/ 12 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  62   |     327|        1.94|   1.047/ 15|   1.053/ 13|   1.055/ 12|   1.057/ 12 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  49   |     174|       18.45|   1.037/ 19|   1.033/ 21|   1.032/ 21|   1.031/ 22 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  69   |    9405|      816.06|   1.009/ 79|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  43   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  51   |     187|       16.27|   1.059/ 12|   1.051/ 13|   1.049/ 14|   1.047/ 15 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  59   |     143|       43.34|   1.037/ 18|   1.034/ 20|   1.034/ 20|   1.033/ 21 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  49   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  63   |   17893|       84.64|   1.059/ 11|   1.053/ 13|   1.052/ 13|   1.050/ 14 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  69   |     114|       16.39|   1.027/ 25|   1.023/ 29|   1.023/ 31|   1.022/ 32 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  62   |      53|        2.53|   1.007/ 93|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  36   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  55   |     163|        6.14|   1.025/ 28|   1.024/ 28|   1.024/ 28|   1.024/ 29 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  71   |    6579|      173.14|   1.030/ 23|   1.020/ 34|   1.018/ 39|   1.015/ 45 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  21   |      55|        3.40|   1.083/  8|   1.064/ 11|   1.049/ 14|   1.033/ 21 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  58   |     442|       23.12|   1.045/ 15|   1.050/ 14|   1.051/ 13|   1.053/ 13 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  69   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  58   |     618|       12.50|   1.037/ 19|   1.032/ 22|   1.030/ 23|   1.029/ 24 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  61   |       9|        1.80|   1.052/ 13|   1.068/ 10|   1.072/  9|   1.076/  9 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  61   |     102|       25.08|   1.014/ 49|   1.004/ **|   1.002/ **|   1.000/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  62   |      85|        7.56|   1.011/ 62|   1.002/ **|   1.000/ **|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  66   |     569|       97.72|   1.009/ 81|   1.005/ **|   1.003/ **|   1.002/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  63   |     452|       43.67|   1.018/ 39|   1.014/ 49|   1.013/ 53|   1.012/ 58 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  66   |    3197|      183.03|   1.050/ 14|   1.044/ 16|   1.042/ 16|   1.041/ 17 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  72   |     664|        6.62|   1.028/ 25|   1.024/ 28|   1.023/ 29|   1.023/ 31 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  49   |      30|        4.56|   1.067/ 10|   1.071/ 10|   1.073/  9|   1.074/  9 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  27   |       8|        5.78|   1.052/ 13|   1.038/ 18|   1.034/ 20|   1.029/ 24 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  44   |       5|        0.05|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  59   |     310|       56.00|   1.018/ 38|   1.013/ 51|   1.012/ 56|   1.011/ 62 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  94   |   29777|      443.92|   1.005/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  60   |      13|        5.76|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  57   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  45   |      13|        3.41|   1.027/ 26|   1.019/ 37|   1.017/ 41|   1.015/ 47 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  71   |    8385|      100.84|   1.009/ 75|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  59   |      29|        0.97|   1.040/ 17|   1.044/ 15|   1.046/ 15|   1.047/ 15 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  69   |     164|       15.30|   1.009/ 74|   1.008/ 82|   1.008/ 83|   1.008/ 85 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  64   |      36|        2.14|   1.040/ 17|   1.044/ 16|   1.045/ 15|   1.045/ 15 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  34   |      17|        1.37|   1.044/ 16|   1.050/ 14|   1.052/ 13|   1.054/ 13 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  23   |       4|        2.55|   1.075/  9|   1.073/  9|   1.087/  8|   1.103/  7 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  44   |      23|        1.97|   1.058/ 12|   1.041/ 17|   1.036/ 19|   1.031/ 22 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  54   |     152|       16.59|   1.039/ 18|   1.033/ 21|   1.031/ 22|   1.030/ 23 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  65   |     483|       49.44|   1.019/ 36|   1.013/ 53|   1.011/ 60|   1.010/ 70 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  69   |    3392|        2.49|   1.054/ 13|   1.047/ 14|   1.046/ 15|   1.044/ 16 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  69   |    1157|        4.33|   1.022/ 32|   1.021/ 33|   1.021/ 33|   1.021/ 33 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  89   |    7226|       86.67|   1.008/ 86|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  76   |     123|        3.15|   1.018/ 38|   1.020/ 35|   1.020/ 35|   1.020/ 34 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  69   |    1653|      335.94|   1.011/ 63|   1.004/ **|   1.002/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  59   |     278|       30.31|   1.012/ 59|   1.010/ 71|   1.009/ 75|   1.009/ 80 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  88   |   33157|      550.42|   1.007/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  61   |       9|        3.47|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  96   |     899|        7.14|   1.028/ 25|   1.019/ 36|   1.017/ 40|   1.015/ 45 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  53   |       9|        0.86|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  55   |      35|        1.89|   1.016/ 43|   1.014/ 50|   1.013/ 52|   1.013/ 55 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  54   |      52|        1.10|   1.060/ 11|   1.063/ 11|   1.064/ 11|   1.064/ 11 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  54   |      32|       17.76|   1.008/ 92|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  45   |     122|       27.59|   1.090/  8|   1.096/  7|   1.097/  7|   1.098/  7 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  46   |      14|        2.18|   1.027/ 26|   1.019/ 36|   1.018/ 39|   1.017/ 41 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  46   |      20|       10.24|   1.011/ 62|   1.005/ **|   1.003/ **|   1.002/ ** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  70   |      27|        3.92|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  45   |      21|        4.70|   1.009/ 78|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  47   |       3|        0.44|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  59   |      57|       20.30|   1.016/ 44|   1.017/ 40|   1.018/ 39|   1.018/ 38 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  63   |     114|        3.49|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  51   |      53|        2.61|   1.043/ 16|   1.044/ 16|   1.044/ 16|   1.044/ 15 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  50   |       1|        0.25|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  61   |    5685|       44.91|   1.062/ 11|   1.057/ 12|   1.056/ 12|   1.054/ 13 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  62   |     224|       83.40|   1.036/ 19|   1.033/ 21|   1.033/ 21|   1.032/ 21 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  70   |     198|        5.52|   1.006/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  74   |    5966|      341.77|   1.008/ 84|   1.004/ **|   1.004/ **|   1.003/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  51   |      21|        4.28|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  53   |       9|        1.38|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  55   |      56|        2.51|   1.028/ 25|   1.023/ 29|   1.022/ 31|   1.021/ 32 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  57   |     217|        1.05|   1.057/ 12|   1.037/ 19|   1.032/ 22|   1.026/ 26 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  58   |     104|       49.90|   1.015/ 46|   1.010/ 67|   1.009/ 75|   1.008/ 84 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  66   |     236|       43.88|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  49   |      23|        4.91|   1.047/ 14|   1.053/ 13|   1.054/ 13|   1.055/ 12 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  61   |     969|        4.42|   1.046/ 15|   1.037/ 19|   1.034/ 20|   1.032/ 22 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  69   |     290|       68.82|   1.022/ 32|   1.018/ 39|   1.017/ 41|   1.016/ 44 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  59   |      11|        1.55|   1.008/ 83|   1.008/ 83|   1.008/ 82|   1.009/ 81 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  60   |    2897|       90.15|   1.054/ 13|   1.046/ 15|   1.044/ 15|   1.043/ 16 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 107   |     930|        8.57|   1.019/ 36|   1.016/ 44|   1.015/ 47|   1.014/ 50 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  68   |     981|       25.56|   1.021/ 32|   1.016/ 44|   1.014/ 48|   1.013/ 52 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  63   |    1252|      121.86|   1.011/ 63|   1.008/ 92|   1.007/ **|   1.006/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  52   |      15|        5.57|   1.018/ 38|   1.018/ 39|   1.018/ 39|   1.017/ 40 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  58   |    1166|       60.07|   1.024/ 29|   1.019/ 36|   1.018/ 39|   1.017/ 41 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  61   |    2909|       19.83|   1.052/ 13|   1.042/ 16|   1.039/ 17|   1.037/ 19 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  56   |     329|        9.61|   1.037/ 18|   1.035/ 20|   1.034/ 20|   1.033/ 21 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  48   |      29|        1.78|   1.067/ 10|   1.060/ 11|   1.058/ 12|   1.055/ 12 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  60   |     248|       35.56|   1.012/ 56|   1.011/ 65|   1.010/ 68|   1.010/ 73 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  26   |      34|        4.30|   1.077/  9|   1.080/  9|   1.079/  9|   1.076/  9 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  59   |      23|        4.09|   1.017/ 40|   1.008/ 83|   1.006/ **|   1.004/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  52   |      29|        5.23|   1.011/ 61|   1.007/ 94|   1.007/ **|   1.006/ ** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  66   |     108|       51.53|   1.006/ **|   1.002/ **|   1.001/ **|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  41   |      59|        3.74|   1.036/ 19|   1.016/ 44|   1.010/ 67|   1.005/ ** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  53   |     290|        4.93|   1.053/ 13|   1.049/ 14|   1.048/ 14|   1.047/ 15 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  77   |   28472|      604.49|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  52   |       9|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  67   |     120|        2.82|   1.070/ 10|   1.058/ 12|   1.054/ 13|   1.051/ 13 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  69   |    3888|      376.09|   1.020/ 34|   1.016/ 44|   1.015/ 47|   1.014/ 51 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  75   |    1946|      226.18|   1.004/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  51   |       3|        0.17|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  49   |      23|        0.40|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  79   |      58|        0.87|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  53   |      12|        1.59|   1.012/ 58|   1.012/ 56|   1.012/ 56|   1.012/ 57 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  55   |       8|        5.87|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  61   |      46|        3.97|   1.005/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  63   |    4299|       51.70|   1.014/ 49|   1.009/ 73|   1.008/ 83|   1.007/ 96 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  80   |   97144|      294.78|   1.018/ 38|   1.012/ 57|   1.011/ 65|   1.009/ 75 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  67   |     543|       12.95|   1.041/ 17|   1.039/ 18|   1.038/ 18|   1.038/ 18 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  60   |     256|       25.89|   1.037/ 19|   1.019/ 36|   1.014/ 48|   1.010/ 71 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  69   |   37414|      563.16|   1.014/ 50|   1.009/ 75|   1.008/ 85|   1.007/ 99 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  51   |      20|        5.69|   1.011/ 62|   1.009/ 76|   1.009/ 80|   1.008/ 85 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  53   |      12|        0.34|   1.019/ 36|   1.022/ 32|   1.023/ 30|   1.024/ 29 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  53   |      10|        0.31|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  47   |       8|        0.47|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  57   |       4|        0.26|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |

