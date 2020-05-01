# State and Country COVID-19 Analysis #
## Updated: 2020-05-01 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  48   |   26200|     1346.79|   1.039/ 18|   1.014/ 51|   1.007/ 94|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  52   |    7627|      858.66|   1.056/ 12|   1.037/ 19|   1.032/ 22|   1.027/ 25 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  43   |    3915|      392.06|   1.048/ 14|   1.037/ 18|   1.035/ 20|   1.032/ 22 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  42   |    3860|      555.47|   1.086/  8|   1.062/ 11|   1.055/ 12|   1.048/ 14 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  43   |    2516|      196.56|   1.078/  9|   1.054/ 13|   1.048/ 14|   1.042/ 16 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  45   |    2422|      191.12|   1.061/ 11|   1.048/ 14|   1.044/ 15|   1.041/ 17 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  43   |    2439|      684.21|   1.071/ 10|   1.044/ 15|   1.037/ 18|   1.030/ 23 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  58   |    2234|       56.53|   1.058/ 12|   1.044/ 16|   1.040/ 17|   1.036/ 19 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  48   |    2002|      430.65|   1.040/ 17|   1.027/ 26|   1.024/ 29|   1.021/ 33 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  54   |    1349|       62.80|   1.051/ 13|   1.036/ 19|   1.033/ 21|   1.029/ 24 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  62   |   72631|      220.40|   1.052/ 13|   1.030/ 23|   1.024/ 29|   1.018/ 37 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  70   |   29364|      487.46|   1.017/ 40|   1.012/ 56|   1.011/ 62|   1.010/ 70 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  51   |   25851|      389.11|   1.048/ 14|   1.042/ 16|   1.041/ 17|   1.040/ 17 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  59   |   25273|      536.58|   1.018/ 38|   1.013/ 54|   1.012/ 60|   1.010/ 67 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  76   |   29421|      438.63|   1.022/ 32|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  51   |    8160|      708.10|   1.036/ 19|   1.018/ 39|   1.013/ 53|   1.009/ 81 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  53   |    7076|       85.10|   1.039/ 18|   1.025/ 27|   1.022/ 32|   1.018/ 38 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  71   |    6240|       74.84|   1.016/ 44|   1.012/ 60|   1.011/ 66|   1.010/ 73 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  45   |    5984|       28.31|   1.088/  8|   1.085/  8|   1.084/  8|   1.084/  8 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  56   |    5068|      290.34|   1.028/ 25|   1.019/ 36|   1.017/ 41|   1.014/ 48 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  37   |     268|       54.69|   1.052/ 13|   1.045/ 15|   1.043/ 16|   1.042/ 17 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  37   |       9|       12.30|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  41   |     329|       45.16|   1.054/ 13|   1.038/ 18|   1.034/ 20|   1.030/ 23 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  38   |      60|       19.72|   1.039/ 18|   1.046/ 15|   1.048/ 14|   1.050/ 14 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  58   |    2234|       56.53|   1.058/ 12|   1.044/ 16|   1.040/ 17|   1.036/ 19 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  48   |     845|      146.77|   1.060/ 11|   1.052/ 13|   1.050/ 14|   1.047/ 15 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  43   |    2439|      684.21|   1.071/ 10|   1.044/ 15|   1.037/ 18|   1.030/ 23 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  36   |     157|      160.78|   1.079/  9|   1.072/  9|   1.071/ 10|   1.069/ 10 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  54   |    1349|       62.80|   1.051/ 13|   1.036/ 19|   1.033/ 21|   1.029/ 24 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  50   |    1168|      109.97|   1.049/ 14|   1.040/ 17|   1.037/ 18|   1.035/ 20 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  31   |      17|       12.05|   1.056/ 12|   1.047/ 15|   1.044/ 15|   1.041/ 17 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  36   |      62|       34.91|   1.033/ 21|   1.023/ 30|   1.020/ 34|   1.017/ 40 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  45   |    2422|      191.12|   1.061/ 11|   1.048/ 14|   1.044/ 15|   1.041/ 17 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  46   |    1044|      155.13|   1.061/ 11|   1.057/ 12|   1.056/ 12|   1.056/ 12 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  37   |     158|       50.16|   1.073/  9|   1.073/  9|   1.073/  9|   1.073/  9 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  49   |     145|       49.76|   1.042/ 16|   1.022/ 32|   1.017/ 41|   1.012/ 60 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  46   |     252|       56.37|   1.048/ 14|   1.037/ 19|   1.034/ 20|   1.031/ 22 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  48   |    2002|      430.65|   1.040/ 17|   1.027/ 26|   1.024/ 29|   1.021/ 33 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  35   |      56|       41.95|   1.055/ 12|   1.030/ 23|   1.023/ 30|   1.016/ 44 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  43   |    1248|      206.50|   1.089/  8|   1.065/ 10|   1.058/ 12|   1.051/ 13 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  42   |    3860|      555.47|   1.086/  8|   1.062/ 11|   1.055/ 12|   1.048/ 14 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  43   |    3915|      392.06|   1.048/ 14|   1.037/ 18|   1.035/ 20|   1.032/ 22 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  41   |     367|       65.16|   1.097/  7|   1.082/  8|   1.077/  9|   1.073/  9 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  43   |     270|       90.85|   1.052/ 13|   1.036/ 19|   1.032/ 21|   1.028/ 25 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  43   |     367|       59.76|   1.058/ 12|   1.048/ 14|   1.046/ 15|   1.044/ 16 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  35   |      17|       15.44|   1.055/ 12|   1.028/ 25|   1.021/ 33|   1.014/ 50 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  34   |      69|       35.91|   1.088/  8|   1.053/ 13|   1.042/ 16|   1.031/ 22 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  46   |     243|       78.80|   1.042/ 16|   1.037/ 19|   1.036/ 19|   1.035/ 20 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  39   |      69|       50.88|   1.055/ 13|   1.041/ 17|   1.038/ 18|   1.035/ 20 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  52   |    7627|      858.66|   1.056/ 12|   1.037/ 19|   1.032/ 22|   1.027/ 25 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  37   |     126|       60.14|   1.087/  8|   1.065/ 11|   1.059/ 12|   1.053/ 13 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  48   |   26200|     1346.79|   1.039/ 18|   1.014/ 51|   1.007/ 94|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  37   |     414|       39.48|   1.075/  9|   1.054/ 13|   1.049/ 14|   1.044/ 16 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  35   |      21|       27.72|   1.070/ 10|   1.049/ 14|   1.042/ 16|   1.034/ 20 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  42   |     966|       82.64|   1.068/ 10|   1.061/ 11|   1.060/ 11|   1.058/ 12 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  43   |     228|       57.65|   1.043/ 16|   1.033/ 21|   1.031/ 23|   1.028/ 25 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  47   |     105|       24.91|   1.037/ 18|   1.031/ 22|   1.030/ 23|   1.028/ 24 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  43   |    2516|      196.56|   1.078/  9|   1.054/ 13|   1.048/ 14|   1.042/ 16 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  41   |      93|       29.26|   1.040/ 17|   1.033/ 21|   1.031/ 22|   1.030/ 23 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  34   |     271|      256.19|   1.063/ 11|   1.045/ 15|   1.040/ 17|   1.035/ 19 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  46   |     223|       43.31|   1.061/ 11|   1.071/ 10|   1.074/  9|   1.077/  9 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  51   |      13|       14.68|   1.034/ 20|   1.047/ 15|   1.050/ 14|   1.053/ 13 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  41   |     201|       29.41|   1.030/ 23|   1.025/ 28|   1.023/ 30|   1.022/ 31 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  45   |     803|       27.70|   1.051/ 13|   1.040/ 17|   1.038/ 18|   1.035/ 20 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  40   |      49|       15.21|   1.060/ 11|   1.036/ 19|   1.029/ 24|   1.023/ 30 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  42   |      51|       81.03|   1.029/ 24|   1.017/ 42|   1.013/ 51|   1.010/ 67 |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  48   |     593|       69.43|   1.073/  9|   1.056/ 12|   1.051/ 13|   1.046/ 15 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  62   |     847|      111.19|   1.025/ 27|   1.019/ 36|   1.018/ 39|   1.016/ 43 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  32   |      42|       23.45|   1.089/  8|   1.045/ 15|   1.034/ 20|   1.024/ 28 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  42   |     319|       54.72|   1.037/ 18|   1.031/ 22|   1.029/ 24|   1.028/ 25 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  18   |       7|       12.09|   1.361/  2|   1.002/ **|   1.000/ --|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  40   |      65|        2.01|   1.064/ 11|   1.062/ 11|   1.062/ 11|   1.061/ 11 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  51   |      30|       10.53|   1.016/ 43|   1.019/ 37|   1.020/ 35|   1.021/ 34 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  50   |     464|       10.78|   1.020/ 34|   1.011/ 65|   1.008/ 82|   1.006/ ** |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  33   |       2|        0.06|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  54   |     231|        5.13|   1.049/ 14|   1.042/ 17|   1.040/ 17|   1.038/ 18 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  36   |      32|       10.96|   1.043/ 16|   1.032/ 21|   1.029/ 24|   1.026/ 26 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  61   |      92|        3.57|   1.029/ 24|   1.026/ 26|   1.026/ 27|   1.026/ 27 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  50   |     608|       68.25|   1.026/ 26|   1.019/ 37|   1.017/ 41|   1.015/ 47 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  49   |      25|        2.47|   1.033/ 21|   1.017/ 40|   1.013/ 52|   1.010/ 73 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  46   |       8|        5.36|   1.013/ 54|   1.008/ 91|   1.006/ **|   1.005/ ** |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  44   |     190|        1.13|   1.078/  9|   1.037/ 19|   1.026/ 26|   1.015/ 45 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  31   |      89|        9.43|   1.059/ 12|   1.056/ 12|   1.055/ 12|   1.055/ 12 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  51   |    8160|      708.10|   1.036/ 19|   1.018/ 39|   1.013/ 53|   1.009/ 81 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  25   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  33   |      61|        5.35|   1.057/ 12|   1.057/ 12|   1.056/ 12|   1.054/ 13 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  41   |      67|       20.34|   1.032/ 21|   1.033/ 21|   1.034/ 20|   1.034/ 20 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  31   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  45   |    5984|       28.31|   1.088/  8|   1.085/  8|   1.084/  8|   1.084/  8 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  51   |      67|        9.58|   1.041/ 17|   1.035/ 20|   1.033/ 21|   1.032/ 22 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  44   |      45|        2.15|   1.021/ 33|   1.008/ 83|   1.005/ **|   1.002/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  18   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  37   |      67|        2.54|   1.092/  7|   1.038/ 18|   1.025/ 28|   1.012/ 58 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  53   |    3719|       97.86|   1.080/  8|   1.058/ 12|   1.052/ 13|   1.046/ 15 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  40   |     232|       12.14|   1.056/ 12|   1.044/ 16|   1.041/ 17|   1.038/ 18 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  51   |    3359|        2.40|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  40   |     297|        6.01|   1.053/ 13|   1.044/ 16|   1.042/ 16|   1.040/ 17 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  43   |       7|        1.30|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  43   |      69|       16.90|   1.053/ 13|   1.043/ 16|   1.041/ 17|   1.039/ 18 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  44   |      66|        5.89|   1.064/ 11|   1.046/ 15|   1.041/ 17|   1.036/ 19 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  48   |     464|       79.71|   1.025/ 27|   1.018/ 38|   1.017/ 42|   1.015/ 46 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  45   |     311|       29.98|   1.031/ 22|   1.019/ 37|   1.015/ 45|   1.012/ 56 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  48   |     841|       48.13|   1.061/ 11|   1.075/  9|   1.079/  9|   1.083/  8 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  54   |     402|        4.01|   1.052/ 13|   1.045/ 15|   1.043/ 16|   1.042/ 17 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  31   |       9|        1.41|   1.021/ 33|   1.033/ 21|   1.036/ 19|   1.039/ 17 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  26   |       3|        0.03|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  41   |     242|       43.79|   1.058/ 12|   1.037/ 19|   1.031/ 22|   1.025/ 27 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  76   |   29421|      438.63|   1.022/ 32|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  42   |       1|        0.46|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  39   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  27   |       6|        1.70|   1.059/ 12|   1.032/ 22|   1.024/ 29|   1.015/ 47 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  53   |    7076|       85.10|   1.039/ 18|   1.025/ 27|   1.022/ 32|   1.018/ 38 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  41   |      15|        0.49|   1.058/ 12|   1.103/  7|   1.114/  6|   1.126/  5 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  51   |     144|       13.46|   1.021/ 33|   1.018/ 39|   1.017/ 41|   1.016/ 43 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  46   |      18|        1.08|   1.085/  8|   1.076/  9|   1.073/  9|   1.070/ 10 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  16   |       7|        0.57|   1.042/ 16|   1.019/ 35|   1.005/ **|   1.000/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  26   |       7|        0.63|   1.100/  7|   1.044/ 16|   1.027/ 26|   1.011/ 65 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  36   |      70|        7.65|   1.048/ 14|   1.045/ 15|   1.045/ 15|   1.045/ 15 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  47   |     337|       34.53|   1.059/ 12|   1.036/ 19|   1.030/ 23|   1.024/ 28 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  51   |    1164|        0.86|   1.071/ 10|   1.062/ 11|   1.061/ 11|   1.059/ 12 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  51   |     854|        3.20|   1.038/ 18|   1.022/ 31|   1.019/ 37|   1.015/ 46 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  71   |    6240|       74.84|   1.016/ 44|   1.012/ 60|   1.011/ 66|   1.010/ 73 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  58   |      92|        2.36|   1.012/ 58|   1.011/ 66|   1.010/ 67|   1.010/ 68 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  51   |    1378|      279.94|   1.069/ 10|   1.054/ 13|   1.050/ 14|   1.046/ 15 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  41   |     225|       24.49|   1.033/ 21|   1.017/ 41|   1.013/ 54|   1.009/ 75 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  70   |   29364|      487.46|   1.017/ 40|   1.012/ 56|   1.011/ 62|   1.010/ 70 |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  43   |       8|        2.87|   1.036/ 19|   1.029/ 24|   1.027/ 26|   1.024/ 28 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  78   |     488|        3.88|   1.069/ 10|   1.066/ 10|   1.065/ 11|   1.064/ 11 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  35   |       8|        0.73|   1.008/ 83|   1.028/ 25|   1.033/ 21|   1.038/ 18 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  37   |      27|        1.45|   1.038/ 18|   1.024/ 29|   1.019/ 36|   1.014/ 48 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  36   |      15|        0.32|   1.022/ 32|   1.011/ 60|   1.010/ 69|   1.009/ 75 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  36   |      12|        6.74|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  27   |      27|        6.19|   1.158/  4|   1.087/  8|   1.069/ 10|   1.050/ 14 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  28   |       8|        1.26|   1.052/ 13|   1.004/ **|   1.000/ --|   1.000/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  28   |      15|        8.07|   1.110/  6|   1.046/ 15|   1.032/ 21|   1.020/ 34 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  52   |      24|        3.56|   1.011/ 61|   1.012/ 57|   1.012/ 56|   1.012/ 55 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  27   |      17|        3.79|   1.072/  9|   1.115/  6|   1.125/  5|   1.133/  5 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  29   |       3|        0.38|   1.260/  2|   1.063/ 11|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  41   |      46|       16.39|   1.029/ 24|   1.020/ 34|   1.018/ 38|   1.016/ 42 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  45   |     103|        3.15|   1.014/ 49|   1.009/ 74|   1.008/ 84|   1.007/ 98 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  33   |      27|        1.34|   1.050/ 14|   1.044/ 15|   1.042/ 16|   1.039/ 18 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  32   |       1|        0.25|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  43   |    1997|       15.77|   1.107/  6|   1.091/  7|   1.086/  8|   1.081/  8 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  44   |     121|       45.00|   1.064/ 11|   1.047/ 15|   1.043/ 16|   1.039/ 18 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  52   |     174|        4.86|   1.019/ 35|   1.013/ 52|   1.012/ 58|   1.011/ 65 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  56   |    5068|      290.34|   1.028/ 25|   1.019/ 36|   1.017/ 41|   1.014/ 48 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  33   |      21|        4.19|   1.061/ 11|   1.022/ 31|   1.011/ 61|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  35   |       3|        0.52|   1.145/  5|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  37   |      34|        1.51|   1.057/ 12|   1.047/ 14|   1.045/ 15|   1.043/ 16 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  39   |      56|        0.27|   1.102/  7|   1.093/  7|   1.091/  7|   1.089/  8 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  40   |      74|       35.43|   1.037/ 19|   1.046/ 15|   1.048/ 14|   1.051/ 13 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  48   |     222|       41.28|   1.024/ 29|   1.012/ 58|   1.009/ 79|   1.006/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  31   |      11|        2.36|   1.059/ 12|   1.021/ 33|   1.011/ 63|   1.000/ ** |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  43   |     383|        1.75|   1.082/  8|   1.070/ 10|   1.067/ 10|   1.064/ 11 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  51   |     194|       45.95|   1.043/ 16|   1.031/ 22|   1.028/ 24|   1.026/ 27 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  41   |      10|        1.34|   1.016/ 44|   1.010/ 68|   1.009/ 78|   1.008/ 91 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  42   |    1057|       32.89|   1.096/  7|   1.086/  8|   1.084/  8|   1.081/  8 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  89   |     722|        6.65|   1.030/ 23|   1.019/ 36|   1.016/ 42|   1.014/ 51 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  50   |     671|       17.49|   1.057/ 12|   1.049/ 14|   1.048/ 14|   1.046/ 15 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  45   |    1022|       99.50|   1.035/ 20|   1.026/ 26|   1.024/ 28|   1.022/ 31 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  34   |      10|        3.79|   1.029/ 24|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  40   |     730|       37.61|   1.045/ 15|   1.040/ 17|   1.038/ 18|   1.037/ 19 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  43   |    1117|        7.61|   1.116/  6|   1.092/  7|   1.086/  8|   1.080/  9 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  38   |     167|        4.87|   1.051/ 13|   1.044/ 16|   1.042/ 16|   1.040/ 17 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  30   |      10|        0.63|   1.121/  6|   1.053/ 13|   1.034/ 20|   1.015/ 46 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  42   |     136|       19.57|   1.013/ 54|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  41   |      14|        2.53|   1.028/ 25|   1.032/ 21|   1.034/ 20|   1.036/ 19 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  34   |      23|        4.19|   1.071/ 10|   1.061/ 11|   1.059/ 12|   1.058/ 12 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  48   |      93|       44.25|   1.027/ 26|   1.016/ 42|   1.014/ 49|   1.012/ 59 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  23   |      32|        1.99|   1.195/  3|   1.125/  5|   1.084/  8|   1.038/ 18 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  35   |     108|        1.84|   1.068/ 10|   1.054/ 13|   1.049/ 14|   1.045/ 15 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  59   |   25273|      536.58|   1.018/ 38|   1.013/ 54|   1.012/ 60|   1.010/ 67 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  34   |       7|        0.32|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  49   |      32|        0.76|   1.093/  7|   1.111/  6|   1.115/  6|   1.119/  6 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  51   |    2750|      265.99|   1.053/ 13|   1.037/ 19|   1.033/ 21|   1.029/ 24 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  57   |    1818|      211.30|   1.024/ 29|   1.015/ 45|   1.013/ 52|   1.011/ 61 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  33   |       3|        0.17|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  31   |      14|        0.25|   1.074/  9|   1.069/ 10|   1.074/  9|   1.081/  8 |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  61   |      57|        0.86|   1.019/ 36|   1.006/ **|   1.003/ **|   1.000/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  35   |       7|        0.93|   1.021/ 33|   1.012/ 56|   1.011/ 64|   1.010/ 72 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  37   |       8|        5.87|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  43   |      40|        3.43|   1.010/ 70|   1.007/ 93|   1.007/ 96|   1.007/ 96 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  45   |    3352|       40.30|   1.050/ 14|   1.034/ 20|   1.030/ 23|   1.026/ 26 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  62   |   72631|      220.40|   1.052/ 13|   1.030/ 23|   1.024/ 29|   1.018/ 37 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  49   |     270|        6.45|   1.062/ 11|   1.052/ 13|   1.049/ 14|   1.047/ 15 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  42   |     105|       10.66|   1.089/  8|   1.091/  7|   1.092/  7|   1.092/  7 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  51   |   25851|      389.11|   1.048/ 14|   1.042/ 16|   1.041/ 17|   1.040/ 17 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  33   |      17|        4.78|   1.051/ 13|   1.042/ 16|   1.039/ 17|   1.036/ 19 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  35   |       9|        0.28|   1.063/ 11|   1.036/ 19|   1.028/ 25|   1.019/ 36 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  35   |      10|        0.32|   1.009/ 77|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  29   |       3|        0.17|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  39   |       4|        0.28|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |

