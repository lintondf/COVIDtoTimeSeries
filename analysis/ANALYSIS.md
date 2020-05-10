# State and Country COVID-19 Analysis #
## Updated: 2020-05-10 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  57   |   27307|     1403.69|   1.016/ 44|   1.009/ 76|   1.008/ 91|   1.006/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  61   |    9701|     1092.22|   1.034/ 20|   1.024/ 28|   1.022/ 31|   1.020/ 35 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  51   |    5120|      736.68|   1.045/ 15|   1.029/ 24|   1.025/ 27|   1.022/ 32 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  52   |    4702|      470.82|   1.026/ 26|   1.017/ 41|   1.014/ 48|   1.012/ 57 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  52   |    3907|      305.17|   1.057/ 12|   1.054/ 13|   1.053/ 13|   1.053/ 13 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  54   |    3423|      270.11|   1.045/ 15|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  52   |    3076|      862.77|   1.037/ 19|   1.025/ 28|   1.022/ 31|   1.019/ 35 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  67   |    2889|       73.11|   1.037/ 19|   1.026/ 26|   1.024/ 29|   1.021/ 33 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  57   |    2349|      505.24|   1.024/ 29|   1.017/ 41|   1.015/ 45|   1.014/ 50 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  63   |    1753|       81.63|   1.037/ 18|   1.032/ 22|   1.030/ 23|   1.029/ 24 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  71   |   85710|      260.09|   1.029/ 24|   1.017/ 41|   1.014/ 49|   1.011/ 61 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  60   |   34182|      514.52|   1.028/ 25|   1.021/ 33|   1.019/ 36|   1.017/ 41 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  79   |   31636|      525.17|   1.011/ 65|   1.007/ 95|   1.006/ **|   1.006/ ** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  68   |   27294|      579.48|   1.011/ 64|   1.007/ 93|   1.007/ **|   1.006/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  85   |   29250|      436.07|   1.008/ 83|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  54   |   10857|       51.36|   1.074/  9|   1.069/ 10|   1.067/ 10|   1.066/ 10 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  60   |    8911|      773.22|   1.017/ 40|   1.010/ 66|   1.009/ 79|   1.007/ 96 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  62   |    7951|       95.62|   1.020/ 35|   1.012/ 58|   1.010/ 69|   1.008/ 84 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  80   |    6791|       81.45|   1.011/ 62|   1.009/ 79|   1.008/ 85|   1.008/ 91 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  65   |    5656|      324.00|   1.016/ 43|   1.011/ 65|   1.009/ 74|   1.008/ 87 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  46   |     389|       79.41|   1.046/ 15|   1.050/ 14|   1.051/ 14|   1.052/ 13 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  46   |      10|       13.37|   1.009/ 76|   1.017/ 42|   1.019/ 37|   1.021/ 33 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  50   |     495|       67.96|   1.055/ 12|   1.063/ 11|   1.065/ 10|   1.068/ 10 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  47   |      96|       31.85|   1.045/ 15|   1.041/ 17|   1.039/ 18|   1.037/ 18 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  67   |    2889|       73.11|   1.037/ 19|   1.026/ 26|   1.024/ 29|   1.021/ 33 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  57   |    1050|      182.26|   1.033/ 21|   1.020/ 35|   1.017/ 41|   1.014/ 51 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  52   |    3076|      862.77|   1.037/ 19|   1.025/ 28|   1.022/ 31|   1.019/ 35 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  45   |     228|      234.53|   1.052/ 13|   1.039/ 18|   1.035/ 19|   1.032/ 21 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  63   |    1753|       81.63|   1.037/ 18|   1.032/ 22|   1.030/ 23|   1.029/ 24 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  59   |    1475|      138.97|   1.031/ 22|   1.025/ 28|   1.023/ 30|   1.021/ 32 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  40   |      18|       12.47|   1.018/ 38|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  45   |      69|       38.54|   1.015/ 45|   1.009/ 77|   1.007/ 93|   1.006/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  54   |    3423|      270.11|   1.045/ 15|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  55   |    1542|      229.10|   1.049/ 14|   1.046/ 15|   1.045/ 15|   1.044/ 16 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  46   |     260|       82.54|   1.061/ 11|   1.055/ 13|   1.053/ 13|   1.051/ 13 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  58   |     177|       60.78|   1.028/ 25|   1.022/ 31|   1.021/ 32|   1.020/ 34 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  55   |     312|       69.81|   1.031/ 22|   1.026/ 27|   1.024/ 28|   1.023/ 30 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  57   |    2349|      505.24|   1.024/ 29|   1.017/ 41|   1.015/ 45|   1.014/ 50 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  44   |      65|       48.56|   1.024/ 29|   1.017/ 41|   1.015/ 46|   1.014/ 51 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  52   |    1699|      280.97|   1.049/ 14|   1.037/ 19|   1.034/ 20|   1.031/ 22 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  51   |    5120|      736.68|   1.045/ 15|   1.029/ 24|   1.025/ 27|   1.022/ 32 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  52   |    4702|      470.82|   1.026/ 26|   1.017/ 41|   1.014/ 48|   1.012/ 57 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  50   |     593|      105.11|   1.065/ 11|   1.050/ 14|   1.046/ 15|   1.042/ 16 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  52   |     417|      140.12|   1.052/ 13|   1.056/ 12|   1.057/ 12|   1.058/ 12 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  52   |     494|       80.53|   1.043/ 16|   1.038/ 18|   1.038/ 18|   1.037/ 19 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  44   |      17|       15.46|   1.010/ 72|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  43   |      95|       48.95|   1.049/ 14|   1.038/ 18|   1.035/ 19|   1.033/ 21 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  55   |     315|      102.34|   1.033/ 21|   1.029/ 24|   1.028/ 24|   1.027/ 25 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  48   |     123|       90.15|   1.067/ 10|   1.079/  9|   1.082/  8|   1.085/  8 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  61   |    9701|     1092.22|   1.034/ 20|   1.024/ 28|   1.022/ 31|   1.020/ 35 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  46   |     199|       95.02|   1.057/ 12|   1.044/ 16|   1.041/ 17|   1.037/ 18 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  57   |   27307|     1403.69|   1.016/ 44|   1.009/ 76|   1.008/ 91|   1.006/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  46   |     559|       53.32|   1.043/ 16|   1.036/ 19|   1.034/ 20|   1.033/ 21 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  44   |      34|       45.11|   1.059/ 12|   1.063/ 11|   1.064/ 11|   1.065/ 11 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  51   |    1391|      119.02|   1.048/ 14|   1.041/ 17|   1.039/ 17|   1.038/ 18 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  52   |     278|       70.21|   1.027/ 26|   1.020/ 34|   1.019/ 37|   1.017/ 40 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  56   |     128|       30.29|   1.027/ 26|   1.025/ 28|   1.024/ 29|   1.023/ 29 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  52   |    3907|      305.17|   1.057/ 12|   1.054/ 13|   1.053/ 13|   1.053/ 13 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  50   |     110|       34.49|   1.024/ 29|   1.017/ 40|   1.016/ 44|   1.014/ 49 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  43   |     426|      402.23|   1.051/ 13|   1.049/ 14|   1.049/ 14|   1.048/ 14 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  55   |     361|       70.03|   1.048/ 14|   1.040/ 17|   1.038/ 18|   1.036/ 19 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  60   |      34|       38.32|   1.063/ 11|   1.069/ 10|   1.071/ 10|   1.072/  9 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  50   |     249|       36.41|   1.025/ 28|   1.023/ 30|   1.022/ 31|   1.022/ 31 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  54   |    1086|       37.44|   1.037/ 19|   1.032/ 21|   1.031/ 22|   1.030/ 23 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  49   |      64|       20.05|   1.041/ 17|   1.038/ 18|   1.038/ 18|   1.038/ 18 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  51   |      55|       88.24|   1.013/ 52|   1.007/ **|   1.005/ **|   1.003/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  57   |     873|      102.31|   1.051/ 13|   1.042/ 16|   1.040/ 17|   1.038/ 18 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  71   |     945|      124.15|   1.016/ 42|   1.012/ 55|   1.012/ 60|   1.011/ 65 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  41   |      55|       30.78|   1.037/ 19|   1.022/ 32|   1.017/ 40|   1.013/ 53 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  51   |     397|       68.22|   1.028/ 25|   1.026/ 27|   1.025/ 27|   1.025/ 28 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  27   |       7|       12.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  49   |     120|        3.73|   1.067/ 10|   1.065/ 11|   1.064/ 11|   1.064/ 11 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  60   |      32|       11.34|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  59   |     499|       11.60|   1.012/ 58|   1.009/ 75|   1.009/ 81|   1.008/ 87 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  42   |       2|        0.06|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  63   |     312|        6.95|   1.038/ 18|   1.033/ 21|   1.032/ 22|   1.031/ 23 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  45   |      45|       15.10|   1.036/ 19|   1.036/ 19|   1.036/ 19|   1.036/ 19 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  70   |     105|        4.09|   1.015/ 46|   1.010/ 69|   1.009/ 80|   1.007/ 96 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  59   |     642|       72.10|   1.010/ 66|   1.004/ **|   1.002/ **|   1.000/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  58   |      30|        2.95|   1.025/ 28|   1.024/ 28|   1.024/ 28|   1.025/ 28 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  55   |       8|        5.29|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  53   |     216|        1.28|   1.033/ 21|   1.021/ 33|   1.018/ 38|   1.016/ 44 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  40   |     127|       13.55|   1.046/ 15|   1.039/ 18|   1.037/ 18|   1.036/ 19 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  60   |    8911|      773.22|   1.017/ 40|   1.010/ 66|   1.009/ 79|   1.007/ 96 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  34   |       2|        0.20|   1.133/  5|   1.018/ 38|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  42   |     112|        9.80|   1.068/ 10|   1.075/  9|   1.077/  9|   1.079/  9 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  50   |      97|       29.24|   1.042/ 17|   1.049/ 14|   1.051/ 13|   1.053/ 13 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  40   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  54   |   10857|       51.36|   1.074/  9|   1.069/ 10|   1.067/ 10|   1.066/ 10 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  60   |      92|       13.23|   1.036/ 19|   1.033/ 21|   1.033/ 21|   1.032/ 22 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  53   |      49|        2.35|   1.012/ 56|   1.010/ 71|   1.009/ 75|   1.009/ 79 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  27   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  46   |     105|        3.94|   1.068/ 10|   1.090/  8|   1.097/  7|   1.104/  7 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  62   |    5308|      139.69|   1.050/ 14|   1.036/ 19|   1.032/ 21|   1.029/ 24 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  12   |      32|        2.00|   1.260/  3|   1.392/  2|   1.181/  4|   1.222/  3 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  49   |     316|       16.52|   1.038/ 18|   1.030/ 23|   1.028/ 25|   1.025/ 27 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  60   |    4637|        3.31|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  49   |     450|        9.11|   1.047/ 15|   1.046/ 15|   1.046/ 15|   1.046/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  52   |       6|        1.20|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  52   |      94|       23.13|   1.034/ 20|   1.025/ 27|   1.023/ 30|   1.020/ 34 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  53   |      80|        7.11|   1.031/ 22|   1.018/ 39|   1.014/ 49|   1.011/ 65 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  57   |     539|       92.49|   1.018/ 38|   1.015/ 45|   1.015/ 48|   1.014/ 50 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  54   |     390|       37.63|   1.026/ 26|   1.025/ 27|   1.025/ 27|   1.025/ 27 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  57   |    1981|      113.43|   1.063/ 11|   1.060/ 11|   1.059/ 12|   1.057/ 12 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  63   |     537|        5.35|   1.037/ 19|   1.031/ 22|   1.029/ 23|   1.028/ 25 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  40   |      17|        2.63|   1.059/ 12|   1.067/ 10|   1.068/ 10|   1.070/ 10 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  18   |       4|        3.24|   1.309/  2|   1.442/  1|   1.442/  1|   1.442/  1 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  35   |       4|        0.04|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  50   |     278|       50.36|   1.029/ 23|   1.022/ 32|   1.020/ 34|   1.018/ 38 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  85   |   29250|      436.07|   1.008/ 83|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  51   |       8|        3.68|   1.119/  6|   1.104/  6|   1.101/  7|   1.097/  7 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  48   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  36   |      10|        2.81|   1.049/ 14|   1.038/ 18|   1.034/ 20|   1.029/ 24 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  62   |    7951|       95.62|   1.020/ 35|   1.012/ 58|   1.010/ 69|   1.008/ 84 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  50   |      22|        0.72|   1.028/ 25|   1.020/ 34|   1.018/ 38|   1.016/ 44 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  60   |     155|       14.48|   1.011/ 63|   1.007/ **|   1.005/ **|   1.004/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  55   |      25|        1.52|   1.057/ 12|   1.046/ 15|   1.043/ 16|   1.041/ 17 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  25   |      12|        0.98|   1.044/ 16|   1.047/ 15|   1.044/ 15|   1.040/ 17 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  14   |       3|        1.77|   1.000/ --|   1.260/  2|   1.260/  2|   1.145/  5 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  35   |      14|        1.17|   1.071/ 10|   1.054/ 13|   1.049/ 14|   1.042/ 16 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  45   |     111|       12.17|   1.052/ 13|   1.053/ 13|   1.054/ 13|   1.054/ 13 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  56   |     420|       43.00|   1.033/ 21|   1.024/ 29|   1.022/ 32|   1.019/ 36 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  60   |    2143|        1.57|   1.069/ 10|   1.069/ 10|   1.069/ 10|   1.069/ 10 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  60   |     984|        3.69|   1.023/ 30|   1.018/ 38|   1.017/ 41|   1.016/ 44 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  80   |    6791|       81.45|   1.011/ 62|   1.009/ 79|   1.008/ 85|   1.008/ 91 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  67   |     105|        2.69|   1.014/ 49|   1.015/ 46|   1.015/ 45|   1.016/ 44 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  60   |    1628|      330.73|   1.029/ 24|   1.012/ 59|   1.007/ 94|   1.003/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  50   |     252|       27.48|   1.016/ 44|   1.011/ 61|   1.010/ 68|   1.009/ 77 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  79   |   31636|      525.17|   1.011/ 65|   1.007/ 95|   1.006/ **|   1.006/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  52   |      10|        3.56|   1.024/ 28|   1.014/ 50|   1.011/ 63|   1.008/ 85 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  87   |     729|        5.79|   1.046/ 15|   1.038/ 18|   1.035/ 19|   1.033/ 21 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  44   |       9|        0.89|   1.016/ 44|   1.009/ 74|   1.007/ 96|   1.005/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  46   |      31|        1.68|   1.023/ 30|   1.021/ 33|   1.020/ 34|   1.020/ 34 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  45   |      31|        0.65|   1.049/ 14|   1.062/ 11|   1.065/ 11|   1.067/ 10 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  45   |      31|       17.50|   1.020/ 34|   1.030/ 23|   1.032/ 21|   1.034/ 20 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  36   |      52|       11.73|   1.079/  9|   1.059/ 12|   1.053/ 13|   1.046/ 15 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  37   |      13|        1.93|   1.037/ 18|   1.051/ 13|   1.055/ 12|   1.058/ 12 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  37   |      19|        9.75|   1.032/ 22|   1.022/ 32|   1.019/ 36|   1.016/ 42 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  61   |      26|        3.84|   1.009/ 80|   1.008/ 92|   1.007/ 96|   1.007/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  36   |      21|        4.79|   1.052/ 13|   1.014/ 50|   1.005/ **|   1.000/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  38   |       3|        0.47|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  50   |      50|       17.89|   1.014/ 48|   1.011/ 62|   1.010/ 67|   1.010/ 72 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  54   |     110|        3.35|   1.008/ 87|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  42   |      36|        1.76|   1.038/ 18|   1.041/ 17|   1.042/ 16|   1.043/ 16 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  41   |       1|        0.25|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  52   |    3465|       27.38|   1.076/  9|   1.069/ 10|   1.068/ 10|   1.067/ 10 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  53   |     162|       60.54|   1.041/ 17|   1.033/ 21|   1.031/ 22|   1.029/ 24 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  61   |     191|        5.31|   1.012/ 56|   1.009/ 75|   1.008/ 81|   1.008/ 89 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  65   |    5656|      324.00|   1.016/ 43|   1.011/ 65|   1.009/ 74|   1.008/ 87 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  42   |      22|        4.32|   1.012/ 56|   1.008/ 88|   1.007/ **|   1.006/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  44   |       5|        0.85|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  46   |      45|        2.01|   1.040/ 17|   1.037/ 18|   1.037/ 19|   1.037/ 19 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  48   |     138|        0.67|   1.091/  7|   1.079/  9|   1.076/  9|   1.072/  9 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  49   |      97|       46.54|   1.028/ 24|   1.021/ 33|   1.019/ 37|   1.016/ 43 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  57   |     225|       41.86|   1.008/ 87|   1.002/ **|   1.000/ **|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  40   |      16|        3.39|   1.041/ 17|   1.061/ 11|   1.066/ 10|   1.071/ 10 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  52   |     669|        3.05|   1.066/ 10|   1.058/ 12|   1.056/ 12|   1.054/ 13 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  60   |     242|       57.48|   1.031/ 22|   1.026/ 26|   1.025/ 27|   1.024/ 29 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  50   |      10|        1.45|   1.008/ 87|   1.003/ **|   1.002/ **|   1.000/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  51   |    1919|       59.71|   1.073/  9|   1.063/ 11|   1.060/ 11|   1.057/ 12 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  98   |     829|        7.64|   1.025/ 28|   1.019/ 36|   1.018/ 39|   1.016/ 42 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  59   |     841|       21.91|   1.033/ 21|   1.023/ 30|   1.020/ 34|   1.017/ 40 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  54   |    1170|      113.83|   1.019/ 36|   1.013/ 55|   1.011/ 63|   1.009/ 74 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  43   |      13|        4.66|   1.016/ 43|   1.014/ 48|   1.014/ 51|   1.013/ 54 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  49   |     961|       49.54|   1.034/ 20|   1.029/ 24|   1.028/ 25|   1.027/ 26 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  52   |    1965|       13.39|   1.075/  9|   1.059/ 12|   1.055/ 13|   1.050/ 14 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  47   |     238|        6.94|   1.044/ 16|   1.043/ 16|   1.043/ 16|   1.043/ 16 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  39   |      14|        0.86|   1.053/ 13|   1.072/  9|   1.079/  9|   1.086/  8 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  51   |     227|       32.54|   1.014/ 48|   1.018/ 37|   1.020/ 35|   1.021/ 33 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  17   |      19|        2.42|   1.133/  5|   1.159/  4|   1.147/  5|   1.129/  5 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  50   |      21|        3.71|   1.036/ 19|   1.035/ 19|   1.035/ 20|   1.034/ 20 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  43   |      28|        5.09|   1.030/ 23|   1.014/ 51|   1.009/ 73|   1.005/ ** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  57   |     104|       49.68|   1.015/ 46|   1.010/ 67|   1.009/ 74|   1.008/ 84 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  32   |      47|        2.98|   1.056/ 12|   1.066/ 10|   1.069/ 10|   1.072/  9 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  44   |     185|        3.15|   1.061/ 11|   1.062/ 11|   1.062/ 11|   1.062/ 11 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  68   |   27294|      579.48|   1.011/ 64|   1.007/ 93|   1.007/ **|   1.006/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  43   |       9|        0.42|   1.014/ 50|   1.021/ 33|   1.023/ 30|   1.025/ 28 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  58   |      68|        1.60|   1.095/  7|   1.094/  7|   1.094/  7|   1.093/  7 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  60   |    3349|      323.95|   1.031/ 22|   1.023/ 30|   1.021/ 33|   1.019/ 37 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  66   |    1923|      223.53|   1.010/ 70|   1.004/ **|   1.002/ **|   1.001/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  42   |       3|        0.17|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  40   |      20|        0.36|   1.041/ 17|   1.042/ 16|   1.042/ 16|   1.042/ 16 |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  70   |      58|        0.87|   1.006/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  44   |      10|        1.38|   1.017/ 41|   1.019/ 37|   1.019/ 36|   1.019/ 36 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  46   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  52   |      45|        3.83|   1.011/ 62|   1.013/ 53|   1.013/ 51|   1.014/ 50 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  54   |    3942|       47.40|   1.025/ 28|   1.015/ 47|   1.012/ 56|   1.010/ 70 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  71   |   85710|      260.09|   1.029/ 24|   1.017/ 41|   1.014/ 49|   1.011/ 61 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  58   |     384|        9.17|   1.046/ 15|   1.040/ 17|   1.038/ 18|   1.037/ 19 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  51   |     194|       19.66|   1.074/  9|   1.064/ 11|   1.062/ 11|   1.059/ 12 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  60   |   34182|      514.52|   1.028/ 25|   1.021/ 33|   1.019/ 36|   1.017/ 41 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  42   |      18|        5.22|   1.021/ 33|   1.007/ **|   1.003/ **|   1.000/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  44   |      11|        0.31|   1.022/ 31|   1.009/ 81|   1.005/ **|   1.002/ ** |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  44   |      10|        0.31|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  38   |       4|        0.21|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  48   |       4|        0.27|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |

