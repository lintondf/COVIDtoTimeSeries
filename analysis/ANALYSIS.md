# State and Country COVID-19 Analysis #
## Updated: 2020-06-03 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  81   |   30495|     1567.59|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  85   |   12318|     1386.79|   1.007/ 94|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  75   |    7250|     1043.18|   1.012/ 56|   1.009/ 75|   1.008/ 82|   1.008/ 90 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  76   |    5943|      464.19|   1.013/ 53|   1.008/ 83|   1.007/ 96|   1.006/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  76   |    5644|      565.12|   1.007/ 94|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  78   |    5824|      459.59|   1.017/ 42|   1.012/ 56|   1.011/ 62|   1.010/ 68 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  91   |    4510|      114.15|   1.017/ 41|   1.014/ 50|   1.013/ 53|   1.012/ 56 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  76   |    4134|     1159.45|   1.010/ 70|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  81   |    2907|      625.27|   1.007/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  76   |    2708|      447.84|   1.016/ 43|   1.012/ 57|   1.011/ 62|   1.010/ 68 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  95   |  111346|      337.88|   1.010/ 71|   1.007/ **|   1.006/ **|   1.006/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  84   |   40179|      604.79|   1.007/ 92|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 103   |   34455|      571.98|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  78   |   33912|      160.41|   1.040/ 17|   1.034/ 20|   1.033/ 21|   1.031/ 22 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 109   |   30041|      447.87|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  92   |   28086|      596.29|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  76   |   11470|       90.62|   1.044/ 15|   1.039/ 18|   1.037/ 18|   1.036/ 19 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  84   |    9706|      842.23|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  86   |    8787|      105.68|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 104   |    7997|       95.91|   1.007/ 95|   1.007/ **|   1.007/ **|   1.007/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  70   |     667|      135.93|   1.018/ 38|   1.015/ 46|   1.014/ 49|   1.014/ 51 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  70   |      10|       13.70|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  74   |     992|      136.28|   1.020/ 35|   1.014/ 50|   1.012/ 56|   1.011/ 63 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  71   |     137|       45.37|   1.018/ 38|   1.018/ 38|   1.018/ 38|   1.018/ 38 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  91   |    4510|      114.15|   1.017/ 41|   1.014/ 50|   1.013/ 53|   1.012/ 56 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  81   |    1553|      269.76|   1.013/ 52|   1.010/ 69|   1.009/ 75|   1.008/ 82 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  76   |    4134|     1159.45|   1.010/ 70|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  69   |     390|      400.58|   1.017/ 41|   1.012/ 60|   1.010/ 67|   1.009/ 76 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  87   |    2626|      122.25|   1.014/ 50|   1.011/ 64|   1.010/ 68|   1.009/ 74 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  83   |    2147|      202.23|   1.016/ 44|   1.014/ 48|   1.014/ 49|   1.014/ 50 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  64   |      17|       12.01|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  69   |      85|       47.33|   1.007/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  78   |    5824|      459.59|   1.017/ 42|   1.012/ 56|   1.011/ 62|   1.010/ 68 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  79   |    2282|      339.04|   1.012/ 55|   1.008/ 82|   1.007/ 93|   1.006/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  70   |     596|      188.95|   1.029/ 24|   1.023/ 29|   1.022/ 31|   1.021/ 33 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  82   |     228|       78.15|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  79   |     451|      100.95|   1.015/ 47|   1.013/ 52|   1.013/ 54|   1.013/ 55 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  81   |    2907|      625.27|   1.007/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  68   |      91|       67.34|   1.018/ 39|   1.019/ 36|   1.020/ 35|   1.020/ 34 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  76   |    2708|      447.84|   1.016/ 43|   1.012/ 57|   1.011/ 62|   1.010/ 68 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  75   |    7250|     1043.18|   1.012/ 56|   1.009/ 75|   1.008/ 82|   1.008/ 90 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  76   |    5644|      565.12|   1.007/ 94|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  74   |    1127|      199.75|   1.025/ 28|   1.021/ 33|   1.020/ 34|   1.019/ 35 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  76   |     789|      265.03|   1.023/ 30|   1.020/ 34|   1.020/ 35|   1.019/ 36 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  76   |     814|      132.57|   1.017/ 41|   1.013/ 52|   1.013/ 55|   1.012/ 59 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  68   |      17|       15.89|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  67   |     182|       94.04|   1.022/ 31|   1.017/ 40|   1.016/ 44|   1.015/ 48 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  79   |     437|      141.96|   1.010/ 67|   1.007/ 96|   1.006/ **|   1.006/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  72   |     268|      197.42|   1.025/ 28|   1.019/ 36|   1.018/ 39|   1.017/ 42 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  85   |   12318|     1386.79|   1.007/ 94|   1.004/ **|   1.003/ **|   1.002/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  70   |     386|      184.25|   1.021/ 33|   1.015/ 46|   1.014/ 50|   1.012/ 55 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  81   |   30495|     1567.59|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  70   |     980|       93.40|   1.022/ 31|   1.020/ 34|   1.020/ 35|   1.019/ 35 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  68   |      66|       85.98|   1.023/ 31|   1.019/ 36|   1.018/ 38|   1.017/ 40 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  75   |    2344|      200.56|   1.018/ 37|   1.015/ 47|   1.014/ 50|   1.013/ 53 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  76   |     342|       86.49|   1.009/ 76|   1.008/ 85|   1.008/ 88|   1.008/ 91 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  80   |     160|       37.88|   1.007/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  76   |    5943|      464.19|   1.013/ 53|   1.008/ 83|   1.007/ 96|   1.006/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  74   |     139|       43.50|   1.008/ 88|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  67   |     755|      712.64|   1.024/ 29|   1.022/ 32|   1.021/ 32|   1.021/ 33 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  79   |     515|      100.08|   1.016/ 43|   1.014/ 49|   1.014/ 50|   1.013/ 52 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  84   |      67|       76.29|   1.023/ 31|   1.019/ 37|   1.018/ 38|   1.017/ 40 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  74   |     387|       56.61|   1.015/ 47|   1.012/ 56|   1.012/ 59|   1.011/ 62 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  78   |    1796|       61.94|   1.016/ 44|   1.012/ 57|   1.011/ 62|   1.010/ 67 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  73   |     120|       37.35|   1.021/ 33|   1.017/ 40|   1.016/ 42|   1.015/ 45 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  75   |      55|       88.32|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  81   |    1476|      172.90|   1.020/ 35|   1.016/ 42|   1.016/ 44|   1.015/ 47 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  95   |    1164|      152.85|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  65   |      79|       44.32|   1.010/ 70|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  75   |     607|      104.24|   1.018/ 37|   1.018/ 38|   1.018/ 38|   1.018/ 38 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  51   |      18|       30.74|   1.036/ 19|   1.038/ 18|   1.039/ 18|   1.039/ 17 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  73   |     286|        8.88|   1.031/ 22|   1.026/ 27|   1.024/ 28|   1.023/ 30 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  84   |      33|       11.56|   1.003/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  83   |     670|       15.58|   1.012/ 55|   1.012/ 55|   1.012/ 55|   1.012/ 56 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  66   |       5|        0.14|   1.032/ 22|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  87   |     582|       12.94|   1.026/ 27|   1.024/ 28|   1.024/ 29|   1.024/ 29 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  69   |     141|       47.67|   1.063/ 11|   1.071/ 10|   1.074/  9|   1.076/  9 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  94   |     105|        4.08|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  83   |     668|       75.07|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  82   |      67|        6.66|   1.039/ 18|   1.041/ 17|   1.042/ 16|   1.042/ 16 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  79   |      18|       11.87|   1.038/ 18|   1.044/ 16|   1.045/ 15|   1.047/ 15 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  77   |     721|        4.28|   1.049/ 14|   1.049/ 14|   1.049/ 14|   1.049/ 14 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  64   |     250|       26.54|   1.025/ 28|   1.022/ 32|   1.021/ 33|   1.020/ 34 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  84   |    9706|      842.23|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  58   |       3|        0.28|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  66   |     372|       32.43|   1.045/ 15|   1.041/ 17|   1.040/ 17|   1.039/ 17 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  74   |     167|       50.66|   1.010/ 68|   1.003/ **|   1.002/ **|   1.000/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  64   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  78   |   33912|      160.41|   1.040/ 17|   1.034/ 20|   1.033/ 21|   1.031/ 22 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  84   |     151|       21.78|   1.017/ 42|   1.013/ 52|   1.013/ 55|   1.012/ 59 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  77   |      54|        2.58|   1.002/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  51   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  70   |     202|        7.61|   1.023/ 30|   1.023/ 31|   1.022/ 31|   1.022/ 31 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  86   |    7876|      207.26|   1.015/ 48|   1.011/ 66|   1.010/ 72|   1.009/ 81 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  11   |       5|        0.85|   1.000/ --|   1.260/  3|   1.508/  1|   1.618/  1 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  36   |      67|        4.13|   1.014/ 51|   1.008/ 91|   1.006/ **|   1.004/ ** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  73   |    1181|       61.81|   1.062/ 11|   1.065/ 11|   1.065/ 10|   1.066/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  84   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  73   |     987|       19.99|   1.035/ 20|   1.035/ 20|   1.035/ 20|   1.035/ 20 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  76   |      11|        2.20|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  76   |     106|       25.90|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  77   |      85|        7.55|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  81   |     585|      100.45|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  78   |     516|       49.83|   1.011/ 65|   1.009/ 75|   1.009/ 78|   1.009/ 80 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  81   |    3853|      220.60|   1.014/ 48|   1.007/ 99|   1.005/ **|   1.003/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  87   |     994|        9.92|   1.032/ 21|   1.034/ 20|   1.034/ 20|   1.035/ 20 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  64   |      50|        7.71|   1.038/ 18|   1.032/ 21|   1.031/ 22|   1.030/ 23 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  42   |      13|        9.69|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  59   |       7|        0.07|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  74   |     328|       59.33|   1.005/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 109   |   30041|      447.87|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  75   |      18|        8.29|   1.051/ 13|   1.057/ 12|   1.059/ 12|   1.060/ 11 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  72   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  60   |      12|        3.32|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  86   |    8787|      105.68|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  74   |      39|        1.29|   1.019/ 37|   1.014/ 50|   1.012/ 55|   1.011/ 61 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  84   |     181|       16.92|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  79   |     111|        6.67|   1.081/  8|   1.089/  8|   1.091/  7|   1.093/  7 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  49   |      24|        1.96|   1.023/ 30|   1.017/ 42|   1.015/ 46|   1.014/ 51 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  38   |       9|        5.33|   1.038/ 18|   1.019/ 37|   1.013/ 52|   1.008/ 86 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  59   |      45|        3.88|   1.057/ 12|   1.063/ 11|   1.065/ 11|   1.067/ 10 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  69   |     227|       24.74|   1.029/ 24|   1.028/ 25|   1.027/ 25|   1.027/ 26 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  80   |     547|       55.96|   1.009/ 73|   1.007/ 98|   1.006/ **|   1.006/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  84   |    6023|        4.42|   1.041/ 17|   1.038/ 18|   1.038/ 18|   1.037/ 19 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  84   |    1681|        6.30|   1.024/ 29|   1.024/ 28|   1.024/ 28|   1.024/ 28 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 104   |    7997|       95.91|   1.007/ 95|   1.007/ **|   1.007/ **|   1.007/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  91   |     202|        5.17|   1.038/ 18|   1.043/ 16|   1.044/ 16|   1.045/ 15 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  84   |    1701|      345.73|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  74   |     293|       31.89|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 103   |   34455|      571.98|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  76   |       9|        3.31|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 111   |    1034|        8.21|   1.011/ 64|   1.006/ **|   1.004/ **|   1.003/ ** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  68   |       9|        0.84|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  70   |      40|        2.14|   1.016/ 44|   1.019/ 37|   1.019/ 35|   1.020/ 34 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  69   |      69|        1.45|   1.029/ 24|   1.025/ 27|   1.025/ 28|   1.024/ 29 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  69   |      30|       16.88|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  60   |     240|       54.37|   1.048/ 14|   1.038/ 18|   1.036/ 19|   1.033/ 21 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  61   |      17|        2.58|   1.012/ 56|   1.011/ 64|   1.010/ 67|   1.010/ 70 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  61   |      25|       13.04|   1.012/ 58|   1.010/ 68|   1.010/ 71|   1.009/ 76 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  85   |      27|        3.90|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  60   |      29|        6.43|   1.014/ 50|   1.011/ 63|   1.010/ 68|   1.009/ 75 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  62   |       5|        0.70|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  74   |      72|       25.93|   1.014/ 48|   1.013/ 51|   1.013/ 52|   1.013/ 53 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  17   |       6|        0.23|   1.126/  5|   1.190/  3|   1.092/  7|   1.000/ -- |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  78   |     117|        3.57|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  66   |      84|        4.16|   1.027/ 25|   1.022/ 32|   1.020/ 34|   1.019/ 37 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  65   |      31|        7.62|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  76   |   11470|       90.62|   1.044/ 15|   1.039/ 18|   1.037/ 18|   1.036/ 19 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  77   |     321|      119.78|   1.024/ 29|   1.021/ 33|   1.020/ 35|   1.019/ 36 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  85   |     208|        5.79|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  18   |       9|        0.29|   1.105/  6|   1.123/  5|   1.111/  6|   1.098/  7 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  89   |    6126|      350.93|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  66   |      22|        4.40|   1.003/ **|   1.004/ **|   1.005/ **|   1.005/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  68   |      46|        7.14|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  70   |      69|        3.09|   1.011/ 64|   1.006/ **|   1.004/ **|   1.003/ ** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  72   |     313|        1.52|   1.033/ 21|   1.029/ 23|   1.029/ 24|   1.028/ 25 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  73   |     136|       65.45|   1.022/ 31|   1.025/ 28|   1.025/ 27|   1.026/ 26 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  81   |     240|       44.80|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  64   |      54|       11.66|   1.056/ 12|   1.056/ 12|   1.056/ 12|   1.056/ 12 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  76   |    1588|        7.24|   1.039/ 18|   1.038/ 18|   1.038/ 18|   1.038/ 18 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  84   |     354|       84.00|   1.015/ 46|   1.013/ 52|   1.013/ 54|   1.012/ 55 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  74   |      11|        1.57|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  75   |    4989|      155.27|   1.036/ 19|   1.032/ 22|   1.031/ 22|   1.030/ 23 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 122   |    1055|        9.72|   1.010/ 68|   1.007/ 93|   1.007/ **|   1.006/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  83   |    1128|       29.39|   1.010/ 69|   1.007/ 98|   1.006/ **|   1.006/ ** |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  78   |    1443|      140.39|   1.010/ 69|   1.010/ 72|   1.010/ 72|   1.009/ 73 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  67   |      41|       14.90|   1.069/ 10|   1.080/  9|   1.083/  8|   1.085/  8 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  73   |    1324|       68.25|   1.009/ 73|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  76   |    5171|       35.24|   1.041/ 17|   1.039/ 18|   1.038/ 18|   1.037/ 18 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  71   |     531|       15.53|   1.036/ 19|   1.038/ 18|   1.038/ 18|   1.038/ 18 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  63   |      47|        2.88|   1.030/ 23|   1.020/ 34|   1.018/ 39|   1.015/ 46 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  75   |     249|       35.81|   1.004/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  41   |      49|        6.16|   1.025/ 27|   1.010/ 66|   1.006/ **|   1.002/ ** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  74   |      24|        4.23|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  67   |      28|        5.20|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  81   |     110|       52.57|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  56   |      79|        4.95|   1.024/ 28|   1.027/ 25|   1.028/ 24|   1.029/ 24 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  68   |     769|       13.09|   1.063/ 11|   1.064/ 11|   1.064/ 11|   1.064/ 11 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  92   |   28086|      596.29|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  67   |      10|        0.48|   1.012/ 56|   1.017/ 42|   1.018/ 39|   1.019/ 37 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  82   |     296|        6.97|   1.071/ 10|   1.072/ 10|   1.072/  9|   1.072/  9 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  84   |    4621|      447.00|   1.012/ 58|   1.009/ 73|   1.009/ 78|   1.008/ 83 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  90   |    1952|      226.89|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  66   |       5|        0.27|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  64   |      21|        0.38|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  94   |      58|        0.87|   1.001/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  68   |      14|        1.80|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  70   |       8|        5.87|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  76   |      49|        4.17|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  78   |    4679|       56.27|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  95   |  111346|      337.88|   1.010/ 71|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  82   |     788|       18.81|   1.023/ 30|   1.018/ 38|   1.017/ 41|   1.016/ 44 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  75   |     282|       28.55|   1.010/ 67|   1.004/ **|   1.002/ **|   1.001/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  84   |   40179|      604.79|   1.007/ 92|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  66   |      23|        6.57|   1.009/ 81|   1.008/ 90|   1.007/ 93|   1.007/ 96 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  68   |      15|        0.45|   1.016/ 43|   1.016/ 44|   1.015/ 45|   1.015/ 45 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  68   |      11|        0.33|   1.042/ 17|   1.058/ 12|   1.062/ 11|   1.066/ 10 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  62   |       7|        0.40|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  72   |       4|        0.26|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |

