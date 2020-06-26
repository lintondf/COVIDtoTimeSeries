# State and Country COVID-19 Analysis #
## Updated: 2020-06-26 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 104   |   31569|    1622.765|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 108   |   13564|    1527.058|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  98   |    8177|    1176.671|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 101   |    7065|     557.557|   1.007/ 99|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  99   |    6734|     526.018|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  99   |    6304|     631.239|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 114   |    5955|     150.718|   1.011/ 60|   1.010/ 67|   1.010/ 69|   1.010/ 70 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  99   |    4387|    1230.379|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 110   |    3367|     156.787|   1.011/ 63|   1.010/ 67|   1.010/ 68|   1.010/ 70 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 104   |    3198|     687.992|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 118   |  126413|     383.600|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 101   |   58476|     276.598|   1.021/ 33|   1.018/ 39|   1.017/ 40|   1.016/ 42 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 107   |   44129|     664.244|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 126   |   35248|     585.133|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 132   |   30222|     450.561|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 115   |   27755|     589.278|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  99   |   26008|     205.474|   1.034/ 20|   1.031/ 22|   1.031/ 22|   1.030/ 23 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 107   |   15844|      11.639|   1.033/ 21|   1.031/ 22|   1.030/ 23|   1.030/ 23 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 127   |    9858|     118.233|   1.011/ 63|   1.012/ 60|   1.012/ 59|   1.012/ 59 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 107   |    9816|     851.752|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  93   |     901|     183.717|   1.014/ 50|   1.013/ 53|   1.013/ 53|   1.013/ 54 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  93   |      12|      16.952|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  97   |    1471|     202.098|   1.019/ 36|   1.019/ 36|   1.019/ 36|   1.019/ 36 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  94   |     241|      79.787|   1.026/ 27|   1.027/ 26|   1.027/ 25|   1.027/ 25 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 114   |    5955|     150.718|   1.011/ 60|   1.010/ 67|   1.010/ 69|   1.010/ 70 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 104   |    1729|     300.263|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  99   |    4387|    1230.379|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  92   |     480|     493.313|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 110   |    3367|     156.787|   1.011/ 63|   1.010/ 67|   1.010/ 68|   1.010/ 70 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 106   |    2820|     265.618|   1.011/ 65|   1.010/ 72|   1.009/ 74|   1.009/ 76 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  87   |      17|      12.007|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  92   |      91|      50.715|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 101   |    7065|     557.557|   1.007/ 99|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 102   |    2663|     395.526|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  93   |     740|     234.651|   1.006/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 105   |     266|      91.139|   1.006/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 102   |     559|     125.221|   1.008/ 89|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 104   |    3198|     687.992|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  91   |     108|      80.157|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  99   |    3245|     536.751|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  98   |    8177|    1176.671|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  99   |    6304|     631.239|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  97   |    1539|     272.886|   1.009/ 74|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  99   |    1044|     350.888|   1.011/ 63|   1.009/ 76|   1.009/ 80|   1.008/ 84 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  99   |    1012|     164.907|   1.010/ 73|   1.009/ 81|   1.008/ 83|   1.008/ 86 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  91   |      21|      19.512|   1.011/ 65|   1.012/ 59|   1.012/ 57|   1.012/ 56 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  90   |     266|     137.537|   1.017/ 40|   1.017/ 42|   1.016/ 42|   1.016/ 42 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 102   |     504|     163.663|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  95   |     372|     273.907|   1.011/ 65|   1.008/ 88|   1.007/ 97|   1.006/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 108   |   13564|    1527.058|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  93   |     500|     238.472|   1.010/ 67|   1.009/ 80|   1.008/ 84|   1.008/ 88 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 104   |   31569|    1622.765|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  93   |    1342|     127.965|   1.014/ 50|   1.013/ 53|   1.013/ 53|   1.013/ 54 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  91   |      82|     107.962|   1.005/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  98   |    2870|     245.501|   1.007/ 95|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  99   |     381|      96.325|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 103   |     196|      46.443|   1.010/ 69|   1.010/ 68|   1.010/ 67|   1.010/ 67 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  99   |    6734|     526.018|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  97   |     153|      47.871|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  90   |     957|     903.233|   1.008/ 92|   1.005/ **|   1.005/ **|   1.004/ ** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 102   |     699|     135.776|   1.013/ 52|   1.013/ 55|   1.013/ 55|   1.012/ 56 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 107   |      89|     100.286|   1.013/ 53|   1.012/ 59|   1.011/ 61|   1.011/ 63 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  97   |     567|      83.020|   1.017/ 42|   1.016/ 42|   1.016/ 42|   1.016/ 42 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 101   |    2320|      80.010|   1.012/ 57|   1.012/ 60|   1.011/ 61|   1.011/ 61 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  96   |     169|      52.580|   1.015/ 45|   1.015/ 47|   1.014/ 48|   1.014/ 49 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  98   |      56|      89.729|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 104   |    1738|     203.567|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 118   |    1307|     171.630|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  88   |      94|      52.225|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  98   |     791|     135.786|   1.009/ 78|   1.007/ 94|   1.007/ 99|   1.007/ ** |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  74   |      20|      35.110|   1.007/ 95|   1.006/ **|   1.006/ **|   1.005/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  96   |     683|      21.204|   1.036/ 19|   1.036/ 19|   1.036/ 19|   1.036/ 19 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 107   |      43|      14.943|   1.020/ 35|   1.023/ 30|   1.024/ 29|   1.024/ 28 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 106   |     881|      20.491|   1.012/ 58|   1.012/ 58|   1.012/ 58|   1.012/ 58 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  89   |      10|       0.326|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 110   |    1142|      25.419|   1.030/ 23|   1.031/ 22|   1.031/ 22|   1.031/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  92   |     439|     148.370|   1.038/ 18|   1.034/ 20|   1.033/ 21|   1.032/ 21 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 117   |     103|       4.015|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 106   |     698|      78.427|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 105   |     183|      18.208|   1.041/ 17|   1.041/ 17|   1.041/ 17|   1.041/ 17 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 102   |      73|      47.519|   1.060/ 11|   1.063/ 11|   1.063/ 11|   1.064/ 11 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 100   |    1773|      10.525|   1.033/ 21|   1.030/ 23|   1.029/ 24|   1.028/ 24 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  87   |     376|      39.940|   1.017/ 42|   1.015/ 45|   1.015/ 46|   1.015/ 47 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 107   |    9816|     851.752|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  81   |      14|       1.234|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  89   |     931|      81.137|   1.039/ 18|   1.037/ 18|   1.037/ 19|   1.037/ 19 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  97   |     175|      52.991|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  87   |       1|       0.428|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 101   |   58476|     276.598|   1.021/ 33|   1.018/ 39|   1.017/ 40|   1.016/ 42 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 107   |     214|      30.742|   1.016/ 44|   1.015/ 45|   1.015/ 45|   1.015/ 46 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 100   |      53|       2.552|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  74   |       1|       0.091|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  93   |     316|      11.896|   1.012/ 56|   1.012/ 59|   1.012/ 59|   1.012/ 60 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 109   |    9002|     236.891|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  34   |      44|       8.016|   1.109/  6|   1.141/  5|   1.150/  4|   1.160/  4 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  59   |      75|       4.637|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  96   |    5890|     308.243|   1.046/ 15|   1.042/ 16|   1.041/ 17|   1.039/ 17 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 107   |    4639|       3.308|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  96   |    2655|      53.740|   1.044/ 16|   1.044/ 16|   1.044/ 15|   1.045/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  99   |      13|       2.472|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  99   |     109|      26.708|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 100   |      85|       7.624|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 104   |     611|     104.851|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 101   |     689|      66.485|   1.014/ 48|   1.015/ 46|   1.015/ 45|   1.016/ 45 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 104   |    4404|     252.143|   1.009/ 79|   1.008/ 88|   1.008/ 90|   1.007/ 92 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 110   |    2442|      24.349|   1.042/ 16|   1.044/ 16|   1.044/ 15|   1.045/ 15 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  87   |     114|      17.567|   1.048/ 14|   1.052/ 13|   1.053/ 13|   1.055/ 13 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  65   |      37|      27.282|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  82   |     116|       1.171|   1.047/ 14|   1.033/ 21|   1.029/ 24|   1.025/ 27 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  97   |     331|      59.838|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 132   |   30222|     450.561|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  98   |      39|      18.174|   1.036/ 19|   1.037/ 19|   1.037/ 18|   1.038/ 18 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  95   |       1|       0.426|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  83   |      14|       3.864|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 109   |    9047|     108.802|   1.001/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  97   |      86|       2.854|   1.051/ 13|   1.057/ 12|   1.058/ 12|   1.060/ 11 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 107   |     193|      17.973|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 102   |     803|      48.371|   1.053/ 13|   1.048/ 14|   1.047/ 15|   1.046/ 15 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  72   |      28|       2.325|   1.013/ 51|   1.016/ 44|   1.016/ 43|   1.017/ 42 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  61   |      20|      12.421|   1.027/ 25|   1.032/ 22|   1.033/ 21|   1.034/ 21 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  82   |     104|       8.941|   1.029/ 24|   1.023/ 29|   1.022/ 31|   1.021/ 33 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  92   |     423|      46.183|   1.028/ 24|   1.028/ 24|   1.028/ 24|   1.028/ 24 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|       0.267|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 103   |     591|      60.481|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 107   |   15844|      11.639|   1.033/ 21|   1.031/ 22|   1.030/ 23|   1.030/ 23 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 107   |    2684|      10.056|   1.019/ 36|   1.018/ 38|   1.018/ 38|   1.018/ 38 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 127   |    9858|     118.233|   1.011/ 63|   1.012/ 60|   1.012/ 59|   1.012/ 59 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 114   |    1238|      31.652|   1.089/  8|   1.096/  7|   1.098/  7|   1.100/  7 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 107   |    1748|     355.140|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  97   |     311|      33.831|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 126   |   35248|     585.133|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  99   |      10|       3.770|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 134   |    1037|       8.236|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  91   |       9|       0.844|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  93   |     136|       7.304|   1.057/ 12|   1.062/ 11|   1.063/ 11|   1.064/ 11 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  92   |     139|       2.918|   1.027/ 26|   1.025/ 27|   1.025/ 28|   1.024/ 28 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  92   |      35|      19.608|   1.012/ 57|   1.015/ 48|   1.015/ 46|   1.016/ 44 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  83   |     360|      81.477|   1.014/ 50|   1.009/ 78|   1.008/ 91|   1.006/ ** |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  84   |      42|       6.482|   1.042/ 16|   1.045/ 15|   1.046/ 15|   1.046/ 15 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  84   |      31|      16.309|   1.008/ 83|   1.007/ 95|   1.007/ 99|   1.007/ ** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 108   |      33|       4.897|   1.007/ **|   1.007/ 99|   1.007/ 99|   1.007/ 99 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  83   |      35|       7.855|   1.007/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  85   |      14|       2.069|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  97   |      79|      28.455|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  40   |      16|       0.623|   1.035/ 20|   1.038/ 18|   1.039/ 17|   1.040/ 17 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 101   |     122|       3.726|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  89   |     120|       5.940|   1.011/ 63|   1.008/ 91|   1.007/ **|   1.006/ ** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  88   |     175|      43.041|   1.032/ 22|   1.024/ 28|   1.022/ 31|   1.021/ 34 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  99   |   26008|     205.474|   1.034/ 20|   1.031/ 22|   1.031/ 22|   1.030/ 23 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 100   |     514|     191.730|   1.021/ 33|   1.020/ 34|   1.020/ 34|   1.020/ 34 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 108   |     218|       6.072|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  32   |       5|       0.179|   1.072/  9|   1.034/ 20|   1.025/ 27|   1.016/ 43 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  41   |      26|       0.860|   1.034/ 20|   1.026/ 26|   1.024/ 29|   1.022/ 31 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 112   |    6190|     354.565|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  89   |      22|       4.441|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  91   |      81|      12.540|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  93   |      68|       3.042|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  95   |     573|       2.780|   1.025/ 28|   1.024/ 29|   1.023/ 30|   1.023/ 30 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  96   |     256|     123.480|   1.031/ 22|   1.033/ 21|   1.034/ 20|   1.034/ 20 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 104   |     247|      46.030|   1.002/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  87   |     162|      34.815|   1.036/ 19|   1.031/ 22|   1.030/ 23|   1.029/ 24 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  99   |    4211|      19.199|   1.039/ 18|   1.038/ 18|   1.037/ 18|   1.037/ 19 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 107   |     543|     128.808|   1.022/ 32|   1.023/ 31|   1.023/ 30|   1.023/ 30 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  97   |      13|       1.803|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  98   |    9047|     281.552|   1.026/ 27|   1.024/ 28|   1.024/ 29|   1.023/ 29 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 145   |    1237|      11.398|   1.008/ 84|   1.007/ 93|   1.007/ 96|   1.007/ 99 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 106   |    1412|      36.781|   1.011/ 65|   1.011/ 66|   1.010/ 66|   1.010/ 66 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 101   |    1589|     154.666|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  90   |     118|      42.848|   1.035/ 20|   1.028/ 25|   1.026/ 26|   1.025/ 28 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  96   |    1558|      80.296|   1.009/ 78|   1.009/ 77|   1.009/ 76|   1.009/ 76 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  99   |    9331|      63.585|   1.021/ 33|   1.017/ 40|   1.016/ 43|   1.015/ 45 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  27   |       2|       0.162|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  94   |    1507|      44.053|   1.040/ 17|   1.039/ 18|   1.039/ 18|   1.038/ 18 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  86   |      93|       5.720|   1.037/ 18|   1.040/ 17|   1.040/ 17|   1.041/ 17 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  98   |     264|      37.922|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  64   |      56|       7.032|   1.008/ 85|   1.008/ 83|   1.008/ 82|   1.009/ 81 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  97   |      27|       4.683|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  90   |      28|       5.132|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 104   |     110|      52.471|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  79   |      93|       5.857|   1.004/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  91   |    2479|      42.184|   1.044/ 16|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|       1.044|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 115   |   27755|     589.278|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  90   |      11|       0.520|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 105   |     683|      16.095|   1.022/ 32|   1.016/ 44|   1.014/ 50|   1.012/ 56 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 107   |    5351|     517.543|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 113   |    1964|     228.312|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  89   |       8|       0.432|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  87   |      21|       0.376|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 117   |      59|       0.880|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  91   |      13|       1.768|   1.003/ **|   1.003/ **|   1.004/ **|   1.004/ ** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  93   |       8|       5.865|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  99   |      50|       4.290|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 101   |    5064|      60.893|   1.004/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 118   |  126413|     383.600|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 105   |    1099|      26.247|   1.015/ 45|   1.014/ 48|   1.014/ 49|   1.014/ 50 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  98   |     313|      31.636|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 107   |   44129|     664.244|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  89   |      25|       7.163|   1.007/ 95|   1.008/ 84|   1.009/ 81|   1.009/ 79 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  91   |      21|       0.607|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  91   |      38|       1.177|   1.037/ 19|   1.040/ 17|   1.040/ 17|   1.041/ 17 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  85   |      14|       0.806|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  95   |       4|       0.264|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |

