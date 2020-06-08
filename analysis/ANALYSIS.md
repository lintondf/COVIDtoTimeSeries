# State and Country COVID-19 Analysis #
## Updated: 2020-06-08 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  86   |   30805|     1583.52|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  90   |   12589|     1417.36|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  80   |    7562|     1088.16|   1.010/ 70|   1.007/ 94|   1.007/ **|   1.006/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  81   |    6186|      483.19|   1.011/ 62|   1.008/ 86|   1.007/ 96|   1.006/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  83   |    6162|      486.30|   1.014/ 48|   1.011/ 62|   1.010/ 66|   1.010/ 72 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  81   |    5799|      580.67|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  96   |    4835|      122.36|   1.016/ 44|   1.013/ 51|   1.013/ 53|   1.012/ 56 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  81   |    4220|     1183.78|   1.007/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  86   |    2990|      643.24|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  81   |    2859|      472.82|   1.014/ 51|   1.011/ 65|   1.010/ 69|   1.009/ 74 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 100   |  115354|      350.04|   1.008/ 82|   1.006/ **|   1.006/ **|   1.005/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  89   |   41310|      621.81|   1.007/ **|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  83   |   39566|      187.15|   1.036/ 19|   1.031/ 22|   1.030/ 23|   1.028/ 24 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 108   |   34709|      576.20|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 114   |   30122|      449.07|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  97   |   27632|      586.66|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  81   |   14325|      113.17|   1.047/ 15|   1.045/ 15|   1.044/ 16|   1.043/ 16 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  89   |    9748|      845.88|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  91   |    8863|      106.59|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 109   |    8294|       99.47|   1.008/ 92|   1.007/ 95|   1.007/ 96|   1.007/ 97 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  75   |     708|      144.43|   1.016/ 45|   1.013/ 52|   1.013/ 54|   1.012/ 56 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  75   |      10|       13.67|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  79   |    1077|      147.98|   1.020/ 35|   1.017/ 41|   1.016/ 43|   1.015/ 45 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  76   |     154|       51.13|   1.022/ 31|   1.024/ 29|   1.024/ 29|   1.024/ 28 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  96   |    4835|      122.36|   1.016/ 44|   1.013/ 51|   1.013/ 53|   1.012/ 56 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  86   |    1617|      280.77|   1.010/ 68|   1.007/ 97|   1.006/ **|   1.006/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  81   |    4220|     1183.78|   1.007/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  74   |     410|      421.43|   1.013/ 52|   1.010/ 72|   1.009/ 79|   1.008/ 88 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  92   |    2790|      129.89|   1.014/ 50|   1.012/ 58|   1.011/ 61|   1.011/ 63 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  88   |    2278|      214.52|   1.013/ 54|   1.011/ 62|   1.011/ 65|   1.010/ 68 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  69   |      17|       12.01|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  74   |      86|       47.91|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  83   |    6162|      486.30|   1.014/ 48|   1.011/ 62|   1.010/ 66|   1.010/ 72 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  84   |    2382|      353.89|   1.011/ 63|   1.008/ 82|   1.008/ 89|   1.007/ 96 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  75   |     650|      206.14|   1.022/ 31|   1.017/ 41|   1.016/ 44|   1.014/ 49 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  87   |     236|       80.85|   1.008/ 84|   1.007/ 99|   1.007/ **|   1.006/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  84   |     482|      107.87|   1.014/ 49|   1.013/ 53|   1.013/ 54|   1.013/ 55 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  86   |    2990|      643.24|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  73   |     100|       74.13|   1.018/ 39|   1.019/ 37|   1.019/ 37|   1.019/ 36 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  81   |    2859|      472.82|   1.014/ 51|   1.011/ 65|   1.010/ 69|   1.009/ 74 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  80   |    7562|     1088.16|   1.010/ 70|   1.007/ 94|   1.007/ **|   1.006/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  81   |    5799|      580.67|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  79   |    1239|      219.67|   1.022/ 31|   1.020/ 35|   1.019/ 36|   1.018/ 38 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  81   |     859|      288.71|   1.020/ 35|   1.017/ 40|   1.017/ 42|   1.016/ 44 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  81   |     853|      138.98|   1.012/ 57|   1.009/ 77|   1.008/ 85|   1.007/ 94 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  73   |      18|       16.51|   1.008/ 91|   1.010/ 71|   1.010/ 68|   1.011/ 64 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  72   |     197|      101.63|   1.019/ 36|   1.016/ 44|   1.015/ 47|   1.014/ 50 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  84   |     454|      147.30|   1.009/ 77|   1.007/ **|   1.006/ **|   1.006/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  77   |     296|      218.03|   1.024/ 29|   1.021/ 34|   1.020/ 35|   1.019/ 36 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  90   |   12589|     1417.36|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  75   |     413|      196.90|   1.017/ 40|   1.013/ 53|   1.012/ 57|   1.011/ 62 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  86   |   30805|     1583.52|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  75   |    1073|      102.29|   1.019/ 37|   1.017/ 41|   1.016/ 43|   1.016/ 44 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  73   |      73|       95.78|   1.024/ 28|   1.023/ 29|   1.023/ 30|   1.023/ 30 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  80   |    2508|      214.54|   1.016/ 44|   1.012/ 56|   1.012/ 60|   1.011/ 65 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  81   |     355|       89.62|   1.008/ 88|   1.007/ **|   1.007/ **|   1.006/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  85   |     164|       38.97|   1.007/ **|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  81   |    6186|      483.19|   1.011/ 62|   1.008/ 86|   1.007/ 96|   1.006/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  79   |     144|       44.95|   1.007/ 97|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  72   |     818|      772.45|   1.019/ 37|   1.016/ 44|   1.015/ 47|   1.014/ 50 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  84   |     551|      107.09|   1.016/ 42|   1.016/ 44|   1.015/ 45|   1.015/ 45 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  89   |      71|       80.02|   1.015/ 45|   1.011/ 61|   1.010/ 67|   1.009/ 74 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  79   |     420|       61.47|   1.017/ 40|   1.017/ 41|   1.017/ 41|   1.017/ 41 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  83   |    1905|       65.69|   1.015/ 48|   1.012/ 58|   1.011/ 61|   1.011/ 64 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  78   |     128|       39.99|   1.017/ 42|   1.013/ 52|   1.012/ 56|   1.011/ 60 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  80   |      55|       88.69|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  86   |    1573|      184.33|   1.015/ 47|   1.011/ 62|   1.010/ 67|   1.009/ 74 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 100   |    1192|      156.55|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  70   |      84|       46.69|   1.013/ 55|   1.012/ 57|   1.012/ 58|   1.012/ 58 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  80   |     659|      113.23|   1.017/ 41|   1.016/ 43|   1.016/ 43|   1.016/ 44 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  56   |      19|       32.55|   1.022/ 32|   1.011/ 61|   1.009/ 80|   1.006/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  78   |     339|       10.51|   1.036/ 19|   1.035/ 20|   1.035/ 20|   1.035/ 20 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  89   |      34|       11.80|   1.004/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  88   |     710|       16.51|   1.012/ 58|   1.012/ 59|   1.012/ 59|   1.012/ 59 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  71   |       2|        0.06|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  92   |     664|       14.78|   1.028/ 25|   1.027/ 25|   1.027/ 25|   1.027/ 25 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  74   |     200|       67.66|   1.065/ 11|   1.069/ 10|   1.070/ 10|   1.071/ 10 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  99   |     104|        4.05|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  88   |     678|       76.16|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  87   |      84|        8.36|   1.043/ 16|   1.045/ 15|   1.046/ 15|   1.047/ 15 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  84   |      23|       14.92|   1.044/ 15|   1.050/ 14|   1.052/ 13|   1.053/ 13 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  82   |     905|        5.37|   1.047/ 15|   1.046/ 15|   1.046/ 15|   1.045/ 15 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  69   |     274|       29.17|   1.022/ 32|   1.019/ 36|   1.019/ 37|   1.018/ 38 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  89   |    9748|      845.88|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  63   |       3|        0.27|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  71   |     471|       41.09|   1.048/ 14|   1.046/ 15|   1.046/ 15|   1.046/ 15 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  79   |     168|       50.94|   1.006/ **|   1.002/ **|   1.000/ **|   1.000/ -- |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  69   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  83   |   39566|      187.15|   1.036/ 19|   1.031/ 22|   1.030/ 23|   1.028/ 24 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  89   |     163|       23.51|   1.019/ 37|   1.017/ 40|   1.017/ 40|   1.017/ 41 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  82   |      54|        2.58|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  56   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  75   |     218|        8.22|   1.019/ 37|   1.017/ 41|   1.017/ 42|   1.016/ 43 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  91   |    8263|      217.46|   1.012/ 57|   1.009/ 77|   1.008/ 84|   1.007/ 92 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  16   |       5|        0.92|   1.260/  3|   1.151/  4|   1.103/  7|   1.058/ 12 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  41   |      69|        4.25|   1.010/ 72|   1.008/ 87|   1.008/ 90|   1.007/ 93 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  78   |    1617|       84.63|   1.064/ 11|   1.065/ 10|   1.066/ 10|   1.066/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  89   |    4638|        3.31|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  78   |    1213|       24.56|   1.041/ 17|   1.043/ 16|   1.044/ 16|   1.045/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  81   |      11|        2.12|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  81   |     106|       26.02|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  82   |      85|        7.54|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  86   |     592|      101.72|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  83   |     541|       52.23|   1.010/ 67|   1.010/ 72|   1.009/ 73|   1.009/ 75 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  86   |    3931|      225.02|   1.011/ 63|   1.006/ **|   1.004/ **|   1.003/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  92   |    1194|       11.90|   1.035/ 20|   1.037/ 19|   1.037/ 18|   1.038/ 18 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  69   |      57|        8.85|   1.030/ 23|   1.025/ 27|   1.024/ 29|   1.022/ 31 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  47   |      12|        9.09|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  64   |      19|        0.20|   1.112/  6|   1.138/  5|   1.144/  5|   1.151/  4 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  79   |     330|       59.67|   1.003/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 114   |   30122|      449.07|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  80   |      22|       10.03|   1.059/ 12|   1.065/ 11|   1.066/ 10|   1.068/ 10 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  77   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  65   |      13|        3.46|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  91   |    8863|      106.59|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  79   |      43|        1.42|   1.023/ 29|   1.023/ 30|   1.023/ 30|   1.023/ 30 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  89   |     185|       17.22|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  84   |     187|       11.27|   1.109/  6|   1.123/  5|   1.126/  5|   1.130/  5 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  54   |      24|        1.99|   1.011/ 62|   1.003/ **|   1.001/ **|   1.000/ -- |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  43   |      11|        6.89|   1.054/ 13|   1.082/  8|   1.090/  8|   1.098/  7 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  64   |      56|        4.83|   1.045/ 15|   1.042/ 16|   1.041/ 17|   1.040/ 17 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  74   |     261|       28.54|   1.029/ 24|   1.028/ 25|   1.028/ 25|   1.028/ 25 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  85   |     563|       57.57|   1.007/ 92|   1.006/ **|   1.005/ **|   1.005/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  89   |    7300|        5.36|   1.042/ 17|   1.040/ 17|   1.040/ 17|   1.040/ 17 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  89   |    1871|        7.01|   1.022/ 31|   1.022/ 31|   1.022/ 32|   1.022/ 32 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 109   |    8294|       99.47|   1.008/ 92|   1.007/ 95|   1.007/ 96|   1.007/ 97 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  96   |     240|        6.14|   1.055/ 12|   1.063/ 11|   1.065/ 10|   1.067/ 10 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  89   |    1714|      348.32|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  79   |     297|       32.32|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 108   |   34709|      576.20|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  81   |      10|        3.52|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 116   |    1053|        8.36|   1.006/ **|   1.002/ **|   1.001/ **|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  73   |       9|        0.84|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  75   |      49|        2.63|   1.032/ 22|   1.039/ 18|   1.041/ 17|   1.043/ 16 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  74   |      82|        1.73|   1.032/ 21|   1.033/ 21|   1.034/ 20|   1.034/ 20 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  74   |      30|       16.89|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  65   |     277|       62.66|   1.038/ 18|   1.030/ 23|   1.028/ 24|   1.026/ 26 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  66   |      21|        3.16|   1.033/ 21|   1.041/ 17|   1.043/ 16|   1.045/ 15 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  66   |      26|       13.51|   1.010/ 72|   1.007/ 95|   1.007/ **|   1.006/ ** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  90   |      28|        4.05|   1.008/ 92|   1.009/ 73|   1.010/ 70|   1.010/ 66 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  65   |      30|        6.80|   1.015/ 46|   1.014/ 50|   1.013/ 52|   1.013/ 53 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  67   |       6|        0.80|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  79   |      75|       26.86|   1.009/ 80|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  22   |       8|        0.32|   1.045/ 15|   1.063/ 11|   1.079/  9|   1.094/  7 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  83   |     117|        3.58|   1.001/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  71   |      93|        4.60|   1.026/ 27|   1.022/ 31|   1.021/ 32|   1.021/ 33 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  70   |      55|       13.56|   1.048/ 14|   1.115/  6|   1.130/  5|   1.121/  6 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  81   |   14325|      113.17|   1.047/ 15|   1.045/ 15|   1.044/ 16|   1.043/ 16 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  82   |     351|      130.84|   1.021/ 33|   1.018/ 38|   1.017/ 40|   1.017/ 41 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  90   |     211|        5.87|   1.003/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  14   |       2|        0.07|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  23   |      13|        0.44|   1.113/  6|   1.099/  7|   1.100/  7|   1.103/  7 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  94   |    6158|      352.73|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  71   |      22|        4.46|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  73   |      60|        9.36|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  75   |      69|        3.10|   1.005/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  77   |     359|        1.74|   1.030/ 23|   1.028/ 25|   1.027/ 25|   1.027/ 26 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  78   |     153|       73.55|   1.021/ 32|   1.023/ 31|   1.023/ 30|   1.023/ 30 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  86   |     241|       44.83|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  69   |      76|       16.19|   1.061/ 11|   1.062/ 11|   1.063/ 11|   1.063/ 11 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  81   |    1954|        8.91|   1.042/ 17|   1.042/ 16|   1.043/ 16|   1.043/ 16 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  89   |     384|       91.13|   1.017/ 40|   1.017/ 40|   1.017/ 41|   1.017/ 40 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  79   |      11|        1.56|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  80   |    5759|      179.24|   1.032/ 21|   1.028/ 24|   1.027/ 25|   1.026/ 26 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 127   |    1087|       10.02|   1.008/ 87|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  88   |    1180|       30.75|   1.010/ 67|   1.009/ 80|   1.008/ 84|   1.008/ 88 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  83   |    1503|      146.29|   1.009/ 80|   1.008/ 86|   1.008/ 88|   1.008/ 90 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  72   |      55|       20.19|   1.063/ 11|   1.065/ 11|   1.065/ 10|   1.066/ 10 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  78   |    1363|       70.26|   1.008/ 90|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  81   |    6138|       41.83|   1.037/ 19|   1.034/ 20|   1.033/ 21|   1.033/ 21 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  76   |     666|       19.45|   1.044/ 16|   1.048/ 14|   1.048/ 14|   1.049/ 14 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  68   |      51|        3.14|   1.024/ 29|   1.017/ 40|   1.015/ 45|   1.014/ 50 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  80   |     252|       36.13|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  46   |      49|        6.23|   1.013/ 52|   1.003/ **|   1.001/ **|   1.000/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  79   |      25|        4.33|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  72   |      28|        5.17|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  86   |     111|       52.81|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  61   |      85|        5.35|   1.018/ 39|   1.016/ 43|   1.015/ 45|   1.015/ 47 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  73   |    1029|       17.52|   1.061/ 11|   1.060/ 11|   1.060/ 11|   1.060/ 11 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  97   |   27632|      586.66|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  72   |      11|        0.51|   1.007/ 98|   1.008/ 85|   1.008/ 82|   1.009/ 80 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  87   |     399|        9.41|   1.053/ 13|   1.049/ 14|   1.048/ 14|   1.046/ 15 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  89   |    4828|      467.04|   1.010/ 67|   1.009/ 81|   1.008/ 86|   1.008/ 91 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  95   |    1947|      226.33|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  71   |       6|        0.35|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  69   |      21|        0.38|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  99   |      58|        0.87|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  73   |      14|        1.79|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  75   |       8|        5.87|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  81   |      49|        4.22|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  83   |    4772|       57.39|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 100   |  115354|      350.04|   1.008/ 82|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  87   |     847|       20.22|   1.019/ 37|   1.014/ 48|   1.013/ 52|   1.012/ 56 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  80   |     289|       29.18|   1.008/ 91|   1.003/ **|   1.002/ **|   1.001/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  89   |   41310|      621.81|   1.007/ **|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  71   |      24|        6.73|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  73   |      17|        0.49|   1.018/ 38|   1.018/ 37|   1.019/ 37|   1.019/ 37 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  73   |      21|        0.65|   1.046/ 15|   1.058/ 12|   1.061/ 11|   1.063/ 11 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  67   |       7|        0.39|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  77   |       4|        0.26|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |

