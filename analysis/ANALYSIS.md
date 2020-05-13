# State and Country COVID-19 Analysis #
## Updated: 2020-05-13 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  60   |   27955|     1437.00|   1.013/ 54|   1.008/ 85|   1.007/ 98|   1.006/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  64   |   10245|     1153.41|   1.027/ 25|   1.019/ 37|   1.017/ 42|   1.014/ 48 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  54   |    5502|      791.78|   1.037/ 19|   1.025/ 28|   1.022/ 31|   1.019/ 36 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  55   |    4855|      486.12|   1.021/ 33|   1.013/ 54|   1.011/ 64|   1.009/ 79 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  55   |    4288|      334.92|   1.045/ 15|   1.036/ 19|   1.033/ 21|   1.031/ 22 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  57   |    3747|      295.71|   1.039/ 18|   1.032/ 21|   1.031/ 22|   1.029/ 24 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  55   |    3223|      904.09|   1.029/ 24|   1.018/ 38|   1.016/ 44|   1.013/ 53 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  70   |    3091|       78.23|   1.031/ 22|   1.022/ 32|   1.020/ 35|   1.017/ 40 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  60   |    2441|      525.08|   1.019/ 36|   1.013/ 53|   1.012/ 59|   1.010/ 68 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  66   |    1888|       87.90|   1.031/ 22|   1.025/ 28|   1.023/ 30|   1.021/ 32 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  74   |   89810|      272.53|   1.023/ 29|   1.014/ 50|   1.011/ 60|   1.009/ 75 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  63   |   35542|      534.98|   1.022/ 32|   1.014/ 49|   1.012/ 57|   1.010/ 68 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  82   |   32220|      534.88|   1.009/ 79|   1.006/ **|   1.005/ **|   1.004/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  88   |   29436|      438.85|   1.006/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  71   |   27724|      588.61|   1.009/ 78|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  57   |   12925|       61.14|   1.068/ 10|   1.061/ 11|   1.060/ 11|   1.058/ 12 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  63   |    9097|      789.40|   1.014/ 51|   1.008/ 88|   1.007/ **|   1.005/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  65   |    8114|       97.58|   1.015/ 46|   1.008/ 85|   1.006/ **|   1.005/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  83   |    6941|       83.24|   1.010/ 71|   1.008/ 92|   1.007/ 99|   1.006/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  68   |    5790|      331.66|   1.013/ 54|   1.008/ 91|   1.006/ **|   1.005/ ** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  49   |     434|       88.59|   1.041/ 17|   1.039/ 18|   1.038/ 18|   1.037/ 19 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  49   |      10|       13.82|   1.005/ **|   1.007/ **|   1.007/ **|   1.007/ 96 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  53   |     575|       79.00|   1.050/ 14|   1.052/ 13|   1.052/ 13|   1.053/ 13 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  50   |     103|       34.02|   1.037/ 19|   1.027/ 26|   1.024/ 29|   1.021/ 33 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  70   |    3091|       78.23|   1.031/ 22|   1.022/ 32|   1.020/ 35|   1.017/ 40 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  60   |    1086|      188.66|   1.024/ 29|   1.012/ 58|   1.009/ 76|   1.006/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  55   |    3223|      904.09|   1.029/ 24|   1.018/ 38|   1.016/ 44|   1.013/ 53 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  48   |     247|      253.79|   1.042/ 16|   1.028/ 24|   1.025/ 27|   1.022/ 31 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  66   |    1888|       87.90|   1.031/ 22|   1.025/ 28|   1.023/ 30|   1.021/ 32 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  62   |    1559|      146.83|   1.026/ 27|   1.019/ 36|   1.017/ 40|   1.016/ 44 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  43   |      17|       12.27|   1.009/ 78|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  48   |      70|       39.36|   1.012/ 57|   1.008/ 89|   1.007/ **|   1.006/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  57   |    3747|      295.71|   1.039/ 18|   1.032/ 21|   1.031/ 22|   1.029/ 24 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  58   |    1689|      250.94|   1.041/ 17|   1.033/ 21|   1.031/ 22|   1.029/ 24 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  49   |     297|       94.18|   1.055/ 12|   1.047/ 14|   1.046/ 15|   1.044/ 16 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  61   |     188|       64.48|   1.025/ 28|   1.021/ 33|   1.020/ 35|   1.019/ 37 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  58   |     331|       74.00|   1.026/ 27|   1.020/ 34|   1.019/ 37|   1.017/ 40 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  60   |    2441|      525.08|   1.019/ 36|   1.013/ 53|   1.012/ 59|   1.010/ 68 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  47   |      67|       49.95|   1.018/ 38|   1.012/ 58|   1.010/ 67|   1.009/ 79 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  55   |    1839|      304.15|   1.041/ 17|   1.031/ 23|   1.028/ 25|   1.025/ 27 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  54   |    5502|      791.78|   1.037/ 19|   1.025/ 28|   1.022/ 31|   1.019/ 36 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  55   |    4855|      486.12|   1.021/ 33|   1.013/ 54|   1.011/ 64|   1.009/ 79 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  53   |     660|      116.98|   1.054/ 13|   1.040/ 17|   1.036/ 19|   1.033/ 21 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  55   |     472|      158.68|   1.045/ 15|   1.043/ 16|   1.043/ 16|   1.042/ 16 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  55   |     543|       88.48|   1.038/ 18|   1.033/ 21|   1.032/ 22|   1.030/ 23 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  47   |      16|       15.26|   1.005/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  46   |     102|       52.83|   1.039/ 18|   1.029/ 24|   1.026/ 26|   1.024/ 29 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  58   |     335|      108.71|   1.027/ 26|   1.021/ 32|   1.020/ 35|   1.018/ 37 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  51   |     146|      107.17|   1.061/ 11|   1.061/ 11|   1.061/ 11|   1.061/ 11 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  64   |   10245|     1153.41|   1.027/ 25|   1.019/ 37|   1.017/ 42|   1.014/ 48 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  49   |     224|      107.04|   1.052/ 13|   1.043/ 16|   1.041/ 17|   1.039/ 18 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  60   |   27955|     1437.00|   1.013/ 54|   1.008/ 85|   1.007/ 98|   1.006/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  49   |     611|       58.23|   1.038/ 18|   1.032/ 22|   1.030/ 23|   1.029/ 24 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  47   |      39|       51.49|   1.053/ 13|   1.048/ 14|   1.047/ 15|   1.046/ 15 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  54   |    1509|      129.06|   1.039/ 18|   1.029/ 24|   1.027/ 26|   1.024/ 29 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  55   |     289|       72.98|   1.021/ 32|   1.015/ 47|   1.013/ 53|   1.012/ 60 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  59   |     135|       31.95|   1.023/ 30|   1.019/ 36|   1.018/ 38|   1.017/ 40 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  55   |    4288|      334.92|   1.045/ 15|   1.036/ 19|   1.033/ 21|   1.031/ 22 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  53   |     116|       36.24|   1.022/ 31|   1.018/ 39|   1.017/ 41|   1.016/ 43 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  46   |     469|      442.99|   1.044/ 16|   1.036/ 19|   1.033/ 21|   1.031/ 22 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  58   |     389|       75.57|   1.039/ 18|   1.028/ 25|   1.025/ 28|   1.022/ 32 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  63   |      41|       46.85|   1.048/ 14|   1.046/ 15|   1.046/ 15|   1.046/ 15 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  53   |     263|       38.52|   1.022/ 31|   1.020/ 35|   1.019/ 36|   1.019/ 37 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  57   |    1181|       40.74|   1.034/ 20|   1.030/ 23|   1.029/ 24|   1.027/ 25 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  52   |      72|       22.45|   1.038/ 18|   1.037/ 18|   1.037/ 18|   1.037/ 19 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  54   |      55|       88.44|   1.008/ 82|   1.002/ **|   1.000/ --|   1.000/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  60   |     957|      112.15|   1.042/ 16|   1.032/ 21|   1.030/ 23|   1.027/ 25 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  74   |     983|      129.08|   1.015/ 45|   1.012/ 56|   1.012/ 60|   1.011/ 64 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  44   |      58|       32.38|   1.030/ 23|   1.018/ 38|   1.015/ 46|   1.012/ 56 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  54   |     424|       72.90|   1.025/ 27|   1.023/ 30|   1.022/ 31|   1.022/ 32 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  30   |       7|       12.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  52   |     138|        4.28|   1.058/ 12|   1.050/ 14|   1.047/ 14|   1.045/ 15 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  63   |      32|       11.32|   1.004/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  62   |     515|       11.99|   1.012/ 58|   1.011/ 65|   1.010/ 66|   1.010/ 68 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  45   |       2|        0.06|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  66   |     339|        7.53|   1.033/ 21|   1.027/ 25|   1.026/ 27|   1.025/ 28 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  48   |      49|       16.41|   1.032/ 21|   1.029/ 24|   1.028/ 24|   1.027/ 25 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  73   |     106|        4.12|   1.010/ 68|   1.004/ **|   1.003/ **|   1.001/ ** |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  62   |     646|       72.51|   1.007/ 94|   1.002/ **|   1.001/ **|   1.000/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  61   |      33|        3.23|   1.028/ 24|   1.030/ 23|   1.031/ 22|   1.032/ 22 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  58   |       8|        5.36|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  56   |     241|        1.43|   1.036/ 19|   1.035/ 20|   1.035/ 20|   1.035/ 20 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  43   |     142|       15.11|   1.043/ 16|   1.038/ 18|   1.037/ 19|   1.036/ 19 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  63   |    9097|      789.40|   1.014/ 51|   1.008/ 88|   1.007/ **|   1.005/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  37   |       1|        0.09|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  45   |     133|       11.64|   1.064/ 11|   1.062/ 11|   1.061/ 11|   1.060/ 11 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  53   |     114|       34.55|   1.046/ 15|   1.052/ 13|   1.054/ 13|   1.055/ 12 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  43   |       1|        0.43|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  57   |   12925|       61.14|   1.068/ 10|   1.061/ 11|   1.060/ 11|   1.058/ 12 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  63   |     100|       14.32|   1.032/ 21|   1.028/ 24|   1.027/ 25|   1.026/ 26 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  56   |      51|        2.43|   1.012/ 56|   1.012/ 59|   1.012/ 59|   1.011/ 60 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  30   |       1|        0.09|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  49   |     129|        4.84|   1.042/ 16|   1.045/ 15|   1.046/ 15|   1.047/ 14 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  65   |    5760|      151.58|   1.042/ 16|   1.030/ 23|   1.027/ 25|   1.024/ 29 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  15   |      37|        2.28|   1.196/  3|   1.108/  6|   1.076/  9|   1.046/ 15 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  52   |     342|       17.90|   1.034/ 20|   1.029/ 24|   1.027/ 26|   1.025/ 27 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  63   |    4637|        3.31|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  52   |     508|       10.28|   1.045/ 15|   1.042/ 16|   1.042/ 16|   1.041/ 17 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  55   |       7|        1.29|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  55   |      98|       24.13|   1.028/ 25|   1.018/ 39|   1.015/ 45|   1.013/ 55 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  56   |      83|        7.39|   1.025/ 28|   1.013/ 52|   1.011/ 64|   1.008/ 85 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  60   |     554|       95.17|   1.014/ 48|   1.010/ 67|   1.009/ 75|   1.008/ 84 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  57   |     412|       39.80|   1.023/ 30|   1.020/ 34|   1.019/ 36|   1.019/ 37 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  60   |    2441|      139.73|   1.073/  9|   1.073/  9|   1.073/  9|   1.072/  9 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  66   |     579|        5.77|   1.032/ 22|   1.026/ 27|   1.024/ 29|   1.022/ 31 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  43   |      20|        3.08|   1.058/ 12|   1.055/ 12|   1.054/ 13|   1.053/ 13 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  21   |       4|        2.94|   1.077/  9|   1.027/ 25|   1.000/ --|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  38   |       5|        0.05|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  53   |     286|       51.71|   1.024/ 29|   1.017/ 42|   1.015/ 47|   1.013/ 53 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  88   |   29436|      438.85|   1.006/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  54   |      10|        4.51|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  51   |       1|        0.43|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  39   |      11|        3.04|   1.041/ 17|   1.031/ 22|   1.028/ 25|   1.025/ 28 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  65   |    8114|       97.58|   1.015/ 46|   1.008/ 85|   1.006/ **|   1.005/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  53   |      23|        0.77|   1.032/ 21|   1.029/ 24|   1.028/ 24|   1.028/ 25 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  63   |     157|       14.61|   1.008/ 85|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  58   |      28|        1.71|   1.049/ 14|   1.039/ 17|   1.037/ 18|   1.036/ 19 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  28   |      12|        0.96|   1.045/ 15|   1.012/ 57|   1.000/ --|   1.000/ -- |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  17   |       3|        2.01|   1.179/  4|   1.143/  5|   1.090/  8|   1.034/ 20 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  38   |      17|        1.47|   1.076/  9|   1.080/  8|   1.081/  8|   1.082/  8 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  48   |     124|       13.57|   1.045/ 15|   1.040/ 17|   1.038/ 18|   1.037/ 19 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  59   |     445|       45.57|   1.029/ 24|   1.021/ 33|   1.019/ 36|   1.017/ 40 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  63   |    2548|        1.87|   1.064/ 11|   1.061/ 11|   1.060/ 11|   1.059/ 12 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  63   |    1030|        3.86|   1.021/ 34|   1.016/ 43|   1.015/ 45|   1.014/ 49 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  83   |    6941|       83.24|   1.010/ 71|   1.008/ 92|   1.007/ 99|   1.006/ ** |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  70   |     111|        2.83|   1.016/ 44|   1.017/ 40|   1.018/ 39|   1.018/ 38 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  63   |    1640|      333.25|   1.020/ 34|   1.006/ **|   1.003/ **|   1.000/ -- |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  53   |     262|       28.51|   1.015/ 45|   1.013/ 53|   1.012/ 56|   1.012/ 58 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  82   |   32220|      534.88|   1.009/ 79|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  55   |      10|        3.56|   1.015/ 45|   1.004/ **|   1.001/ **|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  90   |     794|        6.31|   1.038/ 18|   1.029/ 24|   1.026/ 26|   1.024/ 29 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  47   |       9|        0.88|   1.010/ 69|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  49   |      33|        1.76|   1.019/ 36|   1.016/ 42|   1.016/ 44|   1.015/ 46 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  48   |      36|        0.76|   1.053/ 13|   1.055/ 12|   1.055/ 12|   1.055/ 12 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  48   |      33|       18.34|   1.010/ 73|   1.014/ 50|   1.015/ 46|   1.016/ 43 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  39   |      68|       15.39|   1.082/  8|   1.091/  7|   1.093/  7|   1.096/  7 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  40   |      13|        2.01|   1.032/ 21|   1.021/ 32|   1.017/ 40|   1.012/ 55 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  40   |      19|        9.87|   1.022/ 32|   1.008/ 92|   1.004/ **|   1.001/ ** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  64   |      27|        3.89|   1.007/ 98|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  39   |      21|        4.69|   1.027/ 25|   1.002/ **|   1.000/ --|   1.000/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  41   |       3|        0.47|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  53   |      51|       18.30|   1.012/ 59|   1.008/ 82|   1.008/ 90|   1.007/ ** |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  57   |     111|        3.38|   1.006/ **|   1.004/ **|   1.003/ **|   1.003/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  45   |      40|        1.99|   1.039/ 17|   1.042/ 16|   1.042/ 16|   1.043/ 16 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  44   |       1|        0.25|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  55   |    4056|       32.05|   1.067/ 10|   1.060/ 11|   1.058/ 12|   1.056/ 12 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  56   |     182|       68.01|   1.042/ 16|   1.039/ 18|   1.038/ 18|   1.037/ 18 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  64   |     194|        5.42|   1.010/ 70|   1.007/ **|   1.006/ **|   1.005/ ** |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  68   |    5790|      331.66|   1.013/ 54|   1.008/ 91|   1.006/ **|   1.005/ ** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  45   |      21|        4.32|   1.008/ 87|   1.003/ **|   1.001/ **|   1.000/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  47   |       6|        0.95|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  49   |      49|        2.18|   1.034/ 20|   1.029/ 24|   1.027/ 25|   1.026/ 26 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  51   |     171|        0.83|   1.088/  8|   1.078/  9|   1.075/  9|   1.073/  9 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  52   |      99|       47.48|   1.021/ 34|   1.009/ 78|   1.006/ **|   1.003/ ** |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  60   |     228|       42.41|   1.007/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  43   |      18|        3.84|   1.041/ 17|   1.044/ 16|   1.045/ 15|   1.045/ 15 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  55   |     772|        3.52|   1.060/ 11|   1.052/ 13|   1.050/ 14|   1.048/ 14 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  63   |     260|       61.64|   1.028/ 24|   1.024/ 28|   1.023/ 29|   1.023/ 31 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  53   |      10|        1.44|   1.005/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  54   |    2224|       69.20|   1.064/ 11|   1.052/ 13|   1.049/ 14|   1.046/ 15 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 101   |     856|        7.89|   1.022/ 31|   1.017/ 41|   1.016/ 44|   1.015/ 47 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  62   |     886|       23.09|   1.027/ 26|   1.018/ 39|   1.015/ 45|   1.013/ 53 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  57   |    1197|      116.51|   1.015/ 45|   1.009/ 74|   1.008/ 87|   1.006/ ** |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  46   |      14|        5.08|   1.023/ 30|   1.028/ 25|   1.029/ 24|   1.030/ 23 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  52   |    1034|       53.26|   1.030/ 23|   1.025/ 27|   1.024/ 29|   1.023/ 30 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  55   |    2264|       15.43|   1.066/ 10|   1.052/ 13|   1.048/ 14|   1.045/ 15 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  50   |     267|        7.81|   1.041/ 17|   1.040/ 17|   1.040/ 17|   1.040/ 17 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  42   |      19|        1.16|   1.070/ 10|   1.101/  7|   1.108/  6|   1.116/  6 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  54   |     239|       34.35|   1.015/ 48|   1.017/ 40|   1.018/ 39|   1.018/ 37 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  20   |      20|        2.53|   1.145/  5|   1.072/ 10|   1.035/ 20|   1.000/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  53   |      22|        3.92|   1.029/ 24|   1.022/ 31|   1.020/ 34|   1.018/ 38 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  46   |      28|        5.13|   1.020/ 35|   1.005/ **|   1.001/ **|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  60   |     106|       50.75|   1.012/ 58|   1.008/ 88|   1.007/ **|   1.006/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  35   |      55|        3.48|   1.057/ 12|   1.056/ 12|   1.055/ 13|   1.053/ 13 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  47   |     217|        3.69|   1.058/ 12|   1.056/ 12|   1.055/ 12|   1.054/ 13 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  71   |   27724|      588.61|   1.009/ 78|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  46   |       9|        0.43|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  61   |      84|        1.99|   1.092/  7|   1.089/  8|   1.088/  8|   1.087/  8 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  63   |    3501|      338.69|   1.025/ 28|   1.016/ 42|   1.015/ 48|   1.013/ 55 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  69   |    1932|      224.55|   1.007/ 94|   1.002/ **|   1.001/ **|   1.000/ ** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  45   |       3|        0.17|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  43   |      22|        0.39|   1.041/ 17|   1.035/ 20|   1.034/ 20|   1.033/ 21 |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  73   |      58|        0.87|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  47   |      11|        1.51|   1.023/ 30|   1.031/ 22|   1.033/ 21|   1.035/ 19 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  49   |       8|        5.87|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  55   |      46|        3.92|   1.009/ 75|   1.008/ 81|   1.008/ 84|   1.008/ 87 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  57   |    4056|       48.77|   1.020/ 35|   1.012/ 60|   1.010/ 72|   1.008/ 91 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  74   |   89810|      272.53|   1.023/ 29|   1.014/ 50|   1.011/ 60|   1.009/ 75 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  61   |     432|       10.30|   1.044/ 16|   1.040/ 17|   1.039/ 18|   1.038/ 18 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  54   |     227|       22.94|   1.065/ 11|   1.053/ 13|   1.050/ 14|   1.047/ 15 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  63   |   35542|      534.98|   1.022/ 32|   1.014/ 49|   1.012/ 57|   1.010/ 68 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  45   |      19|        5.43|   1.019/ 37|   1.014/ 50|   1.013/ 54|   1.012/ 56 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  47   |      10|        0.31|   1.013/ 52|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  47   |      10|        0.31|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  41   |       7|        0.38|   1.089/  8|   1.128/  5|   1.137/  5|   1.146/  5 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  51   |       4|        0.26|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |

