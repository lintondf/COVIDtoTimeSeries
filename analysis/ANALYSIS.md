# State and Country COVID-19 Analysis #
## Updated: 2020-05-05 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  52   |   26597|     1367.20|   1.024/ 29|   1.008/ 85|   1.005/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  56   |    8629|      971.46|   1.044/ 15|   1.031/ 22|   1.027/ 25|   1.024/ 28 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  47   |    4339|      434.45|   1.038/ 18|   1.028/ 25|   1.025/ 28|   1.022/ 31 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  46   |    4492|      646.45|   1.065/ 10|   1.041/ 17|   1.035/ 20|   1.029/ 24 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  47   |    3005|      234.75|   1.062/ 11|   1.043/ 16|   1.039/ 17|   1.035/ 19 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  49   |    2826|      223.04|   1.051/ 14|   1.040/ 17|   1.037/ 19|   1.034/ 20 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  47   |    2723|      763.77|   1.051/ 13|   1.031/ 22|   1.026/ 27|   1.021/ 34 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  62   |    2541|       64.31|   1.046/ 15|   1.032/ 21|   1.029/ 24|   1.025/ 27 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  52   |    2165|      465.76|   1.031/ 23|   1.021/ 34|   1.018/ 38|   1.016/ 44 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  58   |    1514|       70.49|   1.041/ 17|   1.030/ 23|   1.027/ 26|   1.024/ 29 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  66   |   78882|      239.37|   1.038/ 18|   1.020/ 34|   1.016/ 43|   1.012/ 60 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  74   |   30513|      506.54|   1.014/ 50|   1.010/ 71|   1.009/ 79|   1.008/ 89 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  55   |   30292|      455.96|   1.041/ 17|   1.036/ 19|   1.035/ 20|   1.034/ 20 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  63   |   26273|      557.80|   1.015/ 48|   1.010/ 67|   1.009/ 75|   1.008/ 84 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  80   |   29407|      438.41|   1.013/ 52|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  55   |    8464|      734.43|   1.024/ 29|   1.010/ 69|   1.007/ **|   1.003/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  49   |    7892|       37.33|   1.079/  9|   1.071/ 10|   1.069/ 10|   1.067/ 10 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  57   |    7508|       90.30|   1.028/ 25|   1.015/ 46|   1.012/ 57|   1.009/ 77 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  75   |    6491|       77.84|   1.013/ 53|   1.010/ 71|   1.009/ 78|   1.008/ 86 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  60   |    5376|      307.95|   1.022/ 31|   1.015/ 45|   1.014/ 51|   1.012/ 58 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  41   |     310|       63.31|   1.044/ 16|   1.035/ 20|   1.033/ 21|   1.031/ 22 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  41   |       9|       12.30|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  45   |     373|       51.26|   1.046/ 15|   1.035/ 20|   1.032/ 21|   1.029/ 23 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  42   |      76|       25.34|   1.051/ 14|   1.065/ 10|   1.069/ 10|   1.073/  9 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  62   |    2541|       64.31|   1.046/ 15|   1.032/ 21|   1.029/ 24|   1.025/ 27 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  52   |     954|      165.68|   1.046/ 15|   1.031/ 22|   1.027/ 25|   1.023/ 30 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  47   |    2723|      763.77|   1.051/ 13|   1.031/ 22|   1.026/ 27|   1.021/ 34 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  40   |     192|      197.52|   1.068/ 10|   1.055/ 12|   1.052/ 13|   1.048/ 14 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  58   |    1514|       70.49|   1.041/ 17|   1.030/ 23|   1.027/ 26|   1.024/ 29 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  54   |    1306|      122.98|   1.038/ 18|   1.028/ 25|   1.025/ 27|   1.023/ 30 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  35   |      18|       12.45|   1.040/ 17|   1.017/ 40|   1.011/ 64|   1.004/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  40   |      66|       37.08|   1.025/ 27|   1.016/ 44|   1.013/ 52|   1.011/ 62 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  49   |    2826|      223.04|   1.051/ 14|   1.040/ 17|   1.037/ 19|   1.034/ 20 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  50   |    1251|      185.77|   1.051/ 13|   1.042/ 16|   1.040/ 17|   1.038/ 18 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  41   |     199|       63.23|   1.067/ 10|   1.059/ 12|   1.057/ 12|   1.055/ 12 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  53   |     157|       53.78|   1.032/ 21|   1.020/ 34|   1.018/ 39|   1.015/ 46 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  50   |     276|       61.73|   1.036/ 19|   1.024/ 29|   1.020/ 34|   1.017/ 40 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  52   |    2165|      465.76|   1.031/ 23|   1.021/ 34|   1.018/ 38|   1.016/ 44 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  39   |      60|       44.38|   1.037/ 19|   1.018/ 39|   1.013/ 53|   1.008/ 81 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  47   |    1434|      237.20|   1.068/ 10|   1.044/ 16|   1.038/ 18|   1.032/ 21 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  46   |    4492|      646.45|   1.065/ 10|   1.041/ 17|   1.035/ 20|   1.029/ 24 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  47   |    4339|      434.45|   1.038/ 18|   1.028/ 25|   1.025/ 28|   1.022/ 31 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  45   |     466|       82.71|   1.083/  8|   1.064/ 11|   1.059/ 12|   1.054/ 13 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  47   |     316|      106.20|   1.046/ 15|   1.039/ 17|   1.038/ 18|   1.037/ 19 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  47   |     414|       67.52|   1.046/ 15|   1.034/ 20|   1.031/ 22|   1.027/ 25 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  39   |      17|       15.74|   1.028/ 24|   1.009/ 77|   1.005/ **|   1.000/ ** |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  38   |      83|       42.94|   1.071/ 10|   1.049/ 14|   1.044/ 16|   1.039/ 18 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  50   |     274|       88.97|   1.037/ 19|   1.031/ 22|   1.030/ 23|   1.029/ 24 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  43   |      89|       65.50|   1.059/ 12|   1.060/ 11|   1.061/ 11|   1.062/ 11 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  56   |    8629|      971.46|   1.044/ 15|   1.031/ 22|   1.027/ 25|   1.024/ 28 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  41   |     160|       76.32|   1.075/  9|   1.063/ 11|   1.060/ 11|   1.058/ 12 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  52   |   26597|     1367.20|   1.024/ 29|   1.008/ 85|   1.005/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  41   |     473|       45.14|   1.055/ 13|   1.036/ 19|   1.031/ 22|   1.026/ 26 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  39   |      26|       34.08|   1.061/ 11|   1.054/ 13|   1.053/ 13|   1.052/ 13 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  46   |    1143|       97.77|   1.055/ 12|   1.042/ 16|   1.039/ 17|   1.036/ 19 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  47   |     252|       63.70|   1.035/ 20|   1.026/ 27|   1.023/ 30|   1.021/ 33 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  51   |     115|       27.16|   1.029/ 23|   1.023/ 30|   1.021/ 32|   1.020/ 35 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  47   |    3005|      234.75|   1.062/ 11|   1.043/ 16|   1.039/ 17|   1.035/ 19 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  45   |     102|       32.03|   1.032/ 21|   1.024/ 29|   1.022/ 32|   1.019/ 36 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  38   |     332|      313.22|   1.055/ 13|   1.054/ 13|   1.055/ 12|   1.055/ 12 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  50   |     291|       56.59|   1.062/ 11|   1.065/ 10|   1.066/ 10|   1.067/ 10 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  55   |      21|       23.58|   1.054/ 13|   1.064/ 11|   1.066/ 10|   1.068/ 10 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  45   |     220|       32.16|   1.026/ 26|   1.023/ 30|   1.022/ 31|   1.021/ 32 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  49   |     932|       32.15|   1.044/ 16|   1.037/ 19|   1.035/ 19|   1.034/ 20 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  44   |      53|       16.59|   1.044/ 16|   1.026/ 26|   1.022/ 31|   1.018/ 38 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  46   |      54|       86.06|   1.023/ 30|   1.017/ 40|   1.016/ 43|   1.015/ 47 |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  52   |     718|       84.08|   1.063/ 11|   1.051/ 13|   1.048/ 14|   1.046/ 15 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  66   |     892|      117.20|   1.019/ 36|   1.013/ 54|   1.011/ 61|   1.010/ 71 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  36   |      51|       28.24|   1.059/ 12|   1.047/ 14|   1.046/ 15|   1.044/ 16 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  46   |     352|       60.52|   1.031/ 22|   1.026/ 27|   1.024/ 28|   1.023/ 30 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  22   |       7|       12.09|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  44   |      86|        2.66|   1.068/ 10|   1.076/  9|   1.077/  9|   1.079/  9 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  55   |      32|       11.11|   1.013/ 54|   1.012/ 56|   1.012/ 56|   1.012/ 57 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  54   |     479|       11.13|   1.015/ 47|   1.009/ 76|   1.008/ 89|   1.006/ ** |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  37   |       2|        0.06|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  58   |     266|        5.92|   1.044/ 16|   1.039/ 18|   1.037/ 18|   1.036/ 19 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  40   |      37|       12.49|   1.037/ 18|   1.034/ 20|   1.033/ 21|   1.033/ 21 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  65   |     100|        3.88|   1.023/ 30|   1.020/ 34|   1.020/ 35|   1.019/ 36 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  54   |     632|       70.96|   1.018/ 38|   1.010/ 67|   1.008/ 82|   1.006/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  53   |      27|        2.65|   1.026/ 27|   1.017/ 41|   1.015/ 46|   1.013/ 52 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  50   |       8|        5.37|   1.007/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  48   |     201|        1.19|   1.048/ 14|   1.019/ 37|   1.012/ 59|   1.005/ ** |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  35   |     106|       11.27|   1.054/ 13|   1.046/ 15|   1.044/ 15|   1.042/ 16 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  55   |    8464|      734.43|   1.024/ 29|   1.010/ 69|   1.007/ **|   1.003/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  29   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  37   |      79|        6.87|   1.062/ 11|   1.064/ 11|   1.065/ 11|   1.065/ 10 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  45   |      78|       23.49|   1.034/ 20|   1.036/ 19|   1.037/ 19|   1.038/ 18 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  35   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  49   |    7892|       37.33|   1.079/  9|   1.071/ 10|   1.069/ 10|   1.067/ 10 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  55   |      77|       11.12|   1.041/ 17|   1.039/ 18|   1.038/ 18|   1.038/ 18 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  48   |      46|        2.21|   1.015/ 46|   1.009/ 78|   1.007/ 92|   1.006/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  22   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  41   |      69|        2.61|   1.044/ 15|   1.019/ 36|   1.013/ 54|   1.006/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  57   |    4421|      116.34|   1.064/ 11|   1.045/ 15|   1.040/ 17|   1.035/ 19 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  44   |     273|       14.27|   1.049/ 14|   1.043/ 16|   1.042/ 16|   1.041/ 17 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  55   |    4709|        3.36|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  44   |     357|        7.23|   1.049/ 14|   1.047/ 15|   1.047/ 15|   1.046/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  47   |       6|        1.24|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  47   |      82|       20.23|   1.047/ 15|   1.043/ 16|   1.043/ 16|   1.042/ 16 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  48   |      74|        6.63|   1.049/ 14|   1.033/ 21|   1.029/ 24|   1.025/ 28 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  52   |     499|       85.62|   1.023/ 30|   1.019/ 36|   1.018/ 37|   1.018/ 39 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  49   |     343|       33.07|   1.029/ 24|   1.025/ 27|   1.025/ 28|   1.024/ 29 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  52   |    1361|       77.90|   1.100/  7|   1.131/  5|   1.139/  5|   1.147/  5 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  58   |     463|        4.62|   1.043/ 16|   1.036/ 19|   1.034/ 20|   1.032/ 21 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  35   |      12|        1.82|   1.040/ 17|   1.062/ 11|   1.068/ 10|   1.074/  9 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  13   |       1|        0.74|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  30   |       3|        0.03|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  45   |     258|       46.59|   1.041/ 17|   1.026/ 27|   1.022/ 32|   1.018/ 39 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  80   |   29407|      438.41|   1.013/ 52|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  46   |       6|        2.57|   1.168/  4|   1.122/  6|   1.111/  6|   1.101/  7 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  43   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  31   |       9|        2.36|   1.051/ 14|   1.080/  9|   1.088/  8|   1.096/  7 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  57   |    7508|       90.30|   1.028/ 25|   1.015/ 46|   1.012/ 57|   1.009/ 77 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  45   |      20|        0.64|   1.038/ 18|   1.041/ 17|   1.041/ 17|   1.041/ 17 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  55   |     150|       14.02|   1.016/ 43|   1.012/ 59|   1.011/ 65|   1.009/ 74 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  50   |      21|        1.25|   1.062/ 11|   1.042/ 17|   1.036/ 19|   1.029/ 23 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  20   |       8|        0.63|   1.021/ 32|   1.018/ 39|   1.032/ 21|   1.048/ 14 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  30   |      10|        0.85|   1.057/ 12|   1.080/  9|   1.088/  8|   1.096/  7 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  40   |      84|        9.21|   1.046/ 15|   1.047/ 15|   1.046/ 15|   1.046/ 15 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  51   |     373|       38.20|   1.044/ 15|   1.028/ 25|   1.024/ 29|   1.020/ 35 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  55   |    1516|        1.11|   1.070/ 10|   1.068/ 10|   1.068/ 10|   1.068/ 10 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  55   |     905|        3.39|   1.028/ 24|   1.018/ 39|   1.015/ 46|   1.012/ 56 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  75   |    6491|       77.84|   1.013/ 53|   1.010/ 71|   1.009/ 78|   1.008/ 86 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  62   |      97|        2.48|   1.012/ 56|   1.013/ 54|   1.013/ 53|   1.013/ 53 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  55   |    1534|      311.78|   1.047/ 14|   1.027/ 25|   1.022/ 32|   1.016/ 43 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  45   |     239|       26.00|   1.023/ 30|   1.016/ 44|   1.014/ 49|   1.013/ 55 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  74   |   30513|      506.54|   1.014/ 50|   1.010/ 71|   1.009/ 79|   1.008/ 89 |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  47   |       9|        3.28|   1.041/ 17|   1.040/ 17|   1.040/ 17|   1.040/ 17 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  82   |     600|        4.77|   1.059/ 12|   1.053/ 13|   1.052/ 13|   1.050/ 14 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  39   |       9|        0.84|   1.021/ 32|   1.037/ 19|   1.041/ 17|   1.045/ 15 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  41   |      28|        1.51|   1.028/ 25|   1.016/ 42|   1.013/ 53|   1.010/ 69 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  40   |      22|        0.47|   1.048/ 14|   1.084/  8|   1.094/  7|   1.104/  6 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  40   |      23|       12.99|   1.006/ **|   1.018/ 37|   1.022/ 32|   1.025/ 28 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  31   |      40|        9.00|   1.103/  7|   1.099/  7|   1.099/  7|   1.099/  7 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  32   |       9|        1.40|   1.013/ 54|   1.033/ 21|   1.039/ 18|   1.046/ 15 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  32   |      17|        8.89|   1.045/ 15|   1.031/ 22|   1.027/ 25|   1.023/ 30 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  56   |      25|        3.71|   1.011/ 63|   1.011/ 61|   1.011/ 61|   1.011/ 61 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  31   |      20|        4.48|   1.111/  6|   1.047/ 15|   1.029/ 24|   1.009/ 76 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  33   |       3|        0.44|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  45   |      48|       17.05|   1.019/ 36|   1.011/ 61|   1.010/ 72|   1.008/ 89 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  49   |     106|        3.25|   1.011/ 62|   1.008/ 86|   1.007/ 95|   1.007/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  37   |      29|        1.44|   1.040/ 17|   1.025/ 27|   1.021/ 32|   1.018/ 39 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  36   |       1|        0.25|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  47   |    2550|       20.14|   1.082/  8|   1.062/ 11|   1.057/ 12|   1.052/ 13 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  48   |     139|       51.83|   1.050/ 14|   1.037/ 19|   1.034/ 20|   1.031/ 22 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  56   |     182|        5.06|   1.015/ 45|   1.011/ 62|   1.010/ 69|   1.009/ 77 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  60   |    5376|      307.95|   1.022/ 31|   1.015/ 45|   1.014/ 51|   1.012/ 58 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  37   |      21|        4.21|   1.027/ 25|   1.008/ 82|   1.004/ **|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  39   |       3|        0.53|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  41   |      38|        1.71|   1.046/ 15|   1.037/ 19|   1.034/ 20|   1.031/ 22 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  43   |      92|        0.45|   1.116/  6|   1.129/  5|   1.133/  5|   1.138/  5 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  44   |      87|       41.96|   1.038/ 18|   1.041/ 17|   1.041/ 17|   1.042/ 16 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  52   |     224|       41.70|   1.014/ 48|   1.004/ **|   1.001/ **|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  35   |      12|        2.61|   1.038/ 18|   1.028/ 25|   1.026/ 26|   1.025/ 27 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  47   |     500|        2.28|   1.076/  9|   1.067/ 10|   1.065/ 10|   1.063/ 11 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  55   |     214|       50.67|   1.035/ 20|   1.025/ 28|   1.022/ 31|   1.020/ 35 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  45   |      10|        1.42|   1.015/ 45|   1.014/ 50|   1.013/ 51|   1.013/ 52 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  46   |    1422|       44.25|   1.087/  8|   1.077/  9|   1.074/  9|   1.072/  9 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  93   |     767|        7.06|   1.028/ 25|   1.019/ 36|   1.017/ 40|   1.015/ 45 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  54   |     757|       19.73|   1.044/ 16|   1.032/ 22|   1.029/ 24|   1.026/ 27 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  49   |    1098|      106.87|   1.027/ 26|   1.019/ 36|   1.017/ 40|   1.015/ 45 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  38   |      12|        4.35|   1.024/ 29|   1.029/ 24|   1.031/ 22|   1.034/ 20 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  44   |     835|       43.02|   1.040/ 17|   1.035/ 20|   1.034/ 21|   1.032/ 21 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  47   |    1488|       10.14|   1.095/  7|   1.073/  9|   1.068/ 10|   1.063/ 11 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  42   |     193|        5.65|   1.045/ 15|   1.039/ 17|   1.038/ 18|   1.037/ 19 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  34   |      10|        0.62|   1.058/ 12|   1.012/ 59|   1.000/ --|   1.000/ -- |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  46   |     187|       26.89|   1.010/ 68|   1.011/ 63|   1.012/ 59|   1.013/ 55 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  12   |       9|        1.12|   1.206/  3|   1.188/  4|   1.127/  5|   1.055/ 12 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  45   |      18|        3.10|   1.038/ 18|   1.050/ 14|   1.053/ 13|   1.056/ 12 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  38   |      26|        4.81|   1.051/ 13|   1.036/ 19|   1.031/ 22|   1.027/ 25 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  52   |      99|       47.08|   1.022/ 32|   1.016/ 43|   1.015/ 46|   1.014/ 49 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  27   |      34|        2.17|   1.132/  5|   1.047/ 15|   1.030/ 23|   1.015/ 46 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  39   |     138|        2.34|   1.064/ 11|   1.062/ 11|   1.061/ 11|   1.061/ 11 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  63   |   26273|      557.80|   1.015/ 48|   1.010/ 67|   1.009/ 75|   1.008/ 84 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  38   |       7|        0.32|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  53   |      48|        1.12|   1.114/  6|   1.132/  5|   1.136/  5|   1.140/  5 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  55   |    3011|      291.29|   1.039/ 18|   1.023/ 30|   1.019/ 37|   1.015/ 47 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  61   |    1881|      218.62|   1.016/ 43|   1.009/ 80|   1.007/ **|   1.005/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  37   |       3|        0.17|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  35   |      17|        0.31|   1.042/ 17|   1.041/ 17|   1.041/ 17|   1.041/ 17 |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  65   |      57|        0.86|   1.010/ 68|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  39   |       9|        1.24|   1.035/ 19|   1.044/ 16|   1.047/ 15|   1.050/ 14 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  41   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  47   |      42|        3.61|   1.010/ 69|   1.012/ 57|   1.013/ 54|   1.014/ 51 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  49   |    3662|       44.04|   1.037/ 18|   1.024/ 29|   1.021/ 34|   1.017/ 40 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  66   |   78882|      239.37|   1.038/ 18|   1.020/ 34|   1.016/ 43|   1.012/ 60 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  53   |     317|        7.58|   1.051/ 13|   1.041/ 17|   1.039/ 18|   1.036/ 19 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  46   |     142|       14.34|   1.083/  8|   1.077/  9|   1.075/  9|   1.073/  9 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  55   |   30292|      455.96|   1.041/ 17|   1.036/ 19|   1.035/ 20|   1.034/ 20 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  37   |      18|        5.15|   1.041/ 17|   1.022/ 31|   1.017/ 41|   1.012/ 58 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  39   |      10|        0.30|   1.044/ 16|   1.023/ 29|   1.019/ 37|   1.014/ 48 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  39   |      10|        0.31|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  33   |       3|        0.17|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  43   |       4|        0.28|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |

