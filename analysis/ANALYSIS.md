# State and Country COVID-19 Analysis #
## Updated: 2020-04-24 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  41   |   23247|     1194.98|   1.077|   1.046|   1.038|   1.030 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  45   |    5915|      665.96|   1.093|   1.063|   1.055|   1.048 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  36   |    3029|      303.27|   1.073|   1.052|   1.047|   1.042 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  35   |    2413|      347.20|   1.118|   1.110|   1.108|   1.107 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  36   |    1875|      146.49|   1.126|   1.114|   1.112|   1.110 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  38   |    1749|      138.04|   1.091|   1.067|   1.062|   1.056 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  36   |    1744|      489.21|   1.116|   1.091|   1.084|   1.077 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  41   |    1617|      347.81|   1.061|   1.046|   1.042|   1.038 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  51   |    1595|       40.37|   1.082|   1.068|   1.064|   1.061 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  47   |    1042|       48.51|   1.078|   1.056|   1.050|   1.044 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  55   |   57287|      173.84|   1.087|   1.058|   1.050|   1.043 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  63   |   26708|      443.38|   1.025|   1.017|   1.016|   1.014 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  52   |   23108|      490.61|   1.028|   1.017|   1.015|   1.013 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  69   |   28057|      418.29|   1.049|   1.015|   1.007|   0.998 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  44   |   20226|      304.45|   1.067|   1.041|   1.035|   1.028 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  44   |    7193|      624.12|   1.073|   1.038|   1.029|   1.020 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  46   |    5852|       70.38|   1.064|   1.046|   1.041|   1.037 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  64   |    5747|       68.93|   1.021|   1.015|   1.014|   1.012 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  44   |    3355|        2.39|   1.000|   1.000|   1.000|   1.000 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  49   |    4364|      249.99|   1.044|   1.032|   1.029|   1.026 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  30   |     207|       42.19|   1.078|   1.068|   1.065|   1.062 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  30   |       9|       12.46|   1.018|   1.000|   0.996|   0.992 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  34   |     245|       33.66|   1.073|   1.071|   1.071|   1.071 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  31   |      45|       15.03|   1.059|   1.031|   1.024|   1.018 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)|  51   |    1595|       40.37|   1.082|   1.068|   1.064|   1.061 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)|  41   |     544|       94.39|   1.072|   1.062|   1.059|   1.058 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)|  36   |    1744|      489.21|   1.116|   1.091|   1.084|   1.077 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  29   |      95|       97.68|   1.098|   1.085|   1.081|   1.078 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)|  47   |    1042|       48.51|   1.078|   1.056|   1.050|   1.044 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)|  43   |     911|       85.80|   1.069|   1.057|   1.054|   1.052 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  24   |      12|        8.27|   1.015|   1.045|   1.055|   1.065 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  29   |      54|       30.09|   1.077|   1.045|   1.038|   1.031 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)|  38   |    1749|      138.04|   1.091|   1.067|   1.062|   1.056 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)|  39   |     734|      108.97|   1.084|   1.056|   1.049|   1.043 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  30   |      99|       31.32|   1.099|   1.069|   1.060|   1.052 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)|  42   |     125|       43.00|   1.084|   1.056|   1.049|   1.042 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)|  39   |     193|       43.25|   1.071|   1.061|   1.059|   1.057 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)|  41   |    1617|      347.81|   1.061|   1.046|   1.042|   1.038 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  28   |      43|       32.34|   1.086|   1.068|   1.060|   1.053 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)|  36   |     765|      126.54|   1.129|   1.127|   1.128|   1.130 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)|  35   |    2413|      347.20|   1.118|   1.110|   1.108|   1.107 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)|  36   |    3029|      303.27|   1.073|   1.052|   1.047|   1.042 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  34   |     197|       34.92|   1.102|   1.110|   1.112|   1.114 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)|  36   |     208|       69.96|   1.076|   1.067|   1.064|   1.062 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)|  36   |     258|       41.96|   1.076|   1.061|   1.056|   1.052 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  28   |      14|       13.24|   1.068|   1.101|   1.109|   1.116 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  27   |      43|       22.16|   1.075|   1.108|   1.117|   1.125 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)|  39   |     190|       61.60|   1.061|   1.038|   1.033|   1.028 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  32   |      51|       37.71|   1.079|   1.065|   1.060|   1.055 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)|  45   |    5915|      665.96|   1.093|   1.063|   1.055|   1.048 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  30   |      78|       37.40|   1.127|   1.097|   1.090|   1.082 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)|  41   |   23247|     1194.98|   1.077|   1.046|   1.038|   1.030 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  30   |     296|       28.19|   1.120|   1.099|   1.091|   1.084 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  28   |      14|       18.27|   1.045|   1.112|   1.132|   1.154 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)|  35   |     661|       56.53|   1.087|   1.080|   1.078|   1.076 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)|  36   |     179|       45.20|   1.058|   1.057|   1.056|   1.056 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)|  40   |      87|       20.68|   1.052|   1.036|   1.031|   1.027 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)|  36   |    1875|      146.49|   1.126|   1.114|   1.112|   1.110 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  34   |      70|       21.97|   1.054|   1.029|   1.022|   1.015 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  27   |     205|      193.87|   1.114|   1.084|   1.075|   1.066 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)|  39   |     149|       28.94|   1.060|   1.040|   1.035|   1.030 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)|  44   |       9|        9.94|   1.000|   1.000|   1.000|   1.000 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  34   |     171|       24.96|   1.045|   1.033|   1.029|   1.026 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)|  38   |     630|       21.73|   1.080|   1.054|   1.047|   1.040 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  33   |      35|       10.94|   1.076|   1.079|   1.080|   1.080 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)|  35   |      44|       69.94|   1.045|   1.037|   1.034|   1.031 |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)|  41   |     395|       46.25|   1.104|   1.086|   1.082|   1.077 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)|  55   |     737|       96.72|   1.034|   1.020|   1.017|   1.013 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  25   |      32|       18.01|   1.173|   1.141|   1.131|   1.121 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)|  35   |     268|       45.97|   1.063|   1.042|   1.037|   1.032 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  11   |       7|       12.09|   1.260|   1.211|   1.386|   1.533 |


# All Countries # 
|Country|Days|Deaths|Deaths/1M|DDGR[-7]|DDGR[-3]|DDGR[-2]|DDGR[-1]|
|-----|----|------|---------|----------|--------|---------|---------|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  33   |      43|        1.33|   1.082|   1.061|   1.055|   1.048 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)|  44   |      27|        9.62|   1.014|   1.010|   1.009|   1.007 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)|  43   |     432|       10.06|   1.044|   1.018|   1.011|   1.005 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  26   |       2|        0.06|   1.000|   1.000|   1.000|   1.000 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)|  47   |     170|        3.79|   1.064|   1.046|   1.041|   1.037 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  29   |      25|        8.52|   1.065|   1.050|   1.045|   1.041 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)|  54   |      79|        3.06|   1.028|   1.000|   0.993|   0.987 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)|  43   |     536|       60.19|   1.045|   1.031|   1.028|   1.025 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)|  42   |      22|        2.21|   1.062|   1.047|   1.043|   1.038 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)|  39   |       8|        4.92|   1.025|   1.008|   1.004|   0.999 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)|  37   |     142|        0.84|   1.140|   1.112|   1.104|   1.096 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  24   |      61|        6.52|   1.092|   1.066|   1.062|   1.059 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)|  44   |    7193|      624.12|   1.073|   1.038|   1.029|   1.020 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  18   |       1|        0.09|   1.000|   1.000|   1.000|   1.000 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  26   |      39|        3.38|   1.043|   1.048|   1.055|   1.061 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  34   |      54|       16.50|   1.033|   1.033|   1.033|   1.033 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  24   |       1|        0.43|   1.000|   1.000|   1.000|   1.000 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)|  38   |    3390|       16.04|   1.097|   1.077|   1.071|   1.066 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)|  44   |      52|        7.49|   1.053|   1.046|   1.044|   1.042 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)|  37   |      42|        2.00|   1.042|   1.030|   1.027|   1.023 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  11   |       1|        0.09|   1.000|   1.000|   1.000|   1.000 |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  30   |      51|        1.92|   1.161|   1.137|   1.127|   1.115 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)|  46   |    2431|       63.99|   1.119|   1.099|   1.094|   1.088 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  33   |     172|        8.99|   1.081|   1.067|   1.064|   1.060 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)|  44   |    3355|        2.39|   1.000|   1.000|   1.000|   1.000 |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  33   |     222|        4.49|   1.081|   1.059|   1.054|   1.050 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)|  36   |       6|        1.26|   1.072|   1.110|   1.118|   1.126 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)|  36   |      55|       13.46|   1.080|   1.057|   1.050|   1.042 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)|  37   |      45|        4.03|   1.088|   1.068|   1.062|   1.057 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)|  41   |     405|       69.50|   1.040|   1.027|   1.024|   1.021 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)|  38   |     275|       26.55|   1.061|   1.040|   1.036|   1.031 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)|  41   |     578|       33.09|   1.057|   1.043|   1.040|   1.037 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)|  47   |     305|        3.04|   1.069|   1.052|   1.048|   1.044 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  24   |       8|        1.17|   1.026|   1.022|   1.018|   1.015 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  19   |       3|        0.03|   1.000|   1.000|   1.000|   1.000 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  34   |     158|       28.63|   1.098|   1.143|   1.155|   1.167 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)|  69   |   28057|      418.29|   1.049|   1.015|   1.007|   0.998 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)|  35   |       1|        0.46|   1.000|   1.000|   1.000|   1.000 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  32   |       1|        0.43|   1.000|   1.000|   1.000|   1.000 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  20   |       5|        1.35|   1.042|   1.081|   1.077|   1.072 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)|  46   |    5852|       70.38|   1.064|   1.046|   1.041|   1.037 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  34   |       9|        0.31|   1.027|   1.011|   1.007|   1.004 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)|  44   |     126|       11.71|   1.027|   1.023|   1.022|   1.022 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)|  39   |       9|        0.56|   1.081|   1.074|   1.071|   1.069 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  19   |       4|        0.38|   1.007|   1.069|   1.108|   1.147 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  29   |      51|        5.62|   1.088|   1.038|   1.022|   1.004 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       2|        0.27|   1.000|   1.000|   1.000|   1.000 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)|  40   |     258|       26.39|   1.101|   1.071|   1.064|   1.056 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)|  44   |     784|        0.58|   1.097|   1.062|   1.053|   1.045 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)|  44   |     716|        2.68|   1.065|   1.041|   1.034|   1.028 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)|  64   |    5747|       68.93|   1.021|   1.015|   1.014|   1.012 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)|  51   |      87|        2.23|   1.014|   1.004|   1.002|   0.999 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)|  44   |     855|      173.65|   1.089|   1.076|   1.072|   1.069 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  34   |     205|       22.30|   1.066|   1.045|   1.040|   1.033 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)|  63   |   26708|      443.38|   1.025|   1.017|   1.016|   1.014 |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)|  36   |       6|        2.22|   1.030|   1.055|   1.061|   1.067 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)|  71   |     292|        2.32|   1.088|   1.097|   1.099|   1.101 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  28   |       7|        0.66|   1.000|   1.000|   1.000|   1.000 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  30   |      21|        1.10|   1.075|   1.029|   1.017|   1.006 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  29   |      15|        0.32|   1.073|   1.039|   1.030|   1.019 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  29   |      13|        7.27|   1.033|   1.006|   1.000|   0.993 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  20   |      15|        3.43|   1.163|   1.223|   1.230|   1.236 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  21   |       8|        1.22|   1.005|   1.084|   1.099|   1.112 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  21   |      11|        5.89|   1.008|   1.200|   1.258|   1.313 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)|  45   |      22|        3.21|   1.009|   1.006|   1.005|   1.005 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  20   |       8|        1.85|   1.055|   1.024|   1.012|   0.999 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  22   |       1|        0.15|   1.000|   1.000|   1.000|   1.000 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  34   |      41|       14.83|   1.061|   1.034|   1.027|   1.020 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)|  38   |      96|        2.94|   1.025|   1.016|   1.014|   1.012 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  26   |      18|        0.87|   1.056|   1.057|   1.068|   1.080 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  25   |       1|        0.25|   1.000|   1.000|   1.000|   1.000 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)|  36   |    1002|        7.91|   1.132|   1.118|   1.114|   1.111 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)|  37   |      86|       31.98|   1.088|   1.071|   1.066|   1.059 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)|  45   |     158|        4.41|   1.034|   1.015|   1.011|   1.007 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)|  49   |    4364|      249.99|   1.044|   1.032|   1.029|   1.026 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  26   |      16|        3.22|   1.174|   1.071|   1.057|   1.045 |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  28   |       3|        0.42|   1.147|   1.131|   1.111|   1.087 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  30   |      24|        1.08|   1.072|   1.056|   1.051|   1.045 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  32   |      31|        0.15|   1.113|   1.112|   1.112|   1.110 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  33   |      59|       28.34|   1.052|   1.029|   1.023|   1.017 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)|  41   |     199|       37.11|   1.047|   1.031|   1.028|   1.024 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  24   |       9|        1.97|   1.102|   1.090|   1.079|   1.067 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)|  36   |     235|        1.07|   1.097|   1.099|   1.099|   1.100 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)|  44   |     153|       36.21|   1.063|   1.053|   1.050|   1.048 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  34   |       9|        1.27|   1.038|   1.022|   1.017|   1.013 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)|  35   |     585|       18.20|   1.107|   1.108|   1.109|   1.110 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)|  82   |     654|        6.03|   1.048|   1.033|   1.029|   1.025 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)|  43   |     474|       12.34|   1.077|   1.051|   1.045|   1.038 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)|  38   |     845|       82.18|   1.052|   1.037|   1.033|   1.029 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  27   |      10|        3.68|   1.033|   1.053|   1.059|   1.064 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  33   |     550|       28.35|   1.057|   1.049|   1.047|   1.045 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)|  36   |     602|        4.10|   1.157|   1.135|   1.129|   1.122 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  31   |     122|        3.58|   1.077|   1.055|   1.050|   1.045 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  23   |       7|        0.41|   1.069|   1.213|   1.246|   1.277 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)|  35   |     136|       19.54|   1.054|   1.027|   1.020|   1.012 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  34   |      12|        2.15|   1.045|   1.018|   1.012|   1.006 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  27   |      16|        2.98|   1.020|   1.047|   1.053|   1.059 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)|  41   |      85|       40.45|   1.051|   1.031|   1.026|   1.022 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  16   |       9|        0.54|   1.316|   1.093|   1.144|   1.195 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  28   |      74|        1.26|   1.117|   1.075|   1.060|   1.044 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      54|        1.04|   1.198|   1.116|   1.097|   1.079 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)|  52   |   23108|      490.61|   1.028|   1.017|   1.015|   1.013 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  27   |       7|        0.32|   1.000|   1.000|   1.000|   1.000 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)|  42   |      16|        0.38|   1.000|   1.000|   1.000|   1.000 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)|  44   |    2084|      201.56|   1.080|   1.067|   1.064|   1.061 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)|  50   |    1634|      189.95|   1.039|   1.025|   1.021|   1.018 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  26   |       2|        0.11|   1.000|   1.145|   1.000|   1.000 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|        0.04|   1.000|   1.000|   1.000|   1.000 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  24   |      11|        0.21|   1.141|   1.148|   1.140|   1.130 |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)|  54   |      56|        0.85|   1.036|   1.012|   1.006|   1.000 |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  28   |       7|        0.88|   1.078|   1.056|   1.042|   1.027 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  30   |       8|        5.87|   1.000|   1.000|   1.000|   1.000 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)|  36   |      40|        3.43|   1.033|   1.005|   0.997|   0.990 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)|  38   |    2610|       31.39|   1.078|   1.061|   1.057|   1.053 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)|  55   |   57287|      173.84|   1.087|   1.058|   1.050|   1.043 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)|  42   |     194|        4.64|   1.087|   1.066|   1.061|   1.056 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)|  35   |      56|        5.68|   1.101|   1.071|   1.064|   1.057 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)|  44   |   20226|      304.45|   1.067|   1.041|   1.035|   1.028 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  26   |      12|        3.43|   1.041|   1.055|   1.059|   1.064 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  28   |       7|        0.20|   1.041|   1.092|   1.105|   1.119 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  28   |      10|        0.31|   1.002|   1.023|   1.029|   1.035 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  22   |       2|        0.11|   1.030|   1.070|   1.059|   1.042 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  32   |       3|        0.20|   1.000|   1.000|   1.000|   1.000 |

