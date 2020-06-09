# State and Country COVID-19 Analysis #
## Updated: 2020-06-09 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# Notes #

- Expect discontinuities in the US around 4/14/2020 as the [CDC](CDC "https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html")  expanded the definition of a COVID-19 death.  
- There is also some weekly pattern to reporting with lower values on the weekend followed by higher values subsequently, at least in some places.
- The Y axis upper limit for DDGR charts was lowered from 2.0 to 1.5 on 4/28 and then to 1.25 on 5/26/20 to better show current lower values.  

# Ten US States with Highest Death Tolls #

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. One per million is 0.0001%.  1% is 10,000 per million.

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDeathRates.png)

Daily Death Growth Rate (DDGR) in the 10 US States with the highest death tolls.

DDGR is the cube root of Arnold Kling's [Three Day Death Reproduction Rate (3DDRR)](http://www.arnoldkling.com/blog/the-3ddrr/).  The 3DDRR is calculated by dividing the cumulative total number of deaths on a given day by the  cumulative total number of deaths three days previously.  Taking the cube root converts this to the geometric mean for the three days.  These values are LOWESS filtered to generate a local-error minimizing non-parametric trend.

If deaths remain constant over the three days, the DDGR equals one.  A value of 2 would indicate that the number of deaths doubles every day.

![US States with Highest Death Toll - Daily Death Growth Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  87   |   30839|     1585.27|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  91   |   12618|     1420.60|   1.006/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  81   |    7601|     1093.75|   1.009/ 75|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  82   |    6234|      486.95|   1.010/ 67|   1.007/ 96|   1.006/ **|   1.006/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  84   |    6230|      491.61|   1.014/ 51|   1.010/ 67|   1.010/ 72|   1.009/ 78 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  82   |    5852|      585.94|   1.007/ 95|   1.007/ **|   1.006/ **|   1.006/ ** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  97   |    4886|      123.65|   1.015/ 46|   1.013/ 54|   1.012/ 57|   1.012/ 60 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  82   |    4239|     1189.10|   1.006/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  87   |    3002|      645.77|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  82   |    2890|      478.01|   1.013/ 53|   1.010/ 68|   1.010/ 72|   1.009/ 78 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 101   |  115880|      351.64|   1.008/ 87|   1.006/ **|   1.005/ **|   1.005/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  90   |   41541|      625.28|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  84   |   40712|      192.57|   1.034/ 20|   1.029/ 24|   1.027/ 25|   1.026/ 26 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 109   |   34727|      576.49|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 115   |   30098|      448.72|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  98   |   27577|      585.50|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  82   |   14898|      117.70|   1.044/ 15|   1.041/ 17|   1.041/ 17|   1.040/ 17 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  90   |    9763|      847.17|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  92   |    8882|      106.81|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 110   |    8360|      100.27|   1.008/ 90|   1.007/ 93|   1.007/ 94|   1.007/ 94 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  76   |     720|      146.88|   1.016/ 43|   1.014/ 49|   1.014/ 50|   1.013/ 51 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  76   |      10|       13.67|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  80   |    1095|      150.37|   1.019/ 37|   1.016/ 43|   1.015/ 45|   1.015/ 47 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  77   |     157|       52.11|   1.021/ 33|   1.022/ 32|   1.022/ 32|   1.022/ 31 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  97   |    4886|      123.65|   1.015/ 46|   1.013/ 54|   1.012/ 57|   1.012/ 60 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  87   |    1624|      282.03|   1.009/ 74|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  82   |    4239|     1189.10|   1.006/ **|   1.004/ **|   1.003/ **|   1.002/ ** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  75   |     413|      424.14|   1.013/ 55|   1.009/ 77|   1.008/ 85|   1.007/ 95 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  93   |    2815|      131.06|   1.013/ 53|   1.011/ 63|   1.010/ 66|   1.010/ 69 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  89   |    2298|      216.40|   1.012/ 58|   1.010/ 68|   1.010/ 72|   1.009/ 76 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  70   |      17|       12.01|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  75   |      86|       47.90|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  84   |    6230|      491.61|   1.014/ 51|   1.010/ 67|   1.010/ 72|   1.009/ 78 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  85   |    2397|      356.02|   1.011/ 65|   1.008/ 86|   1.007/ 93|   1.007/ ** |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  76   |     661|      209.43|   1.021/ 33|   1.016/ 44|   1.014/ 48|   1.013/ 54 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  88   |     238|       81.54|   1.008/ 86|   1.007/ **|   1.007/ **|   1.006/ ** |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  85   |     487|      108.93|   1.013/ 53|   1.012/ 58|   1.011/ 60|   1.011/ 62 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  87   |    3002|      645.77|   1.006/ **|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  74   |     101|       75.14|   1.017/ 42|   1.017/ 41|   1.017/ 41|   1.017/ 41 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  82   |    2890|      478.01|   1.013/ 53|   1.010/ 68|   1.010/ 72|   1.009/ 78 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  81   |    7601|     1093.75|   1.009/ 75|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  82   |    5852|      585.94|   1.007/ 95|   1.007/ **|   1.006/ **|   1.006/ ** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  80   |    1262|      223.71|   1.021/ 32|   1.019/ 37|   1.018/ 38|   1.017/ 40 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  82   |     874|      293.53|   1.019/ 36|   1.016/ 42|   1.016/ 44|   1.015/ 46 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  82   |     861|      140.31|   1.012/ 60|   1.008/ 83|   1.008/ 91|   1.007/ ** |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  74   |      18|       16.64|   1.007/ **|   1.009/ 81|   1.009/ 78|   1.009/ 74 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  73   |     198|      102.55|   1.017/ 40|   1.013/ 53|   1.012/ 57|   1.011/ 63 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  85   |     456|      148.02|   1.008/ 82|   1.006/ **|   1.006/ **|   1.005/ ** |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  78   |     302|      221.90|   1.022/ 31|   1.019/ 37|   1.018/ 38|   1.017/ 40 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  91   |   12618|     1420.60|   1.006/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  76   |     418|      199.54|   1.016/ 42|   1.012/ 56|   1.011/ 60|   1.011/ 66 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  87   |   30839|     1585.27|   1.003/ **|   1.002/ **|   1.001/ **|   1.001/ ** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  76   |    1088|      103.75|   1.018/ 39|   1.015/ 45|   1.015/ 47|   1.014/ 49 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  74   |      74|       97.55|   1.023/ 30|   1.021/ 33|   1.021/ 33|   1.021/ 34 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  81   |    2530|      216.44|   1.014/ 48|   1.011/ 62|   1.010/ 67|   1.009/ 73 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  82   |     357|       90.12|   1.007/ 94|   1.006/ **|   1.006/ **|   1.006/ ** |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  86   |     166|       39.24|   1.007/ **|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  82   |    6234|      486.95|   1.010/ 67|   1.007/ 96|   1.006/ **|   1.006/ ** |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  80   |     144|       45.21|   1.007/ **|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  73   |     829|      782.87|   1.018/ 39|   1.014/ 48|   1.014/ 51|   1.013/ 54 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  85   |     560|      108.68|   1.016/ 44|   1.015/ 46|   1.015/ 47|   1.014/ 48 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  90   |      72|       80.85|   1.014/ 49|   1.010/ 69|   1.009/ 77|   1.008/ 87 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  80   |     426|       62.38|   1.017/ 42|   1.016/ 43|   1.016/ 43|   1.016/ 43 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  84   |    1926|       66.44|   1.014/ 51|   1.011/ 63|   1.010/ 67|   1.010/ 71 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  79   |     130|       40.40|   1.016/ 44|   1.012/ 56|   1.012/ 60|   1.011/ 65 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  81   |      55|       88.72|   1.001/ **|   1.001/ **|   1.000/ **|   1.000/ ** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  87   |    1587|      185.89|   1.014/ 50|   1.010/ 68|   1.009/ 75|   1.008/ 83 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 101   |    1196|      157.06|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  71   |      84|       47.08|   1.011/ 60|   1.010/ 67|   1.010/ 68|   1.010/ 69 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  81   |     668|      114.65|   1.016/ 44|   1.015/ 47|   1.015/ 47|   1.014/ 48 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  57   |      19|       32.45|   1.018/ 38|   1.008/ 88|   1.005/ **|   1.002/ ** |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  79   |     352|       10.93|   1.038/ 18|   1.038/ 18|   1.038/ 18|   1.038/ 18 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  90   |      34|       11.86|   1.005/ **|   1.005/ **|   1.006/ **|   1.006/ ** |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  89   |     718|       16.70|   1.012/ 58|   1.012/ 59|   1.012/ 59|   1.012/ 59 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  72   |       2|        0.06|   1.000/ --|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  93   |     683|       15.21|   1.028/ 25|   1.028/ 25|   1.028/ 25|   1.028/ 25 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  75   |     213|       72.12|   1.063/ 11|   1.066/ 10|   1.066/ 10|   1.067/ 10 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 100   |     104|        4.05|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  89   |     679|       76.31|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  88   |      88|        8.75|   1.043/ 16|   1.045/ 15|   1.046/ 15|   1.047/ 15 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  85   |      24|       15.76|   1.048/ 14|   1.054/ 13|   1.056/ 12|   1.057/ 12 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  83   |     946|        5.62|   1.047/ 15|   1.046/ 15|   1.045/ 15|   1.045/ 15 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  70   |     280|       29.77|   1.022/ 32|   1.019/ 36|   1.019/ 36|   1.018/ 37 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  90   |    9763|      847.17|   1.002/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  64   |       3|        0.29|   1.000/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  72   |     491|       42.82|   1.046/ 15|   1.045/ 15|   1.044/ 16|   1.044/ 16 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  80   |     169|       51.10|   1.006/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  70   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  84   |   40712|      192.57|   1.034/ 20|   1.029/ 24|   1.027/ 25|   1.026/ 26 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  90   |     166|       23.93|   1.018/ 38|   1.017/ 42|   1.016/ 43|   1.016/ 44 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  83   |      54|        2.58|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  57   |       1|        0.09|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  76   |     221|        8.33|   1.018/ 39|   1.016/ 43|   1.016/ 44|   1.015/ 46 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  92   |    8344|      219.58|   1.011/ 61|   1.008/ 83|   1.008/ 90|   1.007/ ** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  17   |       5|        0.95|   1.260/  2|   1.106/  6|   1.080/  9|   1.063/ 11 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  42   |      70|        4.29|   1.009/ 74|   1.008/ 82|   1.008/ 83|   1.008/ 83 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  79   |    1721|       90.07|   1.064/ 11|   1.066/ 10|   1.066/ 10|   1.066/ 10 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  90   |    4638|        3.31|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  79   |    1271|       25.73|   1.041/ 17|   1.044/ 16|   1.045/ 15|   1.045/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  82   |      11|        2.15|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  82   |     106|       26.07|   1.003/ **|   1.001/ **|   1.001/ **|   1.000/ ** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  83   |      84|        7.53|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  87   |     594|      102.00|   1.003/ **|   1.003/ **|   1.002/ **|   1.002/ ** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  84   |     546|       52.72|   1.010/ 67|   1.010/ 72|   1.009/ 73|   1.009/ 74 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  87   |    3930|      224.95|   1.010/ 66|   1.006/ **|   1.005/ **|   1.004/ ** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  93   |    1237|       12.34|   1.035/ 20|   1.036/ 19|   1.037/ 19|   1.037/ 19 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  70   |      59|        9.07|   1.029/ 24|   1.024/ 29|   1.022/ 31|   1.021/ 33 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  48   |      12|        9.07|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  65   |      23|        0.23|   1.118/  6|   1.144/  5|   1.150/  4|   1.157/  4 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  80   |     330|       59.76|   1.003/ **|   1.001/ **|   1.000/ **|   1.000/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 115   |   30098|      448.72|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  81   |      22|       10.27|   1.016/ 43|   1.012/ 60|   1.010/ 66|   1.009/ 74 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  78   |       1|        0.43|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  66   |      13|        3.48|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  92   |    8882|      106.81|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  80   |      44|        1.47|   1.026/ 27|   1.026/ 26|   1.026/ 26|   1.027/ 26 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  90   |     185|       17.28|   1.004/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  85   |     215|       12.96|   1.105/  6|   1.116/  6|   1.119/  6|   1.121/  6 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  55   |      24|        1.98|   1.009/ 73|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  44   |      12|        7.29|   1.052/ 13|   1.070/ 10|   1.076/  9|   1.081/  8 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  65   |      58|        5.00|   1.043/ 16|   1.039/ 18|   1.037/ 18|   1.036/ 19 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  75   |     268|       29.25|   1.028/ 25|   1.027/ 26|   1.026/ 26|   1.026/ 26 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ ** |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  86   |     566|       57.90|   1.007/ 98|   1.005/ **|   1.005/ **|   1.004/ ** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  90   |    7597|        5.58|   1.041/ 17|   1.040/ 17|   1.040/ 17|   1.040/ 17 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  90   |    1911|        7.16|   1.022/ 31|   1.022/ 32|   1.022/ 32|   1.021/ 32 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 110   |    8360|      100.27|   1.008/ 90|   1.007/ 93|   1.007/ 94|   1.007/ 94 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  97   |     270|        6.91|   1.059/ 12|   1.068/ 10|   1.070/ 10|   1.072/  9 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  90   |    1718|      349.06|   1.003/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  80   |     298|       32.46|   1.004/ **|   1.003/ **|   1.003/ **|   1.003/ ** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 109   |   34727|      576.49|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  82   |      10|        3.55|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 117   |    1051|        8.34|   1.006/ **|   1.001/ **|   1.000/ --|   1.000/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  74   |       9|        0.84|   1.000/ **|   1.000/ --|   1.000/ **|   1.000/ ** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  76   |      51|        2.74|   1.032/ 22|   1.039/ 18|   1.041/ 17|   1.042/ 16 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  75   |      85|        1.78|   1.032/ 22|   1.033/ 21|   1.033/ 21|   1.033/ 21 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  75   |      30|       16.97|   1.002/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  66   |     285|       64.57|   1.037/ 19|   1.030/ 23|   1.028/ 24|   1.027/ 26 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  67   |      22|        3.30|   1.031/ 22|   1.038/ 18|   1.039/ 17|   1.041/ 17 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  67   |      26|       13.64|   1.010/ 71|   1.008/ 88|   1.007/ 94|   1.007/ ** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  91   |      28|        4.10|   1.009/ 75|   1.012/ 60|   1.012/ 57|   1.013/ 54 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  66   |      31|        6.86|   1.013/ 52|   1.011/ 62|   1.011/ 65|   1.010/ 68 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  68   |       6|        0.81|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  80   |      75|       26.96|   1.007/ 92|   1.005/ **|   1.004/ **|   1.003/ ** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  23   |       9|        0.35|   1.030/ 23|   1.073/  9|   1.086/  8|   1.099/  7 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  84   |     117|        3.58|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  72   |      95|        4.70|   1.025/ 28|   1.021/ 32|   1.020/ 34|   1.020/ 35 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  71   |      63|       15.41|   1.150/  4|   1.131/  5|   1.126/  5|   1.120/  6 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  82   |   14898|      117.70|   1.044/ 15|   1.041/ 17|   1.041/ 17|   1.040/ 17 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  83   |     358|      133.38|   1.021/ 32|   1.019/ 36|   1.018/ 37|   1.018/ 39 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  91   |     211|        5.88|   1.003/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  15   |       2|        0.07|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  24   |      14|        0.48|   1.105/  6|   1.096/  7|   1.097/  7|   1.098/  7 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  95   |    6156|      352.64|   1.002/ **|   1.000/ **|   1.000/ **|   1.000/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  72   |      22|        4.46|   1.002/ **|   1.002/ **|   1.002/ **|   1.002/ ** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  74   |      62|        9.64|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  76   |      69|        3.10|   1.004/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  78   |     370|        1.79|   1.030/ 23|   1.028/ 25|   1.028/ 25|   1.027/ 25 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  79   |     156|       75.14|   1.021/ 33|   1.022/ 32|   1.022/ 31|   1.022/ 31 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  87   |     241|       44.83|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  70   |      80|       17.17|   1.058/ 12|   1.059/ 12|   1.059/ 12|   1.059/ 12 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  82   |    2050|        9.35|   1.043/ 16|   1.045/ 15|   1.045/ 15|   1.046/ 15 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  90   |     392|       92.87|   1.018/ 38|   1.018/ 38|   1.018/ 38|   1.018/ 38 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  80   |      11|        1.55|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  81   |    5900|      183.63|   1.031/ 22|   1.027/ 25|   1.026/ 26|   1.025/ 27 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 128   |    1096|       10.10|   1.008/ 90|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  89   |    1189|       30.97|   1.010/ 69|   1.008/ 82|   1.008/ 86|   1.008/ 90 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  84   |    1514|      147.29|   1.008/ 84|   1.007/ 92|   1.007/ 95|   1.007/ 98 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  73   |      59|       21.42|   1.062/ 11|   1.063/ 11|   1.063/ 11|   1.063/ 11 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  79   |    1369|       70.54|   1.007/ 94|   1.005/ **|   1.005/ **|   1.004/ ** |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  82   |    6331|       43.14|   1.036/ 19|   1.033/ 21|   1.032/ 22|   1.031/ 22 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  10   |       2|        0.16|   1.260/  2|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  77   |     700|       20.46|   1.045/ 15|   1.049/ 14|   1.050/ 14|   1.051/ 14 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  69   |      51|        3.18|   1.024/ 29|   1.018/ 38|   1.017/ 42|   1.015/ 46 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  81   |     252|       36.19|   1.003/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  47   |      49|        6.25|   1.012/ 56|   1.004/ **|   1.002/ **|   1.000/ ** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  80   |      25|        4.36|   1.007/ **|   1.007/ **|   1.007/ **|   1.007/ ** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  73   |      28|        5.16|   1.000/ --|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  87   |     111|       52.80|   1.001/ **|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  62   |      86|        5.42|   1.018/ 38|   1.016/ 43|   1.016/ 44|   1.015/ 46 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  74   |    1092|       18.57|   1.061/ 11|   1.060/ 11|   1.059/ 12|   1.059/ 12 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198/  3|   1.116/  6|   1.097/  7|   1.079/  9 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  98   |   27577|      585.50|   1.001/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  73   |      11|        0.52|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  88   |     419|        9.87|   1.050/ 14|   1.045/ 15|   1.044/ 16|   1.042/ 16 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  90   |    4868|      470.88|   1.010/ 71|   1.008/ 89|   1.007/ 95|   1.007/ ** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  96   |    1947|      226.34|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  72   |       6|        0.36|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ ** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  70   |      21|        0.38|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ ** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 100   |      58|        0.87|   1.001/ **|   1.001/ **|   1.001/ **|   1.001/ ** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  74   |      14|        1.79|   1.000/ **|   1.000/ --|   1.000/ --|   1.000/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  76   |       8|        5.87|   1.000/ --|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  82   |      50|        4.23|   1.002/ **|   1.002/ **|   1.002/ **|   1.001/ ** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  84   |    4793|       57.64|   1.005/ **|   1.004/ **|   1.004/ **|   1.003/ ** |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 101   |  115880|      351.64|   1.008/ 87|   1.006/ **|   1.005/ **|   1.005/ ** |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  88   |     860|       20.53|   1.018/ 39|   1.014/ 50|   1.013/ 54|   1.012/ 59 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  81   |     290|       29.27|   1.007/ 95|   1.003/ **|   1.003/ **|   1.002/ ** |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  90   |   41541|      625.28|   1.007/ **|   1.005/ **|   1.005/ **|   1.005/ ** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  72   |      24|        6.74|   1.005/ **|   1.003/ **|   1.003/ **|   1.002/ ** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  74   |      17|        0.50|   1.020/ 35|   1.021/ 32|   1.022/ 32|   1.022/ 31 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  74   |      22|        0.68|   1.044/ 16|   1.053/ 13|   1.055/ 12|   1.058/ 12 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  68   |       7|        0.40|   1.000/ **|   1.000/ **|   1.000/ --|   1.000/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  78   |       4|        0.26|   1.000/ --|   1.000/ **|   1.000/ **|   1.000/ -- |

