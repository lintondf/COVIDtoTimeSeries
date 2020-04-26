# State and Country COVID-19 Analysis #
## Updated: 2020-04-26 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

**Note**:  *Expect discontinuities in the US around 4/14/2020 as the [CDC](CDC "https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html")  expanded the definition of a COVID-19 death.  There is also some weekly pattern to reporting with lower values on the weekend followed by higher values subsequently, at least in some places *

# Ten US States with Highest Death Tolls #

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. One per million is 0.0001%.  1% is 10,000 per million.

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDeathRates.png)

Daily Death Growth Rate (DDGR) in the 10 US States with the highest death tolls.

DDGR is the cube root of Arnold Kling's [Three Day Death Reproduction Rate (3DDRR)](http://www.arnoldkling.com/blog/the-3ddrr/).  The 3DDRR is calculated by dividing the cumulative total number of deaths on a given day by the  cumulative total number of deaths three days previously.  Taking the cube root converts this to the geometric mean for the three days.  These values are LOWESS filtered to generate a local-error minimizing non-parametric trend.

If deaths remain constant over the three days, the DDGR equals one.  A value of 2 would indicate that the number of deaths doubles every day.

![US States with Highest Death Toll - Daily Death Growth Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDGR[-7]|DDGR[-3]|DDGR[-2]|DDGR[-1]|
|-----|----|------|---------|----------|--------|---------|---------|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  43   |   24624|     1265.77|   1.069|   1.041|   1.034|   1.026 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  47   |    6492|      730.87|   1.081|   1.055|   1.048|   1.042 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  38   |    3290|      329.47|   1.065|   1.049|   1.046|   1.042 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  37   |    2872|      413.29|   1.111|   1.100|   1.096|   1.093 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  40   |    1957|      154.42|   1.082|   1.064|   1.060|   1.056 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  38   |    1993|      559.05|   1.105|   1.078|   1.071|   1.065 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  38   |    2087|      163.02|   1.110|   1.079|   1.070|   1.061 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  43   |    1759|      378.36|   1.057|   1.047|   1.044|   1.042 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  53   |    1799|       45.53|   1.078|   1.066|   1.063|   1.061 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  49   |    1145|       53.29|   1.071|   1.053|   1.049|   1.044 |


- Days - Number of days since first death
- Deaths - Total deaths to date
- Deaths/1M - Deaths per million in population
- DDGR - **Smoothed** Daily Deaths Growth Rate [n:m] total deaths n days ago over m days ago

# Ten Countries with Highest Death Tolls #

Deaths in the 10 countries with the highest death tolls expressed as deaths per 1 million population. 

![Countries with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/Countries10WorstDeathRates.png)

Daily Death Growth Rate (DDGR) in the 10 countries with the highest death tolls.

![Countries with Highest Death Toll - Daily Death Growth Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/Countries10WorstDDGR.png)

|Country|Days|Deaths|Deaths/1M|DDGR[-7]|DDGR[-3]|DDGR[-2]|DDGR[-1]|
|-----|----|------|---------|----------|--------|---------|---------|
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  57   |   62392|      189.33|   1.077|   1.050|   1.044|   1.037 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  65   |   27550|      457.35|   1.022|   1.016|   1.015|   1.013 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  54   |   23786|      505.01|   1.025|   1.016|   1.014|   1.012 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  71   |   28609|      426.51|   1.039|   1.009|   1.002|   0.994 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  46   |   21575|      324.75|   1.058|   1.037|   1.032|   1.027 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  46   |    7542|      654.44|   1.060|   1.031|   1.024|   1.017 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  48   |    6288|       75.62|   1.057|   1.041|   1.038|   1.034 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  66   |    5900|       70.77|   1.020|   1.014|   1.013|   1.011 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  46   |    3357|        2.39|   1.000|   1.000|   1.000|   1.000 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  51   |    4606|      263.86|   1.040|   1.030|   1.027|   1.025 |


# US and Selected States #

For each country and each US state, deaths per million in population is plotted on the left logarithmic axis and the raw and smoothed DDGR is plotted on the linear right axis.

For the US and each US state a second chart is produced below showing the various estimates of total deaths from the [IHME Projections](https://covid19.healthdata.org/united-states-of-america) website.  Historical data is from [here](http://www.healthdata.org/covid/data-downloads).  Above the date on which the estimate is issued a vertical line is plotted from the lower to the upper final total estimated deaths with a dot indicating the mean estimate.  A shaded region showing the growth to these final estimate is plotted for each IHME projection with a correspondingly colored solid line connecting the mean estimates.  The actual deaths to date are plotted as a solid black line.

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

|State|Days|Deaths|Deaths/1M|DDGR[-7]|DDGR[-3]|DDGR[-2]|DDGR[-1]|
|-----|----|------|---------|----------|--------|---------|---------|
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  32   |     223|       45.49|   1.073|   1.051|   1.046|   1.040 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  32   |       9|       12.37|   1.009|   0.999|   0.997|   0.995 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  36   |     279|       38.38|   1.073|   1.071|   1.071|   1.071 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  33   |      48|       16.00|   1.047|   1.033|   1.030|   1.028 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  53   |    1799|       45.53|   1.078|   1.066|   1.063|   1.061 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  43   |     651|      113.04|   1.076|   1.081|   1.083|   1.085 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  38   |    1993|      559.05|   1.105|   1.078|   1.071|   1.065 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  31   |     111|      113.50|   1.092|   1.078|   1.075|   1.072 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  49   |    1145|       53.29|   1.071|   1.053|   1.049|   1.044 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  45   |     982|       92.53|   1.060|   1.047|   1.044|   1.041 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  26   |      13|        9.33|   1.024|   1.055|   1.061|   1.066 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  31   |      57|       31.92|   1.062|   1.039|   1.034|   1.031 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  40   |    1957|      154.42|   1.082|   1.064|   1.060|   1.056 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  41   |     808|      119.99|   1.073|   1.053|   1.049|   1.044 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  32   |     113|       35.88|   1.086|   1.070|   1.067|   1.064 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  44   |     133|       45.71|   1.069|   1.041|   1.034|   1.027 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  41   |     213|       47.68|   1.064|   1.054|   1.052|   1.050 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  43   |    1759|      378.36|   1.057|   1.047|   1.044|   1.042 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  30   |      49|       36.35|   1.083|   1.068|   1.065|   1.062 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  38   |     920|      152.25|   1.118|   1.108|   1.105|   1.103 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  37   |    2872|      413.29|   1.111|   1.100|   1.096|   1.093 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  38   |    3290|      329.47|   1.065|   1.049|   1.046|   1.042 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  36   |     244|       43.18|   1.104|   1.112|   1.113|   1.114 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  38   |     230|       77.15|   1.070|   1.057|   1.053|   1.050 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  38   |     288|       46.87|   1.071|   1.059|   1.056|   1.054 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  30   |      15|       14.46|   1.081|   1.072|   1.068|   1.062 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  29   |      53|       27.32|   1.091|   1.119|   1.125|   1.131 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  41   |     206|       67.03|   1.056|   1.047|   1.045|   1.044 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  34   |      56|       41.34|   1.075|   1.058|   1.053|   1.049 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  47   |    6492|      730.87|   1.081|   1.055|   1.048|   1.042 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  32   |      94|       44.60|   1.113|   1.100|   1.097|   1.094 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  43   |   24624|     1265.77|   1.069|   1.041|   1.034|   1.026 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  32   |     331|       31.51|   1.113|   1.075|   1.065|   1.055 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  30   |      16|       21.37|   1.059|   1.092|   1.100|   1.108 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  37   |     747|       63.90|   1.083|   1.072|   1.069|   1.066 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  38   |     197|       49.79|   1.057|   1.052|   1.051|   1.050 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  42   |      92|       21.72|   1.046|   1.033|   1.029|   1.026 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  38   |    2087|      163.02|   1.110|   1.079|   1.070|   1.061 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  36   |      79|       24.59|   1.047|   1.048|   1.048|   1.049 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  29   |     226|      213.24|   1.100|   1.068|   1.059|   1.050 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  41   |     164|       31.88|   1.058|   1.050|   1.048|   1.047 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  46   |      10|       11.15|   1.000|   1.000|   1.000|   1.000 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  36   |     179|       26.22|   1.040|   1.031|   1.029|   1.027 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  40   |     681|       23.48|   1.070|   1.048|   1.043|   1.038 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  35   |      41|       12.83|   1.080|   1.077|   1.076|   1.075 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  37   |      46|       74.50|   1.043|   1.036|   1.034|   1.032 |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  43   |     458|       53.60|   1.096|   1.081|   1.078|   1.074 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  57   |     772|      101.35|   1.033|   1.022|   1.020|   1.017 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  27   |      36|       20.17|   1.160|   1.103|   1.085|   1.067 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  37   |     280|       48.16|   1.053|   1.032|   1.027|   1.022 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  13   |       7|       12.37|   1.089|   1.504|   1.337|   1.139 |


# All Countries #

Click on the link in the first column to view the DDGR chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDGR[-7]|DDGR[-3]|DDGR[-2]|DDGR[-1]|
|-----|----|------|---------|----------|--------|---------|---------|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  35   |      47|        1.47|   1.074|   1.056|   1.051|   1.047 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  46   |      28|        9.72|   1.012|   1.008|   1.007|   1.005 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  45   |     441|       10.26|   1.035|   1.014|   1.008|   1.003 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  28   |       2|        0.06|   1.000|   1.000|   1.000|   1.000 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  49   |     188|        4.17|   1.061|   1.049|   1.047|   1.044 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  31   |      28|        9.44|   1.059|   1.047|   1.044|   1.042 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  56   |      81|        3.17|   1.029|   1.015|   1.011|   1.009 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  45   |     560|       62.89|   1.038|   1.026|   1.023|   1.021 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  44   |      23|        2.32|   1.048|   1.029|   1.024|   1.018 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  41   |       8|        5.14|   1.025|   1.022|   1.022|   1.022 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  39   |     160|        0.95|   1.122|   1.084|   1.073|   1.062 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  26   |      68|        7.19|   1.075|   1.057|   1.053|   1.049 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  46   |    7542|      654.44|   1.060|   1.031|   1.024|   1.017 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  20   |       1|        0.09|   1.000|   1.000|   1.000|   1.000 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  28   |      45|        3.95|   1.038|   1.068|   1.076|   1.085 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  36   |      57|       17.41|   1.032|   1.029|   1.028|   1.028 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  26   |       1|        0.43|   1.000|   1.000|   1.000|   1.000 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  40   |    4019|       19.01|   1.095|   1.088|   1.086|   1.084 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  46   |      57|        8.14|   1.051|   1.046|   1.045|   1.043 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  39   |      43|        2.06|   1.036|   1.024|   1.021|   1.018 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  13   |       1|        0.09|   1.000|   1.000|   1.000|   1.000 |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  32   |      56|        2.12|   1.149|   1.079|   1.057|   1.033 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  48   |    2826|       74.37|   1.108|   1.087|   1.081|   1.076 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  35   |     189|        9.89|   1.073|   1.058|   1.054|   1.050 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  46   |    3357|        2.39|   1.000|   1.000|   1.000|   1.000 |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  35   |     242|        4.90|   1.069|   1.052|   1.048|   1.043 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  38   |       7|        1.33|   1.032|   1.020|   1.015|   1.011 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  38   |      58|       14.19|   1.069|   1.040|   1.032|   1.023 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  39   |      52|        4.64|   1.083|   1.072|   1.069|   1.066 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  43   |     424|       72.88|   1.035|   1.026|   1.024|   1.022 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  40   |     288|       27.83|   1.050|   1.032|   1.027|   1.023 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  43   |     613|       35.07|   1.049|   1.037|   1.034|   1.030 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  49   |     329|        3.28|   1.060|   1.044|   1.040|   1.036 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  26   |       8|        1.24|   1.027|   1.032|   1.035|   1.038 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  21   |       3|        0.03|   1.000|   1.000|   1.000|   1.000 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  36   |     194|       35.08|   1.102|   1.114|   1.117|   1.121 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  71   |   28609|      426.51|   1.039|   1.009|   1.002|   0.994 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  37   |       1|        0.46|   1.000|   1.000|   1.000|   1.000 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  34   |       1|        0.43|   1.000|   1.000|   1.000|   1.000 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  22   |       5|        1.41|   1.071|   1.057|   1.047|   1.037 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  48   |    6288|       75.62|   1.057|   1.041|   1.038|   1.034 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  36   |      10|        0.33|   1.020|   1.021|   1.022|   1.022 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  46   |     132|       12.27|   1.026|   1.024|   1.023|   1.023 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  41   |      12|        0.71|   1.103|   1.132|   1.139|   1.147 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  11   |       7|        0.56|   1.326|   1.047|   1.040|   1.043 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  21   |       6|        0.54|   1.005|   1.148|   1.184|   1.219 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  31   |      57|        6.22|   1.074|   1.044|   1.035|   1.028 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000|   1.000|   1.000|   1.000 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  42   |     288|       29.45|   1.088|   1.064|   1.057|   1.051 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  46   |     873|        0.64|   1.085|   1.059|   1.053|   1.048 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  46   |     762|        2.86|   1.057|   1.035|   1.030|   1.024 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  66   |    5900|       70.77|   1.020|   1.014|   1.013|   1.011 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  53   |      88|        2.25|   1.012|   1.005|   1.003|   1.001 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  46   |    1036|      210.58|   1.091|   1.089|   1.088|   1.088 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  36   |     212|       23.12|   1.056|   1.030|   1.023|   1.016 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  65   |   27550|      457.35|   1.022|   1.016|   1.015|   1.013 |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  38   |       7|        2.50|   1.000|   1.000|   1.000|   1.000 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  73   |     350|        2.78|   1.088|   1.096|   1.098|   1.100 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  30   |       7|        0.66|   1.000|   1.000|   1.000|   1.000 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  32   |      24|        1.28|   1.056|   1.055|   1.057|   1.060 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  31   |      15|        0.32|   1.058|   1.017|   1.005|   0.993 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  31   |      13|        7.02|   1.019|   1.001|   0.997|   0.993 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  22   |      19|        4.32|   1.203|   1.167|   1.144|   1.119 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  23   |       9|        1.30|   1.049|   1.066|   1.061|   1.055 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  23   |      14|        7.22|   1.071|   1.156|   1.160|   1.159 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  47   |      23|        3.31|   1.011|   1.012|   1.012|   1.013 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  22   |       8|        1.84|   1.048|   1.006|   0.993|   0.980 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  24   |       1|        0.15|   1.000|   1.000|   1.000|   1.000 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  36   |      43|       15.32|   1.048|   1.026|   1.020|   1.015 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  40   |      99|        3.02|   1.021|   1.015|   1.014|   1.012 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  28   |      21|        1.05|   1.044|   1.091|   1.105|   1.120 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  27   |       1|        0.25|   1.000|   1.000|   1.000|   1.000 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  38   |    1306|       10.32|   1.134|   1.141|   1.143|   1.146 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  39   |      96|       35.74|   1.083|   1.064|   1.059|   1.053 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  47   |     163|        4.56|   1.029|   1.018|   1.015|   1.013 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  51   |    4606|      263.86|   1.040|   1.030|   1.027|   1.025 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  28   |      19|        3.75|   1.111|   1.087|   1.089|   1.093 |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  30   |       3|        0.51|   1.165|   1.128|   1.117|   1.107 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  32   |      27|        1.19|   1.065|   1.057|   1.055|   1.053 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  34   |      36|        0.18|   1.113|   1.107|   1.105|   1.102 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  35   |      60|       29.10|   1.042|   1.020|   1.014|   1.009 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  43   |     209|       38.95|   1.040|   1.028|   1.025|   1.023 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  26   |      10|        2.24|   1.108|   1.079|   1.072|   1.065 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  38   |     278|        1.27|   1.096|   1.092|   1.091|   1.090 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  46   |     166|       39.46|   1.058|   1.047|   1.044|   1.042 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  36   |       9|        1.30|   1.032|   1.018|   1.015|   1.013 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  37   |     710|       22.10|   1.105|   1.104|   1.103|   1.103 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  84   |     677|        6.24|   1.041|   1.025|   1.021|   1.017 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  45   |     529|       13.79|   1.071|   1.056|   1.052|   1.049 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  40   |     901|       87.63|   1.047|   1.036|   1.033|   1.030 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  29   |      11|        3.85|   1.041|   1.040|   1.038|   1.035 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  35   |     602|       31.02|   1.053|   1.047|   1.046|   1.045 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  38   |     735|        5.01|   1.145|   1.118|   1.110|   1.102 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  33   |     136|        3.96|   1.066|   1.054|   1.051|   1.049 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  25   |       8|        0.49|   1.126|   1.105|   1.095|   1.083 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  37   |     135|       19.39|   1.041|   1.011|   1.003|   0.994 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  36   |      12|        2.18|   1.034|   1.014|   1.010|   1.006 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  29   |      18|        3.32|   1.117|   1.073|   1.060|   1.048 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  43   |      87|       41.52|   1.040|   1.021|   1.016|   1.011 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  18   |      19|        1.18|   1.128|   1.202|   1.263|   1.319 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  30   |      86|        1.46|   1.108|   1.081|   1.076|   1.073 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198|   1.116|   1.097|   1.079 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  54   |   23786|      505.01|   1.025|   1.016|   1.014|   1.012 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  29   |       7|        0.32|   1.000|   1.000|   1.000|   1.000 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  44   |      20|        0.46|   1.074|   1.097|   1.102|   1.108 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  46   |    2327|      225.05|   1.074|   1.062|   1.059|   1.056 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  52   |    1696|      197.15|   1.033|   1.022|   1.019|   1.016 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  28   |       2|        0.11|   1.000|   1.000|   1.000|   1.000 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000|   1.000|   1.000|   1.000 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  26   |      12|        0.21|   1.137|   1.046|   1.018|   0.987 |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  56   |      56|        0.85|   1.029|   1.010|   1.005|   1.000 |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  30   |       7|        0.86|   1.030|   1.021|   1.015|   1.008 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  32   |       8|        5.87|   1.000|   1.000|   1.000|   1.000 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  38   |      40|        3.37|   1.021|   0.999|   0.994|   0.988 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  40   |    2854|       34.32|   1.069|   1.053|   1.049|   1.044 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  57   |   62392|      189.33|   1.077|   1.050|   1.044|   1.037 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  44   |     215|        5.14|   1.078|   1.060|   1.055|   1.051 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  37   |      68|        6.83|   1.095|   1.086|   1.085|   1.084 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  46   |   21575|      324.75|   1.058|   1.037|   1.032|   1.027 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  28   |      13|        3.81|   1.046|   1.051|   1.053|   1.054 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  30   |       8|        0.24|   1.061|   1.091|   1.096|   1.101 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  30   |      10|        0.32|   1.010|   1.016|   1.017|   1.018 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  24   |       3|        0.18|   1.073|   1.032|   1.006|   0.978 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  34   |       4|        0.26|   1.000|   1.000|   1.000|   1.000 |

