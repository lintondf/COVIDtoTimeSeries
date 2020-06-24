# State and Country COVID-19 Analysis #
## Updated: 2020-06-24 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# Notes #

- Expect discontinuities in the US around 4/14/2020 as the [CDC](CDC "https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html")  expanded the definition of a COVID-19 death.  
- There is also some weekly pattern to reporting with lower values on the weekend followed by higher values subsequently, at least in some places.

# Ten US States with Highest Death Tolls #

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. One per million is 0.0001%.  1% is 10,000 per million.

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDeathRates.png)

Daily Death Growth Rate (DDGR) in the 10 US States with the highest death tolls.

DDGR is the cube root of Arnold Kling's [Three Day Death Reproduction Rate (3DDRR)](http://www.arnoldkling.com/blog/the-3ddrr/).  The 3DDRR is calculated by dividing the cumulative total number of deaths on a given day by the  cumulative total number of deaths three days previously.  Taking the cube root converts this to the geometric mean for the three days.  These values are LOWESS filtered to generate a local-error minimizing non-parametric trend.

If deaths remain constant over the three days, the DDGR equals one.  A value of 2 would indicate that the number of deaths doubles every day.

![US States with Highest Death Toll - Daily Death Growth Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 102   |   31501|    1619.267|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 106   |   13334|    1501.171|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  96   |    8130|    1169.862|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  99   |    6989|     551.554|   1.007/ 92|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  97   |    6689|     522.460|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  97   |    6289|     629.730|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 112   |    5828|     147.497|   1.011/ 61|   1.010/ 68|   1.010/ 70|   1.009/ 73 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  97   |    4376|    1227.267|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 108   |    3297|     153.495|   1.011/ 65|   1.010/ 71|   1.009/ 73|   1.009/ 75 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 102   |    3175|     683.056|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 116   |  125192|     379.894|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  99   |   56397|     266.763|   1.022/ 32|   1.018/ 38|   1.017/ 40|   1.016/ 42 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 105   |   43895|     660.723|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 124   |   35219|     584.662|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 130   |   30212|     450.418|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 113   |   27591|     585.800|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  97   |   24417|     192.898|   1.034/ 20|   1.031/ 22|   1.031/ 23|   1.030/ 23 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 105   |   14621|      10.741|   1.034/ 20|   1.032/ 22|   1.032/ 22|   1.031/ 22 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 125   |    9630|     115.499|   1.011/ 66|   1.011/ 63|   1.011/ 62|   1.011/ 62 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 105   |    9813|     851.480|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  91   |     876|     178.760|   1.013/ 55|   1.011/ 61|   1.011/ 62|   1.011/ 64 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  91   |      12|      16.785|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  95   |    1411|     193.853|   1.017/ 40|   1.016/ 42|   1.016/ 42|   1.016/ 43 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  92   |     229|      75.783|   1.027/ 26|   1.028/ 24|   1.029/ 24|   1.029/ 24 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 112   |    5828|     147.497|   1.011/ 61|   1.010/ 68|   1.010/ 70|   1.009/ 73 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 102   |    1722|     298.985|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  97   |    4376|    1227.267|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  90   |     463|     475.149|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 108   |    3297|     153.495|   1.011/ 65|   1.010/ 71|   1.009/ 73|   1.009/ 75 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 104   |    2768|     260.708|   1.011/ 63|   1.010/ 69|   1.010/ 71|   1.010/ 72 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  85   |      17|      12.007|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  90   |      90|      50.472|   1.003/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  99   |    6989|     551.554|   1.007/ 92|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 100   |    2637|     391.691|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  91   |     737|     233.749|   1.007/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 103   |     262|      90.094|   1.007/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 100   |     552|     123.644|   1.008/ 90|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 102   |    3175|     683.056|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  89   |     108|      80.224|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  97   |    3216|     532.013|   1.007/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  96   |    8130|    1169.862|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  97   |    6289|     629.730|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  95   |    1521|     269.616|   1.011/ 64|   1.008/ 88|   1.007/ 97|   1.006/ ** |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  97   |    1024|     344.020|   1.010/ 67|   1.008/ 88|   1.007/ 95|   1.007/ ** |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  97   |     995|     162.113|   1.010/ 67|   1.009/ 74|   1.009/ 76|   1.009/ 78 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  89   |      20|      19.094|   1.011/ 64|   1.012/ 57|   1.013/ 55|   1.013/ 54 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  88   |     258|     133.321|   1.018/ 39|   1.017/ 41|   1.017/ 41|   1.017/ 42 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 100   |     499|     162.125|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  93   |     366|     269.487|   1.011/ 63|   1.008/ 88|   1.007/ 98|   1.006/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 106   |   13334|    1501.171|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  91   |     492|     234.407|   1.011/ 64|   1.009/ 77|   1.009/ 81|   1.008/ 85 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 102   |   31501|    1619.267|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  91   |    1306|     124.497|   1.013/ 53|   1.012/ 60|   1.011/ 61|   1.011/ 63 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  89   |      82|     107.537|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  96   |    2838|     242.772|   1.008/ 91|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  97   |     379|      95.827|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 101   |     192|      45.486|   1.010/ 71|   1.010/ 69|   1.010/ 69|   1.010/ 68 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  97   |    6689|     522.460|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  95   |     152|      47.666|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  88   |     947|     894.003|   1.008/ 84|   1.006/ **|   1.005/ **|   1.004/ ** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 100   |     682|     132.367|   1.013/ 54|   1.012/ 57|   1.012/ 58|   1.012/ 59 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 105   |      87|      97.882|   1.012/ 56|   1.011/ 65|   1.010/ 67|   1.010/ 70 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  95   |     549|      80.307|   1.016/ 43|   1.016/ 44|   1.015/ 45|   1.015/ 45 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  99   |    2265|      78.106|   1.012/ 59|   1.011/ 63|   1.011/ 64|   1.011/ 65 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  94   |     164|      51.164|   1.016/ 43|   1.015/ 45|   1.015/ 45|   1.015/ 46 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  96   |      56|      89.545|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 102   |    1722|     201.787|   1.006/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 116   |    1292|     169.728|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  86   |      93|      51.727|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  96   |     779|     133.818|   1.010/ 72|   1.008/ 86|   1.008/ 91|   1.007/ 96 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  72   |      20|      34.663|   1.009/ 74|   1.008/ 85|   1.008/ 87|   1.008/ 89 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  94   |     637|      19.774|   1.036/ 19|   1.036/ 19|   1.036/ 19|   1.036/ 19 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 105   |      40|      14.080|   1.017/ 42|   1.019/ 36|   1.020/ 34|   1.021/ 33 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 104   |     861|      20.014|   1.012/ 56|   1.012/ 55|   1.012/ 55|   1.012/ 55 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  87   |       7|       0.229|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 108   |    1075|      23.930|   1.030/ 23|   1.030/ 23|   1.030/ 23|   1.030/ 23 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  90   |     412|     139.370|   1.040/ 17|   1.036/ 19|   1.035/ 19|   1.034/ 20 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 115   |     103|       4.006|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 104   |     696|      78.147|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 103   |     169|      16.822|   1.042/ 17|   1.042/ 16|   1.042/ 16|   1.042/ 16 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 100   |      66|      42.506|   1.065/ 11|   1.069/ 10|   1.070/ 10|   1.071/ 10 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  98   |    1673|       9.931|   1.035/ 20|   1.032/ 21|   1.031/ 22|   1.031/ 22 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  85   |     365|      38.757|   1.017/ 40|   1.016/ 43|   1.016/ 44|   1.015/ 45 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 105   |    9813|     851.480|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  79   |      13|       1.070|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  87   |     866|      75.460|   1.039/ 18|   1.037/ 19|   1.037/ 19|   1.036/ 19 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  95   |     173|      52.424|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  85   |       1|       0.428|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  99   |   56397|     266.763|   1.022/ 32|   1.018/ 38|   1.017/ 40|   1.016/ 42 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 105   |     207|      29.829|   1.017/ 42|   1.016/ 43|   1.016/ 43|   1.016/ 43 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  98   |      53|       2.554|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  72   |       1|       0.091|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  91   |     302|      11.368|   1.013/ 53|   1.013/ 55|   1.013/ 55|   1.012/ 55 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 107   |    8962|     235.843|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  32   |      35|       6.400|   1.093/  7|   1.134/  5|   1.144/  5|   1.155/  4 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  57   |      75|       4.644|   1.004/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  94   |    5379|     281.532|   1.052/ 13|   1.049/ 14|   1.048/ 14|   1.047/ 15 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 105   |    4638|       3.308|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  94   |    2450|      49.591|   1.046/ 15|   1.048/ 14|   1.049/ 14|   1.049/ 14 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  97   |      12|       2.456|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  97   |     109|      26.710|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  98   |      85|       7.613|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 102   |     610|     104.683|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  99   |     668|      64.465|   1.014/ 48|   1.015/ 46|   1.015/ 45|   1.015/ 45 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 102   |    4337|     248.258|   1.009/ 75|   1.008/ 83|   1.008/ 86|   1.008/ 88 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 108   |    2240|      22.343|   1.043/ 16|   1.045/ 15|   1.045/ 15|   1.046/ 15 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  85   |     103|      15.804|   1.045/ 15|   1.048/ 14|   1.049/ 14|   1.050/ 14 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  63   |      34|      25.188|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  80   |     108|       1.096|   1.061/ 11|   1.048/ 14|   1.044/ 16|   1.040/ 17 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  95   |     331|      59.859|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 130   |   30212|     450.418|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  96   |      37|      16.848|   1.037/ 19|   1.038/ 18|   1.039/ 18|   1.039/ 18 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  93   |       1|       0.426|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  81   |      14|       3.851|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 107   |    9032|     108.629|   1.001/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  95   |      76|       2.522|   1.051/ 13|   1.058/ 12|   1.060/ 11|   1.062/ 11 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 105   |     192|      17.898|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 100   |     730|      43.941|   1.056/ 12|   1.052/ 13|   1.051/ 13|   1.050/ 14 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  70   |      27|       2.250|   1.011/ 65|   1.012/ 60|   1.012/ 58|   1.012/ 57 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  59   |      19|      11.926|   1.030/ 23|   1.034/ 20|   1.035/ 19|   1.037/ 19 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  80   |      99|       8.556|   1.031/ 22|   1.026/ 27|   1.024/ 28|   1.023/ 30 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  90   |     400|      43.622|   1.027/ 26|   1.026/ 26|   1.026/ 26|   1.026/ 26 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|       0.267|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 101   |     589|      60.289|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 105   |   14621|      10.741|   1.034/ 20|   1.032/ 22|   1.032/ 22|   1.031/ 22 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 105   |    2589|       9.701|   1.020/ 35|   1.019/ 36|   1.019/ 36|   1.019/ 36 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 125   |    9630|     115.499|   1.011/ 66|   1.011/ 63|   1.011/ 62|   1.011/ 62 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 112   |    1033|      26.402|   1.089/  8|   1.096/  7|   1.098/  7|   1.100/  7 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 105   |    1745|     354.634|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  95   |     310|      33.687|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 124   |   35219|     584.662|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  97   |      10|       3.770|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 132   |    1038|       8.242|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  89   |       9|       0.844|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  91   |     122|       6.504|   1.059/ 12|   1.066/ 10|   1.067/ 10|   1.069/ 10 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  90   |     132|       2.785|   1.029/ 24|   1.028/ 25|   1.028/ 25|   1.027/ 25 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  90   |      34|      19.028|   1.010/ 67|   1.012/ 56|   1.013/ 54|   1.013/ 52 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  81   |     354|      80.036|   1.015/ 45|   1.010/ 68|   1.009/ 78|   1.008/ 91 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  82   |      39|       5.938|   1.045/ 15|   1.050/ 14|   1.051/ 13|   1.052/ 13 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  82   |      31|      16.111|   1.010/ 68|   1.010/ 71|   1.010/ 71|   1.010/ 72 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 106   |      33|       4.826|   1.006/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  81   |      35|       7.790|   1.008/ 84|   1.007/ 99|   1.007/ **|   1.006/ ** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  83   |      12|       1.713|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  95   |      79|      28.305|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  38   |      15|       0.575|   1.035/ 20|   1.042/ 16|   1.044/ 16|   1.045/ 15 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  99   |     122|       3.717|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  87   |     119|       5.859|   1.012/ 56|   1.009/ 77|   1.008/ 86|   1.007/ 96 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  86   |     171|      41.895|   1.039/ 18|   1.033/ 21|   1.031/ 22|   1.029/ 24 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  97   |   24417|     192.898|   1.034/ 20|   1.031/ 22|   1.031/ 23|   1.030/ 23 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  98   |     494|     184.384|   1.022/ 31|   1.022/ 32|   1.022/ 32|   1.021/ 32 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 106   |     217|       6.050|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  30   |       5|       0.175|   1.080/  8|   1.068/ 10|   1.065/ 11|   1.062/ 11 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  39   |      25|       0.820|   1.038/ 18|   1.028/ 25|   1.025/ 27|   1.023/ 31 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 110   |    6189|     354.528|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  87   |      22|       4.446|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  89   |      79|      12.192|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  91   |      68|       3.043|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  93   |     548|       2.657|   1.027/ 25|   1.026/ 26|   1.026/ 27|   1.026/ 27 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  94   |     240|     115.614|   1.032/ 22|   1.034/ 20|   1.035/ 20|   1.035/ 19 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 102   |     246|      45.775|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  85   |     153|      32.881|   1.040/ 17|   1.036/ 19|   1.035/ 20|   1.034/ 21 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  97   |    3921|      17.878|   1.041/ 17|   1.041/ 17|   1.041/ 17|   1.041/ 17 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 105   |     519|     123.135|   1.020/ 34|   1.021/ 33|   1.021/ 33|   1.021/ 33 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  95   |      13|       1.767|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  96   |    8623|     268.359|   1.026/ 26|   1.024/ 28|   1.024/ 29|   1.023/ 29 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 143   |    1216|      11.206|   1.008/ 85|   1.007/ 97|   1.007/ **|   1.007/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 104   |    1382|      36.000|   1.010/ 66|   1.010/ 67|   1.010/ 68|   1.010/ 68 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  99   |    1587|     154.407|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  88   |     111|      40.365|   1.039/ 18|   1.033/ 21|   1.031/ 22|   1.030/ 23 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  94   |    1530|      78.845|   1.009/ 80|   1.009/ 79|   1.009/ 79|   1.009/ 78 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  97   |    9024|      61.497|   1.022/ 31|   1.019/ 37|   1.018/ 38|   1.017/ 41 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  25   |       2|       0.162|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  92   |    1399|      40.884|   1.043/ 16|   1.042/ 16|   1.042/ 16|   1.042/ 16 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  84   |      86|       5.289|   1.038/ 18|   1.041/ 17|   1.042/ 17|   1.042/ 16 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  96   |     262|      37.683|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  62   |      55|       6.914|   1.009/ 76|   1.010/ 68|   1.010/ 67|   1.011/ 65 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  95   |      27|       4.671|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  88   |      28|       5.132|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 102   |     110|      52.531|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  77   |      93|       5.851|   1.005/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  89   |    2299|      39.117|   1.045/ 15|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|       1.044|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 113   |   27591|     585.800|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  88   |      11|       0.522|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 103   |     664|      15.653|   1.025/ 28|   1.018/ 38|   1.017/ 41|   1.015/ 46 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 105   |    5298|     512.426|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 111   |    1962|     228.067|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  87   |       7|       0.428|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  85   |      21|       0.376|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 115   |      59|       0.880|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  89   |      13|       1.742|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  91   |       8|       5.865|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  97   |      50|       4.284|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  99   |    5026|      60.438|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 116   |  125192|     379.894|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 103   |    1067|      25.489|   1.015/ 45|   1.014/ 50|   1.013/ 51|   1.013/ 53 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  96   |     310|      31.356|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 105   |   43895|     660.723|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  87   |      25|       7.025|   1.006/ **|   1.006/ **|   1.007/ **|   1.007/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  89   |      21|       0.604|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  89   |      35|       1.090|   1.036/ 19|   1.038/ 18|   1.038/ 18|   1.039/ 18 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  83   |      12|       0.695|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  93   |       4|       0.264|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |

