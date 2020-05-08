# State and Country COVID-19 Analysis #
## Updated: 2020-05-08 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  55   |   26906|     1383.09|   1.018/ 39|   1.008/ 90|   1.005/ **|   1.003/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  59   |    9279|     1044.68|   1.038/ 18|   1.027/ 26|   1.024/ 29|   1.022/ 32 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  49   |    4858|      699.06|   1.052/ 13|   1.032/ 22|   1.027/ 25|   1.022/ 31 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  50   |    4568|      457.42|   1.030/ 23|   1.019/ 36|   1.016/ 42|   1.014/ 51 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  50   |    3546|      277.02|   1.060/ 11|   1.056/ 12|   1.055/ 12|   1.055/ 13 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  52   |    3171|      250.25|   1.047/ 15|   1.040/ 17|   1.038/ 18|   1.037/ 19 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  50   |    2940|      824.63|   1.041/ 17|   1.027/ 26|   1.023/ 29|   1.020/ 35 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  65   |    2746|       69.51|   1.040/ 17|   1.028/ 24|   1.025/ 27|   1.023/ 31 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  55   |    2279|      490.14|   1.026/ 26|   1.019/ 36|   1.017/ 40|   1.016/ 44 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  61   |    1645|       76.61|   1.038/ 18|   1.030/ 23|   1.028/ 25|   1.026/ 27 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  69   |   82752|      251.11|   1.032/ 22|   1.018/ 39|   1.014/ 48|   1.011/ 64 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  58   |   32815|      493.93|   1.033/ 21|   1.026/ 27|   1.024/ 29|   1.022/ 31 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  77   |   31192|      517.81|   1.012/ 59|   1.008/ 86|   1.007/ 97|   1.006/ ** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  66   |   26922|      571.60|   1.012/ 58|   1.008/ 84|   1.007/ 95|   1.006/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  83   |   29222|      435.66|   1.010/ 70|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  52   |    9512|       44.99|   1.074/  9|   1.067/ 10|   1.065/ 11|   1.063/ 11 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  58   |    8740|      758.36|   1.019/ 36|   1.010/ 67|   1.008/ 84|   1.006/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  60   |    7781|       93.58|   1.022/ 31|   1.012/ 57|   1.010/ 72|   1.007/ 95 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  78   |    6679|       80.10|   1.012/ 58|   1.009/ 75|   1.009/ 81|   1.008/ 88 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  63   |    5544|      317.58|   1.018/ 38|   1.012/ 59|   1.010/ 68|   1.009/ 81 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  44   |     354|       72.26|   1.044/ 16|   1.045/ 15|   1.045/ 15|   1.045/ 15 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  44   |       9|       12.86|   1.005/ **|   1.013/ 54|   1.015/ 47|   1.017/ 41 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  48   |     432|       59.39|   1.048/ 14|   1.048/ 14|   1.049/ 14|   1.049/ 14 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  45   |      90|       29.90|   1.052/ 13|   1.056/ 12|   1.057/ 12|   1.058/ 12 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  65   |    2746|       69.51|   1.040/ 17|   1.028/ 24|   1.025/ 27|   1.023/ 31 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  55   |    1017|      176.57|   1.038/ 18|   1.025/ 27|   1.022/ 31|   1.019/ 37 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  50   |    2940|      824.63|   1.041/ 17|   1.027/ 26|   1.023/ 29|   1.020/ 35 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  43   |     213|      218.56|   1.057/ 12|   1.040/ 17|   1.036/ 19|   1.032/ 22 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  61   |    1645|       76.61|   1.038/ 18|   1.030/ 23|   1.028/ 25|   1.026/ 27 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  57   |    1409|      132.71|   1.035/ 20|   1.028/ 25|   1.026/ 27|   1.024/ 29 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  38   |      18|       12.55|   1.027/ 26|   1.006/ **|   1.001/ **|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  43   |      68|       38.07|   1.019/ 37|   1.011/ 61|   1.010/ 73|   1.008/ 89 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  52   |    3171|      250.25|   1.047/ 15|   1.040/ 17|   1.038/ 18|   1.037/ 19 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  53   |    1424|      211.45|   1.051/ 13|   1.048/ 14|   1.047/ 15|   1.046/ 15 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  44   |     235|       74.62|   1.064/ 11|   1.059/ 12|   1.057/ 12|   1.056/ 12 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  56   |     169|       58.18|   1.031/ 22|   1.025/ 27|   1.024/ 29|   1.023/ 30 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  53   |     297|       66.56|   1.034/ 20|   1.027/ 26|   1.025/ 27|   1.024/ 29 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  55   |    2279|      490.14|   1.026/ 26|   1.019/ 36|   1.017/ 40|   1.016/ 44 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  42   |      63|       47.18|   1.029/ 24|   1.021/ 33|   1.019/ 36|   1.017/ 40 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  50   |    1593|      263.49|   1.055/ 13|   1.039/ 18|   1.035/ 20|   1.031/ 22 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  49   |    4858|      699.06|   1.052/ 13|   1.032/ 22|   1.027/ 25|   1.022/ 31 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  50   |    4568|      457.42|   1.030/ 23|   1.019/ 36|   1.016/ 42|   1.014/ 51 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  48   |     542|       96.04|   1.071/ 10|   1.054/ 13|   1.049/ 14|   1.045/ 15 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  50   |     374|      125.78|   1.051/ 13|   1.055/ 12|   1.057/ 12|   1.058/ 12 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  50   |     456|       74.33|   1.042/ 16|   1.034/ 21|   1.031/ 22|   1.029/ 23 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  42   |      17|       15.61|   1.015/ 47|   1.002/ **|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  41   |      90|       46.42|   1.053/ 13|   1.034/ 20|   1.029/ 24|   1.024/ 29 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  53   |     299|       97.09|   1.034/ 20|   1.031/ 22|   1.030/ 23|   1.029/ 24 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  46   |     105|       77.12|   1.057/ 12|   1.058/ 12|   1.059/ 12|   1.059/ 12 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  59   |    9279|     1044.68|   1.038/ 18|   1.027/ 26|   1.024/ 29|   1.022/ 32 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  44   |     184|       87.73|   1.064/ 11|   1.050/ 14|   1.047/ 15|   1.043/ 16 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  55   |   26906|     1383.09|   1.018/ 39|   1.008/ 90|   1.005/ **|   1.003/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  44   |     523|       49.87|   1.046/ 15|   1.036/ 19|   1.033/ 21|   1.031/ 22 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  42   |      30|       39.99|   1.057/ 12|   1.057/ 12|   1.058/ 12|   1.058/ 12 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  49   |    1293|      110.58|   1.052/ 13|   1.045/ 15|   1.043/ 16|   1.042/ 17 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  50   |     268|       67.61|   1.029/ 24|   1.021/ 32|   1.019/ 36|   1.017/ 40 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  54   |     122|       28.89|   1.026/ 26|   1.021/ 32|   1.020/ 34|   1.019/ 36 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  50   |    3546|      277.02|   1.060/ 11|   1.056/ 12|   1.055/ 12|   1.055/ 13 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  48   |     106|       33.30|   1.025/ 27|   1.015/ 45|   1.013/ 54|   1.010/ 68 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  41   |     389|      367.37|   1.054/ 13|   1.054/ 13|   1.054/ 13|   1.055/ 13 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  53   |     337|       65.38|   1.054/ 13|   1.050/ 14|   1.049/ 14|   1.048/ 14 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  58   |      28|       32.20|   1.072/ 10|   1.084/  8|   1.087/  8|   1.090/  8 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  48   |     239|       34.95|   1.027/ 25|   1.027/ 25|   1.027/ 25|   1.028/ 25 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  52   |    1020|       35.17|   1.038/ 18|   1.032/ 22|   1.030/ 23|   1.029/ 24 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  47   |      60|       18.58|   1.042/ 16|   1.038/ 18|   1.037/ 19|   1.037/ 19 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  49   |      55|       87.61|   1.016/ 42|   1.009/ 77|   1.007/ 98|   1.005/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  55   |     807|       94.50|   1.054/ 13|   1.043/ 16|   1.040/ 17|   1.037/ 19 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  69   |     922|      121.08|   1.017/ 41|   1.012/ 58|   1.011/ 64|   1.010/ 73 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  39   |      54|       29.89|   1.044/ 16|   1.028/ 25|   1.023/ 30|   1.018/ 37 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  49   |     377|       64.80|   1.028/ 25|   1.024/ 28|   1.023/ 29|   1.023/ 31 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  25   |       7|       12.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  47   |     107|        3.33|   1.072/ 10|   1.076/  9|   1.078/  9|   1.079/  9 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  58   |      32|       11.30|   1.009/ 77|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  57   |     490|       11.39|   1.012/ 56|   1.008/ 82|   1.008/ 92|   1.007/ ** |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  40   |       2|        0.06|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  61   |     293|        6.53|   1.040/ 17|   1.035/ 20|   1.033/ 21|   1.032/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  43   |      42|       14.11|   1.039/ 18|   1.039/ 17|   1.040/ 17|   1.041/ 17 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  68   |     104|        4.04|   1.019/ 37|   1.015/ 46|   1.014/ 49|   1.013/ 53 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  57   |     639|       71.76|   1.013/ 52|   1.006/ **|   1.004/ **|   1.002/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  56   |      28|        2.81|   1.024/ 29|   1.021/ 34|   1.020/ 35|   1.019/ 36 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  53   |       8|        5.32|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  51   |     206|        1.22|   1.035/ 20|   1.014/ 49|   1.009/ 77|   1.004/ ** |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  38   |     118|       12.59|   1.048/ 14|   1.040/ 17|   1.038/ 18|   1.036/ 19 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  58   |    8740|      758.36|   1.019/ 36|   1.010/ 67|   1.008/ 84|   1.006/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  32   |       2|        0.20|   1.175/  4|   1.066/ 10|   1.027/ 25|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  40   |      97|        8.50|   1.066/ 10|   1.072/ 10|   1.074/  9|   1.076/  9 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  48   |      87|       26.39|   1.036/ 19|   1.039/ 18|   1.040/ 17|   1.041/ 17 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  38   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  52   |    9512|       44.99|   1.074/  9|   1.067/ 10|   1.065/ 11|   1.063/ 11 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  58   |      86|       12.42|   1.039/ 17|   1.038/ 18|   1.037/ 18|   1.037/ 19 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  51   |      48|        2.31|   1.015/ 45|   1.014/ 49|   1.014/ 50|   1.014/ 50 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  25   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  44   |      83|        3.13|   1.054/ 13|   1.073/  9|   1.078/  9|   1.084/  8 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  60   |    4970|      130.80|   1.055/ 12|   1.040/ 17|   1.036/ 19|   1.032/ 21 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  10   |      26|        1.58|   1.357/  2|   1.193/  3|   1.193/  3|   1.392/  2 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  47   |     299|       15.67|   1.042/ 16|   1.034/ 20|   1.032/ 21|   1.031/ 23 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  58   |    4970|        3.54|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  47   |     411|        8.33|   1.049/ 14|   1.048/ 14|   1.048/ 14|   1.049/ 14 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  50   |       6|        1.22|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  50   |      91|       22.28|   1.040/ 17|   1.035/ 20|   1.033/ 21|   1.032/ 22 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  51   |      78|        6.93|   1.036/ 19|   1.020/ 35|   1.016/ 44|   1.011/ 60 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  55   |     523|       89.89|   1.020/ 34|   1.017/ 40|   1.016/ 42|   1.016/ 44 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  52   |     371|       35.85|   1.028/ 25|   1.026/ 26|   1.026/ 26|   1.026/ 26 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  55   |    1770|      101.33|   1.081/  8|   1.089/  8|   1.091/  7|   1.092/  7 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  61   |     506|        5.04|   1.038/ 18|   1.032/ 22|   1.030/ 23|   1.028/ 24 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  38   |      15|        2.31|   1.056/ 12|   1.078/  9|   1.084/  8|   1.089/  8 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  16   |       5|        3.56|   1.000/ --|   1.424/  1|   1.384/  2|   1.328/  2 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  33   |       3|        0.03|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  48   |     271|       49.12|   1.034/ 20|   1.025/ 27|   1.023/ 30|   1.021/ 32 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  83   |   29222|      435.66|   1.010/ 70|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  49   |       1|        0.46|   1.125/  5|   1.109/  6|   1.105/  6|   1.101/  7 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  46   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  34   |      10|        2.63|   1.055/ 12|   1.044/ 15|   1.042/ 17|   1.038/ 18 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  60   |    7781|       93.58|   1.022/ 31|   1.012/ 57|   1.010/ 72|   1.007/ 95 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  48   |      21|        0.69|   1.026/ 27|   1.017/ 41|   1.014/ 48|   1.011/ 61 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  58   |     153|       14.31|   1.013/ 55|   1.007/ 93|   1.006/ **|   1.005/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  53   |      23|        1.40|   1.058/ 12|   1.043/ 16|   1.039/ 18|   1.035/ 19 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  23   |      11|        0.93|   1.012/ 55|   1.097/  7|   1.119/  6|   1.140/  5 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  12   |       2|        1.32|   1.000/ --|   1.000/ --|   1.197/  3|   1.285/  2 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  33   |      13|        1.10|   1.072/  9|   1.092/  7|   1.096/  7|   1.100/  7 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  43   |     101|       11.08|   1.053/ 13|   1.060/ 11|   1.062/ 11|   1.064/ 11 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  54   |     402|       41.11|   1.037/ 19|   1.025/ 28|   1.022/ 31|   1.019/ 36 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  58   |    1882|        1.38|   1.072/  9|   1.074/  9|   1.074/  9|   1.075/  9 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  58   |     951|        3.56|   1.024/ 28|   1.017/ 41|   1.015/ 46|   1.013/ 52 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  78   |    6679|       80.10|   1.012/ 58|   1.009/ 75|   1.009/ 81|   1.008/ 88 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  65   |     102|        2.60|   1.014/ 49|   1.015/ 45|   1.016/ 44|   1.016/ 43 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  58   |    1600|      325.09|   1.034/ 20|   1.015/ 46|   1.010/ 68|   1.005/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  48   |     247|       26.92|   1.018/ 38|   1.013/ 54|   1.011/ 61|   1.010/ 68 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  77   |   31192|      517.81|   1.012/ 59|   1.008/ 86|   1.007/ 97|   1.006/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  50   |      10|        3.49|   1.032/ 22|   1.025/ 28|   1.023/ 30|   1.021/ 33 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  85   |     682|        5.41|   1.053/ 13|   1.045/ 15|   1.043/ 16|   1.041/ 17 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  42   |       9|        0.88|   1.020/ 34|   1.019/ 36|   1.019/ 37|   1.018/ 39 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  44   |      30|        1.61|   1.026/ 26|   1.022/ 31|   1.021/ 32|   1.021/ 32 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  43   |      28|        0.58|   1.048/ 14|   1.066/ 10|   1.069/ 10|   1.073/  9 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  43   |      29|       16.22|   1.021/ 32|   1.036/ 19|   1.040/ 17|   1.044/ 15 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  34   |      47|       10.65|   1.091/  7|   1.068/ 10|   1.062/ 11|   1.056/ 12 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  35   |      12|        1.78|   1.033/ 21|   1.065/ 11|   1.073/  9|   1.082/  8 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  35   |      18|        9.47|   1.035/ 19|   1.026/ 26|   1.024/ 29|   1.021/ 33 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  59   |      26|        3.77|   1.008/ 87|   1.006/ **|   1.006/ **|   1.005/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  34   |      21|        4.77|   1.074/  9|   1.031/ 22|   1.020/ 34|   1.010/ 70 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  36   |       3|        0.46|   1.145/  5|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  48   |      49|       17.56|   1.015/ 45|   1.011/ 65|   1.010/ 72|   1.008/ 82 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  52   |     109|        3.32|   1.010/ 73|   1.007/ 98|   1.006/ **|   1.006/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  40   |      33|        1.61|   1.039/ 18|   1.039/ 18|   1.039/ 17|   1.040/ 17 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  39   |       1|        0.25|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  50   |    3058|       24.16|   1.077/  9|   1.066/ 10|   1.063/ 11|   1.061/ 11 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  51   |     152|       56.72|   1.044/ 16|   1.034/ 20|   1.031/ 22|   1.029/ 24 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  59   |     187|        5.22|   1.014/ 49|   1.011/ 64|   1.010/ 68|   1.009/ 74 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  63   |    5544|      317.58|   1.018/ 38|   1.012/ 59|   1.010/ 68|   1.009/ 81 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  40   |      21|        4.30|   1.020/ 35|   1.015/ 46|   1.014/ 49|   1.013/ 53 |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  42   |       5|        0.82|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  44   |      42|        1.87|   1.040/ 17|   1.030/ 23|   1.028/ 25|   1.026/ 27 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  46   |     119|        0.58|   1.100/  7|   1.093/  7|   1.090/  8|   1.088/  8 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  47   |      94|       45.16|   1.032/ 21|   1.028/ 25|   1.026/ 26|   1.025/ 28 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  55   |     224|       41.76|   1.010/ 68|   1.002/ **|   1.000/ **|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  38   |      14|        2.96|   1.033/ 21|   1.040/ 17|   1.042/ 16|   1.045/ 15 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  50   |     603|        2.75|   1.071/ 10|   1.066/ 10|   1.064/ 11|   1.063/ 11 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  58   |     231|       54.66|   1.032/ 21|   1.026/ 27|   1.024/ 28|   1.023/ 30 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  48   |      10|        1.44|   1.011/ 65|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  49   |    1713|       53.30|   1.079/  9|   1.068/ 10|   1.065/ 10|   1.063/ 11 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  96   |     805|        7.42|   1.025/ 27|   1.019/ 37|   1.017/ 40|   1.016/ 44 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  57   |     808|       21.05|   1.037/ 19|   1.026/ 27|   1.023/ 30|   1.020/ 35 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  52   |    1145|      111.46|   1.022/ 31|   1.015/ 46|   1.013/ 52|   1.012/ 60 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  41   |      12|        4.53|   1.018/ 38|   1.016/ 44|   1.015/ 46|   1.014/ 49 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  47   |     909|       46.85|   1.036/ 19|   1.031/ 22|   1.029/ 24|   1.028/ 25 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  50   |    1769|       12.06|   1.082/  8|   1.063/ 11|   1.059/ 12|   1.054/ 13 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  45   |     218|        6.37|   1.044/ 16|   1.041/ 17|   1.041/ 17|   1.040/ 17 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  37   |      12|        0.73|   1.048/ 14|   1.051/ 13|   1.053/ 13|   1.056/ 12 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  49   |     214|       30.66|   1.013/ 52|   1.017/ 42|   1.018/ 39|   1.019/ 37 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  15   |      16|        2.04|   1.187/  4|   1.135/  5|   1.179/  4|   1.221/  3 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  48   |      20|        3.51|   1.039/ 18|   1.043/ 16|   1.044/ 15|   1.045/ 15 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  41   |      27|        5.02|   1.037/ 18|   1.019/ 35|   1.015/ 47|   1.010/ 70 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  55   |     102|       48.78|   1.018/ 39|   1.013/ 54|   1.012/ 59|   1.011/ 65 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  30   |      42|        2.63|   1.063/ 11|   1.062/ 11|   1.064/ 11|   1.068/ 10 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  42   |     163|        2.78|   1.061/ 11|   1.059/ 12|   1.058/ 12|   1.058/ 12 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  66   |   26922|      571.60|   1.012/ 58|   1.008/ 84|   1.007/ 95|   1.006/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  41   |       9|        0.39|   1.018/ 38|   1.038/ 18|   1.044/ 16|   1.049/ 14 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  56   |      59|        1.38|   1.102/  7|   1.103/  7|   1.103/  7|   1.103/  7 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  58   |    3202|      309.76|   1.033/ 21|   1.021/ 33|   1.018/ 38|   1.015/ 46 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  64   |    1912|      222.18|   1.012/ 57|   1.006/ **|   1.004/ **|   1.002/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  40   |       3|        0.17|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  38   |      18|        0.32|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  68   |      58|        0.86|   1.007/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  42   |      10|        1.31|   1.013/ 52|   1.010/ 71|   1.008/ 82|   1.007/ 99 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  44   |       8|        5.87|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  50   |      44|        3.73|   1.010/ 70|   1.011/ 60|   1.012/ 58|   1.012/ 57 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  52   |    3847|       46.27|   1.029/ 24|   1.018/ 39|   1.015/ 46|   1.012/ 56 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  69   |   82752|      251.11|   1.032/ 22|   1.018/ 39|   1.014/ 48|   1.011/ 64 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  56   |     355|        8.48|   1.047/ 15|   1.039/ 18|   1.037/ 19|   1.035/ 20 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  49   |     173|       17.49|   1.079/  9|   1.071/ 10|   1.069/ 10|   1.067/ 10 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  58   |   32815|      493.93|   1.033/ 21|   1.026/ 27|   1.024/ 29|   1.022/ 31 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  40   |      18|        5.14|   1.026/ 26|   1.005/ **|   1.000/ --|   1.000/ -- |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  42   |      11|        0.31|   1.030/ 23|   1.016/ 44|   1.012/ 55|   1.009/ 75 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  42   |      10|        0.31|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  36   |       3|        0.19|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  46   |       4|        0.27|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |

