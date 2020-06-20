# State and Country COVID-19 Analysis #
## Updated: 2020-06-20 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  98   |   31354|    1611.721|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 102   |   13184|    1484.289|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  92   |    8025|    1154.785|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  95   |    6823|     538.445|   1.009/ 75|   1.007/ 96|   1.007/ **|   1.006/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  93   |    6600|     515.571|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  93   |    6242|     624.983|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 108   |    5585|     141.346|   1.013/ 55|   1.011/ 62|   1.011/ 63|   1.011/ 65 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  93   |    4352|    1220.537|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 104   |    3167|     147.464|   1.011/ 62|   1.010/ 69|   1.010/ 71|   1.010/ 73 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  98   |    3132|     673.687|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 112   |  123071|     373.459|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  95   |   52285|     247.312|   1.025/ 28|   1.021/ 33|   1.020/ 35|   1.019/ 37 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 101   |   43428|     653.684|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 120   |   35121|     583.025|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 126   |   30193|     450.134|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 109   |   27227|     578.069|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  93   |   21608|     170.711|   1.035/ 20|   1.032/ 22|   1.031/ 22|   1.030/ 23 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 101   |   12190|       8.955|   1.038/ 18|   1.037/ 19|   1.037/ 19|   1.036/ 19 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 101   |    9806|     850.868|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 121   |    9218|     110.556|   1.010/ 72|   1.010/ 70|   1.010/ 69|   1.010/ 69 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  87   |     837|     170.631|   1.013/ 52|   1.012/ 58|   1.012/ 59|   1.011/ 61 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  87   |      12|      16.256|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  91   |    1318|     181.061|   1.018/ 38|   1.018/ 39|   1.017/ 40|   1.017/ 40 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  88   |     204|      67.464|   1.026/ 26|   1.028/ 25|   1.028/ 24|   1.029/ 24 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 108   |    5585|     141.346|   1.013/ 55|   1.011/ 62|   1.011/ 63|   1.011/ 65 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  98   |    1704|     295.924|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  93   |    4352|    1220.537|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  86   |     448|     460.258|   1.008/ 90|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 104   |    3167|     147.464|   1.011/ 62|   1.010/ 69|   1.010/ 71|   1.010/ 73 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 100   |    2655|     250.039|   1.014/ 51|   1.013/ 53|   1.013/ 53|   1.013/ 54 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  81   |      17|      12.007|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  86   |      89|      49.896|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  95   |    6823|     538.445|   1.009/ 75|   1.007/ 96|   1.007/ **|   1.006/ ** |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  96   |    2579|     383.123|   1.007/ 93|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  87   |     727|     230.499|   1.010/ 66|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  99   |     256|      87.742|   1.007/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  96   |     538|     120.531|   1.010/ 72|   1.008/ 82|   1.008/ 85|   1.008/ 89 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  98   |    3132|     673.687|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  85   |     108|      80.287|   1.006/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  93   |    3151|     521.138|   1.008/ 83|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  92   |    8025|    1154.785|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  93   |    6242|     624.983|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  91   |    1471|     260.800|   1.014/ 50|   1.011/ 64|   1.010/ 68|   1.009/ 74 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  93   |     992|     333.471|   1.012/ 55|   1.010/ 69|   1.009/ 74|   1.009/ 80 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  93   |     956|     155.688|   1.011/ 61|   1.010/ 67|   1.010/ 69|   1.010/ 70 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  85   |      19|      18.236|   1.011/ 64|   1.013/ 55|   1.013/ 53|   1.014/ 51 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  84   |     241|     124.593|   1.020/ 34|   1.020/ 34|   1.020/ 34|   1.021/ 34 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  96   |     488|     158.377|   1.007/ **|   1.006/ **|   1.005/ **|   1.005/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  89   |     354|     260.507|   1.015/ 47|   1.012/ 58|   1.011/ 62|   1.011/ 66 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 102   |   13184|    1484.289|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  87   |     473|     225.714|   1.013/ 53|   1.011/ 62|   1.011/ 64|   1.010/ 67 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  98   |   31354|    1611.721|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  87   |    1248|     118.968|   1.013/ 54|   1.011/ 64|   1.010/ 67|   1.010/ 70 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  85   |      81|     106.401|   1.008/ 88|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  92   |    2769|     236.912|   1.009/ 77|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  93   |     375|      94.803|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  97   |     184|      43.678|   1.011/ 65|   1.011/ 61|   1.011/ 60|   1.012/ 59 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  93   |    6600|     515.571|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  91   |     151|      47.248|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  84   |     924|     872.055|   1.011/ 61|   1.009/ 80|   1.008/ 86|   1.007/ 93 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  96   |     650|     126.176|   1.013/ 54|   1.012/ 58|   1.012/ 60|   1.011/ 61 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 101   |      83|      93.589|   1.015/ 47|   1.013/ 53|   1.013/ 55|   1.012/ 56 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  91   |     515|      75.418|   1.017/ 40|   1.017/ 40|   1.017/ 40|   1.017/ 39 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  95   |    2163|      74.591|   1.013/ 55|   1.012/ 58|   1.012/ 59|   1.011/ 60 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  90   |     154|      48.087|   1.018/ 39|   1.017/ 40|   1.017/ 40|   1.017/ 40 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  92   |      56|      89.041|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  98   |    1698|     198.953|   1.007/ 98|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 112   |    1264|     166.028|   1.005/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  82   |      91|      51.005|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  92   |     753|     129.369|   1.011/ 63|   1.009/ 74|   1.009/ 78|   1.009/ 81 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  68   |      19|      33.280|   1.006/ **|   1.002/ **|   1.001/ **|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  90   |     553|      17.174|   1.039/ 18|   1.040/ 17|   1.040/ 17|   1.040/ 17 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 101   |      37|      12.992|   1.011/ 61|   1.013/ 52|   1.014/ 50|   1.014/ 48 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 100   |     818|      19.029|   1.012/ 56|   1.012/ 56|   1.012/ 56|   1.012/ 55 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  83   |       6|       0.208|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 104   |     956|      21.270|   1.031/ 22|   1.032/ 22|   1.032/ 21|   1.032/ 21 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  86   |     360|     121.828|   1.043/ 16|   1.039/ 18|   1.038/ 18|   1.037/ 19 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 111   |     103|       4.013|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 100   |     691|      77.646|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  99   |     144|      14.324|   1.043/ 16|   1.044/ 16|   1.044/ 16|   1.044/ 16 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  96   |      50|      32.592|   1.068/ 10|   1.075/  9|   1.076/  9|   1.078/  9 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  94   |    1470|       8.727|   1.039/ 17|   1.037/ 19|   1.036/ 19|   1.036/ 19 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  81   |     342|      36.332|   1.019/ 37|   1.017/ 40|   1.017/ 40|   1.017/ 41 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 101   |    9806|     850.868|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  75   |       8|       0.688|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  83   |     750|      65.430|   1.039/ 18|   1.037/ 19|   1.036/ 19|   1.036/ 19 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  91   |     171|      51.905|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  81   |       1|       0.428|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  95   |   52285|     247.312|   1.025/ 28|   1.021/ 33|   1.020/ 35|   1.019/ 37 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 101   |     194|      27.889|   1.015/ 45|   1.014/ 48|   1.014/ 48|   1.014/ 49 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  94   |      53|       2.559|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  68   |       1|       0.091|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  87   |     268|      10.084|   1.005/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 103   |    8848|     232.846|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  28   |      21|       3.795|   1.140/  5|   1.340/  2|   1.385/  2|   1.427/  1 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  53   |      75|       4.629|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  90   |    4289|     224.473|   1.059/ 12|   1.058/ 12|   1.057/ 12|   1.057/ 12 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 101   |    4638|       3.308|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  90   |    2042|      41.349|   1.042/ 16|   1.043/ 16|   1.043/ 16|   1.043/ 16 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  93   |      12|       2.407|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  93   |     109|      26.667|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  94   |      85|       7.581|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  98   |     607|     104.237|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  95   |     628|      60.631|   1.015/ 47|   1.016/ 44|   1.016/ 43|   1.016/ 42 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  98   |    4199|     240.397|   1.009/ 74|   1.008/ 87|   1.008/ 90|   1.007/ 94 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 104   |    1877|      18.723|   1.042/ 16|   1.044/ 15|   1.045/ 15|   1.046/ 15 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  81   |      86|      13.215|   1.034/ 20|   1.034/ 20|   1.034/ 20|   1.034/ 20 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  59   |      12|       8.838|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  76   |      85|       0.864|   1.136/  5|   1.147/  5|   1.150/  4|   1.152/  4 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  91   |     331|      59.902|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 126   |   30193|     450.134|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  92   |      31|      14.255|   1.033/ 21|   1.034/ 20|   1.034/ 20|   1.034/ 20 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  89   |       1|       0.426|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  77   |      14|       3.792|   1.004/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 103   |    9001|     108.248|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  91   |      62|       2.035|   1.039/ 18|   1.044/ 16|   1.045/ 15|   1.047/ 15 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 101   |     190|      17.704|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  96   |     581|      34.988|   1.062/ 11|   1.059/ 12|   1.058/ 12|   1.057/ 12 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  66   |      26|       2.147|   1.010/ 66|   1.011/ 61|   1.012/ 60|   1.012/ 58 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  55   |      17|      10.708|   1.018/ 39|   1.022/ 32|   1.023/ 31|   1.023/ 29 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  76   |      89|       7.670|   1.042/ 17|   1.039/ 17|   1.039/ 18|   1.039/ 18 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  86   |     360|      39.360|   1.026/ 27|   1.024/ 28|   1.024/ 29|   1.024/ 29 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|       0.267|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  97   |     585|      59.890|   1.004/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 101   |   12190|       8.955|   1.038/ 18|   1.037/ 19|   1.037/ 19|   1.036/ 19 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 101   |    2395|       8.972|   1.021/ 33|   1.021/ 33|   1.021/ 33|   1.021/ 34 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 121   |    9218|     110.556|   1.010/ 72|   1.010/ 70|   1.010/ 69|   1.010/ 69 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 108   |     705|      18.028|   1.084/  8|   1.093/  7|   1.095/  7|   1.097/  7 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 101   |    1742|     353.903|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  91   |     307|      33.376|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 120   |   35121|     583.025|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  93   |      10|       3.756|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 128   |    1041|       8.269|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  85   |       9|       0.844|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  87   |      93|       4.966|   1.057/ 12|   1.066/ 10|   1.068/ 10|   1.071/ 10 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  86   |     119|       2.498|   1.032/ 22|   1.032/ 22|   1.032/ 22|   1.032/ 22 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  86   |      33|      18.171|   1.006/ **|   1.007/ 97|   1.007/ 93|   1.008/ 90 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  77   |     339|      76.781|   1.018/ 39|   1.011/ 63|   1.009/ 75|   1.008/ 92 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  78   |      32|       4.940|   1.033/ 21|   1.035/ 20|   1.035/ 19|   1.036/ 19 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  78   |      30|      15.480|   1.014/ 48|   1.016/ 44|   1.016/ 43|   1.017/ 41 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 102   |      32|       4.704|   1.009/ 76|   1.010/ 69|   1.010/ 67|   1.010/ 66 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  77   |      34|       7.600|   1.009/ 78|   1.007/ 95|   1.007/ **|   1.007/ ** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  79   |      10|       1.414|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  91   |      79|      28.143|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  34   |      13|       0.488|   1.036/ 19|   1.043/ 16|   1.046/ 15|   1.049/ 14 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  95   |     121|       3.689|   1.002/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  83   |     114|       5.652|   1.016/ 43|   1.013/ 53|   1.012/ 56|   1.012/ 60 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  82   |     176|      43.098|   1.052/ 13|   1.044/ 15|   1.042/ 16|   1.040/ 17 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  93   |   21608|     170.711|   1.035/ 20|   1.032/ 22|   1.031/ 22|   1.030/ 23 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  94   |     453|     169.060|   1.022/ 31|   1.022/ 31|   1.022/ 32|   1.022/ 32 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 102   |     216|       6.023|   1.002/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  26   |       4|       0.147|   1.018/ 39|   1.091/  7|   1.108/  6|   1.124/  5 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  35   |      22|       0.745|   1.049/ 14|   1.042/ 16|   1.040/ 17|   1.039/ 18 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 106   |    6185|     354.319|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  83   |      22|       4.459|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  85   |      76|      11.797|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  87   |      68|       3.044|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  89   |     493|       2.390|   1.029/ 24|   1.028/ 25|   1.028/ 25|   1.028/ 25 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  90   |     209|     100.833|   1.030/ 23|   1.033/ 21|   1.033/ 21|   1.034/ 20 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  98   |     244|      45.404|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  81   |     133|      28.587|   1.045/ 15|   1.042/ 16|   1.041/ 17|   1.040/ 17 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  93   |    3336|      15.208|   1.045/ 15|   1.046/ 15|   1.046/ 15|   1.046/ 15 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 101   |     479|     113.553|   1.019/ 37|   1.019/ 36|   1.020/ 35|   1.020/ 35 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  91   |      12|       1.651|   1.004/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  92   |    7805|     242.911|   1.027/ 25|   1.025/ 27|   1.025/ 28|   1.024/ 29 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 139   |    1177|      10.850|   1.007/ 97|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 100   |    1325|      34.515|   1.011/ 65|   1.010/ 66|   1.010/ 66|   1.010/ 67 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  95   |    1579|     153.693|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  84   |      97|      35.442|   1.045/ 15|   1.040/ 17|   1.038/ 18|   1.037/ 19 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  90   |    1477|      76.092|   1.008/ 84|   1.008/ 86|   1.008/ 86|   1.008/ 87 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  93   |    8352|      56.912|   1.026/ 26|   1.023/ 30|   1.022/ 31|   1.021/ 33 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  21   |       2|       0.162|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  88   |    1186|      34.668|   1.046/ 15|   1.047/ 15|   1.047/ 15|   1.047/ 15 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  80   |      73|       4.481|   1.038/ 18|   1.042/ 16|   1.043/ 16|   1.044/ 15 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  92   |     259|      37.187|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  58   |      53|       6.651|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  91   |      26|       4.625|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  84   |      28|       5.134|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  98   |     110|      52.653|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  73   |      92|       5.813|   1.007/ **|   1.003/ **|   1.002/ **|   1.000/ ** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  85   |    1959|      33.329|   1.051/ 13|   1.048/ 14|   1.047/ 15|   1.046/ 15 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|       1.044|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 109   |   27227|     578.069|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  84   |      11|       0.526|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  99   |     615|      14.497|   1.030/ 23|   1.024/ 29|   1.022/ 31|   1.021/ 33 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 101   |    5204|     503.412|   1.007/ 98|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 107   |    1957|     227.491|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  83   |       7|       0.413|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  81   |      21|       0.376|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 111   |      59|       0.880|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  85   |      13|       1.753|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  87   |       8|       5.865|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  93   |      50|       4.262|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  95   |    4958|      59.627|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 112   |  123071|     373.459|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  99   |    1007|      24.041|   1.017/ 42|   1.015/ 46|   1.015/ 47|   1.014/ 49 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  92   |     305|      30.821|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 101   |   43428|     653.684|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  83   |      24|       6.833|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  85   |      20|       0.597|   1.011/ 63|   1.009/ 80|   1.008/ 87|   1.007/ 95 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  85   |      31|       0.951|   1.029/ 23|   1.032/ 21|   1.033/ 21|   1.033/ 21 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  79   |      11|       0.633|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  89   |       4|       0.264|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |

