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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  54   |   26817|     1378.50|   1.019/ 36|   1.009/ 80|   1.006/ **|   1.004/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  58   |    9077|     1021.97|   1.039/ 18|   1.027/ 26|   1.024/ 29|   1.021/ 33 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  48   |    4752|      683.75|   1.055/ 12|   1.034/ 20|   1.028/ 24|   1.023/ 30 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  49   |    4488|      449.35|   1.032/ 21|   1.021/ 33|   1.018/ 38|   1.016/ 44 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  49   |    3339|      260.84|   1.059/ 12|   1.049/ 14|   1.047/ 15|   1.045/ 15 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  51   |    3044|      240.22|   1.047/ 15|   1.038/ 18|   1.035/ 19|   1.033/ 21 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  49   |    2859|      801.99|   1.044/ 15|   1.028/ 25|   1.024/ 29|   1.020/ 35 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  64   |    2685|       67.96|   1.042/ 16|   1.029/ 24|   1.026/ 27|   1.023/ 30 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  54   |    2244|      482.67|   1.028/ 25|   1.020/ 35|   1.018/ 39|   1.016/ 44 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  60   |    1600|       74.50|   1.038/ 18|   1.028/ 24|   1.026/ 27|   1.024/ 29 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  68   |   81654|      247.78|   1.033/ 21|   1.018/ 39|   1.014/ 49|   1.010/ 67 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  57   |   32002|      481.70|   1.035/ 20|   1.028/ 25|   1.026/ 27|   1.024/ 28 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  76   |   31000|      514.61|   1.012/ 57|   1.008/ 83|   1.007/ 93|   1.006/ ** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  65   |   26689|      566.65|   1.013/ 55|   1.009/ 80|   1.008/ 91|   1.007/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  82   |   29407|      438.41|   1.011/ 62|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  51   |    8923|       42.21|   1.075/  9|   1.066/ 10|   1.064/ 11|   1.062/ 11 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  57   |    8621|      748.10|   1.020/ 34|   1.009/ 74|   1.007/ **|   1.004/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  59   |    7665|       92.18|   1.023/ 30|   1.012/ 57|   1.009/ 73|   1.007/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  77   |    6610|       79.27|   1.012/ 57|   1.009/ 75|   1.008/ 82|   1.008/ 89 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  62   |    5498|      314.93|   1.019/ 36|   1.012/ 56|   1.011/ 64|   1.009/ 76 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  43   |     336|       68.49|   1.042/ 16|   1.038/ 18|   1.037/ 19|   1.035/ 19 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  43   |       9|       12.52|   1.002/ **|   1.004/ **|   1.005/ **|   1.006/ ** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  47   |     409|       56.25|   1.046/ 15|   1.042/ 16|   1.041/ 17|   1.040/ 17 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  44   |      86|       28.55|   1.053/ 13|   1.061/ 11|   1.064/ 11|   1.066/ 10 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  64   |    2685|       67.96|   1.042/ 16|   1.029/ 24|   1.026/ 27|   1.023/ 30 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  54   |    1000|      173.58|   1.040/ 17|   1.026/ 27|   1.022/ 31|   1.018/ 38 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  49   |    2859|      801.99|   1.044/ 15|   1.028/ 25|   1.024/ 29|   1.020/ 35 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  42   |     207|      212.23|   1.061/ 11|   1.044/ 16|   1.039/ 17|   1.035/ 20 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  60   |    1600|       74.50|   1.038/ 18|   1.028/ 24|   1.026/ 27|   1.024/ 29 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  56   |    1378|      129.80|   1.036/ 19|   1.028/ 24|   1.027/ 26|   1.025/ 28 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  37   |      18|       12.52|   1.032/ 22|   1.010/ 68|   1.005/ **|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  42   |      67|       37.76|   1.020/ 34|   1.011/ 61|   1.009/ 75|   1.007/ 98 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  51   |    3044|      240.22|   1.047/ 15|   1.038/ 18|   1.035/ 19|   1.033/ 21 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  52   |    1360|      202.05|   1.049/ 14|   1.043/ 16|   1.041/ 17|   1.040/ 17 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  43   |     223|       70.63|   1.064/ 11|   1.057/ 12|   1.055/ 12|   1.053/ 13 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  55   |     165|       56.78|   1.033/ 21|   1.026/ 26|   1.025/ 28|   1.024/ 29 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  52   |     290|       64.92|   1.034/ 20|   1.025/ 27|   1.023/ 30|   1.021/ 33 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  54   |    2244|      482.67|   1.028/ 25|   1.020/ 35|   1.018/ 39|   1.016/ 44 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  41   |      62|       46.34|   1.031/ 22|   1.019/ 36|   1.016/ 42|   1.014/ 49 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  49   |    1532|      253.47|   1.058/ 12|   1.038/ 18|   1.033/ 21|   1.028/ 24 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  48   |    4752|      683.75|   1.055/ 12|   1.034/ 20|   1.028/ 24|   1.023/ 30 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  49   |    4488|      449.35|   1.032/ 21|   1.021/ 33|   1.018/ 38|   1.016/ 44 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  47   |     515|       91.26|   1.074/  9|   1.055/ 12|   1.050/ 14|   1.045/ 15 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  49   |     352|      118.33|   1.048/ 14|   1.048/ 14|   1.048/ 14|   1.048/ 14 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  49   |     440|       71.68|   1.042/ 16|   1.031/ 22|   1.028/ 24|   1.026/ 27 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  41   |      17|       15.63|   1.018/ 37|   1.004/ **|   1.000/ **|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  40   |      86|       44.46|   1.057/ 12|   1.031/ 22|   1.025/ 27|   1.019/ 37 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  52   |     290|       94.19|   1.034/ 20|   1.030/ 23|   1.028/ 24|   1.027/ 25 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  45   |      97|       71.40|   1.053/ 13|   1.049/ 14|   1.048/ 14|   1.046/ 15 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  58   |    9077|     1021.97|   1.039/ 18|   1.027/ 26|   1.024/ 29|   1.021/ 33 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  43   |     176|       84.17|   1.068/ 10|   1.055/ 12|   1.052/ 13|   1.050/ 14 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  54   |   26817|     1378.50|   1.019/ 36|   1.009/ 80|   1.006/ **|   1.004/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  43   |     504|       48.09|   1.048/ 14|   1.033/ 21|   1.030/ 23|   1.026/ 26 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  41   |      29|       37.68|   1.056/ 12|   1.051/ 13|   1.051/ 14|   1.050/ 14 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  48   |    1241|      106.13|   1.051/ 13|   1.042/ 16|   1.039/ 18|   1.037/ 19 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  49   |     262|       66.16|   1.030/ 23|   1.021/ 33|   1.018/ 38|   1.016/ 43 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  53   |     119|       28.17|   1.026/ 27|   1.019/ 36|   1.018/ 39|   1.016/ 43 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  49   |    3339|      260.84|   1.059/ 12|   1.049/ 14|   1.047/ 15|   1.045/ 15 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  47   |     105|       32.83|   1.027/ 26|   1.017/ 41|   1.014/ 48|   1.012/ 60 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  40   |     370|      348.89|   1.054/ 13|   1.056/ 12|   1.057/ 12|   1.058/ 12 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  52   |     322|       62.54|   1.056/ 12|   1.054/ 13|   1.053/ 13|   1.052/ 13 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  57   |      26|       29.07|   1.058/ 12|   1.064/ 11|   1.065/ 10|   1.067/ 10 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  47   |     233|       34.08|   1.027/ 25|   1.027/ 26|   1.027/ 26|   1.027/ 26 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  51   |     989|       34.12|   1.039/ 17|   1.033/ 21|   1.031/ 22|   1.029/ 23 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  46   |      57|       17.88|   1.041/ 17|   1.032/ 22|   1.030/ 23|   1.028/ 25 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  48   |      54|       87.20|   1.018/ 38|   1.011/ 66|   1.009/ 80|   1.007/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  54   |     777|       91.06|   1.057/ 12|   1.045/ 15|   1.042/ 16|   1.039/ 18 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  68   |     912|      119.80|   1.017/ 40|   1.012/ 59|   1.010/ 67|   1.009/ 78 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  38   |      53|       29.39|   1.048/ 14|   1.032/ 22|   1.028/ 25|   1.023/ 30 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  48   |     368|       63.29|   1.028/ 25|   1.023/ 30|   1.022/ 31|   1.021/ 33 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  24   |       7|       12.09|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  46   |     100|        3.11|   1.072/  9|   1.080/  9|   1.082/  8|   1.084/  8 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  57   |      32|       11.25|   1.010/ 68|   1.008/ 83|   1.008/ 89|   1.007/ 96 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  56   |     486|       11.30|   1.013/ 54|   1.008/ 84|   1.007/ 96|   1.006/ ** |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  39   |       2|        0.06|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  60   |     284|        6.33|   1.042/ 16|   1.037/ 19|   1.035/ 19|   1.034/ 20 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  42   |      40|       13.56|   1.039/ 17|   1.042/ 16|   1.044/ 16|   1.045/ 15 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  67   |     103|        3.99|   1.020/ 34|   1.017/ 40|   1.016/ 42|   1.016/ 44 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  56   |     638|       71.69|   1.015/ 47|   1.007/ 97|   1.005/ **|   1.003/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  55   |      28|        2.75|   1.024/ 28|   1.019/ 36|   1.018/ 39|   1.017/ 41 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  52   |       8|        5.34|   1.005/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  50   |     204|        1.21|   1.038/ 18|   1.014/ 49|   1.009/ 81|   1.003/ ** |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  37   |     114|       12.13|   1.050/ 14|   1.041/ 17|   1.039/ 18|   1.037/ 19 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  57   |    8621|      748.10|   1.020/ 34|   1.009/ 74|   1.007/ **|   1.004/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  31   |       1|        0.09|   1.173/  4|   1.098/  7|   1.063/ 11|   1.022/ 31 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  39   |      90|        7.86|   1.065/ 11|   1.069/ 10|   1.071/ 10|   1.073/  9 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  47   |      83|       25.27|   1.034/ 20|   1.036/ 19|   1.037/ 19|   1.038/ 18 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  37   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  51   |    8923|       42.21|   1.075/  9|   1.066/ 10|   1.064/ 11|   1.062/ 11 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  57   |      84|       12.01|   1.041/ 17|   1.040/ 17|   1.040/ 17|   1.039/ 17 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  50   |      48|        2.28|   1.016/ 44|   1.014/ 49|   1.014/ 50|   1.014/ 50 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  24   |       1|        0.09|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  43   |      71|        2.66|   1.035/ 20|   1.021/ 34|   1.017/ 41|   1.013/ 52 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  59   |    4771|      125.56|   1.058/ 12|   1.041/ 17|   1.037/ 19|   1.033/ 21 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  46   |     292|       15.27|   1.045/ 15|   1.039/ 18|   1.037/ 18|   1.036/ 19 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  57   |    4887|        3.48|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  46   |     394|        7.97|   1.049/ 14|   1.049/ 14|   1.050/ 14|   1.050/ 14 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  49   |       6|        1.22|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  49   |      88|       21.67|   1.042/ 16|   1.037/ 18|   1.036/ 19|   1.035/ 20 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  50   |      77|        6.84|   1.040/ 17|   1.023/ 31|   1.018/ 38|   1.014/ 50 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  54   |     516|       88.60|   1.021/ 33|   1.018/ 38|   1.017/ 40|   1.017/ 41 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  51   |     361|       34.87|   1.028/ 24|   1.026/ 26|   1.026/ 27|   1.026/ 27 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  54   |    1640|       93.88|   1.093/  7|   1.111/  6|   1.116/  6|   1.120/  6 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  60   |     492|        4.91|   1.040/ 17|   1.033/ 21|   1.031/ 22|   1.029/ 24 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  37   |      14|        2.17|   1.052/ 13|   1.081/  8|   1.088/  8|   1.096/  7 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  15   |       4|        3.21|   1.000/ --|   1.327/  2|   1.475/  1|   1.592/  1 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  32   |       3|        0.03|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  47   |     266|       48.11|   1.037/ 19|   1.027/ 26|   1.025/ 28|   1.022/ 31 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  82   |   29407|      438.41|   1.011/ 62|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  48   |       7|        3.05|   1.493/  1|   1.505/  1|   1.507/  1|   1.509/  1 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  45   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  33   |      10|        2.57|   1.057/ 12|   1.059/ 12|   1.060/ 11|   1.061/ 11 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  59   |    7665|       92.18|   1.023/ 30|   1.012/ 57|   1.009/ 73|   1.007/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  47   |      21|        0.68|   1.030/ 23|   1.024/ 28|   1.022/ 31|   1.020/ 34 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  57   |     152|       14.21|   1.014/ 50|   1.009/ 77|   1.008/ 90|   1.006/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  52   |      22|        1.34|   1.058/ 12|   1.041/ 17|   1.036/ 19|   1.031/ 22 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  22   |      10|        0.85|   1.002/ **|   1.089/  8|   1.121/  6|   1.152/  4 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  11   |       1|        0.62|   1.000/ --|   1.000/ --|   1.102/  7|   1.238/  3 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  32   |      12|        1.04|   1.065/ 11|   1.104/  7|   1.113/  6|   1.123/  5 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  42   |      95|       10.40|   1.050/ 14|   1.054/ 13|   1.055/ 12|   1.056/ 12 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  53   |     391|       40.04|   1.039/ 18|   1.025/ 27|   1.022/ 31|   1.019/ 37 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  57   |    1756|        1.29|   1.073/  9|   1.074/  9|   1.075/  9|   1.076/  9 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  57   |     931|        3.49|   1.025/ 28|   1.016/ 43|   1.014/ 50|   1.012/ 59 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  77   |    6610|       79.27|   1.012/ 57|   1.009/ 75|   1.008/ 82|   1.008/ 89 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  64   |     100|        2.57|   1.014/ 49|   1.016/ 44|   1.016/ 43|   1.016/ 42 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  57   |    1574|      319.82|   1.038/ 18|   1.018/ 39|   1.013/ 55|   1.007/ 95 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  47   |     245|       26.65|   1.020/ 35|   1.014/ 50|   1.013/ 55|   1.011/ 62 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  76   |   31000|      514.61|   1.012/ 57|   1.008/ 83|   1.007/ 93|   1.006/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  49   |       9|        3.44|   1.037/ 19|   1.033/ 21|   1.032/ 22|   1.031/ 22 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  84   |     657|        5.21|   1.056/ 12|   1.050/ 14|   1.048/ 14|   1.046/ 15 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  41   |       9|        0.87|   1.021/ 33|   1.026/ 27|   1.027/ 26|   1.027/ 25 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  43   |      30|        1.58|   1.028/ 24|   1.024/ 28|   1.024/ 29|   1.024/ 29 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  42   |      26|        0.54|   1.045/ 15|   1.063/ 11|   1.068/ 10|   1.072/  9 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  42   |      27|       15.23|   1.022/ 32|   1.043/ 16|   1.048/ 14|   1.053/ 13 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  33   |      45|       10.13|   1.097/  7|   1.080/  9|   1.076/  9|   1.072/  9 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  34   |      11|        1.66|   1.024/ 28|   1.061/ 11|   1.071/ 10|   1.082/  8 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  34   |      18|        9.24|   1.038/ 18|   1.024/ 28|   1.020/ 34|   1.016/ 44 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  58   |      26|        3.76|   1.009/ 77|   1.008/ 91|   1.007/ 96|   1.007/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  33   |      21|        4.69|   1.083/  8|   1.034/ 20|   1.021/ 33|   1.007/ 92 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  35   |       3|        0.49|   1.145/  5|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  47   |      48|       17.31|   1.016/ 45|   1.009/ 77|   1.007/ 95|   1.006/ ** |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  51   |     108|        3.30|   1.010/ 68|   1.007/ 92|   1.007/ **|   1.006/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  39   |      32|        1.56|   1.040/ 17|   1.039/ 18|   1.039/ 18|   1.040/ 17 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  38   |       1|        0.25|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  49   |    2855|       22.56|   1.077/  9|   1.062/ 11|   1.059/ 12|   1.055/ 12 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  50   |     148|       55.25|   1.046/ 15|   1.036/ 19|   1.033/ 21|   1.031/ 23 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  58   |     186|        5.18|   1.015/ 46|   1.012/ 58|   1.011/ 61|   1.011/ 65 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  62   |    5498|      314.93|   1.019/ 36|   1.012/ 56|   1.011/ 64|   1.009/ 76 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  39   |      21|        4.27|   1.018/ 38|   1.012/ 58|   1.011/ 65|   1.010/ 72 |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  41   |       5|        0.79|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  43   |      40|        1.80|   1.041/ 17|   1.029/ 24|   1.026/ 26|   1.023/ 30 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  45   |     111|        0.54|   1.107/  6|   1.106/  6|   1.106/  6|   1.106/  6 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  46   |      92|       44.23|   1.034/ 20|   1.032/ 22|   1.031/ 22|   1.029/ 23 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  54   |     224|       41.82|   1.011/ 60|   1.003/ **|   1.001/ **|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  37   |      13|        2.79|   1.033/ 21|   1.028/ 24|   1.028/ 25|   1.028/ 25 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  49   |     567|        2.58|   1.072/  9|   1.065/ 11|   1.063/ 11|   1.061/ 11 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  57   |     224|       53.16|   1.032/ 21|   1.024/ 29|   1.022/ 32|   1.020/ 35 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  47   |      10|        1.44|   1.012/ 57|   1.009/ 81|   1.008/ 90|   1.007/ ** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  48   |    1616|       50.28|   1.081/  8|   1.070/ 10|   1.067/ 10|   1.064/ 11 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  95   |     788|        7.26|   1.026/ 27|   1.018/ 37|   1.017/ 41|   1.015/ 46 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  56   |     793|       20.66|   1.039/ 18|   1.027/ 25|   1.024/ 29|   1.021/ 33 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  51   |    1129|      109.88|   1.024/ 29|   1.017/ 42|   1.015/ 47|   1.013/ 54 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  40   |      12|        4.49|   1.020/ 34|   1.020/ 35|   1.020/ 34|   1.020/ 34 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  46   |     885|       45.63|   1.038/ 18|   1.032/ 21|   1.031/ 22|   1.029/ 23 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  49   |    1669|       11.37|   1.085/  8|   1.066/ 10|   1.060/ 11|   1.055/ 12 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  44   |     209|        6.12|   1.044/ 16|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  36   |      11|        0.68|   1.046/ 15|   1.038/ 18|   1.037/ 18|   1.038/ 18 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  48   |     205|       29.49|   1.013/ 54|   1.016/ 42|   1.018/ 39|   1.019/ 37 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  14   |      13|        1.67|   1.205/  3|   1.087/  8|   1.126/  5|   1.163/  4 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  47   |      19|        3.38|   1.038/ 18|   1.045/ 15|   1.046/ 15|   1.048/ 14 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  40   |      27|        4.96|   1.041/ 17|   1.023/ 29|   1.019/ 37|   1.014/ 51 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  54   |     101|       48.36|   1.019/ 36|   1.015/ 48|   1.014/ 51|   1.013/ 55 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  29   |      39|        2.43|   1.078/  9|   1.054/ 13|   1.051/ 13|   1.049/ 14 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  41   |     155|        2.63|   1.063/ 11|   1.060/ 11|   1.060/ 11|   1.060/ 11 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  65   |   26689|      566.65|   1.013/ 55|   1.009/ 80|   1.008/ 91|   1.007/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  40   |       8|        0.35|   1.016/ 44|   1.042/ 16|   1.049/ 14|   1.056/ 12 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  55   |      55|        1.29|   1.123/  5|   1.140/  5|   1.145/  5|   1.149/  4 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  57   |    3126|      302.35|   1.034/ 20|   1.020/ 34|   1.017/ 40|   1.014/ 50 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  63   |    1901|      220.93|   1.013/ 52|   1.007/ **|   1.005/ **|   1.003/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  39   |       3|        0.17|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  37   |      18|        0.32|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  67   |      57|        0.86|   1.008/ 89|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  41   |      10|        1.29|   1.018/ 37|   1.016/ 44|   1.015/ 46|   1.014/ 49 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  43   |       8|        5.87|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  49   |      43|        3.68|   1.010/ 70|   1.012/ 59|   1.012/ 57|   1.013/ 55 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  51   |    3782|       45.48|   1.032/ 22|   1.019/ 35|   1.016/ 42|   1.013/ 51 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  68   |   81654|      247.78|   1.033/ 21|   1.018/ 39|   1.014/ 49|   1.010/ 67 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  55   |     342|        8.16|   1.048/ 14|   1.040/ 17|   1.038/ 18|   1.036/ 19 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  48   |     163|       16.44|   1.081/  8|   1.074/  9|   1.072/ 10|   1.070/ 10 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  57   |   32002|      481.70|   1.035/ 20|   1.028/ 25|   1.026/ 27|   1.024/ 28 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  39   |      18|        5.15|   1.031/ 22|   1.010/ 72|   1.004/ **|   1.000/ -- |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  41   |      10|        0.31|   1.035/ 19|   1.020/ 35|   1.016/ 43|   1.013/ 54 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  41   |      10|        0.31|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  35   |       3|        0.17|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  45   |       4|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |

