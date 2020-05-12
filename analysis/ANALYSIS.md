# State and Country COVID-19 Analysis #
## Updated: 2020-05-12 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  59   |   27688|     1423.31|   1.013/ 51|   1.008/ 86|   1.007/ **|   1.006/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  63   |   10056|     1132.15|   1.029/ 24|   1.020/ 34|   1.018/ 39|   1.016/ 44 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  53   |    5376|      773.61|   1.040/ 17|   1.027/ 26|   1.024/ 29|   1.021/ 34 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  54   |    4813|      481.89|   1.023/ 31|   1.014/ 48|   1.012/ 56|   1.010/ 67 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  54   |    4180|      326.51|   1.049/ 14|   1.042/ 16|   1.040/ 17|   1.038/ 18 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  56   |    3642|      287.42|   1.041/ 17|   1.035/ 20|   1.033/ 21|   1.032/ 22 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  54   |    3187|      893.87|   1.031/ 22|   1.021/ 33|   1.018/ 38|   1.016/ 44 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  69   |    3014|       76.27|   1.032/ 21|   1.023/ 30|   1.020/ 34|   1.018/ 38 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  59   |    2408|      518.00|   1.020/ 34|   1.014/ 49|   1.013/ 55|   1.011/ 62 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  65   |    1842|       85.78|   1.033/ 21|   1.027/ 25|   1.026/ 27|   1.024/ 28 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  73   |   88202|      267.65|   1.025/ 28|   1.014/ 48|   1.012/ 58|   1.009/ 73 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  62   |   35179|      529.53|   1.023/ 31|   1.015/ 46|   1.013/ 52|   1.011/ 61 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  81   |   32004|      531.29|   1.009/ 74|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  70   |   27610|      586.20|   1.010/ 73|   1.006/ **|   1.006/ **|   1.005/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  87   |   29265|      436.30|   1.007/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  56   |   12219|       57.80|   1.070/ 10|   1.064/ 11|   1.062/ 11|   1.061/ 11 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  62   |    9055|      785.71|   1.015/ 46|   1.009/ 78|   1.007/ 92|   1.006/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  64   |    8075|       97.12|   1.017/ 42|   1.009/ 75|   1.007/ 92|   1.006/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  82   |    6898|       82.73|   1.010/ 68|   1.008/ 87|   1.007/ 93|   1.007/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  67   |    5742|      328.92|   1.014/ 50|   1.009/ 80|   1.007/ 94|   1.006/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  48   |     417|       84.98|   1.042/ 16|   1.039/ 17|   1.039/ 18|   1.038/ 18 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  48   |      10|       13.69|   1.007/ **|   1.010/ 70|   1.011/ 64|   1.012/ 60 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  52   |     549|       75.47|   1.054/ 13|   1.059/ 12|   1.060/ 11|   1.062/ 11 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  49   |     101|       33.35|   1.039/ 18|   1.030/ 23|   1.027/ 25|   1.024/ 28 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  69   |    3014|       76.27|   1.032/ 21|   1.023/ 30|   1.020/ 34|   1.018/ 38 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  59   |    1071|      185.99|   1.026/ 26|   1.013/ 51|   1.010/ 67|   1.007/ 96 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  54   |    3187|      893.87|   1.031/ 22|   1.021/ 33|   1.018/ 38|   1.016/ 44 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  47   |     240|      246.52|   1.045/ 15|   1.031/ 22|   1.028/ 25|   1.024/ 28 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  65   |    1842|       85.78|   1.033/ 21|   1.027/ 25|   1.026/ 27|   1.024/ 28 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  61   |    1526|      143.72|   1.027/ 26|   1.019/ 35|   1.018/ 39|   1.016/ 44 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  42   |      17|       12.36|   1.011/ 62|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  47   |      70|       39.10|   1.013/ 54|   1.008/ 91|   1.006/ **|   1.005/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  56   |    3642|      287.42|   1.041/ 17|   1.035/ 20|   1.033/ 21|   1.032/ 22 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  57   |    1641|      243.82|   1.044/ 16|   1.037/ 19|   1.035/ 19|   1.034/ 20 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  48   |     285|       90.22|   1.057/ 12|   1.049/ 14|   1.047/ 15|   1.045/ 15 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  60   |     184|       63.23|   1.026/ 27|   1.022/ 32|   1.021/ 33|   1.020/ 35 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  57   |     323|       72.41|   1.027/ 25|   1.021/ 33|   1.019/ 36|   1.018/ 38 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  59   |    2408|      518.00|   1.020/ 34|   1.014/ 49|   1.013/ 55|   1.011/ 62 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  46   |      67|       49.61|   1.020/ 34|   1.014/ 49|   1.013/ 54|   1.011/ 61 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  54   |    1793|      296.66|   1.044/ 16|   1.032/ 21|   1.030/ 23|   1.027/ 25 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  53   |    5376|      773.61|   1.040/ 17|   1.027/ 26|   1.024/ 29|   1.021/ 34 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  54   |    4813|      481.89|   1.023/ 31|   1.014/ 48|   1.012/ 56|   1.010/ 67 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  52   |     640|      113.50|   1.058/ 12|   1.043/ 16|   1.040/ 17|   1.037/ 19 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  54   |     454|      152.42|   1.047/ 15|   1.047/ 15|   1.047/ 15|   1.047/ 15 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  54   |     528|       85.96|   1.040/ 17|   1.035/ 20|   1.034/ 20|   1.033/ 21 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  46   |      16|       15.34|   1.006/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  45   |      99|       51.28|   1.041/ 17|   1.028/ 25|   1.025/ 28|   1.022/ 32 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  57   |     328|      106.52|   1.029/ 24|   1.025/ 28|   1.023/ 29|   1.022/ 31 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  50   |     138|      101.46|   1.064/ 11|   1.068/ 10|   1.070/ 10|   1.071/ 10 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  63   |   10056|     1132.15|   1.029/ 24|   1.020/ 34|   1.018/ 39|   1.016/ 44 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  48   |     216|      102.94|   1.054/ 13|   1.044/ 16|   1.041/ 17|   1.039/ 18 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  59   |   27688|     1423.31|   1.013/ 51|   1.008/ 86|   1.007/ **|   1.006/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  48   |     593|       56.56|   1.040/ 17|   1.033/ 21|   1.031/ 22|   1.030/ 23 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  46   |      38|       49.30|   1.055/ 12|   1.053/ 13|   1.053/ 13|   1.052/ 13 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  53   |    1465|      125.32|   1.041/ 17|   1.031/ 22|   1.029/ 24|   1.026/ 26 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  54   |     286|       72.23|   1.023/ 30|   1.017/ 41|   1.015/ 46|   1.014/ 51 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  58   |     133|       31.48|   1.024/ 28|   1.022/ 32|   1.021/ 33|   1.020/ 34 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  54   |    4180|      326.51|   1.049/ 14|   1.042/ 16|   1.040/ 17|   1.038/ 18 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  52   |     114|       35.74|   1.023/ 30|   1.018/ 38|   1.017/ 40|   1.016/ 43 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  45   |     456|      430.07|   1.047/ 15|   1.041/ 17|   1.039/ 18|   1.037/ 18 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  57   |     379|       73.66|   1.041/ 17|   1.031/ 22|   1.028/ 24|   1.025/ 27 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  62   |      39|       43.65|   1.049/ 14|   1.048/ 14|   1.048/ 14|   1.047/ 14 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  52   |     257|       37.57|   1.022/ 32|   1.018/ 39|   1.017/ 41|   1.016/ 44 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  56   |    1151|       39.69|   1.035/ 19|   1.031/ 22|   1.030/ 23|   1.029/ 24 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  51   |      69|       21.53|   1.039/ 18|   1.038/ 18|   1.037/ 18|   1.037/ 18 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  53   |      55|       88.37|   1.010/ 70|   1.003/ **|   1.001/ **|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  59   |     927|      108.64|   1.045/ 15|   1.035/ 20|   1.032/ 21|   1.030/ 23 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  73   |     969|      127.28|   1.016/ 44|   1.012/ 56|   1.011/ 60|   1.011/ 65 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  43   |      57|       31.55|   1.031/ 22|   1.016/ 43|   1.012/ 57|   1.008/ 85 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  53   |     415|       71.30|   1.026/ 26|   1.024/ 28|   1.024/ 29|   1.023/ 30 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  29   |       7|       12.09|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  51   |     132|        4.10|   1.061/ 11|   1.055/ 12|   1.053/ 13|   1.052/ 13 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  62   |      32|       11.34|   1.005/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  61   |     509|       11.85|   1.012/ 59|   1.010/ 69|   1.010/ 72|   1.009/ 75 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  44   |       2|        0.06|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  65   |     330|        7.34|   1.035/ 20|   1.029/ 23|   1.028/ 24|   1.027/ 26 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  47   |      47|       16.00|   1.034/ 20|   1.031/ 22|   1.031/ 23|   1.030/ 23 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  72   |     106|        4.12|   1.011/ 61|   1.006/ **|   1.004/ **|   1.002/ ** |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  61   |     644|       72.29|   1.008/ 84|   1.002/ **|   1.001/ **|   1.000/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  60   |      32|        3.14|   1.029/ 24|   1.032/ 22|   1.033/ 21|   1.033/ 21 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  57   |       8|        5.26|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  55   |     231|        1.37|   1.035/ 20|   1.030/ 23|   1.029/ 24|   1.028/ 24 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  42   |     137|       14.56|   1.043/ 16|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  62   |    9055|      785.71|   1.015/ 46|   1.009/ 78|   1.007/ 92|   1.006/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  36   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  44   |     127|       11.03|   1.066/ 10|   1.067/ 10|   1.067/ 10|   1.067/ 10 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  52   |     108|       32.72|   1.045/ 15|   1.052/ 13|   1.054/ 13|   1.056/ 12 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  42   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  56   |   12219|       57.80|   1.070/ 10|   1.064/ 11|   1.062/ 11|   1.061/ 11 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  62   |      97|       13.98|   1.034/ 20|   1.031/ 22|   1.030/ 23|   1.029/ 24 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  55   |      50|        2.40|   1.012/ 59|   1.010/ 70|   1.009/ 73|   1.009/ 76 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  29   |       1|        0.09|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  48   |     121|        4.56|   1.056/ 12|   1.064/ 11|   1.066/ 10|   1.069/ 10 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  64   |    5625|      148.04|   1.044/ 16|   1.032/ 22|   1.029/ 24|   1.025/ 27 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  14   |      32|        1.99|   1.213/  3|   1.144/  5|   1.087/  8|   1.019/ 36 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  51   |     332|       17.39|   1.035/ 20|   1.029/ 24|   1.027/ 26|   1.025/ 28 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  62   |    4637|        3.31|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  51   |     489|        9.90|   1.046/ 15|   1.044/ 15|   1.044/ 16|   1.043/ 16 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  54   |       6|        1.26|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  54   |      97|       23.91|   1.030/ 23|   1.020/ 34|   1.017/ 40|   1.015/ 47 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  55   |      82|        7.29|   1.026/ 26|   1.014/ 49|   1.011/ 62|   1.008/ 86 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  59   |     550|       94.52|   1.016/ 43|   1.013/ 55|   1.012/ 59|   1.011/ 64 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  56   |     405|       39.09|   1.024/ 29|   1.022/ 32|   1.021/ 33|   1.020/ 34 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  59   |    2287|      130.90|   1.070/ 10|   1.068/ 10|   1.067/ 10|   1.066/ 10 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  65   |     565|        5.63|   1.033/ 21|   1.028/ 25|   1.026/ 26|   1.025/ 28 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  42   |      19|        2.89|   1.058/ 12|   1.056/ 12|   1.055/ 12|   1.053/ 13 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  20   |       4|        2.94|   1.058/ 12|   1.048/ 14|   1.016/ 44|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  37   |       5|        0.05|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  52   |     284|       51.40|   1.025/ 27|   1.018/ 38|   1.017/ 41|   1.015/ 46 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  87   |   29265|      436.30|   1.007/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  53   |       9|        4.28|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  50   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  38   |      11|        2.97|   1.045/ 15|   1.033/ 21|   1.029/ 24|   1.024/ 28 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  64   |    8075|       97.12|   1.017/ 42|   1.009/ 75|   1.007/ 92|   1.006/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  52   |      23|        0.76|   1.037/ 19|   1.036/ 19|   1.036/ 19|   1.036/ 19 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  62   |     156|       14.59|   1.009/ 76|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  57   |      27|        1.65|   1.051/ 13|   1.040/ 17|   1.038/ 18|   1.036/ 19 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  27   |      12|        0.97|   1.047/ 15|   1.022/ 31|   1.011/ 63|   1.000/ -- |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  16   |       3|        2.02|   1.000/ --|   1.189/  3|   1.156/  4|   1.126/  5 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  37   |      16|        1.35|   1.071/ 10|   1.064/ 11|   1.062/ 11|   1.059/ 12 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  47   |     120|       13.05|   1.046/ 15|   1.041/ 17|   1.040/ 17|   1.039/ 18 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  58   |     438|       44.86|   1.030/ 23|   1.023/ 30|   1.021/ 33|   1.019/ 36 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  62   |    2412|        1.77|   1.066/ 10|   1.064/ 11|   1.063/ 11|   1.062/ 11 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  62   |    1016|        3.81|   1.021/ 32|   1.017/ 41|   1.016/ 44|   1.015/ 47 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  82   |    6898|       82.73|   1.010/ 68|   1.008/ 87|   1.007/ 93|   1.007/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  69   |     109|        2.78|   1.016/ 45|   1.017/ 40|   1.017/ 40|   1.018/ 39 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  62   |    1643|      333.92|   1.023/ 30|   1.008/ 89|   1.004/ **|   1.000/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  52   |     259|       28.18|   1.015/ 45|   1.012/ 55|   1.012/ 59|   1.011/ 63 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  81   |   32004|      531.29|   1.009/ 74|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  54   |      10|        3.57|   1.018/ 38|   1.006/ **|   1.003/ **|   1.000/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  89   |     772|        6.13|   1.040/ 17|   1.031/ 22|   1.029/ 24|   1.027/ 26 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  46   |       9|        0.89|   1.012/ 57|   1.003/ **|   1.001/ **|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  48   |      32|        1.73|   1.020/ 34|   1.018/ 39|   1.017/ 40|   1.017/ 41 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  47   |      34|        0.72|   1.050/ 14|   1.055/ 13|   1.055/ 12|   1.056/ 12 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  47   |      33|       18.12|   1.010/ 68|   1.015/ 46|   1.016/ 43|   1.017/ 40 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  38   |      61|       13.87|   1.077/  9|   1.074/  9|   1.073/  9|   1.073/  9 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  39   |      13|        2.00|   1.034/ 20|   1.031/ 23|   1.029/ 24|   1.026/ 26 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  39   |      19|        9.85|   1.025/ 27|   1.011/ 61|   1.008/ 88|   1.004/ ** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  63   |      26|        3.88|   1.008/ 86|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  38   |      21|        4.74|   1.036/ 19|   1.005/ **|   1.000/ --|   1.000/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  40   |       3|        0.47|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  52   |      51|       18.21|   1.013/ 55|   1.009/ 75|   1.008/ 81|   1.008/ 89 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  56   |     110|        3.37|   1.007/ **|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  44   |      39|        1.92|   1.040/ 17|   1.045/ 15|   1.046/ 15|   1.047/ 14 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  43   |       1|        0.25|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  54   |    3849|       30.41|   1.069/ 10|   1.062/ 11|   1.060/ 11|   1.058/ 12 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  55   |     175|       65.37|   1.042/ 16|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  63   |     193|        5.39|   1.011/ 64|   1.008/ 90|   1.007/ 99|   1.006/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  67   |    5742|      328.92|   1.014/ 50|   1.009/ 80|   1.007/ 94|   1.006/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  44   |      22|        4.32|   1.009/ 75|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  46   |       6|        0.87|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  48   |      48|        2.13|   1.037/ 19|   1.032/ 21|   1.031/ 22|   1.031/ 23 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  50   |     160|        0.78|   1.091/  7|   1.081/  8|   1.078/  9|   1.076/  9 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  51   |      98|       47.20|   1.023/ 30|   1.013/ 54|   1.010/ 70|   1.007/ ** |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  59   |     226|       42.06|   1.007/ **|   1.002/ **|   1.001/ **|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  42   |      17|        3.72|   1.043/ 16|   1.054/ 13|   1.056/ 12|   1.059/ 12 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  54   |     738|        3.36|   1.062/ 11|   1.054/ 13|   1.052/ 13|   1.049/ 14 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  62   |     255|       60.40|   1.030/ 23|   1.026/ 27|   1.025/ 28|   1.024/ 29 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  52   |      10|        1.44|   1.006/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  53   |    2119|       65.95|   1.067/ 10|   1.056/ 12|   1.053/ 13|   1.050/ 14 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 100   |     850|        7.83|   1.023/ 31|   1.017/ 40|   1.016/ 43|   1.015/ 47 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  61   |     869|       22.63|   1.028/ 24|   1.018/ 37|   1.016/ 43|   1.013/ 51 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  56   |    1189|      115.72|   1.016/ 43|   1.010/ 69|   1.008/ 82|   1.007/ 99 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  45   |      14|        4.97|   1.022/ 31|   1.028/ 24|   1.029/ 23|   1.031/ 22 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  51   |    1009|       52.01|   1.031/ 22|   1.027/ 26|   1.025/ 27|   1.024/ 29 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  54   |    2168|       14.77|   1.069/ 10|   1.054/ 13|   1.051/ 14|   1.047/ 15 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  49   |     257|        7.51|   1.042/ 16|   1.041/ 17|   1.041/ 17|   1.041/ 17 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  41   |      18|        1.08|   1.068/ 10|   1.105/  6|   1.115/  6|   1.124/  5 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  53   |     236|       33.87|   1.015/ 47|   1.019/ 37|   1.019/ 36|   1.020/ 34 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  19   |      20|        2.50|   1.128/  5|   1.102/  7|   1.064/ 11|   1.021/ 33 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  52   |      22|        3.86|   1.031/ 22|   1.025/ 28|   1.023/ 30|   1.021/ 33 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  45   |      28|        5.09|   1.023/ 31|   1.006/ **|   1.001/ **|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  59   |     106|       50.45|   1.013/ 53|   1.009/ 76|   1.008/ 86|   1.007/ 99 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  34   |      53|        3.35|   1.057/ 12|   1.063/ 11|   1.064/ 11|   1.065/ 11 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  46   |     207|        3.53|   1.060/ 11|   1.060/ 11|   1.060/ 11|   1.060/ 11 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  70   |   27610|      586.20|   1.010/ 73|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  45   |       9|        0.43|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  60   |      79|        1.86|   1.095/  7|   1.093/  7|   1.092/  7|   1.091/  7 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  62   |    3460|      334.69|   1.027/ 26|   1.019/ 37|   1.017/ 41|   1.015/ 46 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  68   |    1930|      224.34|   1.008/ 87|   1.003/ **|   1.001/ **|   1.000/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  44   |       3|        0.17|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  42   |      22|        0.39|   1.045/ 15|   1.043/ 16|   1.044/ 16|   1.045/ 15 |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  72   |      58|        0.87|   1.005/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  46   |      11|        1.48|   1.023/ 30|   1.030/ 23|   1.032/ 22|   1.034/ 20 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  48   |       8|        5.87|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  54   |      46|        3.90|   1.010/ 68|   1.010/ 67|   1.010/ 67|   1.010/ 68 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  56   |    4025|       48.40|   1.021/ 32|   1.013/ 55|   1.010/ 67|   1.008/ 84 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  73   |   88202|      267.65|   1.025/ 28|   1.014/ 48|   1.012/ 58|   1.009/ 73 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  60   |     416|        9.92|   1.045/ 15|   1.040/ 17|   1.039/ 17|   1.038/ 18 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  53   |     217|       21.91|   1.069/ 10|   1.059/ 12|   1.056/ 12|   1.054/ 13 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  62   |   35179|      529.53|   1.023/ 31|   1.015/ 46|   1.013/ 52|   1.011/ 61 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  44   |      19|        5.39|   1.019/ 36|   1.013/ 53|   1.012/ 59|   1.011/ 64 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  46   |      11|        0.31|   1.016/ 43|   1.003/ **|   1.000/ --|   1.000/ -- |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  46   |      10|        0.31|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  40   |       6|        0.33|   1.081/  8|   1.119/  6|   1.128/  5|   1.137/  5 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  50   |       4|        0.27|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |

