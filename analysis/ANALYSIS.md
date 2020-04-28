# State and Country COVID-19 Analysis #
## Updated: 2020-04-28 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

**Note**:  *Expect discontinuities in the US around 4/14/2020 as the [CDC](CDC "https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html")  expanded the definition of a COVID-19 death.  There is also some weekly pattern to reporting with lower values on the weekend followed by higher values subsequently, at least in some places *

# Ten US States with Highest Death Tolls #

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. One per million is 0.0001%.  1% is 10,000 per million.

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDeathRates.png)

Daily Death Growth Rate (DDGR) in the 10 US States with the highest death tolls.

DDGR is the cube root of Arnold Kling's [Three Day Death Reproduction Rate (3DDRR)](http://www.arnoldkling.com/blog/the-3ddrr/).  The 3DDRR is calculated by dividing the cumulative total number of deaths on a given day by the  cumulative total number of deaths three days previously.  Taking the cube root converts this to the geometric mean for the three days.  These values are LOWESS filtered to generate a local-error minimizing non-parametric trend.

If deaths remain constant over the three days, the DDGR equals one.  A value of 2 would indicate that the number of deaths doubles every day.

![US States with Highest Death Toll - Daily Death Growth Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|-----|----|------|---------|----------|--------|---------|---------|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  45   |   25448|     1308.16|   1.056|   1.028|   1.020|   1.013 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  49   |    6890|      775.70|   1.067|   1.040|   1.033|   1.026 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  40   |    3543|      354.81|   1.057|   1.042|   1.039|   1.035 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  39   |    3288|      473.06|   1.102|   1.083|   1.078|   1.072 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  40   |    2200|      617.05|   1.091|   1.063|   1.055|   1.048 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  42   |    2134|      168.44|   1.071|   1.053|   1.048|   1.044 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  40   |    2197|      171.64|   1.090|   1.049|   1.038|   1.025 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  55   |    1976|       50.02|   1.069|   1.054|   1.051|   1.047 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  45   |    1862|      400.57|   1.049|   1.036|   1.033|   1.029 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  51   |    1220|       56.80|   1.060|   1.039|   1.034|   1.028 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  59   |   66669|      202.31|   1.065|   1.039|   1.032|   1.026 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  67   |   28297|      469.75|   1.020|   1.014|   1.013|   1.012 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  56   |   24409|      518.24|   1.022|   1.015|   1.013|   1.011 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  73   |   28889|      430.69|   1.030|   1.004|   0.997|   0.991 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  48   |   22725|      342.06|   1.049|   1.032|   1.028|   1.023 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  48   |    7846|      680.78|   1.049|   1.026|   1.020|   1.014 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  50   |    6635|       79.80|   1.048|   1.032|   1.028|   1.024 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  68   |    6043|       72.48|   1.018|   1.013|   1.012|   1.010 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  48   |    3358|        2.39|   1.000|   1.000|   1.000|   1.000 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  42   |    4689|       22.18|   1.092|   1.084|   1.083|   1.082 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  34   |     237|       48.27|   1.062|   1.039|   1.033|   1.027 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  34   |       9|       12.32|   1.003|   0.999|   0.999|   0.998 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  38   |     302|       41.46|   1.066|   1.051|   1.048|   1.044 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  35   |      52|       17.13|   1.041|   1.034|   1.032|   1.031 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  55   |    1976|       50.02|   1.069|   1.054|   1.051|   1.047 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  45   |     735|      127.67|   1.072|   1.072|   1.072|   1.073 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  40   |    2200|      617.05|   1.091|   1.063|   1.055|   1.048 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  33   |     128|      131.28|   1.087|   1.080|   1.078|   1.077 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  51   |    1220|       56.80|   1.060|   1.039|   1.034|   1.028 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  47   |    1043|       98.25|   1.052|   1.037|   1.033|   1.029 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  28   |      15|       10.73|   1.043|   1.060|   1.063|   1.066 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  33   |      59|       32.92|   1.047|   1.027|   1.023|   1.018 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  42   |    2134|      168.44|   1.071|   1.053|   1.048|   1.044 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  43   |     880|      130.75|   1.064|   1.049|   1.045|   1.042 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  34   |     128|       40.57|   1.079|   1.067|   1.065|   1.063 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  46   |     139|       47.56|   1.056|   1.030|   1.024|   1.017 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  43   |     228|       51.00|   1.056|   1.043|   1.039|   1.036 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  45   |    1862|      400.57|   1.049|   1.036|   1.033|   1.029 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  32   |      53|       39.66|   1.075|   1.053|   1.048|   1.044 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  40   |    1059|      175.17|   1.106|   1.088|   1.082|   1.076 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  39   |    3288|      473.06|   1.102|   1.083|   1.078|   1.072 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  40   |    3543|      354.81|   1.057|   1.042|   1.039|   1.035 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  38   |     296|       52.57|   1.107|   1.107|   1.106|   1.106 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  40   |     247|       82.97|   1.063|   1.046|   1.042|   1.037 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  40   |     323|       52.64|   1.066|   1.059|   1.057|   1.056 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  32   |      16|       14.68|   1.077|   1.032|   1.019|   1.004 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  31   |      61|       31.61|   1.102|   1.090|   1.086|   1.080 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  43   |     218|       70.89|   1.047|   1.036|   1.033|   1.031 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  36   |      62|       45.78|   1.068|   1.051|   1.048|   1.044 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  49   |    6890|      775.70|   1.067|   1.040|   1.033|   1.026 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  34   |     107|       51.20|   1.106|   1.086|   1.081|   1.076 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  45   |   25448|     1308.16|   1.056|   1.028|   1.020|   1.013 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  34   |     361|       34.42|   1.096|   1.059|   1.049|   1.040 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  32   |      19|       24.87|   1.071|   1.081|   1.082|   1.082 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  39   |     811|       69.39|   1.074|   1.054|   1.049|   1.044 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  40   |     209|       52.91|   1.051|   1.040|   1.037|   1.034 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  44   |      96|       22.84|   1.041|   1.029|   1.026|   1.023 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  40   |    2197|      171.64|   1.090|   1.049|   1.038|   1.025 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  38   |      86|       26.81|   1.048|   1.049|   1.050|   1.051 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  31   |     245|      230.93|   1.084|   1.058|   1.052|   1.046 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  43   |     180|       34.96|   1.054|   1.048|   1.048|   1.047 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  48   |      11|       12.52|   1.047|   1.064|   1.068|   1.073 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  38   |     188|       27.49|   1.036|   1.027|   1.025|   1.024 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  42   |     719|       24.80|   1.059|   1.036|   1.030|   1.024 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  37   |      45|       13.98|   1.075|   1.059|   1.055|   1.050 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  39   |      49|       77.91|   1.039|   1.029|   1.027|   1.024 |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  45   |     510|       59.78|   1.086|   1.068|   1.064|   1.059 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  59   |     800|      105.07|   1.029|   1.020|   1.017|   1.015 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  29   |      38|       21.12|   1.136|   1.061|   1.039|   1.017 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  39   |     291|       49.99|   1.044|   1.025|   1.020|   1.015 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  15   |       7|       12.09|   1.218|   1.242|   1.079|   0.870 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|
|-----|----|------|---------|----------|--------|---------|---------|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  37   |      54|        1.68|   1.069|   1.064|   1.063|   1.062 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  48   |      28|        9.91|   1.011|   1.008|   1.008|   1.007 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  47   |     449|       10.45|   1.027|   1.011|   1.007|   1.003 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  30   |       2|        0.06|   1.000|   1.000|   1.000|   1.000 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  51   |     205|        4.55|   1.056|   1.047|   1.045|   1.043 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  33   |      30|       10.07|   1.052|   1.042|   1.040|   1.037 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  58   |      85|        3.30|   1.027|   1.018|   1.016|   1.015 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  47   |     578|       64.88|   1.032|   1.020|   1.017|   1.014 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  46   |      24|        2.38|   1.040|   1.020|   1.015|   1.009 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  43   |       8|        5.27|   1.020|   1.015|   1.014|   1.013 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  41   |     174|        1.03|   1.104|   1.062|   1.050|   1.038 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  28   |      76|        8.03|   1.065|   1.057|   1.056|   1.054 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  48   |    7846|      680.78|   1.049|   1.026|   1.020|   1.014 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  22   |       1|        0.09|   1.000|   1.000|   1.000|   1.000 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  30   |      52|        4.57|   1.049|   1.068|   1.072|   1.076 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  38   |      61|       18.39|   1.031|   1.029|   1.028|   1.027 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  28   |       1|        0.43|   1.000|   1.000|   1.000|   1.000 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  42   |    4689|       22.18|   1.092|   1.084|   1.083|   1.082 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  48   |      60|        8.69|   1.046|   1.037|   1.035|   1.033 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  41   |      44|        2.11|   1.030|   1.016|   1.012|   1.009 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  15   |       1|        0.09|   1.000|   1.000|   1.000|   1.000 |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  34   |      63|        2.37|   1.128|   1.076|   1.061|   1.046 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  50   |    3204|       84.32|   1.096|   1.073|   1.067|   1.061 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  37   |     205|       10.75|   1.066|   1.049|   1.045|   1.040 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  48   |    3358|        2.39|   1.000|   1.000|   1.000|   1.000 |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  37   |     262|        5.30|   1.060|   1.046|   1.042|   1.038 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  40   |       7|        1.35|   1.000|   1.000|   1.000|   1.000 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  40   |      61|       14.97|   1.059|   1.035|   1.028|   1.022 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  41   |      58|        5.22|   1.078|   1.066|   1.063|   1.060 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  45   |     441|       75.76|   1.031|   1.023|   1.021|   1.019 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  42   |     298|       28.79|   1.041|   1.024|   1.020|   1.016 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  45   |     651|       37.28|   1.043|   1.032|   1.030|   1.027 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  51   |     353|        3.52|   1.054|   1.040|   1.036|   1.033 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  28   |       8|        1.27|   1.028|   1.020|   1.018|   1.016 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  23   |       3|        0.03|   1.000|   1.000|   1.000|   1.000 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  38   |     220|       39.79|   1.072|   1.056|   1.052|   1.048 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  73   |   28889|      430.69|   1.030|   1.004|   0.997|   0.991 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  39   |       1|        0.46|   1.000|   1.000|   1.000|   1.000 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  36   |       1|        0.43|   1.000|   1.000|   1.000|   1.000 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  24   |       6|        1.62|   1.077|   1.059|   1.056|   1.053 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  50   |    6635|       79.80|   1.048|   1.032|   1.028|   1.024 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  38   |      11|        0.35|   1.024|   1.034|   1.036|   1.039 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  48   |     137|       12.81|   1.024|   1.022|   1.022|   1.021 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  43   |      15|        0.91|   1.103|   1.121|   1.126|   1.132 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  13   |       7|        0.59|   1.260|   1.053|   1.053|   1.053 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  23   |       7|        0.59|   1.063|   1.084|   1.077|   1.068 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  33   |      61|        6.71|   1.065|   1.046|   1.043|   1.041 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000|   1.000|   1.000|   1.000 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  44   |     310|       31.77|   1.075|   1.049|   1.042|   1.035 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  48   |     975|        0.72|   1.077|   1.059|   1.055|   1.052 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  48   |     808|        3.03|   1.050|   1.033|   1.029|   1.025 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  68   |    6043|       72.48|   1.018|   1.013|   1.012|   1.010 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  55   |      89|        2.28|   1.011|   1.006|   1.004|   1.003 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  48   |    1189|      241.60|   1.088|   1.083|   1.082|   1.082 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  38   |     217|       23.60|   1.045|   1.020|   1.013|   1.007 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  67   |   28297|      469.75|   1.020|   1.014|   1.013|   1.012 |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  40   |       7|        2.68|   1.042|   1.045|   1.045|   1.046 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  75   |     407|        3.23|   1.082|   1.085|   1.086|   1.087 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  32   |       7|        0.66|   1.000|   1.000|   1.000|   1.000 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  34   |      26|        1.38|   1.051|   1.052|   1.054|   1.056 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  33   |      15|        0.31|   1.040|   1.003|   0.993|   0.983 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  33   |      12|        6.89|   1.010|   0.999|   0.998|   0.996 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  24   |      23|        5.24|   1.207|   1.144|   1.128|   1.113 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  25   |       8|        1.29|   1.069|   1.033|   1.016|   0.998 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  25   |      14|        7.45|   1.116|   1.074|   1.053|   1.027 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  49   |      23|        3.44|   1.014|   1.019|   1.020|   1.022 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  24   |      12|        2.66|   1.054|   1.118|   1.133|   1.148 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  26   |       1|        0.15|   1.092|   1.137|   1.111|   1.078 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  38   |      43|       15.54|   1.037|   1.016|   1.011|   1.006 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  42   |     101|        3.08|   1.018|   1.013|   1.011|   1.010 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  30   |      24|        1.19|   1.057|   1.068|   1.070|   1.071 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  29   |       1|        0.25|   1.000|   1.000|   1.000|   1.000 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  40   |    1568|       12.39|   1.126|   1.114|   1.112|   1.109 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  41   |     106|       39.50|   1.077|   1.059|   1.055|   1.051 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  49   |     168|        4.67|   1.024|   1.014|   1.012|   1.010 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  53   |    4807|      275.36|   1.035|   1.025|   1.023|   1.020 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  30   |      20|        4.09|   1.078|   1.064|   1.060|   1.056 |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  32   |       3|        0.46|   1.229|   1.084|   1.045|   1.003 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  34   |      30|        1.33|   1.064|   1.059|   1.059|   1.059 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  36   |      43|        0.21|   1.111|   1.094|   1.089|   1.085 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  37   |      64|       30.64|   1.035|   1.024|   1.022|   1.020 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  45   |     215|       40.13|   1.033|   1.021|   1.017|   1.014 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  28   |      11|        2.33|   1.092|   1.050|   1.039|   1.027 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  40   |     316|        1.44|   1.089|   1.076|   1.072|   1.068 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  48   |     179|       42.32|   1.052|   1.040|   1.037|   1.035 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  38   |       9|        1.31|   1.024|   1.010|   1.007|   1.004 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  39   |     831|       25.86|   1.101|   1.093|   1.090|   1.087 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  86   |     699|        6.44|   1.037|   1.024|   1.021|   1.017 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  47   |     582|       15.17|   1.065|   1.053|   1.050|   1.048 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  42   |     954|       92.79|   1.042|   1.032|   1.030|   1.028 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  31   |      11|        3.86|   1.042|   1.019|   1.012|   1.004 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  37   |     653|       33.63|   1.050|   1.045|   1.044|   1.043 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  40   |     876|        5.97|   1.132|   1.104|   1.096|   1.089 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  35   |     148|        4.32|   1.059|   1.050|   1.048|   1.046 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  27   |      10|        0.59|   1.136|   1.111|   1.099|   1.087 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  39   |     133|       19.06|   1.029|   1.001|   0.994|   0.986 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  38   |      13|        2.28|   1.026|   1.018|   1.017|   1.016 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  31   |      19|        3.55|   1.071|   1.053|   1.047|   1.042 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  45   |      88|       42.21|   1.032|   1.015|   1.010|   1.005 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  20   |      27|        1.70|   1.116|   1.212|   1.206|   1.193 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  32   |      95|        1.61|   1.089|   1.067|   1.063|   1.060 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198|   1.116|   1.097|   1.079 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  56   |   24409|      518.24|   1.022|   1.015|   1.013|   1.011 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  31   |       7|        0.32|   1.000|   1.000|   1.000|   1.000 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  46   |      24|        0.56|   1.085|   1.104|   1.109|   1.114 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  48   |    2502|      242.04|   1.063|   1.047|   1.043|   1.039 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  54   |    1747|      203.03|   1.028|   1.017|   1.015|   1.012 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  30   |       2|        0.11|   1.000|   1.000|   1.000|   1.000 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000|   1.000|   1.000|   1.000 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  28   |      11|        0.20|   1.086|   1.013|   0.993|   0.974 |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  58   |      57|        0.85|   1.023|   1.006|   1.002|   0.998 |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  32   |       6|        0.84|   1.034|   1.008|   1.000|   0.992 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  34   |       8|        5.87|   1.000|   1.000|   1.000|   1.000 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  40   |      39|        3.35|   1.013|   0.999|   0.996|   0.993 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  42   |    3075|       36.98|   1.061|   1.045|   1.040|   1.036 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  59   |   66669|      202.31|   1.065|   1.039|   1.032|   1.026 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  46   |     235|        5.60|   1.068|   1.051|   1.046|   1.042 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  39   |      81|        8.18|   1.093|   1.093|   1.094|   1.095 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  48   |   22725|      342.06|   1.049|   1.032|   1.028|   1.023 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  30   |      15|        4.32|   1.050|   1.064|   1.068|   1.071 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  32   |       9|        0.26|   1.076|   1.061|   1.055|   1.049 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  32   |      10|        0.32|   1.011|   1.008|   1.006|   1.004 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  26   |       3|        0.17|   1.071|   1.006|   0.988|   0.973 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  36   |       4|        0.28|   1.000|   1.000|   1.000|   1.000 |

