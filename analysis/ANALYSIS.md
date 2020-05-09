# State and Country COVID-19 Analysis #
## Updated: 2020-05-09 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  56   |   27187|     1397.53|   1.017/ 41|   1.009/ 76|   1.007/ 94|   1.006/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  60   |    9527|     1072.63|   1.036/ 19|   1.026/ 26|   1.024/ 29|   1.022/ 32 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  50   |    5013|      721.29|   1.048/ 14|   1.031/ 22|   1.027/ 25|   1.023/ 30 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  51   |    4620|      462.59|   1.028/ 25|   1.017/ 40|   1.015/ 47|   1.012/ 57 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  51   |    3731|      291.41|   1.059/ 12|   1.055/ 12|   1.055/ 13|   1.054/ 13 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  53   |    3291|      259.73|   1.046/ 15|   1.040/ 17|   1.039/ 18|   1.037/ 18 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  51   |    2999|      841.28|   1.039/ 18|   1.026/ 27|   1.023/ 30|   1.020/ 35 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  66   |    2828|       71.59|   1.038/ 18|   1.027/ 25|   1.025/ 28|   1.022/ 31 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  56   |    2318|      498.70|   1.025/ 28|   1.018/ 38|   1.017/ 42|   1.015/ 46 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  62   |    1703|       79.29|   1.038/ 18|   1.031/ 22|   1.030/ 23|   1.028/ 24 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  70   |   84660|      256.90|   1.030/ 23|   1.018/ 39|   1.015/ 46|   1.012/ 58 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  59   |   33502|      504.27|   1.031/ 22|   1.024/ 29|   1.022/ 31|   1.020/ 34 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  78   |   31468|      522.39|   1.011/ 62|   1.008/ 89|   1.007/ 99|   1.006/ ** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  67   |   27081|      574.96|   1.011/ 61|   1.008/ 89|   1.007/ **|   1.006/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  84   |   29403|      438.35|   1.009/ 73|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  53   |   10157|       48.04|   1.074/  9|   1.068/ 10|   1.067/ 10|   1.065/ 10 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  59   |    8806|      764.08|   1.019/ 37|   1.011/ 63|   1.009/ 76|   1.007/ 94 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  61   |    7848|       94.39|   1.021/ 32|   1.013/ 55|   1.011/ 66|   1.008/ 81 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  79   |    6729|       80.70|   1.011/ 60|   1.009/ 77|   1.008/ 83|   1.008/ 90 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  64   |    5612|      321.48|   1.017/ 41|   1.011/ 63|   1.010/ 72|   1.008/ 85 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  45   |     373|       76.01|   1.046/ 15|   1.050/ 14|   1.051/ 13|   1.052/ 13 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  45   |      10|       13.16|   1.009/ 76|   1.019/ 37|   1.021/ 32|   1.024/ 29 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  49   |     463|       63.56|   1.052/ 13|   1.057/ 12|   1.058/ 12|   1.060/ 11 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  46   |      93|       30.96|   1.049/ 14|   1.049/ 14|   1.049/ 14|   1.048/ 14 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  66   |    2828|       71.59|   1.038/ 18|   1.027/ 25|   1.025/ 28|   1.022/ 31 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  56   |    1039|      180.38|   1.036/ 19|   1.022/ 31|   1.019/ 36|   1.016/ 44 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  51   |    2999|      841.28|   1.039/ 18|   1.026/ 27|   1.023/ 30|   1.020/ 35 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  44   |     221|      227.23|   1.054/ 13|   1.039/ 18|   1.035/ 20|   1.031/ 22 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  62   |    1703|       79.29|   1.038/ 18|   1.031/ 22|   1.030/ 23|   1.028/ 24 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  58   |    1448|      136.42|   1.033/ 21|   1.027/ 26|   1.025/ 27|   1.024/ 29 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  39   |      18|       12.47|   1.022/ 31|   1.003/ **|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  44   |      69|       38.41|   1.017/ 40|   1.011/ 65|   1.009/ 76|   1.008/ 91 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  53   |    3291|      259.73|   1.046/ 15|   1.040/ 17|   1.039/ 18|   1.037/ 18 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  54   |    1485|      220.65|   1.052/ 13|   1.050/ 14|   1.050/ 14|   1.049/ 14 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  45   |     248|       78.55|   1.063/ 11|   1.057/ 12|   1.056/ 12|   1.055/ 13 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  57   |     173|       59.27|   1.029/ 24|   1.023/ 30|   1.021/ 32|   1.020/ 34 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  54   |     305|       68.37|   1.033/ 21|   1.027/ 26|   1.025/ 27|   1.024/ 29 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  56   |    2318|      498.70|   1.025/ 28|   1.018/ 38|   1.017/ 42|   1.015/ 46 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  43   |      64|       47.76|   1.027/ 26|   1.018/ 38|   1.016/ 42|   1.015/ 47 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  51   |    1637|      270.79|   1.052/ 13|   1.037/ 19|   1.033/ 21|   1.030/ 23 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  50   |    5013|      721.29|   1.048/ 14|   1.031/ 22|   1.027/ 25|   1.023/ 30 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  51   |    4620|      462.59|   1.028/ 25|   1.017/ 40|   1.015/ 47|   1.012/ 57 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  49   |     565|      100.18|   1.068/ 10|   1.052/ 13|   1.048/ 14|   1.044/ 15 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  51   |     396|      133.11|   1.053/ 13|   1.057/ 12|   1.059/ 12|   1.060/ 11 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  51   |     475|       77.39|   1.042/ 16|   1.037/ 19|   1.035/ 19|   1.034/ 20 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  43   |      17|       15.49|   1.012/ 59|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  42   |      93|       48.00|   1.050/ 14|   1.036/ 19|   1.033/ 21|   1.030/ 23 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  54   |     306|       99.44|   1.034/ 20|   1.030/ 23|   1.029/ 24|   1.028/ 24 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  47   |     113|       83.34|   1.060/ 11|   1.066/ 10|   1.067/ 10|   1.069/ 10 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  60   |    9527|     1072.63|   1.036/ 19|   1.026/ 26|   1.024/ 29|   1.022/ 32 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  45   |     191|       91.01|   1.060/ 11|   1.046/ 15|   1.043/ 16|   1.039/ 17 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  56   |   27187|     1397.53|   1.017/ 41|   1.009/ 76|   1.007/ 94|   1.006/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  45   |     539|       51.42|   1.045/ 15|   1.036/ 19|   1.034/ 21|   1.031/ 22 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  43   |      32|       42.44|   1.060/ 11|   1.066/ 10|   1.068/ 10|   1.069/ 10 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  50   |    1347|      115.20|   1.051/ 13|   1.045/ 15|   1.043/ 16|   1.042/ 16 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  51   |     272|       68.81|   1.028/ 24|   1.021/ 33|   1.019/ 36|   1.018/ 39 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  55   |     125|       29.55|   1.026/ 26|   1.023/ 30|   1.022/ 32|   1.021/ 33 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  51   |    3731|      291.41|   1.059/ 12|   1.055/ 12|   1.055/ 13|   1.054/ 13 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  49   |     108|       33.86|   1.024/ 28|   1.016/ 43|   1.014/ 49|   1.012/ 58 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  42   |     407|      384.41|   1.052/ 13|   1.052/ 13|   1.051/ 13|   1.051/ 13 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  54   |     349|       67.77|   1.051/ 14|   1.045/ 15|   1.043/ 16|   1.041/ 17 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  59   |      31|       35.25|   1.072/ 10|   1.083/  8|   1.085/  8|   1.088/  8 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  49   |     244|       35.75|   1.027/ 26|   1.027/ 26|   1.027/ 26|   1.027/ 26 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  53   |    1050|       36.23|   1.037/ 19|   1.032/ 22|   1.030/ 23|   1.029/ 24 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  48   |      62|       19.24|   1.041/ 17|   1.037/ 19|   1.036/ 19|   1.036/ 19 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  50   |      55|       88.14|   1.015/ 47|   1.008/ 90|   1.006/ **|   1.004/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  56   |     844|       98.87|   1.052/ 13|   1.042/ 16|   1.039/ 17|   1.037/ 19 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  70   |     935|      122.76|   1.017/ 42|   1.012/ 57|   1.011/ 63|   1.010/ 70 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  40   |      55|       30.47|   1.040/ 17|   1.026/ 27|   1.022/ 32|   1.017/ 40 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  50   |     387|       66.45|   1.028/ 25|   1.025/ 28|   1.024/ 28|   1.024/ 29 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  26   |       7|       12.09|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  48   |     114|        3.52|   1.070/ 10|   1.071/ 10|   1.072/  9|   1.072/  9 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  59   |      32|       11.32|   1.008/ 88|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  58   |     495|       11.51|   1.012/ 57|   1.009/ 77|   1.008/ 83|   1.008/ 91 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  41   |       2|        0.06|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  62   |     303|        6.75|   1.039/ 18|   1.034/ 20|   1.033/ 21|   1.032/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  44   |      43|       14.62|   1.037/ 19|   1.037/ 19|   1.037/ 19|   1.037/ 19 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  69   |     104|        4.07|   1.017/ 41|   1.012/ 56|   1.011/ 62|   1.010/ 69 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  58   |     642|       72.12|   1.012/ 59|   1.005/ **|   1.003/ **|   1.001/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  57   |      29|        2.85|   1.024/ 29|   1.021/ 32|   1.021/ 33|   1.021/ 34 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  54   |       8|        5.31|   1.003/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  52   |     212|        1.26|   1.033/ 21|   1.018/ 39|   1.014/ 50|   1.010/ 66 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  39   |     123|       13.04|   1.047/ 15|   1.040/ 17|   1.038/ 18|   1.036/ 19 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  59   |    8806|      764.08|   1.019/ 37|   1.011/ 63|   1.009/ 76|   1.007/ 94 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  33   |       2|        0.20|   1.157/  4|   1.039/ 17|   1.002/ **|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  41   |     105|        9.13|   1.067/ 10|   1.073/  9|   1.074/  9|   1.076/  9 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  49   |      91|       27.71|   1.039/ 18|   1.045/ 15|   1.047/ 15|   1.048/ 14 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  39   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  53   |   10157|       48.04|   1.074/  9|   1.068/ 10|   1.067/ 10|   1.065/ 10 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  59   |      89|       12.80|   1.038/ 18|   1.035/ 19|   1.035/ 20|   1.034/ 20 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  52   |      49|        2.33|   1.014/ 50|   1.012/ 57|   1.012/ 59|   1.012/ 60 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  26   |       1|        0.09|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  45   |      97|        3.65|   1.074/  9|   1.108/  6|   1.117/  6|   1.127/  5 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  61   |    5118|      134.70|   1.052/ 13|   1.038/ 18|   1.034/ 20|   1.031/ 23 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  11   |      29|        1.81|   1.310/  2|   1.193/  3|   1.187/  4|   1.181/  4 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  48   |     308|       16.11|   1.040/ 17|   1.031/ 22|   1.029/ 23|   1.027/ 25 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  59   |    4637|        3.31|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  48   |     431|        8.72|   1.048/ 14|   1.048/ 14|   1.048/ 14|   1.048/ 14 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  51   |       6|        1.21|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  51   |      93|       22.73|   1.037/ 18|   1.030/ 23|   1.028/ 24|   1.026/ 26 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  52   |      79|        7.06|   1.034/ 20|   1.019/ 37|   1.015/ 47|   1.011/ 64 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  56   |     532|       91.34|   1.019/ 36|   1.016/ 43|   1.015/ 45|   1.015/ 47 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  53   |     381|       36.75|   1.027/ 25|   1.026/ 27|   1.026/ 27|   1.026/ 27 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  56   |    1877|      107.43|   1.073/  9|   1.074/  9|   1.074/  9|   1.074/  9 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  62   |     522|        5.21|   1.038/ 18|   1.032/ 22|   1.030/ 23|   1.029/ 24 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  39   |      16|        2.48|   1.058/ 12|   1.073/  9|   1.076/  9|   1.080/  9 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  17   |       5|        3.47|   1.206/  3|   1.442/  1|   1.442/  1|   1.442/  1 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  34   |       3|        0.03|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  49   |     273|       49.43|   1.032/ 22|   1.023/ 30|   1.021/ 32|   1.019/ 35 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  84   |   29403|      438.35|   1.009/ 73|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  50   |       1|        0.46|   1.092/  7|   1.121/  6|   1.128/  5|   1.135/  5 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  47   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  35   |      10|        2.74|   1.051/ 13|   1.041/ 17|   1.038/ 18|   1.034/ 20 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  61   |    7848|       94.39|   1.021/ 32|   1.013/ 55|   1.011/ 66|   1.008/ 81 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  49   |      21|        0.69|   1.023/ 29|   1.013/ 53|   1.010/ 71|   1.006/ ** |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  59   |     154|       14.38|   1.012/ 59|   1.007/ 99|   1.006/ **|   1.005/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  54   |      24|        1.47|   1.059/ 12|   1.047/ 15|   1.045/ 15|   1.042/ 16 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  24   |      12|        0.96|   1.027/ 26|   1.069/ 10|   1.075/  9|   1.079/  9 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  13   |       2|        1.39|   1.000/ --|   1.260/  2|   1.260/  2|   1.260/  2 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  34   |      13|        1.14|   1.074/  9|   1.072/  9|   1.070/ 10|   1.068/ 10 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  44   |     107|       11.67|   1.053/ 13|   1.058/ 12|   1.060/ 11|   1.061/ 11 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  55   |     409|       41.89|   1.035/ 20|   1.024/ 29|   1.021/ 33|   1.019/ 37 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  59   |    2010|        1.48|   1.071/ 10|   1.071/ 10|   1.071/ 10|   1.071/ 10 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  59   |     965|        3.62|   1.024/ 29|   1.018/ 39|   1.016/ 43|   1.015/ 47 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  79   |    6729|       80.70|   1.011/ 60|   1.009/ 77|   1.008/ 83|   1.008/ 90 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  66   |     103|        2.64|   1.014/ 50|   1.015/ 47|   1.015/ 46|   1.015/ 45 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  59   |    1606|      326.40|   1.032/ 21|   1.014/ 50|   1.009/ 77|   1.004/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  49   |     250|       27.18|   1.017/ 41|   1.012/ 60|   1.010/ 67|   1.009/ 76 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  78   |   31468|      522.39|   1.011/ 62|   1.008/ 89|   1.007/ 99|   1.006/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  51   |      10|        3.53|   1.028/ 25|   1.019/ 37|   1.017/ 42|   1.014/ 48 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  86   |     708|        5.62|   1.049/ 14|   1.040/ 17|   1.038/ 18|   1.036/ 19 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  43   |       9|        0.88|   1.018/ 39|   1.014/ 48|   1.013/ 53|   1.011/ 60 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  45   |      31|        1.65|   1.025/ 27|   1.022/ 31|   1.022/ 32|   1.022/ 32 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  44   |      29|        0.62|   1.051/ 14|   1.066/ 10|   1.070/ 10|   1.073/  9 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  44   |      30|       16.82|   1.021/ 34|   1.032/ 22|   1.034/ 20|   1.037/ 18 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  35   |      49|       11.17|   1.084/  8|   1.063/ 11|   1.057/ 12|   1.051/ 13 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  36   |      12|        1.86|   1.036/ 19|   1.062/ 11|   1.068/ 10|   1.074/  9 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  36   |      18|        9.66|   1.034/ 21|   1.023/ 29|   1.021/ 33|   1.018/ 39 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  60   |      26|        3.81|   1.008/ 83|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  35   |      21|        4.77|   1.063/ 11|   1.021/ 33|   1.011/ 64|   1.001/ ** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  37   |       3|        0.48|   1.145/  5|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  49   |      50|       17.73|   1.015/ 45|   1.012/ 57|   1.011/ 61|   1.011/ 65 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  53   |     109|        3.33|   1.009/ 79|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  41   |      34|        1.68|   1.038/ 18|   1.037/ 18|   1.038/ 18|   1.038/ 18 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  40   |       1|        0.25|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  51   |    3243|       25.62|   1.077/  9|   1.068/ 10|   1.065/ 10|   1.063/ 11 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  52   |     157|       58.50|   1.042/ 16|   1.033/ 21|   1.031/ 23|   1.028/ 24 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  60   |     189|        5.28|   1.013/ 52|   1.010/ 67|   1.010/ 71|   1.009/ 77 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  64   |    5612|      321.48|   1.017/ 41|   1.011/ 63|   1.010/ 72|   1.008/ 85 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  41   |      21|        4.30|   1.014/ 49|   1.010/ 69|   1.009/ 75|   1.008/ 82 |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  43   |       5|        0.83|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  45   |      43|        1.94|   1.039/ 17|   1.033/ 21|   1.032/ 22|   1.030/ 23 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  47   |     128|        0.62|   1.094/  7|   1.084/  8|   1.081/  8|   1.077/  9 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  48   |      95|       45.94|   1.031/ 22|   1.024/ 28|   1.022/ 31|   1.020/ 35 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  56   |     225|       41.90|   1.009/ 77|   1.002/ **|   1.000/ **|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  39   |      15|        3.17|   1.036/ 19|   1.048/ 14|   1.051/ 13|   1.055/ 12 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  51   |     634|        2.89|   1.069/ 10|   1.063/ 11|   1.061/ 11|   1.059/ 12 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  59   |     236|       55.94|   1.032/ 22|   1.026/ 26|   1.025/ 28|   1.024/ 29 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  49   |      10|        1.44|   1.009/ 75|   1.005/ **|   1.003/ **|   1.002/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  50   |    1818|       56.60|   1.076/  9|   1.065/ 10|   1.063/ 11|   1.060/ 11 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  97   |     812|        7.48|   1.025/ 27|   1.019/ 36|   1.018/ 39|   1.016/ 43 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  58   |     828|       21.57|   1.035/ 20|   1.024/ 28|   1.022/ 32|   1.019/ 37 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  53   |    1156|      112.49|   1.021/ 34|   1.014/ 50|   1.012/ 57|   1.010/ 67 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  42   |      13|        4.55|   1.016/ 44|   1.012/ 57|   1.011/ 64|   1.009/ 74 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  48   |     937|       48.30|   1.035/ 20|   1.030/ 23|   1.029/ 24|   1.028/ 25 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  51   |    1858|       12.66|   1.078/  9|   1.060/ 11|   1.056/ 12|   1.051/ 13 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  46   |     228|        6.66|   1.043/ 16|   1.042/ 16|   1.042/ 16|   1.042/ 16 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  38   |      13|        0.77|   1.047/ 15|   1.056/ 12|   1.060/ 11|   1.064/ 11 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  50   |     220|       31.53|   1.013/ 51|   1.018/ 39|   1.019/ 37|   1.020/ 35 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  16   |      18|        2.27|   1.167/  4|   1.168/  4|   1.180/  4|   1.190/  3 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  49   |      21|        3.63|   1.039/ 18|   1.042/ 16|   1.043/ 16|   1.044/ 16 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  42   |      28|        5.08|   1.034/ 20|   1.016/ 43|   1.011/ 61|   1.007/ ** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  56   |     103|       49.30|   1.016/ 43|   1.012/ 59|   1.011/ 65|   1.010/ 72 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  31   |      44|        2.79|   1.062/ 11|   1.061/ 11|   1.062/ 11|   1.064/ 11 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  43   |     174|        2.96|   1.061/ 11|   1.060/ 11|   1.060/ 11|   1.059/ 12 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  67   |   27081|      574.96|   1.011/ 61|   1.008/ 89|   1.007/ **|   1.006/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  42   |       9|        0.41|   1.014/ 51|   1.025/ 28|   1.028/ 25|   1.031/ 22 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  57   |      63|        1.48|   1.097/  7|   1.096/  7|   1.096/  7|   1.096/  7 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  59   |    3267|      316.01|   1.032/ 22|   1.022/ 32|   1.019/ 35|   1.017/ 40 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  65   |    1914|      222.47|   1.011/ 63|   1.005/ **|   1.003/ **|   1.002/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  41   |       3|        0.17|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  39   |      19|        0.34|   1.005/ **|   1.016/ 44|   1.019/ 37|   1.022/ 31 |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  69   |      57|        0.86|   1.006/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  43   |      10|        1.35|   1.015/ 47|   1.015/ 48|   1.014/ 49|   1.014/ 50 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  45   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  51   |      44|        3.79|   1.011/ 66|   1.012/ 56|   1.013/ 54|   1.013/ 53 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  53   |    3884|       46.71|   1.027/ 26|   1.016/ 43|   1.013/ 51|   1.011/ 64 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  70   |   84660|      256.90|   1.030/ 23|   1.018/ 39|   1.015/ 46|   1.012/ 58 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  57   |     369|        8.80|   1.046/ 15|   1.039/ 18|   1.037/ 18|   1.036/ 19 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  50   |     184|       18.59|   1.076/  9|   1.067/ 10|   1.065/ 11|   1.063/ 11 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  59   |   33502|      504.27|   1.031/ 22|   1.024/ 29|   1.022/ 31|   1.020/ 34 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  41   |      18|        5.17|   1.023/ 30|   1.006/ **|   1.001/ **|   1.000/ -- |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  43   |      11|        0.31|   1.026/ 27|   1.012/ 60|   1.008/ 86|   1.005/ ** |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  43   |      10|        0.31|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  37   |       4|        0.21|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  47   |       4|        0.27|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |

