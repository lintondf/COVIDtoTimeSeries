# State and Country COVID-19 Analysis #
## Updated: 2020-05-23 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# Notes #

- Expect discontinuities in the US around 4/14/2020 as the [CDC](CDC "https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html")  expanded the definition of a COVID-19 death.  
- There is also some weekly pattern to reporting with lower values on the weekend followed by higher values subsequently, at least in some places.
- The Y axis upper limit for DDGR charts was lowered from 2.0 to 1.5 on 4/28 to better show current lower values.  

# Ten US States with Highest Death Tolls #

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. One per million is 0.0001%.  1% is 10,000 per million.

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDeathRates.png)

Daily Death Growth Rate (DDGR) in the 10 US States with the highest death tolls.

DDGR is the cube root of Arnold Kling's [Three Day Death Reproduction Rate (3DDRR)](http://www.arnoldkling.com/blog/the-3ddrr/).  The 3DDRR is calculated by dividing the cumulative total number of deaths on a given day by the  cumulative total number of deaths three days previously.  Taking the cube root converts this to the geometric mean for the three days.  These values are LOWESS filtered to generate a local-error minimizing non-parametric trend.

If deaths remain constant over the three days, the DDGR equals one.  A value of 2 would indicate that the number of deaths doubles every day.

![US States with Highest Death Toll - Daily Death Growth Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  70   |   29570|     1520.01|   1.007/ 99|   1.005/ **|   1.004/ **|   1.003/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  74   |   11615|     1307.66|   1.016/ 45|   1.010/ 69|   1.009/ 79|   1.007/ 93 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  64   |    6543|      941.44|   1.021/ 33|   1.015/ 46|   1.013/ 51|   1.012/ 58 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  65   |    5270|      527.66|   1.011/ 61|   1.008/ 87|   1.007/ 97|   1.006/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  65   |    5287|      412.97|   1.026/ 27|   1.017/ 41|   1.015/ 47|   1.013/ 55 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  67   |    4921|      388.35|   1.029/ 24|   1.024/ 28|   1.023/ 30|   1.022/ 31 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  80   |    3804|       96.28|   1.024/ 28|   1.021/ 33|   1.020/ 35|   1.019/ 36 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  65   |    3757|     1053.68|   1.018/ 38|   1.014/ 51|   1.013/ 55|   1.011/ 60 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  70   |    2722|      585.44|   1.013/ 52|   1.011/ 65|   1.010/ 69|   1.009/ 73 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  65   |    2316|      383.09|   1.026/ 26|   1.020/ 34|   1.018/ 37|   1.017/ 41 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  84   |  101656|      308.47|   1.016/ 44|   1.011/ 62|   1.010/ 69|   1.009/ 77 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  73   |   38292|      576.37|   1.011/ 60|   1.008/ 84|   1.008/ 92|   1.007/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  92   |   33651|      558.62|   1.005/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  81   |   28861|      612.76|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  98   |   29923|      446.11|   1.004/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  67   |   21804|      103.13|   1.056/ 12|   1.051/ 13|   1.050/ 14|   1.049/ 14 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  73   |    9521|      826.15|   1.006/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  75   |    8515|      102.40|   1.007/ 94|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  93   |    7425|       89.05|   1.008/ 88|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  65   |    7035|       55.58|   1.060/ 11|   1.057/ 12|   1.056/ 12|   1.055/ 12 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  59   |     568|      115.92|   1.028/ 25|   1.021/ 32|   1.020/ 35|   1.018/ 39 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  59   |      10|       13.94|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  63   |     831|      114.11|   1.037/ 19|   1.031/ 22|   1.030/ 23|   1.028/ 25 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  60   |     113|       37.46|   1.019/ 37|   1.013/ 52|   1.012/ 57|   1.011/ 62 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  80   |    3804|       96.28|   1.024/ 28|   1.021/ 33|   1.020/ 35|   1.019/ 36 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  70   |    1351|      234.55|   1.024/ 28|   1.023/ 29|   1.023/ 30|   1.023/ 30 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  65   |    3757|     1053.68|   1.018/ 38|   1.014/ 51|   1.013/ 55|   1.011/ 60 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  58   |     336|      345.27|   1.032/ 22|   1.027/ 25|   1.026/ 26|   1.025/ 27 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  76   |    2283|      106.28|   1.022/ 32|   1.018/ 39|   1.017/ 42|   1.016/ 44 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  72   |    1831|      172.48|   1.019/ 35|   1.017/ 42|   1.016/ 44|   1.015/ 46 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  53   |      17|       12.03|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  58   |      78|       43.47|   1.012/ 59|   1.013/ 54|   1.013/ 53|   1.013/ 52 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  67   |    4921|      388.35|   1.029/ 24|   1.024/ 28|   1.023/ 30|   1.022/ 31 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  68   |    2047|      304.00|   1.024/ 29|   1.017/ 41|   1.015/ 45|   1.014/ 50 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  59   |     435|      137.92|   1.042/ 16|   1.037/ 18|   1.036/ 19|   1.035/ 20 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  71   |     216|       74.13|   1.015/ 47|   1.011/ 65|   1.010/ 73|   1.008/ 82 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  68   |     390|       87.34|   1.022/ 31|   1.021/ 33|   1.021/ 33|   1.021/ 34 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  70   |    2722|      585.44|   1.013/ 52|   1.011/ 65|   1.010/ 69|   1.009/ 73 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  57   |      75|       56.05|   1.013/ 54|   1.011/ 65|   1.010/ 69|   1.010/ 72 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  65   |    2316|      383.09|   1.026/ 26|   1.020/ 34|   1.018/ 37|   1.017/ 41 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  64   |    6543|      941.44|   1.021/ 33|   1.015/ 46|   1.013/ 51|   1.012/ 58 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  65   |    5270|      527.66|   1.011/ 61|   1.008/ 87|   1.007/ 97|   1.006/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  63   |     881|      156.20|   1.035/ 20|   1.027/ 25|   1.025/ 27|   1.024/ 29 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  65   |     625|      210.11|   1.031/ 22|   1.026/ 27|   1.024/ 28|   1.023/ 30 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  65   |     702|      114.30|   1.027/ 25|   1.023/ 30|   1.022/ 31|   1.021/ 32 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  57   |      16|       14.98|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  56   |     144|       74.29|   1.038/ 18|   1.040/ 17|   1.040/ 17|   1.041/ 17 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  68   |     396|      128.45|   1.020/ 34|   1.017/ 40|   1.017/ 41|   1.016/ 43 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  61   |     213|      156.49|   1.043/ 16|   1.037/ 19|   1.035/ 20|   1.034/ 20 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  74   |   11615|     1307.66|   1.016/ 45|   1.010/ 69|   1.009/ 79|   1.007/ 93 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  59   |     317|      151.19|   1.036/ 19|   1.029/ 24|   1.027/ 26|   1.025/ 28 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  70   |   29570|     1520.01|   1.007/ 99|   1.005/ **|   1.004/ **|   1.003/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  59   |     783|       74.69|   1.026/ 26|   1.022/ 32|   1.021/ 33|   1.019/ 35 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  57   |      53|       69.43|   1.037/ 19|   1.032/ 22|   1.030/ 23|   1.029/ 24 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  64   |    1922|      164.43|   1.029/ 24|   1.024/ 28|   1.024/ 29|   1.023/ 31 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  65   |     312|       78.79|   1.012/ 59|   1.008/ 85|   1.007/ 94|   1.007/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  69   |     151|       35.84|   1.014/ 50|   1.010/ 67|   1.009/ 73|   1.009/ 80 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  65   |    5287|      412.97|   1.026/ 27|   1.017/ 41|   1.015/ 47|   1.013/ 55 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  63   |     131|       41.12|   1.013/ 54|   1.009/ 74|   1.008/ 82|   1.008/ 92 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  56   |     583|      550.62|   1.028/ 25|   1.022/ 31|   1.021/ 33|   1.019/ 36 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  68   |     447|       86.83|   1.020/ 35|   1.014/ 49|   1.013/ 54|   1.011/ 61 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  73   |      59|       66.58|   1.031/ 22|   1.025/ 28|   1.023/ 30|   1.022/ 32 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  63   |     327|       47.80|   1.019/ 37|   1.016/ 43|   1.015/ 45|   1.014/ 48 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  67   |    1532|       52.84|   1.027/ 26|   1.023/ 29|   1.023/ 30|   1.022/ 32 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  62   |      96|       29.88|   1.031/ 22|   1.029/ 24|   1.028/ 24|   1.027/ 25 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  64   |      55|       87.64|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  70   |    1199|      140.47|   1.027/ 26|   1.019/ 35|   1.018/ 39|   1.016/ 43 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  84   |    1084|      142.31|   1.011/ 65|   1.009/ 81|   1.008/ 86|   1.008/ 91 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  54   |      73|       40.81|   1.023/ 30|   1.021/ 32|   1.021/ 33|   1.020/ 34 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  64   |     505|       86.73|   1.019/ 36|   1.017/ 41|   1.016/ 43|   1.015/ 45 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  40   |      11|       19.76|   1.024/ 29|   1.049/ 14|   1.055/ 12|   1.061/ 11 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  62   |     211|        6.54|   1.046/ 15|   1.041/ 17|   1.039/ 17|   1.038/ 18 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  73   |      31|       11.05|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  72   |     582|       13.53|   1.012/ 57|   1.012/ 56|   1.012/ 56|   1.012/ 56 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  55   |       2|        0.06|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  76   |     439|        9.77|   1.028/ 24|   1.026/ 27|   1.025/ 27|   1.025/ 28 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  58   |      71|       23.89|   1.041/ 17|   1.045/ 15|   1.046/ 15|   1.048/ 14 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  83   |     105|        4.08|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  72   |     646|       72.60|   1.002/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  71   |      45|        4.45|   1.033/ 21|   1.035/ 20|   1.036/ 19|   1.036/ 19 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  68   |      12|        8.00|   1.020/ 34|   1.024/ 29|   1.025/ 28|   1.025/ 27 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  66   |     411|        2.44|   1.052/ 13|   1.058/ 12|   1.059/ 12|   1.061/ 11 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  53   |     194|       20.64|   1.033/ 21|   1.029/ 24|   1.028/ 25|   1.027/ 26 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  73   |    9521|      826.15|   1.006/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  47   |       2|        0.17|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  55   |     228|       19.90|   1.058/ 12|   1.054/ 13|   1.053/ 13|   1.053/ 13 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  63   |     154|       46.72|   1.028/ 25|   1.021/ 33|   1.019/ 37|   1.017/ 41 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  53   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  67   |   21804|      103.13|   1.056/ 12|   1.051/ 13|   1.050/ 14|   1.049/ 14 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  73   |     125|       17.99|   1.027/ 26|   1.024/ 29|   1.024/ 29|   1.023/ 30 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  66   |      53|        2.56|   1.006/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  40   |       1|        0.09|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  59   |     172|        6.47|   1.024/ 28|   1.025/ 28|   1.025/ 28|   1.025/ 28 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  75   |    6958|      183.10|   1.023/ 31|   1.014/ 49|   1.012/ 58|   1.010/ 70 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  25   |      60|        3.68|   1.062/ 11|   1.029/ 24|   1.021/ 32|   1.014/ 49 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  62   |     568|       29.70|   1.056/ 12|   1.065/ 11|   1.067/ 10|   1.070/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  73   |    4638|        3.31|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  62   |     693|       14.04|   1.034/ 20|   1.030/ 23|   1.029/ 24|   1.028/ 25 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  65   |      11|        2.08|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  65   |     103|       25.16|   1.009/ 79|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  66   |      84|        7.52|   1.007/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  70   |     576|       98.94|   1.007/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  67   |     471|       45.49|   1.014/ 48|   1.011/ 65|   1.010/ 72|   1.009/ 80 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  70   |    3522|      201.60|   1.036/ 19|   1.029/ 24|   1.027/ 26|   1.025/ 28 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  76   |     729|        7.27|   1.026/ 26|   1.023/ 29|   1.023/ 30|   1.022/ 31 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  53   |      36|        5.49|   1.055/ 12|   1.050/ 14|   1.048/ 14|   1.047/ 15 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  31   |      10|        7.16|   1.072/ 10|   1.072/  9|   1.072/  9|   1.074/  9 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  48   |       5|        0.05|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  63   |     319|       57.67|   1.013/ 55|   1.008/ 89|   1.006/ **|   1.005/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  98   |   29923|      446.11|   1.004/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  64   |      14|        6.40|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  61   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  49   |      13|        3.42|   1.015/ 45|   1.004/ **|   1.001/ **|   1.000/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  75   |    8515|      102.40|   1.007/ 94|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  63   |      33|        1.09|   1.033/ 21|   1.032/ 22|   1.031/ 22|   1.031/ 22 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  73   |     169|       15.80|   1.008/ 82|   1.008/ 88|   1.008/ 90|   1.008/ 91 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  68   |      46|        2.80|   1.060/ 11|   1.067/ 10|   1.069/ 10|   1.071/ 10 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  38   |      20|        1.60|   1.043/ 16|   1.038/ 18|   1.036/ 19|   1.033/ 21 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  27   |       7|        4.09|   1.070/ 10|   1.144/  5|   1.161/  4|   1.176/  4 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  48   |      26|        2.22|   1.048/ 14|   1.038/ 18|   1.035/ 20|   1.032/ 22 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  58   |     168|       18.31|   1.032/ 21|   1.026/ 27|   1.024/ 28|   1.023/ 30 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  69   |     502|       51.37|   1.015/ 47|   1.009/ 74|   1.008/ 87|   1.007/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  73   |    3995|        2.93|   1.048/ 14|   1.042/ 16|   1.040/ 17|   1.039/ 18 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  73   |    1284|        4.81|   1.024/ 28|   1.026/ 27|   1.026/ 27|   1.026/ 26 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  93   |    7425|       89.05|   1.008/ 88|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  80   |     136|        3.48|   1.023/ 30|   1.026/ 26|   1.027/ 26|   1.028/ 25 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  73   |    1663|      337.92|   1.008/ 83|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  63   |     287|       31.20|   1.009/ 74|   1.007/ 99|   1.006/ **|   1.006/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  92   |   33651|      558.62|   1.005/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  65   |       9|        3.40|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 100   |     947|        7.52|   1.020/ 34|   1.013/ 55|   1.011/ 64|   1.009/ 79 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  57   |       9|        0.85|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  59   |      36|        1.94|   1.011/ 61|   1.007/ 95|   1.006/ **|   1.005/ ** |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  58   |      58|        1.22|   1.039/ 17|   1.027/ 25|   1.024/ 29|   1.020/ 35 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  58   |      31|       17.07|   1.004/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  49   |     152|       34.45|   1.074/  9|   1.061/ 11|   1.057/ 12|   1.053/ 13 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  50   |      15|        2.24|   1.015/ 46|   1.007/ 98|   1.005/ **|   1.003/ ** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  50   |      21|       11.23|   1.017/ 40|   1.021/ 33|   1.022/ 31|   1.023/ 30 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  74   |      27|        3.90|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  49   |      23|        5.15|   1.014/ 49|   1.018/ 38|   1.019/ 35|   1.021/ 33 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  51   |       3|        0.44|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  63   |      61|       21.91|   1.017/ 41|   1.018/ 38|   1.018/ 38|   1.019/ 37 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  67   |     116|        3.54|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  55   |      62|        3.05|   1.042/ 16|   1.041/ 17|   1.041/ 17|   1.041/ 17 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  54   |       1|        0.25|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  65   |    7035|       55.58|   1.060/ 11|   1.057/ 12|   1.056/ 12|   1.055/ 12 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  66   |     249|       92.83|   1.031/ 22|   1.028/ 25|   1.027/ 26|   1.026/ 27 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  74   |     200|        5.58|   1.005/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  78   |    6031|      345.49|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  55   |      21|        4.25|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  57   |      16|        2.41|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  59   |      61|        2.75|   1.027/ 26|   1.024/ 29|   1.024/ 29|   1.023/ 30 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  61   |     239|        1.16|   1.044/ 15|   1.029/ 24|   1.025/ 28|   1.021/ 33 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  62   |     111|       53.43|   1.017/ 40|   1.017/ 39|   1.018/ 39|   1.018/ 39 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  70   |     239|       44.49|   1.005/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  53   |      31|        6.64|   1.063/ 11|   1.076/  9|   1.079/  9|   1.083/  8 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  65   |    1107|        5.05|   1.042/ 16|   1.035/ 19|   1.034/ 20|   1.032/ 21 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  73   |     308|       72.89|   1.019/ 37|   1.015/ 47|   1.014/ 50|   1.013/ 53 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  63   |      11|        1.57|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  64   |    3420|      106.43|   1.048/ 14|   1.042/ 16|   1.041/ 17|   1.039/ 17 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 111   |     967|        8.91|   1.015/ 47|   1.011/ 65|   1.010/ 72|   1.009/ 80 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  72   |    1031|       26.87|   1.017/ 40|   1.013/ 55|   1.011/ 60|   1.010/ 67 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  67   |    1298|      126.31|   1.011/ 65|   1.009/ 77|   1.009/ 81|   1.008/ 85 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  56   |      17|        6.15|   1.024/ 29|   1.029/ 24|   1.030/ 23|   1.031/ 22 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  62   |    1227|       63.24|   1.018/ 38|   1.013/ 54|   1.011/ 61|   1.010/ 69 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  65   |    3385|       23.07|   1.046/ 15|   1.039/ 18|   1.037/ 18|   1.036/ 19 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  60   |     371|       10.84|   1.034/ 20|   1.031/ 22|   1.030/ 23|   1.029/ 23 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  52   |      36|        2.19|   1.063/ 11|   1.053/ 13|   1.050/ 14|   1.047/ 15 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  64   |     249|       35.72|   1.010/ 70|   1.007/ 99|   1.006/ **|   1.006/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  30   |      38|        4.87|   1.077/  9|   1.041/ 17|   1.032/ 22|   1.022/ 31 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  63   |      24|        4.15|   1.012/ 60|   1.005/ **|   1.003/ **|   1.002/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  56   |      29|        5.26|   1.006/ **|   1.003/ **|   1.002/ **|   1.001/ ** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  70   |     108|       51.79|   1.005/ **|   1.002/ **|   1.001/ **|   1.000/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  45   |      63|        3.95|   1.026/ 27|   1.015/ 47|   1.012/ 56|   1.010/ 69 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  57   |     373|        6.35|   1.062/ 11|   1.066/ 10|   1.067/ 10|   1.068/ 10 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  81   |   28861|      612.76|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  56   |       9|        0.42|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  71   |     143|        3.37|   1.060/ 11|   1.048/ 14|   1.045/ 15|   1.042/ 16 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  73   |    4089|      395.53|   1.017/ 41|   1.013/ 53|   1.012/ 57|   1.011/ 62 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  79   |    1949|      226.48|   1.003/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  55   |       3|        0.17|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  53   |      22|        0.40|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  83   |      57|        0.86|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  57   |      12|        1.65|   1.013/ 53|   1.012/ 56|   1.012/ 57|   1.012/ 58 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  59   |       8|        5.87|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  65   |      47|        4.04|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  67   |    4418|       53.12|   1.011/ 65|   1.007/ **|   1.006/ **|   1.005/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  84   |  101656|      308.47|   1.016/ 44|   1.011/ 62|   1.010/ 69|   1.009/ 77 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  71   |     619|       14.79|   1.036/ 19|   1.033/ 21|   1.032/ 21|   1.032/ 22 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  64   |     266|       26.90|   1.026/ 26|   1.012/ 58|   1.008/ 83|   1.005/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  73   |   38292|      576.37|   1.011/ 60|   1.008/ 84|   1.008/ 92|   1.007/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  55   |      20|        5.82|   1.008/ 83|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  57   |      13|        0.38|   1.020/ 34|   1.023/ 30|   1.023/ 30|   1.024/ 29 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  57   |      10|        0.31|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  51   |       8|        0.45|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  61   |       4|        0.26|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |

