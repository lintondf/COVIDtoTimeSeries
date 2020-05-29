# State and Country COVID-19 Analysis #
## Updated: 2020-05-29 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  76   |   30164|     1550.57|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  80   |   12058|     1357.53|   1.010/ 71|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  70   |    6946|      999.57|   1.014/ 48|   1.009/ 74|   1.008/ 85|   1.007/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  71   |    5666|      442.57|   1.017/ 42|   1.010/ 72|   1.008/ 87|   1.006/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  71   |    5475|      548.26|   1.008/ 83|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  73   |    5446|      429.76|   1.021/ 33|   1.016/ 43|   1.015/ 47|   1.013/ 52 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  86   |    4200|      106.30|   1.019/ 37|   1.015/ 45|   1.014/ 48|   1.014/ 51 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  71   |    3984|     1117.35|   1.013/ 54|   1.009/ 77|   1.008/ 86|   1.007/ 97 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  76   |    2837|      610.36|   1.009/ 79|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  71   |    2537|      419.62|   1.020/ 35|   1.015/ 48|   1.013/ 52|   1.012/ 58 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  90   |  107344|      325.74|   1.012/ 59|   1.008/ 85|   1.007/ 95|   1.006/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  79   |   39210|      590.19|   1.008/ 84|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  98   |   34179|      567.40|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 104   |   30026|      447.65|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  87   |   28630|      607.86|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  73   |   28277|      133.75|   1.048/ 14|   1.043/ 16|   1.041/ 17|   1.040/ 17 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  79   |    9630|      835.58|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  71   |    9350|       73.86|   1.053/ 13|   1.049/ 14|   1.048/ 14|   1.047/ 15 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  81   |    8669|      104.25|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  99   |    7727|       92.68|   1.007/ 96|   1.006/ **|   1.006/ **|   1.006/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  65   |     618|      126.10|   1.020/ 35|   1.014/ 49|   1.013/ 54|   1.011/ 61 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  65   |      10|       13.77|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  69   |     921|      126.52|   1.024/ 29|   1.016/ 44|   1.013/ 51|   1.011/ 61 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  66   |     124|       41.05|   1.017/ 40|   1.016/ 44|   1.016/ 44|   1.015/ 45 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  86   |    4200|      106.30|   1.019/ 37|   1.015/ 45|   1.014/ 48|   1.014/ 51 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  76   |    1473|      255.70|   1.018/ 39|   1.015/ 47|   1.014/ 49|   1.013/ 52 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  71   |    3984|     1117.35|   1.013/ 54|   1.009/ 77|   1.008/ 86|   1.007/ 97 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  64   |     368|      377.93|   1.021/ 33|   1.014/ 48|   1.013/ 54|   1.011/ 63 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  82   |    2478|      115.39|   1.016/ 43|   1.012/ 56|   1.011/ 61|   1.010/ 66 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  78   |    2001|      188.49|   1.017/ 40|   1.015/ 46|   1.015/ 47|   1.014/ 48 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  59   |      17|       12.01|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  64   |      82|       45.96|   1.010/ 73|   1.009/ 77|   1.009/ 78|   1.009/ 80 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  73   |    5446|      429.76|   1.021/ 33|   1.016/ 43|   1.015/ 47|   1.013/ 52 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  74   |    2187|      324.84|   1.015/ 45|   1.010/ 71|   1.008/ 83|   1.007/ 99 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  65   |     526|      166.77|   1.036/ 19|   1.031/ 22|   1.030/ 23|   1.029/ 24 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  77   |     223|       76.58|   1.009/ 73|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  74   |     422|       94.38|   1.014/ 48|   1.011/ 60|   1.011/ 64|   1.010/ 69 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  76   |    2837|      610.36|   1.009/ 79|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  63   |      82|       60.99|   1.014/ 49|   1.014/ 48|   1.015/ 48|   1.015/ 47 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  71   |    2537|      419.62|   1.020/ 35|   1.015/ 48|   1.013/ 52|   1.012/ 58 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  70   |    6946|      999.57|   1.014/ 48|   1.009/ 74|   1.008/ 85|   1.007/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  71   |    5475|      548.26|   1.008/ 83|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  69   |    1006|      178.42|   1.027/ 25|   1.022/ 31|   1.021/ 33|   1.019/ 36 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  71   |     712|      239.10|   1.026/ 27|   1.022/ 31|   1.021/ 33|   1.020/ 34 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  71   |     759|      123.60|   1.017/ 41|   1.011/ 66|   1.009/ 78|   1.007/ 94 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  63   |      16|       15.41|   1.005/ **|   1.008/ 83|   1.009/ 76|   1.010/ 70 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  62   |     166|       85.68|   1.027/ 25|   1.023/ 30|   1.022/ 32|   1.020/ 34 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  74   |     421|      136.71|   1.014/ 51|   1.010/ 68|   1.009/ 74|   1.009/ 81 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  67   |     244|      179.37|   1.030/ 23|   1.022/ 31|   1.020/ 34|   1.019/ 37 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  80   |   12058|     1357.53|   1.010/ 71|   1.005/ **|   1.004/ **|   1.003/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  65   |     357|      170.20|   1.026/ 27|   1.019/ 37|   1.017/ 41|   1.015/ 46 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  76   |   30164|     1550.57|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  65   |     874|       83.34|   1.022/ 31|   1.019/ 36|   1.018/ 37|   1.018/ 39 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  63   |      60|       78.15|   1.025/ 28|   1.019/ 37|   1.017/ 41|   1.015/ 45 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  70   |    2175|      186.10|   1.023/ 30|   1.019/ 36|   1.018/ 38|   1.017/ 41 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  71   |     327|       82.75|   1.010/ 69|   1.008/ 84|   1.008/ 88|   1.007/ 93 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  75   |     156|       37.04|   1.008/ 87|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  71   |    5666|      442.57|   1.017/ 42|   1.010/ 72|   1.008/ 87|   1.006/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  69   |     135|       42.25|   1.008/ 88|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  62   |     673|      635.25|   1.026/ 26|   1.025/ 27|   1.025/ 28|   1.025/ 28 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  74   |     480|       93.18|   1.018/ 39|   1.015/ 46|   1.014/ 48|   1.014/ 51 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  79   |      62|       69.85|   1.021/ 32|   1.015/ 47|   1.013/ 53|   1.011/ 61 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  69   |     362|       52.96|   1.018/ 37|   1.017/ 41|   1.016/ 42|   1.016/ 43 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  73   |    1687|       58.19|   1.020/ 35|   1.015/ 45|   1.014/ 48|   1.013/ 52 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  68   |     110|       34.16|   1.025/ 27|   1.022/ 31|   1.021/ 33|   1.020/ 34 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  70   |      55|       87.60|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  76   |    1347|      157.87|   1.024/ 28|   1.021/ 34|   1.020/ 35|   1.019/ 37 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  90   |    1130|      148.38|   1.009/ 79|   1.007/ 97|   1.007/ **|   1.006/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  60   |      78|       43.35|   1.014/ 48|   1.009/ 77|   1.007/ 93|   1.006/ ** |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  70   |     552|       94.79|   1.017/ 41|   1.015/ 46|   1.015/ 47|   1.014/ 49 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  46   |      15|       25.77|   1.032/ 21|   1.044/ 16|   1.047/ 15|   1.050/ 14 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  68   |     254|        7.88|   1.034/ 20|   1.027/ 25|   1.025/ 27|   1.024/ 29 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  79   |      32|       11.30|   1.004/ **|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  78   |     629|       14.64|   1.013/ 53|   1.013/ 52|   1.013/ 52|   1.013/ 52 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  61   |       2|        0.06|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  82   |     515|       11.45|   1.029/ 24|   1.027/ 25|   1.027/ 25|   1.027/ 26 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  64   |      97|       32.81|   1.053/ 13|   1.061/ 11|   1.063/ 11|   1.065/ 10 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  89   |     105|        4.08|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  78   |     654|       73.41|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  77   |      55|        5.50|   1.034/ 20|   1.035/ 20|   1.035/ 20|   1.035/ 19 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  74   |      15|        9.75|   1.028/ 24|   1.031/ 22|   1.032/ 22|   1.032/ 21 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  72   |     569|        3.38|   1.052/ 13|   1.054/ 13|   1.054/ 13|   1.054/ 13 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  59   |     224|       23.81|   1.027/ 25|   1.024/ 29|   1.023/ 30|   1.022/ 32 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  79   |    9630|      835.58|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  53   |       3|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  61   |     305|       26.55|   1.051/ 13|   1.047/ 15|   1.046/ 15|   1.045/ 15 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  69   |     163|       49.46|   1.018/ 38|   1.011/ 64|   1.009/ 78|   1.007/ 98 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  59   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  73   |   28277|      133.75|   1.048/ 14|   1.043/ 16|   1.041/ 17|   1.040/ 17 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  79   |     141|       20.30|   1.021/ 34|   1.017/ 40|   1.017/ 41|   1.016/ 44 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  72   |      54|        2.57|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  46   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  65   |     185|        6.97|   1.023/ 30|   1.022/ 32|   1.022/ 32|   1.021/ 32 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  81   |    7444|      195.91|   1.017/ 41|   1.011/ 65|   1.009/ 75|   1.008/ 90 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  31   |      65|        3.99|   1.023/ 30|   1.017/ 42|   1.015/ 45|   1.014/ 48 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  68   |     861|       45.04|   1.063/ 11|   1.069/ 10|   1.071/ 10|   1.072/  9 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  79   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  68   |     835|       16.91|   1.033/ 21|   1.032/ 22|   1.031/ 22|   1.031/ 22 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  71   |      11|        2.23|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  71   |     104|       25.51|   1.006/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  72   |      85|        7.54|   1.004/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  76   |     581|       99.77|   1.003/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  73   |     492|       47.50|   1.011/ 65|   1.008/ 91|   1.007/ **|   1.006/ ** |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  76   |    3794|      217.18|   1.024/ 29|   1.016/ 43|   1.014/ 50|   1.012/ 58 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  82   |     848|        8.46|   1.026/ 26|   1.025/ 27|   1.025/ 28|   1.025/ 28 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  59   |      42|        6.48|   1.039/ 17|   1.030/ 23|   1.027/ 26|   1.024/ 28 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  37   |      13|        9.78|   1.058/ 12|   1.045/ 15|   1.041/ 17|   1.036/ 19 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  54   |       6|        0.06|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  69   |     324|       58.66|   1.007/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 104   |   30026|      447.65|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  70   |      15|        7.01|   1.025/ 28|   1.018/ 37|   1.017/ 41|   1.015/ 45 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  67   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  55   |      12|        3.33|   1.005/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  81   |    8669|      104.25|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  69   |      37|        1.21|   1.024/ 29|   1.020/ 35|   1.018/ 37|   1.017/ 40 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  79   |     177|       16.49|   1.007/ 96|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  74   |      70|        4.23|   1.062/ 11|   1.067/ 10|   1.069/ 10|   1.070/ 10 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  44   |      22|        1.80|   1.029/ 23|   1.017/ 40|   1.014/ 49|   1.011/ 62 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  33   |       8|        4.86|   1.073/  9|   1.040/ 17|   1.031/ 22|   1.024/ 29 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  54   |      33|        2.88|   1.052/ 13|   1.056/ 12|   1.057/ 12|   1.059/ 12 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  64   |     200|       21.86|   1.032/ 22|   1.030/ 23|   1.029/ 23|   1.029/ 24 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  75   |     525|       53.76|   1.011/ 62|   1.008/ 91|   1.007/ **|   1.006/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  79   |    4977|        3.66|   1.042/ 16|   1.037/ 19|   1.035/ 19|   1.034/ 20 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  79   |    1492|        5.59|   1.024/ 29|   1.025/ 28|   1.025/ 28|   1.025/ 27 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  99   |    7727|       92.68|   1.007/ 96|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  86   |     167|        4.27|   1.031/ 22|   1.035/ 20|   1.036/ 19|   1.037/ 19 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  79   |    1684|      342.08|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  69   |     291|       31.66|   1.005/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  98   |   34179|      567.40|   1.004/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  71   |       9|        3.33|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 106   |    1002|        7.96|   1.015/ 46|   1.009/ 77|   1.008/ 92|   1.006/ ** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  63   |       9|        0.84|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  65   |      37|        2.00|   1.009/ 74|   1.008/ 92|   1.007/ 97|   1.007/ ** |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  64   |      61|        1.28|   1.024/ 29|   1.012/ 57|   1.009/ 77|   1.006/ ** |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  64   |      30|       16.87|   1.004/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  55   |     199|       44.93|   1.059/ 12|   1.044/ 16|   1.040/ 17|   1.036/ 19 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  56   |      16|        2.44|   1.018/ 38|   1.019/ 35|   1.020/ 35|   1.020/ 34 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  56   |      23|       12.29|   1.015/ 47|   1.016/ 44|   1.016/ 44|   1.016/ 44 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  80   |      26|        3.87|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  55   |      27|        6.08|   1.020/ 35|   1.024/ 29|   1.024/ 28|   1.025/ 27 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  57   |       3|        0.44|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  69   |      67|       24.14|   1.016/ 42|   1.017/ 41|   1.017/ 41|   1.017/ 41 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  12   |       2|        0.08|   1.145/  5|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  73   |     117|        3.57|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  61   |      75|        3.71|   1.036/ 19|   1.032/ 21|   1.031/ 22|   1.030/ 23 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  60   |      15|        3.60|   1.202/  3|   1.202/  3|   1.203/  3|   1.205/  3 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  71   |    9350|       73.86|   1.053/ 13|   1.049/ 14|   1.048/ 14|   1.047/ 15 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  72   |     289|      107.70|   1.029/ 24|   1.026/ 27|   1.025/ 27|   1.024/ 28 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  80   |     204|        5.70|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  13   |       5|        0.16|   1.145/  5|   1.101/  7|   1.088/  8|   1.078/  9 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  84   |    6089|      348.77|   1.004/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  61   |      21|        4.29|   1.002/ **|   1.003/ **|   1.004/ **|   1.004/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  63   |      31|        4.72|   1.159/  4|   1.198/  3|   1.208/  3|   1.218/  3 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  65   |      67|        3.00|   1.018/ 38|   1.014/ 51|   1.012/ 56|   1.011/ 61 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  67   |     274|        1.33|   1.034/ 20|   1.026/ 27|   1.024/ 29|   1.022/ 31 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  68   |     121|       58.15|   1.015/ 45|   1.015/ 45|   1.015/ 45|   1.015/ 45 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  76   |     241|       44.82|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  59   |      43|        9.25|   1.052/ 13|   1.049/ 14|   1.048/ 14|   1.047/ 15 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  71   |    1328|        6.06|   1.035/ 20|   1.029/ 24|   1.028/ 25|   1.027/ 26 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  79   |     332|       78.67|   1.015/ 46|   1.012/ 58|   1.011/ 62|   1.010/ 66 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  69   |      11|        1.58|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  70   |    4261|      132.63|   1.043/ 16|   1.038/ 18|   1.037/ 18|   1.036/ 19 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 117   |    1010|        9.31|   1.011/ 62|   1.008/ 89|   1.007/ **|   1.006/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  78   |    1088|       28.36|   1.013/ 55|   1.009/ 78|   1.008/ 87|   1.007/ 98 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  73   |    1375|      133.75|   1.010/ 68|   1.009/ 73|   1.009/ 74|   1.009/ 75 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  62   |      26|        9.62|   1.066/ 10|   1.086/  8|   1.091/  7|   1.096/  7 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  68   |    1285|       66.24|   1.012/ 56|   1.008/ 86|   1.007/ **|   1.006/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  71   |    4251|       28.97|   1.042/ 16|   1.038/ 18|   1.037/ 18|   1.036/ 19 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  66   |     445|       13.00|   1.032/ 21|   1.030/ 23|   1.030/ 23|   1.029/ 23 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  58   |      42|        2.60|   1.041/ 17|   1.028/ 25|   1.024/ 28|   1.021/ 33 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  70   |     248|       35.67|   1.005/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  36   |      47|        5.89|   1.043/ 16|   1.035/ 20|   1.033/ 21|   1.032/ 22 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  69   |      24|        4.20|   1.005/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  62   |      29|        5.24|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  76   |     110|       52.30|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  51   |      69|        4.35|   1.021/ 33|   1.021/ 34|   1.021/ 33|   1.021/ 33 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  63   |     563|        9.57|   1.068/ 10|   1.073/  9|   1.074/  9|   1.076/  9 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  87   |   28630|      607.86|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  62   |      10|        0.44|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  77   |     202|        4.76|   1.058/ 12|   1.052/ 13|   1.051/ 14|   1.049/ 14 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  79   |    4376|      423.26|   1.014/ 48|   1.012/ 59|   1.011/ 62|   1.010/ 66 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  85   |    1952|      226.85|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  61   |       4|        0.24|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  59   |      21|        0.38|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  89   |      57|        0.86|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  63   |      13|        1.75|   1.013/ 52|   1.013/ 54|   1.013/ 54|   1.013/ 54 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  65   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  71   |      49|        4.15|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  73   |    4564|       54.88|   1.008/ 88|   1.005/ **|   1.005/ **|   1.004/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  90   |  107344|      325.74|   1.012/ 59|   1.008/ 85|   1.007/ 95|   1.006/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  77   |     718|       17.14|   1.028/ 24|   1.024/ 29|   1.023/ 31|   1.021/ 32 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  70   |     277|       28.00|   1.015/ 45|   1.006/ **|   1.004/ **|   1.002/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  79   |   39210|      590.19|   1.008/ 84|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  61   |      22|        6.34|   1.011/ 65|   1.010/ 68|   1.010/ 68|   1.010/ 69 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  63   |      14|        0.42|   1.017/ 40|   1.018/ 39|   1.018/ 39|   1.018/ 39 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  63   |      10|        0.32|   1.008/ 90|   1.012/ 58|   1.013/ 53|   1.014/ 48 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  57   |       7|        0.41|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  67   |       4|        0.26|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |

