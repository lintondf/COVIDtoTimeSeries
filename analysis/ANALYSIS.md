# State and Country COVID-19 Analysis #
## Updated: 2020-05-22 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  69   |   29434|     1513.06|   1.008/ 92|   1.005/ **|   1.004/ **|   1.004/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  73   |   11481|     1292.60|   1.016/ 42|   1.011/ 65|   1.009/ 76|   1.008/ 90 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  63   |    6444|      927.29|   1.022/ 31|   1.016/ 45|   1.014/ 50|   1.012/ 56 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  64   |    5237|      524.41|   1.012/ 58|   1.008/ 84|   1.007/ 94|   1.006/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  64   |    5216|      407.44|   1.026/ 26|   1.017/ 41|   1.014/ 48|   1.012/ 58 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  66   |    4819|      380.30|   1.030/ 23|   1.025/ 27|   1.024/ 29|   1.023/ 30 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  79   |    3719|       94.12|   1.025/ 28|   1.020/ 34|   1.019/ 36|   1.018/ 38 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  64   |    3714|     1041.71|   1.019/ 37|   1.014/ 49|   1.013/ 54|   1.012/ 59 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  69   |    2690|      578.66|   1.014/ 51|   1.011/ 64|   1.010/ 68|   1.009/ 73 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  64   |    2278|      376.75|   1.028/ 25|   1.021/ 33|   1.019/ 35|   1.018/ 39 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  83   |  100290|      304.33|   1.016/ 43|   1.011/ 63|   1.010/ 71|   1.009/ 81 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  72   |   38191|      574.86|   1.012/ 58|   1.008/ 86|   1.007/ 98|   1.006/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  91   |   33503|      556.17|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  97   |   29829|      444.70|   1.004/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  80   |   28738|      610.14|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  66   |   20789|       98.34|   1.057/ 12|   1.052/ 13|   1.050/ 14|   1.049/ 14 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  72   |    9509|      825.11|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  74   |    8498|      102.20|   1.008/ 88|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  92   |    7380|       88.51|   1.008/ 88|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  64   |    6652|       52.55|   1.059/ 12|   1.055/ 12|   1.054/ 13|   1.053/ 13 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  58   |     559|      114.09|   1.029/ 24|   1.022/ 32|   1.020/ 35|   1.018/ 38 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  58   |      10|       13.98|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  62   |     811|      111.36|   1.038/ 18|   1.032/ 21|   1.030/ 23|   1.029/ 24 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  59   |     111|       36.74|   1.018/ 39|   1.010/ 70|   1.008/ 87|   1.006/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  79   |    3719|       94.12|   1.025/ 28|   1.020/ 34|   1.019/ 36|   1.018/ 38 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  69   |    1322|      229.52|   1.025/ 28|   1.024/ 29|   1.024/ 29|   1.023/ 29 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  64   |    3714|     1041.71|   1.019/ 37|   1.014/ 49|   1.013/ 54|   1.012/ 59 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  57   |     328|      336.83|   1.033/ 21|   1.029/ 23|   1.028/ 24|   1.027/ 25 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  75   |    2240|      104.27|   1.022/ 31|   1.018/ 39|   1.017/ 42|   1.015/ 45 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  71   |    1796|      169.18|   1.019/ 36|   1.015/ 45|   1.015/ 47|   1.014/ 51 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  52   |      17|       12.05|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  57   |      77|       42.85|   1.011/ 65|   1.011/ 65|   1.011/ 65|   1.011/ 65 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  66   |    4819|      380.30|   1.030/ 23|   1.025/ 27|   1.024/ 29|   1.023/ 30 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  67   |    2009|      298.43|   1.025/ 28|   1.017/ 39|   1.016/ 44|   1.014/ 50 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  58   |     421|      133.47|   1.042/ 16|   1.036/ 19|   1.034/ 20|   1.033/ 21 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  70   |     214|       73.58|   1.016/ 44|   1.012/ 60|   1.010/ 66|   1.009/ 74 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  67   |     382|       85.47|   1.022/ 31|   1.021/ 34|   1.020/ 34|   1.020/ 35 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  69   |    2690|      578.66|   1.014/ 51|   1.011/ 64|   1.010/ 68|   1.009/ 73 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  56   |      75|       55.44|   1.013/ 52|   1.011/ 62|   1.011/ 65|   1.010/ 68 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  64   |    2278|      376.75|   1.028/ 25|   1.021/ 33|   1.019/ 35|   1.018/ 39 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  63   |    6444|      927.29|   1.022/ 31|   1.016/ 45|   1.014/ 50|   1.012/ 56 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  64   |    5237|      524.41|   1.012/ 58|   1.008/ 84|   1.007/ 94|   1.006/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  62   |     859|      152.32|   1.035/ 20|   1.026/ 26|   1.024/ 28|   1.022/ 31 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  64   |     612|      205.68|   1.032/ 21|   1.027/ 26|   1.025/ 27|   1.024/ 29 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  64   |     687|      111.97|   1.028/ 25|   1.024/ 29|   1.023/ 30|   1.022/ 32 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  56   |      16|       14.99|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  55   |     138|       71.32|   1.035/ 19|   1.035/ 20|   1.035/ 20|   1.034/ 20 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  67   |     389|      126.29|   1.020/ 35|   1.016/ 42|   1.016/ 45|   1.015/ 47 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  60   |     206|      151.74|   1.042/ 16|   1.034/ 20|   1.032/ 22|   1.030/ 23 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  73   |   11481|     1292.60|   1.016/ 42|   1.011/ 65|   1.009/ 76|   1.008/ 90 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  58   |     309|      147.56|   1.037/ 19|   1.030/ 23|   1.028/ 25|   1.026/ 27 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  69   |   29434|     1513.06|   1.008/ 92|   1.005/ **|   1.004/ **|   1.004/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  58   |     766|       73.00|   1.026/ 27|   1.020/ 35|   1.018/ 38|   1.017/ 41 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  56   |      51|       67.57|   1.036/ 19|   1.029/ 24|   1.027/ 25|   1.025/ 27 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  63   |    1875|      160.37|   1.029/ 24|   1.024/ 28|   1.023/ 30|   1.022/ 31 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  64   |     310|       78.24|   1.012/ 60|   1.007/ 92|   1.006/ **|   1.006/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  68   |     150|       35.55|   1.014/ 50|   1.010/ 70|   1.009/ 77|   1.008/ 87 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  64   |    5216|      407.44|   1.026/ 26|   1.017/ 41|   1.014/ 48|   1.012/ 58 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  62   |     131|       40.88|   1.014/ 50|   1.011/ 65|   1.010/ 71|   1.009/ 78 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  55   |     568|      536.21|   1.028/ 24|   1.021/ 32|   1.020/ 35|   1.018/ 38 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  67   |     441|       85.65|   1.021/ 33|   1.014/ 48|   1.013/ 54|   1.011/ 61 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  72   |      58|       65.75|   1.031/ 22|   1.025/ 27|   1.024/ 29|   1.022/ 32 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  62   |     322|       47.15|   1.020/ 35|   1.017/ 40|   1.017/ 42|   1.016/ 43 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  66   |    1502|       51.82|   1.028/ 25|   1.025/ 28|   1.024/ 29|   1.023/ 30 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  61   |      93|       29.12|   1.033/ 21|   1.031/ 22|   1.031/ 22|   1.030/ 23 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  63   |      55|       87.58|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  69   |    1173|      137.41|   1.027/ 26|   1.019/ 36|   1.017/ 40|   1.015/ 46 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  83   |    1074|      141.06|   1.011/ 62|   1.009/ 76|   1.009/ 80|   1.008/ 85 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  53   |      72|       39.98|   1.023/ 29|   1.022/ 32|   1.021/ 33|   1.021/ 33 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  63   |     497|       85.29|   1.019/ 36|   1.016/ 42|   1.016/ 44|   1.015/ 46 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  39   |      11|       18.35|   1.016/ 43|   1.038/ 18|   1.044/ 16|   1.050/ 14 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  61   |     202|        6.26|   1.047/ 15|   1.040/ 17|   1.039/ 18|   1.037/ 19 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  72   |      32|       11.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  71   |     575|       13.36|   1.012/ 57|   1.012/ 57|   1.012/ 57|   1.012/ 57 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  54   |       2|        0.06|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  75   |     427|        9.49|   1.028/ 24|   1.025/ 27|   1.024/ 28|   1.024/ 29 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  57   |      67|       22.79|   1.039/ 17|   1.043/ 16|   1.044/ 16|   1.045/ 15 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  82   |     105|        4.09|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  71   |     646|       72.51|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  70   |      43|        4.30|   1.032/ 21|   1.034/ 20|   1.035/ 20|   1.035/ 20 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  67   |      12|        7.85|   1.023/ 30|   1.029/ 24|   1.030/ 23|   1.031/ 22 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  65   |     389|        2.31|   1.051/ 13|   1.057/ 12|   1.059/ 12|   1.060/ 11 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  52   |     189|       20.10|   1.034/ 20|   1.030/ 23|   1.029/ 24|   1.028/ 25 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  72   |    9509|      825.11|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  46   |       3|        0.26|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  54   |     216|       18.85|   1.057/ 12|   1.052/ 13|   1.051/ 14|   1.049/ 14 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  62   |     152|       46.12|   1.030/ 23|   1.023/ 30|   1.021/ 33|   1.019/ 37 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  52   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  66   |   20789|       98.34|   1.057/ 12|   1.052/ 13|   1.050/ 14|   1.049/ 14 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  72   |     122|       17.55|   1.026/ 27|   1.023/ 30|   1.022/ 31|   1.021/ 33 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  65   |      53|        2.55|   1.006/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  39   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  58   |     170|        6.39|   1.022/ 31|   1.022/ 32|   1.021/ 33|   1.021/ 33 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  74   |    6891|      181.34|   1.024/ 29|   1.015/ 46|   1.013/ 54|   1.011/ 65 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  24   |      59|        3.66|   1.075/  9|   1.036/ 19|   1.029/ 24|   1.022/ 31 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  61   |     531|       27.80|   1.053/ 13|   1.061/ 11|   1.063/ 11|   1.065/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  72   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  61   |     672|       13.59|   1.034/ 20|   1.030/ 23|   1.028/ 24|   1.027/ 25 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  64   |      10|        2.02|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  64   |     103|       25.18|   1.009/ 74|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  65   |      84|        7.50|   1.007/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  69   |     574|       98.52|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  66   |     467|       45.10|   1.015/ 46|   1.011/ 62|   1.010/ 68|   1.009/ 76 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  69   |    3433|      196.52|   1.038/ 18|   1.031/ 22|   1.029/ 23|   1.027/ 25 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  75   |     712|        7.10|   1.027/ 26|   1.024/ 29|   1.023/ 30|   1.022/ 31 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  52   |      34|        5.29|   1.058/ 12|   1.054/ 13|   1.053/ 13|   1.052/ 13 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  30   |       9|        6.39|   1.060/ 11|   1.034/ 20|   1.027/ 25|   1.021/ 33 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  47   |       5|        0.05|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  62   |     317|       57.33|   1.014/ 50|   1.009/ 77|   1.008/ 90|   1.006/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  97   |   29829|      444.70|   1.004/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  63   |      14|        6.25|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  60   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  48   |      13|        3.43|   1.018/ 38|   1.007/ **|   1.004/ **|   1.000/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  74   |    8498|      102.20|   1.008/ 88|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  62   |      32|        1.07|   1.036/ 19|   1.037/ 18|   1.038/ 18|   1.038/ 18 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  72   |     168|       15.68|   1.008/ 81|   1.008/ 88|   1.008/ 89|   1.008/ 91 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  67   |      43|        2.61|   1.060/ 11|   1.068/ 10|   1.070/ 10|   1.072/  9 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  37   |      19|        1.55|   1.043/ 16|   1.045/ 15|   1.044/ 15|   1.043/ 16 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  26   |       6|        3.86|   1.049/ 14|   1.126/  5|   1.144/  5|   1.160/  4 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  47   |      25|        2.14|   1.048/ 14|   1.034/ 20|   1.031/ 23|   1.027/ 26 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  57   |     162|       17.71|   1.032/ 22|   1.024/ 28|   1.022/ 31|   1.020/ 34 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  68   |     499|       51.05|   1.016/ 43|   1.011/ 65|   1.009/ 74|   1.008/ 87 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  72   |    3849|        2.83|   1.050/ 14|   1.043/ 16|   1.042/ 16|   1.040/ 17 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  72   |    1249|        4.68|   1.024/ 29|   1.025/ 28|   1.025/ 27|   1.026/ 27 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  92   |    7380|       88.51|   1.008/ 88|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  79   |     133|        3.39|   1.021/ 32|   1.024/ 29|   1.024/ 28|   1.025/ 28 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  72   |    1666|      338.45|   1.009/ 78|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  62   |     285|       31.06|   1.010/ 67|   1.008/ 83|   1.008/ 88|   1.007/ 94 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  91   |   33503|      556.17|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  64   |       9|        3.42|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  99   |     931|        7.39|   1.022/ 31|   1.014/ 48|   1.012/ 56|   1.010/ 66 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  56   |       9|        0.85|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  58   |      36|        1.94|   1.013/ 54|   1.009/ 75|   1.008/ 83|   1.007/ 94 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  57   |      57|        1.20|   1.045/ 15|   1.035/ 20|   1.032/ 21|   1.030/ 23 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  57   |      31|       17.15|   1.005/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  48   |     145|       32.83|   1.078/  9|   1.067/ 10|   1.063/ 11|   1.059/ 12 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  49   |      15|        2.23|   1.018/ 39|   1.009/ 78|   1.007/ 99|   1.005/ ** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  49   |      21|       10.98|   1.017/ 40|   1.021/ 33|   1.022/ 31|   1.024/ 29 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  73   |      27|        3.90|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  48   |      22|        5.02|   1.014/ 50|   1.018/ 38|   1.020/ 35|   1.022/ 32 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  50   |       3|        0.44|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  62   |      60|       21.56|   1.018/ 39|   1.020/ 35|   1.020/ 34|   1.021/ 33 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  66   |     116|        3.53|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  54   |      59|        2.92|   1.041/ 17|   1.039/ 18|   1.039/ 18|   1.038/ 18 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  53   |       1|        0.25|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  64   |    6652|       52.55|   1.059/ 12|   1.055/ 12|   1.054/ 13|   1.053/ 13 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  65   |     243|       90.51|   1.032/ 21|   1.029/ 24|   1.028/ 25|   1.027/ 26 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  73   |     199|        5.55|   1.005/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  77   |    6009|      344.22|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  54   |      21|        4.26|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  56   |      13|        1.99|   1.185/  4|   1.255/  3|   1.272/  2|   1.289/  2 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  58   |      60|        2.69|   1.026/ 26|   1.024/ 29|   1.023/ 30|   1.022/ 31 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  60   |     234|        1.13|   1.046/ 15|   1.028/ 25|   1.023/ 30|   1.019/ 37 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  61   |     109|       52.48|   1.017/ 40|   1.016/ 42|   1.016/ 42|   1.016/ 42 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  69   |     238|       44.34|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  52   |      29|        6.12|   1.061/ 11|   1.073/  9|   1.076/  9|   1.080/  9 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  64   |    1072|        4.89|   1.042/ 16|   1.035/ 20|   1.033/ 21|   1.031/ 22 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  72   |     304|       71.99|   1.019/ 36|   1.015/ 45|   1.014/ 48|   1.013/ 52 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  62   |      11|        1.57|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  63   |    3282|      102.14|   1.050/ 14|   1.044/ 16|   1.042/ 16|   1.041/ 17 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 110   |     962|        8.86|   1.016/ 44|   1.012/ 59|   1.011/ 64|   1.010/ 70 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  71   |    1018|       26.51|   1.018/ 38|   1.013/ 53|   1.012/ 58|   1.011/ 64 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  66   |    1287|      125.27|   1.011/ 64|   1.009/ 79|   1.008/ 83|   1.008/ 87 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  55   |      16|        5.90|   1.019/ 36|   1.020/ 34|   1.020/ 34|   1.021/ 34 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  61   |    1212|       62.47|   1.019/ 35|   1.014/ 48|   1.013/ 53|   1.012/ 59 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  64   |    3266|       22.26|   1.047/ 15|   1.039/ 18|   1.037/ 19|   1.035/ 20 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  59   |     359|       10.50|   1.035/ 20|   1.031/ 22|   1.030/ 23|   1.029/ 23 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  51   |      34|        2.10|   1.066/ 10|   1.060/ 11|   1.058/ 12|   1.056/ 12 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  63   |     248|       35.58|   1.011/ 64|   1.008/ 83|   1.008/ 90|   1.007/ 98 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  29   |      37|        4.67|   1.079/  9|   1.045/ 15|   1.034/ 20|   1.023/ 30 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  62   |      24|        4.14|   1.012/ 58|   1.004/ **|   1.002/ **|   1.000/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  55   |      29|        5.25|   1.007/ 94|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  69   |     108|       51.64|   1.005/ **|   1.001/ **|   1.001/ **|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  44   |      62|        3.93|   1.028/ 24|   1.017/ 42|   1.014/ 49|   1.012/ 59 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  56   |     348|        5.92|   1.059/ 12|   1.062/ 11|   1.062/ 11|   1.063/ 11 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  80   |   28738|      610.14|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  55   |       9|        0.43|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  70   |     136|        3.21|   1.061/ 11|   1.049/ 14|   1.046/ 15|   1.042/ 16 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  72   |    4046|      391.34|   1.018/ 39|   1.013/ 52|   1.012/ 56|   1.011/ 61 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  78   |    1950|      226.68|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  54   |       3|        0.17|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  52   |      22|        0.40|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  82   |      57|        0.86|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  56   |      12|        1.64|   1.015/ 46|   1.015/ 45|   1.015/ 45|   1.015/ 45 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  58   |       8|        5.87|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  64   |      47|        4.03|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  66   |    4398|       52.89|   1.011/ 60|   1.007/ 93|   1.007/ **|   1.006/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  83   |  100290|      304.33|   1.016/ 43|   1.011/ 63|   1.010/ 71|   1.009/ 81 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  70   |     602|       14.37|   1.038/ 18|   1.035/ 20|   1.035/ 20|   1.034/ 20 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  63   |     262|       26.53|   1.028/ 24|   1.013/ 53|   1.009/ 76|   1.005/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  72   |   38191|      574.86|   1.012/ 58|   1.008/ 86|   1.007/ 98|   1.006/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  54   |      20|        5.80|   1.009/ 74|   1.007/ 96|   1.007/ **|   1.006/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  56   |      13|        0.38|   1.022/ 31|   1.027/ 26|   1.028/ 24|   1.030/ 23 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  56   |      10|        0.31|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  50   |       8|        0.46|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  60   |       4|        0.26|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |

