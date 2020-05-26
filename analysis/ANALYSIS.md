# State and Country COVID-19 Analysis #
## Updated: 2020-05-26 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  73   |   29877|     1535.83|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  77   |   11851|     1334.22|   1.012/ 56|   1.007/ 93|   1.006/ **|   1.005/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  67   |    6752|      971.62|   1.017/ 40|   1.012/ 59|   1.010/ 67|   1.009/ 77 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  68   |    5386|      539.35|   1.010/ 71|   1.007/ 98|   1.006/ **|   1.006/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  68   |    5523|      431.43|   1.021/ 32|   1.014/ 50|   1.012/ 57|   1.010/ 68 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  70   |    5213|      411.37|   1.025/ 28|   1.020/ 35|   1.018/ 38|   1.017/ 41 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  83   |    4008|      101.43|   1.022/ 32|   1.018/ 39|   1.017/ 41|   1.016/ 43 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  68   |    3887|     1090.32|   1.015/ 45|   1.011/ 61|   1.010/ 66|   1.009/ 73 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  73   |    2786|      599.22|   1.011/ 64|   1.008/ 84|   1.008/ 92|   1.007/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  68   |    2436|      402.89|   1.023/ 31|   1.017/ 41|   1.015/ 45|   1.014/ 50 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  87   |  104490|      317.07|   1.013/ 51|   1.009/ 73|   1.008/ 82|   1.007/ 92 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  76   |   38888|      585.35|   1.010/ 71|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  95   |   33917|      563.05|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 101   |   29921|      446.08|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  84   |   29012|      615.97|   1.004/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  70   |   25024|      118.37|   1.052/ 13|   1.047/ 15|   1.046/ 15|   1.044/ 15 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  76   |    9593|      832.41|   1.005/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  78   |    8601|      103.44|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  68   |    8136|       64.28|   1.055/ 12|   1.050/ 14|   1.049/ 14|   1.048/ 14 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  96   |    7581|       90.92|   1.008/ 92|   1.007/ **|   1.006/ **|   1.006/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  62   |     595|      121.38|   1.023/ 30|   1.016/ 43|   1.014/ 48|   1.013/ 55 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  62   |      10|       13.86|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  66   |     886|      121.70|   1.030/ 23|   1.022/ 31|   1.020/ 34|   1.018/ 38 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  63   |     118|       39.11|   1.018/ 38|   1.015/ 46|   1.014/ 48|   1.014/ 50 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  83   |    4008|      101.43|   1.022/ 32|   1.018/ 39|   1.017/ 41|   1.016/ 43 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  73   |    1413|      245.37|   1.019/ 36|   1.017/ 42|   1.016/ 44|   1.015/ 46 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  68   |    3887|     1090.32|   1.015/ 45|   1.011/ 61|   1.010/ 66|   1.009/ 73 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  61   |     354|      363.03|   1.025/ 27|   1.019/ 37|   1.017/ 40|   1.015/ 45 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  79   |    2385|      111.05|   1.019/ 36|   1.015/ 46|   1.014/ 49|   1.013/ 52 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  75   |    1910|      179.90|   1.017/ 40|   1.014/ 48|   1.014/ 50|   1.013/ 53 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  56   |      17|       12.02|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  61   |      80|       44.80|   1.010/ 67|   1.010/ 68|   1.010/ 68|   1.010/ 69 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  70   |    5213|      411.37|   1.025/ 28|   1.020/ 35|   1.018/ 38|   1.017/ 41 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  71   |    2121|      315.00|   1.019/ 36|   1.013/ 54|   1.011/ 62|   1.010/ 72 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  62   |     482|      152.75|   1.039/ 17|   1.035/ 20|   1.034/ 20|   1.033/ 21 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  74   |     220|       75.43|   1.011/ 65|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  71   |     407|       91.19|   1.017/ 40|   1.015/ 47|   1.014/ 49|   1.013/ 52 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  73   |    2786|      599.22|   1.011/ 64|   1.008/ 84|   1.008/ 92|   1.007/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  60   |      78|       58.38|   1.014/ 50|   1.013/ 52|   1.013/ 52|   1.013/ 53 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  68   |    2436|      402.89|   1.023/ 31|   1.017/ 41|   1.015/ 45|   1.014/ 50 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  67   |    6752|      971.62|   1.017/ 40|   1.012/ 59|   1.010/ 67|   1.009/ 77 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  68   |    5386|      539.35|   1.010/ 71|   1.007/ 98|   1.006/ **|   1.006/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  66   |     945|      167.64|   1.030/ 23|   1.024/ 29|   1.022/ 31|   1.020/ 34 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  68   |     670|      224.96|   1.028/ 25|   1.023/ 30|   1.022/ 32|   1.021/ 33 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  68   |     738|      120.26|   1.022/ 31|   1.017/ 40|   1.016/ 44|   1.015/ 48 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  60   |      16|       14.97|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  59   |     156|       80.54|   1.032/ 22|   1.029/ 24|   1.029/ 24|   1.028/ 25 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  71   |     408|      132.60|   1.015/ 45|   1.011/ 60|   1.011/ 66|   1.010/ 72 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  64   |     230|      169.22|   1.035/ 20|   1.027/ 26|   1.025/ 28|   1.023/ 30 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  77   |   11851|     1334.22|   1.012/ 56|   1.007/ 93|   1.006/ **|   1.005/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  62   |     339|      161.85|   1.031/ 22|   1.024/ 29|   1.022/ 32|   1.020/ 34 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  73   |   29877|     1535.83|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  62   |     827|       78.85|   1.023/ 30|   1.019/ 37|   1.018/ 39|   1.016/ 42 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  60   |      57|       74.35|   1.030/ 23|   1.023/ 30|   1.021/ 32|   1.020/ 35 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  67   |    2058|      176.03|   1.027/ 26|   1.024/ 29|   1.023/ 30|   1.022/ 31 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  68   |     320|       80.75|   1.010/ 67|   1.008/ 90|   1.007/ 98|   1.006/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  72   |     154|       36.63|   1.011/ 64|   1.007/ 96|   1.006/ **|   1.005/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  68   |    5523|      431.43|   1.021/ 32|   1.014/ 50|   1.012/ 57|   1.010/ 68 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  66   |     134|       41.83|   1.010/ 69|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  59   |     624|      588.78|   1.027/ 26|   1.023/ 30|   1.022/ 31|   1.022/ 32 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  71   |     460|       89.31|   1.018/ 39|   1.013/ 52|   1.012/ 57|   1.011/ 62 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  76   |      61|       68.92|   1.025/ 28|   1.017/ 39|   1.016/ 44|   1.014/ 51 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  66   |     345|       50.44|   1.020/ 35|   1.018/ 38|   1.018/ 39|   1.017/ 40 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  70   |    1617|       55.77|   1.023/ 31|   1.019/ 37|   1.018/ 39|   1.016/ 42 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  65   |     103|       32.00|   1.028/ 25|   1.024/ 29|   1.023/ 30|   1.022/ 31 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  67   |      55|       87.44|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  73   |    1263|      147.94|   1.024/ 29|   1.018/ 38|   1.017/ 41|   1.015/ 45 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  87   |    1105|      145.09|   1.009/ 78|   1.007/ **|   1.006/ **|   1.006/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  57   |      76|       42.39|   1.019/ 37|   1.015/ 47|   1.014/ 51|   1.012/ 56 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  67   |     528|       90.61|   1.017/ 40|   1.015/ 45|   1.015/ 47|   1.014/ 49 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  43   |      13|       22.57|   1.019/ 37|   1.024/ 28|   1.026/ 27|   1.027/ 25 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  65   |     235|        7.29|   1.043/ 16|   1.038/ 18|   1.037/ 19|   1.035/ 19 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  76   |      32|       11.09|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  75   |     605|       14.08|   1.013/ 54|   1.013/ 52|   1.013/ 52|   1.013/ 52 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  58   |       2|        0.06|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  79   |     474|       10.55|   1.028/ 24|   1.026/ 26|   1.026/ 27|   1.025/ 27 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  61   |      82|       27.76|   1.044/ 15|   1.050/ 14|   1.051/ 13|   1.053/ 13 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  86   |     105|        4.08|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  75   |     647|       72.73|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  74   |      50|        4.97|   1.035/ 20|   1.037/ 19|   1.038/ 18|   1.038/ 18 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  71   |      14|        8.91|   1.029/ 24|   1.034/ 20|   1.036/ 19|   1.037/ 19 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  69   |     489|        2.90|   1.054/ 13|   1.058/ 12|   1.059/ 12|   1.060/ 11 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  56   |     209|       22.26|   1.030/ 23|   1.026/ 27|   1.025/ 28|   1.024/ 29 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  76   |    9593|      832.41|   1.005/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  50   |       2|        0.17|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  58   |     266|       23.21|   1.056/ 12|   1.053/ 13|   1.052/ 13|   1.052/ 13 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  66   |     159|       48.27|   1.021/ 32|   1.013/ 54|   1.011/ 65|   1.008/ 83 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  56   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  70   |   25024|      118.37|   1.052/ 13|   1.047/ 15|   1.046/ 15|   1.044/ 15 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  76   |     134|       19.30|   1.025/ 27|   1.023/ 30|   1.022/ 31|   1.022/ 31 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  69   |      53|        2.56|   1.004/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  43   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  62   |     178|        6.72|   1.023/ 30|   1.022/ 31|   1.022/ 32|   1.021/ 33 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  78   |    7224|      190.12|   1.019/ 36|   1.012/ 59|   1.010/ 69|   1.008/ 84 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  28   |      62|        3.81|   1.036/ 19|   1.018/ 39|   1.014/ 51|   1.010/ 72 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  65   |     704|       36.86|   1.061/ 11|   1.070/ 10|   1.073/  9|   1.075/  9 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  76   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  65   |     759|       15.37|   1.034/ 20|   1.031/ 22|   1.030/ 23|   1.030/ 23 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  68   |      11|        2.18|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  68   |     103|       25.35|   1.007/ **|   1.002/ **|   1.001/ **|   1.000/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  69   |      84|        7.52|   1.005/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  73   |     578|       99.35|   1.005/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  70   |     482|       46.50|   1.011/ 61|   1.007/ 96|   1.006/ **|   1.005/ ** |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  73   |    3665|      209.83|   1.030/ 23|   1.021/ 33|   1.019/ 37|   1.016/ 42 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  79   |     786|        7.84|   1.027/ 26|   1.025/ 27|   1.025/ 28|   1.025/ 28 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  56   |      39|        6.01|   1.044/ 15|   1.033/ 21|   1.030/ 23|   1.027/ 25 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  34   |      12|        8.83|   1.073/  9|   1.075/  9|   1.078/  9|   1.081/  8 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  51   |       5|        0.05|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  66   |     322|       58.25|   1.009/ 80|   1.004/ **|   1.002/ **|   1.001/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 101   |   29921|      446.08|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  67   |      14|        6.65|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  64   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  52   |      13|        3.39|   1.009/ 74|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  78   |    8601|      103.44|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  66   |      35|        1.15|   1.026/ 27|   1.021/ 33|   1.020/ 35|   1.018/ 38 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  76   |     173|       16.18|   1.008/ 84|   1.008/ 89|   1.008/ 90|   1.008/ 91 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  71   |      57|        3.44|   1.057/ 12|   1.062/ 11|   1.064/ 11|   1.065/ 10 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  41   |      21|        1.73|   1.038/ 18|   1.030/ 23|   1.027/ 25|   1.025/ 28 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  30   |       7|        4.44|   1.099/  7|   1.049/ 14|   1.034/ 20|   1.017/ 40 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  51   |      28|        2.42|   1.042/ 16|   1.032/ 22|   1.029/ 23|   1.027/ 26 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  61   |     183|       19.98|   1.033/ 21|   1.030/ 23|   1.030/ 23|   1.029/ 24 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  72   |     514|       52.62|   1.012/ 57|   1.008/ 92|   1.006/ **|   1.005/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  76   |    4478|        3.29|   1.044/ 16|   1.038/ 18|   1.037/ 19|   1.035/ 19 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  76   |    1386|        5.19|   1.025/ 28|   1.026/ 27|   1.026/ 27|   1.026/ 26 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  96   |    7581|       90.92|   1.008/ 92|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  83   |     150|        3.84|   1.029/ 24|   1.033/ 21|   1.034/ 20|   1.035/ 20 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  76   |    1675|      340.42|   1.007/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  66   |     290|       31.52|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  95   |   33917|      563.05|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  68   |       9|        3.37|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 103   |     970|        7.70|   1.018/ 39|   1.011/ 64|   1.009/ 76|   1.007/ 93 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  60   |       9|        0.85|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  62   |      37|        1.96|   1.007/ 96|   1.002/ **|   1.001/ **|   1.000/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  61   |      59|        1.24|   1.028/ 25|   1.013/ 52|   1.009/ 74|   1.005/ ** |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  61   |      30|       16.79|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  52   |     177|       39.94|   1.068/ 10|   1.055/ 13|   1.051/ 13|   1.047/ 15 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  53   |      15|        2.30|   1.013/ 51|   1.010/ 68|   1.009/ 74|   1.009/ 80 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  53   |      22|       11.74|   1.015/ 48|   1.015/ 47|   1.015/ 46|   1.015/ 46 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  77   |      26|        3.88|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  52   |      25|        5.66|   1.021/ 32|   1.030/ 23|   1.033/ 21|   1.035/ 20 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  54   |       3|        0.44|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  66   |      64|       22.97|   1.016/ 43|   1.016/ 42|   1.016/ 42|   1.016/ 42 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  70   |     117|        3.57|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  58   |      69|        3.39|   1.039/ 18|   1.037/ 19|   1.036/ 19|   1.036/ 19 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  57   |       8|        2.00|   1.161/  4|   1.105/  6|   1.089/  8|   1.073/  9 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  68   |    8136|       64.28|   1.055/ 12|   1.050/ 14|   1.049/ 14|   1.048/ 14 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  69   |     268|       99.77|   1.029/ 24|   1.025/ 27|   1.025/ 28|   1.024/ 29 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  77   |     202|        5.63|   1.005/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  10   |       4|        0.13|   1.260/  2|   1.145/  5|   1.000/ --|   1.101/  7 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  81   |    6055|      346.85|   1.004/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  58   |      21|        4.23|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  60   |      19|        2.94|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  62   |      65|        2.89|   1.022/ 32|   1.018/ 39|   1.017/ 41|   1.016/ 43 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  64   |     255|        1.24|   1.036/ 19|   1.023/ 30|   1.020/ 35|   1.017/ 41 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  65   |     115|       55.59|   1.015/ 47|   1.014/ 51|   1.013/ 51|   1.013/ 52 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  73   |     240|       44.71|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  56   |      38|        8.11|   1.063/ 11|   1.070/ 10|   1.071/ 10|   1.073/  9 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  68   |    1222|        5.57|   1.039/ 18|   1.033/ 21|   1.032/ 22|   1.031/ 22 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  76   |     321|       76.01|   1.017/ 41|   1.014/ 50|   1.013/ 53|   1.012/ 56 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  66   |      11|        1.58|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  67   |    3806|      118.46|   1.044/ 16|   1.038/ 18|   1.036/ 19|   1.035/ 20 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 114   |     991|        9.13|   1.012/ 57|   1.008/ 84|   1.007/ 96|   1.006/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  75   |    1059|       27.60|   1.014/ 49|   1.010/ 70|   1.009/ 78|   1.008/ 89 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  70   |    1336|      130.03|   1.010/ 66|   1.009/ 73|   1.009/ 75|   1.009/ 77 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  59   |      20|        7.18|   1.049/ 14|   1.067/ 10|   1.071/ 10|   1.076/  9 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  65   |    1255|       64.69|   1.015/ 48|   1.009/ 73|   1.008/ 85|   1.007/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  68   |    3803|       25.91|   1.044/ 16|   1.039/ 18|   1.038/ 18|   1.036/ 19 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  63   |     406|       11.88|   1.034/ 20|   1.031/ 22|   1.031/ 22|   1.030/ 23 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  55   |      39|        2.41|   1.051/ 14|   1.036/ 19|   1.033/ 21|   1.029/ 24 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  67   |     248|       35.57|   1.007/ 96|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  33   |      42|        5.34|   1.056/ 12|   1.037/ 19|   1.033/ 21|   1.029/ 24 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  66   |      24|        4.20|   1.009/ 81|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  59   |      29|        5.26|   1.004/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  73   |     109|       51.94|   1.004/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  48   |      65|        4.09|   1.019/ 37|   1.012/ 59|   1.010/ 68|   1.009/ 80 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  60   |     453|        7.71|   1.062/ 11|   1.066/ 10|   1.067/ 10|   1.068/ 10 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  84   |   29012|      615.97|   1.004/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  59   |       9|        0.43|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  74   |     172|        4.04|   1.062/ 11|   1.054/ 13|   1.052/ 13|   1.051/ 13 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  76   |    4229|      409.10|   1.015/ 47|   1.011/ 61|   1.010/ 67|   1.009/ 73 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  82   |    1952|      226.89|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  58   |       3|        0.17|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  56   |      22|        0.39|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  86   |      57|        0.86|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  60   |      13|        1.69|   1.011/ 61|   1.010/ 67|   1.010/ 69|   1.010/ 71 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  62   |       8|        5.87|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  68   |      48|        4.11|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  70   |    4498|       54.09|   1.009/ 77|   1.006/ **|   1.005/ **|   1.004/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  87   |  104490|      317.07|   1.013/ 51|   1.009/ 73|   1.008/ 82|   1.007/ 92 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  74   |     671|       16.03|   1.032/ 22|   1.028/ 25|   1.026/ 26|   1.025/ 27 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  67   |     271|       27.37|   1.020/ 35|   1.007/ 95|   1.004/ **|   1.001/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  76   |   38888|      585.35|   1.010/ 71|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  58   |      22|        6.15|   1.015/ 48|   1.017/ 40|   1.018/ 39|   1.019/ 37 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  60   |      14|        0.40|   1.014/ 49|   1.013/ 54|   1.012/ 56|   1.012/ 59 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  60   |      10|        0.31|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  54   |       8|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  64   |       4|        0.26|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |

