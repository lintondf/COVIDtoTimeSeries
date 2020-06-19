# State and Country COVID-19 Analysis #
## Updated: 2020-06-19 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  97   |   31307|    1609.321|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 101   |   13128|    1478.030|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  91   |    7988|    1149.390|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  94   |    6783|     535.268|   1.009/ 73|   1.007/ 94|   1.007/ **|   1.006/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  92   |    6578|     513.806|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  92   |    6228|     623.591|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 107   |    5516|     139.591|   1.013/ 55|   1.011/ 62|   1.011/ 64|   1.010/ 67 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  92   |    4349|    1219.756|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  97   |    3119|     670.912|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 103   |    3132|     145.818|   1.011/ 62|   1.010/ 70|   1.010/ 72|   1.009/ 74 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 111   |  122374|     371.343|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  94   |   51323|     242.761|   1.025/ 28|   1.021/ 33|   1.020/ 35|   1.019/ 37 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 100   |   43296|     651.704|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 119   |   35075|     582.271|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 125   |   30166|     449.735|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 108   |   27149|     576.417|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  92   |   20979|     165.736|   1.035/ 20|   1.032/ 22|   1.031/ 22|   1.030/ 23 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 100   |   11576|       8.504|   1.040/ 17|   1.039/ 18|   1.039/ 18|   1.038/ 18 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 100   |    9806|     850.910|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 120   |    9123|     109.424|   1.009/ 74|   1.010/ 72|   1.010/ 71|   1.010/ 71 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  86   |     827|     168.637|   1.013/ 53|   1.012/ 59|   1.011/ 61|   1.011/ 63 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  86   |      12|      16.048|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  90   |    1294|     177.754|   1.018/ 39|   1.017/ 41|   1.017/ 42|   1.016/ 42 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  87   |     198|      65.552|   1.024/ 28|   1.025/ 27|   1.026/ 27|   1.026/ 27 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 107   |    5516|     139.591|   1.013/ 55|   1.011/ 62|   1.011/ 64|   1.010/ 67 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  97   |    1696|     294.538|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  92   |    4349|    1219.756|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  85   |     445|     457.362|   1.008/ 87|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 103   |    3132|     145.818|   1.011/ 62|   1.010/ 70|   1.010/ 72|   1.009/ 74 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  99   |    2619|     246.706|   1.014/ 51|   1.013/ 53|   1.013/ 53|   1.013/ 54 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  80   |      17|      12.007|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  85   |      89|      49.673|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  94   |    6783|     535.268|   1.009/ 73|   1.007/ 94|   1.007/ **|   1.006/ ** |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  95   |    2560|     380.299|   1.007/ 94|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  86   |     725|     229.704|   1.011/ 62|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  98   |     254|      87.207|   1.006/ **|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  95   |     534|     119.550|   1.010/ 71|   1.008/ 83|   1.008/ 86|   1.008/ 90 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  97   |    3119|     670.912|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  84   |     108|      80.232|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  92   |    3135|     518.590|   1.009/ 78|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  91   |    7988|    1149.390|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  92   |    6228|     623.591|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  90   |    1457|     258.399|   1.014/ 49|   1.011/ 62|   1.010/ 66|   1.010/ 71 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  92   |     985|     331.006|   1.013/ 53|   1.011/ 65|   1.010/ 69|   1.009/ 74 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  92   |     945|     153.935|   1.010/ 68|   1.009/ 78|   1.009/ 81|   1.008/ 85 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  84   |      19|      18.014|   1.010/ 70|   1.012/ 60|   1.012/ 58|   1.012/ 56 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  83   |     236|     121.984|   1.020/ 34|   1.020/ 34|   1.020/ 34|   1.020/ 34 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  95   |     485|     157.364|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  88   |     351|     257.822|   1.015/ 45|   1.013/ 55|   1.012/ 58|   1.011/ 62 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 101   |   13128|    1478.030|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  86   |     468|     223.338|   1.013/ 53|   1.011/ 61|   1.011/ 64|   1.010/ 66 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  97   |   31307|    1609.321|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  86   |    1237|     117.944|   1.014/ 51|   1.012/ 59|   1.011/ 62|   1.011/ 65 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  84   |      81|     106.210|   1.008/ 84|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  91   |    2747|     234.999|   1.009/ 75|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  92   |     374|      94.532|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  96   |     182|      43.169|   1.011/ 65|   1.011/ 62|   1.011/ 61|   1.012/ 60 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  92   |    6578|     513.806|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  90   |     151|      47.163|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  83   |     915|     863.527|   1.012/ 60|   1.009/ 78|   1.008/ 85|   1.008/ 92 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  95   |     641|     124.554|   1.013/ 55|   1.011/ 61|   1.011/ 62|   1.011/ 64 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 100   |      82|      92.369|   1.015/ 47|   1.013/ 54|   1.012/ 56|   1.012/ 57 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  90   |     507|      74.143|   1.018/ 39|   1.018/ 39|   1.018/ 39|   1.018/ 39 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  94   |    2138|      73.726|   1.012/ 56|   1.011/ 61|   1.011/ 63|   1.011/ 64 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  89   |     151|      47.201|   1.017/ 40|   1.017/ 42|   1.016/ 42|   1.016/ 42 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  91   |      55|      88.872|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  97   |    1688|     197.802|   1.007/ 93|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 111   |    1257|     165.038|   1.005/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  81   |      91|      50.828|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  91   |     746|     128.134|   1.011/ 63|   1.009/ 74|   1.009/ 78|   1.008/ 82 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  67   |      19|      32.719|   1.005/ **|   1.000/ --|   1.000/ --|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  89   |     533|      16.552|   1.039/ 18|   1.040/ 17|   1.040/ 17|   1.040/ 17 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 100   |      37|      12.857|   1.010/ 71|   1.011/ 61|   1.012/ 59|   1.012/ 57 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  99   |     808|      18.784|   1.012/ 57|   1.012/ 57|   1.012/ 57|   1.012/ 57 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  82   |       6|       0.203|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 103   |     926|      20.605|   1.031/ 23|   1.031/ 22|   1.031/ 22|   1.031/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  85   |     347|     117.388|   1.045/ 15|   1.042/ 16|   1.041/ 17|   1.040/ 17 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 110   |     103|       4.017|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  99   |     690|      77.495|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  98   |     138|      13.735|   1.043/ 16|   1.044/ 16|   1.044/ 16|   1.044/ 16 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  95   |      47|      30.417|   1.067/ 10|   1.074/  9|   1.076/  9|   1.078/  9 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  93   |    1417|       8.412|   1.040/ 17|   1.038/ 18|   1.038/ 18|   1.037/ 19 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  80   |     336|      35.726|   1.019/ 37|   1.017/ 40|   1.017/ 41|   1.017/ 41 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 100   |    9806|     850.910|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  74   |       6|       0.524|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  82   |     725|      63.229|   1.040/ 17|   1.039/ 18|   1.038/ 18|   1.038/ 18 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  90   |     171|      51.751|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  80   |       1|       0.428|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  94   |   51323|     242.761|   1.025/ 28|   1.021/ 33|   1.020/ 35|   1.019/ 37 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 100   |     191|      27.480|   1.015/ 46|   1.014/ 50|   1.014/ 51|   1.013/ 52 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  93   |      53|       2.560|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  67   |       1|       0.091|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  86   |     261|       9.814|   1.005/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 102   |    8825|     232.239|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  27   |      19|       3.416|   1.097/  7|   1.293/  2|   1.337/  2|   1.380/  2 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  52   |      75|       4.616|   1.007/ 98|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  89   |    4022|     210.507|   1.058/ 12|   1.056/ 12|   1.056/ 12|   1.056/ 12 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 100   |    4638|       3.308|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  89   |    1962|      39.713|   1.042/ 16|   1.043/ 16|   1.043/ 16|   1.043/ 16 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  92   |      12|       2.393|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  92   |     109|      26.653|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  93   |      85|       7.568|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  97   |     606|     104.094|   1.002/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  94   |     618|      59.655|   1.014/ 48|   1.015/ 45|   1.016/ 44|   1.016/ 43 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  97   |    4155|     237.854|   1.009/ 77|   1.007/ 96|   1.007/ **|   1.006/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 103   |    1799|      17.942|   1.041/ 17|   1.044/ 16|   1.044/ 16|   1.045/ 15 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  80   |      83|      12.765|   1.033/ 21|   1.033/ 21|   1.033/ 21|   1.032/ 21 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  58   |      12|       8.843|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  75   |      79|       0.802|   1.150/  4|   1.169/  4|   1.173/  4|   1.178/  4 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  90   |     331|      59.948|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 125   |   30166|     449.735|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  91   |      30|      13.628|   1.028/ 25|   1.027/ 26|   1.026/ 26|   1.026/ 27 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  88   |       1|       0.426|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  76   |      14|       3.767|   1.005/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 102   |    8994|     108.171|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  90   |      59|       1.944|   1.036/ 19|   1.040/ 17|   1.042/ 17|   1.043/ 16 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 100   |     189|      17.659|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  95   |     546|      32.882|   1.064/ 11|   1.062/ 11|   1.061/ 11|   1.060/ 11 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  65   |      26|       2.115|   1.010/ 68|   1.010/ 67|   1.011/ 65|   1.011/ 64 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  54   |      17|      10.379|   1.014/ 48|   1.016/ 44|   1.016/ 43|   1.017/ 42 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  75   |      85|       7.378|   1.043/ 16|   1.042/ 17|   1.041/ 17|   1.041/ 17 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  85   |     352|      38.456|   1.026/ 26|   1.025/ 27|   1.025/ 27|   1.025/ 28 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|       0.267|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  96   |     585|      59.810|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 100   |   11576|       8.504|   1.040/ 17|   1.039/ 18|   1.039/ 18|   1.038/ 18 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 100   |    2348|       8.795|   1.021/ 32|   1.021/ 33|   1.021/ 33|   1.021/ 33 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 120   |    9123|     109.424|   1.009/ 74|   1.010/ 72|   1.010/ 71|   1.010/ 71 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 107   |     643|      16.423|   1.083/  8|   1.091/  7|   1.094/  7|   1.096/  7 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 100   |    1741|     353.805|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  90   |     306|      33.314|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 119   |   35075|     582.271|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  92   |      10|       3.747|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 127   |    1040|       8.258|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  84   |       9|       0.844|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  86   |      87|       4.644|   1.054/ 13|   1.062/ 11|   1.064/ 11|   1.066/ 10 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  85   |     115|       2.419|   1.030/ 23|   1.030/ 23|   1.030/ 23|   1.030/ 23 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  85   |      32|      18.058|   1.007/ **|   1.008/ 88|   1.008/ 85|   1.008/ 82 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  76   |     337|      76.214|   1.019/ 36|   1.012/ 56|   1.010/ 66|   1.009/ 79 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  77   |      31|       4.794|   1.034/ 20|   1.037/ 19|   1.037/ 18|   1.038/ 18 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  77   |      29|      15.260|   1.013/ 52|   1.014/ 49|   1.015/ 48|   1.015/ 47 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 101   |      32|       4.668|   1.010/ 71|   1.011/ 63|   1.011/ 61|   1.012/ 59 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  76   |      34|       7.561|   1.010/ 70|   1.009/ 80|   1.008/ 83|   1.008/ 87 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  78   |       9|       1.340|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  90   |      79|      28.108|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  33   |      12|       0.468|   1.038/ 18|   1.046/ 15|   1.049/ 14|   1.052/ 13 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  94   |     121|       3.680|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  82   |     113|       5.595|   1.017/ 41|   1.014/ 50|   1.013/ 53|   1.012/ 57 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  81   |     169|      41.375|   1.051/ 13|   1.046/ 15|   1.044/ 16|   1.043/ 16 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  92   |   20979|     165.736|   1.035/ 20|   1.032/ 22|   1.031/ 22|   1.030/ 23 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  93   |     444|     165.416|   1.022/ 31|   1.022/ 31|   1.022/ 32|   1.022/ 32 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 101   |     216|       6.014|   1.002/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  25   |       4|       0.142|   1.000/ --|   1.073/  9|   1.089/  8|   1.105/  6 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  34   |      22|       0.720|   1.052/ 13|   1.040/ 17|   1.038/ 18|   1.035/ 20 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 105   |    6181|     354.094|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  82   |      22|       4.463|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  84   |      76|      11.757|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  86   |      68|       3.048|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  88   |     480|       2.327|   1.029/ 24|   1.029/ 24|   1.029/ 24|   1.028/ 24 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  89   |     203|      97.675|   1.029/ 23|   1.032/ 22|   1.033/ 21|   1.033/ 21 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  97   |     243|      45.328|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  80   |     128|      27.480|   1.047/ 15|   1.044/ 16|   1.043/ 16|   1.043/ 16 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  92   |    3188|      14.536|   1.045/ 15|   1.046/ 15|   1.046/ 15|   1.046/ 15 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 100   |     470|     111.371|   1.019/ 37|   1.019/ 36|   1.019/ 36|   1.019/ 35 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  90   |      11|       1.600|   1.004/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  91   |    7616|     237.012|   1.028/ 24|   1.026/ 26|   1.026/ 27|   1.025/ 27 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 138   |    1171|      10.788|   1.007/ 95|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  99   |    1309|      34.107|   1.010/ 68|   1.010/ 71|   1.010/ 72|   1.010/ 73 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  94   |    1578|     153.528|   1.004/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  83   |      93|      34.018|   1.046/ 15|   1.040/ 17|   1.039/ 18|   1.037/ 18 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  89   |    1463|      75.411|   1.008/ 88|   1.008/ 92|   1.007/ 93|   1.007/ 94 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  92   |    8182|      55.757|   1.027/ 26|   1.023/ 30|   1.022/ 31|   1.021/ 32 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  20   |       2|       0.162|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  87   |    1136|      33.203|   1.046/ 15|   1.048/ 14|   1.048/ 14|   1.048/ 14 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  79   |      70|       4.290|   1.037/ 19|   1.041/ 17|   1.042/ 16|   1.043/ 16 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  91   |     258|      37.060|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  57   |      52|       6.594|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  90   |      26|       4.607|   1.005/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  83   |      28|       5.135|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  97   |     110|      52.666|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  72   |      92|       5.814|   1.008/ 89|   1.004/ **|   1.003/ **|   1.002/ ** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  84   |    1875|      31.903|   1.053/ 13|   1.049/ 14|   1.049/ 14|   1.048/ 14 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|       1.044|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 108   |   27149|     576.417|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  83   |      11|       0.526|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  98   |     602|      14.190|   1.032/ 22|   1.026/ 27|   1.024/ 29|   1.022/ 31 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 100   |    5181|     501.171|   1.007/ 96|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 106   |    1956|     227.354|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  82   |       7|       0.407|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  80   |      21|       0.376|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 110   |      59|       0.880|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  84   |      13|       1.758|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  86   |       8|       5.865|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  92   |      50|       4.256|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  94   |    4945|      59.471|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 111   |  122374|     371.343|   1.006/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  98   |     992|      23.687|   1.016/ 43|   1.014/ 49|   1.014/ 51|   1.013/ 52 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  91   |     303|      30.642|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 100   |   43296|     651.704|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  82   |      24|       6.818|   1.004/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  84   |      20|       0.594|   1.012/ 56|   1.010/ 67|   1.010/ 71|   1.009/ 76 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  84   |      30|       0.921|   1.029/ 24|   1.031/ 22|   1.032/ 22|   1.032/ 21 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  78   |      11|       0.617|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  88   |       4|       0.264|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |

