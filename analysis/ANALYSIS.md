# State and Country COVID-19 Analysis #
## Updated: 2020-05-11 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  58   |   27555|     1416.45|   1.014/ 48|   1.009/ 79|   1.007/ 94|   1.006/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  62   |    9919|     1116.74|   1.032/ 22|   1.023/ 30|   1.020/ 34|   1.018/ 38 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  52   |    5270|      758.32|   1.042/ 16|   1.028/ 24|   1.025/ 28|   1.022/ 32 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  53   |    4751|      475.73|   1.024/ 28|   1.016/ 44|   1.013/ 52|   1.011/ 62 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  53   |    4050|      316.39|   1.053/ 13|   1.048/ 14|   1.047/ 15|   1.045/ 15 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  55   |    3532|      278.75|   1.043/ 16|   1.038/ 18|   1.037/ 19|   1.035/ 19 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  53   |    3124|      876.30|   1.034/ 20|   1.023/ 30|   1.020/ 34|   1.018/ 39 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  68   |    2963|       74.99|   1.035/ 20|   1.025/ 28|   1.022/ 31|   1.020/ 35 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  58   |    2384|      512.92|   1.022/ 32|   1.015/ 45|   1.014/ 50|   1.012/ 56 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  64   |    1803|       83.97|   1.036/ 19|   1.030/ 23|   1.029/ 24|   1.028/ 25 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  72   |   87358|      265.09|   1.027/ 26|   1.016/ 43|   1.014/ 51|   1.011/ 63 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  61   |   34673|      521.90|   1.025/ 28|   1.017/ 40|   1.016/ 44|   1.014/ 50 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  80   |   31878|      529.19|   1.010/ 69|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  69   |   27427|      582.31|   1.010/ 68|   1.007/ **|   1.006/ **|   1.005/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  86   |   29389|      438.14|   1.008/ 90|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  55   |   11521|       54.49|   1.073/  9|   1.067/ 10|   1.066/ 10|   1.065/ 11 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  61   |    8966|      777.97|   1.016/ 43|   1.009/ 73|   1.008/ 87|   1.006/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  63   |    7991|       96.10|   1.018/ 38|   1.010/ 67|   1.009/ 81|   1.007/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  81   |    6838|       82.01|   1.011/ 65|   1.008/ 84|   1.008/ 90|   1.007/ 97 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  66   |    5714|      327.32|   1.015/ 46|   1.010/ 70|   1.009/ 80|   1.007/ 94 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  47   |     403|       82.27|   1.045/ 15|   1.045/ 15|   1.045/ 15|   1.045/ 15 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  47   |      10|       13.57|   1.009/ 81|   1.014/ 50|   1.015/ 46|   1.017/ 42 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  51   |     524|       72.03|   1.056/ 12|   1.063/ 11|   1.065/ 10|   1.068/ 10 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  48   |      98|       32.61|   1.041/ 17|   1.033/ 21|   1.030/ 23|   1.028/ 25 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  68   |    2963|       74.99|   1.035/ 20|   1.025/ 28|   1.022/ 31|   1.020/ 35 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  58   |    1065|      184.97|   1.029/ 24|   1.016/ 43|   1.013/ 53|   1.010/ 71 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  53   |    3124|      876.30|   1.034/ 20|   1.023/ 30|   1.020/ 34|   1.018/ 39 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  46   |     235|      241.70|   1.049/ 14|   1.036/ 19|   1.033/ 21|   1.029/ 23 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  64   |    1803|       83.97|   1.036/ 19|   1.030/ 23|   1.029/ 24|   1.028/ 25 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  60   |    1503|      141.58|   1.029/ 24|   1.022/ 31|   1.020/ 34|   1.019/ 37 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  41   |      18|       12.37|   1.014/ 48|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  46   |      69|       38.71|   1.013/ 51|   1.007/ **|   1.005/ **|   1.004/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  55   |    3532|      278.75|   1.043/ 16|   1.038/ 18|   1.037/ 19|   1.035/ 19 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  56   |    1596|      237.01|   1.047/ 15|   1.041/ 17|   1.040/ 17|   1.038/ 18 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  47   |     273|       86.44|   1.059/ 12|   1.052/ 13|   1.051/ 13|   1.049/ 14 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  59   |     180|       61.82|   1.026/ 26|   1.021/ 33|   1.020/ 34|   1.019/ 36 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  56   |     318|       71.25|   1.029/ 24|   1.023/ 30|   1.022/ 32|   1.020/ 34 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  58   |    2384|      512.92|   1.022/ 32|   1.015/ 45|   1.014/ 50|   1.012/ 56 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  45   |      66|       48.99|   1.022/ 31|   1.015/ 46|   1.013/ 51|   1.012/ 58 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  53   |    1740|      287.80|   1.047/ 15|   1.034/ 20|   1.032/ 22|   1.029/ 24 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  52   |    5270|      758.32|   1.042/ 16|   1.028/ 24|   1.025/ 28|   1.022/ 32 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  53   |    4751|      475.73|   1.024/ 28|   1.016/ 44|   1.013/ 52|   1.011/ 62 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  51   |     615|      109.09|   1.061/ 11|   1.047/ 15|   1.044/ 16|   1.040/ 17 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  53   |     437|      146.72|   1.050/ 14|   1.052/ 13|   1.052/ 13|   1.053/ 13 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  53   |     511|       83.18|   1.042/ 16|   1.038/ 18|   1.037/ 18|   1.037/ 19 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  45   |      16|       15.36|   1.008/ 89|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  44   |      96|       49.87|   1.043/ 16|   1.029/ 23|   1.026/ 27|   1.022/ 31 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  56   |     323|      104.72|   1.031/ 22|   1.026/ 26|   1.025/ 28|   1.024/ 29 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  49   |     131|       96.50|   1.067/ 10|   1.075/  9|   1.077/  9|   1.080/  9 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  62   |    9919|     1116.74|   1.032/ 22|   1.023/ 30|   1.020/ 34|   1.018/ 38 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  47   |     207|       98.73|   1.055/ 12|   1.044/ 16|   1.041/ 17|   1.038/ 18 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  58   |   27555|     1416.45|   1.014/ 48|   1.009/ 79|   1.007/ 94|   1.006/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  47   |     576|       54.91|   1.042/ 16|   1.035/ 20|   1.033/ 21|   1.031/ 22 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  45   |      36|       47.29|   1.058/ 12|   1.059/ 12|   1.059/ 12|   1.059/ 12 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  52   |    1434|      122.66|   1.045/ 15|   1.036/ 19|   1.034/ 20|   1.032/ 21 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  53   |     282|       71.16|   1.025/ 27|   1.019/ 37|   1.017/ 40|   1.016/ 44 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  57   |     130|       30.85|   1.026/ 27|   1.023/ 30|   1.022/ 31|   1.022/ 32 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  53   |    4050|      316.39|   1.053/ 13|   1.048/ 14|   1.047/ 15|   1.045/ 15 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  51   |     112|       35.04|   1.024/ 29|   1.019/ 37|   1.017/ 40|   1.016/ 42 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  44   |     442|      417.12|   1.049/ 14|   1.045/ 15|   1.044/ 16|   1.043/ 16 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  56   |     370|       71.90|   1.044/ 16|   1.034/ 20|   1.031/ 22|   1.028/ 24 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  61   |      37|       41.27|   1.054/ 13|   1.055/ 12|   1.056/ 12|   1.056/ 12 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  51   |     252|       36.93|   1.023/ 30|   1.020/ 35|   1.019/ 37|   1.018/ 38 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  55   |    1118|       38.56|   1.036/ 19|   1.032/ 21|   1.031/ 22|   1.030/ 23 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  50   |      67|       20.84|   1.039/ 17|   1.038/ 18|   1.038/ 18|   1.038/ 18 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  52   |      55|       88.50|   1.012/ 60|   1.005/ **|   1.003/ **|   1.001/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  58   |     904|      105.96|   1.049/ 14|   1.040/ 17|   1.037/ 18|   1.035/ 20 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  72   |     958|      125.87|   1.016/ 43|   1.012/ 55|   1.012/ 60|   1.011/ 64 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  42   |      56|       31.28|   1.034/ 20|   1.019/ 36|   1.015/ 46|   1.011/ 64 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  52   |     406|       69.80|   1.027/ 25|   1.025/ 27|   1.025/ 28|   1.024/ 28 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  28   |       7|       12.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  50   |     127|        3.93|   1.064/ 11|   1.060/ 11|   1.059/ 12|   1.057/ 12 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  61   |      32|       11.34|   1.006/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  60   |     505|       11.73|   1.012/ 58|   1.010/ 71|   1.009/ 74|   1.009/ 78 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  43   |       2|        0.06|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  64   |     322|        7.16|   1.037/ 19|   1.031/ 22|   1.030/ 23|   1.029/ 24 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  46   |      46|       15.56|   1.035/ 20|   1.033/ 21|   1.033/ 21|   1.033/ 21 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  71   |     105|        4.11|   1.013/ 53|   1.008/ 89|   1.006/ **|   1.005/ ** |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  60   |     644|       72.35|   1.009/ 74|   1.003/ **|   1.001/ **|   1.000/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  59   |      31|        3.05|   1.027/ 26|   1.028/ 25|   1.028/ 24|   1.029/ 24 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  56   |       8|        5.28|   1.002/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  54   |     224|        1.33|   1.033/ 21|   1.026/ 27|   1.024/ 28|   1.023/ 30 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  41   |     132|       14.04|   1.045/ 15|   1.039/ 18|   1.037/ 18|   1.036/ 19 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  61   |    8966|      777.97|   1.016/ 43|   1.009/ 73|   1.008/ 87|   1.006/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  35   |       2|        0.19|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  43   |     120|       10.45|   1.067/ 10|   1.071/ 10|   1.072/  9|   1.073/  9 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  51   |     102|       31.00|   1.044/ 16|   1.052/ 13|   1.054/ 13|   1.056/ 12 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  41   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  55   |   11521|       54.49|   1.073/  9|   1.067/ 10|   1.066/ 10|   1.065/ 11 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  61   |      95|       13.60|   1.035/ 20|   1.032/ 21|   1.031/ 22|   1.030/ 23 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  54   |      50|        2.37|   1.012/ 59|   1.009/ 74|   1.009/ 78|   1.008/ 83 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  28   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  47   |     113|        4.24|   1.061/ 11|   1.072/  9|   1.076/  9|   1.079/  9 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  63   |    5447|      143.34|   1.047/ 15|   1.033/ 21|   1.030/ 23|   1.027/ 26 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  13   |      32|        1.99|   1.241/  3|   1.181/  4|   1.118/  6|   1.047/ 15 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  50   |     324|       16.97|   1.036/ 19|   1.029/ 24|   1.027/ 26|   1.025/ 28 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  61   |    4637|        3.31|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  50   |     470|        9.51|   1.047/ 15|   1.046/ 15|   1.046/ 15|   1.045/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  53   |       6|        1.22|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  53   |      96|       23.52|   1.032/ 22|   1.022/ 31|   1.020/ 35|   1.017/ 41 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  54   |      81|        7.24|   1.029/ 24|   1.016/ 43|   1.013/ 54|   1.010/ 71 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  58   |     545|       93.64|   1.017/ 40|   1.014/ 49|   1.013/ 52|   1.013/ 55 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  55   |     397|       38.37|   1.025/ 27|   1.023/ 30|   1.023/ 30|   1.023/ 31 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  58   |    2139|      122.45|   1.067/ 10|   1.065/ 11|   1.064/ 11|   1.062/ 11 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  64   |     552|        5.51|   1.035/ 19|   1.030/ 23|   1.028/ 24|   1.027/ 25 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  41   |      18|        2.77|   1.058/ 12|   1.062/ 11|   1.062/ 11|   1.062/ 11 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  19   |       4|        3.05|   1.357/  2|   1.145/  5|   1.000/ --|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  36   |       5|        0.05|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  51   |     280|       50.58|   1.027/ 25|   1.020/ 35|   1.018/ 38|   1.016/ 42 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  86   |   29389|      438.14|   1.008/ 90|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  52   |       9|        4.11|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  49   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  37   |      11|        2.86|   1.047/ 15|   1.036/ 19|   1.032/ 22|   1.028/ 25 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  63   |    7991|       96.10|   1.018/ 38|   1.010/ 67|   1.009/ 81|   1.007/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  51   |      23|        0.74|   1.032/ 22|   1.029/ 24|   1.028/ 25|   1.027/ 26 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  61   |     156|       14.53|   1.010/ 67|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  56   |      27|        1.60|   1.054/ 13|   1.044/ 16|   1.042/ 16|   1.040/ 17 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  26   |      12|        0.98|   1.054/ 13|   1.033/ 21|   1.023/ 31|   1.010/ 67 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  15   |       3|        1.94|   1.000/ --|   1.224/  3|   1.186/  4|   1.145/  5 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  36   |      15|        1.26|   1.071/ 10|   1.056/ 12|   1.050/ 14|   1.044/ 16 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  46   |     115|       12.56|   1.049/ 14|   1.045/ 15|   1.044/ 15|   1.043/ 16 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  57   |     428|       43.82|   1.032/ 22|   1.023/ 30|   1.021/ 33|   1.019/ 36 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  61   |    2279|        1.67|   1.068/ 10|   1.066/ 10|   1.066/ 10|   1.066/ 10 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  61   |     998|        3.74|   1.022/ 31|   1.017/ 40|   1.016/ 43|   1.015/ 47 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  81   |    6838|       82.01|   1.011/ 65|   1.008/ 84|   1.008/ 90|   1.007/ 97 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  68   |     107|        2.73|   1.015/ 46|   1.017/ 42|   1.017/ 41|   1.017/ 40 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  61   |    1628|      330.74|   1.026/ 26|   1.010/ 71|   1.006/ **|   1.002/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  51   |     255|       27.77|   1.015/ 45|   1.012/ 59|   1.011/ 64|   1.010/ 71 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  80   |   31878|      529.19|   1.010/ 69|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  53   |      10|        3.56|   1.021/ 33|   1.010/ 69|   1.007/ 99|   1.004/ ** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  88   |     754|        5.98|   1.043/ 16|   1.034/ 20|   1.032/ 22|   1.030/ 23 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  45   |       9|        0.89|   1.013/ 52|   1.006/ **|   1.004/ **|   1.002/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  47   |      32|        1.70|   1.022/ 32|   1.019/ 37|   1.018/ 38|   1.018/ 38 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  46   |      33|        0.69|   1.051/ 13|   1.057/ 12|   1.058/ 12|   1.059/ 12 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  46   |      32|       17.90|   1.018/ 39|   1.024/ 28|   1.026/ 27|   1.027/ 25 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  37   |      56|       12.66|   1.077/  9|   1.065/ 11|   1.061/ 11|   1.057/ 12 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  38   |      13|        1.96|   1.037/ 19|   1.040/ 17|   1.040/ 17|   1.039/ 18 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  38   |      19|        9.84|   1.029/ 24|   1.016/ 44|   1.013/ 55|   1.009/ 74 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  62   |      26|        3.86|   1.009/ 77|   1.008/ 86|   1.008/ 88|   1.008/ 91 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  37   |      21|        4.75|   1.044/ 16|   1.008/ 87|   1.000/ --|   1.000/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  39   |       3|        0.47|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  51   |      50|       18.05|   1.013/ 51|   1.010/ 69|   1.009/ 75|   1.008/ 82 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  55   |     110|        3.35|   1.007/ 95|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  43   |      37|        1.84|   1.040/ 17|   1.045/ 15|   1.047/ 15|   1.048/ 14 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  42   |       1|        0.25|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  53   |    3648|       28.82|   1.073/  9|   1.066/ 10|   1.064/ 11|   1.063/ 11 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  54   |     169|       63.04|   1.041/ 17|   1.036/ 19|   1.034/ 20|   1.033/ 21 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  62   |     192|        5.36|   1.012/ 59|   1.009/ 78|   1.008/ 84|   1.008/ 92 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  66   |    5714|      327.32|   1.015/ 46|   1.010/ 70|   1.009/ 80|   1.007/ 94 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  43   |      21|        4.31|   1.011/ 64|   1.006/ **|   1.005/ **|   1.003/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  45   |       6|        0.86|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  47   |      46|        2.08|   1.039/ 18|   1.036/ 19|   1.035/ 19|   1.035/ 20 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  49   |     149|        0.72|   1.091/  7|   1.082/  8|   1.079/  9|   1.077/  9 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  50   |      98|       47.03|   1.026/ 26|   1.016/ 42|   1.014/ 50|   1.011/ 64 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  58   |     225|       41.97|   1.007/ 99|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  41   |      17|        3.58|   1.043/ 16|   1.059/ 12|   1.063/ 11|   1.067/ 10 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  53   |     700|        3.19|   1.063/ 11|   1.054/ 13|   1.052/ 13|   1.050/ 14 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  61   |     248|       58.85|   1.030/ 23|   1.026/ 27|   1.025/ 28|   1.024/ 29 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  51   |      10|        1.44|   1.007/ **|   1.002/ **|   1.000/ **|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  52   |    2026|       63.04|   1.070/ 10|   1.059/ 11|   1.057/ 12|   1.054/ 13 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  99   |     835|        7.69|   1.024/ 29|   1.018/ 38|   1.017/ 41|   1.016/ 44 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  60   |     858|       22.35|   1.031/ 22|   1.021/ 33|   1.018/ 38|   1.016/ 44 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  55   |    1178|      114.63|   1.018/ 39|   1.011/ 62|   1.010/ 72|   1.008/ 87 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  44   |      13|        4.83|   1.019/ 36|   1.022/ 32|   1.022/ 31|   1.022/ 31 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  50   |     987|       50.86|   1.033/ 21|   1.028/ 24|   1.027/ 25|   1.026/ 26 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  53   |    2058|       14.02|   1.072/ 10|   1.056/ 12|   1.052/ 13|   1.049/ 14 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  48   |     247|        7.23|   1.043/ 16|   1.043/ 16|   1.042/ 16|   1.043/ 16 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  40   |      16|        0.97|   1.059/ 12|   1.092/  7|   1.101/  7|   1.110/  6 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  52   |     231|       33.21|   1.015/ 47|   1.019/ 37|   1.020/ 35|   1.021/ 33 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  18   |      20|        2.49|   1.086/  8|   1.138/  5|   1.098/  7|   1.049/ 14 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  51   |      22|        3.78|   1.033/ 21|   1.029/ 24|   1.027/ 25|   1.026/ 27 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  44   |      28|        5.11|   1.026/ 26|   1.009/ 76|   1.005/ **|   1.001/ ** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  58   |     105|       50.17|   1.014/ 49|   1.010/ 68|   1.009/ 76|   1.008/ 85 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  33   |      51|        3.19|   1.057/ 12|   1.064/ 11|   1.065/ 10|   1.067/ 10 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  45   |     196|        3.33|   1.061/ 11|   1.062/ 11|   1.062/ 11|   1.063/ 11 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  69   |   27427|      582.31|   1.010/ 68|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  44   |       9|        0.42|   1.002/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  59   |      73|        1.72|   1.098/  7|   1.097/  7|   1.097/  7|   1.097/  7 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  61   |    3397|      328.61|   1.029/ 23|   1.021/ 33|   1.019/ 36|   1.017/ 40 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  67   |    1923|      223.49|   1.009/ 78|   1.003/ **|   1.002/ **|   1.000/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  43   |       3|        0.17|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  41   |      21|        0.38|   1.043/ 16|   1.054/ 13|   1.058/ 12|   1.061/ 11 |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  71   |      58|        0.87|   1.005/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  45   |      11|        1.43|   1.022/ 32|   1.029/ 24|   1.030/ 23|   1.032/ 22 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  47   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  53   |      45|        3.87|   1.011/ 63|   1.012/ 56|   1.013/ 55|   1.013/ 54 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  55   |    3973|       47.78|   1.023/ 30|   1.013/ 52|   1.011/ 63|   1.009/ 80 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  72   |   87358|      265.09|   1.027/ 26|   1.016/ 43|   1.014/ 51|   1.011/ 63 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  59   |     399|        9.52|   1.045/ 15|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  52   |     207|       20.89|   1.072/  9|   1.062/ 11|   1.060/ 11|   1.057/ 12 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  61   |   34673|      521.90|   1.025/ 28|   1.017/ 40|   1.016/ 44|   1.014/ 50 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  43   |      19|        5.30|   1.020/ 34|   1.011/ 60|   1.009/ 73|   1.008/ 90 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  45   |      11|        0.31|   1.019/ 37|   1.006/ **|   1.002/ **|   1.000/ -- |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  45   |      10|        0.31|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  39   |       4|        0.23|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  49   |       4|        0.27|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |

