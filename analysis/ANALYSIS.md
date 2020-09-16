# State and Country COVID-19 Analysis #
## Updated: at 2020-09-16 for data as of 2020-09-15 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.3% of deaths and 39.0% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

![Deaths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeaths.png)

![Daily Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeathsPerDay.png)

Despite quite large rhetorical, political, and social differences in their approaches to the pandemic, the rates of death in these four states appear to be converging.  Deaths in Florida and California have followed nearly identical trajectories since early April 2020 with Florida somewhat higher, but both falling well below New York and above Texas.


![Cases](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestConfirmed%20Cases.png)

![Daily Case Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestConfirmed%20CasesPerDay.png)

The next two plots show the latest 21-day trajectory of deaths/day/million vs confirmed cases/day/million for the four largest population states and for all states with non-trival death rates.

![Four State Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/FourDailyCasesVsDeaths.png)

![All States Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/AllDailyCasesVsDeaths.png)

The next plots shows the total US deaths to date from COVID-19 compared to historical seasonal flus and 20th century pandemics.  The number of deaths in each flu/pandemic is divided by the US population in millions at the time of the flu/pandemic.   In all cases the midpoint CDC estimate for fatalities is used.  In all cases except the Spanish Flu (1918) these are for a full year.  The vertical axis is limited for readability; the Spanish Flu was nearly 10 times more deadly than the 1957 Asian flu on a _per capita_ basis.

![Compared To Flus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/ComparedToFlus.png)


Daily Death Growth Rate (DDGR)  is the cube root of Arnold Kling's [Three Day Death Reproduction Rate (3DDRR)](http://www.arnoldkling.com/blog/the-3ddrr/).  The 3DDRR is calculated by dividing the cumulative total number of deaths on a given day by the  cumulative total number of deaths three days previously; yes, technically this is a factor not a rate, but we must grant Professor Kling the author's naming rights.  Taking the cube root converts this to the geometric mean for the three days.  These values are LOWESS filtered to generate local-error minimizing non-parametric trend lines.

If deaths remain constant over the three days, the DDGR equals one.  A value of 2 would indicate that the number of deaths doubles every day.

Up until June 29, 2020, this page reported the DDGR directly, but as the high growth phase of the pandemic has passed, the DDGR values have  declined toward one, required progressively more digits of precision to show differences.  Accordingly, henceforth this page will report DDGR as a true growth percentage rate (100*(DDGR-1)) which will be termed the Daily Death Rate of Growth (DDRG).  A DDRG of 100% means the number of deaths doubles every day, 0% means no new deaths.


# Ten US States with Highest Death Tolls #

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.4% of deaths and 56.6% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 168   |   33051|    1698.983|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 168   |   16031|    1804.805|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 168   |   14739|     373.029|   0.7%/ 98|   0.6%/110|   0.6%/113|   0.6%/117 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 168   |   14902|     513.940|   0.8%/ 84|   0.7%/103|   0.6%/110|   0.6%/117 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 168   |   12945|     602.722|   0.8%/ 88|   0.7%/102|   0.6%/107|   0.6%/111 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 168   |    9238|    1329.349|   0.1%/520|   0.1%/550|   0.1%/558|   0.1%/566 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 168   |    8574|     676.615|   0.2%/278|   0.2%/278|   0.2%/278|   0.2%/278 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 168   |    7877|     615.309|   0.2%/447|   0.1%/487|   0.1%/498|   0.1%/510 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 168   |    6933|     694.209|   0.2%/461|   0.1%/474|   0.1%/478|   0.1%/481 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 168   |    6549|     616.840|   0.8%/ 83|   0.7%/ 97|   0.7%/101|   0.7%/105 |


- Days - Number of days since first death
- Deaths - Total deaths to date
- Deaths/1M - Deaths per million in population
- DDRG - **LOWESS Smoothed** Daily Deaths Rate of Growth. [n:m] total deaths n days ago over m days ago followed by the DDRG expressed as the number of days to double the total deaths count if that rate holds

# Ten Countries with Highest Death Tolls #

Deaths in the 10 countries with the highest death tolls expressed as deaths per 1 million population. 

![Countries with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/Countries10WorstDeathRates.png)

Daily Death Rate of Growth (DDRG) in the 10 countries with the highest death tolls.

![Countries with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/Countries10WorstDDGR.png)

|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 168   |  196525|     596.353|   0.4%/171|   0.4%/186|   0.4%/190|   0.4%/194 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 168   |  134185|     634.712|   0.6%/119|   0.5%/133|   0.5%/137|   0.5%/141 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 168   |   82315|      60.471|   1.5%/ 48|   1.4%/ 50|   1.4%/ 51|   1.4%/ 51 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 168   |   72323|     571.370|   0.7%/103|   0.6%/112|   0.6%/115|   0.6%/118 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 168   |   41738|     628.254|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 168   |   35627|     591.432|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 168   |   30933|     461.170|   0.1%/922|   0.1%/836|   0.1%/817|   0.1%/798 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 168   |   31217|     971.551|   0.4%/154|   0.4%/175|   0.4%/182|   0.4%/188 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 168   |   29863|     634.025|   0.2%/384|   0.2%/346|   0.2%/338|   0.2%/330 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 168   |   23470|     281.490|   0.5%/129|   0.5%/135|   0.5%/137|   0.5%/138 |


# US and Selected States #

For each country and each US state, deaths per million in population is plotted on the left logarithmic axis and the raw and smoothed DDRG is plotted on the linear right axis.


## United States ##
![United States](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)

## Florida ##
![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)

## Maryland ##
![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)

## Maine ##
![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)

# US States #

Click on the link in the first column to view the deaths and DDRG charts for a specific state.

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 168   |    2423|     494.266|   0.7%/101|   0.6%/107|   0.6%/109|   0.6%/111 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 168   |      47|      63.671|   0.9%/ 77|   0.8%/ 84|   0.8%/ 86|   0.8%/ 88 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 168   |    5440|     747.342|   0.4%/182|   0.3%/254|   0.2%/281|   0.2%/316 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 168   |    1035|     342.805|   1.6%/ 44|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 168   |   14739|     373.029|   0.7%/ 98|   0.6%/110|   0.6%/113|   0.6%/117 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 168   |    1998|     346.952|   0.2%/432|   0.2%/456|   0.1%/462|   0.1%/469 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 168   |    4481|    1256.899|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 168   |     616|     632.357|   0.1%/495|   0.1%/462|   0.2%/454|   0.2%/445 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 168   |   12945|     602.722|   0.8%/ 88|   0.7%/102|   0.6%/107|   0.6%/111 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 168   |    6549|     616.840|   0.8%/ 83|   0.7%/ 97|   0.7%/101|   0.7%/105 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 168   |     111|      78.128|   2.6%/ 26|   2.4%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 168   |     439|     245.629|   0.9%/ 77|   0.7%/106|   0.6%/118|   0.5%/132 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 168   |    8574|     676.615|   0.2%/278|   0.2%/278|   0.2%/278|   0.2%/278 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 168   |    3463|     514.348|   0.3%/236|   0.3%/248|   0.3%/251|   0.3%/254 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 168   |    1250|     396.141|   0.6%/107|   0.6%/117|   0.6%/120|   0.6%/124 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 168   |     527|     181.004|   1.3%/ 52|   1.5%/ 47|   1.5%/ 45|   1.6%/ 44 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 168   |    1079|     241.505|   0.9%/ 78|   0.9%/ 80|   0.9%/ 80|   0.9%/ 80 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 168   |    5312|    1142.675|   0.4%/165|   0.4%/191|   0.3%/198|   0.3%/206 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 168   |     136|     101.446|   0.2%/322|   0.2%/330|   0.2%/331|   0.2%/332 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 168   |    3859|     638.317|   0.2%/425|   0.1%/464|   0.1%/476|   0.1%/488 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 168   |    9238|    1329.349|   0.1%/520|   0.1%/550|   0.1%/558|   0.1%/566 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 168   |    6933|     694.209|   0.2%/461|   0.1%/474|   0.1%/478|   0.1%/481 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 168   |    1979|     350.860|   0.4%/178|   0.4%/180|   0.4%/181|   0.4%/181 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 168   |    2779|     933.780|   0.7%/103|   0.6%/122|   0.5%/128|   0.5%/135 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 168   |    1771|     288.549|   0.7%/101|   0.7%/105|   0.7%/106|   0.6%/107 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 168   |     138|     129.048|   2.0%/ 35|   2.1%/ 33|   2.1%/ 33|   2.1%/ 33 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 168   |     436|     225.460|   0.6%/118|   0.6%/117|   0.6%/117|   0.6%/117 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 168   |    1508|     489.496|   0.7%/ 93|   0.6%/116|   0.6%/124|   0.5%/133 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 168   |     437|     321.042|   0.1%/815|   0.1%/860|   0.1%/867|   0.1%/873 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 168   |   16031|    1804.805|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 168   |     836|     398.759|   0.4%/172|   0.4%/195|   0.3%/202|   0.3%/210 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 168   |   33051|    1698.983|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 168   |    3124|     297.898|   0.9%/ 81|   0.8%/ 85|   0.8%/ 86|   0.8%/ 87 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 168   |     170|     223.273|   1.1%/ 60|   1.2%/ 58|   1.2%/ 58|   1.2%/ 57 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 168   |    4472|     382.621|   0.5%/139|   0.5%/141|   0.5%/142|   0.5%/143 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 168   |     930|     234.923|   0.9%/ 80|   0.8%/ 91|   0.7%/ 94|   0.7%/ 97 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 168   |     522|     123.658|   0.8%/ 85|   0.7%/ 93|   0.7%/ 95|   0.7%/ 97 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 168   |    7877|     615.309|   0.2%/447|   0.1%/487|   0.1%/498|   0.1%/510 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 168   |     553|     173.182|   1.6%/ 45|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 168   |    1075|    1014.772|   0.2%/373|   0.2%/359|   0.2%/355|   0.2%/351 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 168   |    3149|     611.553|   0.8%/ 82|   0.7%/ 93|   0.7%/ 96|   0.7%/100 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 168   |     183|     207.016|   0.7%/100|   0.7%/ 95|   0.7%/ 94|   0.7%/ 93 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 168   |    2134|     312.326|   1.3%/ 54|   1.2%/ 57|   1.2%/ 58|   1.2%/ 58 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 168   |   14902|     513.940|   0.8%/ 84|   0.7%/103|   0.6%/110|   0.6%/117 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 168   |  196525|     596.353|   0.4%/171|   0.4%/186|   0.4%/190|   0.4%/194 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 168   |     442|     137.981|   0.4%/164|   0.3%/209|   0.3%/224|   0.3%/241 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 168   |      58|      92.950|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 168   |    2790|     326.911|   0.4%/156|   0.4%/168|   0.4%/171|   0.4%/175 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 168   |    2022|     265.541|   0.3%/238|   0.2%/290|   0.2%/306|   0.2%/323 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 168   |     289|     161.002|   1.7%/ 41|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 168   |    1223|     209.988|   0.5%/134|   0.5%/138|   0.5%/139|   0.5%/140 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 156   |      44|      75.979|   0.1%/885|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 168   |    1429|      44.334|   0.1%/832|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 168   |     350|     123.121|   1.2%/ 58|   1.1%/ 66|   1.0%/ 68|   1.0%/ 71 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 168   |    1636|      38.056|   0.5%/134|   0.5%/142|   0.5%/144|   0.5%/146 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 168   |     138|       4.424|   1.5%/ 45|   1.5%/ 45|   1.5%/ 46|   1.5%/ 46 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 168   |   12278|     273.215|   2.0%/ 34|   1.8%/ 38|   1.8%/ 39|   1.7%/ 40 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 168   |     925|     312.882|   0.3%/220|   0.3%/247|   0.3%/255|   0.3%/263 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 168   |     969|      37.735|   1.2%/ 56|   0.8%/ 90|   0.6%/107|   0.5%/130 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 168   |     753|      84.581|   0.2%/443|   0.2%/373|   0.2%/357|   0.2%/343 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 168   |     567|      56.274|   0.4%/177|   0.4%/176|   0.4%/176|   0.4%/176 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 168   |     213|     137.741|   0.8%/ 92|   0.8%/ 89|   0.8%/ 88|   0.8%/ 87 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 168   |    4848|      28.778|   0.8%/ 88|   0.7%/ 96|   0.7%/ 98|   0.7%/100 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 168   |     760|      80.791|   0.8%/ 91|   0.8%/ 90|   0.8%/ 90|   0.8%/ 90 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 168   |    9923|     861.001|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 163   |      40|       3.432|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 168   |    7520|     655.624|   0.9%/ 74|   0.8%/ 88|   0.7%/ 92|   0.7%/ 97 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 168   |     731|     221.461|   1.1%/ 65|   0.9%/ 74|   0.9%/ 77|   0.9%/ 80 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 168   |      12|       5.203|   5.7%/ 12|   5.8%/ 12|   5.8%/ 12|   5.7%/ 12 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 168   |  134185|     634.712|   0.6%/119|   0.5%/133|   0.5%/137|   0.5%/141 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 168   |     754|     108.416|   1.1%/ 64|   1.0%/ 72|   0.9%/ 74|   0.9%/ 77 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 168   |      56|       2.684|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 156   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 168   |     417|      15.726|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 168   |    9240|     243.166|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 116   |      62|      11.321|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 141   |      80|       4.940|   0.1%/540|   0.2%/395|   0.2%/368|   0.2%/344 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 168   |   12078|     632.115|   0.4%/155|   0.4%/161|   0.4%/162|   0.4%/164 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 168   |    4743|       3.383|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 168   |   24013|     486.142|   1.2%/ 60|   1.0%/ 71|   0.9%/ 74|   0.9%/ 78 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 168   |     629|     124.428|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 168   |     221|      54.263|   1.5%/ 47|   1.7%/ 42|   1.7%/ 41|   1.7%/ 39 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 168   |     109|       9.690|   0.8%/ 83|   0.9%/ 74|   1.0%/ 72|   1.0%/ 71 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 168   |     631|     108.387|   0.1%/787|   0.1%/682|   0.1%/660|   0.1%/639 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 168   |    2029|     195.925|   1.0%/ 69|   0.9%/ 74|   0.9%/ 75|   0.9%/ 76 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 168   |    7060|     404.177|   0.5%/153|   0.4%/158|   0.4%/160|   0.4%/161 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 168   |    5688|      56.726|   0.3%/218|   0.3%/222|   0.3%/223|   0.3%/225 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 168   |     810|     124.944|   0.6%/109|   0.5%/138|   0.5%/148|   0.4%/159 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 147   |      83|      61.107|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 164   |    1088|      11.030|   1.6%/ 43|   1.3%/ 54|   1.2%/ 58|   1.1%/ 62 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 168   |     338|      61.067|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 168   |   30933|     461.170|   0.1%/922|   0.1%/836|   0.1%/817|   0.1%/798 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 168   |      53|      24.473|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 168   |     114|      48.406|   0.0%/ --|   1.0%/ 70|   1.0%/ 70|   1.0%/ 71 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 165   |      19|       5.229|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 168   |    9367|     112.648|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 168   |     296|       9.785|   0.4%/194|   0.2%/316|   0.2%/370|   0.2%/444 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 168   |     313|      29.204|   1.1%/ 64|   1.1%/ 63|   1.1%/ 63|   1.1%/ 62 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 168   |    3033|     182.649|   0.5%/133|   0.4%/169|   0.4%/181|   0.4%/196 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 154   |      65|       5.314|   0.4%/163|   0.3%/273|   0.2%/330|   0.2%/419 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 143   |      40|      24.845|   0.4%/173|   0.4%/168|   0.4%/167|   0.4%/167 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 164   |     221|      19.063|   0.5%/140|   0.5%/136|   0.5%/135|   0.5%/134 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 168   |    2164|     236.264|   0.8%/ 89|   0.7%/105|   0.6%/110|   0.6%/117 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 168   |     635|      64.925|   0.3%/253|   0.3%/214|   0.3%/206|   0.4%/198 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 168   |   82315|      60.471|   1.5%/ 48|   1.4%/ 50|   1.4%/ 51|   1.4%/ 51 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 168   |    8987|      33.669|   1.3%/ 55|   1.3%/ 55|   1.3%/ 55|   1.3%/ 55 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 168   |   23470|     281.490|   0.5%/129|   0.5%/135|   0.5%/137|   0.5%/138 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 168   |    8248|     210.785|   1.0%/ 70|   0.9%/ 75|   0.9%/ 76|   0.9%/ 78 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 168   |    1782|     362.154|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 168   |    1169|     127.185|   1.4%/ 51|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 168   |   35627|     591.432|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 168   |      46|      16.971|   4.9%/ 14|   5.6%/ 12|   5.8%/ 12|   6.0%/ 11 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 168   |    1486|      11.798|   0.8%/ 83|   0.8%/ 89|   0.8%/ 91|   0.7%/ 93 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 168   |      19|       1.750|   4.1%/ 17|   4.7%/ 15|   4.9%/ 14|   5.1%/ 14 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 168   |    1697|      90.837|   0.4%/161|   0.3%/227|   0.3%/253|   0.2%/286 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 168   |     640|      13.460|   0.5%/128|   0.4%/180|   0.3%/198|   0.3%/221 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 168   |     512|     285.010|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 165   |     565|     127.863|   0.4%/165|   0.4%/164|   0.4%/163|   0.4%/163 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 166   |    1014|     155.153|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 166   |      35|      18.608|   0.2%/431|   0.1%/634|   0.1%/727|   0.1%/855 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 168   |     257|      37.724|   3.0%/ 23|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 165   |      82|      18.327|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 167   |     383|      55.731|   2.8%/ 25|   2.7%/ 25|   2.7%/ 26|   2.7%/ 26 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 168   |      87|      31.275|   0.1%/554|   0.1%/752|   0.1%/824|   0.1%/908 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 122   |     215|       8.207|   0.7%/ 94|   0.7%/105|   0.6%/108|   0.6%/111 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 168   |     129|       3.929|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 168   |     128|       6.322|   0.1%/626|   0.1%/559|   0.1%/545|   0.1%/533 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 168   |     161|      39.569|   0.1%/808|   0.1%/807|   0.1%/809|   0.1%/813 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 168   |   72323|     571.370|   0.7%/103|   0.6%/112|   0.6%/115|   0.6%/118 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 168   |    1146|     427.226|   0.8%/ 84|   0.8%/ 85|   0.8%/ 85|   0.8%/ 85 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 168   |    1851|      51.591|   2.4%/ 29|   2.1%/ 33|   2.0%/ 34|   1.9%/ 36 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 114   |      36|       1.187|   3.2%/ 22|   3.6%/ 19|   3.8%/ 18|   3.9%/ 18 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  68   |     105|      42.658|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36|   2.0%/ 35 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 123   |     384|      12.797|   3.3%/ 21|   2.6%/ 26|   2.5%/ 28|   2.3%/ 30 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 168   |    6304|     361.118|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 168   |      22|       4.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 168   |     147|      22.678|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 168   |      69|       3.092|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 168   |    1090|       5.290|   0.4%/188|   0.4%/187|   0.4%/187|   0.4%/187 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 168   |     658|     316.792|   0.6%/107|   0.6%/107|   0.6%/106|   0.7%/106 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 168   |     265|      49.408|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 168   |     798|     171.039|   1.1%/ 65|   1.0%/ 66|   1.0%/ 66|   1.0%/ 67 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 168   |    6408|      29.216|   0.1%/748|   0.1%/877|   0.1%/917|   0.1%/960 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 168   |    2209|     523.606|   0.6%/122|   0.5%/140|   0.5%/145|   0.5%/151 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  51   |       6|       0.684|   0.8%/ 90|   4.7%/ 15|   5.7%/ 12|   6.8%/ 10 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 168   |     634|      88.700|   3.6%/ 19|   3.0%/ 23|   2.8%/ 25|   2.6%/ 26 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 168   |   31217|     971.551|   0.4%/154|   0.4%/175|   0.4%/182|   0.4%/188 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 168   |    4552|      41.946|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 168   |    2222|      57.909|   0.5%/132|   0.5%/135|   0.5%/136|   0.5%/137 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 168   |    1870|     181.971|   0.2%/358|   0.2%/341|   0.2%/337|   0.2%/333 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 168   |     208|      75.554|   0.3%/238|   0.3%/233|   0.3%/232|   0.3%/231 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 168   |    4306|     221.916|   1.0%/ 67|   0.9%/ 73|   0.9%/ 75|   0.9%/ 77 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 168   |   18744|     127.731|   0.6%/120|   0.6%/122|   0.6%/123|   0.6%/124 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 109   |      23|       1.877|   3.4%/ 20|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 168   |    4364|     127.548|   0.7%/ 99|   0.6%/107|   0.6%/110|   0.6%/112 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 168   |     303|      18.680|   0.3%/207|   0.2%/315|   0.2%/361|   0.2%/422 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 168   |     740|     106.260|   0.2%/394|   0.1%/584|   0.1%/660|   0.1%/758 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 146   |      72|       9.167|   0.2%/434|   0.1%/477|   0.1%/493|   0.1%/512 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 168   |      27|       4.734|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 168   |      39|       7.064|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 168   |     136|      64.994|   0.1%/958|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 161   |      99|       6.208|   0.1%/668|   0.1%/870|   0.1%/944|   0.1%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 168   |   15998|     272.193|   0.6%/113|   0.5%/153|   0.4%/168|   0.4%/186 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 168   |   29863|     634.025|   0.2%/384|   0.2%/346|   0.2%/338|   0.2%/330 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 168   |      12|       0.567|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 168   |     839|      19.781|   0.1%/833|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 168   |    5852|     566.039|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 168   |    2025|     235.324|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 168   |     170|       9.709|   2.3%/ 30|   2.1%/ 33|   2.1%/ 34|   2.0%/ 34 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 168   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 168   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 168   |      38|       5.031|   1.9%/ 36|   2.3%/ 29|   2.5%/ 28|   2.6%/ 27 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 168   |      59|      43.245|   6.5%/ 11|   6.6%/ 10|   6.7%/ 10|   6.7%/ 10 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 168   |     112|       9.514|   2.7%/ 25|   3.1%/ 22|   3.2%/ 22|   3.3%/ 21 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 168   |    7080|      85.136|   0.8%/ 87|   0.9%/ 79|   0.9%/ 77|   0.9%/ 75 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 168   |  196525|     596.353|   0.4%/171|   0.4%/186|   0.4%/190|   0.4%/194 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  54   |      58|       1.444|   4.8%/ 14|   3.9%/ 18|   3.8%/ 18|   3.7%/ 19 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 168   |    3329|      79.501|   1.6%/ 42|   1.7%/ 42|   1.7%/ 41|   1.7%/ 41 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 168   |     402|      40.610|   0.3%/236|   0.3%/248|   0.3%/251|   0.3%/254 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 168   |   41738|     628.254|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 168   |      46|      13.137|   0.1%/485|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 168   |     408|      11.949|   1.6%/ 43|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 168   |     507|      15.742|   1.8%/ 39|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  47   |      35|       0.364|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 167   |     315|      17.595|   0.6%/107|   0.7%/104|   0.7%/103|   0.7%/101 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 168   |     243|      16.027|   0.5%/137|   0.1%/497|   0.0%/ ***|   0.0%/ -- |

