# State and Country COVID-19 Analysis #
## Updated: 2020-04-25 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  42   |   24093|     1238.50|   1.071|   1.042|   1.034|   1.026 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  46   |    6244|      702.96|   1.087|   1.060|   1.053|   1.047 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  37   |    3158|      316.22|   1.070|   1.053|   1.049|   1.045 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  36   |    2647|      380.82|   1.114|   1.107|   1.104|   1.102 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  39   |    1847|      145.79|   1.086|   1.066|   1.061|   1.056 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  37   |    1863|      522.57|   1.110|   1.085|   1.078|   1.072 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  37   |    1991|      155.51|   1.119|   1.097|   1.091|   1.085 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  42   |    1695|      364.55|   1.059|   1.047|   1.044|   1.042 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  52   |    1703|       43.11|   1.081|   1.069|   1.066|   1.064 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  48   |    1102|       51.29|   1.074|   1.055|   1.050|   1.045 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  56   |   60295|      182.97|   1.082|   1.055|   1.048|   1.041 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  64   |   27197|      451.49|   1.023|   1.017|   1.015|   1.014 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  53   |   23389|      496.57|   1.026|   1.017|   1.014|   1.012 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  70   |   28669|      427.41|   1.043|   1.012|   1.004|   0.996 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  45   |   20787|      312.89|   1.062|   1.038|   1.033|   1.027 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  45   |    7316|      634.84|   1.066|   1.034|   1.026|   1.018 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  47   |    6063|       72.91|   1.061|   1.044|   1.040|   1.036 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  65   |    5812|       69.70|   1.020|   1.015|   1.013|   1.012 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  45   |    3356|        2.39|   1.000|   1.000|   1.000|   1.000 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  50   |    4497|      257.62|   1.042|   1.031|   1.029|   1.026 |


# US and Selected States #
## United States ##
![United States](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)

## Florida ##
![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)

## Maryland ##
![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)

## Maine ##
![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)

# US States #
|State|Days|Deaths|Deaths/1M|DDGR[-7]|DDGR[-3]|DDGR[-2]|DDGR[-1]|
|-----|----|------|---------|----------|--------|---------|---------|
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  31   |     216|       44.06|   1.075|   1.062|   1.058|   1.054 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  31   |       9|       12.38|   1.013|   0.999|   0.995|   0.992 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  35   |     263|       36.16|   1.074|   1.075|   1.075|   1.076 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  32   |      47|       15.58|   1.051|   1.031|   1.026|   1.022 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  52   |    1703|       43.11|   1.081|   1.069|   1.066|   1.064 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  42   |     599|      104.10|   1.073|   1.073|   1.074|   1.075 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  37   |    1863|      522.57|   1.110|   1.085|   1.078|   1.072 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  30   |     102|      104.79|   1.095|   1.080|   1.075|   1.071 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  48   |    1102|       51.29|   1.074|   1.055|   1.050|   1.045 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  44   |     953|       89.72|   1.064|   1.054|   1.052|   1.049 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  25   |      13|        8.94|   1.016|   1.059|   1.071|   1.082 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  30   |      56|       31.10|   1.068|   1.043|   1.037|   1.033 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  39   |    1847|      145.79|   1.086|   1.066|   1.061|   1.056 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  40   |     772|      114.72|   1.077|   1.055|   1.049|   1.044 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  31   |     106|       33.55|   1.091|   1.071|   1.065|   1.060 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  43   |     129|       44.22|   1.077|   1.048|   1.040|   1.033 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  40   |     204|       45.66|   1.068|   1.060|   1.059|   1.057 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  42   |    1695|      364.55|   1.059|   1.047|   1.044|   1.042 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  29   |      47|       34.61|   1.086|   1.072|   1.068|   1.064 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  37   |     840|      138.90|   1.124|   1.115|   1.114|   1.113 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  36   |    2647|      380.82|   1.114|   1.107|   1.104|   1.102 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  37   |    3158|      316.22|   1.070|   1.053|   1.049|   1.045 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  35   |     220|       38.93|   1.104|   1.112|   1.113|   1.115 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  37   |     218|       73.39|   1.073|   1.061|   1.058|   1.055 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  37   |     273|       44.43|   1.074|   1.061|   1.057|   1.054 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  29   |      15|       14.02|   1.074|   1.093|   1.096|   1.099 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  28   |      49|       25.10|   1.083|   1.121|   1.130|   1.140 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  40   |     199|       64.49|   1.057|   1.044|   1.041|   1.039 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  33   |      54|       39.76|   1.076|   1.067|   1.064|   1.061 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  46   |    6244|      702.96|   1.087|   1.060|   1.053|   1.047 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  31   |      85|       40.64|   1.119|   1.103|   1.099|   1.095 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  42   |   24093|     1238.50|   1.071|   1.042|   1.034|   1.026 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  31   |     313|       29.87|   1.116|   1.088|   1.080|   1.071 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  29   |      15|       19.93|   1.048|   1.102|   1.116|   1.131 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  36   |     708|       60.55|   1.086|   1.078|   1.076|   1.074 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  37   |     188|       47.53|   1.058|   1.054|   1.053|   1.053 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  41   |      89|       21.16|   1.049|   1.033|   1.029|   1.025 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  37   |    1991|      155.51|   1.119|   1.097|   1.091|   1.085 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  35   |      74|       23.10|   1.049|   1.034|   1.030|   1.027 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  28   |     217|      204.85|   1.103|   1.073|   1.064|   1.055 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  40   |     157|       30.44|   1.059|   1.048|   1.046|   1.043 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  45   |       9|       10.58|   1.000|   1.000|   1.000|   1.000 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  35   |     174|       25.46|   1.042|   1.030|   1.026|   1.023 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  39   |     654|       22.56|   1.075|   1.051|   1.045|   1.039 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  34   |      38|       11.86|   1.077|   1.076|   1.075|   1.074 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  36   |      45|       72.18|   1.044|   1.034|   1.031|   1.028 |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  42   |     427|       50.07|   1.100|   1.084|   1.080|   1.076 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  56   |     760|       99.76|   1.034|   1.023|   1.021|   1.018 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  26   |      35|       19.48|   1.167|   1.122|   1.107|   1.090 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  36   |     276|       47.35|   1.058|   1.037|   1.032|   1.027 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  12   |       8|       14.19|   1.260|   1.442|   1.518|   1.518 |


# All Countries # 
|Country|Days|Deaths|Deaths/1M|DDGR[-7]|DDGR[-3]|DDGR[-2]|DDGR[-1]|
|-----|----|------|---------|----------|--------|---------|---------|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  34   |      45|        1.40|   1.079|   1.058|   1.053|   1.048 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  45   |      28|        9.68|   1.013|   1.010|   1.009|   1.008 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  44   |     439|       10.22|   1.039|   1.016|   1.011|   1.005 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  27   |       2|        0.06|   1.000|   1.000|   1.000|   1.000 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  48   |     179|        3.99|   1.062|   1.047|   1.044|   1.040 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  30   |      27|        9.01|   1.062|   1.046|   1.042|   1.039 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  55   |      79|        3.09|   1.028|   1.006|   1.001|   0.996 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  44   |     550|       61.83|   1.042|   1.030|   1.027|   1.024 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  43   |      23|        2.27|   1.054|   1.035|   1.031|   1.026 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  40   |       8|        5.05|   1.024|   1.015|   1.014|   1.012 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  38   |     152|        0.90|   1.132|   1.098|   1.088|   1.077 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  25   |      64|        6.82|   1.082|   1.060|   1.056|   1.052 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  45   |    7316|      634.84|   1.066|   1.034|   1.026|   1.018 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  19   |       1|        0.09|   1.000|   1.000|   1.000|   1.000 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  27   |      42|        3.70|   1.040|   1.061|   1.070|   1.079 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  35   |      56|       16.93|   1.032|   1.031|   1.031|   1.030 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  25   |       1|        0.43|   1.000|   1.000|   1.000|   1.000 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  39   |    3679|       17.40|   1.095|   1.081|   1.077|   1.073 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  45   |      54|        7.83|   1.053|   1.048|   1.047|   1.046 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  38   |      43|        2.04|   1.039|   1.028|   1.025|   1.022 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  12   |       1|        0.09|   1.000|   1.000|   1.000|   1.000 |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  31   |      52|        1.96|   1.153|   1.091|   1.072|   1.051 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  47   |    2618|       68.89|   1.113|   1.092|   1.087|   1.082 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  34   |     181|        9.47|   1.076|   1.064|   1.061|   1.058 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  45   |    3356|        2.39|   1.000|   1.000|   1.000|   1.000 |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  34   |     233|        4.71|   1.074|   1.056|   1.052|   1.048 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  37   |       7|        1.30|   1.064|   1.059|   1.057|   1.055 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  37   |      56|       13.75|   1.073|   1.046|   1.038|   1.030 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  38   |      49|        4.35|   1.085|   1.070|   1.066|   1.061 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  42   |     415|       71.23|   1.037|   1.027|   1.024|   1.022 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  39   |     281|       27.10|   1.056|   1.037|   1.032|   1.028 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  42   |     600|       34.32|   1.052|   1.041|   1.039|   1.036 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  48   |     318|        3.18|   1.064|   1.048|   1.043|   1.039 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  25   |       8|        1.21|   1.027|   1.027|   1.027|   1.028 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  20   |       3|        0.03|   1.000|   1.000|   1.000|   1.000 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  35   |     178|       32.16|   1.103|   1.130|   1.138|   1.146 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  70   |   28669|      427.41|   1.043|   1.012|   1.004|   0.996 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  36   |       1|        0.46|   1.000|   1.000|   1.000|   1.000 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  33   |       1|        0.43|   1.000|   1.000|   1.000|   1.000 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  21   |       5|        1.39|   1.065|   1.083|   1.079|   1.074 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  47   |    6063|       72.91|   1.061|   1.044|   1.040|   1.036 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  35   |      10|        0.32|   1.023|   1.016|   1.014|   1.013 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  45   |     129|       12.01|   1.026|   1.023|   1.022|   1.022 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  40   |      10|        0.62|   1.088|   1.102|   1.106|   1.110 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  10   |       6|        0.49|   1.442|   1.063|   1.063|   1.000 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  20   |       5|        0.47|   1.000|   1.128|   1.183|   1.237 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  30   |      54|        5.93|   1.085|   1.035|   1.021|   1.005 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000|   1.000|   1.000|   1.000 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  41   |     273|       27.94|   1.095|   1.068|   1.062|   1.055 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  45   |     822|        0.60|   1.090|   1.059|   1.052|   1.044 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  45   |     735|        2.75|   1.060|   1.037|   1.031|   1.025 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  65   |    5812|       69.70|   1.020|   1.015|   1.013|   1.012 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  52   |      88|        2.25|   1.013|   1.005|   1.002|   1.000 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  45   |     944|      191.89|   1.090|   1.082|   1.080|   1.078 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  35   |     208|       22.67|   1.061|   1.037|   1.031|   1.024 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  64   |   27197|      451.49|   1.023|   1.017|   1.015|   1.014 |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  37   |       6|        2.38|   1.000|   1.000|   1.000|   1.000 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  72   |     320|        2.54|   1.089|   1.097|   1.099|   1.102 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  29   |       7|        0.66|   1.000|   1.000|   1.000|   1.000 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  31   |      22|        1.19|   1.065|   1.041|   1.036|   1.032 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  30   |      15|        0.32|   1.068|   1.026|   1.015|   1.002 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  30   |      13|        7.21|   1.025|   1.003|   0.998|   0.993 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  21   |      17|        3.75|   1.189|   1.175|   1.151|   1.124 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  22   |       8|        1.27|   1.024|   1.075|   1.075|   1.072 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  22   |      13|        6.67|   1.011|   1.208|   1.246|   1.281 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  46   |      22|        3.23|   1.009|   1.008|   1.008|   1.007 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  21   |       8|        1.82|   1.052|   1.017|   1.006|   0.994 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  23   |       1|        0.15|   1.000|   1.000|   1.000|   1.000 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  35   |      42|       15.01|   1.055|   1.028|   1.021|   1.015 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  39   |      97|        2.97|   1.023|   1.015|   1.013|   1.012 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  27   |      20|        0.98|   1.048|   1.087|   1.104|   1.121 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  26   |       1|        0.25|   1.000|   1.000|   1.000|   1.000 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  37   |    1154|        9.12|   1.133|   1.135|   1.136|   1.137 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  38   |      90|       33.65|   1.086|   1.064|   1.057|   1.050 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  46   |     162|        4.51|   1.031|   1.018|   1.015|   1.012 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  50   |    4497|      257.62|   1.042|   1.031|   1.029|   1.026 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  27   |      17|        3.51|   1.139|   1.083|   1.079|   1.077 |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  29   |       3|        0.47|   1.173|   1.129|   1.115|   1.099 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  31   |      25|        1.12|   1.066|   1.056|   1.052|   1.048 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  33   |      33|        0.16|   1.112|   1.117|   1.117|   1.117 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  34   |      60|       28.76|   1.047|   1.023|   1.017|   1.011 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  42   |     205|       38.21|   1.043|   1.031|   1.028|   1.025 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  25   |      10|        2.12|   1.104|   1.084|   1.075|   1.065 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  37   |     257|        1.17|   1.097|   1.095|   1.094|   1.094 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  45   |     159|       37.80|   1.060|   1.050|   1.047|   1.045 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  35   |       9|        1.28|   1.036|   1.025|   1.022|   1.020 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  36   |     644|       20.04|   1.105|   1.106|   1.106|   1.106 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  83   |     657|        6.06|   1.045|   1.029|   1.025|   1.021 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  44   |     503|       13.10|   1.073|   1.054|   1.049|   1.045 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  39   |     871|       84.71|   1.049|   1.036|   1.033|   1.029 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  28   |      10|        3.78|   1.036|   1.050|   1.053|   1.054 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  34   |     575|       29.62|   1.054|   1.048|   1.046|   1.045 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  37   |     664|        4.53|   1.151|   1.126|   1.119|   1.112 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  32   |     129|        3.76|   1.071|   1.053|   1.050|   1.046 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  24   |       7|        0.46|   1.101|   1.131|   1.128|   1.123 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  36   |     136|       19.59|   1.048|   1.018|   1.009|   1.001 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  35   |      12|        2.16|   1.040|   1.019|   1.014|   1.010 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  28   |      17|        3.20|   1.124|   1.074|   1.049|   1.022 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  42   |      86|       41.18|   1.045|   1.026|   1.022|   1.017 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  17   |      16|        1.01|   1.215|   1.153|   1.205|   1.258 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  29   |      79|        1.34|   1.113|   1.079|   1.070|   1.062 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198|   1.116|   1.097|   1.079 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  53   |   23389|      496.57|   1.026|   1.017|   1.014|   1.012 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  28   |       7|        0.32|   1.000|   1.000|   1.000|   1.000 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  43   |      18|        0.42|   1.000|   1.000|   1.000|   1.000 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  45   |    2207|      213.48|   1.078|   1.066|   1.063|   1.061 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  51   |    1663|      193.27|   1.036|   1.023|   1.020|   1.017 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  27   |       2|        0.11|   1.000|   1.000|   1.000|   1.000 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000|   1.000|   1.000|   1.000 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  25   |      12|        0.21|   1.148|   1.065|   1.042|   1.016 |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  55   |      56|        0.84|   1.033|   1.011|   1.006|   1.001 |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  29   |       7|        0.87|   1.025|   1.030|   1.029|   1.027 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  31   |       8|        5.87|   1.000|   1.000|   1.000|   1.000 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  37   |      40|        3.38|   1.027|   1.001|   0.995|   0.988 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  39   |    2729|       32.81|   1.073|   1.057|   1.053|   1.048 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  56   |   60295|      182.97|   1.082|   1.055|   1.048|   1.041 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  43   |     206|        4.92|   1.084|   1.066|   1.062|   1.058 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  36   |      62|        6.23|   1.096|   1.079|   1.076|   1.074 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  45   |   20787|      312.89|   1.062|   1.038|   1.033|   1.027 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  27   |      12|        3.54|   1.044|   1.050|   1.052|   1.053 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  29   |       8|        0.23|   1.048|   1.098|   1.109|   1.120 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  29   |      10|        0.31|   1.006|   1.020|   1.024|   1.027 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  23   |       2|        0.11|   1.061|   1.050|   1.032|   1.009 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  33   |       4|        0.25|   1.000|   1.000|   1.000|   1.000 |

