# State and Country COVID-19 Analysis #
## Updated: 2020-06-27 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 105   |   31594|    1624.082|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 109   |   13757|    1548.840|   1.004/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  99   |    8196|    1179.356|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 102   |    7108|     560.962|   1.007/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 100   |    6762|     528.176|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 100   |    6313|     632.117|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 115   |    6015|     152.232|   1.012/ 60|   1.011/ 66|   1.010/ 67|   1.010/ 69 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 100   |    4395|    1232.754|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 111   |    3402|     158.406|   1.011/ 62|   1.010/ 66|   1.010/ 67|   1.010/ 68 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 105   |    3210|     690.467|   1.004/ **|   1.004/ **|   1.003/ **|   1.003/ ** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 119   |  126940|     385.199|   1.005/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 102   |   59639|     282.097|   1.021/ 33|   1.018/ 39|   1.017/ 41|   1.016/ 43 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 108   |   44268|     666.323|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 127   |   35247|     585.129|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 133   |   30213|     450.436|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 116   |   27832|     590.909|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 100   |   26855|     212.166|   1.033/ 21|   1.031/ 22|   1.031/ 22|   1.030/ 23 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 108   |   16451|      12.086|   1.032/ 22|   1.030/ 23|   1.029/ 24|   1.029/ 24 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 128   |    9974|     119.624|   1.011/ 62|   1.012/ 59|   1.012/ 58|   1.012/ 57 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 108   |    9821|     852.171|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  94   |     913|     186.183|   1.014/ 50|   1.013/ 52|   1.013/ 52|   1.013/ 52 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  94   |      13|      17.257|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  98   |    1503|     206.555|   1.021/ 33|   1.021/ 33|   1.021/ 33|   1.021/ 33 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  95   |     247|      81.902|   1.025/ 27|   1.026/ 27|   1.026/ 26|   1.026/ 26 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 115   |    6015|     152.232|   1.012/ 60|   1.011/ 66|   1.010/ 67|   1.010/ 69 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 105   |    1730|     300.497|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 100   |    4395|    1232.754|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  93   |     488|     501.332|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 111   |    3402|     158.406|   1.011/ 62|   1.010/ 66|   1.010/ 67|   1.010/ 68 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 107   |    2846|     268.006|   1.010/ 67|   1.009/ 73|   1.009/ 75|   1.009/ 78 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  88   |      17|      12.007|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  93   |      91|      50.830|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 102   |    7108|     560.962|   1.007/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 103   |    2672|     396.959|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  93   |     740|     234.651|   1.006/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 106   |     267|      91.734|   1.006/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 103   |     563|     126.031|   1.008/ 89|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 105   |    3210|     690.467|   1.004/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  92   |     108|      80.195|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 100   |    3262|     539.478|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  99   |    8196|    1179.356|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 100   |    6313|     632.117|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  98   |    1549|     274.665|   1.009/ 80|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 100   |    1055|     354.437|   1.011/ 64|   1.009/ 76|   1.009/ 79|   1.008/ 83 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 100   |    1021|     166.344|   1.009/ 75|   1.008/ 83|   1.008/ 86|   1.008/ 88 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  92   |      21|      19.781|   1.011/ 62|   1.012/ 55|   1.013/ 54|   1.013/ 53 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  91   |     270|     139.737|   1.017/ 41|   1.016/ 43|   1.016/ 44|   1.016/ 44 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 103   |     506|     164.406|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  96   |     377|     277.049|   1.011/ 61|   1.009/ 78|   1.008/ 84|   1.008/ 91 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 109   |   13757|    1548.840|   1.004/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  94   |     505|     240.656|   1.010/ 68|   1.008/ 81|   1.008/ 85|   1.008/ 90 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 105   |   31594|    1624.082|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  94   |    1360|     129.715|   1.014/ 50|   1.013/ 53|   1.013/ 53|   1.013/ 54 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  92   |      82|     108.250|   1.005/ **|   1.001/ **|   1.001/ **|   1.000/ -- |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  99   |    2882|     246.538|   1.007/ 99|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 100   |     383|      96.666|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 104   |     198|      46.994|   1.011/ 65|   1.011/ 63|   1.011/ 62|   1.011/ 61 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 100   |    6762|     528.176|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  98   |     153|      48.001|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  91   |     960|     906.616|   1.007/ 95|   1.005/ **|   1.004/ **|   1.004/ ** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 103   |     707|     137.279|   1.013/ 53|   1.012/ 56|   1.012/ 57|   1.012/ 58 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 108   |      90|     101.684|   1.013/ 51|   1.012/ 56|   1.012/ 57|   1.012/ 58 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  98   |     577|      84.431|   1.017/ 41|   1.017/ 41|   1.017/ 41|   1.017/ 41 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 102   |    2351|      81.084|   1.013/ 55|   1.012/ 57|   1.012/ 57|   1.012/ 57 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  97   |     171|      53.237|   1.014/ 48|   1.014/ 51|   1.013/ 52|   1.013/ 53 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  99   |      56|      89.803|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 105   |    1744|     204.376|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 119   |    1313|     172.487|   1.006/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  89   |      94|      52.396|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  99   |     795|     136.561|   1.009/ 81|   1.007/ 98|   1.007/ **|   1.006/ ** |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  75   |      20|      35.253|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  97   |     707|      21.924|   1.036/ 19|   1.036/ 19|   1.035/ 19|   1.035/ 20 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 108   |      44|      15.342|   1.022/ 31|   1.026/ 26|   1.027/ 25|   1.028/ 25 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 107   |     891|      20.723|   1.012/ 59|   1.012/ 59|   1.012/ 59|   1.012/ 60 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  90   |      10|       0.332|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 111   |    1178|      26.203|   1.030/ 23|   1.031/ 22|   1.031/ 22|   1.031/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  93   |     451|     152.543|   1.037/ 19|   1.034/ 21|   1.033/ 21|   1.032/ 22 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 118   |     103|       4.020|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 107   |     699|      78.560|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 106   |     191|      18.924|   1.041/ 17|   1.041/ 17|   1.041/ 17|   1.041/ 17 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 103   |      77|      50.131|   1.058/ 12|   1.060/ 11|   1.060/ 11|   1.060/ 11 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 101   |    1819|      10.799|   1.032/ 22|   1.029/ 24|   1.028/ 25|   1.027/ 26 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  88   |     382|      40.555|   1.016/ 42|   1.015/ 46|   1.015/ 47|   1.014/ 48 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 108   |    9821|     852.171|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  82   |      15|       1.305|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  90   |     964|      84.069|   1.038/ 18|   1.037/ 19|   1.036/ 19|   1.036/ 19 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  98   |     176|      53.219|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  88   |       1|       0.428|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 102   |   59639|     282.097|   1.021/ 33|   1.018/ 39|   1.017/ 41|   1.016/ 43 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 108   |     217|      31.223|   1.015/ 45|   1.015/ 46|   1.015/ 47|   1.015/ 47 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 101   |      53|       2.550|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  75   |       1|       0.091|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  94   |     322|      12.114|   1.011/ 62|   1.010/ 67|   1.010/ 68|   1.010/ 69 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 110   |    9027|     237.564|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  35   |      47|       8.515|   1.110/  6|   1.117/  6|   1.119/  6|   1.120/  6 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  60   |      75|       4.635|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  97   |    6136|     321.130|   1.045/ 15|   1.041/ 17|   1.040/ 17|   1.039/ 18 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 108   |    4639|       3.308|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  97   |    2772|      56.109|   1.042/ 16|   1.043/ 16|   1.043/ 16|   1.043/ 16 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 100   |      13|       2.477|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 100   |     109|      26.712|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 101   |      85|       7.627|   1.001/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 105   |     611|     104.907|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 102   |     699|      67.511|   1.015/ 46|   1.016/ 44|   1.016/ 44|   1.016/ 43 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 105   |    4440|     254.177|   1.009/ 78|   1.008/ 87|   1.008/ 89|   1.008/ 91 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 111   |    2549|      25.419|   1.042/ 16|   1.043/ 16|   1.044/ 16|   1.044/ 16 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  88   |     120|      18.544|   1.050/ 14|   1.054/ 13|   1.055/ 12|   1.056/ 12 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  66   |      38|      27.981|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  83   |     118|       1.195|   1.050/ 14|   1.035/ 20|   1.031/ 22|   1.027/ 26 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  98   |     331|      59.866|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 133   |   30213|     450.436|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  99   |      41|      18.790|   1.034/ 20|   1.034/ 20|   1.034/ 20|   1.034/ 20 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  96   |       1|       0.426|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  84   |      14|       3.869|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 110   |    9058|     108.941|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  98   |      91|       3.017|   1.050/ 14|   1.055/ 12|   1.057/ 12|   1.058/ 12 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 108   |     193|      18.015|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 103   |     839|      50.547|   1.052/ 13|   1.048/ 14|   1.047/ 15|   1.046/ 15 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  73   |      29|       2.357|   1.013/ 51|   1.015/ 45|   1.016/ 44|   1.016/ 42 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  62   |      21|      12.964|   1.030/ 23|   1.035/ 20|   1.036/ 19|   1.037/ 18 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  83   |     106|       9.122|   1.028/ 24|   1.024/ 29|   1.023/ 31|   1.021/ 32 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  93   |     438|      47.778|   1.030/ 23|   1.031/ 22|   1.031/ 22|   1.031/ 22 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|       0.267|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 104   |     592|      60.603|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 108   |   16451|      12.086|   1.032/ 22|   1.030/ 23|   1.029/ 24|   1.029/ 24 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 108   |    2735|      10.245|   1.019/ 36|   1.018/ 38|   1.018/ 38|   1.018/ 39 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 128   |    9974|     119.624|   1.011/ 62|   1.012/ 59|   1.012/ 58|   1.012/ 57 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 115   |    1361|      34.785|   1.088/  8|   1.095/  7|   1.096/  7|   1.098/  7 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 108   |    1750|     355.514|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  98   |     312|      33.964|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 127   |   35247|     585.129|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 100   |      10|       3.770|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 135   |    1035|       8.216|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  92   |       9|       0.844|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  94   |     144|       7.709|   1.055/ 12|   1.059/ 12|   1.060/ 11|   1.061/ 11 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  93   |     142|       2.988|   1.026/ 26|   1.025/ 28|   1.024/ 28|   1.024/ 29 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  93   |      36|      19.887|   1.011/ 63|   1.013/ 54|   1.013/ 52|   1.014/ 50 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  84   |     364|      82.279|   1.013/ 54|   1.008/ 86|   1.007/ **|   1.006/ ** |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  85   |      44|       6.784|   1.041/ 17|   1.043/ 16|   1.044/ 16|   1.045/ 15 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  85   |      31|      16.384|   1.007/ 93|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 109   |      34|       4.929|   1.007/ 96|   1.007/ 94|   1.007/ 94|   1.007/ 94 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  84   |      35|       7.883|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  86   |      15|       2.245|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  98   |      80|      28.541|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  41   |      17|       0.639|   1.035/ 20|   1.035/ 20|   1.035/ 20|   1.035/ 20 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 102   |     122|       3.730|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  90   |     121|       5.982|   1.010/ 68|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  89   |     175|      42.855|   1.030/ 23|   1.022/ 31|   1.020/ 34|   1.018/ 38 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 100   |   26855|     212.166|   1.033/ 21|   1.031/ 22|   1.031/ 22|   1.030/ 23 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 101   |     524|     195.500|   1.021/ 34|   1.020/ 35|   1.020/ 35|   1.019/ 35 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 109   |     218|       6.084|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  33   |       5|       0.179|   1.063/ 11|   1.024/ 29|   1.014/ 49|   1.004/ ** |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  42   |      27|       0.891|   1.034/ 20|   1.028/ 24|   1.027/ 26|   1.026/ 27 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 113   |    6188|     354.474|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  90   |      22|       4.439|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  92   |      82|      12.750|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  94   |      68|       3.044|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  96   |     585|       2.838|   1.024/ 29|   1.022/ 31|   1.022/ 32|   1.021/ 32 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  97   |     265|     127.396|   1.031/ 22|   1.033/ 21|   1.033/ 21|   1.033/ 21 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 105   |     248|      46.144|   1.002/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  88   |     167|      35.891|   1.035/ 20|   1.030/ 23|   1.029/ 24|   1.027/ 25 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 100   |    4348|      19.824|   1.037/ 18|   1.036/ 19|   1.035/ 19|   1.035/ 20 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 108   |     556|     131.753|   1.022/ 32|   1.023/ 30|   1.023/ 30|   1.023/ 29 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  98   |      13|       1.817|   1.000/ **|   1.000/ **|   1.001/ **|   1.001/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  99   |    9249|     287.852|   1.025/ 27|   1.024/ 29|   1.023/ 30|   1.023/ 30 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 146   |    1249|      11.506|   1.008/ 82|   1.008/ 91|   1.007/ 93|   1.007/ 95 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 107   |    1427|      37.181|   1.011/ 64|   1.011/ 64|   1.011/ 64|   1.011/ 64 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 102   |    1592|     154.953|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  91   |     121|      43.979|   1.034/ 20|   1.028/ 25|   1.026/ 26|   1.024/ 28 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  97   |    1572|      81.021|   1.009/ 78|   1.009/ 77|   1.009/ 76|   1.009/ 76 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 100   |    9497|      64.714|   1.020/ 35|   1.016/ 42|   1.015/ 45|   1.015/ 47 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  28   |       2|       0.162|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  95   |    1563|      45.670|   1.039/ 17|   1.038/ 18|   1.038/ 18|   1.037/ 19 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  87   |      96|       5.950|   1.037/ 18|   1.039/ 17|   1.040/ 17|   1.040/ 17 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  99   |     265|      38.044|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  65   |      56|       7.149|   1.010/ 72|   1.011/ 65|   1.011/ 63|   1.011/ 61 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  98   |      27|       4.688|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  91   |      28|       5.132|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 105   |     110|      52.426|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  80   |      93|       5.866|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  92   |    2574|      43.791|   1.043/ 16|   1.039/ 18|   1.038/ 18|   1.037/ 19 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|       1.044|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 116   |   27832|     590.909|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  91   |      11|       0.518|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 106   |     695|      16.365|   1.020/ 34|   1.014/ 49|   1.013/ 55|   1.011/ 63 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 108   |    5382|     520.595|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 114   |    1966|     228.488|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  90   |       8|       0.442|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  88   |      21|       0.376|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 118   |      59|       0.880|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  92   |      13|       1.781|   1.005/ **|   1.006/ **|   1.007/ **|   1.007/ 98 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  94   |       8|       5.865|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 100   |      50|       4.294|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 102   |    5084|      61.138|   1.004/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 119   |  126940|     385.199|   1.005/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 106   |    1117|      26.663|   1.015/ 45|   1.014/ 48|   1.014/ 49|   1.014/ 49 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  99   |     314|      31.766|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 108   |   44268|     666.323|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  90   |      25|       7.226|   1.008/ 87|   1.009/ 76|   1.009/ 73|   1.010/ 71 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  92   |      21|       0.610|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  92   |      39|       1.224|   1.039/ 18|   1.042/ 16|   1.043/ 16|   1.043/ 16 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  86   |      16|       0.868|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  96   |       4|       0.264|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |

