# State and Country COVID-19 Analysis #
## Updated: 2020-06-17 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  95   |   31228|    1605.278|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  99   |   13029|    1466.822|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  89   |    7921|    1139.756|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  92   |    6682|     527.302|   1.010/ 71|   1.007/ 94|   1.007/ **|   1.006/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  90   |    6519|     509.226|   1.007/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  90   |    6190|     619.798|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 105   |    5390|     136.424|   1.013/ 54|   1.011/ 62|   1.011/ 65|   1.010/ 67 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  90   |    4334|    1215.591|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  95   |    3097|     666.220|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 101   |    3069|     142.913|   1.011/ 61|   1.010/ 70|   1.010/ 73|   1.009/ 75 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 109   |  121183|     367.728|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  92   |   49235|     232.888|   1.026/ 27|   1.021/ 32|   1.020/ 34|   1.019/ 36 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  98   |   42998|     647.209|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 117   |   35017|     581.307|   1.001/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 123   |   30149|     449.478|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 106   |   27203|     577.547|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  90   |   19702|     155.651|   1.036/ 19|   1.032/ 22|   1.031/ 22|   1.030/ 23 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  98   |   10303|       7.569|   1.039/ 17|   1.038/ 18|   1.038/ 18|   1.038/ 18 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  98   |    9802|     850.503|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 118   |    8944|     107.274|   1.009/ 79|   1.009/ 77|   1.009/ 77|   1.009/ 77 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  84   |     808|     164.885|   1.014/ 50|   1.012/ 56|   1.012/ 58|   1.012/ 59 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  84   |      11|      15.582|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  88   |    1251|     171.830|   1.018/ 39|   1.016/ 42|   1.016/ 43|   1.016/ 44 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  85   |     188|      62.155|   1.021/ 32|   1.021/ 32|   1.021/ 32|   1.021/ 32 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 105   |    5390|     136.424|   1.013/ 54|   1.011/ 62|   1.011/ 65|   1.010/ 67 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  95   |    1684|     292.344|   1.006/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  90   |    4334|    1215.591|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  83   |     441|     452.435|   1.009/ 77|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 101   |    3069|     142.913|   1.011/ 61|   1.010/ 70|   1.010/ 73|   1.009/ 75 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  97   |    2551|     240.219|   1.013/ 52|   1.013/ 55|   1.012/ 56|   1.012/ 56 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  78   |      17|      12.007|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  83   |      88|      49.262|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  92   |    6682|     527.302|   1.010/ 71|   1.007/ 94|   1.007/ **|   1.006/ ** |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  93   |    2529|     375.707|   1.008/ 91|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  84   |     715|     226.617|   1.012/ 57|   1.007/ 95|   1.006/ **|   1.005/ ** |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  96   |     251|      86.212|   1.007/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  93   |     525|     117.506|   1.010/ 71|   1.008/ 84|   1.008/ 88|   1.007/ 93 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  95   |    3097|     666.220|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  82   |     107|      79.782|   1.008/ 90|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  90   |    3095|     511.854|   1.010/ 72|   1.007/ 93|   1.007/ **|   1.006/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  89   |    7921|    1139.756|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  90   |    6190|     619.798|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  88   |    1426|     252.853|   1.016/ 43|   1.013/ 53|   1.012/ 56|   1.012/ 59 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  90   |     964|     324.071|   1.013/ 52|   1.010/ 67|   1.010/ 72|   1.009/ 79 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  90   |     926|     150.875|   1.010/ 72|   1.008/ 90|   1.007/ 96|   1.007/ ** |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  82   |      19|      17.556|   1.008/ 87|   1.009/ 76|   1.009/ 74|   1.010/ 71 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  81   |     226|     117.088|   1.019/ 37|   1.018/ 39|   1.017/ 40|   1.017/ 40 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  93   |     479|     155.577|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  86   |     342|     251.690|   1.017/ 41|   1.014/ 49|   1.013/ 51|   1.013/ 54 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  99   |   13029|    1466.822|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  84   |     458|     218.428|   1.014/ 51|   1.011/ 60|   1.011/ 63|   1.010/ 66 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  95   |   31228|    1605.278|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  84   |    1210|     115.329|   1.014/ 50|   1.011/ 60|   1.011/ 63|   1.010/ 67 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  82   |      81|     105.638|   1.011/ 66|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  89   |    2711|     231.900|   1.010/ 68|   1.008/ 91|   1.007/ **|   1.006/ ** |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  90   |     371|      93.855|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  94   |     178|      42.187|   1.009/ 74|   1.010/ 72|   1.010/ 71|   1.010/ 71 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  90   |    6519|     509.226|   1.007/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  88   |     150|      46.890|   1.005/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  81   |     899|     848.420|   1.012/ 59|   1.008/ 83|   1.008/ 92|   1.007/ ** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  93   |     627|     121.812|   1.013/ 52|   1.012/ 56|   1.012/ 58|   1.012/ 59 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  98   |      80|      90.106|   1.015/ 46|   1.013/ 52|   1.013/ 54|   1.012/ 56 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  88   |     489|      71.619|   1.018/ 39|   1.018/ 39|   1.018/ 39|   1.018/ 39 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  92   |    2087|      71.986|   1.011/ 61|   1.010/ 72|   1.009/ 75|   1.009/ 78 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  87   |     146|      45.582|   1.016/ 42|   1.015/ 45|   1.015/ 46|   1.015/ 47 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  89   |      55|      88.721|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  95   |    1673|     196.048|   1.008/ 84|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 109   |    1245|     163.476|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  79   |      90|      50.375|   1.008/ 84|   1.007/ 95|   1.007/ 99|   1.007/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  89   |     733|     125.908|   1.011/ 61|   1.010/ 72|   1.009/ 75|   1.009/ 79 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  65   |      19|      32.865|   1.008/ 89|   1.001/ **|   1.000/ --|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  87   |     493|      15.310|   1.040/ 17|   1.040/ 17|   1.041/ 17|   1.041/ 17 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  98   |      36|      12.562|   1.007/ 97|   1.008/ 85|   1.008/ 83|   1.009/ 80 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  97   |     788|      18.331|   1.012/ 59|   1.012/ 59|   1.012/ 60|   1.012/ 60 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  80   |       6|       0.186|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 101   |     870|      19.355|   1.030/ 23|   1.030/ 23|   1.030/ 23|   1.031/ 23 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  83   |     321|     108.526|   1.049/ 14|   1.047/ 15|   1.046/ 15|   1.045/ 15 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 108   |     103|       4.023|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  97   |     687|      77.164|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  96   |     127|      12.611|   1.043/ 16|   1.044/ 16|   1.044/ 15|   1.045/ 15 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  93   |      41|      26.356|   1.067/ 10|   1.075/  9|   1.078/  9|   1.080/  9 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  91   |    1316|       7.813|   1.042/ 16|   1.040/ 17|   1.039/ 18|   1.039/ 18 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  78   |     325|      34.517|   1.019/ 36|   1.018/ 39|   1.017/ 40|   1.017/ 41 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  98   |    9802|     850.503|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  72   |       5|       0.409|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  80   |     673|      58.673|   1.042/ 16|   1.040/ 17|   1.040/ 17|   1.040/ 17 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  88   |     170|      51.484|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  78   |       1|       0.428|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  92   |   49235|     232.888|   1.026/ 27|   1.021/ 32|   1.020/ 34|   1.019/ 36 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  98   |     186|      26.694|   1.014/ 50|   1.012/ 57|   1.012/ 58|   1.011/ 60 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  91   |      53|       2.563|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  65   |       1|       0.091|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  84   |     246|       9.257|   1.007/ **|   1.002/ **|   1.001/ **|   1.000/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 100   |    8753|     230.360|   1.007/ 97|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  25   |       8|       1.433|   1.052/ 13|   1.154/  4|   1.185/  4|   1.216/  3 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  50   |      74|       4.572|   1.008/ 91|   1.007/ 97|   1.007/ **|   1.007/ ** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  87   |    3520|     184.206|   1.063/ 11|   1.064/ 11|   1.064/ 11|   1.064/ 11 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  98   |    4638|       3.308|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  87   |    1808|      36.594|   1.043/ 16|   1.044/ 16|   1.045/ 15|   1.045/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  90   |      12|       2.355|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  90   |     108|      26.589|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  91   |      85|       7.554|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  95   |     604|     103.787|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  92   |     598|      57.779|   1.013/ 52|   1.014/ 50|   1.014/ 49|   1.014/ 49 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  95   |    4096|     234.456|   1.009/ 78|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 101   |    1650|      16.458|   1.038/ 18|   1.040/ 17|   1.041/ 17|   1.041/ 17 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  78   |      78|      11.971|   1.034/ 20|   1.034/ 20|   1.034/ 20|   1.034/ 20 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  56   |      12|       8.850|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  73   |      66|       0.672|   1.140/  5|   1.159/  4|   1.163/  4|   1.168/  4 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  88   |     331|      59.952|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 123   |   30149|     449.478|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  89   |      27|      12.562|   1.013/ 53|   1.010/ 70|   1.009/ 75|   1.008/ 82 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  86   |       1|       0.426|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  74   |      14|       3.709|   1.008/ 85|   1.010/ 70|   1.010/ 67|   1.011/ 64 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 100   |    8974|     107.922|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  88   |      54|       1.795|   1.028/ 25|   1.030/ 23|   1.031/ 22|   1.031/ 22 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  98   |     188|      17.563|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  93   |     476|      28.696|   1.072/ 10|   1.071/ 10|   1.070/ 10|   1.070/ 10 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  63   |      25|       2.070|   1.011/ 64|   1.011/ 63|   1.011/ 62|   1.011/ 60 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  52   |      16|      10.054|   1.034/ 20|   1.035/ 20|   1.035/ 19|   1.036/ 19 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  73   |      79|       6.815|   1.044/ 16|   1.042/ 16|   1.041/ 17|   1.041/ 17 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  83   |     335|      36.631|   1.027/ 25|   1.026/ 26|   1.026/ 26|   1.026/ 27 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|       0.267|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  94   |     581|      59.500|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  98   |   10303|       7.569|   1.039/ 17|   1.038/ 18|   1.038/ 18|   1.038/ 18 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  98   |    2252|       8.439|   1.021/ 32|   1.021/ 33|   1.021/ 33|   1.021/ 33 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 118   |    8944|     107.274|   1.009/ 79|   1.009/ 77|   1.009/ 77|   1.009/ 77 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 105   |     538|      13.749|   1.079/  9|   1.088/  8|   1.090/  8|   1.092/  7 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  98   |    1738|     353.181|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  88   |     305|      33.173|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 117   |   35017|     581.307|   1.001/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  90   |      10|       3.727|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 125   |    1044|       8.289|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  82   |       9|       0.844|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  84   |      77|       4.126|   1.047/ 15|   1.054/ 13|   1.056/ 12|   1.058/ 12 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  83   |     108|       2.279|   1.031/ 22|   1.031/ 22|   1.031/ 22|   1.031/ 22 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  83   |      32|      17.780|   1.007/ **|   1.008/ 87|   1.008/ 83|   1.009/ 80 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  74   |     330|      74.547|   1.023/ 31|   1.015/ 45|   1.014/ 51|   1.012/ 59 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  75   |      29|       4.480|   1.032/ 21|   1.035/ 20|   1.035/ 19|   1.036/ 19 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  75   |      28|      14.752|   1.011/ 64|   1.011/ 64|   1.011/ 64|   1.011/ 64 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  99   |      31|       4.573|   1.011/ 62|   1.013/ 53|   1.013/ 51|   1.014/ 50 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  74   |      33|       7.447|   1.011/ 63|   1.010/ 70|   1.010/ 72|   1.009/ 74 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  76   |       8|       1.163|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  88   |      78|      27.931|   1.006/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  31   |      11|       0.424|   1.040/ 17|   1.005/ **|   1.000/ --|   1.000/ -- |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  92   |     120|       3.658|   1.003/ **|   1.003/ **|   1.004/ **|   1.004/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  80   |     110|       5.445|   1.019/ 36|   1.016/ 43|   1.015/ 45|   1.015/ 47 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  79   |     142|      34.839|   1.077/  9|   1.081/  8|   1.082/  8|   1.083/  8 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  90   |   19702|     155.651|   1.036/ 19|   1.032/ 22|   1.031/ 22|   1.030/ 23 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  91   |     424|     158.242|   1.022/ 31|   1.021/ 32|   1.021/ 33|   1.021/ 33 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  99   |     215|       5.994|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  23   |       2|       0.067|   1.005/ **|   1.118/  6|   1.150/  4|   1.182/  4 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  32   |      20|       0.666|   1.062/ 11|   1.045/ 15|   1.041/ 17|   1.038/ 18 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 103   |    6178|     353.905|   1.001/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  80   |      22|       4.468|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  82   |      74|      11.427|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  84   |      68|       3.046|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  86   |     453|       2.200|   1.028/ 25|   1.026/ 26|   1.026/ 27|   1.026/ 27 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  87   |     190|      91.551|   1.027/ 26|   1.029/ 24|   1.030/ 23|   1.030/ 23 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  95   |     243|      45.192|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  78   |     118|      25.305|   1.050/ 14|   1.048/ 14|   1.047/ 14|   1.047/ 15 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  90   |    2918|      13.304|   1.045/ 15|   1.046/ 15|   1.046/ 15|   1.046/ 15 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  98   |     452|     107.139|   1.018/ 39|   1.018/ 38|   1.018/ 38|   1.018/ 38 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  88   |      11|       1.563|   1.001/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  89   |    7221|     224.730|   1.029/ 24|   1.026/ 26|   1.026/ 27|   1.025/ 27 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 136   |    1155|      10.644|   1.008/ 89|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  97   |    1282|      33.408|   1.010/ 71|   1.009/ 77|   1.009/ 78|   1.009/ 80 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  92   |    1570|     152.806|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  81   |      87|      31.702|   1.049/ 14|   1.044/ 16|   1.042/ 16|   1.041/ 17 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  87   |    1439|      74.180|   1.007/ 93|   1.007/ **|   1.007/ **|   1.006/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  90   |    7821|      53.297|   1.028/ 25|   1.024/ 29|   1.023/ 30|   1.022/ 31 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  18   |       2|       0.162|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  85   |    1038|      30.332|   1.047/ 15|   1.049/ 14|   1.050/ 14|   1.050/ 14 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  77   |      64|       3.942|   1.031/ 22|   1.032/ 21|   1.032/ 21|   1.033/ 21 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  89   |     257|      36.842|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  55   |      52|       6.568|   1.007/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  88   |      26|       4.565|   1.006/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  81   |      28|       5.137|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  95   |     110|      52.720|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  70   |      92|       5.782|   1.010/ 67|   1.007/ **|   1.006/ **|   1.005/ ** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  82   |    1705|      29.013|   1.056/ 12|   1.054/ 13|   1.053/ 13|   1.053/ 13 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|       1.044|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 106   |   27203|     577.547|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  81   |      11|       0.527|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  96   |     571|      13.451|   1.036/ 19|   1.031/ 22|   1.029/ 24|   1.028/ 25 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  98   |    5116|     494.902|   1.007/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 104   |    1952|     226.929|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  80   |       7|       0.392|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  78   |      21|       0.376|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 108   |      58|       0.880|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  82   |      13|       1.765|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  84   |       8|       5.865|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  90   |      50|       4.238|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  92   |    4917|      59.125|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 109   |  121183|     367.728|   1.006/ **|   1.005/ **|   1.004/ **|   1.004/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  96   |     962|      22.968|   1.015/ 45|   1.013/ 53|   1.012/ 56|   1.012/ 59 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  89   |     300|      30.349|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  98   |   42998|     647.209|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  80   |      24|       6.767|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  82   |      20|       0.584|   1.015/ 46|   1.014/ 49|   1.014/ 50|   1.014/ 51 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  82   |      28|       0.870|   1.028/ 25|   1.031/ 23|   1.031/ 22|   1.032/ 22 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  76   |      10|       0.583|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  86   |       4|       0.264|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |

