# State and Country COVID-19 Analysis #
## Updated: 2020-06-18 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  96   |   31281|    1607.958|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 100   |   13090|    1473.735|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  90   |    7962|    1145.639|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  93   |    6725|     530.671|   1.009/ 73|   1.007/ 96|   1.007/ **|   1.006/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  91   |    6542|     511.001|   1.007/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  91   |    6207|     621.538|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 106   |    5457|     138.111|   1.013/ 55|   1.011/ 63|   1.011/ 66|   1.010/ 68 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  91   |    4338|    1216.687|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  96   |    3111|     669.120|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 102   |    3102|     144.451|   1.011/ 62|   1.010/ 71|   1.009/ 73|   1.009/ 76 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 110   |  121898|     369.899|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  93   |   50159|     237.256|   1.025/ 27|   1.021/ 33|   1.020/ 35|   1.019/ 37 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  99   |   43148|     649.470|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 118   |   35063|     582.064|   1.001/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 124   |   30178|     449.908|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 107   |   27161|     576.658|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  91   |   20302|     160.393|   1.035/ 20|   1.032/ 22|   1.031/ 22|   1.030/ 23 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  99   |   10927|       8.028|   1.039/ 18|   1.038/ 18|   1.038/ 18|   1.038/ 18 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  99   |    9800|     850.355|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 119   |    9033|     108.336|   1.009/ 76|   1.009/ 74|   1.009/ 74|   1.009/ 73 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  85   |     817|     166.557|   1.013/ 53|   1.011/ 60|   1.011/ 62|   1.011/ 65 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  85   |      12|      15.852|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  89   |    1270|     174.533|   1.017/ 40|   1.016/ 43|   1.016/ 44|   1.016/ 45 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  86   |     192|      63.707|   1.022/ 31|   1.023/ 30|   1.023/ 30|   1.023/ 30 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 106   |    5457|     138.111|   1.013/ 55|   1.011/ 63|   1.011/ 66|   1.010/ 68 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  96   |    1692|     293.871|   1.006/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  91   |    4338|    1216.687|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  84   |     443|     455.283|   1.008/ 83|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 102   |    3102|     144.451|   1.011/ 62|   1.010/ 71|   1.009/ 73|   1.009/ 76 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  98   |    2586|     243.577|   1.014/ 51|   1.013/ 53|   1.013/ 54|   1.013/ 54 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  79   |      17|      12.007|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  84   |      88|      49.467|   1.004/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  93   |    6725|     530.671|   1.009/ 73|   1.007/ 96|   1.007/ **|   1.006/ ** |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  94   |    2547|     378.392|   1.007/ 92|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  85   |     719|     227.732|   1.012/ 59|   1.007/ 99|   1.006/ **|   1.005/ ** |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  97   |     252|      86.626|   1.006/ **|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  94   |     530|     118.642|   1.010/ 70|   1.008/ 82|   1.008/ 86|   1.008/ 90 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  96   |    3111|     669.120|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  83   |     108|      79.992|   1.007/ 95|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  91   |    3112|     514.760|   1.009/ 76|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  90   |    7962|    1145.639|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  91   |    6207|     621.538|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  89   |    1440|     255.350|   1.015/ 46|   1.012/ 58|   1.011/ 62|   1.010/ 66 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  91   |     974|     327.418|   1.013/ 52|   1.011/ 66|   1.010/ 70|   1.009/ 75 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  91   |     933|     151.987|   1.009/ 74|   1.008/ 92|   1.007/ 98|   1.007/ ** |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  83   |      19|      17.789|   1.009/ 77|   1.010/ 67|   1.011/ 64|   1.011/ 62 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  82   |     231|     119.580|   1.020/ 35|   1.019/ 36|   1.019/ 36|   1.019/ 36 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  94   |     482|     156.611|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  87   |     346|     254.647|   1.016/ 43|   1.013/ 52|   1.013/ 55|   1.012/ 59 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 100   |   13090|    1473.735|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  85   |     463|     220.676|   1.013/ 52|   1.011/ 61|   1.011/ 64|   1.010/ 67 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  96   |   31281|    1607.958|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  85   |    1222|     116.550|   1.014/ 51|   1.011/ 60|   1.011/ 63|   1.010/ 67 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  83   |      81|     105.775|   1.009/ 75|   1.005/ **|   1.004/ **|   1.002/ ** |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  90   |    2732|     233.764|   1.010/ 71|   1.007/ 98|   1.006/ **|   1.006/ ** |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  91   |     373|      94.152|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  95   |     180|      42.641|   1.010/ 68|   1.011/ 65|   1.011/ 64|   1.011/ 63 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  91   |    6542|     511.001|   1.007/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  89   |     150|      47.022|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  82   |     908|     857.165|   1.012/ 59|   1.009/ 79|   1.008/ 86|   1.007/ 95 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  94   |     635|     123.267|   1.013/ 53|   1.012/ 59|   1.011/ 60|   1.011/ 62 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  99   |      81|      91.175|   1.015/ 47|   1.013/ 53|   1.013/ 55|   1.012/ 57 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  89   |     498|      72.856|   1.017/ 39|   1.018/ 39|   1.018/ 39|   1.018/ 39 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  93   |    2109|      72.748|   1.012/ 60|   1.010/ 68|   1.010/ 70|   1.010/ 72 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  88   |     149|      46.413|   1.017/ 41|   1.016/ 43|   1.016/ 43|   1.016/ 44 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  90   |      55|      88.711|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  96   |    1684|     197.283|   1.008/ 88|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 110   |    1251|     164.264|   1.005/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  80   |      91|      50.639|   1.008/ 92|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  90   |     740|     127.105|   1.011/ 62|   1.009/ 74|   1.009/ 78|   1.008/ 82 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  66   |      19|      32.889|   1.006/ **|   1.000/ --|   1.000/ --|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  88   |     511|      15.870|   1.038/ 18|   1.039/ 18|   1.039/ 18|   1.039/ 18 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  99   |      36|      12.709|   1.008/ 84|   1.009/ 74|   1.010/ 71|   1.010/ 69 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  98   |     798|      18.555|   1.012/ 58|   1.012/ 58|   1.012/ 59|   1.012/ 59 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  81   |       6|       0.196|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 102   |     897|      19.960|   1.030/ 23|   1.031/ 23|   1.031/ 22|   1.031/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  84   |     334|     113.068|   1.047/ 14|   1.044/ 15|   1.044/ 16|   1.043/ 16 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 109   |     103|       4.019|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  98   |     689|      77.342|   1.002/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  97   |     133|      13.173|   1.043/ 16|   1.044/ 16|   1.044/ 16|   1.044/ 16 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  94   |      43|      28.178|   1.067/ 10|   1.074/  9|   1.076/  9|   1.078/  9 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  92   |    1368|       8.120|   1.041/ 17|   1.039/ 18|   1.038/ 18|   1.038/ 18 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  79   |     330|      35.090|   1.019/ 37|   1.017/ 40|   1.017/ 41|   1.016/ 42 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  99   |    9800|     850.355|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  73   |       5|       0.427|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  81   |     699|      60.917|   1.041/ 17|   1.040/ 17|   1.039/ 18|   1.039/ 18 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  89   |     170|      51.582|   1.004/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  79   |       1|       0.428|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  93   |   50159|     237.256|   1.025/ 27|   1.021/ 33|   1.020/ 35|   1.019/ 37 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  99   |     188|      27.036|   1.014/ 49|   1.013/ 55|   1.012/ 56|   1.012/ 58 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  92   |      53|       2.562|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  66   |       1|       0.091|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  85   |     253|       9.544|   1.007/ 95|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 101   |    8778|     231.012|   1.007/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  26   |      14|       2.524|   1.061/ 11|   1.233/  3|   1.277/  2|   1.319/  2 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  51   |      75|       4.597|   1.007/ 94|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  88   |    3758|     196.697|   1.060/ 11|   1.059/ 12|   1.058/ 12|   1.058/ 12 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  99   |    4638|       3.308|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  88   |    1882|      38.105|   1.043/ 16|   1.044/ 16|   1.044/ 15|   1.045/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  91   |      12|       2.373|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  91   |     108|      26.615|   1.002/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  92   |      85|       7.558|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  96   |     605|     103.954|   1.002/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  93   |     608|      58.741|   1.014/ 49|   1.015/ 46|   1.015/ 45|   1.015/ 45 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  96   |    4131|     236.462|   1.009/ 79|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 102   |    1721|      17.162|   1.040/ 17|   1.042/ 16|   1.043/ 16|   1.043/ 16 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  79   |      80|      12.352|   1.033/ 21|   1.032/ 21|   1.032/ 21|   1.032/ 22 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  57   |      12|       8.842|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  74   |      72|       0.733|   1.144/  5|   1.163/  4|   1.167/  4|   1.171/  4 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  89   |     331|      59.919|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 124   |   30178|     449.908|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  90   |      28|      13.063|   1.014/ 51|   1.010/ 66|   1.010/ 72|   1.009/ 78 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  87   |       1|       0.426|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  75   |      14|       3.742|   1.007/ 99|   1.008/ 84|   1.009/ 81|   1.009/ 78 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 101   |    8979|     107.988|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  89   |      57|       1.866|   1.032/ 22|   1.035/ 20|   1.036/ 19|   1.037/ 19 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  99   |     189|      17.601|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  94   |     510|      30.696|   1.068/ 10|   1.065/ 10|   1.065/ 11|   1.064/ 11 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  64   |      26|       2.096|   1.011/ 62|   1.012/ 58|   1.012/ 56|   1.013/ 54 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  53   |      16|      10.245|   1.027/ 25|   1.027/ 26|   1.027/ 26|   1.027/ 26 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  74   |      82|       7.108|   1.044/ 15|   1.043/ 16|   1.043/ 16|   1.042/ 16 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  84   |     344|      37.555|   1.027/ 25|   1.026/ 26|   1.026/ 27|   1.026/ 27 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|       0.267|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  95   |     583|      59.620|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  99   |   10927|       8.028|   1.039/ 18|   1.038/ 18|   1.038/ 18|   1.038/ 18 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  99   |    2298|       8.610|   1.021/ 32|   1.021/ 33|   1.021/ 33|   1.021/ 33 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 119   |    9033|     108.336|   1.009/ 76|   1.009/ 74|   1.009/ 74|   1.009/ 73 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 106   |     586|      14.988|   1.080/  8|   1.089/  8|   1.091/  7|   1.094/  7 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  99   |    1739|     353.322|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  89   |     305|      33.241|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 118   |   35063|     582.064|   1.001/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  91   |      10|       3.740|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 126   |    1045|       8.296|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  83   |       9|       0.844|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  85   |      82|       4.388|   1.051/ 14|   1.059/ 12|   1.061/ 11|   1.063/ 11 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  84   |     111|       2.338|   1.029/ 23|   1.029/ 24|   1.029/ 24|   1.029/ 24 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  84   |      32|      17.921|   1.007/ 98|   1.009/ 81|   1.009/ 77|   1.009/ 74 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  75   |     333|      75.263|   1.021/ 33|   1.014/ 50|   1.012/ 58|   1.010/ 68 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  76   |      30|       4.639|   1.034/ 20|   1.037/ 19|   1.037/ 18|   1.038/ 18 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  76   |      29|      15.019|   1.012/ 57|   1.013/ 55|   1.013/ 54|   1.013/ 53 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 100   |      32|       4.618|   1.011/ 65|   1.012/ 57|   1.012/ 55|   1.013/ 54 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  75   |      34|       7.504|   1.011/ 64|   1.010/ 70|   1.010/ 72|   1.009/ 74 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  77   |       9|       1.259|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  89   |      78|      27.999|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  32   |      12|       0.443|   1.039/ 18|   1.030/ 23|   1.029/ 23|   1.029/ 24 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  93   |     120|       3.669|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  81   |     112|       5.518|   1.018/ 39|   1.015/ 47|   1.014/ 49|   1.013/ 52 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  80   |     155|      37.906|   1.057/ 12|   1.054/ 13|   1.053/ 13|   1.052/ 13 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  91   |   20302|     160.393|   1.035/ 20|   1.032/ 22|   1.031/ 22|   1.030/ 23 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  92   |     434|     161.853|   1.022/ 31|   1.021/ 32|   1.021/ 32|   1.021/ 33 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 100   |     215|       6.006|   1.002/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  24   |       4|       0.133|   1.024/ 29|   1.175/  4|   1.217/  3|   1.258/  3 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  33   |      21|       0.684|   1.058/ 12|   1.037/ 19|   1.033/ 21|   1.028/ 24 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 104   |    6183|     354.171|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  81   |      22|       4.464|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  83   |      74|      11.531|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  85   |      68|       3.042|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  87   |     467|       2.264|   1.028/ 24|   1.027/ 25|   1.027/ 25|   1.027/ 26 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  88   |     196|      94.474|   1.028/ 24|   1.031/ 22|   1.031/ 22|   1.032/ 22 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  96   |     243|      45.263|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  79   |     123|      26.394|   1.049/ 14|   1.046/ 15|   1.046/ 15|   1.045/ 15 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  91   |    3052|      13.915|   1.044/ 15|   1.046/ 15|   1.046/ 15|   1.046/ 15 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  99   |     461|     109.287|   1.018/ 37|   1.019/ 37|   1.019/ 36|   1.019/ 36 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  89   |      11|       1.575|   1.001/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  90   |    7426|     231.104|   1.028/ 24|   1.026/ 26|   1.026/ 27|   1.025/ 27 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 137   |    1161|      10.701|   1.008/ 92|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  98   |    1295|      33.748|   1.010/ 71|   1.009/ 75|   1.009/ 77|   1.009/ 78 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  93   |    1573|     153.101|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  82   |      90|      32.873|   1.047/ 15|   1.041/ 17|   1.040/ 17|   1.038/ 18 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  88   |    1451|      74.795|   1.008/ 90|   1.007/ 96|   1.007/ 98|   1.007/ 99 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  91   |    7991|      54.453|   1.027/ 25|   1.024/ 29|   1.023/ 30|   1.022/ 32 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  19   |       2|       0.162|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  86   |    1085|      31.701|   1.046/ 15|   1.048/ 14|   1.049/ 14|   1.049/ 14 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  78   |      67|       4.112|   1.034/ 20|   1.037/ 18|   1.038/ 18|   1.039/ 18 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  90   |     257|      36.960|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  56   |      52|       6.586|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  89   |      26|       4.587|   1.006/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  82   |      28|       5.137|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  96   |     110|      52.710|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  71   |      92|       5.794|   1.009/ 77|   1.005/ **|   1.004/ **|   1.003/ ** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  83   |    1788|      30.427|   1.055/ 13|   1.052/ 13|   1.051/ 13|   1.051/ 13 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|       1.044|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 107   |   27161|     576.658|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  82   |      11|       0.527|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  97   |     586|      13.812|   1.034/ 20|   1.028/ 24|   1.027/ 26|   1.025/ 27 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  99   |    5146|     497.777|   1.007/ 99|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 105   |    1954|     227.096|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  81   |       7|       0.400|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  79   |      21|       0.376|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 109   |      59|       0.880|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  83   |      13|       1.760|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  85   |       8|       5.865|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  91   |      50|       4.246|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  93   |    4928|      59.267|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 110   |  121898|     369.899|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  97   |     975|      23.278|   1.016/ 45|   1.013/ 52|   1.013/ 54|   1.012/ 57 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  90   |     302|      30.510|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  99   |   43148|     649.470|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  81   |      24|       6.789|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  83   |      20|       0.589|   1.014/ 51|   1.012/ 57|   1.012/ 59|   1.011/ 61 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  83   |      29|       0.897|   1.029/ 24|   1.032/ 21|   1.033/ 21|   1.033/ 21 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  77   |      11|       0.603|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  87   |       4|       0.264|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |

