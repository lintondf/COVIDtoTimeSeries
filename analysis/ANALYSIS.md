# State and Country COVID-19 Analysis #
## Updated: 2020-04-29 ##

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
|-----|----|------|---------|----------|--------|---------|---------|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  46   |   25857|     1329.15|   1.050|   1.021|   1.014|   1.007 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  50   |    7136|      803.36|   1.061|   1.036|   1.029|   1.022 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  41   |    3667|      367.17|   1.054|   1.041|   1.038|   1.035 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  40   |    3478|      500.41|   1.097|   1.073|   1.066|   1.060 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  43   |    2221|      175.29|   1.067|   1.049|   1.044|   1.040 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  41   |    2278|      638.96|   1.084|   1.055|   1.047|   1.040 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  41   |    2250|      175.79|   1.082|   1.044|   1.033|   1.021 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  56   |    2066|       52.28|   1.064|   1.049|   1.045|   1.041 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  46   |    1914|      411.62|   1.045|   1.031|   1.028|   1.024 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  52   |    1265|       58.90|   1.056|   1.036|   1.031|   1.026 |


- Days - Number of days since first death
- Deaths - Total deaths to date
- Deaths/1M - Deaths per million in population
- DDGR - **Smoothed** Daily Deaths Growth Rate [n:m] total deaths n days ago over m days ago

# Ten Countries with Highest Death Tolls #

Deaths in the 10 countries with the highest death tolls expressed as deaths per 1 million population. 

![Countries with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/Countries10WorstDeathRates.png)

Daily Death Growth Rate (DDGR) in the 10 countries with the highest death tolls.

![Countries with Highest Death Toll - Daily Death Growth Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/Countries10WorstDDGR.png)

|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|-----|----|------|---------|----------|--------|---------|---------|
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  60   |   68900|      209.08|   1.059|   1.034|   1.028|   1.022 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  68   |   28707|      476.55|   1.019|   1.014|   1.012|   1.011 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  57   |   24656|      523.47|   1.020|   1.014|   1.012|   1.010 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  74   |   29282|      436.56|   1.027|   1.003|   0.997|   0.991 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  49   |   23159|      348.60|   1.045|   1.028|   1.024|   1.020 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  49   |    7928|      687.89|   1.045|   1.022|   1.017|   1.011 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  51   |    6776|       81.50|   1.045|   1.029|   1.025|   1.021 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  69   |    6101|       73.17|   1.017|   1.012|   1.011|   1.010 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  43   |    5078|       24.02|   1.090|   1.083|   1.081|   1.080 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  49   |    3358|        2.39|   1.000|   1.000|   1.000|   1.000 |


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
|-----|----|------|---------|----------|--------|---------|---------|
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  35   |     245|       49.95|   1.057|   1.039|   1.035|   1.030 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  35   |       9|       12.31|   1.002|   0.999|   0.999|   0.998 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  39   |     307|       42.21|   1.060|   1.039|   1.034|   1.028 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  36   |      54|       18.05|   1.039|   1.040|   1.040|   1.041 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  56   |    2066|       52.28|   1.064|   1.049|   1.045|   1.041 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  46   |     774|      134.45|   1.067|   1.063|   1.063|   1.062 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  41   |    2278|      638.96|   1.084|   1.055|   1.047|   1.040 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  34   |     138|      141.45|   1.084|   1.078|   1.076|   1.075 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  52   |    1265|       58.90|   1.056|   1.036|   1.031|   1.026 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  48   |    1082|      101.93|   1.050|   1.037|   1.034|   1.030 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  29   |      16|       11.38|   1.049|   1.064|   1.067|   1.070 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  34   |      61|       33.88|   1.040|   1.026|   1.022|   1.019 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  43   |    2221|      175.29|   1.067|   1.049|   1.044|   1.040 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  44   |     924|      137.23|   1.061|   1.048|   1.045|   1.042 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  35   |     136|       43.23|   1.076|   1.067|   1.065|   1.063 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  47   |     140|       48.03|   1.050|   1.025|   1.019|   1.012 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  44   |     236|       52.85|   1.052|   1.039|   1.036|   1.032 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  46   |    1914|      411.62|   1.045|   1.031|   1.028|   1.024 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  33   |      55|       40.56|   1.069|   1.046|   1.041|   1.035 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  41   |    1123|      185.67|   1.100|   1.078|   1.071|   1.064 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  40   |    3478|      500.41|   1.097|   1.073|   1.066|   1.060 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  41   |    3667|      367.17|   1.054|   1.041|   1.038|   1.035 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  39   |     321|       56.87|   1.105|   1.099|   1.098|   1.096 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  41   |     254|       85.28|   1.058|   1.040|   1.036|   1.031 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  41   |     339|       55.18|   1.064|   1.058|   1.056|   1.055 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  33   |      16|       14.77|   1.065|   1.025|   1.013|   1.001 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  32   |      64|       32.88|   1.102|   1.073|   1.064|   1.055 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  44   |     226|       73.23|   1.044|   1.033|   1.030|   1.028 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  37   |      64|       46.99|   1.064|   1.048|   1.045|   1.042 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  50   |    7136|      803.36|   1.061|   1.036|   1.029|   1.022 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  35   |     113|       53.77|   1.100|   1.075|   1.068|   1.062 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  46   |   25857|     1329.15|   1.050|   1.021|   1.014|   1.007 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  35   |     376|       35.87|   1.088|   1.056|   1.048|   1.040 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  33   |      20|       26.34|   1.070|   1.075|   1.074|   1.073 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  40   |     846|       72.40|   1.069|   1.049|   1.043|   1.038 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  41   |     215|       54.39|   1.048|   1.035|   1.032|   1.029 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  45   |      99|       23.53|   1.040|   1.031|   1.028|   1.026 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  41   |    2250|      175.79|   1.082|   1.044|   1.033|   1.021 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  39   |      88|       27.68|   1.046|   1.042|   1.041|   1.041 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  32   |     254|      239.38|   1.076|   1.052|   1.046|   1.040 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  44   |     190|       36.85|   1.053|   1.049|   1.049|   1.049 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  49   |      11|       12.97|   1.000|   1.000|   1.000|   1.000 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  39   |     192|       28.03|   1.034|   1.025|   1.023|   1.021 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  43   |     740|       25.53|   1.055|   1.034|   1.029|   1.024 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  38   |      46|       14.30|   1.070|   1.044|   1.037|   1.030 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  40   |      49|       79.24|   1.036|   1.023|   1.020|   1.017 |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  46   |     538|       63.01|   1.081|   1.061|   1.056|   1.050 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  60   |     817|      107.34|   1.027|   1.019|   1.018|   1.016 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  30   |      40|       22.11|   1.120|   1.053|   1.035|   1.016 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  40   |     301|       51.68|   1.040|   1.026|   1.023|   1.019 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  16   |       7|       12.13|   1.361|   1.081|   1.010|   0.956 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|-----|----|------|---------|----------|--------|---------|---------|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  38   |      58|        1.79|   1.067|   1.067|   1.067|   1.068 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  49   |      29|       10.12|   1.013|   1.013|   1.013|   1.013 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  48   |     455|       10.58|   1.024|   1.011|   1.008|   1.005 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  31   |       2|        0.06|   1.000|   1.000|   1.000|   1.000 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  52   |     214|        4.76|   1.054|   1.045|   1.043|   1.042 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  34   |      31|       10.40|   1.049|   1.037|   1.034|   1.031 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  59   |      87|        3.37|   1.028|   1.021|   1.019|   1.018 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  48   |     589|       66.17|   1.029|   1.019|   1.017|   1.014 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  47   |      24|        2.39|   1.036|   1.017|   1.012|   1.007 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  44   |       8|        5.32|   1.017|   1.012|   1.011|   1.010 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  42   |     180|        1.07|   1.095|   1.051|   1.039|   1.027 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  29   |      79|        8.44|   1.062|   1.057|   1.056|   1.055 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  49   |    7928|      687.89|   1.045|   1.022|   1.017|   1.011 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  23   |       1|        0.09|   1.000|   1.000|   1.000|   1.000 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  31   |      55|        4.80|   1.053|   1.064|   1.066|   1.068 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  39   |      63|       18.96|   1.031|   1.029|   1.029|   1.028 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  29   |       1|        0.43|   1.000|   1.000|   1.000|   1.000 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  43   |    5078|       24.02|   1.090|   1.083|   1.081|   1.080 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  49   |      62|        8.89|   1.043|   1.033|   1.030|   1.028 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  42   |      44|        2.12|   1.027|   1.013|   1.009|   1.005 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  16   |       1|        0.09|   1.000|   1.000|   1.000|   1.000 |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  35   |      64|        2.42|   1.115|   1.061|   1.047|   1.032 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  51   |    3370|       88.69|   1.090|   1.067|   1.061|   1.055 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  38   |     214|       11.21|   1.063|   1.046|   1.042|   1.038 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  49   |    3358|        2.39|   1.000|   1.000|   1.000|   1.000 |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  38   |     274|        5.54|   1.057|   1.045|   1.042|   1.038 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  41   |       7|        1.33|   1.000|   1.000|   1.000|   1.000 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  41   |      63|       15.50|   1.056|   1.036|   1.031|   1.026 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  42   |      62|        5.49|   1.074|   1.060|   1.057|   1.054 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  46   |     449|       77.15|   1.029|   1.021|   1.019|   1.017 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  43   |     301|       29.08|   1.037|   1.021|   1.017|   1.013 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  46   |     708|       40.55|   1.040|   1.030|   1.027|   1.025 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  52   |     369|        3.68|   1.052|   1.041|   1.038|   1.035 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  29   |       8|        1.27|   1.025|   1.014|   1.012|   1.009 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  24   |       3|        0.03|   1.000|   1.000|   1.000|   1.000 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  39   |     229|       41.44|   1.067|   1.048|   1.043|   1.038 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  74   |   29282|      436.56|   1.027|   1.003|   0.997|   0.991 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  40   |       1|        0.46|   1.000|   1.000|   1.000|   1.000 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  37   |       1|        0.43|   1.000|   1.000|   1.000|   1.000 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  25   |       6|        1.67|   1.073|   1.060|   1.058|   1.056 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  51   |    6776|       81.50|   1.045|   1.029|   1.025|   1.021 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  39   |      11|        0.36|   1.028|   1.041|   1.045|   1.049 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  49   |     140|       13.06|   1.024|   1.022|   1.021|   1.021 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  44   |      16|        0.96|   1.100|   1.109|   1.111|   1.114 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  14   |       7|        0.58|   1.063|   1.053|   1.053|   1.000 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  24   |       7|        0.59|   1.079|   1.055|   1.036|   1.013 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  34   |      64|        7.01|   1.058|   1.043|   1.041|   1.039 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000|   1.000|   1.000|   1.000 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  45   |     319|       32.63|   1.069|   1.044|   1.037|   1.031 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  49   |    1029|        0.76|   1.074|   1.060|   1.056|   1.053 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  49   |     823|        3.08|   1.046|   1.030|   1.026|   1.022 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  69   |    6101|       73.17|   1.017|   1.012|   1.011|   1.010 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  56   |      90|        2.30|   1.011|   1.007|   1.006|   1.005 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  49   |    1257|      255.50|   1.081|   1.072|   1.070|   1.068 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  39   |     218|       23.77|   1.040|   1.017|   1.011|   1.005 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  68   |   28707|      476.55|   1.019|   1.014|   1.012|   1.011 |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  41   |       7|        2.73|   1.039|   1.034|   1.033|   1.031 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  76   |     433|        3.44|   1.078|   1.078|   1.078|   1.078 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  33   |       7|        0.66|   1.000|   1.000|   1.000|   1.000 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  35   |      26|        1.42|   1.049|   1.041|   1.040|   1.038 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  34   |      15|        0.31|   1.032|   0.999|   0.991|   0.982 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  34   |      12|        6.80|   1.005|   1.000|   0.999|   0.998 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  25   |      25|        5.57|   1.193|   1.120|   1.101|   1.082 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  26   |       8|        1.29|   1.074|   1.020|   1.002|   0.985 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  26   |      14|        7.56|   1.142|   1.063|   1.027|   0.989 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  50   |      24|        3.49|   1.013|   1.017|   1.018|   1.019 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  25   |      14|        3.15|   1.070|   1.128|   1.142|   1.155 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  27   |       2|        0.34|   1.147|   1.098|   1.060|   1.014 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  39   |      44|       15.80|   1.033|   1.016|   1.012|   1.008 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  43   |     102|        3.10|   1.017|   1.011|   1.010|   1.008 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  31   |      25|        1.25|   1.050|   1.054|   1.054|   1.054 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  30   |       1|        0.25|   1.000|   1.000|   1.000|   1.000 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  41   |    1700|       13.43|   1.119|   1.102|   1.098|   1.093 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  42   |     111|       41.22|   1.072|   1.051|   1.047|   1.042 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  50   |     170|        4.74|   1.022|   1.014|   1.012|   1.010 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  54   |    4898|      280.57|   1.032|   1.022|   1.020|   1.017 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  31   |      21|        4.18|   1.076|   1.050|   1.042|   1.034 |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  33   |       4|        0.55|   1.000|   1.000|   1.000|   1.000 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  35   |      31|        1.40|   1.063|   1.057|   1.056|   1.055 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  37   |      46|        0.22|   1.107|   1.089|   1.084|   1.080 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  38   |      67|       32.20|   1.033|   1.033|   1.033|   1.034 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  46   |     218|       40.67|   1.030|   1.017|   1.014|   1.011 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  29   |      11|        2.32|   1.081|   1.035|   1.022|   1.009 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  41   |     334|        1.52|   1.085|   1.069|   1.065|   1.060 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  49   |     182|       43.20|   1.048|   1.035|   1.032|   1.028 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  39   |       9|        1.30|   1.020|   1.007|   1.004|   1.001 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  40   |     896|       27.90|   1.099|   1.086|   1.082|   1.078 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  87   |     704|        6.49|   1.035|   1.023|   1.020|   1.017 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  48   |     613|       15.97|   1.061|   1.051|   1.049|   1.046 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  43   |     976|       94.99|   1.039|   1.030|   1.028|   1.026 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  32   |      11|        3.86|   1.040|   1.011|   1.003|   0.994 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  38   |     678|       34.92|   1.048|   1.042|   1.041|   1.039 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  41   |     944|        6.43|   1.126|   1.097|   1.089|   1.082 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  36   |     154|        4.51|   1.056|   1.047|   1.045|   1.043 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  28   |      10|        0.62|   1.138|   1.101|   1.090|   1.079 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  40   |     132|       18.98|   1.024|   0.998|   0.991|   0.985 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  39   |      13|        2.36|   1.026|   1.026|   1.026|   1.027 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  32   |      20|        3.73|   1.068|   1.058|   1.055|   1.053 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  46   |      90|       42.84|   1.029|   1.014|   1.010|   1.006 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  21   |      30|        1.89|   1.153|   1.198|   1.184|   1.166 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  33   |      98|        1.67|   1.082|   1.057|   1.052|   1.047 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198|   1.116|   1.097|   1.079 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  57   |   24656|      523.47|   1.020|   1.014|   1.012|   1.010 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  32   |       7|        0.32|   1.000|   1.000|   1.000|   1.000 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  47   |      26|        0.62|   1.090|   1.110|   1.114|   1.119 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  49   |    2577|      249.26|   1.058|   1.041|   1.036|   1.032 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  55   |    1770|      205.71|   1.027|   1.017|   1.014|   1.012 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  31   |       2|        0.11|   1.000|   1.000|   1.000|   1.000 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000|   1.000|   1.000|   1.000 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  29   |      11|        0.19|   1.072|   1.004|   0.989|   0.974 |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  59   |      57|        0.85|   1.022|   1.006|   1.002|   0.999 |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  33   |       6|        0.83|   1.028|   1.004|   0.997|   0.990 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  35   |       8|        5.87|   1.000|   1.000|   1.000|   1.000 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  41   |      39|        3.37|   1.011|   1.002|   1.000|   0.998 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  43   |    3167|       38.09|   1.057|   1.041|   1.037|   1.032 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  60   |   68900|      209.08|   1.059|   1.034|   1.028|   1.022 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  47   |     246|        5.87|   1.066|   1.050|   1.047|   1.043 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  40   |      88|        8.93|   1.091|   1.092|   1.093|   1.094 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  49   |   23159|      348.60|   1.045|   1.028|   1.024|   1.020 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  31   |      16|        4.47|   1.052|   1.056|   1.056|   1.057 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  33   |       9|        0.26|   1.071|   1.044|   1.036|   1.026 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  33   |      10|        0.32|   1.010|   1.005|   1.003|   1.002 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  27   |       3|        0.17|   1.000|   1.000|   1.000|   1.000 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  37   |       4|        0.28|   1.000|   1.000|   1.000|   1.000 |

