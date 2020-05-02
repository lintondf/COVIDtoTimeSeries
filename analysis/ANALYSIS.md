# State and Country COVID-19 Analysis #
## Updated: 2020-05-02 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  49   |   26141|     1343.78|   1.033/ 21|   1.012/ 56|   1.007/ 94|   1.002/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  53   |    7877|      886.81|   1.054/ 13|   1.037/ 18|   1.033/ 21|   1.029/ 23 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  44   |    4035|      404.03|   1.045/ 15|   1.035/ 20|   1.032/ 22|   1.029/ 24 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  43   |    4019|      578.31|   1.081/  8|   1.058/ 12|   1.051/ 13|   1.045/ 15 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  44   |    2672|      208.74|   1.077/  9|   1.059/ 12|   1.055/ 12|   1.052/ 13 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  46   |    2536|      200.16|   1.059/ 12|   1.047/ 15|   1.044/ 16|   1.041/ 17 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  44   |    2529|      709.36|   1.066/ 10|   1.041/ 17|   1.034/ 20|   1.028/ 24 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  59   |    2312|       58.51|   1.056/ 12|   1.042/ 16|   1.039/ 18|   1.035/ 20 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  49   |    2045|      439.80|   1.038/ 18|   1.026/ 26|   1.023/ 30|   1.021/ 34 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  55   |    1388|       64.62|   1.049/ 14|   1.035/ 20|   1.032/ 22|   1.028/ 24 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  63   |   73958|      224.42|   1.048/ 14|   1.028/ 25|   1.022/ 31|   1.017/ 40 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  71   |   29611|      491.57|   1.016/ 43|   1.011/ 61|   1.010/ 68|   1.009/ 77 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  52   |   27165|      408.89|   1.051/ 13|   1.051/ 13|   1.052/ 13|   1.052/ 13 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  77   |   29206|      435.42|   1.019/ 36|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  60   |   25552|      542.50|   1.017/ 40|   1.012/ 57|   1.011/ 64|   1.010/ 72 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  52   |    8293|      719.56|   1.033/ 21|   1.016/ 42|   1.012/ 56|   1.008/ 84 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  54   |    7233|       86.99|   1.036/ 19|   1.023/ 30|   1.020/ 35|   1.017/ 42 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  46   |    6480|       30.65|   1.087/  8|   1.084/  8|   1.084/  8|   1.084/  8 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  72   |    6316|       75.75|   1.015/ 46|   1.011/ 62|   1.010/ 67|   1.009/ 74 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  57   |    5140|      294.45|   1.027/ 26|   1.019/ 37|   1.016/ 42|   1.014/ 48 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  38   |     283|       57.70|   1.051/ 13|   1.048/ 14|   1.048/ 14|   1.048/ 14 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  38   |       9|       12.30|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  42   |     341|       46.83|   1.053/ 13|   1.042/ 16|   1.039/ 18|   1.036/ 19 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  39   |      63|       20.74|   1.040/ 17|   1.045/ 15|   1.046/ 15|   1.048/ 14 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  59   |    2312|       58.51|   1.056/ 12|   1.042/ 16|   1.039/ 18|   1.035/ 20 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  49   |     879|      152.67|   1.057/ 12|   1.048/ 14|   1.045/ 15|   1.042/ 16 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  44   |    2529|      709.36|   1.066/ 10|   1.041/ 17|   1.034/ 20|   1.028/ 24 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  37   |     165|      169.86|   1.077/  9|   1.067/ 10|   1.065/ 11|   1.062/ 11 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  55   |    1388|       64.62|   1.049/ 14|   1.035/ 20|   1.032/ 22|   1.028/ 24 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  51   |    1206|      113.60|   1.047/ 15|   1.039/ 18|   1.037/ 19|   1.035/ 20 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  32   |      17|       12.19|   1.056/ 12|   1.034/ 20|   1.028/ 25|   1.021/ 33 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  37   |      64|       35.58|   1.031/ 22|   1.021/ 33|   1.018/ 39|   1.015/ 46 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  46   |    2536|      200.16|   1.059/ 12|   1.047/ 15|   1.044/ 16|   1.041/ 17 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  47   |    1119|      166.26|   1.063/ 11|   1.064/ 11|   1.064/ 11|   1.065/ 10 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  38   |     170|       53.81|   1.072/  9|   1.075/  9|   1.075/  9|   1.076/  9 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  50   |     148|       50.94|   1.039/ 18|   1.022/ 31|   1.018/ 39|   1.013/ 51 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  47   |     258|       57.85|   1.045/ 15|   1.034/ 20|   1.032/ 22|   1.029/ 24 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  49   |    2045|      439.80|   1.038/ 18|   1.026/ 26|   1.023/ 30|   1.021/ 34 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  36   |      58|       42.84|   1.050/ 14|   1.026/ 26|   1.020/ 35|   1.013/ 52 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  44   |    1289|      213.24|   1.082/  8|   1.052/ 13|   1.044/ 16|   1.036/ 19 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  43   |    4019|      578.31|   1.081/  8|   1.058/ 12|   1.051/ 13|   1.045/ 15 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  44   |    4035|      404.03|   1.045/ 15|   1.035/ 20|   1.032/ 22|   1.029/ 24 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  42   |     393|       69.74|   1.094/  7|   1.077/  9|   1.072/  9|   1.067/ 10 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  44   |     283|       94.95|   1.050/ 14|   1.038/ 18|   1.035/ 20|   1.032/ 21 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  44   |     380|       61.97|   1.055/ 12|   1.044/ 16|   1.041/ 17|   1.038/ 18 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  36   |      17|       15.70|   1.049/ 14|   1.025/ 28|   1.019/ 36|   1.014/ 50 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  35   |      73|       37.93|   1.084/  8|   1.060/ 11|   1.053/ 13|   1.046/ 15 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  47   |     251|       81.35|   1.041/ 17|   1.037/ 18|   1.036/ 19|   1.035/ 20 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  40   |      75|       54.98|   1.055/ 12|   1.054/ 13|   1.054/ 13|   1.054/ 13 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  53   |    7877|      886.81|   1.054/ 13|   1.037/ 18|   1.033/ 21|   1.029/ 23 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  38   |     134|       64.06|   1.083/  8|   1.065/ 10|   1.061/ 11|   1.056/ 12 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  49   |   26141|     1343.78|   1.033/ 21|   1.012/ 56|   1.007/ 94|   1.002/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  38   |     434|       41.37|   1.069/ 10|   1.052/ 13|   1.048/ 14|   1.044/ 16 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  36   |      23|       29.60|   1.066/ 10|   1.047/ 14|   1.042/ 16|   1.036/ 19 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  43   |    1018|       87.06|   1.068/ 10|   1.065/ 11|   1.064/ 11|   1.064/ 11 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  44   |     236|       59.52|   1.041/ 17|   1.033/ 21|   1.030/ 23|   1.028/ 25 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  48   |     108|       25.52|   1.035/ 20|   1.028/ 25|   1.027/ 26|   1.025/ 27 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  44   |    2672|      208.74|   1.077/  9|   1.059/ 12|   1.055/ 12|   1.052/ 13 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  42   |      96|       30.15|   1.038/ 18|   1.032/ 21|   1.030/ 23|   1.029/ 24 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  35   |     282|      265.98|   1.059/ 12|   1.045/ 15|   1.042/ 16|   1.038/ 18 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  47   |     241|       46.89|   1.066/ 10|   1.079/  9|   1.082/  8|   1.086/  8 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  52   |      14|       15.86|   1.038/ 18|   1.049/ 14|   1.052/ 13|   1.054/ 13 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  42   |     206|       30.14|   1.029/ 24|   1.025/ 27|   1.024/ 28|   1.023/ 29 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  46   |     841|       28.99|   1.050/ 14|   1.043/ 16|   1.041/ 17|   1.040/ 17 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  41   |      50|       15.45|   1.055/ 12|   1.034/ 20|   1.028/ 24|   1.023/ 30 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  43   |      51|       81.97|   1.027/ 26|   1.016/ 43|   1.013/ 51|   1.011/ 64 |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  49   |     619|       72.49|   1.070/ 10|   1.054/ 13|   1.050/ 14|   1.045/ 15 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  63   |     859|      112.74|   1.024/ 29|   1.018/ 39|   1.016/ 42|   1.015/ 46 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  33   |      44|       24.78|   1.080/  9|   1.047/ 15|   1.040/ 17|   1.033/ 21 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  43   |     328|       56.26|   1.036/ 19|   1.030/ 23|   1.029/ 24|   1.028/ 25 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  19   |       7|       12.09|   1.225/  3|   1.001/ **|   1.000/ --|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  41   |      69|        2.13|   1.063/ 11|   1.060/ 11|   1.060/ 11|   1.059/ 12 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  52   |      31|       10.72|   1.016/ 44|   1.018/ 38|   1.019/ 37|   1.020/ 35 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  51   |     466|       10.84|   1.019/ 37|   1.010/ 70|   1.008/ 87|   1.006/ ** |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  34   |       2|        0.06|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  55   |     238|        5.29|   1.047/ 15|   1.038/ 18|   1.036/ 19|   1.034/ 20 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  37   |      33|       11.28|   1.041/ 17|   1.031/ 22|   1.029/ 24|   1.026/ 27 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  62   |      94|        3.66|   1.028/ 25|   1.026/ 26|   1.026/ 27|   1.026/ 27 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  51   |     614|       68.97|   1.024/ 28|   1.016/ 42|   1.014/ 48|   1.013/ 55 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  50   |      26|        2.54|   1.032/ 22|   1.020/ 35|   1.017/ 40|   1.014/ 48 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  47   |       8|        5.37|   1.011/ 64|   1.005/ **|   1.004/ **|   1.002/ ** |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  45   |     191|        1.14|   1.070/ 10|   1.031/ 22|   1.022/ 32|   1.012/ 59 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  32   |      94|        9.94|   1.058/ 12|   1.056/ 12|   1.056/ 12|   1.056/ 12 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  52   |    8293|      719.56|   1.033/ 21|   1.016/ 42|   1.012/ 56|   1.008/ 84 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  26   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  34   |      65|        5.70|   1.059/ 12|   1.060/ 11|   1.059/ 12|   1.058/ 12 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  42   |      69|       21.05|   1.032/ 21|   1.034/ 20|   1.035/ 20|   1.035/ 19 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  32   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  46   |    6480|       30.65|   1.087/  8|   1.084/  8|   1.084/  8|   1.084/  8 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  52   |      69|        9.93|   1.042/ 16|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  45   |      45|        2.16|   1.019/ 36|   1.008/ 83|   1.006/ **|   1.003/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  19   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  38   |      68|        2.58|   1.078/  9|   1.030/ 23|   1.019/ 36|   1.008/ 87 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  54   |    3923|      103.24|   1.076/  9|   1.055/ 12|   1.049/ 14|   1.044/ 16 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  41   |     240|       12.57|   1.054/ 13|   1.042/ 16|   1.040/ 17|   1.037/ 19 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  52   |    3359|        2.40|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  41   |     311|        6.30|   1.052/ 13|   1.045/ 15|   1.043/ 16|   1.042/ 16 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  44   |       7|        1.30|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  44   |      73|       17.86|   1.052/ 13|   1.047/ 15|   1.046/ 15|   1.046/ 15 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  45   |      68|        6.07|   1.059/ 12|   1.041/ 17|   1.037/ 19|   1.032/ 21 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  49   |     471|       80.87|   1.024/ 29|   1.018/ 39|   1.016/ 43|   1.015/ 47 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  46   |     317|       30.65|   1.029/ 23|   1.020/ 35|   1.018/ 39|   1.015/ 46 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  49   |     928|       53.15|   1.054/ 13|   1.061/ 11|   1.063/ 11|   1.065/ 10 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  55   |     417|        4.16|   1.050/ 14|   1.043/ 16|   1.042/ 16|   1.041/ 17 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  32   |      10|        1.49|   1.023/ 30|   1.046/ 15|   1.051/ 13|   1.057/ 12 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  10   |       1|        0.74|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  27   |       3|        0.03|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  42   |     248|       44.90|   1.053/ 13|   1.033/ 21|   1.027/ 25|   1.022/ 32 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  77   |   29206|      435.42|   1.019/ 36|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  43   |       1|        0.46|   1.210/  3|   1.057/ 12|   1.007/ 94|   1.000/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  40   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  28   |       7|        1.80|   1.056/ 12|   1.035/ 20|   1.029/ 23|   1.024/ 29 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  54   |    7233|       86.99|   1.036/ 19|   1.023/ 30|   1.020/ 35|   1.017/ 42 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  42   |      16|        0.53|   1.061/ 11|   1.097/  7|   1.106/  6|   1.116/  6 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  52   |     146|       13.61|   1.019/ 36|   1.015/ 46|   1.014/ 49|   1.013/ 54 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  47   |      19|        1.12|   1.077/  9|   1.063/ 11|   1.059/ 12|   1.054/ 13 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  17   |       7|        0.57|   1.041/ 17|   1.009/ 74|   1.000/ **|   1.000/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  27   |       8|        0.67|   1.086/  8|   1.058/ 12|   1.052/ 13|   1.048/ 14 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  37   |      74|        8.05|   1.047/ 15|   1.047/ 14|   1.048/ 14|   1.048/ 14 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  48   |     348|       35.64|   1.054/ 13|   1.034/ 20|   1.028/ 24|   1.023/ 30 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  52   |    1241|        0.91|   1.070/ 10|   1.064/ 11|   1.062/ 11|   1.061/ 11 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  52   |     868|        3.25|   1.034/ 20|   1.019/ 36|   1.016/ 44|   1.012/ 57 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  72   |    6316|       75.75|   1.015/ 46|   1.011/ 62|   1.010/ 67|   1.009/ 74 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  59   |      93|        2.38|   1.012/ 57|   1.011/ 62|   1.011/ 63|   1.011/ 63 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  52   |    1433|      291.18|   1.064/ 11|   1.047/ 15|   1.042/ 16|   1.037/ 18 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  42   |     229|       24.95|   1.030/ 23|   1.017/ 40|   1.014/ 48|   1.012/ 58 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  71   |   29611|      491.57|   1.016/ 43|   1.011/ 61|   1.010/ 68|   1.009/ 77 |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  44   |       8|        2.96|   1.036/ 19|   1.031/ 22|   1.030/ 23|   1.028/ 24 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  79   |     517|        4.10|   1.066/ 10|   1.063/ 11|   1.061/ 11|   1.060/ 11 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  36   |       8|        0.74|   1.011/ 65|   1.024/ 28|   1.028/ 24|   1.032/ 22 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  38   |      27|        1.45|   1.034/ 20|   1.016/ 43|   1.010/ 66|   1.004/ ** |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  37   |      16|        0.34|   1.020/ 35|   1.014/ 50|   1.014/ 50|   1.014/ 48 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  37   |      16|        8.82|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  28   |      30|        6.77|   1.139/  5|   1.083/  8|   1.071/ 10|   1.058/ 12 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  29   |       8|        1.24|   1.038/ 18|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  29   |      16|        8.35|   1.050/ 14|   1.053/ 13|   1.056/ 12|   1.059/ 12 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  53   |      24|        3.59|   1.010/ 68|   1.010/ 70|   1.010/ 70|   1.010/ 71 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  28   |      18|        4.07|   1.076/  9|   1.099/  7|   1.102/  7|   1.104/  6 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  30   |       3|        0.42|   1.194/  3|   1.089/  8|   1.063/ 11|   1.037/ 18 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  42   |      46|       16.60|   1.026/ 27|   1.018/ 39|   1.016/ 44|   1.014/ 49 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  46   |     104|        3.18|   1.013/ 52|   1.009/ 75|   1.008/ 84|   1.007/ 96 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  34   |      28|        1.38|   1.049/ 14|   1.038/ 18|   1.034/ 20|   1.030/ 23 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  33   |       1|        0.25|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  44   |    2156|       17.03|   1.103/  7|   1.086/  8|   1.081/  8|   1.076/  9 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  45   |     126|       46.84|   1.061/ 11|   1.047/ 14|   1.044/ 16|   1.041/ 17 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  53   |     176|        4.90|   1.018/ 38|   1.013/ 55|   1.011/ 62|   1.010/ 71 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  57   |    5140|      294.45|   1.027/ 26|   1.019/ 37|   1.016/ 42|   1.014/ 48 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  34   |      21|        4.24|   1.055/ 12|   1.017/ 40|   1.006/ **|   1.000/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  36   |       3|        0.46|   1.145/  5|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  38   |      35|        1.56|   1.053/ 13|   1.042/ 17|   1.038/ 18|   1.035/ 20 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  40   |      63|        0.31|   1.104/  6|   1.107/  6|   1.108/  6|   1.109/  6 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  41   |      78|       37.38|   1.038/ 18|   1.047/ 15|   1.049/ 14|   1.052/ 13 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  49   |     222|       41.36|   1.021/ 32|   1.009/ 73|   1.006/ **|   1.003/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  32   |      11|        2.41|   1.050/ 14|   1.021/ 33|   1.013/ 52|   1.006/ ** |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  44   |     414|        1.89|   1.082/  8|   1.075/  9|   1.074/  9|   1.072/  9 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  52   |     200|       47.44|   1.042/ 16|   1.033/ 21|   1.030/ 23|   1.028/ 25 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  42   |      10|        1.37|   1.016/ 43|   1.016/ 43|   1.016/ 43|   1.016/ 43 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  43   |    1143|       35.58|   1.095/  7|   1.087/  8|   1.085/  8|   1.084/  8 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  90   |     739|        6.81|   1.030/ 23|   1.019/ 36|   1.017/ 41|   1.014/ 49 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  51   |     695|       18.10|   1.054/ 13|   1.045/ 15|   1.043/ 16|   1.041/ 17 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  46   |    1045|      101.68|   1.033/ 21|   1.025/ 28|   1.023/ 31|   1.021/ 34 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  35   |      11|        3.94|   1.025/ 28|   1.011/ 65|   1.007/ 94|   1.005/ ** |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  41   |     756|       38.94|   1.044/ 16|   1.039/ 18|   1.038/ 18|   1.036/ 19 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  44   |    1221|        8.32|   1.112/  6|   1.092/  7|   1.087/  8|   1.083/  8 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  39   |     173|        5.05|   1.049/ 14|   1.041/ 17|   1.039/ 18|   1.037/ 19 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  31   |      10|        0.62|   1.106/  6|   1.035/ 19|   1.017/ 42|   1.000/ -- |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  43   |     149|       21.45|   1.007/ 96|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  42   |      15|        2.65|   1.029/ 24|   1.037/ 19|   1.039/ 18|   1.042/ 17 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  35   |      24|        4.35|   1.062/ 11|   1.063/ 11|   1.063/ 11|   1.063/ 11 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  49   |      94|       44.80|   1.025/ 27|   1.017/ 41|   1.015/ 47|   1.013/ 54 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  24   |      32|        2.00|   1.204/  3|   1.084/  8|   1.039/ 18|   1.000/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  36   |     115|        1.96|   1.065/ 10|   1.058/ 12|   1.055/ 12|   1.053/ 13 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  60   |   25552|      542.50|   1.017/ 40|   1.012/ 57|   1.011/ 64|   1.010/ 72 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  35   |       7|        0.32|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  50   |      36|        0.85|   1.103/  7|   1.120/  6|   1.125/  5|   1.129/  5 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  52   |    2843|      274.99|   1.050/ 14|   1.036/ 19|   1.032/ 22|   1.028/ 25 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  58   |    1843|      214.23|   1.022/ 32|   1.014/ 50|   1.012/ 57|   1.010/ 68 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  34   |       2|        0.11|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  32   |      15|        0.27|   1.057/ 12|   1.107/  6|   1.123/  5|   1.141/  5 |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  62   |      58|        0.87|   1.016/ 42|   1.005/ **|   1.002/ **|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  36   |       8|        1.04|   1.031/ 22|   1.067/ 10|   1.076/  9|   1.087/  8 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  38   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  44   |      41|        3.46|   1.009/ 76|   1.009/ 80|   1.009/ 78|   1.009/ 76 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  46   |    3450|       41.49|   1.047/ 15|   1.032/ 22|   1.028/ 25|   1.024/ 29 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  63   |   73958|      224.42|   1.048/ 14|   1.028/ 25|   1.022/ 31|   1.017/ 40 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  50   |     283|        6.77|   1.060/ 11|   1.050/ 14|   1.048/ 14|   1.045/ 15 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  43   |     114|       11.54|   1.088/  8|   1.089/  8|   1.089/  8|   1.089/  8 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  52   |   27165|      408.89|   1.051/ 13|   1.051/ 13|   1.052/ 13|   1.052/ 13 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  34   |      17|        4.95|   1.051/ 13|   1.042/ 16|   1.040/ 17|   1.037/ 18 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  36   |      10|        0.28|   1.059/ 12|   1.033/ 21|   1.025/ 27|   1.018/ 38 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  36   |      10|        0.32|   1.007/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  30   |       3|        0.17|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  40   |       4|        0.28|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |

