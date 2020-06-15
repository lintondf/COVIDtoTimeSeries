# State and Country COVID-19 Analysis #
## Updated: 2020-06-15 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  93   |   31139|     1600.68|   1.002/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  97   |   12923|     1454.98|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  87   |    7855|     1130.24|   1.007/ 99|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  90   |    6587|      519.82|   1.011/ 62|   1.009/ 78|   1.008/ 84|   1.008/ 90 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  88   |    6459|      504.53|   1.008/ 87|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  88   |    6142|      615.00|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 103   |    5271|      133.41|   1.014/ 50|   1.012/ 56|   1.012/ 58|   1.011/ 60 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  88   |    4315|     1210.16|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  93   |    3076|      661.77|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  88   |    3050|      504.57|   1.011/ 65|   1.009/ 81|   1.008/ 86|   1.007/ 93 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 107   |  120014|      364.18|   1.007/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  90   |   47247|      223.48|   1.028/ 24|   1.024/ 29|   1.023/ 30|   1.022/ 32 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  96   |   42698|      642.69|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 115   |   34955|      580.28|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 121   |   30139|      449.32|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 104   |   27270|      578.99|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  88   |   18517|      146.29|   1.039/ 18|   1.035/ 20|   1.034/ 20|   1.033/ 21 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  96   |    9796|      850.02|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  96   |    9472|        6.96|   1.039/ 18|   1.037/ 18|   1.037/ 19|   1.037/ 19 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 116   |    8780|      105.30|   1.008/ 84|   1.008/ 84|   1.008/ 83|   1.008/ 83 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  82   |     790|      161.18|   1.016/ 44|   1.015/ 46|   1.015/ 46|   1.015/ 47 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  82   |      11|       14.92|   1.013/ 52|   1.018/ 39|   1.019/ 36|   1.020/ 34 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  86   |    1211|      166.39|   1.019/ 36|   1.018/ 39|   1.017/ 40|   1.017/ 40 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  83   |     180|       59.61|   1.022/ 31|   1.023/ 30|   1.023/ 30|   1.023/ 30 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 103   |    5271|      133.41|   1.014/ 50|   1.012/ 56|   1.012/ 58|   1.011/ 60 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  93   |    1672|      290.29|   1.007/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  88   |    4315|     1210.16|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  81   |     435|      447.00|   1.010/ 69|   1.008/ 92|   1.007/ **|   1.006/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  99   |    3009|      140.11|   1.012/ 57|   1.011/ 64|   1.011/ 65|   1.010/ 68 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  95   |    2486|      234.11|   1.014/ 50|   1.013/ 52|   1.013/ 53|   1.013/ 53 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  76   |      17|       12.01|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  81   |      87|       48.90|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  90   |    6587|      519.82|   1.011/ 62|   1.009/ 78|   1.008/ 84|   1.008/ 90 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  91   |    2500|      371.36|   1.009/ 81|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  82   |     705|      223.50|   1.014/ 49|   1.009/ 75|   1.008/ 87|   1.007/ ** |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  94   |     248|       85.22|   1.008/ 91|   1.007/ 99|   1.007/ **|   1.007/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  91   |     517|      115.68|   1.011/ 62|   1.010/ 71|   1.009/ 74|   1.009/ 76 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  93   |    3076|      661.77|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  80   |     106|       79.20|   1.009/ 74|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  88   |    3050|      504.57|   1.011/ 65|   1.009/ 81|   1.008/ 86|   1.007/ 93 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  87   |    7855|     1130.24|   1.007/ 99|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  88   |    6142|      615.00|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  86   |    1391|      246.71|   1.018/ 38|   1.016/ 44|   1.015/ 46|   1.014/ 48 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  88   |     946|      317.70|   1.015/ 46|   1.012/ 56|   1.012/ 60|   1.011/ 64 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  88   |     912|      148.66|   1.011/ 61|   1.010/ 72|   1.009/ 75|   1.009/ 78 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  80   |      18|       17.25|   1.003/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  79   |     218|      112.75|   1.019/ 36|   1.018/ 38|   1.018/ 39|   1.017/ 40 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  91   |     474|      153.94|   1.008/ 90|   1.006/ **|   1.006/ **|   1.006/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  84   |     333|      245.08|   1.020/ 35|   1.017/ 40|   1.017/ 42|   1.016/ 43 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  97   |   12923|     1454.98|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  82   |     448|      213.49|   1.014/ 50|   1.011/ 61|   1.011/ 64|   1.010/ 68 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  93   |   31139|     1600.68|   1.002/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  82   |    1183|      112.78|   1.015/ 46|   1.013/ 53|   1.013/ 55|   1.012/ 58 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  80   |      80|      104.61|   1.014/ 51|   1.010/ 70|   1.009/ 78|   1.008/ 87 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  87   |    2671|      228.47|   1.011/ 60|   1.009/ 79|   1.008/ 86|   1.007/ 93 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  88   |     369|       93.19|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  92   |     174|       41.26|   1.008/ 85|   1.008/ 87|   1.008/ 88|   1.008/ 88 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  88   |    6459|      504.53|   1.008/ 87|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  86   |     149|       46.51|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  79   |     884|      834.05|   1.013/ 54|   1.009/ 73|   1.009/ 81|   1.008/ 90 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  91   |     613|      119.05|   1.015/ 45|   1.015/ 48|   1.014/ 48|   1.014/ 49 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  96   |      78|       87.84|   1.017/ 40|   1.016/ 45|   1.015/ 46|   1.015/ 47 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  86   |     472|       69.13|   1.018/ 38|   1.019/ 37|   1.019/ 36|   1.019/ 36 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  90   |    2047|       70.59|   1.012/ 59|   1.010/ 70|   1.009/ 73|   1.009/ 76 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  85   |     142|       44.15|   1.018/ 39|   1.016/ 42|   1.016/ 43|   1.016/ 43 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  87   |      55|       88.76|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  93   |    1657|      194.15|   1.010/ 71|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 107   |    1232|      161.84|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  77   |      89|       49.73|   1.010/ 69|   1.009/ 73|   1.009/ 74|   1.009/ 75 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  87   |     720|      123.64|   1.013/ 52|   1.012/ 58|   1.011/ 60|   1.011/ 62 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  63   |      19|       32.92|   1.011/ 63|   1.003/ **|   1.001/ **|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  85   |     457|       14.18|   1.042/ 16|   1.043/ 16|   1.044/ 16|   1.044/ 15 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  96   |      35|       12.35|   1.007/ 94|   1.009/ 81|   1.009/ 78|   1.009/ 76 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  95   |     770|       17.91|   1.012/ 58|   1.012/ 59|   1.012/ 59|   1.012/ 60 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  78   |       5|        0.17|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  99   |     819|       18.23|   1.030/ 23|   1.031/ 22|   1.031/ 22|   1.031/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  81   |     294|       99.25|   1.053/ 13|   1.051/ 13|   1.051/ 13|   1.051/ 13 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 106   |     104|        4.03|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  95   |     685|       76.97|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  94   |     117|       11.60|   1.045/ 15|   1.047/ 14|   1.048/ 14|   1.048/ 14 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  91   |      35|       22.86|   1.061/ 11|   1.069/ 10|   1.071/ 10|   1.073/  9 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  89   |    1219|        7.24|   1.044/ 16|   1.042/ 16|   1.041/ 17|   1.041/ 17 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  76   |     314|       33.36|   1.020/ 34|   1.019/ 37|   1.018/ 38|   1.018/ 39 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  96   |    9796|      850.02|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  70   |       4|        0.38|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  78   |     622|       54.21|   1.043/ 16|   1.041/ 17|   1.040/ 17|   1.040/ 17 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  86   |     169|       51.21|   1.004/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  76   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  90   |   47247|      223.48|   1.028/ 24|   1.024/ 29|   1.023/ 30|   1.022/ 32 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  96   |     181|       26.03|   1.014/ 48|   1.013/ 54|   1.012/ 56|   1.012/ 58 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  89   |      54|        2.57|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  63   |       1|        0.09|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  82   |     230|        8.65|   1.009/ 80|   1.005/ **|   1.003/ **|   1.002/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  98   |    8674|      228.28|   1.008/ 84|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  23   |       7|        1.29|   1.041/ 17|   1.083/  8|   1.100/  7|   1.119/  6 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  48   |      73|        4.52|   1.008/ 87|   1.007/ 94|   1.007/ 96|   1.007/ 99 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  85   |    3041|      159.17|   1.068/ 10|   1.069/ 10|   1.070/ 10|   1.070/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  96   |    4638|        3.31|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  85   |    1656|       33.53|   1.042/ 16|   1.044/ 16|   1.044/ 16|   1.045/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  88   |      12|        2.31|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  88   |     108|       26.49|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  89   |      85|        7.55|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  93   |     602|      103.41|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  90   |     581|       56.13|   1.011/ 61|   1.012/ 60|   1.012/ 60|   1.012/ 60 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  93   |    4045|      231.59|   1.009/ 74|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  99   |    1521|       15.17|   1.035/ 20|   1.036/ 19|   1.036/ 19|   1.036/ 19 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  76   |      73|       11.25|   1.037/ 19|   1.037/ 19|   1.037/ 19|   1.037/ 18 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  54   |      12|        8.86|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  71   |      53|        0.54|   1.130/  5|   1.150/  4|   1.155/  4|   1.159/  4 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  86   |     331|       59.93|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 121   |   30139|      449.32|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  87   |      25|       11.67|   1.013/ 55|   1.010/ 73|   1.009/ 79|   1.008/ 86 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  84   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  72   |      14|        3.63|   1.006/ **|   1.007/ 94|   1.008/ 90|   1.008/ 86 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  98   |    8957|      107.72|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  86   |      51|        1.69|   1.022/ 31|   1.023/ 31|   1.023/ 30|   1.023/ 30 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  96   |     188|       17.51|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  91   |     408|       24.55|   1.077/  9|   1.079/  9|   1.079/  9|   1.079/  9 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  61   |      25|        2.01|   1.009/ 79|   1.007/ **|   1.007/ **|   1.006/ ** |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  50   |      15|        9.48|   1.042/ 16|   1.052/ 13|   1.054/ 13|   1.056/ 12 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  71   |      72|        6.25|   1.043/ 16|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  81   |     319|       34.78|   1.029/ 24|   1.029/ 24|   1.029/ 24|   1.029/ 24 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  92   |     578|       59.15|   1.005/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  96   |    9472|        6.96|   1.039/ 18|   1.037/ 18|   1.037/ 19|   1.037/ 19 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  96   |    2160|        8.09|   1.021/ 32|   1.021/ 33|   1.021/ 33|   1.020/ 34 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 116   |    8780|      105.30|   1.008/ 84|   1.008/ 84|   1.008/ 83|   1.008/ 83 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 103   |     453|       11.58|   1.074/  9|   1.083/  8|   1.085/  8|   1.087/  8 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  96   |    1735|      352.47|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  86   |     303|       33.02|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 115   |   34955|      580.28|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  88   |      10|        3.70|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 123   |    1048|        8.32|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  80   |       9|        0.84|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  82   |      69|        3.71|   1.043/ 16|   1.050/ 14|   1.052/ 13|   1.054/ 13 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  81   |     102|        2.15|   1.032/ 21|   1.033/ 21|   1.033/ 21|   1.033/ 21 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  81   |      31|       17.45|   1.004/ **|   1.005/ **|   1.005/ **|   1.006/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  72   |     321|       72.52|   1.025/ 27|   1.018/ 38|   1.016/ 43|   1.014/ 48 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  73   |      27|        4.18|   1.032/ 21|   1.036/ 19|   1.036/ 19|   1.037/ 19 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  73   |      28|       14.46|   1.012/ 59|   1.012/ 57|   1.012/ 57|   1.012/ 56 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  97   |      30|        4.46|   1.012/ 60|   1.014/ 50|   1.014/ 48|   1.015/ 46 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  72   |      33|        7.29|   1.011/ 61|   1.010/ 70|   1.010/ 72|   1.009/ 74 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  74   |       7|        0.96|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  86   |      77|       27.68|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  29   |      11|        0.40|   1.057/ 12|   1.023/ 30|   1.013/ 55|   1.002/ ** |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  90   |     119|        3.63|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  78   |     107|        5.29|   1.022/ 31|   1.020/ 34|   1.020/ 35|   1.019/ 36 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  77   |     116|       28.48|   1.100/  7|   1.091/  7|   1.088/  8|   1.085/  8 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  88   |   18517|      146.29|   1.039/ 18|   1.035/ 20|   1.034/ 20|   1.033/ 21 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  89   |     407|      151.66|   1.022/ 31|   1.021/ 32|   1.021/ 32|   1.021/ 33 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  97   |     214|        5.97|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  21   |       2|        0.07|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  30   |      19|        0.63|   1.075/  9|   1.052/ 13|   1.047/ 15|   1.042/ 16 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 101   |    6174|      353.67|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  78   |      22|        4.47|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  80   |      72|       11.14|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  82   |      68|        3.05|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  84   |     430|        2.09|   1.028/ 25|   1.026/ 27|   1.025/ 27|   1.025/ 28 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  85   |     179|       86.33|   1.024/ 29|   1.025/ 27|   1.026/ 27|   1.026/ 26 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  93   |     242|       45.10|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  76   |     108|       23.06|   1.052/ 13|   1.050/ 14|   1.050/ 14|   1.049/ 14 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  88   |    2669|       12.17|   1.043/ 16|   1.044/ 16|   1.044/ 16|   1.044/ 16 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  96   |     436|      103.25|   1.017/ 40|   1.017/ 40|   1.017/ 40|   1.017/ 40 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  86   |      11|        1.54|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  87   |    6848|      213.12|   1.027/ 25|   1.024/ 29|   1.023/ 30|   1.023/ 31 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 134   |    1138|       10.49|   1.008/ 92|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  95   |    1259|       32.80|   1.010/ 70|   1.009/ 77|   1.009/ 78|   1.009/ 80 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  90   |    1560|      151.81|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  79   |      80|       29.30|   1.053/ 13|   1.049/ 14|   1.048/ 14|   1.047/ 15 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  85   |    1418|       73.08|   1.007/ **|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  88   |    7467|       50.88|   1.030/ 23|   1.027/ 26|   1.026/ 27|   1.025/ 28 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  16   |       2|        0.16|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  83   |     944|       27.59|   1.047/ 15|   1.050/ 14|   1.051/ 13|   1.052/ 13 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  75   |      59|        3.67|   1.027/ 26|   1.026/ 27|   1.026/ 27|   1.025/ 27 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  87   |     255|       36.65|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  53   |      51|        6.52|   1.009/ 80|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  86   |      26|        4.51|   1.006/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  79   |      28|        5.14|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  93   |     110|       52.76|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  68   |      91|        5.72|   1.012/ 59|   1.008/ 87|   1.007/ 99|   1.006/ ** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  80   |    1537|       26.15|   1.059/ 12|   1.057/ 12|   1.056/ 12|   1.056/ 12 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 104   |   27270|      578.99|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  79   |      11|        0.53|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  94   |     535|       12.62|   1.040/ 17|   1.035/ 20|   1.033/ 21|   1.032/ 22 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  96   |    5065|      489.92|   1.008/ 89|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 102   |    1950|      226.67|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  78   |       7|        0.39|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  76   |      21|        0.38|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 106   |      58|        0.88|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  80   |      13|        1.77|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  82   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  88   |      50|        4.24|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  90   |    4888|       58.79|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 107   |  120014|      364.18|   1.007/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  94   |     937|       22.37|   1.017/ 42|   1.014/ 49|   1.013/ 52|   1.013/ 54 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  87   |     298|       30.09|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  96   |   42698|      642.69|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  78   |      24|        6.74|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  80   |      19|        0.57|   1.018/ 38|   1.019/ 37|   1.019/ 37|   1.019/ 37 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  80   |      26|        0.82|   1.023/ 29|   1.026/ 27|   1.026/ 26|   1.027/ 26 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  74   |      10|        0.54|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  84   |       4|        0.26|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |

