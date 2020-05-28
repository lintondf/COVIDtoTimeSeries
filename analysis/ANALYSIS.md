# State and Country COVID-19 Analysis #
## Updated: 2020-05-28 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# Notes #

- Expect discontinuities in the US around 4/14/2020 as the [CDC](CDC "https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html")  expanded the definition of a COVID-19 death.  
- There is also some weekly pattern to reporting with lower values on the weekend followed by higher values subsequently, at least in some places.
- The Y axis upper limit for DDGR charts was lowered from 2.0 to 1.5 on 4/28 and then to 1.25 on 5/26/20 to better show current lower values.  

# Ten US States with Highest Death Tolls #

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. One per million is 0.0001%.  1% is 10,000 per million.

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDeathRates.png)

Daily Death Growth Rate (DDGR) in the 10 US States with the highest death tolls.

DDGR is the cube root of Arnold Kling's [Three Day Death Reproduction Rate (3DDRR)](http://www.arnoldkling.com/blog/the-3ddrr/).  The 3DDRR is calculated by dividing the cumulative total number of deaths on a given day by the  cumulative total number of deaths three days previously.  Taking the cube root converts this to the geometric mean for the three days.  These values are LOWESS filtered to generate a local-error minimizing non-parametric trend.

If deaths remain constant over the three days, the DDGR equals one.  A value of 2 would indicate that the number of deaths doubles every day.

![US States with Highest Death Toll - Daily Death Growth Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  75   |   30066|     1545.52|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  79   |   11975|     1348.24|   1.010/ 67|   1.006/ **|   1.004/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  69   |    6873|      988.97|   1.015/ 46|   1.010/ 71|   1.008/ 82|   1.007/ 98 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  70   |    5448|      545.50|   1.009/ 81|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  70   |    5625|      439.39|   1.017/ 39|   1.010/ 69|   1.008/ 84|   1.006/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  72   |    5371|      423.85|   1.022/ 32|   1.016/ 43|   1.015/ 47|   1.013/ 51 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  85   |    4129|      104.49|   1.019/ 36|   1.015/ 45|   1.014/ 48|   1.013/ 52 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  70   |    3958|     1110.15|   1.014/ 50|   1.010/ 70|   1.009/ 77|   1.008/ 87 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  75   |    2819|      606.48|   1.009/ 75|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  70   |    2506|      414.49|   1.020/ 34|   1.015/ 46|   1.014/ 51|   1.012/ 57 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  89   |  106249|      322.41|   1.012/ 58|   1.008/ 85|   1.007/ 96|   1.006/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  78   |   39143|      589.18|   1.009/ 81|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  97   |   34076|      565.68|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 103   |   29965|      446.73|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  86   |   28776|      610.95|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  72   |   27192|      128.62|   1.049/ 14|   1.043/ 16|   1.042/ 16|   1.041/ 17 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  78   |    9624|      835.14|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  70   |    8931|       70.56|   1.053/ 13|   1.048/ 14|   1.047/ 15|   1.046/ 15 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  80   |    8651|      104.04|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  98   |    7680|       92.12|   1.007/ 95|   1.006/ **|   1.006/ **|   1.006/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  64   |     612|      124.83|   1.021/ 33|   1.015/ 46|   1.014/ 51|   1.012/ 57 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  64   |      10|       13.81|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  68   |     910|      125.04|   1.025/ 28|   1.016/ 43|   1.014/ 50|   1.012/ 60 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  65   |     121|       40.25|   1.017/ 42|   1.014/ 49|   1.014/ 51|   1.013/ 52 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  85   |    4129|      104.49|   1.019/ 36|   1.015/ 45|   1.014/ 48|   1.013/ 52 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  75   |    1451|      251.92|   1.017/ 40|   1.014/ 48|   1.014/ 51|   1.013/ 55 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  70   |    3958|     1110.15|   1.014/ 50|   1.010/ 70|   1.009/ 77|   1.008/ 87 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  63   |     363|      373.07|   1.022/ 31|   1.016/ 43|   1.014/ 48|   1.013/ 55 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  81   |    2443|      113.75|   1.017/ 42|   1.012/ 56|   1.011/ 61|   1.010/ 67 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  77   |    1968|      185.35|   1.017/ 41|   1.014/ 48|   1.014/ 50|   1.013/ 52 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  58   |      17|       12.01|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  63   |      81|       45.51|   1.009/ 75|   1.008/ 82|   1.008/ 84|   1.008/ 86 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  72   |    5371|      423.85|   1.022/ 32|   1.016/ 43|   1.015/ 47|   1.013/ 51 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  73   |    2161|      320.94|   1.016/ 43|   1.010/ 69|   1.008/ 82|   1.007/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  64   |     512|      162.29|   1.036/ 19|   1.031/ 22|   1.030/ 23|   1.029/ 24 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  76   |     222|       76.32|   1.010/ 71|   1.006/ **|   1.005/ **|   1.003/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  73   |     416|       93.17|   1.014/ 48|   1.011/ 61|   1.011/ 65|   1.010/ 71 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  75   |    2819|      606.48|   1.009/ 75|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  62   |      81|       59.91|   1.013/ 53|   1.013/ 55|   1.013/ 55|   1.012/ 56 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  70   |    2506|      414.49|   1.020/ 34|   1.015/ 46|   1.014/ 51|   1.012/ 57 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  69   |    6873|      988.97|   1.015/ 46|   1.010/ 71|   1.008/ 82|   1.007/ 98 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  70   |    5448|      545.50|   1.009/ 81|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  68   |     985|      174.68|   1.028/ 25|   1.021/ 32|   1.020/ 35|   1.018/ 38 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  70   |     698|      234.37|   1.026/ 27|   1.021/ 32|   1.020/ 34|   1.019/ 36 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  70   |     754|      122.78|   1.018/ 38|   1.012/ 58|   1.010/ 67|   1.009/ 80 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  62   |      16|       15.27|   1.003/ **|   1.006/ **|   1.006/ **|   1.007/ ** |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  61   |     161|       83.45|   1.027/ 26|   1.022/ 32|   1.020/ 34|   1.019/ 37 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  73   |     416|      135.20|   1.014/ 48|   1.011/ 64|   1.010/ 70|   1.009/ 76 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  66   |     239|      175.93|   1.030/ 23|   1.022/ 32|   1.019/ 35|   1.017/ 40 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  79   |   11975|     1348.24|   1.010/ 67|   1.006/ **|   1.004/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  64   |     352|      167.83|   1.028/ 25|   1.020/ 34|   1.019/ 37|   1.017/ 41 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  75   |   30066|     1545.52|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  64   |     856|       81.58|   1.022/ 32|   1.017/ 40|   1.016/ 43|   1.015/ 46 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  62   |      59|       76.97|   1.026/ 26|   1.020/ 35|   1.018/ 38|   1.016/ 42 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  69   |    2133|      182.45|   1.023/ 29|   1.019/ 35|   1.018/ 37|   1.017/ 40 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  70   |     325|       82.12|   1.010/ 70|   1.008/ 89|   1.007/ 94|   1.007/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  74   |     156|       36.91|   1.008/ 82|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  70   |    5625|      439.39|   1.017/ 39|   1.010/ 69|   1.008/ 84|   1.006/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  68   |     135|       42.12|   1.009/ 81|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  61   |     655|      617.98|   1.025/ 27|   1.023/ 30|   1.022/ 31|   1.022/ 32 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  73   |     472|       91.68|   1.017/ 39|   1.014/ 49|   1.013/ 52|   1.012/ 56 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  78   |      62|       69.79|   1.021/ 32|   1.014/ 49|   1.012/ 57|   1.010/ 68 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  68   |     356|       52.15|   1.019/ 37|   1.017/ 41|   1.017/ 42|   1.016/ 43 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  72   |    1665|       57.43|   1.020/ 34|   1.016/ 43|   1.015/ 46|   1.014/ 50 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  67   |     107|       33.42|   1.026/ 27|   1.022/ 31|   1.021/ 33|   1.020/ 34 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  69   |      55|       87.35|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  75   |    1313|      153.86|   1.024/ 29|   1.019/ 36|   1.018/ 39|   1.017/ 41 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  89   |    1120|      147.14|   1.009/ 80|   1.007/ **|   1.006/ **|   1.006/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  59   |      77|       43.04|   1.015/ 45|   1.010/ 67|   1.009/ 78|   1.007/ 94 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  69   |     542|       93.17|   1.016/ 42|   1.014/ 49|   1.014/ 51|   1.013/ 53 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  45   |      14|       24.55|   1.024/ 28|   1.033/ 21|   1.035/ 20|   1.037/ 19 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  67   |     247|        7.67|   1.036/ 19|   1.029/ 24|   1.027/ 25|   1.025/ 27 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  78   |      32|       11.24|   1.004/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  77   |     622|       14.45|   1.013/ 53|   1.013/ 52|   1.013/ 51|   1.014/ 51 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  60   |       2|        0.06|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  81   |     501|       11.15|   1.029/ 24|   1.027/ 25|   1.027/ 26|   1.027/ 26 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  63   |      92|       30.99|   1.049/ 14|   1.055/ 12|   1.057/ 12|   1.058/ 12 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  88   |     105|        4.09|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  77   |     649|       72.92|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  76   |      53|        5.31|   1.034/ 20|   1.035/ 20|   1.035/ 19|   1.036/ 19 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  73   |      15|        9.48|   1.028/ 24|   1.032/ 21|   1.033/ 21|   1.034/ 20 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  71   |     544|        3.23|   1.053/ 13|   1.056/ 12|   1.057/ 12|   1.057/ 12 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  58   |     219|       23.30|   1.028/ 24|   1.024/ 28|   1.023/ 30|   1.022/ 31 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  78   |    9624|      835.14|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  52   |       2|        0.17|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  60   |     292|       25.45|   1.053/ 13|   1.049/ 14|   1.048/ 14|   1.047/ 15 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  68   |     162|       49.18|   1.019/ 36|   1.011/ 62|   1.009/ 75|   1.007/ 96 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  58   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  72   |   27192|      128.62|   1.049/ 14|   1.043/ 16|   1.042/ 16|   1.041/ 17 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  78   |     139|       20.00|   1.022/ 31|   1.019/ 36|   1.018/ 38|   1.018/ 39 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  71   |      54|        2.56|   1.003/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  45   |       1|        0.09|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  64   |     184|        6.93|   1.024/ 29|   1.022/ 31|   1.022/ 31|   1.022/ 32 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  80   |    7383|      194.30|   1.017/ 40|   1.011/ 63|   1.009/ 74|   1.008/ 88 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  30   |      64|        3.92|   1.025/ 27|   1.016/ 44|   1.014/ 51|   1.012/ 59 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  67   |     808|       42.30|   1.063/ 11|   1.070/ 10|   1.072/  9|   1.074/  9 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  78   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  67   |     808|       16.35|   1.033/ 21|   1.031/ 22|   1.031/ 22|   1.030/ 23 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  70   |      11|        2.22|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  70   |     104|       25.47|   1.006/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  71   |      84|        7.53|   1.004/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  75   |     580|       99.53|   1.004/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  72   |     488|       47.13|   1.010/ 68|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  75   |    3742|      214.21|   1.026/ 27|   1.017/ 40|   1.015/ 46|   1.013/ 53 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  81   |     826|        8.24|   1.026/ 26|   1.025/ 27|   1.025/ 28|   1.024/ 28 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  58   |      41|        6.34|   1.041/ 17|   1.030/ 23|   1.027/ 25|   1.024/ 29 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  36   |      13|        9.57|   1.063/ 11|   1.058/ 12|   1.057/ 12|   1.055/ 13 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  53   |       5|        0.06|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  68   |     324|       58.60|   1.007/ 93|   1.003/ **|   1.002/ **|   1.001/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 103   |   29965|      446.73|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  69   |      15|        6.89|   1.028/ 24|   1.023/ 30|   1.021/ 32|   1.020/ 34 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  66   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  54   |      13|        3.36|   1.006/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  80   |    8651|      104.04|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  68   |      36|        1.19|   1.025/ 28|   1.020/ 34|   1.019/ 36|   1.018/ 39 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  78   |     176|       16.38|   1.007/ 93|   1.007/ **|   1.007/ **|   1.007/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  73   |      65|        3.92|   1.052/ 13|   1.056/ 12|   1.057/ 12|   1.058/ 12 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  43   |      21|        1.75|   1.031/ 22|   1.016/ 43|   1.012/ 56|   1.008/ 83 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  32   |       7|        4.64|   1.080/  8|   1.042/ 16|   1.031/ 22|   1.021/ 33 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  53   |      32|        2.74|   1.049/ 14|   1.049/ 14|   1.050/ 14|   1.050/ 14 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  63   |     195|       21.24|   1.033/ 21|   1.031/ 22|   1.030/ 23|   1.030/ 23 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  74   |     522|       53.46|   1.011/ 60|   1.008/ 91|   1.007/ **|   1.006/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  78   |    4813|        3.54|   1.042/ 16|   1.037/ 19|   1.036/ 19|   1.034/ 20 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  78   |    1456|        5.45|   1.024/ 29|   1.025/ 28|   1.025/ 28|   1.025/ 27 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  98   |    7680|       92.12|   1.007/ 95|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  85   |     161|        4.12|   1.030/ 23|   1.034/ 20|   1.035/ 20|   1.036/ 19 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  78   |    1682|      341.66|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  68   |     290|       31.62|   1.005/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  97   |   34076|      565.68|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  70   |       9|        3.35|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 105   |     988|        7.84|   1.015/ 45|   1.009/ 79|   1.007/ 97|   1.006/ ** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  62   |       9|        0.85|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  64   |      37|        1.99|   1.009/ 81|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  63   |      60|        1.26|   1.024/ 29|   1.011/ 65|   1.007/ 97|   1.004/ ** |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  63   |      30|       16.83|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  54   |     192|       43.40|   1.062/ 11|   1.047/ 15|   1.043/ 16|   1.039/ 17 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  55   |      16|        2.40|   1.019/ 35|   1.022/ 31|   1.023/ 30|   1.024/ 29 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  55   |      23|       12.03|   1.013/ 53|   1.013/ 54|   1.013/ 55|   1.012/ 56 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  79   |      26|        3.87|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  54   |      27|        5.94|   1.020/ 34|   1.026/ 27|   1.027/ 26|   1.028/ 25 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  56   |       3|        0.44|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  68   |      66|       23.71|   1.015/ 45|   1.015/ 45|   1.015/ 45|   1.015/ 45 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  11   |       2|        0.08|   1.193/  3|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  72   |     117|        3.57|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  60   |      73|        3.61|   1.037/ 19|   1.034/ 20|   1.033/ 21|   1.032/ 21 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  59   |      12|        2.97|   1.077/  9|   1.145/  5|   1.294/  2|   1.387/  2 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  70   |    8931|       70.56|   1.053/ 13|   1.048/ 14|   1.047/ 15|   1.046/ 15 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  71   |     281|      104.91|   1.029/ 24|   1.026/ 26|   1.026/ 27|   1.025/ 28 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  79   |     204|        5.67|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  12   |       4|        0.14|   1.107/  6|   1.101/  7|   1.101/  7|   1.101/  7 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  83   |    6072|      347.83|   1.004/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  60   |      21|        4.26|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  62   |      26|        3.98|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  64   |      66|        2.97|   1.019/ 36|   1.015/ 47|   1.014/ 50|   1.013/ 55 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  66   |     269|        1.30|   1.035/ 20|   1.025/ 27|   1.023/ 30|   1.021/ 33 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  67   |     119|       57.24|   1.014/ 48|   1.014/ 50|   1.014/ 51|   1.013/ 51 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  75   |     240|       44.77|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  58   |      41|        8.87|   1.055/ 12|   1.054/ 13|   1.054/ 13|   1.053/ 13 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  70   |    1295|        5.91|   1.036/ 19|   1.031/ 23|   1.029/ 24|   1.028/ 25 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  78   |     328|       77.86|   1.016/ 44|   1.013/ 55|   1.012/ 58|   1.011/ 62 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  68   |      11|        1.58|   1.003/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  69   |    4101|      127.64|   1.043/ 16|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 116   |    1005|        9.26|   1.011/ 62|   1.008/ 91|   1.007/ **|   1.006/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  77   |    1078|       28.09|   1.013/ 53|   1.009/ 76|   1.008/ 85|   1.007/ 96 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  72   |    1362|      132.53|   1.010/ 67|   1.010/ 72|   1.009/ 74|   1.009/ 75 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  61   |      24|        8.72|   1.062/ 11|   1.082/  8|   1.087/  8|   1.093/  7 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  67   |    1275|       65.69|   1.013/ 53|   1.009/ 80|   1.008/ 92|   1.006/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  70   |    4099|       27.93|   1.043/ 16|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  65   |     431|       12.60|   1.032/ 21|   1.030/ 23|   1.029/ 23|   1.029/ 24 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  57   |      41|        2.53|   1.043/ 16|   1.029/ 24|   1.025/ 28|   1.021/ 33 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  69   |     248|       35.59|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  35   |      45|        5.75|   1.047/ 15|   1.037/ 18|   1.036/ 19|   1.034/ 20 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  68   |      24|        4.20|   1.006/ **|   1.002/ **|   1.001/ **|   1.000/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  61   |      29|        5.25|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  75   |     109|       52.17|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  50   |      67|        4.23|   1.020/ 35|   1.019/ 37|   1.018/ 37|   1.018/ 38 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  62   |     525|        8.92|   1.068/ 10|   1.074/  9|   1.076/  9|   1.077/  9 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  86   |   28776|      610.95|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  61   |      10|        0.44|   1.009/ 78|   1.014/ 49|   1.016/ 44|   1.017/ 40 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  76   |     192|        4.53|   1.060/ 11|   1.054/ 13|   1.053/ 13|   1.051/ 13 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  78   |    4329|      418.74|   1.014/ 48|   1.011/ 62|   1.010/ 66|   1.010/ 71 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  84   |    1953|      226.99|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  60   |       4|        0.23|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  58   |      22|        0.39|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  88   |      57|        0.86|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  62   |      13|        1.74|   1.015/ 47|   1.015/ 45|   1.015/ 45|   1.016/ 44 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  64   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  70   |      48|        4.14|   1.004/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  72   |    4545|       54.66|   1.008/ 84|   1.006/ **|   1.005/ **|   1.004/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  89   |  106249|      322.41|   1.012/ 58|   1.008/ 85|   1.007/ 96|   1.006/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  76   |     703|       16.79|   1.029/ 24|   1.025/ 28|   1.023/ 29|   1.022/ 31 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  69   |     274|       27.71|   1.017/ 42|   1.006/ **|   1.003/ **|   1.001/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  78   |   39143|      589.18|   1.009/ 81|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  60   |      22|        6.29|   1.012/ 58|   1.012/ 56|   1.012/ 55|   1.013/ 55 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  62   |      14|        0.41|   1.016/ 42|   1.016/ 42|   1.016/ 43|   1.016/ 43 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  62   |      10|        0.31|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  56   |       8|        0.42|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  66   |       4|        0.26|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |

