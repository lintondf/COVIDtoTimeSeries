# State and Country COVID-19 Analysis #
## Updated: 2020-04-30 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  47   |   25911|     1331.95|   1.045/ 15|   1.017/ 39|   1.011/ 65|   1.004/183 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  51   |    7321|      824.25|   1.058/ 12|   1.034/ 20|   1.028/ 25|   1.022/ 31 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  42   |    3800|      380.54|   1.051/ 14|   1.039/ 18|   1.036/ 19|   1.033/ 21 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  41   |    3660|      526.69|   1.091/  7|   1.067/ 10|   1.060/ 11|   1.053/ 13 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  42   |    2399|      187.41|   1.079/  9|   1.048/ 14|   1.039/ 18|   1.030/ 23 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  44   |    2322|      183.25|   1.063/ 11|   1.047/ 15|   1.043/ 16|   1.039/ 18 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  42   |    2373|      665.51|   1.077/  9|   1.049/ 14|   1.042/ 16|   1.035/ 20 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  57   |    2143|       54.23|   1.061/ 11|   1.046/ 15|   1.042/ 16|   1.038/ 18 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  47   |    1951|      419.74|   1.042/ 16|   1.028/ 25|   1.024/ 28|   1.021/ 33 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  53   |    1301|       60.56|   1.053/ 13|   1.035/ 20|   1.031/ 23|   1.026/ 26 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  61   |   70337|      213.44|   1.055/ 12|   1.031/ 22|   1.025/ 27|   1.019/ 36 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  69   |   28992|      481.29|   1.018/ 39|   1.013/ 54|   1.012/ 60|   1.010/ 67 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  50   |   24606|      370.37|   1.044/ 15|   1.033/ 21|   1.030/ 23|   1.027/ 26 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  58   |   25020|      531.21|   1.019/ 36|   1.013/ 52|   1.012/ 58|   1.011/ 65 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  75   |   29095|      433.76|   1.024/ 29|   1.001/541|   0.996/ ? |   0.990/ ?  |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  50   |    8094|      702.30|   1.040/ 17|   1.020/ 34|   1.015/ 45|   1.011/ 65 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  52   |    6950|       83.59|   1.042/ 16|   1.027/ 26|   1.023/ 30|   1.020/ 35 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  70   |    6183|       74.16|   1.016/ 42|   1.012/ 58|   1.011/ 63|   1.010/ 70 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  44   |    5516|       26.09|   1.089/  8|   1.083/  8|   1.082/  8|   1.082/  8 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  55   |    4974|      284.92|   1.030/ 23|   1.020/ 35|   1.018/ 39|   1.015/ 46 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  36   |     256|       52.24|   1.053/ 13|   1.041/ 17|   1.038/ 18|   1.035/ 19 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  36   |       9|       12.30|   1.001/1099|   1.000/ ? |   1.000/ ? |   0.999/ ?  |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  40   |     318|       43.72|   1.056/ 12|   1.037/ 19|   1.031/ 22|   1.026/ 27 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  37   |      57|       18.79|   1.039/ 18|   1.040/ 17|   1.040/ 17|   1.041/ 17 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  57   |    2143|       54.23|   1.061/ 11|   1.046/ 15|   1.042/ 16|   1.038/ 18 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  47   |     812|      140.99|   1.064/ 11|   1.057/ 12|   1.056/ 12|   1.054/ 13 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  42   |    2373|      665.51|   1.077/  9|   1.049/ 14|   1.042/ 16|   1.035/ 20 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  35   |     147|      151.01|   1.082/  8|   1.074/  9|   1.072/  9|   1.070/ 10 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  53   |    1301|       60.56|   1.053/ 13|   1.035/ 20|   1.031/ 23|   1.026/ 26 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  49   |    1123|      105.81|   1.050/ 14|   1.040/ 17|   1.038/ 18|   1.035/ 20 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  30   |      17|       11.80|   1.054/ 13|   1.060/ 11|   1.061/ 11|   1.061/ 11 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  35   |      62|       34.45|   1.037/ 19|   1.024/ 29|   1.021/ 33|   1.017/ 40 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  44   |    2322|      183.25|   1.063/ 11|   1.047/ 15|   1.043/ 16|   1.039/ 18 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  45   |     970|      144.07|   1.059/ 12|   1.049/ 14|   1.046/ 15|   1.044/ 16 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  36   |     147|       46.44|   1.073/  9|   1.069/ 10|   1.069/ 10|   1.068/ 10 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  48   |     144|       49.26|   1.046/ 15|   1.025/ 28|   1.019/ 36|   1.014/ 50 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  45   |     244|       54.56|   1.050/ 14|   1.038/ 18|   1.035/ 20|   1.032/ 22 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  47   |    1951|      419.74|   1.042/ 16|   1.028/ 25|   1.024/ 28|   1.021/ 33 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  34   |      56|       41.45|   1.062/ 11|   1.037/ 18|   1.031/ 22|   1.024/ 28 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  42   |    1190|      196.78|   1.095/  7|   1.070/ 10|   1.063/ 11|   1.055/ 12 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  41   |    3660|      526.69|   1.091/  7|   1.067/ 10|   1.060/ 11|   1.053/ 13 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  42   |    3800|      380.54|   1.051/ 14|   1.039/ 18|   1.036/ 19|   1.033/ 21 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  40   |     345|       61.10|   1.102/  7|   1.089/  8|   1.085/  8|   1.081/  8 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  42   |     263|       88.26|   1.054/ 13|   1.036/ 19|   1.032/ 22|   1.027/ 26 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  42   |     353|       57.60|   1.063/ 11|   1.058/ 12|   1.057/ 12|   1.057/ 12 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  34   |      16|       15.25|   1.062/ 11|   1.025/ 27|   1.015/ 45|   1.005/136 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  33   |      64|       33.29|   1.092/  7|   1.054/ 13|   1.042/ 16|   1.029/ 23 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  45   |     233|       75.67|   1.042/ 16|   1.033/ 21|   1.031/ 23|   1.028/ 24 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  38   |      65|       48.00|   1.057/ 12|   1.038/ 18|   1.033/ 21|   1.028/ 25 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  51   |    7321|      824.25|   1.058/ 12|   1.034/ 20|   1.028/ 25|   1.022/ 31 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  36   |     119|       56.79|   1.093/  7|   1.065/ 10|   1.058/ 12|   1.051/ 14 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  47   |   25911|     1331.95|   1.045/ 15|   1.017/ 39|   1.011/ 65|   1.004/183 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  36   |     396|       37.74|   1.080/  9|   1.054/ 13|   1.048/ 14|   1.042/ 16 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  34   |      21|       27.27|   1.073/  9|   1.065/ 11|   1.060/ 11|   1.056/ 12 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  41   |     905|       77.39|   1.067/ 10|   1.054/ 13|   1.050/ 14|   1.047/ 15 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  42   |     222|       56.08|   1.045/ 15|   1.033/ 21|   1.030/ 23|   1.027/ 26 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  46   |     102|       24.29|   1.038/ 18|   1.030/ 23|   1.028/ 24|   1.027/ 26 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  42   |    2399|      187.41|   1.079/  9|   1.048/ 14|   1.039/ 18|   1.030/ 23 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  40   |      91|       28.34|   1.043/ 16|   1.035/ 20|   1.033/ 21|   1.031/ 22 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  33   |     260|      245.63|   1.070/ 10|   1.046/ 15|   1.041/ 17|   1.035/ 20 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  45   |     206|       39.92|   1.056/ 12|   1.059/ 12|   1.060/ 11|   1.061/ 11 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  50   |      12|       13.86|   1.000/3121657384082680|   1.000/ ? |   1.000/3121657384082680|   1.000/ ?  |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  40   |     197|       28.77|   1.032/ 22|   1.025/ 28|   1.023/ 30|   1.022/ 32 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  44   |     770|       26.56|   1.052/ 13|   1.036/ 19|   1.032/ 22|   1.028/ 24 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  39   |      47|       14.75|   1.064/ 11|   1.039/ 18|   1.032/ 21|   1.025/ 28 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  41   |      50|       79.74|   1.032/ 22|   1.019/ 36|   1.016/ 44|   1.012/ 56 |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  47   |     563|       65.94|   1.076/  9|   1.057/ 12|   1.052/ 13|   1.047/ 14 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  61   |     830|      109.00|   1.026/ 26|   1.019/ 36|   1.017/ 40|   1.016/ 44 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  31   |      40|       22.44|   1.103/  7|   1.044/ 15|   1.029/ 24|   1.013/ 52 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  41   |     309|       53.07|   1.039/ 18|   1.028/ 24|   1.026/ 27|   1.024/ 29 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  17   |       7|       12.09|   1.426/  1|   1.029/ 24|   0.996/ ? |   0.973/ ?  |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  39   |      61|        1.89|   1.067/ 10|   1.066/ 10|   1.066/ 10|   1.067/ 10 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  50   |      29|       10.31|   1.014/ 50|   1.015/ 46|   1.015/ 45|   1.016/ 44 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  49   |     458|       10.65|   1.022/ 31|   1.010/ 67|   1.007/ 92|   1.005/145 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  32   |       2|        0.06|   1.000/ ? |   1.000/ ? |   1.000/ ? |   1.000/ ?  |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  53   |     222|        4.94|   1.051/ 13|   1.043/ 16|   1.041/ 17|   1.039/ 17 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  35   |      31|       10.61|   1.046/ 15|   1.033/ 21|   1.030/ 23|   1.026/ 26 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  60   |      89|        3.48|   1.028/ 25|   1.024/ 29|   1.023/ 30|   1.023/ 30 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  49   |     598|       67.15|   1.028/ 25|   1.019/ 37|   1.017/ 42|   1.014/ 48 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  48   |      25|        2.44|   1.035/ 20|   1.017/ 41|   1.012/ 56|   1.008/ 89 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  45   |       8|        5.34|   1.015/ 47|   1.009/ 74|   1.008/ 85|   1.007/100 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  43   |     184|        1.09|   1.086/  8|   1.044/ 16|   1.032/ 21|   1.021/ 33 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  30   |      84|        8.92|   1.060/ 11|   1.056/ 12|   1.055/ 13|   1.054/ 13 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  50   |    8094|      702.30|   1.040/ 17|   1.020/ 34|   1.015/ 45|   1.011/ 65 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  24   |       1|        0.09|   1.000/3121657384082680|   1.000/ ? |   1.000/1040552461360893|   1.000/ ?  |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  32   |      59|        5.12|   1.056/ 12|   1.062/ 11|   1.063/ 11|   1.063/ 11 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  40   |      65|       19.58|   1.031/ 22|   1.030/ 23|   1.030/ 23|   1.029/ 23 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  30   |       1|        0.43|   1.000/ ? |   1.000/ ? |   1.000/ ? |   1.000/1040552461360893 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  44   |    5516|       26.09|   1.089/  8|   1.083/  8|   1.082/  8|   1.082/  8 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  50   |      64|        9.25|   1.042/ 16|   1.034/ 20|   1.032/ 22|   1.030/ 23 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  43   |      44|        2.13|   1.024/ 29|   1.010/ 68|   1.007/101|   1.003/202 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  17   |       1|        0.09|   1.000/ ? |   1.000/ ? |   1.000/ ? |   1.000/ ?  |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  36   |      67|        2.52|   1.104/  6|   1.049/ 14|   1.035/ 19|   1.022/ 31 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  52   |    3563|       93.77|   1.085/  8|   1.062/ 11|   1.056/ 12|   1.050/ 14 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  39   |     222|       11.63|   1.059/ 12|   1.045/ 15|   1.041/ 17|   1.038/ 18 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  50   |    3359|        2.40|   1.000/10638|   1.000/ ? |   1.000/ ? |   1.000/ ?  |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  39   |     284|        5.75|   1.055/ 12|   1.044/ 16|   1.041/ 17|   1.038/ 18 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  42   |       7|        1.33|   1.000/ ? |   1.000/3121657384082680|   1.000/ ? |   1.000/ ?  |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  42   |      66|       16.27|   1.054/ 13|   1.041/ 17|   1.038/ 18|   1.035/ 19 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  43   |      64|        5.68|   1.069/ 10|   1.052/ 13|   1.048/ 14|   1.043/ 16 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  47   |     456|       78.29|   1.027/ 26|   1.019/ 36|   1.017/ 41|   1.015/ 46 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  44   |     306|       29.58|   1.033/ 21|   1.020/ 35|   1.016/ 43|   1.012/ 56 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  47   |     777|       44.50|   1.038/ 18|   1.027/ 25|   1.025/ 28|   1.022/ 31 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  53   |     385|        3.84|   1.052/ 13|   1.043/ 16|   1.041/ 17|   1.039/ 18 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  30   |       9|        1.32|   1.023/ 31|   1.020/ 35|   1.019/ 36|   1.018/ 38 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  25   |       3|        0.03|   1.000/ ? |   1.000/ ? |   1.000/ ? |   1.000/1040552461360893 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  40   |     237|       42.90|   1.064/ 11|   1.042/ 16|   1.036/ 19|   1.030/ 23 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  75   |   29095|      433.76|   1.024/ 29|   1.001/541|   0.996/ ? |   0.990/ ?  |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  41   |       1|        0.46|   1.000/ ? |   1.000/3121657384082680|   1.000/520276230680446|   1.000/780414346020670 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  38   |       1|        0.43|   1.000/3121657384082680|   1.000/3121657384082680|   1.000/ ? |   1.000/780414346020670 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  26   |       6|        1.69|   1.064/ 11|   1.045/ 15|   1.039/ 18|   1.032/ 21 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  52   |    6950|       83.59|   1.042/ 16|   1.027/ 26|   1.023/ 30|   1.020/ 35 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  40   |      11|        0.37|   1.042/ 16|   1.079/  9|   1.088/  8|   1.098/  7 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  50   |     142|       13.28|   1.022/ 31|   1.020/ 35|   1.019/ 36|   1.019/ 37 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  45   |      17|        1.02|   1.093/  7|   1.092/  7|   1.091/  7|   1.091/  7 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  15   |       7|        0.57|   1.092/  7|   1.034/ 20|   1.016/ 43|   0.995/ ?  |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  25   |       7|        0.57|   1.081/  8|   1.036/ 19|   1.016/ 43|   0.993/ ?  |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  35   |      67|        7.27|   1.054/ 13|   1.041/ 17|   1.040/ 17|   1.038/ 18 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ ? |   1.000/ ? |   1.000/ ? |   1.000/624331476816536 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  46   |     330|       33.75|   1.063/ 11|   1.039/ 18|   1.033/ 21|   1.027/ 26 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  50   |    1097|        0.81|   1.072/  9|   1.062/ 11|   1.059/ 12|   1.057/ 12 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  50   |     843|        3.16|   1.042/ 16|   1.027/ 26|   1.023/ 30|   1.019/ 36 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  70   |    6183|       74.16|   1.016/ 42|   1.012/ 58|   1.011/ 63|   1.010/ 70 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  57   |      91|        2.33|   1.011/ 61|   1.009/ 80|   1.008/ 86|   1.008/ 91 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  50   |    1322|      268.66|   1.075/  9|   1.062/ 11|   1.058/ 12|   1.055/ 12 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  40   |     222|       24.17|   1.036/ 19|   1.016/ 43|   1.011/ 62|   1.006/108 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  69   |   28992|      481.29|   1.018/ 39|   1.013/ 54|   1.012/ 60|   1.010/ 67 |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  42   |       8|        2.76|   1.036/ 19|   1.026/ 27|   1.023/ 30|   1.019/ 36 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  77   |     462|        3.67|   1.073/  9|   1.072/  9|   1.072/  9|   1.071/ 10 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  34   |       7|        0.70|   1.003/229|   1.019/ 36|   1.023/ 30|   1.028/ 25 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  36   |      27|        1.44|   1.043/ 16|   1.032/ 21|   1.029/ 24|   1.025/ 27 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  35   |      15|        0.31|   1.026/ 26|   1.001/664|   0.995/ ? |   0.990/ ?  |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  35   |      12|        6.73|   1.006/115|   0.999/ ? |   0.998/ ? |   0.997/ ?  |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  26   |      26|        5.91|   1.174/  4|   1.102/  7|   1.083/  8|   1.064/ 11 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  27   |       8|        1.26|   1.062/ 11|   1.010/ 68|   0.996/ ? |   0.981/ ?  |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  27   |      15|        7.76|   1.112/  6|   1.054/ 13|   1.033/ 21|   1.012/ 60 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  51   |      24|        3.53|   1.012/ 56|   1.014/ 49|   1.015/ 47|   1.015/ 45 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  26   |      16|        3.52|   1.085/  8|   1.138/  5|   1.149/  4|   1.159/  4 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  28   |       2|        0.34|   1.175/  4|   1.065/ 11|   1.021/ 32|   0.972/ ?  |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  40   |      45|       16.18|   1.030/ 23|   1.018/ 38|   1.015/ 45|   1.013/ 54 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  44   |     102|        3.13|   1.015/ 45|   1.010/ 70|   1.009/ 80|   1.007/ 94 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  32   |      26|        1.30|   1.051/ 13|   1.046/ 15|   1.044/ 16|   1.041/ 17 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  31   |       1|        0.25|   1.000/ ? |   1.000/ ? |   1.000/ ? |   1.000/3121657384082680 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  42   |    1850|       14.61|   1.114/  6|   1.096/  7|   1.092/  7|   1.086/  8 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  43   |     115|       42.92|   1.068/ 10|   1.049/ 14|   1.045/ 15|   1.040/ 17 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  51   |     172|        4.79|   1.021/ 34|   1.013/ 53|   1.011/ 61|   1.010/ 72 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  55   |    4974|      284.92|   1.030/ 23|   1.020/ 35|   1.018/ 39|   1.015/ 46 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  32   |      21|        4.22|   1.069/ 10|   1.034/ 20|   1.023/ 30|   1.012/ 58 |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  34   |       4|        0.54|   1.145/  5|   1.000/ ? |   1.000/ ? |   1.000/ ?  |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  36   |      33|        1.46|   1.060/ 11|   1.052/ 13|   1.050/ 14|   1.049/ 14 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  38   |      51|        0.25|   1.104/  7|   1.086/  8|   1.081/  8|   1.076/  9 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  39   |      70|       33.70|   1.035/ 19|   1.040/ 17|   1.041/ 17|   1.043/ 16 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  47   |     219|       40.89|   1.027/ 26|   1.014/ 48|   1.011/ 61|   1.008/ 86 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  30   |      11|        2.32|   1.070/ 10|   1.023/ 30|   1.010/ 71|   0.996/ ?  |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  42   |     356|        1.62|   1.082/  8|   1.067/ 10|   1.062/ 11|   1.058/ 12 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  50   |     188|       44.58|   1.045/ 15|   1.032/ 22|   1.028/ 24|   1.025/ 28 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  40   |       9|        1.31|   1.016/ 43|   1.005/135|   1.002/282|   1.000/ ?  |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  41   |     968|       30.14|   1.096/  7|   1.085/  8|   1.082/  8|   1.078/  9 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  88   |     717|        6.61|   1.032/ 22|   1.020/ 34|   1.017/ 41|   1.014/ 49 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  49   |     641|       16.71|   1.060/ 11|   1.050/ 14|   1.048/ 14|   1.046/ 15 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  44   |    1002|       97.52|   1.037/ 19|   1.029/ 24|   1.026/ 26|   1.024/ 28 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  33   |      10|        3.81|   1.034/ 20|   1.006/121|   0.998/ ? |   0.990/ ?  |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  39   |     703|       36.24|   1.047/ 15|   1.041/ 17|   1.039/ 17|   1.038/ 18 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  42   |    1031|        7.02|   1.120/  6|   1.093/  7|   1.085/  8|   1.078/  9 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  37   |     161|        4.69|   1.054/ 13|   1.045/ 15|   1.043/ 16|   1.041/ 17 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  29   |      10|        0.62|   1.134/  5|   1.075/  9|   1.059/ 12|   1.042/ 16 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  41   |     130|       18.71|   1.019/ 37|   0.996/ ? |   0.990/ ? |   0.985/ ?  |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  40   |      14|        2.43|   1.027/ 25|   1.034/ 20|   1.036/ 19|   1.038/ 18 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  33   |      22|        3.95|   1.075/  9|   1.059/ 12|   1.055/ 12|   1.051/ 13 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  47   |      91|       43.40|   1.028/ 25|   1.015/ 47|   1.011/ 61|   1.008/ 85 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  22   |      32|        2.00|   1.190/  3|   1.166/  4|   1.131/  5|   1.092/  7 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  34   |     104|        1.77|   1.073/  9|   1.057/ 12|   1.054/ 13|   1.049/ 14 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  58   |   25020|      531.21|   1.019/ 36|   1.013/ 52|   1.012/ 58|   1.011/ 65 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  33   |       7|        0.32|   1.000/ ? |   1.000/3121657384082680|   1.000/ ? |   1.000/3121657384082680 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  48   |      29|        0.69|   1.088/  8|   1.105/  6|   1.109/  6|   1.113/  6 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  50   |    2667|      257.98|   1.055/ 12|   1.039/ 18|   1.034/ 20|   1.030/ 23 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  56   |    1799|      209.14|   1.025/ 27|   1.017/ 41|   1.015/ 47|   1.013/ 55 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  32   |       2|        0.11|   1.000/ ? |   1.000/3121657384082680|   1.000/624331476816536|   1.000/3121657384082680 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/3121657384082680|   1.000/ ? |   1.000/ ? |   1.000/ ?  |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  30   |      12|        0.22|   1.056/ 12|   0.990/ ? |   0.977/ ? |   0.965/ ?  |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  60   |      57|        0.86|   1.020/ 34|   1.007/104|   1.003/208|   1.000/35633 |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  34   |       7|        0.86|   1.024/ 28|   1.011/ 60|   1.009/ 81|   1.006/115 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  36   |       8|        5.87|   1.000/ ? |   1.000/ ? |   1.000/ ? |   1.000/1560828692041340 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  42   |      40|        3.39|   1.010/ 70|   1.005/131|   1.005/153|   1.004/174 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  44   |    3271|       39.33|   1.054/ 13|   1.037/ 18|   1.033/ 21|   1.029/ 24 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  61   |   70337|      213.44|   1.055/ 12|   1.031/ 22|   1.025/ 27|   1.019/ 36 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  48   |     259|        6.18|   1.064/ 11|   1.052/ 13|   1.049/ 14|   1.046/ 15 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  41   |      97|        9.78|   1.090/  8|   1.091/  7|   1.092/  7|   1.093/  7 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  50   |   24606|      370.37|   1.044/ 15|   1.033/ 21|   1.030/ 23|   1.027/ 26 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  32   |      16|        4.56|   1.054/ 13|   1.042/ 16|   1.039/ 18|   1.035/ 20 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  34   |       9|        0.27|   1.069/ 10|   1.038/ 18|   1.029/ 24|   1.019/ 36 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  34   |      10|        0.32|   1.009/ 80|   1.003/274|   1.000/1441|   0.998/ ?  |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  28   |       3|        0.17|   1.000/ ? |   1.000/ ? |   1.000/ ? |   1.000/3121657384082680 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  38   |       4|        0.28|   1.000/ ? |   1.000/ ? |   1.000/ ? |   1.000/ ?  |

