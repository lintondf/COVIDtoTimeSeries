# State and Country COVID-19 Analysis #
## Updated: 2020-05-27 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  74   |   29989|     1541.58|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  78   |   11934|     1343.56|   1.011/ 62|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  68   |    6826|      982.24|   1.016/ 43|   1.011/ 65|   1.009/ 74|   1.008/ 86 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  69   |    5409|      541.61|   1.009/ 78|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  69   |    5556|      434.01|   1.019/ 36|   1.011/ 61|   1.009/ 73|   1.008/ 91 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  71   |    5279|      416.61|   1.023/ 30|   1.017/ 40|   1.016/ 43|   1.015/ 47 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  84   |    4074|      103.11|   1.020/ 34|   1.016/ 42|   1.015/ 45|   1.014/ 48 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  69   |    3918|     1099.00|   1.014/ 48|   1.010/ 66|   1.009/ 73|   1.008/ 82 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  74   |    2805|      603.48|   1.010/ 69|   1.007/ 94|   1.007/ **|   1.006/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  69   |    2465|      407.69|   1.021/ 33|   1.015/ 45|   1.014/ 49|   1.013/ 55 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  88   |  105536|      320.25|   1.013/ 55|   1.009/ 79|   1.008/ 89|   1.007/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  77   |   38908|      585.65|   1.009/ 78|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  96   |   34027|      564.88|   1.004/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 102   |   29996|      447.19|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  85   |   28866|      612.86|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  71   |   26053|      123.23|   1.050/ 14|   1.045/ 15|   1.043/ 16|   1.042/ 16 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  77   |    9598|      832.85|   1.005/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  79   |    8615|      103.60|   1.005/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  69   |    8513|       67.25|   1.053/ 13|   1.048/ 14|   1.047/ 15|   1.046/ 15 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  97   |    7626|       91.46|   1.007/ 94|   1.006/ **|   1.006/ **|   1.006/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  63   |     603|      122.97|   1.022/ 31|   1.016/ 45|   1.014/ 50|   1.012/ 56 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  63   |      10|       13.82|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  67   |     896|      123.05|   1.027/ 26|   1.018/ 37|   1.016/ 42|   1.014/ 49 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  64   |     120|       39.77|   1.017/ 40|   1.015/ 47|   1.014/ 48|   1.014/ 49 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  84   |    4074|      103.11|   1.020/ 34|   1.016/ 42|   1.015/ 45|   1.014/ 48 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  74   |    1431|      248.57|   1.018/ 38|   1.015/ 47|   1.014/ 49|   1.013/ 53 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  69   |    3918|     1099.00|   1.014/ 48|   1.010/ 66|   1.009/ 73|   1.008/ 82 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  62   |     359|      368.43|   1.024/ 29|   1.017/ 41|   1.015/ 46|   1.013/ 52 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  80   |    2417|      112.54|   1.017/ 40|   1.013/ 52|   1.012/ 57|   1.011/ 62 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  76   |    1941|      182.78|   1.017/ 41|   1.014/ 49|   1.013/ 51|   1.013/ 54 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  57   |      17|       12.01|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  62   |      81|       45.09|   1.009/ 74|   1.009/ 80|   1.008/ 82|   1.008/ 84 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  71   |    5279|      416.61|   1.023/ 30|   1.017/ 40|   1.016/ 43|   1.015/ 47 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  72   |    2146|      318.79|   1.018/ 39|   1.011/ 62|   1.010/ 72|   1.008/ 86 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  63   |     496|      157.15|   1.037/ 18|   1.032/ 21|   1.031/ 22|   1.030/ 23 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  75   |     221|       75.73|   1.010/ 69|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  72   |     412|       92.26|   1.016/ 44|   1.013/ 55|   1.012/ 59|   1.011/ 63 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  74   |    2805|      603.48|   1.010/ 69|   1.007/ 94|   1.007/ **|   1.006/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  61   |      79|       59.05|   1.013/ 52|   1.013/ 55|   1.012/ 56|   1.012/ 57 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  69   |    2465|      407.69|   1.021/ 33|   1.015/ 45|   1.014/ 49|   1.013/ 55 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  68   |    6826|      982.24|   1.016/ 43|   1.011/ 65|   1.009/ 74|   1.008/ 86 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  69   |    5409|      541.61|   1.009/ 78|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  67   |     962|      170.64|   1.029/ 24|   1.022/ 32|   1.020/ 34|   1.019/ 37 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  69   |     682|      229.10|   1.026/ 26|   1.022/ 32|   1.021/ 33|   1.020/ 35 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  69   |     746|      121.52|   1.020/ 34|   1.015/ 47|   1.013/ 52|   1.012/ 58 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  61   |      16|       15.12|   1.002/ **|   1.002/ **|   1.003/ **|   1.003/ ** |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  60   |     158|       81.93|   1.029/ 24|   1.024/ 29|   1.023/ 30|   1.022/ 32 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  72   |     413|      134.01|   1.014/ 49|   1.010/ 68|   1.009/ 75|   1.008/ 85 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  65   |     234|      171.90|   1.032/ 22|   1.023/ 30|   1.021/ 33|   1.019/ 37 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  78   |   11934|     1343.56|   1.011/ 62|   1.006/ **|   1.005/ **|   1.004/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  63   |     345|      164.65|   1.030/ 23|   1.023/ 30|   1.021/ 33|   1.019/ 36 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  74   |   29989|     1541.58|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  63   |     838|       79.87|   1.022/ 32|   1.017/ 42|   1.015/ 45|   1.014/ 49 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  61   |      57|       75.41|   1.028/ 25|   1.021/ 33|   1.019/ 37|   1.017/ 40 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  68   |    2098|      179.49|   1.025/ 28|   1.021/ 33|   1.020/ 34|   1.019/ 36 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  69   |     322|       81.32|   1.010/ 70|   1.007/ 94|   1.007/ **|   1.006/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  73   |     155|       36.74|   1.010/ 71|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  69   |    5556|      434.01|   1.019/ 36|   1.011/ 61|   1.009/ 73|   1.008/ 91 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  67   |     134|       41.96|   1.009/ 75|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  60   |     639|      603.51|   1.026/ 27|   1.023/ 30|   1.022/ 31|   1.022/ 32 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  72   |     466|       90.54|   1.017/ 40|   1.013/ 52|   1.012/ 56|   1.011/ 61 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  77   |      61|       68.71|   1.022/ 32|   1.014/ 50|   1.012/ 59|   1.010/ 72 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  67   |     350|       51.21|   1.019/ 36|   1.017/ 40|   1.017/ 41|   1.017/ 42 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  71   |    1639|       56.51|   1.022/ 32|   1.017/ 40|   1.016/ 42|   1.015/ 45 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  66   |     105|       32.71|   1.026/ 27|   1.022/ 32|   1.021/ 33|   1.020/ 35 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  68   |      55|       87.45|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  74   |    1289|      151.05|   1.023/ 29|   1.018/ 38|   1.017/ 41|   1.016/ 44 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  88   |    1113|      146.18|   1.009/ 79|   1.007/ **|   1.006/ **|   1.006/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  58   |      77|       42.70|   1.017/ 42|   1.011/ 60|   1.010/ 69|   1.009/ 81 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  68   |     534|       91.77|   1.016/ 42|   1.014/ 50|   1.013/ 53|   1.012/ 56 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  44   |      14|       23.39|   1.018/ 39|   1.023/ 30|   1.024/ 29|   1.025/ 27 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  66   |     242|        7.50|   1.039/ 18|   1.033/ 21|   1.031/ 22|   1.030/ 23 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  77   |      32|       11.16|   1.003/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  76   |     613|       14.27|   1.013/ 53|   1.013/ 52|   1.014/ 51|   1.014/ 51 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  59   |       2|        0.06|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  80   |     488|       10.85|   1.028/ 25|   1.027/ 26|   1.026/ 26|   1.026/ 27 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  62   |      86|       29.24|   1.046/ 15|   1.052/ 13|   1.054/ 13|   1.055/ 12 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  87   |     105|        4.08|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  76   |     649|       72.87|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  75   |      52|        5.14|   1.034/ 20|   1.035/ 19|   1.036/ 19|   1.036/ 19 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  72   |      14|        9.14|   1.029/ 24|   1.033/ 21|   1.034/ 20|   1.035/ 20 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  70   |     515|        3.06|   1.054/ 13|   1.058/ 12|   1.058/ 12|   1.059/ 12 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  57   |     214|       22.75|   1.029/ 24|   1.025/ 28|   1.024/ 29|   1.023/ 30 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  77   |    9598|      832.85|   1.005/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  51   |       2|        0.17|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  59   |     279|       24.34|   1.055/ 13|   1.051/ 13|   1.051/ 14|   1.050/ 14 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  67   |     160|       48.59|   1.020/ 34|   1.012/ 56|   1.010/ 67|   1.008/ 84 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  57   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  71   |   26053|      123.23|   1.050/ 14|   1.045/ 15|   1.043/ 16|   1.042/ 16 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  77   |     136|       19.62|   1.024/ 29|   1.021/ 33|   1.020/ 34|   1.020/ 35 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  70   |      53|        2.56|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  44   |       1|        0.09|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  63   |     181|        6.80|   1.024/ 29|   1.023/ 29|   1.023/ 30|   1.023/ 30 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  79   |    7282|      191.63|   1.018/ 38|   1.011/ 63|   1.009/ 74|   1.008/ 91 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  29   |      63|        3.85|   1.030/ 23|   1.015/ 46|   1.011/ 61|   1.008/ 89 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  66   |     754|       39.44|   1.062/ 11|   1.071/ 10|   1.073/  9|   1.075/  9 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  77   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  66   |     784|       15.87|   1.033/ 21|   1.031/ 22|   1.031/ 23|   1.030/ 23 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  69   |      11|        2.21|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  69   |     103|       25.36|   1.007/ **|   1.002/ **|   1.001/ **|   1.000/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  70   |      85|        7.54|   1.005/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  74   |     580|       99.56|   1.004/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  71   |     484|       46.74|   1.011/ 66|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  74   |    3724|      213.21|   1.028/ 25|   1.019/ 37|   1.016/ 42|   1.014/ 49 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  80   |     807|        8.04|   1.027/ 26|   1.026/ 27|   1.025/ 27|   1.025/ 27 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  57   |      40|        6.13|   1.042/ 16|   1.031/ 22|   1.028/ 24|   1.025/ 28 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  35   |      13|        9.27|   1.070/ 10|   1.065/ 10|   1.065/ 10|   1.065/ 11 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  52   |       5|        0.05|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  67   |     323|       58.37|   1.008/ 86|   1.003/ **|   1.002/ **|   1.001/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 102   |   29996|      447.19|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  68   |      15|        6.81|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  65   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  53   |      13|        3.37|   1.007/ 92|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  79   |    8615|      103.60|   1.005/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  67   |      36|        1.17|   1.026/ 27|   1.022/ 32|   1.020/ 34|   1.019/ 36 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  77   |     175|       16.29|   1.008/ 89|   1.007/ 95|   1.007/ 97|   1.007/ 99 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  72   |      61|        3.66|   1.054/ 13|   1.058/ 12|   1.059/ 12|   1.060/ 11 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  42   |      21|        1.75|   1.035/ 20|   1.022/ 31|   1.018/ 37|   1.015/ 46 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  31   |       7|        4.54|   1.086/  8|   1.046/ 15|   1.033/ 21|   1.020/ 34 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  52   |      30|        2.58|   1.045/ 15|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  62   |     189|       20.63|   1.034/ 20|   1.032/ 22|   1.031/ 22|   1.031/ 22 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  73   |     517|       52.94|   1.012/ 59|   1.007/ 94|   1.006/ **|   1.005/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  77   |    4631|        3.40|   1.043/ 16|   1.038/ 18|   1.036/ 19|   1.035/ 20 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  77   |    1419|        5.32|   1.024/ 29|   1.025/ 28|   1.025/ 28|   1.025/ 28 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  97   |    7626|       91.46|   1.007/ 94|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  84   |     155|        3.97|   1.030/ 23|   1.034/ 20|   1.035/ 20|   1.036/ 19 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  77   |    1675|      340.35|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  67   |     290|       31.56|   1.006/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  96   |   34027|      564.88|   1.004/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  69   |       9|        3.35|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 104   |     984|        7.81|   1.016/ 43|   1.009/ 75|   1.008/ 91|   1.006/ ** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  61   |       9|        0.85|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  63   |      37|        1.97|   1.008/ 88|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  62   |      60|        1.25|   1.025/ 28|   1.011/ 66|   1.007/ **|   1.003/ ** |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  62   |      30|       16.85|   1.003/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  53   |     184|       41.65|   1.066/ 10|   1.052/ 13|   1.049/ 14|   1.045/ 15 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  54   |      15|        2.36|   1.016/ 42|   1.017/ 41|   1.017/ 40|   1.017/ 40 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  54   |      23|       11.84|   1.013/ 53|   1.012/ 56|   1.012/ 57|   1.012/ 58 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  78   |      26|        3.88|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  53   |      26|        5.80|   1.021/ 33|   1.027/ 25|   1.029/ 24|   1.031/ 23 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  55   |       3|        0.44|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  67   |      65|       23.35|   1.015/ 45|   1.016/ 45|   1.015/ 45|   1.015/ 45 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  10   |       2|        0.08|   1.260/  2|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  71   |     117|        3.57|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  59   |      71|        3.51|   1.039/ 18|   1.036/ 19|   1.036/ 19|   1.035/ 20 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  58   |      10|        2.41|   1.169/  4|   1.140/  5|   1.133/  5|   1.125/  5 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  69   |    8513|       67.25|   1.053/ 13|   1.048/ 14|   1.047/ 15|   1.046/ 15 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  70   |     275|      102.42|   1.029/ 24|   1.026/ 26|   1.025/ 27|   1.024/ 28 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  78   |     203|        5.66|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  11   |       4|        0.14|   1.205/  3|   1.123/  5|   1.101/  7|   1.101/  7 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  82   |    6071|      347.78|   1.004/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  59   |      21|        4.23|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  61   |      21|        3.28|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  63   |      65|        2.93|   1.020/ 34|   1.016/ 42|   1.015/ 45|   1.014/ 49 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  65   |     261|        1.26|   1.036/ 19|   1.024/ 29|   1.021/ 33|   1.018/ 37 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  66   |     117|       56.36|   1.014/ 49|   1.013/ 52|   1.013/ 53|   1.013/ 54 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  74   |     240|       44.76|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  57   |      40|        8.50|   1.059/ 12|   1.062/ 11|   1.062/ 11|   1.063/ 11 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  69   |    1256|        5.73|   1.037/ 18|   1.032/ 22|   1.030/ 23|   1.029/ 24 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  77   |     324|       76.88|   1.017/ 42|   1.014/ 51|   1.013/ 54|   1.012/ 57 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  67   |      11|        1.58|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  68   |    3956|      123.11|   1.043/ 16|   1.038/ 18|   1.036/ 19|   1.035/ 20 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 115   |     994|        9.16|   1.011/ 61|   1.008/ 91|   1.007/ **|   1.006/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  76   |    1071|       27.91|   1.014/ 51|   1.010/ 72|   1.009/ 81|   1.008/ 91 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  71   |    1348|      131.20|   1.010/ 67|   1.009/ 74|   1.009/ 75|   1.009/ 77 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  60   |      22|        7.88|   1.057/ 12|   1.077/  9|   1.082/  8|   1.087/  8 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  66   |    1267|       65.31|   1.014/ 50|   1.009/ 77|   1.008/ 89|   1.007/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  69   |    3940|       26.85|   1.043/ 16|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  64   |     419|       12.24|   1.033/ 21|   1.031/ 23|   1.030/ 23|   1.029/ 23 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  56   |      40|        2.47|   1.046/ 15|   1.031/ 22|   1.027/ 25|   1.023/ 30 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  68   |     248|       35.66|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  34   |      44|        5.56|   1.050/ 14|   1.037/ 18|   1.035/ 20|   1.033/ 21 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  67   |      24|        4.19|   1.007/ 94|   1.002/ **|   1.001/ **|   1.000/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  60   |      29|        5.26|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  74   |     109|       52.12|   1.004/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  49   |      66|        4.16|   1.019/ 36|   1.015/ 47|   1.014/ 50|   1.013/ 53 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  61   |     488|        8.31|   1.065/ 10|   1.070/ 10|   1.071/ 10|   1.073/  9 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  85   |   28866|      612.86|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  60   |       9|        0.43|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  75   |     180|        4.24|   1.061/ 11|   1.054/ 13|   1.053/ 13|   1.051/ 13 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  77   |    4271|      413.11|   1.014/ 49|   1.011/ 65|   1.010/ 70|   1.009/ 77 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  83   |    1951|      226.72|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  59   |       3|        0.17|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  57   |      22|        0.39|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  87   |      57|        0.86|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  61   |      13|        1.72|   1.013/ 53|   1.013/ 53|   1.013/ 53|   1.013/ 53 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  63   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  69   |      48|        4.12|   1.005/ **|   1.004/ **|   1.004/ **|   1.004/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  71   |    4516|       54.31|   1.009/ 81|   1.006/ **|   1.005/ **|   1.004/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  88   |  105536|      320.25|   1.013/ 55|   1.009/ 79|   1.008/ 89|   1.007/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  75   |     687|       16.39|   1.030/ 23|   1.026/ 26|   1.025/ 28|   1.024/ 29 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  68   |     274|       27.67|   1.018/ 39|   1.007/ **|   1.004/ **|   1.001/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  77   |   38908|      585.65|   1.009/ 78|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  59   |      22|        6.23|   1.013/ 52|   1.015/ 47|   1.015/ 46|   1.016/ 45 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  61   |      14|        0.41|   1.015/ 45|   1.015/ 47|   1.014/ 48|   1.014/ 49 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  61   |      10|        0.31|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  55   |       8|        0.42|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  65   |       4|        0.26|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |

