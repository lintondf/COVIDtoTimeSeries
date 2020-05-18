# State and Country COVID-19 Analysis #
## Updated: 2020-05-18 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  65   |   28859|     1483.47|   1.010/ 72|   1.007/ **|   1.006/ **|   1.005/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  69   |   11006|     1239.11|   1.021/ 32|   1.015/ 47|   1.013/ 53|   1.012/ 60 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  59   |    6068|      873.10|   1.028/ 24|   1.020/ 34|   1.019/ 37|   1.017/ 41 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  60   |    5086|      509.25|   1.015/ 47|   1.009/ 76|   1.008/ 90|   1.006/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  60   |    4896|      382.46|   1.036/ 19|   1.027/ 26|   1.024/ 28|   1.022/ 32 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  62   |    4383|      345.87|   1.035/ 20|   1.031/ 22|   1.030/ 23|   1.029/ 24 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  60   |    3514|      985.60|   1.023/ 29|   1.018/ 39|   1.017/ 42|   1.015/ 45 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  75   |    3433|       86.89|   1.027/ 25|   1.021/ 32|   1.020/ 35|   1.018/ 37 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  65   |    2574|      553.77|   1.015/ 46|   1.011/ 63|   1.010/ 69|   1.009/ 77 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  60   |    2101|      347.48|   1.034/ 20|   1.026/ 26|   1.025/ 28|   1.023/ 30 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  79   |   95779|      290.64|   1.019/ 36|   1.013/ 55|   1.011/ 62|   1.010/ 72 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  68   |   37304|      561.50|   1.015/ 45|   1.010/ 71|   1.008/ 82|   1.007/ 99 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  87   |   32987|      547.61|   1.007/ 99|   1.005/ **|   1.004/ **|   1.003/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  93   |   29601|      441.31|   1.005/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  76   |   28401|      602.99|   1.007/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  62   |   17079|       80.79|   1.062/ 11|   1.056/ 12|   1.055/ 12|   1.054/ 13 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  68   |    9380|      813.90|   1.010/ 72|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  70   |    8371|      100.68|   1.010/ 68|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  88   |    7185|       86.18|   1.008/ 84|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  70   |    6488|      170.75|   1.032/ 22|   1.022/ 31|   1.020/ 35|   1.017/ 40 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  54   |     518|      105.57|   1.037/ 18|   1.033/ 21|   1.032/ 22|   1.031/ 23 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  54   |      10|       14.03|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  58   |     718|       98.64|   1.047/ 15|   1.045/ 15|   1.044/ 15|   1.044/ 16 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  55   |     107|       35.62|   1.022/ 31|   1.009/ 80|   1.005/ **|   1.002/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  75   |    3433|       86.89|   1.027/ 25|   1.021/ 32|   1.020/ 35|   1.018/ 37 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  65   |    1204|      209.13|   1.027/ 26|   1.025/ 28|   1.024/ 28|   1.024/ 29 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  60   |    3514|      985.60|   1.023/ 29|   1.018/ 39|   1.017/ 42|   1.015/ 45 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  53   |     292|      299.86|   1.040/ 17|   1.036/ 19|   1.036/ 19|   1.035/ 20 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  71   |    2092|       97.39|   1.026/ 27|   1.021/ 33|   1.020/ 35|   1.018/ 38 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  67   |    1690|      159.20|   1.022/ 32|   1.017/ 42|   1.015/ 45|   1.014/ 49 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  48   |      17|       12.12|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  53   |      73|       41.09|   1.011/ 64|   1.009/ 75|   1.009/ 77|   1.009/ 79 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  62   |    4383|      345.87|   1.035/ 20|   1.031/ 22|   1.030/ 23|   1.029/ 24 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  63   |    1882|      279.62|   1.031/ 22|   1.022/ 31|   1.020/ 34|   1.018/ 38 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  54   |     370|      117.13|   1.049/ 14|   1.044/ 16|   1.042/ 16|   1.041/ 17 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  66   |     205|       70.37|   1.020/ 34|   1.017/ 41|   1.016/ 43|   1.015/ 46 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  63   |     354|       79.19|   1.019/ 36|   1.014/ 51|   1.012/ 57|   1.011/ 64 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  65   |    2574|      553.77|   1.015/ 46|   1.011/ 63|   1.010/ 69|   1.009/ 77 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  52   |      71|       53.10|   1.015/ 45|   1.012/ 56|   1.012/ 59|   1.011/ 63 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  60   |    2101|      347.48|   1.034/ 20|   1.026/ 26|   1.025/ 28|   1.023/ 30 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  59   |    6068|      873.10|   1.028/ 24|   1.020/ 34|   1.019/ 37|   1.017/ 41 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  60   |    5086|      509.25|   1.015/ 47|   1.009/ 76|   1.008/ 90|   1.006/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  58   |     778|      137.87|   1.043/ 16|   1.033/ 21|   1.031/ 22|   1.028/ 24 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  60   |     553|      185.90|   1.037/ 19|   1.032/ 22|   1.030/ 23|   1.029/ 24 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  60   |     628|      102.29|   1.032/ 21|   1.028/ 24|   1.027/ 25|   1.026/ 26 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  52   |      16|       15.07|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  51   |     121|       62.52|   1.039/ 17|   1.040/ 17|   1.040/ 17|   1.041/ 17 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  63   |     365|      118.53|   1.022/ 31|   1.018/ 39|   1.017/ 42|   1.015/ 45 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  56   |     182|      133.60|   1.050/ 14|   1.044/ 16|   1.042/ 16|   1.040/ 17 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  69   |   11006|     1239.11|   1.021/ 32|   1.015/ 47|   1.013/ 53|   1.012/ 60 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  54   |     276|      131.64|   1.046/ 15|   1.041/ 17|   1.040/ 17|   1.038/ 18 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  65   |   28859|     1483.47|   1.010/ 72|   1.007/ **|   1.006/ **|   1.005/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  54   |     709|       67.65|   1.034/ 21|   1.030/ 23|   1.029/ 24|   1.028/ 25 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  52   |      46|       60.79|   1.042/ 16|   1.032/ 22|   1.029/ 24|   1.026/ 26 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  59   |    1712|      146.50|   1.033/ 21|   1.026/ 26|   1.025/ 28|   1.023/ 30 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  60   |     302|       76.27|   1.014/ 48|   1.009/ 79|   1.007/ 95|   1.006/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  64   |     145|       34.32|   1.017/ 41|   1.013/ 55|   1.011/ 61|   1.010/ 67 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  60   |    4896|      382.46|   1.036/ 19|   1.027/ 26|   1.024/ 28|   1.022/ 32 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  58   |     125|       39.22|   1.019/ 37|   1.017/ 40|   1.017/ 41|   1.016/ 42 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  51   |     526|      496.31|   1.034/ 20|   1.023/ 29|   1.021/ 33|   1.018/ 38 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  63   |     422|       81.98|   1.027/ 26|   1.018/ 39|   1.015/ 45|   1.013/ 53 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  68   |      53|       60.17|   1.044/ 16|   1.042/ 17|   1.041/ 17|   1.040/ 17 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  58   |     300|       43.95|   1.025/ 27|   1.026/ 27|   1.026/ 27|   1.026/ 27 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  62   |    1366|       47.11|   1.032/ 21|   1.030/ 23|   1.030/ 23|   1.029/ 24 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  57   |      84|       26.09|   1.032/ 21|   1.029/ 24|   1.028/ 25|   1.027/ 26 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  59   |      55|       87.55|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  65   |    1091|      127.79|   1.035/ 20|   1.026/ 26|   1.024/ 29|   1.022/ 31 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  79   |    1037|      136.20|   1.012/ 55|   1.010/ 70|   1.009/ 74|   1.009/ 80 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  49   |      66|       36.60|   1.028/ 25|   1.027/ 25|   1.028/ 25|   1.028/ 25 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  59   |     467|       80.16|   1.022/ 31|   1.020/ 35|   1.019/ 36|   1.018/ 38 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  35   |       7|       12.09|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  57   |     172|        5.35|   1.056/ 12|   1.052/ 13|   1.051/ 13|   1.051/ 14 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  68   |      32|       11.20|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  67   |     547|       12.73|   1.012/ 57|   1.012/ 57|   1.012/ 57|   1.012/ 58 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  50   |       2|        0.06|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  71   |     386|        8.60|   1.030/ 23|   1.027/ 26|   1.026/ 27|   1.025/ 28 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  53   |      57|       19.12|   1.033/ 21|   1.034/ 20|   1.034/ 20|   1.034/ 20 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  78   |     106|        4.11|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  67   |     646|       72.53|   1.004/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  66   |      38|        3.76|   1.029/ 24|   1.031/ 22|   1.031/ 22|   1.031/ 22 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  63   |      10|        6.64|   1.036/ 19|   1.051/ 14|   1.055/ 13|   1.059/ 12 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  61   |     310|        1.84|   1.045/ 15|   1.051/ 13|   1.053/ 13|   1.054/ 13 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  48   |     168|       17.89|   1.037/ 18|   1.034/ 20|   1.033/ 21|   1.032/ 21 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  68   |    9380|      813.90|   1.010/ 72|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  42   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  50   |     179|       15.62|   1.063/ 11|   1.058/ 12|   1.057/ 12|   1.056/ 12 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  58   |     139|       42.07|   1.040/ 17|   1.039/ 18|   1.038/ 18|   1.038/ 18 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  48   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  62   |   17079|       80.79|   1.062/ 11|   1.056/ 12|   1.055/ 12|   1.054/ 13 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  68   |     112|       16.05|   1.028/ 25|   1.024/ 29|   1.023/ 30|   1.022/ 32 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  61   |      53|        2.52|   1.008/ 81|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  35   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  54   |     160|        6.04|   1.027/ 25|   1.029/ 24|   1.029/ 23|   1.030/ 23 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  70   |    6488|      170.75|   1.032/ 22|   1.022/ 31|   1.020/ 35|   1.017/ 40 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  20   |      54|        3.35|   1.091/  7|   1.078/  9|   1.065/ 11|   1.050/ 14 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  57   |     418|       21.88|   1.042/ 16|   1.045/ 15|   1.046/ 15|   1.047/ 15 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  68   |    4637|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  57   |     599|       12.13|   1.039/ 18|   1.034/ 20|   1.033/ 21|   1.031/ 22 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  60   |       9|        1.68|   1.050/ 14|   1.066/ 10|   1.070/ 10|   1.074/  9 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  60   |     102|       25.13|   1.017/ 42|   1.006/ **|   1.004/ **|   1.001/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  61   |      84|        7.54|   1.013/ 53|   1.004/ **|   1.001/ **|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  65   |     566|       97.28|   1.009/ 75|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  62   |     448|       43.20|   1.019/ 36|   1.016/ 44|   1.015/ 47|   1.014/ 50 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  65   |    3080|      176.30|   1.053/ 13|   1.049/ 14|   1.048/ 14|   1.046/ 15 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  71   |     647|        6.46|   1.028/ 24|   1.024/ 29|   1.023/ 30|   1.022/ 31 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  48   |      28|        4.27|   1.067/ 10|   1.072/  9|   1.074/  9|   1.076/  9 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  26   |       8|        5.66|   1.001/ **|   1.018/ 39|   1.021/ 33|   1.024/ 29 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  43   |       5|        0.05|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  58   |     306|       55.41|   1.019/ 35|   1.015/ 46|   1.014/ 49|   1.013/ 53 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  93   |   29601|      441.31|   1.005/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  59   |      12|        5.54|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  56   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  44   |      13|        3.39|   1.030/ 23|   1.023/ 29|   1.022/ 31|   1.021/ 34 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  70   |    8371|      100.68|   1.010/ 68|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  58   |      28|        0.94|   1.042/ 16|   1.049/ 14|   1.051/ 13|   1.054/ 13 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  68   |     163|       15.17|   1.009/ 75|   1.008/ 84|   1.008/ 86|   1.008/ 88 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  63   |      34|        2.06|   1.039/ 17|   1.042/ 16|   1.043/ 16|   1.043/ 16 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  33   |      16|        1.33|   1.047/ 15|   1.056/ 12|   1.059/ 12|   1.063/ 11 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  22   |       4|        2.39|   1.099/  7|   1.052/ 13|   1.064/ 11|   1.080/  8 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  43   |      22|        1.91|   1.063/ 11|   1.049/ 14|   1.045/ 15|   1.041/ 17 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  53   |     147|       16.09|   1.040/ 17|   1.035/ 20|   1.033/ 21|   1.032/ 22 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  64   |     478|       48.93|   1.020/ 34|   1.014/ 50|   1.012/ 57|   1.010/ 66 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  68   |    3251|        2.39|   1.055/ 12|   1.049/ 14|   1.047/ 15|   1.045/ 15 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  68   |    1129|        4.23|   1.020/ 34|   1.019/ 36|   1.019/ 37|   1.019/ 37 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  88   |    7185|       86.18|   1.008/ 84|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  75   |     121|        3.09|   1.017/ 41|   1.018/ 38|   1.019/ 37|   1.019/ 37 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  68   |    1660|      337.31|   1.012/ 57|   1.005/ **|   1.003/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  58   |     276|       30.02|   1.012/ 58|   1.010/ 72|   1.009/ 77|   1.008/ 83 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  87   |   32987|      547.61|   1.007/ 99|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  60   |      10|        3.50|   1.006/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  95   |     880|        6.99|   1.030/ 23|   1.021/ 32|   1.019/ 36|   1.017/ 40 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  52   |       9|        0.86|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  54   |      35|        1.86|   1.017/ 41|   1.015/ 46|   1.015/ 47|   1.014/ 49 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  53   |      50|        1.05|   1.062/ 11|   1.068/ 10|   1.069/ 10|   1.071/ 10 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  53   |      32|       17.85|   1.008/ 84|   1.008/ 89|   1.007/ 93|   1.007/ 98 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  44   |     112|       25.37|   1.091/  7|   1.100/  7|   1.103/  7|   1.105/  6 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  45   |      14|        2.15|   1.030/ 23|   1.025/ 28|   1.024/ 29|   1.023/ 29 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  45   |      19|       10.21|   1.013/ 53|   1.006/ **|   1.005/ **|   1.003/ ** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  69   |      27|        3.91|   1.003/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  44   |      21|        4.62|   1.009/ 81|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  46   |       3|        0.45|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  58   |      55|       19.85|   1.014/ 49|   1.015/ 48|   1.015/ 47|   1.015/ 47 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  62   |     114|        3.47|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  50   |      51|        2.51|   1.043/ 16|   1.044/ 16|   1.045/ 15|   1.045/ 15 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  49   |       1|        0.25|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  60   |    5426|       42.87|   1.065/ 11|   1.061/ 11|   1.060/ 11|   1.059/ 12 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  61   |     217|       80.81|   1.038/ 18|   1.035/ 20|   1.035/ 20|   1.034/ 20 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  69   |     197|        5.50|   1.006/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  73   |    5936|      340.06|   1.009/ 77|   1.005/ **|   1.004/ **|   1.003/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  50   |      21|        4.29|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  52   |       9|        1.35|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  54   |      55|        2.46|   1.028/ 24|   1.024/ 29|   1.023/ 30|   1.021/ 32 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  56   |     213|        1.03|   1.061/ 11|   1.040/ 17|   1.035/ 20|   1.029/ 24 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  57   |     102|       49.09|   1.015/ 46|   1.008/ 83|   1.007/ **|   1.005/ ** |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  65   |     234|       43.66|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  48   |      22|        4.61|   1.044/ 16|   1.046/ 15|   1.047/ 15|   1.048/ 14 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  60   |     940|        4.29|   1.049/ 14|   1.040/ 17|   1.038/ 18|   1.035/ 20 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  68   |     286|       67.78|   1.023/ 30|   1.019/ 37|   1.018/ 39|   1.017/ 41 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  58   |      11|        1.53|   1.009/ 73|   1.010/ 70|   1.010/ 68|   1.011/ 66 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  59   |    2763|       85.98|   1.055/ 12|   1.046/ 15|   1.044/ 16|   1.042/ 16 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 106   |     923|        8.51|   1.021/ 33|   1.017/ 41|   1.016/ 43|   1.015/ 45 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  67   |     965|       25.14|   1.023/ 30|   1.017/ 40|   1.016/ 44|   1.014/ 48 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  62   |    1244|      121.09|   1.011/ 61|   1.007/ 92|   1.007/ **|   1.006/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  51   |      15|        5.49|   1.018/ 38|   1.017/ 41|   1.016/ 42|   1.016/ 43 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  57   |    1145|       59.00|   1.025/ 28|   1.020/ 34|   1.019/ 36|   1.018/ 38 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  60   |    2810|       19.15|   1.054/ 13|   1.044/ 16|   1.041/ 17|   1.039/ 18 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  55   |     318|        9.30|   1.038/ 18|   1.036/ 19|   1.035/ 20|   1.034/ 20 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  47   |      28|        1.70|   1.072/ 10|   1.074/  9|   1.074/  9|   1.073/  9 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  59   |     246|       35.39|   1.013/ 54|   1.012/ 58|   1.011/ 60|   1.011/ 63 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  25   |      32|        4.05|   1.078/  9|   1.082/  8|   1.084/  8|   1.086/  8 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  58   |      23|        4.08|   1.018/ 38|   1.008/ 82|   1.006/ **|   1.004/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  51   |      28|        5.20|   1.012/ 59|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  65   |     108|       51.41|   1.007/ **|   1.003/ **|   1.002/ **|   1.000/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  40   |      59|        3.72|   1.040/ 17|   1.017/ 42|   1.010/ 68|   1.004/ ** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  52   |     276|        4.70|   1.054/ 13|   1.050/ 14|   1.048/ 14|   1.047/ 15 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  76   |   28401|      602.99|   1.007/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  51   |       9|        0.44|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  66   |     115|        2.70|   1.075/  9|   1.064/ 11|   1.061/ 11|   1.058/ 12 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  68   |    3844|      371.83|   1.022/ 31|   1.018/ 38|   1.017/ 40|   1.016/ 42 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  74   |    1948|      226.42|   1.004/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  50   |       3|        0.17|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  48   |      23|        0.41|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  78   |      58|        0.87|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  52   |      12|        1.56|   1.008/ 84|   1.007/ 93|   1.007/ 99|   1.006/ ** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  54   |       8|        5.87|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  60   |      46|        3.96|   1.005/ **|   1.001/ **|   1.001/ **|   1.000/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  62   |    4271|       51.36|   1.015/ 46|   1.010/ 69|   1.009/ 78|   1.008/ 89 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  79   |   95779|      290.64|   1.019/ 36|   1.013/ 55|   1.011/ 62|   1.010/ 72 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  66   |     523|       12.48|   1.041/ 17|   1.039/ 18|   1.039/ 18|   1.038/ 18 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  59   |     252|       25.46|   1.040/ 17|   1.022/ 32|   1.017/ 41|   1.012/ 57 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  68   |   37304|      561.50|   1.015/ 45|   1.010/ 71|   1.008/ 82|   1.007/ 99 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  50   |      20|        5.63|   1.011/ 65|   1.008/ 90|   1.007/ **|   1.006/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  52   |      11|        0.33|   1.015/ 45|   1.015/ 47|   1.015/ 47|   1.015/ 46 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  52   |      10|        0.31|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  46   |       8|        0.47|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  56   |       4|        0.26|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |

