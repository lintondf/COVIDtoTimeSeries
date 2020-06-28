# State and Country COVID-19 Analysis #
## Updated: 2020-06-28 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 106   |   31636|    1626.222|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 110   |   13962|    1571.866|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 100   |    8225|    1183.608|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 103   |    7136|     563.109|   1.007/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 101   |    6777|     529.381|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 101   |    6316|     632.389|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 116   |    6081|     153.891|   1.011/ 61|   1.010/ 67|   1.010/ 68|   1.010/ 70 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 101   |    4397|    1233.238|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 112   |    3439|     160.136|   1.011/ 62|   1.010/ 66|   1.010/ 67|   1.010/ 68 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 106   |    3223|     693.246|   1.004/ **|   1.004/ **|   1.003/ **|   1.003/ ** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 120   |  127759|     387.683|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 103   |   60579|     286.544|   1.020/ 34|   1.017/ 40|   1.017/ 41|   1.016/ 43 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 109   |   44360|     667.721|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 128   |   35271|     585.529|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 134   |   30233|     450.722|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 117   |   27908|     592.519|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 101   |   27629|     218.274|   1.033/ 21|   1.031/ 22|   1.030/ 23|   1.030/ 23 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 109   |   17060|      12.533|   1.031/ 22|   1.029/ 24|   1.028/ 24|   1.028/ 25 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 129   |   10096|     121.091|   1.011/ 61|   1.012/ 58|   1.012/ 57|   1.012/ 57 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 109   |    9820|     852.075|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  95   |     924|     188.542|   1.014/ 51|   1.013/ 53|   1.013/ 54|   1.013/ 54 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  95   |      13|      17.628|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  99   |    1537|     211.226|   1.021/ 33|   1.021/ 32|   1.022/ 32|   1.022/ 32 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  96   |     254|      84.133|   1.025/ 27|   1.026/ 27|   1.026/ 26|   1.026/ 26 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 116   |    6081|     153.891|   1.011/ 61|   1.010/ 67|   1.010/ 68|   1.010/ 70 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 106   |    1735|     301.283|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 101   |    4397|    1233.238|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  94   |     496|     508.933|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 112   |    3439|     160.136|   1.011/ 62|   1.010/ 66|   1.010/ 67|   1.010/ 68 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 108   |    2871|     270.419|   1.010/ 68|   1.009/ 75|   1.009/ 77|   1.009/ 79 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  89   |      17|      12.007|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  94   |      91|      51.020|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 103   |    7136|     563.109|   1.007/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 104   |    2686|     399.040|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  95   |     744|     235.740|   1.005/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 107   |     269|      92.345|   1.007/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 104   |     567|     126.947|   1.008/ 88|   1.007/ **|   1.007/ **|   1.006/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 106   |    3223|     693.246|   1.004/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  93   |     108|      80.084|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 101   |    3272|     541.130|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 100   |    8225|    1183.608|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 101   |    6316|     632.389|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  99   |    1554|     275.530|   1.008/ 87|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 101   |    1063|     357.282|   1.010/ 66|   1.009/ 79|   1.008/ 83|   1.008/ 87 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 101   |    1028|     167.577|   1.009/ 78|   1.008/ 87|   1.008/ 90|   1.007/ 93 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  93   |      21|      20.055|   1.012/ 59|   1.013/ 53|   1.013/ 52|   1.014/ 50 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  92   |     274|     141.802|   1.016/ 42|   1.016/ 44|   1.015/ 45|   1.015/ 46 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 104   |     509|     165.289|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  97   |     380|     279.347|   1.012/ 59|   1.009/ 73|   1.009/ 77|   1.008/ 82 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 110   |   13962|    1571.866|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  95   |     508|     242.307|   1.010/ 71|   1.008/ 85|   1.008/ 90|   1.007/ 94 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 106   |   31636|    1626.222|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  95   |    1375|     131.131|   1.013/ 52|   1.012/ 56|   1.012/ 57|   1.012/ 58 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  93   |      82|     108.124|   1.004/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 100   |    2900|     248.074|   1.007/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 101   |     384|      97.063|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 105   |     200|      47.520|   1.011/ 64|   1.011/ 62|   1.011/ 61|   1.011/ 61 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 101   |    6777|     529.381|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  99   |     154|      48.112|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  92   |     966|     911.677|   1.007/ 99|   1.005/ **|   1.004/ **|   1.004/ ** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 104   |     716|     139.105|   1.013/ 53|   1.012/ 56|   1.012/ 57|   1.012/ 57 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 109   |      91|     103.149|   1.014/ 48|   1.014/ 51|   1.013/ 51|   1.013/ 52 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  99   |     586|      85.820|   1.017/ 41|   1.017/ 41|   1.017/ 41|   1.017/ 41 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 103   |    2381|      82.119|   1.013/ 54|   1.013/ 55|   1.013/ 55|   1.013/ 55 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  98   |     173|      53.902|   1.014/ 50|   1.013/ 54|   1.013/ 55|   1.012/ 56 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 100   |      56|      89.875|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 106   |    1758|     205.923|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 120   |    1321|     173.447|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  90   |      94|      52.651|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 100   |     801|     137.616|   1.008/ 82|   1.007/ 99|   1.007/ **|   1.006/ ** |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  76   |      21|      35.429|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  98   |     730|      22.642|   1.036/ 19|   1.035/ 20|   1.035/ 20|   1.035/ 20 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 109   |      45|      15.795|   1.025/ 28|   1.029/ 24|   1.030/ 23|   1.031/ 22 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 108   |     901|      20.952|   1.012/ 60|   1.011/ 61|   1.011/ 61|   1.011/ 61 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  91   |      11|       0.339|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 112   |    1212|      26.970|   1.030/ 23|   1.030/ 23|   1.031/ 23|   1.031/ 23 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  94   |     466|     157.410|   1.036/ 19|   1.032/ 21|   1.031/ 22|   1.031/ 23 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 119   |     103|       4.023|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 108   |     701|      78.724|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 107   |     198|      19.665|   1.040/ 17|   1.040/ 17|   1.040/ 17|   1.040/ 17 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 104   |      81|      52.701|   1.056/ 12|   1.057/ 12|   1.057/ 12|   1.057/ 12 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 102   |    1869|      11.093|   1.031/ 22|   1.027/ 25|   1.027/ 26|   1.026/ 27 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  89   |     387|      41.110|   1.016/ 43|   1.015/ 47|   1.014/ 48|   1.014/ 49 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 109   |    9820|     852.075|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  83   |      16|       1.384|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  91   |     998|      86.976|   1.038/ 18|   1.036/ 19|   1.036/ 19|   1.036/ 19 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  99   |     177|      53.552|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  89   |       1|       0.428|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 103   |   60579|     286.544|   1.020/ 34|   1.017/ 40|   1.017/ 41|   1.016/ 43 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 109   |     220|      31.651|   1.015/ 46|   1.014/ 48|   1.014/ 48|   1.014/ 49 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 102   |      53|       2.550|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  76   |       1|       0.091|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  95   |     327|      12.318|   1.010/ 68|   1.009/ 76|   1.009/ 78|   1.009/ 80 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 111   |    9029|     237.622|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  36   |      50|       9.182|   1.106/  6|   1.099/  7|   1.096/  7|   1.093/  7 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  61   |      75|       4.626|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  98   |    6388|     334.340|   1.044/ 16|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 109   |    4639|       3.308|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  98   |    2895|      58.610|   1.043/ 16|   1.044/ 16|   1.044/ 16|   1.044/ 16 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 101   |      13|       2.524|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 101   |     109|      26.695|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 102   |      86|       7.642|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 106   |     611|     104.993|   1.001/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 103   |     710|      68.564|   1.015/ 47|   1.015/ 45|   1.016/ 44|   1.016/ 44 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 106   |    4481|     256.535|   1.009/ 76|   1.008/ 82|   1.008/ 84|   1.008/ 85 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 112   |    2653|      26.458|   1.041/ 17|   1.043/ 16|   1.043/ 16|   1.043/ 16 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  89   |     127|      19.644|   1.051/ 13|   1.056/ 12|   1.057/ 12|   1.058/ 12 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  67   |      39|      28.807|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  84   |     122|       1.232|   1.052/ 13|   1.035/ 19|   1.031/ 22|   1.027/ 26 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  99   |     331|      59.845|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 134   |   30233|     450.722|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 100   |      42|      19.334|   1.031/ 22|   1.031/ 22|   1.031/ 22|   1.031/ 22 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  97   |       1|       0.426|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  85   |      14|       3.871|   1.001/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 111   |    9063|     108.996|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  99   |      96|       3.186|   1.048/ 14|   1.053/ 13|   1.054/ 13|   1.055/ 12 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 109   |     193|      18.039|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 104   |     879|      52.935|   1.051/ 13|   1.048/ 14|   1.047/ 15|   1.046/ 15 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  74   |      29|       2.395|   1.014/ 51|   1.015/ 45|   1.016/ 44|   1.016/ 43 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  63   |      21|      13.398|   1.033/ 21|   1.038/ 18|   1.040/ 17|   1.041/ 17 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  84   |     108|       9.332|   1.028/ 25|   1.024/ 29|   1.023/ 31|   1.021/ 32 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  94   |     453|      49.484|   1.032/ 22|   1.033/ 21|   1.033/ 21|   1.034/ 20 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|       0.267|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 105   |     593|      60.632|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 109   |   17060|      12.533|   1.031/ 22|   1.029/ 24|   1.028/ 24|   1.028/ 25 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 109   |    2783|      10.425|   1.019/ 37|   1.018/ 38|   1.018/ 38|   1.018/ 39 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 129   |   10096|     121.091|   1.011/ 61|   1.012/ 58|   1.012/ 57|   1.012/ 57 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 116   |    1478|      37.773|   1.088/  8|   1.093/  7|   1.095/  7|   1.096/  7 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 109   |    1750|     355.680|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  99   |     313|      34.112|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 128   |   35271|     585.529|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 101   |      10|       3.767|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 136   |    1036|       8.227|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  93   |       9|       0.844|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  95   |     154|       8.235|   1.057/ 12|   1.061/ 11|   1.062/ 11|   1.063/ 11 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  94   |     146|       3.061|   1.026/ 27|   1.024/ 28|   1.024/ 29|   1.024/ 29 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  94   |      36|      20.112|   1.010/ 70|   1.011/ 61|   1.012/ 60|   1.012/ 58 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  85   |     365|      82.672|   1.012/ 59|   1.007/ 96|   1.006/ **|   1.005/ ** |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  86   |      46|       7.038|   1.039/ 18|   1.041/ 17|   1.041/ 17|   1.042/ 16 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  86   |      31|      16.444|   1.007/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 110   |      34|       4.953|   1.007/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  85   |      35|       7.896|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  87   |      17|       2.422|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  99   |      80|      28.566|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  42   |      17|       0.649|   1.034/ 20|   1.028/ 24|   1.026/ 26|   1.024/ 28 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 103   |     122|       3.733|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  91   |     122|       6.002|   1.009/ 75|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  90   |     178|      43.634|   1.028/ 25|   1.020/ 35|   1.018/ 39|   1.016/ 45 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 101   |   27629|     218.274|   1.033/ 21|   1.031/ 22|   1.030/ 23|   1.030/ 23 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 102   |     534|     199.249|   1.020/ 34|   1.019/ 35|   1.019/ 36|   1.019/ 36 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 110   |     219|       6.103|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  34   |       5|       0.179|   1.053/ 13|   1.016/ 43|   1.006/ **|   1.000/ -- |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  43   |      28|       0.920|   1.035/ 20|   1.033/ 21|   1.032/ 21|   1.032/ 21 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 114   |    6190|     354.597|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  91   |      22|       4.435|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  93   |      83|      12.795|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  95   |      68|       3.041|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  97   |     596|       2.890|   1.022/ 31|   1.021/ 34|   1.020/ 35|   1.019/ 35 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  98   |     273|     131.214|   1.030/ 23|   1.032/ 22|   1.032/ 21|   1.032/ 21 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 106   |     248|      46.246|   1.002/ **|   1.002/ **|   1.002/ **|   1.003/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  89   |     172|      36.887|   1.035/ 20|   1.030/ 23|   1.029/ 24|   1.028/ 25 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 101   |    4484|      20.442|   1.036/ 19|   1.034/ 20|   1.033/ 21|   1.033/ 21 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 109   |     569|     134.972|   1.022/ 31|   1.023/ 29|   1.024/ 29|   1.024/ 29 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  99   |      13|       1.851|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 100   |    9471|     294.749|   1.025/ 28|   1.023/ 30|   1.023/ 30|   1.022/ 31 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 147   |    1258|      11.593|   1.008/ 83|   1.008/ 91|   1.007/ 93|   1.007/ 95 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 108   |    1442|      37.569|   1.011/ 64|   1.011/ 65|   1.011/ 65|   1.011/ 65 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 103   |    1593|     155.037|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  92   |     124|      45.120|   1.032/ 22|   1.025/ 27|   1.024/ 29|   1.022/ 31 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  98   |    1586|      81.739|   1.009/ 78|   1.009/ 77|   1.009/ 77|   1.009/ 77 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 101   |    9633|      65.643|   1.019/ 36|   1.016/ 44|   1.015/ 46|   1.014/ 49 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  29   |       2|       0.162|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  96   |    1616|      47.240|   1.038/ 18|   1.036/ 19|   1.036/ 19|   1.035/ 19 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  88   |     100|       6.177|   1.037/ 19|   1.039/ 18|   1.039/ 18|   1.040/ 17 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 100   |     266|      38.189|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  66   |      57|       7.253|   1.011/ 62|   1.013/ 53|   1.013/ 51|   1.014/ 49 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  99   |      27|       4.689|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  92   |      28|       5.132|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 106   |     110|      52.413|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  81   |      93|       5.855|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  93   |    2662|      45.289|   1.042/ 16|   1.037/ 18|   1.036/ 19|   1.035/ 20 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|       1.044|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 117   |   27908|     592.519|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  92   |      11|       0.517|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 107   |     699|      16.478|   1.019/ 36|   1.013/ 53|   1.011/ 61|   1.010/ 70 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 109   |    5403|     522.629|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 115   |    1967|     228.596|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  91   |       8|       0.455|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  89   |      21|       0.376|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 119   |      59|       0.880|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  93   |      14|       1.792|   1.005/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  95   |       8|       5.865|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 101   |      50|       4.295|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 103   |    5101|      61.346|   1.004/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 120   |  127759|     387.683|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 107   |    1133|      27.058|   1.016/ 44|   1.015/ 47|   1.015/ 48|   1.014/ 48 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 100   |     316|      31.916|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 109   |   44360|     667.721|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  91   |      26|       7.282|   1.008/ 91|   1.009/ 81|   1.009/ 78|   1.009/ 76 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  93   |      21|       0.612|   1.007/ 97|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  93   |      41|       1.269|   1.039/ 18|   1.041/ 17|   1.042/ 16|   1.043/ 16 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  87   |      17|       0.943|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  97   |       5|       0.334|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |

