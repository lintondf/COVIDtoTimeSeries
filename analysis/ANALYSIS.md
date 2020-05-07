# State and Country COVID-19 Analysis #
## Updated: 2020-05-07 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  53   |   26539|     1364.24|   1.021/ 33|   1.008/ 85|   1.005/ **|   1.002/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  57   |    8813|      992.22|   1.041/ 17|   1.028/ 25|   1.024/ 28|   1.021/ 33 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  47   |    4594|      661.07|   1.060/ 11|   1.037/ 19|   1.031/ 22|   1.025/ 27 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  48   |    4425|      443.13|   1.035/ 20|   1.024/ 29|   1.021/ 33|   1.018/ 38 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  48   |    3182|      248.55|   1.059/ 12|   1.045/ 15|   1.042/ 16|   1.039/ 17 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  50   |    2937|      231.80|   1.048/ 14|   1.038/ 18|   1.035/ 20|   1.033/ 21 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  48   |    2802|      785.85|   1.047/ 15|   1.028/ 24|   1.024/ 29|   1.019/ 36 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  63   |    2603|       65.88|   1.044/ 16|   1.030/ 23|   1.027/ 26|   1.023/ 30 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  53   |    2198|      472.86|   1.029/ 24|   1.019/ 36|   1.017/ 41|   1.015/ 47 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  59   |    1550|       72.16|   1.039/ 18|   1.028/ 25|   1.025/ 28|   1.022/ 31 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  67   |   79820|      242.21|   1.035/ 20|   1.018/ 38|   1.014/ 49|   1.010/ 69 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  56   |   31202|      469.65|   1.038/ 18|   1.032/ 22|   1.030/ 23|   1.029/ 24 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  75   |   30705|      509.73|   1.013/ 54|   1.009/ 78|   1.008/ 88|   1.007/ ** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  64   |   26520|      563.06|   1.014/ 51|   1.009/ 73|   1.008/ 82|   1.007/ 93 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  81   |   29198|      435.30|   1.012/ 59|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  56   |    8550|      741.93|   1.021/ 32|   1.009/ 76|   1.006/ **|   1.003/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  50   |    8392|       39.70|   1.076/  9|   1.067/ 10|   1.065/ 11|   1.063/ 11 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  58   |    7597|       91.37|   1.025/ 28|   1.013/ 54|   1.010/ 71|   1.007/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  76   |    6559|       78.66|   1.013/ 55|   1.009/ 73|   1.009/ 80|   1.008/ 88 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  61   |    5430|      311.03|   1.021/ 33|   1.014/ 50|   1.012/ 57|   1.011/ 66 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  42   |     321|       65.48|   1.042/ 16|   1.034/ 21|   1.031/ 22|   1.029/ 23 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  42   |       9|       12.30|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  46   |     390|       53.59|   1.046/ 15|   1.039/ 18|   1.037/ 18|   1.036/ 19 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  43   |      81|       27.00|   1.052/ 13|   1.064/ 11|   1.067/ 10|   1.070/ 10 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  63   |    2603|       65.88|   1.044/ 16|   1.030/ 23|   1.027/ 26|   1.023/ 30 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  53   |     976|      169.41|   1.043/ 16|   1.029/ 24|   1.025/ 28|   1.021/ 33 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  48   |    2802|      785.85|   1.047/ 15|   1.028/ 24|   1.024/ 29|   1.019/ 36 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  41   |     199|      204.62|   1.065/ 11|   1.050/ 14|   1.046/ 15|   1.042/ 16 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  59   |    1550|       72.16|   1.039/ 18|   1.028/ 25|   1.025/ 28|   1.022/ 31 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  55   |    1340|      126.16|   1.037/ 19|   1.027/ 25|   1.025/ 27|   1.023/ 30 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  36   |      18|       12.55|   1.036/ 19|   1.015/ 45|   1.010/ 70|   1.004/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  41   |      67|       37.34|   1.023/ 31|   1.013/ 55|   1.010/ 68|   1.008/ 88 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  50   |    2937|      231.80|   1.048/ 14|   1.038/ 18|   1.035/ 20|   1.033/ 21 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  51   |    1289|      191.51|   1.048/ 14|   1.039/ 18|   1.036/ 19|   1.034/ 21 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  42   |     211|       66.90|   1.065/ 10|   1.058/ 12|   1.056/ 12|   1.053/ 13 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  54   |     162|       55.48|   1.032/ 21|   1.024/ 29|   1.022/ 32|   1.020/ 35 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  51   |     282|       63.13|   1.035/ 20|   1.024/ 29|   1.021/ 32|   1.019/ 37 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  53   |    2198|      472.86|   1.029/ 24|   1.019/ 36|   1.017/ 41|   1.015/ 47 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  40   |      61|       45.54|   1.034/ 20|   1.018/ 38|   1.015/ 47|   1.011/ 61 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  48   |    1493|      246.98|   1.063/ 11|   1.040/ 17|   1.034/ 20|   1.029/ 24 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  47   |    4594|      661.07|   1.060/ 11|   1.037/ 19|   1.031/ 22|   1.025/ 27 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  48   |    4425|      443.13|   1.035/ 20|   1.024/ 29|   1.021/ 33|   1.018/ 38 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  46   |     492|       87.17|   1.078/  9|   1.059/ 12|   1.054/ 13|   1.049/ 14 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  48   |     333|      111.77|   1.046/ 15|   1.042/ 16|   1.042/ 16|   1.041/ 17 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  48   |     427|       69.62|   1.043/ 16|   1.031/ 22|   1.028/ 25|   1.025/ 28 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  40   |      17|       15.76|   1.023/ 31|   1.006/ **|   1.003/ **|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  39   |      85|       43.71|   1.065/ 11|   1.041/ 17|   1.036/ 19|   1.031/ 22 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  51   |     281|       91.07|   1.035/ 20|   1.029/ 24|   1.027/ 25|   1.026/ 27 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  44   |      94|       68.81|   1.056/ 12|   1.055/ 13|   1.054/ 13|   1.054/ 13 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  57   |    8813|      992.22|   1.041/ 17|   1.028/ 25|   1.024/ 28|   1.021/ 33 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  42   |     169|       80.46|   1.072/  9|   1.061/ 11|   1.058/ 12|   1.056/ 12 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  53   |   26539|     1364.24|   1.021/ 33|   1.008/ 85|   1.005/ **|   1.002/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  42   |     490|       46.69|   1.050/ 14|   1.033/ 21|   1.029/ 24|   1.025/ 28 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  40   |      27|       35.08|   1.057/ 12|   1.045/ 15|   1.043/ 16|   1.040/ 17 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  47   |    1183|      101.24|   1.052/ 13|   1.040/ 17|   1.037/ 19|   1.033/ 21 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  48   |     257|       65.05|   1.032/ 21|   1.022/ 31|   1.020/ 35|   1.017/ 40 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  52   |     117|       27.72|   1.027/ 25|   1.021/ 33|   1.019/ 36|   1.017/ 40 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  48   |    3182|      248.55|   1.059/ 12|   1.045/ 15|   1.042/ 16|   1.039/ 17 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  46   |     104|       32.55|   1.030/ 23|   1.021/ 33|   1.018/ 38|   1.016/ 44 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  39   |     351|      331.03|   1.055/ 12|   1.057/ 12|   1.057/ 12|   1.058/ 12 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  51   |     308|       59.74|   1.059/ 12|   1.060/ 11|   1.060/ 11|   1.060/ 11 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  56   |      23|       25.88|   1.051/ 13|   1.056/ 12|   1.057/ 12|   1.059/ 12 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  46   |     226|       33.01|   1.026/ 27|   1.023/ 29|   1.023/ 30|   1.022/ 31 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  50   |     962|       33.18|   1.041/ 17|   1.035/ 20|   1.033/ 21|   1.031/ 22 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  45   |      55|       17.16|   1.042/ 16|   1.028/ 24|   1.025/ 27|   1.022/ 31 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  47   |      54|       86.60|   1.021/ 33|   1.015/ 47|   1.013/ 52|   1.012/ 59 |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  53   |     748|       87.60|   1.061/ 11|   1.050/ 14|   1.047/ 15|   1.044/ 15 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  67   |     902|      118.40|   1.018/ 38|   1.012/ 58|   1.010/ 66|   1.009/ 77 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  37   |      51|       28.72|   1.054/ 13|   1.037/ 19|   1.033/ 21|   1.029/ 24 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  47   |     360|       61.83|   1.029/ 24|   1.024/ 29|   1.023/ 31|   1.021/ 32 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  23   |       7|       12.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  45   |      93|        2.87|   1.071/ 10|   1.081/  8|   1.083/  8|   1.086/  8 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  56   |      32|       11.19|   1.012/ 60|   1.010/ 67|   1.010/ 70|   1.010/ 73 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  55   |     481|       11.20|   1.014/ 51|   1.008/ 84|   1.007/ 99|   1.006/ ** |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  38   |       2|        0.06|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  59   |     275|        6.11|   1.043/ 16|   1.038/ 18|   1.036/ 19|   1.035/ 20 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  41   |      39|       13.08|   1.039/ 18|   1.040/ 17|   1.041/ 17|   1.042/ 16 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  66   |     101|        3.94|   1.022/ 31|   1.019/ 36|   1.019/ 37|   1.018/ 38 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  55   |     634|       71.24|   1.016/ 42|   1.009/ 80|   1.007/ **|   1.005/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  54   |      27|        2.69|   1.024/ 29|   1.016/ 43|   1.014/ 48|   1.013/ 54 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  51   |       8|        5.35|   1.006/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  49   |     201|        1.19|   1.043/ 16|   1.015/ 45|   1.009/ 80|   1.002/ ** |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  36   |     110|       11.70|   1.052/ 13|   1.043/ 16|   1.040/ 17|   1.037/ 19 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  56   |    8550|      741.93|   1.021/ 32|   1.009/ 76|   1.006/ **|   1.003/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  30   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  38   |      84|        7.36|   1.064/ 11|   1.071/ 10|   1.073/  9|   1.075/  9 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  46   |      80|       24.19|   1.034/ 20|   1.036/ 19|   1.036/ 19|   1.037/ 19 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  36   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  50   |    8392|       39.70|   1.076/  9|   1.067/ 10|   1.065/ 11|   1.063/ 11 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  56   |      80|       11.55|   1.040/ 17|   1.038/ 18|   1.038/ 18|   1.038/ 18 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  49   |      47|        2.25|   1.016/ 45|   1.012/ 58|   1.011/ 62|   1.010/ 66 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  23   |       1|        0.09|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  42   |      70|        2.62|   1.036/ 19|   1.015/ 46|   1.009/ 75|   1.003/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  58   |    4620|      121.59|   1.061/ 11|   1.043/ 16|   1.038/ 18|   1.034/ 20 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  45   |     282|       14.77|   1.047/ 14|   1.042/ 16|   1.040/ 17|   1.039/ 18 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  56   |    4891|        3.49|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  45   |     375|        7.58|   1.049/ 14|   1.048/ 14|   1.048/ 14|   1.048/ 14 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  48   |       6|        1.24|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  48   |      86|       20.99|   1.045/ 15|   1.041/ 17|   1.040/ 17|   1.039/ 18 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  49   |      75|        6.73|   1.044/ 16|   1.028/ 25|   1.024/ 29|   1.019/ 36 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  53   |     507|       87.12|   1.022/ 31|   1.019/ 36|   1.018/ 38|   1.018/ 39 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  50   |     352|       34.00|   1.029/ 24|   1.026/ 27|   1.026/ 27|   1.025/ 27 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  53   |    1514|       86.68|   1.098/  7|   1.123/  5|   1.130/  5|   1.136/  5 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  59   |     477|        4.75|   1.041/ 17|   1.034/ 20|   1.032/ 21|   1.030/ 23 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  36   |      13|        1.98|   1.045/ 15|   1.070/ 10|   1.076/  9|   1.083/  8 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  14   |       1|        0.74|   1.000/ --|   1.000/ --|   1.442/  1|   1.442/  1 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  31   |       3|        0.03|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  46   |     264|       47.71|   1.039/ 18|   1.027/ 26|   1.024/ 29|   1.021/ 33 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  81   |   29198|      435.30|   1.012/ 59|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  47   |       6|        2.82|   1.045/ 15|   1.057/ 12|   1.060/ 11|   1.063/ 11 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  44   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  32   |       9|        2.48|   1.054/ 13|   1.074/  9|   1.079/  9|   1.085/  8 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  58   |    7597|       91.37|   1.025/ 28|   1.013/ 54|   1.010/ 71|   1.007/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  46   |      20|        0.66|   1.033/ 21|   1.030/ 23|   1.029/ 24|   1.028/ 25 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  56   |     152|       14.14|   1.015/ 46|   1.010/ 68|   1.009/ 77|   1.008/ 90 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  51   |      21|        1.28|   1.058/ 12|   1.038/ 18|   1.033/ 21|   1.027/ 26 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  21   |       9|        0.75|   1.010/ 68|   1.054/ 13|   1.078/  9|   1.103/  7 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  10   |       1|        0.62|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  31   |      11|        0.96|   1.061/ 11|   1.099/  7|   1.110/  6|   1.120/  6 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  41   |      90|        9.79|   1.048/ 14|   1.051/ 13|   1.052/ 13|   1.053/ 13 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  52   |     384|       39.27|   1.041/ 17|   1.026/ 26|   1.023/ 31|   1.019/ 37 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  56   |    1635|        1.20|   1.071/ 10|   1.072/  9|   1.072/  9|   1.072/  9 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  56   |     920|        3.45|   1.026/ 26|   1.017/ 41|   1.014/ 48|   1.012/ 57 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  76   |    6559|       78.66|   1.013/ 55|   1.009/ 73|   1.009/ 80|   1.008/ 88 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  63   |      99|        2.52|   1.014/ 51|   1.015/ 47|   1.015/ 46|   1.015/ 45 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  56   |    1562|      317.42|   1.042/ 16|   1.021/ 33|   1.016/ 44|   1.010/ 68 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  46   |     243|       26.40|   1.021/ 32|   1.015/ 45|   1.014/ 49|   1.013/ 54 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  75   |   30705|      509.73|   1.013/ 54|   1.009/ 78|   1.008/ 88|   1.007/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  48   |       9|        3.37|   1.047/ 14|   1.042/ 16|   1.041/ 17|   1.039/ 17 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  83   |     629|        5.00|   1.058/ 12|   1.052/ 13|   1.051/ 14|   1.049/ 14 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  40   |       9|        0.86|   1.023/ 30|   1.034/ 20|   1.037/ 19|   1.040/ 17 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  42   |      29|        1.54|   1.028/ 25|   1.022/ 32|   1.020/ 34|   1.019/ 36 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  41   |      24|        0.51|   1.048/ 14|   1.074/  9|   1.081/  8|   1.088/  8 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  41   |      26|       14.35|   1.015/ 47|   1.032/ 21|   1.037/ 19|   1.042/ 16 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  32   |      42|        9.60|   1.100/  7|   1.093/  7|   1.092/  7|   1.091/  7 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  33   |      10|        1.52|   1.020/ 35|   1.055/ 13|   1.064/ 11|   1.075/  9 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  33   |      17|        9.09|   1.041/ 17|   1.027/ 25|   1.023/ 29|   1.019/ 36 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  57   |      26|        3.74|   1.010/ 69|   1.009/ 73|   1.009/ 75|   1.009/ 77 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  32   |      21|        4.62|   1.093/  7|   1.039/ 18|   1.023/ 29|   1.007/ 94 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  34   |       3|        0.50|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  46   |      48|       17.14|   1.017/ 42|   1.009/ 79|   1.007/ **|   1.005/ ** |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  50   |     107|        3.27|   1.011/ 64|   1.008/ 85|   1.007/ 93|   1.007/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  38   |      31|        1.51|   1.040/ 17|   1.033/ 21|   1.032/ 22|   1.031/ 22 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  37   |       1|        0.25|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  48   |    2707|       21.38|   1.078/  9|   1.061/ 11|   1.057/ 12|   1.052/ 13 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  49   |     143|       53.30|   1.047/ 15|   1.035/ 20|   1.031/ 22|   1.028/ 24 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  57   |     184|        5.12|   1.015/ 46|   1.011/ 62|   1.010/ 67|   1.009/ 74 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  61   |    5430|      311.03|   1.021/ 33|   1.014/ 50|   1.012/ 57|   1.011/ 66 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  38   |      21|        4.27|   1.026/ 27|   1.008/ 86|   1.004/ **|   1.001/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  40   |       5|        0.75|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  42   |      39|        1.76|   1.044/ 16|   1.033/ 21|   1.031/ 22|   1.028/ 25 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  44   |     102|        0.49|   1.112/  6|   1.119/  6|   1.121/  6|   1.123/  5 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  45   |      90|       43.17|   1.036/ 19|   1.036/ 19|   1.036/ 19|   1.035/ 19 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  53   |     224|       41.66|   1.013/ 54|   1.003/ **|   1.001/ **|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  36   |      13|        2.72|   1.034/ 20|   1.029/ 24|   1.028/ 24|   1.028/ 25 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  48   |     531|        2.42|   1.073/  9|   1.064/ 11|   1.062/ 11|   1.060/ 11 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  56   |     219|       51.99|   1.033/ 21|   1.023/ 30|   1.021/ 33|   1.018/ 37 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  46   |      10|        1.43|   1.014/ 50|   1.011/ 63|   1.010/ 67|   1.010/ 71 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  47   |    1514|       47.12|   1.084/  8|   1.073/  9|   1.071/ 10|   1.068/ 10 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  94   |     783|        7.21|   1.026/ 26|   1.019/ 37|   1.017/ 42|   1.015/ 47 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  55   |     774|       20.16|   1.041/ 17|   1.029/ 24|   1.026/ 26|   1.023/ 30 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  50   |    1116|      108.61|   1.025/ 27|   1.018/ 38|   1.016/ 43|   1.014/ 48 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  39   |      12|        4.43|   1.023/ 30|   1.023/ 29|   1.024/ 28|   1.025/ 27 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  45   |     859|       44.29|   1.039/ 18|   1.033/ 21|   1.032/ 22|   1.030/ 23 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  48   |    1584|       10.80|   1.090/  8|   1.069/ 10|   1.064/ 11|   1.058/ 12 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  43   |     201|        5.87|   1.044/ 15|   1.040/ 17|   1.039/ 18|   1.037/ 18 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  35   |      10|        0.64|   1.051/ 13|   1.021/ 33|   1.013/ 51|   1.007/ ** |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  47   |     198|       28.37|   1.012/ 57|   1.014/ 50|   1.015/ 47|   1.016/ 44 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  13   |      11|        1.33|   1.233/  3|   1.129/  5|   1.101/  7|   1.097/  7 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  46   |      18|        3.20|   1.038/ 18|   1.046/ 15|   1.048/ 14|   1.050/ 14 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  39   |      27|        4.89|   1.045/ 15|   1.029/ 24|   1.024/ 29|   1.020/ 35 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  53   |     100|       47.67|   1.020/ 34|   1.015/ 45|   1.014/ 48|   1.013/ 52 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  28   |      37|        2.32|   1.101/  7|   1.051/ 14|   1.044/ 16|   1.039/ 18 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  40   |     147|        2.49|   1.064/ 11|   1.062/ 11|   1.062/ 11|   1.062/ 11 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  64   |   26520|      563.06|   1.014/ 51|   1.009/ 73|   1.008/ 82|   1.007/ 93 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  39   |       7|        0.32|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  54   |      51|        1.21|   1.118/  6|   1.136/  5|   1.140/  5|   1.145/  5 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  56   |    3079|      297.83|   1.036/ 19|   1.021/ 34|   1.017/ 41|   1.013/ 53 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  62   |    1896|      220.35|   1.015/ 47|   1.007/ 92|   1.006/ **|   1.004/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  38   |       3|        0.17|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  36   |      18|        0.32|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  66   |      57|        0.86|   1.009/ 80|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  40   |      10|        1.27|   1.020/ 35|   1.019/ 36|   1.019/ 36|   1.019/ 36 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  42   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  48   |      43|        3.65|   1.010/ 70|   1.012/ 56|   1.013/ 54|   1.014/ 51 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  50   |    3737|       44.94|   1.034/ 20|   1.022/ 32|   1.018/ 38|   1.015/ 45 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  67   |   79820|      242.21|   1.035/ 20|   1.018/ 38|   1.014/ 49|   1.010/ 69 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  54   |     330|        7.89|   1.050/ 14|   1.041/ 17|   1.038/ 18|   1.036/ 19 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  47   |     152|       15.35|   1.082/  8|   1.075/  9|   1.073/  9|   1.071/ 10 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  56   |   31202|      469.65|   1.038/ 18|   1.032/ 22|   1.030/ 23|   1.029/ 24 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  38   |      18|        5.18|   1.036/ 19|   1.015/ 46|   1.009/ 75|   1.003/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  40   |      10|        0.30|   1.040/ 17|   1.025/ 27|   1.022/ 31|   1.020/ 35 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  40   |      10|        0.31|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  34   |       3|        0.17|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  44   |       4|        0.27|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |

