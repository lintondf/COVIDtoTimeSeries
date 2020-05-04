# State and Country COVID-19 Analysis #
## Updated: 2020-05-04 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  51   |   26328|     1353.39|   1.027/ 26|   1.008/ 83|   1.004/ **|   1.000/ -- |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  55   |    8395|      945.13|   1.049/ 14|   1.035/ 20|   1.031/ 22|   1.028/ 24 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  46   |    4255|      426.02|   1.040/ 17|   1.030/ 23|   1.027/ 25|   1.025/ 28 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  45   |    4335|      623.77|   1.071/ 10|   1.047/ 15|   1.040/ 17|   1.034/ 20 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  46   |    2909|      227.24|   1.067/ 10|   1.049/ 14|   1.046/ 15|   1.042/ 16 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  48   |    2745|      216.63|   1.054/ 13|   1.044/ 16|   1.041/ 17|   1.039/ 18 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  46   |    2669|      748.47|   1.056/ 12|   1.034/ 20|   1.028/ 24|   1.023/ 30 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  61   |    2463|       62.35|   1.050/ 14|   1.036/ 19|   1.033/ 21|   1.029/ 23 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  51   |    2123|      456.58|   1.033/ 21|   1.023/ 30|   1.020/ 34|   1.018/ 39 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  57   |    1473|       68.57|   1.044/ 15|   1.032/ 21|   1.030/ 23|   1.027/ 26 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  65   |   77057|      233.83|   1.041/ 17|   1.023/ 30|   1.018/ 38|   1.013/ 51 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  73   |   30208|      501.47|   1.015/ 47|   1.010/ 67|   1.009/ 75|   1.008/ 84 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  54   |   29402|      442.57|   1.045/ 15|   1.042/ 16|   1.042/ 17|   1.041/ 17 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  62   |   26085|      553.81|   1.015/ 45|   1.011/ 65|   1.010/ 72|   1.008/ 82 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  79   |   29211|      435.50|   1.015/ 47|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  54   |    8438|      732.15|   1.026/ 26|   1.012/ 57|   1.009/ 81|   1.005/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  48   |    7441|       35.20|   1.082/  8|   1.077/  9|   1.076/  9|   1.074/  9 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  56   |    7443|       89.51|   1.030/ 23|   1.017/ 40|   1.014/ 48|   1.011/ 62 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  74   |    6440|       77.24|   1.014/ 51|   1.010/ 68|   1.009/ 74|   1.009/ 81 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  59   |    5300|      303.59|   1.024/ 29|   1.017/ 41|   1.015/ 46|   1.013/ 52 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  40   |     303|       61.70|   1.047/ 14|   1.042/ 16|   1.041/ 17|   1.040/ 17 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  40   |       9|       12.30|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  44   |     363|       49.90|   1.048/ 14|   1.037/ 19|   1.034/ 20|   1.031/ 22 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  41   |      72|       23.74|   1.047/ 15|   1.060/ 11|   1.063/ 11|   1.067/ 10 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  61   |    2463|       62.35|   1.050/ 14|   1.036/ 19|   1.033/ 21|   1.029/ 23 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  51   |     933|      161.97|   1.050/ 14|   1.038/ 18|   1.035/ 20|   1.031/ 22 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  46   |    2669|      748.47|   1.056/ 12|   1.034/ 20|   1.028/ 24|   1.023/ 30 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  39   |     184|      188.64|   1.071/ 10|   1.060/ 11|   1.057/ 12|   1.053/ 13 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  57   |    1473|       68.57|   1.044/ 15|   1.032/ 21|   1.030/ 23|   1.027/ 26 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  53   |    1269|      119.51|   1.041/ 17|   1.030/ 23|   1.028/ 25|   1.026/ 27 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  34   |      18|       12.38|   1.046/ 15|   1.020/ 35|   1.012/ 57|   1.004/ ** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  39   |      66|       36.71|   1.028/ 25|   1.019/ 36|   1.017/ 40|   1.015/ 45 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  48   |    2745|      216.63|   1.054/ 13|   1.044/ 16|   1.041/ 17|   1.039/ 18 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  49   |    1212|      179.99|   1.057/ 12|   1.053/ 13|   1.052/ 13|   1.051/ 13 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  40   |     191|       60.39|   1.070/ 10|   1.066/ 10|   1.065/ 10|   1.064/ 11 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  52   |     153|       52.55|   1.034/ 21|   1.019/ 36|   1.016/ 44|   1.012/ 56 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  49   |     270|       60.33|   1.039/ 18|   1.027/ 26|   1.023/ 30|   1.020/ 34 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  51   |    2123|      456.58|   1.033/ 21|   1.023/ 30|   1.020/ 34|   1.018/ 39 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  38   |      59|       44.15|   1.041/ 17|   1.022/ 32|   1.017/ 41|   1.012/ 59 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  46   |    1397|      231.11|   1.070/ 10|   1.043/ 16|   1.036/ 19|   1.029/ 23 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  45   |    4335|      623.77|   1.071/ 10|   1.047/ 15|   1.040/ 17|   1.034/ 20 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  46   |    4255|      426.02|   1.040/ 17|   1.030/ 23|   1.027/ 25|   1.025/ 28 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  44   |     445|       78.88|   1.087/  8|   1.070/ 10|   1.066/ 10|   1.061/ 11 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  46   |     306|      102.72|   1.048/ 14|   1.042/ 17|   1.040/ 17|   1.039/ 18 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  46   |     405|       66.05|   1.049/ 14|   1.038/ 18|   1.035/ 20|   1.032/ 22 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  38   |      17|       15.83|   1.036/ 19|   1.013/ 55|   1.007/ 93|   1.002/ ** |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  37   |      80|       41.39|   1.078/  9|   1.058/ 12|   1.054/ 13|   1.050/ 14 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  49   |     266|       86.51|   1.038/ 18|   1.033/ 21|   1.032/ 21|   1.031/ 22 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  42   |      85|       62.68|   1.061/ 11|   1.069/ 10|   1.071/ 10|   1.074/  9 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  55   |    8395|      945.13|   1.049/ 14|   1.035/ 20|   1.031/ 22|   1.028/ 24 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  40   |     152|       72.32|   1.078/  9|   1.065/ 10|   1.062/ 11|   1.060/ 11 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  51   |   26328|     1353.39|   1.027/ 26|   1.008/ 83|   1.004/ **|   1.000/ -- |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  40   |     464|       44.24|   1.060/ 11|   1.042/ 16|   1.038/ 18|   1.034/ 20 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  38   |      25|       32.96|   1.065/ 11|   1.061/ 11|   1.061/ 11|   1.061/ 11 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  45   |    1105|       94.57|   1.060/ 11|   1.050/ 14|   1.048/ 14|   1.045/ 15 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  46   |     248|       62.76|   1.038/ 18|   1.030/ 23|   1.028/ 25|   1.026/ 27 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  50   |     113|       26.78|   1.031/ 22|   1.025/ 27|   1.024/ 29|   1.023/ 31 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  46   |    2909|      227.24|   1.067/ 10|   1.049/ 14|   1.046/ 15|   1.042/ 16 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  44   |     101|       31.57|   1.035/ 20|   1.028/ 24|   1.026/ 26|   1.024/ 28 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  37   |     312|      294.87|   1.055/ 12|   1.050/ 14|   1.049/ 14|   1.048/ 14 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  49   |     276|       53.64|   1.064/ 11|   1.071/ 10|   1.073/  9|   1.075/  9 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  54   |      19|       21.59|   1.050/ 14|   1.061/ 11|   1.063/ 11|   1.066/ 10 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  44   |     215|       31.43|   1.027/ 26|   1.023/ 30|   1.022/ 31|   1.021/ 32 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  48   |     904|       31.19|   1.046/ 15|   1.040/ 17|   1.039/ 17|   1.038/ 18 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  43   |      52|       16.25|   1.047/ 14|   1.028/ 24|   1.023/ 30|   1.019/ 37 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  45   |      53|       84.93|   1.025/ 28|   1.019/ 37|   1.017/ 41|   1.016/ 44 |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  51   |     683|       79.98|   1.066/ 10|   1.052/ 13|   1.049/ 14|   1.046/ 15 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  65   |     881|      115.76|   1.021/ 33|   1.015/ 47|   1.013/ 53|   1.012/ 60 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  35   |      49|       27.38|   1.067/ 10|   1.054/ 13|   1.053/ 13|   1.051/ 13 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  45   |     345|       59.30|   1.033/ 21|   1.028/ 24|   1.027/ 25|   1.026/ 26 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  21   |       7|       12.09|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  43   |      79|        2.45|   1.065/ 11|   1.069/ 10|   1.070/ 10|   1.070/ 10 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  54   |      31|       11.01|   1.014/ 49|   1.015/ 47|   1.015/ 46|   1.015/ 45 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  53   |     475|       11.03|   1.016/ 44|   1.009/ 75|   1.008/ 90|   1.006/ ** |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  36   |       2|        0.06|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  57   |     255|        5.68|   1.044/ 16|   1.037/ 19|   1.035/ 19|   1.034/ 20 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  39   |      35|       11.87|   1.037/ 18|   1.030/ 23|   1.028/ 25|   1.026/ 27 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  64   |      98|        3.81|   1.024/ 28|   1.022/ 31|   1.022/ 31|   1.022/ 32 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  53   |     626|       70.35|   1.020/ 34|   1.012/ 56|   1.010/ 67|   1.008/ 83 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  52   |      26|        2.61|   1.028/ 25|   1.019/ 37|   1.017/ 41|   1.015/ 46 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  49   |       8|        5.37|   1.008/ 87|   1.002/ **|   1.001/ **|   1.000/ -- |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  47   |     197|        1.17|   1.055/ 13|   1.021/ 33|   1.013/ 54|   1.004/ ** |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  34   |     102|       10.86|   1.056/ 12|   1.050/ 14|   1.049/ 14|   1.048/ 14 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  54   |    8438|      732.15|   1.026/ 26|   1.012/ 57|   1.009/ 81|   1.005/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  28   |       1|        0.09|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  36   |      73|        6.38|   1.061/ 11|   1.060/ 11|   1.060/ 11|   1.060/ 11 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  44   |      75|       22.65|   1.033/ 21|   1.036/ 19|   1.036/ 19|   1.037/ 18 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  34   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  48   |    7441|       35.20|   1.082/  8|   1.077/  9|   1.076/  9|   1.074/  9 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  54   |      74|       10.69|   1.040/ 17|   1.037/ 18|   1.036/ 19|   1.036/ 19 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  47   |      46|        2.18|   1.016/ 44|   1.008/ 88|   1.006/ **|   1.004/ ** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  21   |       1|        0.09|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  40   |      70|        2.63|   1.055/ 13|   1.021/ 33|   1.013/ 54|   1.005/ ** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  56   |    4271|      112.41|   1.068/ 10|   1.048/ 14|   1.044/ 16|   1.039/ 18 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  43   |     261|       13.67|   1.050/ 14|   1.042/ 16|   1.041/ 17|   1.039/ 18 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  54   |    4798|        3.42|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  43   |     340|        6.89|   1.050/ 14|   1.047/ 15|   1.046/ 15|   1.046/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  46   |       6|        1.27|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  46   |      80|       19.53|   1.050/ 14|   1.048/ 14|   1.048/ 14|   1.048/ 14 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  47   |      72|        6.44|   1.052/ 13|   1.037/ 19|   1.033/ 21|   1.029/ 24 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  51   |     489|       83.96|   1.023/ 30|   1.019/ 37|   1.018/ 39|   1.017/ 42 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  48   |     334|       32.21|   1.029/ 24|   1.024/ 29|   1.023/ 30|   1.022/ 32 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  51   |    1192|       68.22|   1.093/  7|   1.122/  6|   1.130/  5|   1.138/  5 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  57   |     448|        4.47|   1.046/ 15|   1.039/ 18|   1.037/ 19|   1.035/ 19 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  34   |      11|        1.67|   1.034/ 20|   1.051/ 13|   1.056/ 12|   1.060/ 11 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  12   |       1|        0.74|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  29   |       3|        0.03|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  44   |     255|       46.18|   1.045/ 15|   1.026/ 26|   1.021/ 32|   1.017/ 41 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  79   |   29211|      435.50|   1.015/ 47|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  45   |       5|        2.27|   1.171/  4|   1.090/  8|   1.067/ 10|   1.044/ 16 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  42   |       1|        0.43|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  30   |       8|        2.17|   1.045/ 15|   1.075/  9|   1.083/  8|   1.093/  7 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  56   |    7443|       89.51|   1.030/ 23|   1.017/ 40|   1.014/ 48|   1.011/ 62 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  44   |      19|        0.61|   1.051/ 13|   1.062/ 11|   1.065/ 10|   1.068/ 10 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  54   |     149|       13.90|   1.017/ 41|   1.012/ 57|   1.011/ 64|   1.010/ 73 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  49   |      20|        1.20|   1.063/ 11|   1.043/ 16|   1.036/ 19|   1.030/ 23 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  19   |       7|        0.57|   1.034/ 20|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  29   |       9|        0.75|   1.064/ 11|   1.065/ 11|   1.068/ 10|   1.072/  9 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  39   |      81|        8.85|   1.046/ 15|   1.049/ 14|   1.050/ 14|   1.050/ 14 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  50   |     366|       37.49|   1.047/ 14|   1.030/ 23|   1.025/ 27|   1.021/ 33 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  54   |    1409|        1.04|   1.069/ 10|   1.065/ 11|   1.064/ 11|   1.063/ 11 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  54   |     895|        3.35|   1.029/ 23|   1.018/ 39|   1.015/ 47|   1.012/ 59 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  74   |    6440|       77.24|   1.014/ 51|   1.010/ 68|   1.009/ 74|   1.009/ 81 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  61   |      96|        2.45|   1.012/ 57|   1.012/ 58|   1.012/ 57|   1.012/ 57 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  54   |    1513|      307.45|   1.052/ 13|   1.033/ 21|   1.027/ 25|   1.022/ 31 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  44   |     236|       25.70|   1.025/ 27|   1.017/ 41|   1.015/ 46|   1.013/ 52 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  73   |   30208|      501.47|   1.015/ 47|   1.010/ 67|   1.009/ 75|   1.008/ 84 |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  46   |       9|        3.17|   1.037/ 18|   1.035/ 20|   1.034/ 20|   1.034/ 20 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  81   |     570|        4.53|   1.061/ 11|   1.055/ 12|   1.053/ 13|   1.052/ 13 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  38   |       9|        0.81|   1.018/ 38|   1.034/ 20|   1.038/ 18|   1.043/ 16 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  40   |      27|        1.47|   1.027/ 25|   1.010/ 70|   1.005/ **|   1.000/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  39   |      21|        0.43|   1.045/ 15|   1.085/  8|   1.096/  7|   1.108/  6 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  39   |      21|       11.61|   1.026/ 26|   1.054/ 13|   1.062/ 11|   1.070/ 10 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  30   |      36|        8.22|   1.107/  6|   1.098/  7|   1.097/  7|   1.097/  7 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  31   |       8|        1.28|   1.015/ 46|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  31   |      17|        8.77|   1.047/ 15|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  55   |      25|        3.68|   1.011/ 64|   1.011/ 63|   1.011/ 63|   1.011/ 63 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  30   |      20|        4.44|   1.123/  5|   1.068/ 10|   1.052/ 13|   1.035/ 20 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  32   |       3|        0.44|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  44   |      47|       16.96|   1.021/ 33|   1.013/ 52|   1.011/ 60|   1.010/ 71 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  48   |     106|        3.23|   1.012/ 58|   1.009/ 78|   1.008/ 86|   1.007/ 95 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  36   |      29|        1.41|   1.044/ 16|   1.024/ 28|   1.019/ 36|   1.014/ 50 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  35   |       1|        0.25|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  46   |    2434|       19.23|   1.088/  8|   1.069/ 10|   1.064/ 11|   1.059/ 12 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  47   |     134|       50.03|   1.054/ 13|   1.040/ 17|   1.037/ 19|   1.034/ 20 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  55   |     179|        5.00|   1.016/ 44|   1.011/ 65|   1.009/ 74|   1.008/ 86 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  59   |    5300|      303.59|   1.024/ 29|   1.017/ 41|   1.015/ 46|   1.013/ 52 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  36   |      21|        4.25|   1.033/ 21|   1.012/ 56|   1.007/ 96|   1.002/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  38   |       3|        0.52|   1.063/ 11|   1.042/ 16|   1.039/ 17|   1.038/ 18 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  40   |      37|        1.67|   1.047/ 15|   1.037/ 18|   1.034/ 20|   1.031/ 22 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  42   |      82|        0.40|   1.114/  6|   1.132/  5|   1.137/  5|   1.142/  5 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  43   |      84|       40.65|   1.039/ 18|   1.045/ 15|   1.046/ 15|   1.048/ 14 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  51   |     223|       41.51|   1.016/ 42|   1.005/ **|   1.002/ **|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  34   |      12|        2.57|   1.040/ 17|   1.028/ 25|   1.026/ 27|   1.024/ 28 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  46   |     473|        2.16|   1.080/  9|   1.073/  9|   1.072/ 10|   1.070/ 10 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  54   |     210|       49.85|   1.038/ 18|   1.028/ 24|   1.026/ 26|   1.024/ 29 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  44   |      10|        1.41|   1.017/ 42|   1.017/ 40|   1.017/ 40|   1.018/ 39 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  45   |    1328|       41.32|   1.091/  7|   1.082/  8|   1.080/  9|   1.078/  9 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  92   |     762|        7.02|   1.029/ 24|   1.019/ 36|   1.017/ 40|   1.015/ 46 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  53   |     736|       19.19|   1.047/ 15|   1.035/ 20|   1.032/ 21|   1.029/ 24 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  48   |    1082|      105.30|   1.029/ 24|   1.021/ 33|   1.019/ 37|   1.017/ 41 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  37   |      12|        4.25|   1.026/ 26|   1.033/ 21|   1.036/ 19|   1.039/ 17 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  43   |     808|       41.63|   1.042/ 16|   1.036/ 19|   1.035/ 20|   1.034/ 20 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  46   |    1406|        9.58|   1.101/  7|   1.081/  8|   1.076/  9|   1.071/ 10 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  41   |     186|        5.44|   1.046/ 15|   1.040/ 17|   1.038/ 18|   1.036/ 19 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  33   |      10|        0.61|   1.072/  9|   1.011/ 61|   1.000/ --|   1.000/ -- |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  45   |     176|       25.30|   1.005/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  11   |       8|        1.02|   1.432/  1|   1.220/  3|   1.183/  4|   1.080/  8 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  44   |      17|        2.95|   1.036/ 19|   1.050/ 14|   1.054/ 13|   1.057/ 12 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  37   |      25|        4.66|   1.054/ 13|   1.039/ 18|   1.035/ 20|   1.031/ 22 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  51   |      97|       46.29|   1.023/ 30|   1.016/ 43|   1.015/ 47|   1.013/ 52 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  26   |      33|        2.09|   1.167/  4|   1.047/ 15|   1.020/ 35|   1.000/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  38   |     130|        2.21|   1.064/ 11|   1.062/ 11|   1.062/ 11|   1.062/ 11 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  62   |   26085|      553.81|   1.015/ 45|   1.011/ 65|   1.010/ 72|   1.008/ 82 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  37   |       7|        0.32|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  52   |      44|        1.04|   1.111/  6|   1.128/  5|   1.132/  5|   1.137/  5 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  54   |    2968|      287.06|   1.042/ 16|   1.027/ 26|   1.023/ 30|   1.019/ 37 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  60   |    1873|      217.66|   1.018/ 39|   1.010/ 67|   1.008/ 82|   1.007/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  36   |       3|        0.17|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  34   |      17|        0.30|   1.057/ 12|   1.070/ 10|   1.075/  9|   1.080/  8 |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  64   |      58|        0.87|   1.012/ 57|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  38   |       9|        1.18|   1.039/ 17|   1.061/ 11|   1.068/ 10|   1.075/  9 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  40   |       8|        5.87|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  46   |      42|        3.55|   1.009/ 75|   1.011/ 63|   1.012/ 60|   1.012/ 57 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  48   |    3607|       43.38|   1.040/ 17|   1.026/ 26|   1.023/ 30|   1.020/ 35 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  65   |   77057|      233.83|   1.041/ 17|   1.023/ 30|   1.018/ 38|   1.013/ 51 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  52   |     306|        7.31|   1.054/ 13|   1.044/ 16|   1.041/ 17|   1.039/ 18 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  45   |     132|       13.35|   1.084/  8|   1.080/  9|   1.078/  9|   1.077/  9 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  54   |   29402|      442.57|   1.045/ 15|   1.042/ 16|   1.042/ 17|   1.041/ 17 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  36   |      18|        5.13|   1.045/ 15|   1.030/ 23|   1.026/ 26|   1.022/ 31 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  38   |      10|        0.29|   1.048/ 14|   1.023/ 30|   1.017/ 41|   1.011/ 64 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  38   |      10|        0.31|   1.005/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  32   |       3|        0.17|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  42   |       4|        0.28|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |

