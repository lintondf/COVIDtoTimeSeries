# State and Country COVID-19 Analysis #
## Updated: 2020-06-02 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  80   |   30450|     1565.27|   1.004/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  84   |   12293|     1383.98|   1.008/ 87|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  74   |    7192|     1034.95|   1.012/ 56|   1.009/ 78|   1.008/ 87|   1.007/ 97 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  75   |    5881|      459.37|   1.014/ 50|   1.009/ 78|   1.008/ 90|   1.006/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  75   |    5608|      561.57|   1.008/ 91|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  77   |    5746|      453.43|   1.018/ 39|   1.013/ 53|   1.012/ 58|   1.011/ 64 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  90   |    4455|      112.74|   1.017/ 40|   1.014/ 48|   1.014/ 50|   1.013/ 53 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  75   |    4105|     1151.48|   1.011/ 65|   1.008/ 91|   1.007/ **|   1.006/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  80   |    2895|      622.78|   1.007/ 95|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  75   |    2671|      441.88|   1.017/ 41|   1.013/ 54|   1.012/ 59|   1.011/ 65 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  94   |  110735|      336.02|   1.010/ 68|   1.007/ 94|   1.007/ **|   1.006/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  83   |   39892|      600.47|   1.007/ 92|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 102   |   34430|      571.56|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  77   |   32766|      154.99|   1.042/ 16|   1.036/ 19|   1.035/ 20|   1.034/ 21 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 108   |   30066|      448.25|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  91   |   28162|      597.92|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  75   |   11053|       87.32|   1.046/ 15|   1.041/ 17|   1.040/ 17|   1.039/ 18 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  83   |    9687|      840.53|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  85   |    8762|      105.38|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 103   |    7937|       95.19|   1.007/ 97|   1.007/ **|   1.006/ **|   1.006/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  69   |     656|      133.71|   1.018/ 38|   1.015/ 47|   1.014/ 50|   1.013/ 53 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  69   |      10|       13.71|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  73   |     976|      134.05|   1.021/ 33|   1.015/ 48|   1.013/ 53|   1.012/ 60 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  70   |     135|       44.59|   1.019/ 36|   1.020/ 35|   1.020/ 34|   1.020/ 34 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  90   |    4455|      112.74|   1.017/ 40|   1.014/ 48|   1.014/ 50|   1.013/ 53 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  80   |    1541|      267.61|   1.014/ 48|   1.011/ 62|   1.010/ 67|   1.009/ 73 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  75   |    4105|     1151.48|   1.011/ 65|   1.008/ 91|   1.007/ **|   1.006/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  68   |     387|      397.16|   1.018/ 39|   1.013/ 55|   1.011/ 61|   1.010/ 69 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  86   |    2600|      121.03|   1.015/ 48|   1.011/ 61|   1.011/ 65|   1.010/ 70 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  82   |    2120|      199.65|   1.016/ 43|   1.014/ 48|   1.014/ 49|   1.014/ 50 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  63   |      17|       12.01|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  68   |      84|       47.11|   1.007/ 95|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  77   |    5746|      453.43|   1.018/ 39|   1.013/ 53|   1.012/ 58|   1.011/ 64 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  78   |    2266|      336.60|   1.013/ 53|   1.009/ 80|   1.008/ 91|   1.007/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  69   |     583|      184.65|   1.030/ 23|   1.025/ 27|   1.024/ 29|   1.023/ 30 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  81   |     226|       77.63|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  78   |     446|       99.76|   1.016/ 44|   1.014/ 48|   1.014/ 50|   1.014/ 51 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  80   |    2895|      622.78|   1.007/ 95|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  67   |      89|       65.84|   1.017/ 40|   1.019/ 36|   1.020/ 35|   1.020/ 34 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  75   |    2671|      441.88|   1.017/ 41|   1.013/ 54|   1.012/ 59|   1.011/ 65 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  74   |    7192|     1034.95|   1.012/ 56|   1.009/ 78|   1.008/ 87|   1.007/ 97 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  75   |    5608|      561.57|   1.008/ 91|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  73   |    1103|      195.50|   1.026/ 26|   1.022/ 31|   1.022/ 32|   1.021/ 33 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  75   |     772|      259.34|   1.024/ 29|   1.021/ 33|   1.020/ 35|   1.019/ 36 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  75   |     802|      130.72|   1.018/ 38|   1.015/ 46|   1.014/ 48|   1.014/ 51 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  67   |      17|       15.83|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  66   |     180|       92.95|   1.025/ 28|   1.021/ 33|   1.020/ 35|   1.019/ 37 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  78   |     435|      141.34|   1.012/ 60|   1.009/ 79|   1.008/ 86|   1.007/ 94 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  71   |     263|      193.29|   1.025/ 27|   1.019/ 36|   1.018/ 39|   1.016/ 43 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  84   |   12293|     1383.98|   1.008/ 87|   1.005/ **|   1.004/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  69   |     380|      181.30|   1.022/ 32|   1.016/ 43|   1.015/ 47|   1.013/ 52 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  80   |   30450|     1565.27|   1.004/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  69   |     960|       91.55|   1.023/ 30|   1.022/ 32|   1.022/ 32|   1.021/ 32 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  67   |      64|       83.97|   1.022/ 31|   1.018/ 38|   1.017/ 41|   1.016/ 44 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  74   |    2313|      197.84|   1.019/ 36|   1.015/ 45|   1.014/ 49|   1.013/ 52 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  75   |     342|       86.33|   1.011/ 63|   1.011/ 66|   1.010/ 66|   1.010/ 67 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  79   |     159|       37.62|   1.007/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  75   |    5881|      459.37|   1.014/ 50|   1.009/ 78|   1.008/ 90|   1.006/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  73   |     138|       43.15|   1.008/ 91|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  66   |     741|      699.30|   1.025/ 28|   1.024/ 29|   1.024/ 29|   1.024/ 29 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  78   |     509|       98.92|   1.017/ 41|   1.015/ 45|   1.015/ 47|   1.014/ 48 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  83   |      66|       74.98|   1.026/ 27|   1.023/ 30|   1.022/ 31|   1.021/ 32 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  73   |     381|       55.80|   1.015/ 47|   1.012/ 56|   1.012/ 59|   1.011/ 63 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  77   |    1773|       61.14|   1.017/ 42|   1.013/ 54|   1.012/ 59|   1.011/ 64 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  72   |     118|       36.88|   1.023/ 30|   1.020/ 35|   1.019/ 36|   1.018/ 38 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  74   |      55|       88.22|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  80   |    1455|      170.50|   1.021/ 32|   1.018/ 38|   1.017/ 40|   1.017/ 42 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  94   |    1159|      152.17|   1.007/ 93|   1.006/ **|   1.006/ **|   1.005/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  64   |      79|       44.09|   1.010/ 69|   1.005/ **|   1.003/ **|   1.002/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  74   |     596|      102.43|   1.019/ 36|   1.019/ 36|   1.019/ 36|   1.019/ 36 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  50   |      17|       29.94|   1.037/ 19|   1.042/ 16|   1.043/ 16|   1.044/ 15 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  72   |     280|        8.70|   1.032/ 22|   1.026/ 26|   1.025/ 28|   1.023/ 29 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  83   |      33|       11.52|   1.004/ **|   1.004/ **|   1.004/ **|   1.005/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  82   |     662|       15.40|   1.013/ 55|   1.013/ 54|   1.013/ 54|   1.013/ 54 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  65   |       4|        0.14|   1.038/ 18|   1.004/ **|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  86   |     568|       12.64|   1.026/ 26|   1.025/ 28|   1.024/ 28|   1.024/ 29 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  68   |     130|       44.01|   1.061/ 11|   1.070/ 10|   1.072/ 10|   1.074/  9 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  93   |     105|        4.08|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  82   |     666|       74.80|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  81   |      64|        6.39|   1.037/ 18|   1.039/ 18|   1.040/ 17|   1.040/ 17 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  78   |      18|       11.41|   1.038/ 18|   1.044/ 16|   1.046/ 15|   1.047/ 15 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  76   |     688|        4.08|   1.049/ 14|   1.049/ 14|   1.049/ 14|   1.049/ 14 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  63   |     245|       25.99|   1.025/ 27|   1.022/ 31|   1.022/ 32|   1.021/ 33 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  83   |    9687|      840.53|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  57   |       3|        0.28|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  65   |     354|       30.84|   1.044/ 16|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  73   |     166|       50.35|   1.011/ 63|   1.004/ **|   1.002/ **|   1.000/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  63   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  77   |   32766|      154.99|   1.042/ 16|   1.036/ 19|   1.035/ 20|   1.034/ 21 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  83   |     149|       21.48|   1.017/ 40|   1.014/ 49|   1.013/ 52|   1.013/ 55 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  76   |      54|        2.58|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  50   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  69   |     198|        7.46|   1.024/ 29|   1.024/ 29|   1.024/ 29|   1.024/ 29 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  85   |    7776|      204.64|   1.015/ 47|   1.010/ 66|   1.009/ 74|   1.008/ 84 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  10   |       4|        0.68|   1.000/ **|   1.000/ --|   1.260/  2|   1.587/  1 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  35   |      67|        4.11|   1.015/ 45|   1.009/ 78|   1.007/ 95|   1.006/ ** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  72   |    1108|       57.98|   1.062/ 11|   1.065/ 10|   1.066/ 10|   1.066/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  83   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  72   |     952|       19.26|   1.034/ 20|   1.033/ 21|   1.033/ 21|   1.033/ 21 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  75   |      11|        2.21|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  75   |     105|       25.84|   1.005/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  76   |      85|        7.55|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  80   |     584|      100.30|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  77   |     510|       49.26|   1.011/ 65|   1.009/ 77|   1.009/ 81|   1.008/ 84 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  80   |    3860|      220.95|   1.016/ 44|   1.008/ 88|   1.006/ **|   1.004/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  86   |     959|        9.57|   1.031/ 22|   1.032/ 22|   1.032/ 22|   1.032/ 21 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  63   |      48|        7.43|   1.040/ 17|   1.035/ 20|   1.034/ 20|   1.033/ 21 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  41   |      13|        9.74|   1.009/ 79|   1.006/ **|   1.004/ **|   1.003/ ** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  58   |       7|        0.07|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  73   |     327|       59.15|   1.005/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 108   |   30066|      448.25|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  74   |      17|        7.92|   1.023/ 31|   1.018/ 39|   1.017/ 41|   1.015/ 45 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  71   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  59   |      12|        3.28|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  85   |    8762|      105.38|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  73   |      38|        1.27|   1.018/ 37|   1.013/ 53|   1.012/ 59|   1.010/ 68 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  83   |     180|       16.83|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  78   |     101|        6.08|   1.082/  8|   1.091/  7|   1.094/  7|   1.096/  7 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  48   |      24|        1.94|   1.026/ 27|   1.021/ 33|   1.020/ 35|   1.019/ 37 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  37   |       8|        5.29|   1.046/ 15|   1.024/ 29|   1.019/ 37|   1.014/ 50 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  58   |      43|        3.68|   1.059/ 12|   1.067/ 10|   1.070/ 10|   1.072/  9 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  68   |     221|       24.08|   1.028/ 24|   1.026/ 26|   1.025/ 27|   1.025/ 28 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  79   |     542|       55.50|   1.010/ 69|   1.008/ 92|   1.007/ **|   1.006/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  83   |    5790|        4.25|   1.041/ 17|   1.038/ 18|   1.038/ 18|   1.037/ 19 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  83   |    1644|        6.16|   1.024/ 28|   1.025/ 28|   1.025/ 27|   1.025/ 27 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 103   |    7937|       95.19|   1.007/ 97|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  90   |     194|        4.97|   1.036/ 19|   1.040/ 17|   1.041/ 17|   1.042/ 16 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  83   |    1698|      345.00|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  73   |     292|       31.77|   1.003/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 102   |   34430|      571.56|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  75   |       9|        3.31|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 110   |    1032|        8.20|   1.012/ 58|   1.007/ **|   1.005/ **|   1.004/ ** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  67   |       9|        0.84|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  69   |      39|        2.09|   1.012/ 57|   1.013/ 53|   1.013/ 52|   1.014/ 51 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  68   |      67|        1.41|   1.028/ 25|   1.023/ 30|   1.022/ 31|   1.021/ 32 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  68   |      30|       16.89|   1.002/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  59   |     231|       52.35|   1.050/ 14|   1.040/ 17|   1.037/ 18|   1.035/ 20 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  60   |      17|        2.54|   1.012/ 59|   1.009/ 74|   1.009/ 79|   1.008/ 86 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  60   |      25|       12.95|   1.013/ 52|   1.012/ 56|   1.012/ 57|   1.012/ 59 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  84   |      27|        3.89|   1.002/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  59   |      28|        6.37|   1.014/ 49|   1.012/ 57|   1.011/ 61|   1.010/ 66 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  61   |       5|        0.67|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  73   |      72|       25.61|   1.015/ 45|   1.015/ 46|   1.015/ 46|   1.015/ 46 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  16   |       7|        0.27|   1.000/ --|   1.364/  2|   1.321/  2|   1.260/  3 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  77   |     117|        3.57|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  65   |      83|        4.08|   1.030/ 23|   1.025/ 28|   1.024/ 29|   1.022/ 31 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  64   |      27|        6.53|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  75   |   11053|       87.32|   1.046/ 15|   1.041/ 17|   1.040/ 17|   1.039/ 18 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  76   |     315|      117.65|   1.025/ 28|   1.022/ 32|   1.021/ 33|   1.020/ 34 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  84   |     207|        5.77|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  17   |       8|        0.28|   1.099/  7|   1.135/  5|   1.138/  5|   1.139/  5 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  88   |    6126|      350.90|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  65   |      22|        4.39|   1.004/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  67   |      42|        6.51|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  69   |      69|        3.08|   1.012/ 58|   1.007/ **|   1.005/ **|   1.004/ ** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  71   |     303|        1.47|   1.032/ 22|   1.026/ 26|   1.025/ 27|   1.024/ 29 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  72   |     132|       63.78|   1.022/ 32|   1.024/ 28|   1.025/ 28|   1.026/ 27 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  80   |     241|       44.82|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  63   |      51|       10.90|   1.051/ 14|   1.047/ 14|   1.046/ 15|   1.045/ 15 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  75   |    1524|        6.95|   1.037/ 18|   1.036/ 19|   1.035/ 20|   1.035/ 20 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  83   |     349|       82.68|   1.014/ 48|   1.012/ 56|   1.012/ 58|   1.011/ 61 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  73   |      11|        1.57|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  74   |    4860|      151.24|   1.039/ 18|   1.035/ 20|   1.034/ 21|   1.033/ 21 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 121   |    1045|        9.63|   1.011/ 64|   1.008/ 86|   1.007/ 94|   1.007/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  82   |    1121|       29.21|   1.010/ 67|   1.007/ 96|   1.006/ **|   1.006/ ** |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  77   |    1429|      139.03|   1.010/ 69|   1.010/ 72|   1.010/ 72|   1.009/ 73 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  66   |      38|       13.78|   1.069/ 10|   1.082/  8|   1.085/  8|   1.088/  8 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  72   |    1318|       67.93|   1.010/ 70|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  75   |    4976|       33.91|   1.042/ 16|   1.039/ 17|   1.039/ 18|   1.038/ 18 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  70   |     511|       14.94|   1.035/ 19|   1.036/ 19|   1.036/ 19|   1.036/ 19 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  62   |      46|        2.85|   1.033/ 21|   1.023/ 30|   1.021/ 33|   1.018/ 38 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  74   |     249|       35.79|   1.004/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  40   |      49|        6.17|   1.029/ 24|   1.015/ 46|   1.011/ 61|   1.007/ 95 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  73   |      24|        4.21|   1.004/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  66   |      28|        5.21|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  80   |     110|       52.53|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  55   |      77|        4.84|   1.024/ 29|   1.027/ 26|   1.027/ 25|   1.028/ 24 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  67   |     725|       12.34|   1.064/ 11|   1.065/ 10|   1.065/ 10|   1.065/ 10 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  91   |   28162|      597.92|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  66   |      10|        0.47|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  81   |     275|        6.49|   1.073/  9|   1.074/  9|   1.074/  9|   1.075/  9 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  83   |    4574|      442.40|   1.013/ 55|   1.010/ 67|   1.010/ 71|   1.009/ 75 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  89   |    1951|      226.81|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  65   |       5|        0.26|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  63   |      21|        0.38|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  93   |      57|        0.86|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  67   |      13|        1.79|   1.007/ 93|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  69   |       8|        5.87|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  75   |      49|        4.17|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  77   |    4654|       55.97|   1.007/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  94   |  110735|      336.02|   1.010/ 68|   1.007/ 94|   1.007/ **|   1.006/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  81   |     774|       18.47|   1.024/ 29|   1.019/ 36|   1.018/ 38|   1.017/ 41 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  74   |     282|       28.51|   1.011/ 62|   1.004/ **|   1.003/ **|   1.001/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  83   |   39892|      600.47|   1.007/ 92|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  65   |      23|        6.51|   1.008/ 88|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  67   |      15|        0.44|   1.015/ 45|   1.015/ 47|   1.014/ 48|   1.014/ 49 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  67   |      11|        0.33|   1.017/ 40|   1.025/ 28|   1.027/ 25|   1.029/ 24 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  61   |       7|        0.40|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  71   |       4|        0.26|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |

