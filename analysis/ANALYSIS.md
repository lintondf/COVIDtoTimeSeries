# State and Country COVID-19 Analysis #
## Updated: 2020-06-22 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 100   |   31426|    1615.456|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 104   |   13262|    1493.065|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  94   |    8082|    1163.014|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  97   |    6912|     545.478|   1.008/ 82|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  95   |    6650|     519.481|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  95   |    6269|     627.742|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 110   |    5710|     144.511|   1.012/ 56|   1.011/ 63|   1.011/ 65|   1.010/ 67 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  95   |    4365|    1224.249|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 106   |    3233|     150.533|   1.011/ 62|   1.010/ 68|   1.010/ 69|   1.010/ 71 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 100   |    3154|     678.486|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 114   |  124171|     376.796|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  97   |   54380|     257.225|   1.024/ 29|   1.020/ 35|   1.019/ 36|   1.018/ 38 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 103   |   43671|     657.347|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 122   |   35175|     583.921|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 128   |   30202|     450.263|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 111   |   27415|     582.062|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  95   |   22950|     181.314|   1.034/ 20|   1.031/ 22|   1.030/ 23|   1.029/ 23 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 103   |   13409|       9.850|   1.036/ 19|   1.034/ 20|   1.034/ 20|   1.033/ 21 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 103   |    9810|     851.246|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 123   |    9417|     112.948|   1.010/ 69|   1.010/ 66|   1.011/ 66|   1.011/ 65 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  89   |     857|     174.834|   1.013/ 51|   1.012/ 55|   1.012/ 56|   1.012/ 58 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  89   |      12|      16.559|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  93   |    1366|     187.711|   1.019/ 37|   1.018/ 38|   1.018/ 38|   1.018/ 38 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  90   |     216|      71.646|   1.028/ 25|   1.030/ 23|   1.031/ 23|   1.031/ 22 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 110   |    5710|     144.511|   1.012/ 56|   1.011/ 63|   1.011/ 65|   1.010/ 67 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 100   |    1713|     297.540|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  95   |    4365|    1224.249|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  88   |     452|     464.282|   1.007/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 106   |    3233|     150.533|   1.011/ 62|   1.010/ 68|   1.010/ 69|   1.010/ 71 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 102   |    2714|     255.662|   1.012/ 56|   1.012/ 59|   1.012/ 60|   1.011/ 61 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  83   |      17|      12.007|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  88   |      90|      50.225|   1.004/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  97   |    6912|     545.478|   1.008/ 82|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  98   |    2609|     387.590|   1.007/ 97|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  89   |     733|     232.411|   1.008/ 82|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 101   |     259|      88.951|   1.007/ 98|   1.007/ **|   1.007/ **|   1.006/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  98   |     546|     122.150|   1.008/ 82|   1.007/ 98|   1.007/ **|   1.006/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 100   |    3154|     678.486|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  87   |     108|      80.350|   1.004/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  95   |    3186|     527.022|   1.008/ 91|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  94   |    8082|    1163.014|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  95   |    6269|     627.742|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  93   |    1498|     265.662|   1.013/ 55|   1.010/ 71|   1.009/ 77|   1.008/ 83 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  95   |    1006|     337.950|   1.010/ 70|   1.007/ 99|   1.006/ **|   1.006/ ** |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  95   |     977|     159.124|   1.012/ 60|   1.011/ 64|   1.011/ 65|   1.011/ 65 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  87   |      20|      18.593|   1.009/ 75|   1.010/ 67|   1.011/ 65|   1.011/ 64 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  86   |     249|     128.884|   1.019/ 37|   1.018/ 37|   1.018/ 38|   1.018/ 38 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  98   |     494|     160.392|   1.007/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  91   |     361|     265.604|   1.013/ 52|   1.010/ 67|   1.010/ 72|   1.009/ 78 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 104   |   13262|    1493.065|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  89   |     483|     230.365|   1.012/ 57|   1.011/ 66|   1.010/ 68|   1.010/ 71 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 100   |   31426|    1615.456|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  89   |    1271|     121.204|   1.012/ 59|   1.010/ 72|   1.009/ 76|   1.009/ 81 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  87   |      82|     106.979|   1.007/ 95|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  94   |    2806|     240.084|   1.009/ 80|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  95   |     377|      95.365|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  99   |     188|      44.561|   1.010/ 69|   1.010/ 66|   1.011/ 65|   1.011/ 65 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  95   |    6650|     519.481|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  93   |     152|      47.462|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  86   |     936|     883.870|   1.010/ 71|   1.007/ 97|   1.006/ **|   1.006/ ** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  98   |     665|     129.221|   1.013/ 53|   1.012/ 56|   1.012/ 57|   1.012/ 58 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 103   |      85|      95.860|   1.014/ 49|   1.013/ 55|   1.012/ 56|   1.012/ 58 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  93   |     533|      77.933|   1.017/ 41|   1.017/ 41|   1.017/ 41|   1.017/ 41 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  97   |    2215|      76.400|   1.013/ 55|   1.012/ 58|   1.012/ 59|   1.012/ 60 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  92   |     159|      49.642|   1.017/ 41|   1.016/ 42|   1.016/ 42|   1.016/ 43 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  94   |      56|      89.319|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 100   |    1710|     200.351|   1.006/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 114   |    1279|     167.896|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  84   |      92|      51.288|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  94   |     767|     131.808|   1.011/ 64|   1.010/ 73|   1.009/ 75|   1.009/ 78 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  70   |      20|      34.066|   1.012/ 60|   1.011/ 64|   1.011/ 64|   1.011/ 64 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  92   |     595|      18.467|   1.038/ 18|   1.038/ 18|   1.038/ 18|   1.038/ 18 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 103   |      38|      13.292|   1.016/ 42|   1.020/ 35|   1.020/ 34|   1.021/ 33 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 102   |     840|      19.530|   1.013/ 54|   1.013/ 54|   1.013/ 53|   1.013/ 53 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  85   |       7|       0.217|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 106   |    1014|      22.563|   1.030/ 23|   1.031/ 22|   1.031/ 22|   1.031/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  88   |     386|     130.490|   1.041/ 17|   1.037/ 19|   1.036/ 19|   1.035/ 20 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 113   |     103|       4.007|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 102   |     694|      77.899|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 101   |     156|      15.523|   1.042/ 16|   1.042/ 16|   1.042/ 16|   1.042/ 16 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  98   |      58|      37.472|   1.068/ 10|   1.073/  9|   1.075/  9|   1.076/  9 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  96   |    1572|       9.332|   1.037/ 18|   1.035/ 20|   1.034/ 20|   1.033/ 21 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  83   |     353|      37.565|   1.018/ 38|   1.017/ 41|   1.017/ 41|   1.016/ 42 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 103   |    9810|     851.246|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  77   |      10|       0.887|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  85   |     804|      70.093|   1.038/ 18|   1.035/ 19|   1.035/ 20|   1.034/ 20 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  93   |     172|      52.148|   1.004/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  83   |       1|       0.428|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  97   |   54380|     257.225|   1.024/ 29|   1.020/ 35|   1.019/ 36|   1.018/ 38 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 103   |     200|      28.814|   1.016/ 43|   1.016/ 44|   1.015/ 45|   1.015/ 45 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  96   |      53|       2.557|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  70   |       1|       0.091|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  89   |     285|      10.740|   1.011/ 63|   1.010/ 72|   1.009/ 75|   1.009/ 77 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 105   |    8913|     234.550|   1.006/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  30   |      25|       4.581|   1.087/  8|   1.067/ 10|   1.062/ 11|   1.058/ 12 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  55   |      75|       4.644|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  92   |    4853|     254.004|   1.058/ 12|   1.056/ 12|   1.056/ 12|   1.056/ 12 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 103   |    4638|       3.308|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  92   |    2233|      45.215|   1.044/ 16|   1.045/ 15|   1.045/ 15|   1.045/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  95   |      12|       2.435|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  95   |     109|      26.698|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  96   |      85|       7.599|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 100   |     608|     104.444|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  97   |     648|      62.573|   1.015/ 47|   1.016/ 44|   1.016/ 43|   1.016/ 43 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 100   |    4268|     244.351|   1.010/ 72|   1.009/ 81|   1.008/ 83|   1.008/ 86 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 106   |    2052|      20.463|   1.043/ 16|   1.045/ 15|   1.046/ 15|   1.046/ 15 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  83   |      93|      14.362|   1.039/ 18|   1.040/ 17|   1.040/ 17|   1.041/ 17 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  61   |      30|      21.843|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  78   |      98|       0.990|   1.077/  9|   1.069/ 10|   1.067/ 10|   1.064/ 11 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  93   |     331|      59.867|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 128   |   30202|     450.263|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  94   |      33|      15.385|   1.033/ 21|   1.033/ 21|   1.033/ 21|   1.033/ 21 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  91   |       1|       0.426|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  79   |      14|       3.827|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 105   |    9018|     108.461|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  93   |      67|       2.228|   1.049/ 14|   1.056/ 12|   1.058/ 12|   1.060/ 11 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 103   |     191|      17.813|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  98   |     656|      39.485|   1.060/ 11|   1.057/ 12|   1.056/ 12|   1.055/ 12 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  68   |      27|       2.198|   1.011/ 62|   1.012/ 55|   1.013/ 54|   1.013/ 52 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  57   |      18|      11.184|   1.027/ 26|   1.031/ 22|   1.032/ 21|   1.033/ 21 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  78   |      95|       8.165|   1.037/ 18|   1.034/ 20|   1.033/ 21|   1.032/ 21 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  88   |     377|      41.156|   1.024/ 28|   1.023/ 30|   1.023/ 31|   1.022/ 31 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|       0.267|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  99   |     587|      60.109|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 103   |   13409|       9.850|   1.036/ 19|   1.034/ 20|   1.034/ 20|   1.033/ 21 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 103   |    2493|       9.342|   1.021/ 33|   1.020/ 34|   1.020/ 34|   1.020/ 34 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 123   |    9417|     112.948|   1.010/ 69|   1.010/ 66|   1.011/ 66|   1.011/ 65 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 110   |     853|      21.799|   1.087/  8|   1.096/  7|   1.098/  7|   1.100/  7 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 103   |    1744|     354.309|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  93   |     308|      33.525|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 122   |   35175|     583.921|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  95   |      10|       3.766|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 130   |    1040|       8.257|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  87   |       9|       0.844|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  89   |     106|       5.700|   1.060/ 11|   1.069/ 10|   1.071/ 10|   1.073/  9 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  88   |     126|       2.646|   1.031/ 22|   1.031/ 22|   1.031/ 22|   1.031/ 22 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  88   |      33|      18.371|   1.005/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  79   |     347|      78.417|   1.016/ 42|   1.010/ 67|   1.009/ 79|   1.007/ 95 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  80   |      35|       5.385|   1.039/ 18|   1.042/ 16|   1.043/ 16|   1.043/ 16 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  80   |      30|      15.840|   1.012/ 57|   1.013/ 55|   1.013/ 54|   1.013/ 53 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 104   |      33|       4.772|   1.008/ 91|   1.008/ 86|   1.008/ 85|   1.008/ 84 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  79   |      34|       7.696|   1.008/ 86|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  81   |      11|       1.530|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  93   |      79|      28.227|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  36   |      14|       0.525|   1.035/ 20|   1.038/ 18|   1.040/ 17|   1.041/ 17 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  97   |     121|       3.705|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  85   |     117|       5.762|   1.014/ 49|   1.011/ 65|   1.010/ 71|   1.009/ 78 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  84   |     165|      40.494|   1.047/ 15|   1.042/ 16|   1.041/ 17|   1.039/ 17 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  95   |   22950|     181.314|   1.034/ 20|   1.031/ 22|   1.030/ 23|   1.029/ 23 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  96   |     474|     176.738|   1.022/ 31|   1.022/ 31|   1.022/ 31|   1.022/ 32 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 104   |     217|       6.037|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  28   |       5|       0.162|   1.076/  9|   1.061/ 11|   1.052/ 13|   1.042/ 17 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  37   |      24|       0.786|   1.043/ 16|   1.034/ 20|   1.032/ 22|   1.029/ 24 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 108   |    6188|     354.460|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  85   |      22|       4.453|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  87   |      77|      11.939|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  89   |      68|       3.044|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  91   |     521|       2.527|   1.028/ 24|   1.028/ 25|   1.028/ 25|   1.027/ 25 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  92   |     224|     107.996|   1.031/ 22|   1.034/ 20|   1.035/ 20|   1.035/ 19 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 100   |     244|      45.521|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  83   |     143|      30.731|   1.043/ 16|   1.039/ 18|   1.038/ 18|   1.037/ 19 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  95   |    3631|      16.555|   1.044/ 16|   1.044/ 15|   1.045/ 15|   1.045/ 15 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 103   |     498|     117.947|   1.019/ 37|   1.019/ 36|   1.019/ 36|   1.019/ 36 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  93   |      12|       1.720|   1.003/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  94   |    8202|     255.249|   1.026/ 26|   1.024/ 29|   1.024/ 29|   1.023/ 30 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 141   |    1196|      11.025|   1.008/ 89|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 102   |    1354|      35.285|   1.011/ 63|   1.011/ 63|   1.011/ 63|   1.011/ 63 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  97   |    1583|     154.063|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  86   |     104|      38.016|   1.044/ 16|   1.039/ 18|   1.038/ 18|   1.037/ 19 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  92   |    1503|      77.456|   1.009/ 80|   1.009/ 80|   1.009/ 80|   1.009/ 80 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  95   |    8703|      59.309|   1.025/ 28|   1.021/ 32|   1.020/ 34|   1.020/ 35 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  23   |       2|       0.162|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  90   |    1292|      37.755|   1.045/ 15|   1.045/ 15|   1.045/ 15|   1.045/ 15 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  82   |      79|       4.881|   1.039/ 18|   1.043/ 16|   1.044/ 16|   1.045/ 15 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  94   |     261|      37.425|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  60   |      54|       6.780|   1.008/ 85|   1.009/ 79|   1.009/ 78|   1.009/ 77 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  93   |      27|       4.652|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  86   |      28|       5.133|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 100   |     110|      52.592|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  75   |      93|       5.832|   1.005/ **|   1.002/ **|   1.001/ **|   1.000/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  87   |    2130|      36.247|   1.048/ 14|   1.044/ 16|   1.043/ 16|   1.042/ 16 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|       1.044|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 111   |   27415|     582.062|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  86   |      11|       0.524|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 101   |     642|      15.117|   1.028/ 25|   1.021/ 32|   1.020/ 35|   1.018/ 38 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 103   |    5248|     507.667|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 109   |    1960|     227.810|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  85   |       7|       0.422|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  83   |      21|       0.376|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 113   |      59|       0.880|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  87   |      13|       1.747|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  89   |       8|       5.865|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  95   |      50|       4.274|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  97   |    4990|      60.014|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 114   |  124171|     376.796|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 101   |    1037|      24.770|   1.016/ 43|   1.015/ 47|   1.014/ 48|   1.014/ 49 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  94   |     308|      31.101|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 103   |   43671|     657.347|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  85   |      24|       6.938|   1.005/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  87   |      21|       0.602|   1.009/ 81|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  87   |      33|       1.023|   1.035/ 20|   1.038/ 18|   1.039/ 18|   1.039/ 17 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  81   |      12|       0.655|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  91   |       4|       0.264|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |

