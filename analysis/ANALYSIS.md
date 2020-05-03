# State and Country COVID-19 Analysis #
## Updated: 2020-05-03 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  50   |   26386|     1356.34|   1.029/ 24|   1.010/ 67|   1.006/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  54   |    8184|      921.36|   1.052/ 13|   1.038/ 18|   1.034/ 20|   1.031/ 22 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  45   |    4147|      415.21|   1.043/ 16|   1.033/ 21|   1.030/ 23|   1.028/ 25 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  44   |    4200|      604.42|   1.076/  9|   1.051/ 13|   1.045/ 15|   1.039/ 18 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  45   |    2786|      217.64|   1.073/  9|   1.055/ 12|   1.051/ 13|   1.047/ 15 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  47   |    2639|      208.26|   1.057/ 12|   1.046/ 15|   1.044/ 16|   1.041/ 17 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  45   |    2595|      727.87|   1.061/ 11|   1.038/ 18|   1.032/ 21|   1.026/ 26 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  60   |    2400|       60.74|   1.053/ 13|   1.040/ 17|   1.036/ 19|   1.033/ 21 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  50   |    2092|      450.06|   1.035/ 19|   1.025/ 27|   1.023/ 31|   1.020/ 35 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  56   |    1437|       66.92|   1.047/ 15|   1.035/ 20|   1.032/ 22|   1.029/ 24 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  64   |   76000|      230.62|   1.045/ 15|   1.026/ 27|   1.021/ 33|   1.016/ 44 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  72   |   29975|      497.60|   1.015/ 45|   1.011/ 63|   1.010/ 70|   1.009/ 79 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  53   |   28314|      426.18|   1.049/ 14|   1.047/ 15|   1.046/ 15|   1.046/ 15 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  61   |   25791|      547.58|   1.016/ 43|   1.011/ 61|   1.010/ 68|   1.009/ 77 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  78   |   29459|      439.19|   1.017/ 40|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  53   |    8334|      723.20|   1.030/ 23|   1.014/ 51|   1.010/ 71|   1.006/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  55   |    7326|       88.10|   1.033/ 21|   1.020/ 34|   1.017/ 40|   1.014/ 49 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  47   |    6964|       32.94|   1.085/  8|   1.082/  8|   1.081/  8|   1.080/  8 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  73   |    6370|       76.39|   1.014/ 48|   1.011/ 65|   1.010/ 71|   1.009/ 78 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  58   |    5234|      299.81|   1.025/ 27|   1.018/ 39|   1.016/ 44|   1.014/ 49 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  39   |     293|       59.86|   1.050/ 14|   1.047/ 15|   1.046/ 15|   1.046/ 15 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  39   |       9|       12.30|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  43   |     348|       47.86|   1.050/ 14|   1.037/ 19|   1.034/ 21|   1.030/ 23 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  40   |      67|       22.13|   1.043/ 16|   1.054/ 13|   1.057/ 12|   1.059/ 12 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  60   |    2400|       60.74|   1.053/ 13|   1.040/ 17|   1.036/ 19|   1.033/ 21 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  50   |     910|      157.95|   1.053/ 13|   1.043/ 16|   1.039/ 17|   1.036/ 19 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  45   |    2595|      727.87|   1.061/ 11|   1.038/ 18|   1.032/ 21|   1.026/ 26 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  38   |     175|      179.43|   1.074/  9|   1.063/ 11|   1.060/ 11|   1.057/ 12 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  56   |    1437|       66.92|   1.047/ 15|   1.035/ 20|   1.032/ 22|   1.029/ 24 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  52   |    1243|      117.09|   1.044/ 16|   1.035/ 20|   1.033/ 21|   1.031/ 23 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  33   |      17|       12.17|   1.050/ 14|   1.024/ 29|   1.017/ 42|   1.008/ 83 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  38   |      65|       36.30|   1.029/ 24|   1.020/ 35|   1.017/ 40|   1.015/ 46 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  47   |    2639|      208.26|   1.057/ 12|   1.046/ 15|   1.044/ 16|   1.041/ 17 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  48   |    1170|      173.78|   1.062/ 11|   1.062/ 11|   1.063/ 11|   1.063/ 11 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  39   |     180|       57.12|   1.072/  9|   1.071/ 10|   1.071/ 10|   1.071/ 10 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  51   |     150|       51.57|   1.036/ 19|   1.020/ 35|   1.016/ 44|   1.012/ 59 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  48   |     265|       59.29|   1.042/ 16|   1.030/ 23|   1.027/ 25|   1.024/ 29 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  50   |    2092|      450.06|   1.035/ 19|   1.025/ 27|   1.023/ 31|   1.020/ 35 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  37   |      58|       43.37|   1.045/ 15|   1.024/ 29|   1.018/ 38|   1.012/ 56 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  45   |    1339|      221.49|   1.076/  9|   1.048/ 14|   1.041/ 17|   1.034/ 20 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  44   |    4200|      604.42|   1.076/  9|   1.051/ 13|   1.045/ 15|   1.039/ 18 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  45   |    4147|      415.21|   1.043/ 16|   1.033/ 21|   1.030/ 23|   1.028/ 25 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  43   |     418|       74.03|   1.091/  7|   1.074/  9|   1.069/ 10|   1.065/ 11 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  45   |     293|       98.50|   1.049/ 14|   1.040/ 17|   1.037/ 18|   1.035/ 19 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  45   |     393|       64.06|   1.052/ 13|   1.041/ 17|   1.039/ 18|   1.036/ 19 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  37   |      17|       15.73|   1.043/ 16|   1.018/ 39|   1.012/ 59|   1.006/ ** |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  36   |      77|       39.70|   1.082/  8|   1.066/ 10|   1.062/ 11|   1.059/ 12 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  48   |     259|       84.19|   1.040/ 17|   1.037/ 19|   1.036/ 19|   1.035/ 20 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  41   |      80|       59.02|   1.060/ 11|   1.068/ 10|   1.071/ 10|   1.073/  9 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  54   |    8184|      921.36|   1.052/ 13|   1.038/ 18|   1.034/ 20|   1.031/ 22 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  39   |     142|       67.62|   1.080/  8|   1.065/ 10|   1.061/ 11|   1.058/ 12 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  50   |   26386|     1356.34|   1.029/ 24|   1.010/ 67|   1.006/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  39   |     449|       42.85|   1.065/ 10|   1.048/ 14|   1.044/ 16|   1.040/ 17 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  37   |      24|       31.20|   1.064/ 11|   1.053/ 13|   1.050/ 14|   1.047/ 14 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  44   |    1067|       91.25|   1.065/ 11|   1.058/ 12|   1.057/ 12|   1.055/ 12 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  45   |     242|       61.23|   1.040/ 17|   1.032/ 21|   1.030/ 23|   1.028/ 24 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  49   |     110|       26.18|   1.033/ 21|   1.027/ 25|   1.026/ 27|   1.024/ 28 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  45   |    2786|      217.64|   1.073/  9|   1.055/ 12|   1.051/ 13|   1.047/ 15 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  43   |      99|       30.85|   1.037/ 19|   1.032/ 22|   1.030/ 23|   1.028/ 24 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  36   |     296|      279.27|   1.056/ 12|   1.047/ 15|   1.045/ 15|   1.043/ 16 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  48   |     259|       50.28|   1.065/ 10|   1.076/  9|   1.079/  9|   1.082/  8 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  53   |      16|       17.86|   1.050/ 14|   1.058/ 12|   1.060/ 11|   1.061/ 11 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  43   |     211|       30.83|   1.028/ 24|   1.024/ 28|   1.024/ 29|   1.023/ 30 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  47   |     872|       30.08|   1.049/ 14|   1.043/ 16|   1.042/ 16|   1.041/ 17 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  42   |      51|       15.93|   1.051/ 13|   1.031/ 22|   1.025/ 27|   1.020/ 34 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  44   |      52|       83.41|   1.026/ 27|   1.018/ 39|   1.016/ 44|   1.014/ 51 |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  50   |     651|       76.32|   1.067/ 10|   1.052/ 13|   1.048/ 14|   1.045/ 15 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  64   |     873|      114.58|   1.023/ 31|   1.017/ 42|   1.015/ 46|   1.014/ 50 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  34   |      47|       26.36|   1.070/ 10|   1.055/ 13|   1.052/ 13|   1.051/ 14 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  44   |     337|       57.93|   1.034/ 20|   1.030/ 23|   1.029/ 24|   1.028/ 24 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  20   |       7|       12.09|   1.021/ 32|   1.000/ --|   1.000/ **|   1.000/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  42   |      73|        2.26|   1.062/ 11|   1.061/ 11|   1.061/ 11|   1.060/ 11 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  53   |      31|       10.88|   1.015/ 45|   1.017/ 40|   1.018/ 39|   1.018/ 38 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  52   |     471|       10.96|   1.017/ 40|   1.010/ 69|   1.008/ 82|   1.007/ ** |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  35   |       2|        0.06|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  56   |     247|        5.50|   1.045/ 15|   1.037/ 18|   1.036/ 19|   1.034/ 20 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  38   |      34|       11.54|   1.039/ 18|   1.030/ 23|   1.028/ 24|   1.026/ 27 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  63   |      96|        3.73|   1.026/ 27|   1.024/ 29|   1.023/ 29|   1.023/ 30 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  52   |     622|       69.87|   1.022/ 31|   1.014/ 48|   1.012/ 55|   1.010/ 66 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  51   |      26|        2.57|   1.031/ 22|   1.021/ 34|   1.018/ 38|   1.016/ 43 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  48   |       8|        5.38|   1.009/ 74|   1.004/ **|   1.002/ **|   1.001/ ** |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  46   |     196|        1.16|   1.062/ 11|   1.026/ 26|   1.017/ 39|   1.009/ 79 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  33   |      98|       10.43|   1.057/ 12|   1.054/ 13|   1.054/ 13|   1.053/ 13 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  53   |    8334|      723.20|   1.030/ 23|   1.014/ 51|   1.010/ 71|   1.006/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  27   |       1|        0.09|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  35   |      68|        5.94|   1.059/ 12|   1.054/ 13|   1.052/ 13|   1.051/ 14 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  43   |      72|       21.75|   1.033/ 21|   1.035/ 20|   1.035/ 20|   1.036/ 19 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  33   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  47   |    6964|       32.94|   1.085/  8|   1.082/  8|   1.081/  8|   1.080/  8 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  53   |      72|       10.32|   1.041/ 17|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  46   |      45|        2.17|   1.017/ 41|   1.007/ 94|   1.005/ **|   1.003/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  20   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  39   |      69|        2.58|   1.061/ 11|   1.027/ 25|   1.019/ 36|   1.011/ 63 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  55   |    4082|      107.43|   1.072/  9|   1.052/ 13|   1.047/ 15|   1.041/ 17 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  42   |     251|       13.12|   1.052/ 13|   1.042/ 16|   1.040/ 17|   1.038/ 18 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  53   |    4669|        3.33|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  42   |     326|        6.59|   1.051/ 13|   1.046/ 15|   1.045/ 15|   1.045/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  45   |       6|        1.27|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  45   |      76|       18.69|   1.051/ 13|   1.047/ 15|   1.046/ 15|   1.046/ 15 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  46   |      71|        6.29|   1.056/ 12|   1.040/ 17|   1.036/ 19|   1.032/ 22 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  50   |     481|       82.53|   1.023/ 29|   1.018/ 38|   1.017/ 41|   1.016/ 44 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  47   |     325|       31.38|   1.029/ 24|   1.022/ 31|   1.020/ 34|   1.019/ 37 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  50   |    1037|       59.37|   1.077/  9|   1.100/  7|   1.106/  6|   1.112/  6 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  56   |     434|        4.32|   1.048/ 14|   1.041/ 17|   1.040/ 17|   1.038/ 18 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  33   |      10|        1.59|   1.030/ 23|   1.053/ 13|   1.059/ 12|   1.066/ 10 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  11   |       1|        0.74|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  28   |       3|        0.03|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  43   |     250|       45.22|   1.048/ 14|   1.028/ 24|   1.023/ 30|   1.018/ 39 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  78   |   29459|      439.19|   1.017/ 40|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  44   |       4|        2.04|   1.186/  4|   1.074/  9|   1.040/ 17|   1.004/ ** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  41   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  29   |       7|        1.96|   1.050/ 14|   1.049/ 14|   1.050/ 14|   1.052/ 13 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  55   |    7326|       88.10|   1.033/ 21|   1.020/ 34|   1.017/ 40|   1.014/ 49 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  43   |      18|        0.58|   1.058/ 12|   1.080/  9|   1.085/  8|   1.091/  7 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  53   |     147|       13.75|   1.018/ 38|   1.014/ 51|   1.012/ 56|   1.011/ 62 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  48   |      19|        1.17|   1.070/ 10|   1.051/ 13|   1.046/ 15|   1.040/ 17 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  18   |       7|        0.57|   1.042/ 16|   1.002/ **|   1.000/ --|   1.000/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  28   |       8|        0.70|   1.072/  9|   1.070/ 10|   1.077/  9|   1.085/  8 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  38   |      77|        8.40|   1.046/ 15|   1.049/ 14|   1.050/ 14|   1.050/ 14 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  49   |     356|       36.45|   1.051/ 13|   1.032/ 21|   1.027/ 25|   1.023/ 31 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  53   |    1323|        0.97|   1.070/ 10|   1.064/ 11|   1.063/ 11|   1.062/ 11 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  53   |     878|        3.29|   1.032/ 22|   1.018/ 39|   1.014/ 48|   1.011/ 63 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  73   |    6370|       76.39|   1.014/ 48|   1.011/ 65|   1.010/ 71|   1.009/ 78 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  60   |      94|        2.41|   1.012/ 58|   1.012/ 60|   1.012/ 60|   1.012/ 60 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  53   |    1472|      299.19|   1.058/ 12|   1.041/ 17|   1.036/ 19|   1.031/ 22 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  43   |     232|       25.27|   1.028/ 25|   1.017/ 40|   1.015/ 47|   1.013/ 54 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  72   |   29975|      497.60|   1.015/ 45|   1.011/ 63|   1.010/ 70|   1.009/ 79 |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  45   |       8|        3.03|   1.037/ 19|   1.034/ 20|   1.033/ 21|   1.032/ 21 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  80   |     544|        4.32|   1.063/ 11|   1.058/ 12|   1.057/ 12|   1.055/ 12 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  37   |       8|        0.78|   1.015/ 47|   1.030/ 23|   1.034/ 20|   1.038/ 18 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  39   |      27|        1.44|   1.029/ 24|   1.010/ 69|   1.004/ **|   1.000/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  38   |      18|        0.39|   1.032/ 21|   1.066/ 10|   1.076/  9|   1.086/  8 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  38   |      19|       10.38|   1.055/ 12|   1.141/  5|   1.162/  4|   1.184/  4 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  29   |      33|        7.36|   1.121/  6|   1.087/  8|   1.080/  9|   1.073/  9 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  30   |       8|        1.24|   1.024/ 29|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  30   |      16|        8.63|   1.047/ 15|   1.046/ 15|   1.047/ 15|   1.047/ 14 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  54   |      25|        3.64|   1.010/ 66|   1.011/ 65|   1.011/ 66|   1.010/ 66 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  29   |      19|        4.30|   1.093/  7|   1.085/  8|   1.079/  9|   1.072/  9 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  31   |       3|        0.44|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  43   |      47|       16.78|   1.023/ 29|   1.015/ 46|   1.013/ 53|   1.011/ 62 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  47   |     105|        3.20|   1.013/ 55|   1.009/ 78|   1.008/ 86|   1.007/ 97 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  35   |      28|        1.38|   1.046/ 15|   1.031/ 22|   1.027/ 26|   1.022/ 32 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  34   |       1|        0.25|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  45   |    2291|       18.10|   1.097/  7|   1.078/  9|   1.073/  9|   1.068/ 10 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  46   |     131|       48.75|   1.058/ 12|   1.045/ 15|   1.042/ 16|   1.039/ 18 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  54   |     178|        4.96|   1.017/ 40|   1.012/ 58|   1.011/ 65|   1.009/ 74 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  58   |    5234|      299.81|   1.025/ 27|   1.018/ 39|   1.016/ 44|   1.014/ 49 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  35   |      21|        4.23|   1.034/ 20|   1.013/ 52|   1.008/ 89|   1.002/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  37   |       3|        0.50|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  39   |      36|        1.61|   1.050/ 14|   1.038/ 18|   1.035/ 20|   1.031/ 22 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  41   |      73|        0.35|   1.111/  6|   1.124/  5|   1.128/  5|   1.132/  5 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  42   |      81|       39.01|   1.039/ 18|   1.047/ 15|   1.050/ 14|   1.052/ 13 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  50   |     223|       41.59|   1.019/ 37|   1.008/ 92|   1.005/ **|   1.002/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  33   |      12|        2.49|   1.044/ 15|   1.028/ 25|   1.024/ 29|   1.021/ 33 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  45   |     443|        2.02|   1.082/  8|   1.077/  9|   1.076/  9|   1.075/  9 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  53   |     205|       48.65|   1.041/ 17|   1.032/ 21|   1.030/ 23|   1.028/ 25 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  43   |      10|        1.39|   1.018/ 39|   1.020/ 34|   1.021/ 33|   1.022/ 31 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  44   |    1236|       38.47|   1.094/  7|   1.086/  8|   1.084/  8|   1.082/  8 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  91   |     745|        6.87|   1.030/ 23|   1.020/ 34|   1.018/ 38|   1.016/ 44 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  52   |     718|       18.71|   1.051/ 14|   1.040/ 17|   1.038/ 18|   1.035/ 20 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  47   |    1062|      103.35|   1.031/ 23|   1.022/ 31|   1.020/ 34|   1.018/ 38 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  36   |      11|        4.12|   1.024/ 29|   1.023/ 30|   1.024/ 29|   1.025/ 27 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  42   |     783|       40.36|   1.043/ 16|   1.038/ 18|   1.036/ 19|   1.035/ 20 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  45   |    1309|        8.92|   1.107/  6|   1.088/  8|   1.083/  8|   1.078/  9 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  40   |     179|        5.24|   1.048/ 14|   1.040/ 17|   1.038/ 18|   1.036/ 19 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  32   |      10|        0.62|   1.088/  8|   1.022/ 31|   1.004/ **|   1.000/ -- |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  44   |     164|       23.51|   1.038/ 18|   1.062/ 11|   1.069/ 10|   1.076/  9 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  10   |       8|        1.03|   1.587/  1|   1.205/  3|   1.205/  3|   1.260/  3 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  43   |      16|        2.80|   1.033/ 21|   1.044/ 16|   1.047/ 15|   1.050/ 14 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  36   |      25|        4.54|   1.062/ 11|   1.051/ 14|   1.047/ 14|   1.044/ 15 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  50   |      96|       45.62|   1.024/ 29|   1.016/ 42|   1.015/ 47|   1.013/ 52 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  25   |      32|        2.02|   1.196/  3|   1.060/ 11|   1.022/ 32|   1.000/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  37   |     122|        2.08|   1.064/ 11|   1.058/ 12|   1.056/ 12|   1.054/ 13 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  61   |   25791|      547.58|   1.016/ 43|   1.011/ 61|   1.010/ 68|   1.009/ 77 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  36   |       7|        0.32|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  51   |      40|        0.95|   1.108/  6|   1.125/  5|   1.130/  5|   1.134/  5 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  53   |    2904|      280.86|   1.047/ 15|   1.032/ 21|   1.029/ 24|   1.025/ 28 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  59   |    1856|      215.72|   1.020/ 35|   1.012/ 57|   1.010/ 67|   1.008/ 82 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  35   |       3|        0.17|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  33   |      16|        0.29|   1.066/ 10|   1.088/  8|   1.097/  7|   1.106/  6 |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  63   |      57|        0.86|   1.014/ 48|   1.003/ **|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  37   |       8|        1.13|   1.041/ 17|   1.074/  9|   1.084/  8|   1.094/  7 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  39   |       8|        5.87|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  45   |      41|        3.51|   1.010/ 72|   1.010/ 67|   1.011/ 64|   1.011/ 61 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  47   |    3520|       42.34|   1.043/ 16|   1.029/ 24|   1.025/ 27|   1.022/ 32 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  64   |   76000|      230.62|   1.045/ 15|   1.026/ 27|   1.021/ 33|   1.016/ 44 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  51   |     294|        7.03|   1.057/ 12|   1.047/ 15|   1.044/ 16|   1.042/ 16 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  44   |     123|       12.44|   1.087/  8|   1.085/  8|   1.084/  8|   1.083/  8 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  53   |   28314|      426.18|   1.049/ 14|   1.047/ 15|   1.046/ 15|   1.046/ 15 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  35   |      18|        5.05|   1.049/ 14|   1.041/ 17|   1.039/ 17|   1.037/ 19 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  37   |      10|        0.28|   1.053/ 13|   1.023/ 30|   1.015/ 45|   1.008/ 91 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  37   |      10|        0.31|   1.005/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  31   |       3|        0.17|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  41   |       4|        0.28|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |

