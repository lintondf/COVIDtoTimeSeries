# State and Country COVID-19 Analysis #
## Updated: 2020-05-25 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  72   |   29795|     1531.57|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  76   |   11804|     1328.98|   1.014/ 51|   1.009/ 80|   1.007/ 93|   1.006/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  66   |    6698|      963.84|   1.019/ 37|   1.013/ 53|   1.012/ 60|   1.010/ 68 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  67   |    5349|      535.61|   1.010/ 66|   1.008/ 92|   1.007/ **|   1.006/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  67   |    5447|      425.45|   1.023/ 29|   1.016/ 44|   1.014/ 50|   1.012/ 57 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  69   |    5120|      404.05|   1.026/ 26|   1.022/ 32|   1.020/ 34|   1.019/ 36 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  82   |    3952|      100.02|   1.023/ 30|   1.020/ 35|   1.019/ 37|   1.018/ 38 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  67   |    3842|     1077.66|   1.016/ 42|   1.012/ 56|   1.011/ 62|   1.010/ 68 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  72   |    2769|      595.56|   1.012/ 58|   1.009/ 73|   1.009/ 78|   1.008/ 84 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  67   |    2396|      396.25|   1.024/ 29|   1.018/ 38|   1.017/ 42|   1.015/ 46 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  86   |  103771|      314.89|   1.014/ 48|   1.010/ 66|   1.009/ 73|   1.008/ 82 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  75   |   38650|      581.76|   1.010/ 67|   1.007/ 96|   1.006/ **|   1.006/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  94   |   33859|      562.08|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  83   |   29121|      618.27|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 100   |   29954|      446.57|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  69   |   23934|      113.21|   1.054/ 13|   1.049/ 14|   1.048/ 14|   1.047/ 15 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  75   |    9563|      829.76|   1.005/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  77   |    8567|      103.03|   1.006/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  95   |    7527|       90.28|   1.008/ 90|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  67   |    7771|       61.40|   1.058/ 12|   1.054/ 13|   1.053/ 13|   1.052/ 13 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  61   |     586|      119.42|   1.025/ 28|   1.018/ 39|   1.016/ 44|   1.014/ 49 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  61   |      10|       13.88|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  65   |     869|      119.40|   1.033/ 21|   1.026/ 27|   1.024/ 29|   1.022/ 32 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  62   |     117|       38.66|   1.019/ 37|   1.016/ 44|   1.015/ 46|   1.015/ 47 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  82   |    3952|      100.02|   1.023/ 30|   1.020/ 35|   1.019/ 37|   1.018/ 38 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  72   |    1396|      242.40|   1.021/ 32|   1.019/ 36|   1.019/ 37|   1.018/ 38 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  67   |    3842|     1077.66|   1.016/ 42|   1.012/ 56|   1.011/ 62|   1.010/ 68 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  60   |     348|      357.89|   1.027/ 25|   1.022/ 32|   1.020/ 35|   1.018/ 38 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  78   |    2357|      109.75|   1.020/ 34|   1.017/ 42|   1.016/ 44|   1.015/ 47 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  74   |    1887|      177.75|   1.019/ 37|   1.016/ 43|   1.015/ 45|   1.015/ 47 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  55   |      17|       12.02|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  60   |      79|       44.43|   1.011/ 61|   1.012/ 58|   1.012/ 58|   1.012/ 57 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  69   |    5120|      404.05|   1.026/ 26|   1.022/ 32|   1.020/ 34|   1.019/ 36 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  70   |    2103|      312.44|   1.021/ 33|   1.015/ 47|   1.013/ 53|   1.012/ 60 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  61   |     468|      148.18|   1.041/ 17|   1.037/ 19|   1.036/ 19|   1.035/ 20 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  73   |     218|       74.97|   1.012/ 58|   1.007/ 94|   1.006/ **|   1.005/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  70   |     403|       90.17|   1.019/ 36|   1.017/ 40|   1.017/ 41|   1.016/ 42 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  72   |    2769|      595.56|   1.012/ 58|   1.009/ 73|   1.009/ 78|   1.008/ 84 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  59   |      78|       57.67|   1.014/ 50|   1.013/ 53|   1.013/ 53|   1.013/ 54 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  67   |    2396|      396.25|   1.024/ 29|   1.018/ 38|   1.017/ 42|   1.015/ 46 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  66   |    6698|      963.84|   1.019/ 37|   1.013/ 53|   1.012/ 60|   1.010/ 68 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  67   |    5349|      535.61|   1.010/ 66|   1.008/ 92|   1.007/ **|   1.006/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  65   |     924|      163.79|   1.032/ 21|   1.026/ 27|   1.024/ 29|   1.023/ 30 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  67   |     655|      220.03|   1.029/ 24|   1.024/ 29|   1.023/ 30|   1.022/ 32 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  67   |     727|      118.42|   1.024/ 28|   1.020/ 35|   1.019/ 37|   1.018/ 39 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  59   |      16|       14.97|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  58   |     153|       78.84|   1.035/ 20|   1.035/ 20|   1.035/ 20|   1.034/ 20 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  70   |     404|      131.27|   1.017/ 42|   1.013/ 54|   1.012/ 58|   1.011/ 63 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  63   |     225|      165.31|   1.038/ 18|   1.031/ 22|   1.029/ 23|   1.028/ 25 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  76   |   11804|     1328.98|   1.014/ 51|   1.009/ 80|   1.007/ 93|   1.006/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  61   |     332|      158.17|   1.033/ 21|   1.026/ 27|   1.024/ 29|   1.022/ 31 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  72   |   29795|     1531.57|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  61   |     813|       77.56|   1.025/ 27|   1.022/ 32|   1.021/ 34|   1.020/ 35 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  59   |      55|       72.66|   1.032/ 21|   1.026/ 27|   1.024/ 28|   1.023/ 30 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  66   |    2019|      172.72|   1.028/ 25|   1.025/ 28|   1.024/ 29|   1.023/ 30 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  67   |     317|       80.10|   1.011/ 63|   1.008/ 85|   1.007/ 93|   1.007/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  71   |     153|       36.38|   1.012/ 58|   1.009/ 81|   1.008/ 90|   1.007/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  67   |    5447|      425.45|   1.023/ 29|   1.016/ 44|   1.014/ 50|   1.012/ 57 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  65   |     133|       41.56|   1.011/ 65|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  58   |     613|      578.33|   1.028/ 25|   1.025/ 28|   1.024/ 29|   1.023/ 29 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  70   |     456|       88.66|   1.018/ 38|   1.013/ 52|   1.012/ 57|   1.011/ 63 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  75   |      60|       68.11|   1.028/ 25|   1.022/ 32|   1.020/ 34|   1.019/ 37 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  65   |     339|       49.60|   1.020/ 35|   1.018/ 39|   1.017/ 40|   1.017/ 41 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  69   |    1589|       54.81|   1.024/ 29|   1.020/ 35|   1.019/ 36|   1.018/ 38 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  64   |     101|       31.41|   1.029/ 24|   1.026/ 27|   1.025/ 28|   1.024/ 29 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  66   |      55|       87.56|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  72   |    1243|      145.59|   1.025/ 28|   1.019/ 37|   1.017/ 40|   1.016/ 43 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  86   |    1098|      144.25|   1.009/ 74|   1.007/ 96|   1.007/ **|   1.006/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  56   |      75|       42.00|   1.021/ 33|   1.018/ 38|   1.017/ 40|   1.016/ 42 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  66   |     521|       89.47|   1.018/ 38|   1.016/ 43|   1.016/ 44|   1.015/ 46 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  42   |      13|       21.81|   1.027/ 26|   1.042/ 16|   1.046/ 15|   1.049/ 14 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  64   |     228|        7.08|   1.045/ 15|   1.041/ 17|   1.040/ 17|   1.039/ 18 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  75   |      31|       11.05|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  74   |     597|       13.89|   1.013/ 55|   1.013/ 54|   1.013/ 54|   1.013/ 53 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  57   |       2|        0.06|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  78   |     462|       10.29|   1.029/ 24|   1.027/ 26|   1.026/ 26|   1.026/ 27 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  60   |      78|       26.30|   1.043/ 16|   1.048/ 14|   1.049/ 14|   1.050/ 14 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  85   |     105|        4.08|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  74   |     647|       72.72|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  73   |      48|        4.80|   1.035/ 20|   1.037/ 19|   1.038/ 18|   1.038/ 18 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  70   |      13|        8.60|   1.025/ 27|   1.030/ 23|   1.031/ 22|   1.032/ 22 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  68   |     461|        2.74|   1.053/ 13|   1.059/ 12|   1.060/ 11|   1.061/ 11 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  55   |     204|       21.70|   1.031/ 22|   1.027/ 26|   1.026/ 27|   1.025/ 28 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  75   |    9563|      829.76|   1.005/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  49   |       3|        0.24|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  57   |     253|       22.08|   1.058/ 12|   1.055/ 12|   1.054/ 13|   1.054/ 13 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  65   |     157|       47.70|   1.023/ 30|   1.015/ 45|   1.013/ 53|   1.011/ 64 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  55   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  69   |   23934|      113.21|   1.054/ 13|   1.049/ 14|   1.048/ 14|   1.047/ 15 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  75   |     131|       18.88|   1.026/ 26|   1.025/ 28|   1.024/ 29|   1.024/ 29 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  68   |      53|        2.56|   1.004/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  42   |       1|        0.09|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  61   |     176|        6.62|   1.025/ 28|   1.024/ 28|   1.024/ 29|   1.024/ 29 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  77   |    7122|      187.44|   1.020/ 34|   1.012/ 56|   1.010/ 66|   1.009/ 81 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  27   |      61|        3.77|   1.043/ 16|   1.020/ 35|   1.014/ 49|   1.009/ 79 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  64   |     654|       34.22|   1.060/ 11|   1.070/ 10|   1.072/  9|   1.075/  9 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  75   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  64   |     737|       14.92|   1.034/ 20|   1.031/ 22|   1.030/ 23|   1.030/ 23 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  67   |      11|        2.16|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  67   |     103|       25.23|   1.008/ 90|   1.002/ **|   1.000/ **|   1.000/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  68   |      84|        7.53|   1.006/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  72   |     578|       99.33|   1.005/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  69   |     478|       46.17|   1.013/ 55|   1.009/ 79|   1.008/ 89|   1.007/ ** |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  72   |    3634|      208.06|   1.033/ 21|   1.023/ 30|   1.021/ 33|   1.018/ 38 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  78   |     767|        7.65|   1.026/ 26|   1.024/ 28|   1.024/ 29|   1.023/ 29 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  55   |      38|        5.85|   1.048/ 14|   1.038/ 18|   1.036/ 19|   1.033/ 21 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  33   |      11|        8.25|   1.078/  9|   1.085/  8|   1.089/  8|   1.095/  7 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  50   |       5|        0.05|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  65   |     321|       58.04|   1.010/ 70|   1.005/ **|   1.003/ **|   1.002/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 100   |   29954|      446.57|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  66   |      14|        6.58|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  63   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  51   |      13|        3.40|   1.011/ 63|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  77   |    8567|      103.03|   1.006/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  65   |      34|        1.13|   1.027/ 25|   1.024/ 29|   1.023/ 30|   1.021/ 32 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  75   |     172|       16.06|   1.008/ 83|   1.008/ 87|   1.008/ 88|   1.008/ 89 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  70   |      54|        3.22|   1.060/ 11|   1.067/ 10|   1.068/ 10|   1.070/ 10 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  40   |      21|        1.70|   1.042/ 16|   1.034/ 20|   1.032/ 22|   1.029/ 24 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  29   |       7|        4.22|   1.097/  7|   1.057/ 12|   1.043/ 16|   1.027/ 25 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  50   |      27|        2.36|   1.044/ 15|   1.034/ 20|   1.032/ 22|   1.030/ 23 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  60   |     178|       19.42|   1.034/ 20|   1.031/ 22|   1.030/ 23|   1.030/ 23 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  71   |     510|       52.14|   1.013/ 54|   1.008/ 88|   1.007/ **|   1.005/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  75   |    4308|        3.16|   1.046/ 15|   1.039/ 17|   1.038/ 18|   1.036/ 19 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  75   |    1353|        5.07|   1.025/ 27|   1.026/ 26|   1.027/ 26|   1.027/ 25 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  95   |    7527|       90.28|   1.008/ 90|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  82   |     145|        3.70|   1.027/ 25|   1.031/ 22|   1.032/ 21|   1.034/ 21 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  75   |    1670|      339.25|   1.007/ 93|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  65   |     289|       31.40|   1.007/ 95|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  94   |   33859|      562.08|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  67   |       9|        3.37|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 102   |     966|        7.67|   1.019/ 37|   1.012/ 59|   1.010/ 70|   1.008/ 85 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  59   |       9|        0.85|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  61   |      36|        1.95|   1.008/ 82|   1.004/ **|   1.003/ **|   1.001/ ** |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  60   |      59|        1.24|   1.030/ 23|   1.016/ 44|   1.012/ 59|   1.008/ 92 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  60   |      30|       16.83|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  51   |     168|       37.97|   1.070/ 10|   1.057/ 12|   1.053/ 13|   1.049/ 14 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  52   |      15|        2.24|   1.011/ 63|   1.004/ **|   1.002/ **|   1.000/ ** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  52   |      22|       11.60|   1.016/ 43|   1.018/ 39|   1.018/ 38|   1.019/ 37 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  76   |      27|        3.89|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  51   |      25|        5.52|   1.020/ 34|   1.029/ 24|   1.031/ 22|   1.034/ 21 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  53   |       3|        0.44|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  65   |      63|       22.68|   1.016/ 42|   1.017/ 40|   1.017/ 40|   1.018/ 39 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  69   |     117|        3.56|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  57   |      66|        3.27|   1.041/ 17|   1.039/ 17|   1.039/ 18|   1.039/ 18 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  56   |       1|        0.25|   1.167/  4|   1.109/  6|   1.092/  7|   1.074/  9 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  67   |    7771|       61.40|   1.058/ 12|   1.054/ 13|   1.053/ 13|   1.052/ 13 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  68   |     261|       97.29|   1.029/ 24|   1.025/ 28|   1.024/ 29|   1.023/ 30 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  76   |     201|        5.61|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  80   |    6054|      346.81|   1.005/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  57   |      21|        4.24|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  59   |      18|        2.81|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  61   |      64|        2.85|   1.023/ 30|   1.020/ 35|   1.019/ 36|   1.018/ 38 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  63   |     249|        1.21|   1.039/ 17|   1.026/ 27|   1.022/ 31|   1.019/ 37 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  64   |     114|       55.01|   1.016/ 44|   1.015/ 45|   1.015/ 45|   1.015/ 45 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  72   |     240|       44.67|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  55   |      36|        7.69|   1.065/ 11|   1.075/  9|   1.077/  9|   1.080/  9 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  67   |    1182|        5.39|   1.040/ 17|   1.034/ 20|   1.033/ 21|   1.032/ 22 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  75   |     316|       74.90|   1.017/ 40|   1.014/ 50|   1.013/ 53|   1.012/ 56 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  65   |      11|        1.58|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  66   |    3679|      114.51|   1.045/ 15|   1.039/ 18|   1.037/ 18|   1.036/ 19 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 113   |     981|        9.04|   1.013/ 53|   1.009/ 77|   1.008/ 86|   1.007/ 98 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  74   |    1052|       27.41|   1.015/ 45|   1.011/ 64|   1.010/ 70|   1.009/ 79 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  69   |    1323|      128.70|   1.010/ 66|   1.009/ 76|   1.009/ 78|   1.009/ 81 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  58   |      19|        6.82|   1.040/ 17|   1.054/ 13|   1.058/ 12|   1.062/ 11 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  64   |    1248|       64.29|   1.015/ 45|   1.010/ 68|   1.009/ 79|   1.007/ 93 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  67   |    3659|       24.93|   1.045/ 15|   1.039/ 17|   1.038/ 18|   1.037/ 19 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  62   |     395|       11.54|   1.034/ 20|   1.032/ 22|   1.031/ 22|   1.031/ 22 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  54   |      38|        2.35|   1.055/ 12|   1.042/ 16|   1.038/ 18|   1.035/ 20 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  66   |     248|       35.67|   1.008/ 87|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  32   |      41|        5.17|   1.061/ 11|   1.039/ 18|   1.034/ 20|   1.030/ 23 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  65   |      24|        4.18|   1.010/ 70|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  58   |      29|        5.26|   1.005/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  72   |     109|       51.93|   1.004/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  47   |      64|        4.00|   1.019/ 36|   1.009/ 80|   1.006/ **|   1.004/ ** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  59   |     422|        7.18|   1.062/ 11|   1.065/ 11|   1.065/ 10|   1.066/ 10 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  83   |   29121|      618.27|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  58   |       9|        0.42|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  73   |     161|        3.80|   1.055/ 12|   1.043/ 16|   1.040/ 17|   1.037/ 19 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  75   |    4184|      404.68|   1.016/ 44|   1.012/ 57|   1.011/ 62|   1.010/ 67 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  81   |    1949|      226.57|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  57   |       3|        0.17|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  55   |      22|        0.39|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  85   |      57|        0.86|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  59   |      13|        1.66|   1.009/ 79|   1.007/ 98|   1.007/ **|   1.006/ ** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  61   |       8|        5.87|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  67   |      48|        4.09|   1.005/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  69   |    4468|       53.73|   1.009/ 73|   1.006/ **|   1.005/ **|   1.004/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  86   |  103771|      314.89|   1.014/ 48|   1.010/ 66|   1.009/ 73|   1.008/ 82 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  73   |     655|       15.63|   1.033/ 21|   1.030/ 23|   1.029/ 24|   1.028/ 25 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  66   |     270|       27.33|   1.022/ 32|   1.009/ 77|   1.006/ **|   1.003/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  75   |   38650|      581.76|   1.010/ 67|   1.007/ 96|   1.006/ **|   1.006/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  57   |      21|        6.05|   1.012/ 56|   1.013/ 52|   1.014/ 50|   1.014/ 49 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  59   |      13|        0.39|   1.016/ 44|   1.016/ 45|   1.015/ 45|   1.015/ 46 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  59   |      10|        0.31|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  53   |       8|        0.44|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  63   |       4|        0.26|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |

