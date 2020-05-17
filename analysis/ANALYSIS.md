# State and Country COVID-19 Analysis #
## Updated: 2020-05-17 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  64   |   28721|     1476.37|   1.010/ 68|   1.007/ 99|   1.006/ **|   1.005/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  68   |   10891|     1226.15|   1.023/ 30|   1.016/ 43|   1.014/ 48|   1.013/ 54 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  58   |    5972|      859.40|   1.030/ 23|   1.022/ 31|   1.020/ 35|   1.018/ 38 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  59   |    5041|      504.72|   1.016/ 44|   1.010/ 70|   1.009/ 81|   1.007/ 97 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  59   |    4789|      374.04|   1.039/ 18|   1.031/ 22|   1.029/ 24|   1.026/ 26 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  61   |    4264|      336.49|   1.037/ 19|   1.033/ 21|   1.032/ 21|   1.031/ 22 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  59   |    3448|      967.16|   1.024/ 28|   1.018/ 39|   1.016/ 42|   1.015/ 46 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  74   |    3375|       85.41|   1.028/ 24|   1.022/ 31|   1.021/ 33|   1.020/ 35 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  64   |    2554|      549.33|   1.016/ 43|   1.012/ 59|   1.011/ 64|   1.010/ 71 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  70   |    2057|       95.79|   1.027/ 25|   1.022/ 31|   1.021/ 33|   1.020/ 35 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  78   |   94902|      287.98|   1.020/ 34|   1.013/ 51|   1.012/ 58|   1.010/ 67 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  67   |   36948|      556.15|   1.017/ 41|   1.011/ 65|   1.009/ 77|   1.007/ 94 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  86   |   32877|      545.79|   1.007/ 94|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  75   |   28274|      600.29|   1.007/ 95|   1.005/ **|   1.004/ **|   1.004/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  92   |   29595|      441.22|   1.005/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  61   |   16213|       76.69|   1.064/ 11|   1.059/ 12|   1.057/ 12|   1.056/ 12 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  67   |    9321|      808.77|   1.010/ 67|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  69   |    8322|      100.09|   1.011/ 62|   1.006/ **|   1.005/ **|   1.003/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  87   |    7134|       85.56|   1.009/ 81|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  69   |    6340|      166.84|   1.034/ 20|   1.024/ 29|   1.022/ 32|   1.019/ 36 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  53   |     505|      102.89|   1.040/ 17|   1.038/ 18|   1.037/ 18|   1.037/ 19 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  53   |      10|       14.02|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  57   |     692|       95.13|   1.049/ 14|   1.049/ 14|   1.048/ 14|   1.048/ 14 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  54   |     108|       35.67|   1.026/ 27|   1.012/ 55|   1.009/ 76|   1.006/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  74   |    3375|       85.41|   1.028/ 24|   1.022/ 31|   1.021/ 33|   1.020/ 35 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  64   |    1178|      204.57|   1.026/ 27|   1.022/ 31|   1.021/ 32|   1.021/ 33 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  59   |    3448|      967.16|   1.024/ 28|   1.018/ 39|   1.016/ 42|   1.015/ 46 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  52   |     283|      290.31|   1.040/ 17|   1.036/ 19|   1.036/ 19|   1.035/ 20 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  70   |    2057|       95.79|   1.027/ 25|   1.022/ 31|   1.021/ 33|   1.020/ 35 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  66   |    1670|      157.26|   1.023/ 30|   1.018/ 39|   1.017/ 42|   1.015/ 45 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  47   |      17|       12.13|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  52   |      73|       40.78|   1.011/ 60|   1.010/ 67|   1.010/ 68|   1.010/ 69 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  61   |    4264|      336.49|   1.037/ 19|   1.033/ 21|   1.032/ 21|   1.031/ 22 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  62   |    1853|      275.22|   1.033/ 21|   1.024/ 29|   1.022/ 31|   1.020/ 35 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  53   |     356|      112.69|   1.051/ 13|   1.046/ 15|   1.045/ 15|   1.044/ 16 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  65   |     202|       69.38|   1.022/ 32|   1.018/ 38|   1.017/ 40|   1.017/ 42 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  62   |     351|       78.51|   1.021/ 33|   1.016/ 44|   1.014/ 48|   1.013/ 52 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  64   |    2554|      549.33|   1.016/ 43|   1.012/ 59|   1.011/ 64|   1.010/ 71 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  51   |      71|       52.54|   1.017/ 41|   1.014/ 48|   1.014/ 51|   1.013/ 53 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  59   |    2049|      338.84|   1.035/ 19|   1.028/ 25|   1.026/ 26|   1.024/ 28 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  58   |    5972|      859.40|   1.030/ 23|   1.022/ 31|   1.020/ 35|   1.018/ 38 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  59   |    5041|      504.72|   1.016/ 44|   1.010/ 70|   1.009/ 81|   1.007/ 97 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  57   |     753|      133.45|   1.045/ 15|   1.035/ 20|   1.033/ 21|   1.030/ 23 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  59   |     538|      180.66|   1.038/ 18|   1.034/ 20|   1.032/ 21|   1.031/ 22 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  59   |     612|       99.72|   1.034/ 20|   1.030/ 23|   1.029/ 24|   1.028/ 24 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  51   |      16|       15.08|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  50   |     117|       60.23|   1.037/ 18|   1.035/ 20|   1.035/ 20|   1.034/ 20 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  62   |     360|      116.95|   1.023/ 30|   1.019/ 37|   1.017/ 40|   1.016/ 42 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  55   |     174|      128.31|   1.052/ 13|   1.046/ 15|   1.044/ 16|   1.042/ 16 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  68   |   10891|     1226.15|   1.023/ 30|   1.016/ 43|   1.014/ 48|   1.013/ 54 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  53   |     266|      126.87|   1.048/ 14|   1.043/ 16|   1.042/ 16|   1.041/ 17 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  64   |   28721|     1476.37|   1.010/ 68|   1.007/ 99|   1.006/ **|   1.005/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  53   |     691|       65.90|   1.035/ 20|   1.031/ 22|   1.030/ 23|   1.030/ 23 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  51   |      45|       59.24|   1.044/ 15|   1.036/ 19|   1.033/ 21|   1.031/ 22 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  58   |    1679|      143.65|   1.035/ 20|   1.029/ 24|   1.027/ 26|   1.025/ 27 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  59   |     300|       75.69|   1.016/ 43|   1.010/ 68|   1.009/ 79|   1.007/ 95 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  63   |     143|       33.98|   1.019/ 36|   1.015/ 45|   1.014/ 48|   1.014/ 51 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  59   |    4789|      374.04|   1.039/ 18|   1.031/ 22|   1.029/ 24|   1.026/ 26 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  57   |     123|       38.63|   1.019/ 36|   1.017/ 41|   1.016/ 42|   1.016/ 43 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  50   |     517|      488.18|   1.036/ 19|   1.025/ 27|   1.023/ 30|   1.020/ 35 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  62   |     419|       81.32|   1.029/ 24|   1.020/ 35|   1.018/ 39|   1.015/ 45 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  67   |      51|       57.97|   1.047/ 15|   1.047/ 15|   1.046/ 15|   1.046/ 15 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  57   |     294|       42.96|   1.027/ 26|   1.028/ 25|   1.028/ 25|   1.028/ 24 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  61   |    1327|       45.76|   1.033/ 21|   1.031/ 23|   1.030/ 23|   1.030/ 23 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  56   |      82|       25.45|   1.034/ 20|   1.031/ 22|   1.030/ 23|   1.029/ 24 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  58   |      55|       87.64|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  64   |    1070|      125.33|   1.037/ 19|   1.029/ 24|   1.027/ 26|   1.025/ 28 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  78   |    1029|      135.14|   1.013/ 52|   1.011/ 63|   1.010/ 67|   1.010/ 71 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  48   |      64|       35.55|   1.027/ 25|   1.025/ 28|   1.025/ 28|   1.025/ 28 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  58   |     459|       78.92|   1.023/ 30|   1.021/ 33|   1.020/ 34|   1.020/ 35 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  34   |       7|       12.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  56   |     165|        5.11|   1.054/ 13|   1.048/ 14|   1.046/ 15|   1.045/ 15 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  67   |      32|       11.22|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  66   |     541|       12.58|   1.012/ 56|   1.012/ 57|   1.012/ 57|   1.012/ 57 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  49   |       2|        0.06|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  70   |     377|        8.39|   1.032/ 22|   1.028/ 24|   1.028/ 25|   1.027/ 26 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  52   |      54|       18.31|   1.031/ 22|   1.029/ 24|   1.028/ 24|   1.028/ 25 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  77   |     105|        4.11|   1.005/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  66   |     647|       72.64|   1.005/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  65   |      37|        3.64|   1.028/ 25|   1.029/ 24|   1.029/ 23|   1.030/ 23 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  62   |      10|        6.22|   1.031/ 22|   1.045/ 15|   1.049/ 14|   1.053/ 13 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  60   |     294|        1.74|   1.044/ 15|   1.050/ 14|   1.052/ 13|   1.053/ 13 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  47   |     163|       17.33|   1.039/ 18|   1.035/ 20|   1.034/ 20|   1.034/ 21 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  67   |    9321|      808.77|   1.010/ 67|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  41   |       1|        0.09|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  49   |     171|       14.90|   1.065/ 10|   1.064/ 11|   1.064/ 11|   1.063/ 11 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  57   |     134|       40.72|   1.041/ 17|   1.041/ 17|   1.041/ 17|   1.041/ 17 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  47   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  61   |   16213|       76.69|   1.064/ 11|   1.059/ 12|   1.057/ 12|   1.056/ 12 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  67   |     109|       15.66|   1.028/ 24|   1.024/ 29|   1.023/ 30|   1.022/ 32 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  60   |      52|        2.51|   1.010/ 72|   1.008/ 90|   1.007/ 96|   1.007/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  34   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  53   |     156|        5.88|   1.030/ 23|   1.033/ 21|   1.034/ 20|   1.035/ 20 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  69   |    6340|      166.84|   1.034/ 20|   1.024/ 29|   1.022/ 32|   1.019/ 36 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  19   |      52|        3.20|   1.114/  6|   1.086/  8|   1.082/  8|   1.075/  9 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  56   |     397|       20.80|   1.038/ 18|   1.039/ 17|   1.040/ 17|   1.040/ 17 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  67   |    4637|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  56   |     582|       11.79|   1.040/ 17|   1.035/ 19|   1.034/ 20|   1.033/ 21 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  59   |       8|        1.57|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  59   |     102|       24.98|   1.019/ 36|   1.009/ 77|   1.006/ **|   1.004/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  60   |      85|        7.56|   1.015/ 45|   1.006/ **|   1.003/ **|   1.001/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  64   |     565|       97.02|   1.010/ 70|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  61   |     442|       42.66|   1.021/ 33|   1.018/ 38|   1.018/ 39|   1.017/ 41 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  64   |    2966|      169.77|   1.055/ 13|   1.049/ 14|   1.047/ 14|   1.046/ 15 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  70   |     633|        6.31|   1.028/ 24|   1.023/ 30|   1.022/ 31|   1.021/ 33 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  47   |      26|        3.93|   1.064/ 11|   1.067/ 10|   1.068/ 10|   1.069/ 10 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  25   |       7|        5.48|   1.097/  7|   1.184/  4|   1.208/  3|   1.232/  3 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  42   |       5|        0.06|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  57   |     303|       54.78|   1.021/ 34|   1.016/ 43|   1.015/ 46|   1.014/ 50 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  92   |   29595|      441.22|   1.005/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  58   |      12|        5.34|   1.000/ --|   1.036/ 19|   1.036/ 19|   1.069/ 10 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  55   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  43   |      12|        3.34|   1.033/ 21|   1.029/ 24|   1.028/ 24|   1.028/ 25 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  69   |    8322|      100.09|   1.011/ 62|   1.006/ **|   1.005/ **|   1.003/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  57   |      27|        0.90|   1.039/ 18|   1.044/ 16|   1.045/ 15|   1.047/ 15 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  67   |     161|       15.02|   1.009/ 79|   1.007/ 99|   1.007/ **|   1.006/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  62   |      33|        1.99|   1.043/ 16|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  32   |      15|        1.26|   1.044/ 16|   1.063/ 11|   1.070/ 10|   1.078/  9 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  21   |       3|        1.87|   1.145/  5|   1.036/ 19|   1.029/ 24|   1.025/ 28 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  42   |      22|        1.86|   1.070/ 10|   1.061/ 11|   1.059/ 12|   1.057/ 12 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  52   |     143|       15.62|   1.043/ 16|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  63   |     472|       48.30|   1.022/ 32|   1.015/ 46|   1.013/ 52|   1.012/ 60 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  67   |    3104|        2.28|   1.057/ 12|   1.051/ 13|   1.049/ 14|   1.048/ 14 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  67   |    1102|        4.13|   1.019/ 36|   1.017/ 41|   1.016/ 42|   1.016/ 44 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  87   |    7134|       85.56|   1.009/ 81|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  74   |     119|        3.03|   1.016/ 42|   1.017/ 40|   1.018/ 39|   1.018/ 39 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  67   |    1650|      335.36|   1.013/ 53|   1.005/ **|   1.003/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  57   |     273|       29.72|   1.013/ 55|   1.010/ 69|   1.009/ 73|   1.009/ 78 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  86   |   32877|      545.79|   1.007/ 94|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  59   |      10|        3.50|   1.007/ 96|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  94   |     868|        6.89|   1.031/ 22|   1.022/ 31|   1.020/ 34|   1.018/ 38 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  51   |       9|        0.87|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  53   |      34|        1.84|   1.017/ 42|   1.014/ 48|   1.014/ 50|   1.013/ 53 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  52   |      47|        0.99|   1.062/ 11|   1.068/ 10|   1.070/ 10|   1.071/ 10 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  52   |      33|       18.18|   1.009/ 75|   1.011/ 66|   1.011/ 65|   1.011/ 64 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  43   |     103|       23.22|   1.091/  7|   1.102/  7|   1.105/  6|   1.108/  6 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  44   |      14|        2.12|   1.028/ 25|   1.019/ 37|   1.016/ 43|   1.014/ 50 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  44   |      19|       10.20|   1.015/ 47|   1.009/ 81|   1.007/ 97|   1.006/ ** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  68   |      27|        3.92|   1.004/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  43   |      20|        4.58|   1.010/ 67|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  45   |       3|        0.45|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  57   |      55|       19.53|   1.014/ 48|   1.015/ 47|   1.015/ 47|   1.015/ 46 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  61   |     113|        3.46|   1.007/ **|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  49   |      48|        2.39|   1.042/ 16|   1.045/ 15|   1.045/ 15|   1.046/ 15 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  48   |       1|        0.25|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  59   |    5138|       40.59|   1.066/ 10|   1.064/ 11|   1.063/ 11|   1.062/ 11 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  60   |     210|       78.35|   1.039/ 18|   1.037/ 19|   1.036/ 19|   1.036/ 19 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  68   |     197|        5.49|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  72   |    5921|      339.20|   1.010/ 71|   1.006/ **|   1.005/ **|   1.004/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  49   |      21|        4.29|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  51   |       8|        1.31|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  53   |      53|        2.39|   1.029/ 24|   1.024/ 29|   1.023/ 31|   1.021/ 32 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  55   |     205|        1.00|   1.066/ 10|   1.046/ 15|   1.041/ 17|   1.036/ 19 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  56   |     101|       48.71|   1.015/ 46|   1.007/ 98|   1.005/ **|   1.003/ ** |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  64   |     233|       43.50|   1.007/ 96|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  47   |      21|        4.41|   1.040/ 17|   1.041/ 17|   1.041/ 17|   1.041/ 17 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  59   |     906|        4.13|   1.050/ 14|   1.041/ 17|   1.039/ 18|   1.036/ 19 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  67   |     281|       66.52|   1.023/ 29|   1.019/ 36|   1.018/ 38|   1.017/ 40 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  57   |      11|        1.52|   1.010/ 67|   1.011/ 61|   1.012/ 58|   1.012/ 56 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  58   |    2651|       82.51|   1.056/ 12|   1.047/ 15|   1.044/ 16|   1.042/ 16 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 105   |     907|        8.36|   1.021/ 32|   1.018/ 39|   1.017/ 41|   1.016/ 43 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  66   |     952|       24.81|   1.024/ 29|   1.018/ 38|   1.017/ 41|   1.015/ 45 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  61   |    1233|      120.02|   1.012/ 58|   1.008/ 91|   1.007/ **|   1.006/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  50   |      15|        5.40|   1.018/ 39|   1.016/ 44|   1.015/ 46|   1.014/ 48 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  56   |    1126|       58.01|   1.026/ 26|   1.022/ 32|   1.021/ 33|   1.020/ 35 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  59   |    2691|       18.34|   1.056/ 12|   1.045/ 15|   1.042/ 16|   1.039/ 18 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  54   |     308|        9.00|   1.039/ 18|   1.037/ 19|   1.036/ 19|   1.035/ 19 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  46   |      26|        1.62|   1.075/  9|   1.084/  8|   1.085/  8|   1.087/  8 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  58   |     246|       35.39|   1.013/ 52|   1.013/ 54|   1.012/ 56|   1.012/ 57 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  24   |      29|        3.71|   1.090/  8|   1.084/  8|   1.090/  8|   1.095/  7 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  57   |      23|        4.04|   1.019/ 35|   1.009/ 73|   1.007/ **|   1.004/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  50   |      28|        5.18|   1.012/ 56|   1.005/ **|   1.004/ **|   1.002/ ** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  64   |     108|       51.37|   1.008/ 90|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  39   |      58|        3.67|   1.044/ 16|   1.021/ 33|   1.014/ 49|   1.007/ 93 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  51   |     265|        4.50|   1.056/ 12|   1.053/ 13|   1.053/ 13|   1.052/ 13 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  75   |   28274|      600.29|   1.007/ 95|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  50   |      10|        0.44|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  65   |     109|        2.57|   1.082/  8|   1.075/  9|   1.073/  9|   1.071/ 10 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  67   |    3779|      365.55|   1.023/ 29|   1.019/ 36|   1.018/ 38|   1.017/ 40 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  73   |    1944|      225.94|   1.005/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  49   |       3|        0.17|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  47   |      23|        0.41|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  77   |      58|        0.87|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  51   |      12|        1.56|   1.011/ 64|   1.011/ 62|   1.011/ 63|   1.011/ 64 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  53   |       8|        5.87|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  59   |      46|        3.96|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  61   |    4222|       50.78|   1.016/ 44|   1.010/ 67|   1.009/ 77|   1.008/ 90 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  78   |   94902|      287.98|   1.020/ 34|   1.013/ 51|   1.012/ 58|   1.010/ 67 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  65   |     503|       12.01|   1.042/ 16|   1.039/ 18|   1.038/ 18|   1.038/ 18 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  58   |     250|       25.30|   1.043/ 16|   1.025/ 27|   1.020/ 34|   1.015/ 45 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  67   |   36948|      556.15|   1.017/ 41|   1.011/ 65|   1.009/ 77|   1.007/ 94 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  49   |      20|        5.56|   1.011/ 65|   1.006/ **|   1.004/ **|   1.003/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  51   |      11|        0.32|   1.014/ 49|   1.011/ 63|   1.010/ 67|   1.010/ 70 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  51   |      10|        0.31|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  45   |       8|        0.46|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  55   |       4|        0.26|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |

