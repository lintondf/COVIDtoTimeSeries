# State and Country COVID-19 Analysis #
## Updated: at 2020-07-31 for data as of 2020-07-30 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 36.0% of deaths and 40.0% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 69.0% of deaths and 56.2% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 121   |   32698|    1680.798|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 121   |   15861|    1785.726|   0.1%/818|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 121   |    8953|     226.576|   1.4%/ 51|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 121   |    8588|    1235.734|   0.2%/402|   0.2%/427|   0.2%/433|   0.2%/438 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 121   |    7673|     605.531|   0.2%/326|   0.2%/353|   0.2%/359|   0.2%/364 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 121   |    7198|     562.232|   0.2%/321|   0.2%/357|   0.2%/367|   0.2%/378 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 121   |    6452|     300.388|   2.4%/ 28|   2.5%/ 27|   2.6%/ 27|   2.6%/ 27 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 121   |    6439|     644.719|   0.1%/672|   0.1%/806|   0.1%/845|   0.1%/887 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 121   |    5768|     198.934|   4.1%/ 17|   4.7%/ 15|   4.8%/ 14|   4.9%/ 14 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 121   |    4434|    1243.566|   0.1%/902|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 121   |  151004|     458.220|   0.7%/103|   0.7%/ 95|   0.7%/ 93|   0.8%/ 91 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 121   |   91665|     433.585|   1.3%/ 55|   1.2%/ 59|   1.2%/ 60|   1.1%/ 61 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 121   |   46115|     694.127|   0.1%/486|   0.1%/520|   0.1%/528|   0.1%/537 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 121   |   46390|     366.491|   1.5%/ 47|   1.4%/ 50|   1.3%/ 51|   1.3%/ 52 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 121   |   35897|      26.371|   2.4%/ 29|   2.3%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 121   |   35150|     583.518|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 121   |   30260|     451.125|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 121   |   28442|     603.863|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 121   |   19583|     609.454|   1.2%/ 55|   1.1%/ 61|   1.1%/ 63|   1.1%/ 65 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 121   |   16622|     199.357|   1.4%/ 49|   1.4%/ 49|   1.4%/ 50|   1.4%/ 50 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 121   |    1573|     320.829|   1.7%/ 40|   1.7%/ 42|   1.6%/ 42|   1.6%/ 43 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 121   |      22|      29.523|   2.1%/ 32|   2.8%/ 24|   3.0%/ 23|   3.2%/ 21 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 121   |    3661|     503.000|   2.6%/ 27|   2.4%/ 29|   2.3%/ 30|   2.2%/ 31 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 121   |     436|     144.479|   1.9%/ 37|   2.0%/ 34|   2.1%/ 33|   2.1%/ 33 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 121   |    8953|     226.576|   1.4%/ 51|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 121   |    1819|     315.804|   0.3%/216|   0.4%/198|   0.4%/193|   0.4%/189 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 121   |    4434|    1243.566|   0.1%/902|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 121   |     581|     596.914|   0.1%/477|   0.1%/503|   0.1%/513|   0.1%/523 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 121   |    6452|     300.388|   2.4%/ 28|   2.5%/ 27|   2.6%/ 27|   2.6%/ 27 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 121   |    3643|     343.105|   1.2%/ 58|   1.3%/ 52|   1.4%/ 50|   1.4%/ 49 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 121   |      27|      19.194|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 121   |     163|      91.339|   3.5%/ 20|   4.2%/ 16|   4.4%/ 16|   4.6%/ 15 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 121   |    7673|     605.531|   0.2%/326|   0.2%/353|   0.2%/359|   0.2%/364 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 121   |    2943|     437.209|   0.4%/190|   0.4%/184|   0.4%/183|   0.4%/181 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 121   |     858|     272.020|   0.7%/ 96|   0.7%/ 93|   0.7%/ 93|   0.8%/ 92 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 121   |     344|     117.935|   1.1%/ 65|   1.3%/ 55|   1.3%/ 53|   1.4%/ 51 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 121   |     728|     162.941|   0.9%/ 80|   0.9%/ 78|   0.9%/ 78|   0.9%/ 77 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 121   |    3874|     833.367|   0.8%/ 82|   1.0%/ 71|   1.0%/ 68|   1.0%/ 66 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 121   |     122|      90.471|   0.4%/163|   0.4%/171|   0.4%/173|   0.4%/174 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 121   |    3481|     575.703|   0.3%/246|   0.3%/240|   0.3%/238|   0.3%/237 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 121   |    8588|    1235.734|   0.2%/402|   0.2%/427|   0.2%/433|   0.2%/438 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 121   |    6439|     644.719|   0.1%/672|   0.1%/806|   0.1%/845|   0.1%/887 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 121   |    1635|     289.876|   0.3%/224|   0.3%/234|   0.3%/238|   0.3%/241 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 121   |    1581|     531.150|   1.4%/ 48|   1.5%/ 46|   1.5%/ 45|   1.5%/ 45 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 121   |    1244|     202.728|   0.8%/ 87|   0.9%/ 79|   0.9%/ 77|   0.9%/ 75 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 121   |      54|      50.659|   3.6%/ 19|   4.1%/ 17|   4.2%/ 16|   4.4%/ 16 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 121   |     327|     169.185|   0.7%/100|   0.7%/ 97|   0.7%/ 97|   0.7%/ 97 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 121   |     788|     255.746|   1.6%/ 42|   1.7%/ 40|   1.8%/ 39|   1.8%/ 39 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 121   |     413|     303.965|   0.3%/220|   0.3%/218|   0.3%/217|   0.3%/217 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 121   |   15861|    1785.726|   0.1%/818|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 121   |     634|     302.557|   0.9%/ 76|   1.0%/ 72|   1.0%/ 71|   1.0%/ 70 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 121   |   32698|    1680.798|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 121   |    1913|     182.434|   1.3%/ 54|   1.3%/ 53|   1.3%/ 52|   1.3%/ 52 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 121   |     103|     134.995|   1.0%/ 72|   1.0%/ 70|   1.0%/ 70|   1.0%/ 70 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 121   |    3417|     292.297|   0.7%/ 95|   0.8%/ 86|   0.8%/ 83|   0.9%/ 81 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 121   |     520|     131.513|   1.4%/ 51|   1.6%/ 44|   1.6%/ 43|   1.6%/ 42 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 121   |     308|      73.096|   1.7%/ 40|   1.9%/ 35|   2.0%/ 34|   2.1%/ 33 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 121   |    7198|     562.232|   0.2%/321|   0.2%/357|   0.2%/367|   0.2%/378 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 121   |     211|      66.036|   1.6%/ 44|   1.8%/ 38|   1.9%/ 37|   1.9%/ 36 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 121   |    1010|     953.150|   0.1%/479|   0.1%/603|   0.1%/644|   0.1%/692 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 121   |    1654|     321.315|   3.2%/ 22|   3.4%/ 20|   3.5%/ 20|   3.5%/ 19 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 121   |     129|     145.500|   0.9%/ 76|   0.8%/ 88|   0.8%/ 91|   0.7%/ 95 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 121   |    1040|     152.182|   1.8%/ 37|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 121   |    5768|     198.934|   4.1%/ 17|   4.7%/ 15|   4.8%/ 14|   4.9%/ 14 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 121   |  151004|     458.220|   0.7%/103|   0.7%/ 95|   0.7%/ 93|   0.8%/ 91 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 121   |     299|      93.137|   1.8%/ 39|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 121   |      56|      89.855|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 121   |    2126|     249.044|   0.4%/155|   0.4%/164|   0.4%/166|   0.4%/167 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 121   |    1544|     202.779|   0.7%/101|   0.7%/ 93|   0.8%/ 91|   0.8%/ 88 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 121   |     108|      60.111|   0.9%/ 77|   1.2%/ 60|   1.2%/ 57|   1.3%/ 54 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 121   |     913|     156.808|   0.7%/101|   0.8%/ 88|   0.8%/ 86|   0.8%/ 83 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 109   |      26|      45.673|   0.8%/ 86|   0.7%/ 94|   0.7%/ 97|   0.7%/ 99 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 121   |    1325|      41.129|   1.1%/ 65|   0.6%/108|   0.5%/129|   0.4%/162 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 121   |     154|      54.141|   3.0%/ 23|   3.1%/ 23|   3.1%/ 22|   3.1%/ 22 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 121   |    1198|      27.860|   0.9%/ 73|   1.0%/ 72|   1.0%/ 72|   1.0%/ 71 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 121   |      46|       1.491|   5.3%/ 13|   6.4%/ 11|   6.3%/ 11|   7.5%/  9 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 121   |    3388|      75.391|   3.5%/ 20|   3.7%/ 19|   3.7%/ 18|   3.8%/ 18 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 121   |     750|     253.487|   1.3%/ 53|   1.0%/ 67|   1.0%/ 73|   0.9%/ 79 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 121   |     177|       6.902|   3.9%/ 18|   4.9%/ 14|   5.2%/ 13|   5.5%/ 12 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 121   |     715|      80.295|   0.1%/970|   0.1%/816|   0.1%/781|   0.1%/746 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 121   |     452|      44.910|   2.0%/ 34|   1.8%/ 38|   1.8%/ 39|   1.7%/ 40 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 121   |     149|      96.466|   1.5%/ 48|   1.2%/ 56|   1.2%/ 58|   1.1%/ 61 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 121   |    3104|      18.425|   1.5%/ 46|   1.4%/ 49|   1.4%/ 50|   1.4%/ 51 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 121   |     555|      59.022|   1.0%/ 72|   0.9%/ 78|   0.9%/ 80|   0.9%/ 81 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 121   |    9835|     853.399|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 116   |      38|       3.219|   3.1%/ 22|   1.0%/ 71|   0.9%/ 73|   0.9%/ 73 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 121   |    2885|     251.565|   2.7%/ 26|   2.6%/ 27|   2.5%/ 27|   2.5%/ 27 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 121   |     309|      93.685|   1.9%/ 37|   2.0%/ 35|   2.0%/ 35|   2.0%/ 35 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 121   |       1|       0.428|   6.9%/ 10|  11.1%/  6|  12.2%/  6|  13.4%/  5 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 121   |   91665|     433.585|   1.3%/ 55|   1.2%/ 59|   1.2%/ 60|   1.1%/ 61 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 121   |     368|      52.967|   1.8%/ 38|   1.9%/ 36|   2.0%/ 35|   2.0%/ 34 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 121   |      53|       2.540|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 109   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 121   |     395|      14.895|   0.5%/152|   0.4%/154|   0.4%/156|   0.4%/158 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 121   |    8974|     236.170|   0.1%/816|   0.1%/937|   0.1%/970|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  69   |      60|      10.918|   0.9%/ 80|   0.3%/206|   0.2%/384|   0.0%/ *** |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  94   |      75|       4.618|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 121   |    9760|     510.824|   0.9%/ 74|   0.8%/ 85|   0.8%/ 88|   0.8%/ 91 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 121   |    4653|       3.318|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 121   |    9701|     196.395|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 121   |     145|      28.702|   8.4%/  8|   9.0%/  8|   9.1%/  7|   9.2%/  7 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 121   |     140|      34.384|   1.3%/ 54|   1.6%/ 44|   1.7%/ 42|   1.7%/ 40 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 121   |      87|       7.772|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 121   |     614|     105.459|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 121   |    1131|     109.160|   1.5%/ 47|   1.5%/ 46|   1.5%/ 45|   1.5%/ 45 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 121   |    5673|     324.744|   0.6%/114|   0.6%/125|   0.5%/128|   0.5%/131 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 121   |    4856|      48.426|   1.1%/ 64|   0.8%/ 84|   0.8%/ 92|   0.7%/100 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 121   |     449|      69.191|   2.8%/ 25|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 100   |      51|      37.548|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 117   |     258|       2.611|   4.1%/ 17|   4.5%/ 15|   4.6%/ 15|   4.6%/ 15 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 121   |     329|      59.475|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 121   |   30260|     451.125|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 121   |      49|      22.607|   0.4%/176|   0.5%/148|   0.5%/142|   0.5%/137 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 121   |       8|       3.404|   6.8%/ 10|   8.2%/  8|   8.5%/  8|   8.8%/  8 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 118   |      17|       4.454|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 121   |    9140|     109.924|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 121   |     174|       5.749|   1.5%/ 47|   1.6%/ 44|   1.6%/ 43|   1.6%/ 43 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 121   |     204|      18.985|   0.3%/261|   0.3%/219|   0.3%/211|   0.3%/205 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 121   |    1911|     115.094|   2.2%/ 31|   1.9%/ 37|   1.8%/ 39|   1.7%/ 41 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 107   |      46|       3.760|   1.4%/ 49|   1.6%/ 43|   1.7%/ 42|   1.7%/ 40 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  96   |      26|      16.206|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 117   |     163|      14.101|   0.8%/ 89|   0.4%/155|   0.4%/188|   0.3%/237 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 121   |    1268|     138.476|   3.1%/ 22|   3.4%/ 20|   3.5%/ 20|   3.6%/ 19 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 121   |     597|      61.069|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 121   |   35897|      26.371|   2.4%/ 29|   2.3%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 121   |    5137|      19.248|   1.8%/ 38|   1.7%/ 40|   1.7%/ 40|   1.7%/ 41 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 121   |   16622|     199.357|   1.4%/ 49|   1.4%/ 49|   1.4%/ 50|   1.4%/ 50 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 121   |    4793|     122.497|   2.1%/ 33|   1.7%/ 40|   1.7%/ 42|   1.6%/ 44 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 121   |    1767|     358.952|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 121   |     500|      54.417|   1.9%/ 37|   2.0%/ 34|   2.0%/ 34|   2.1%/ 34 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 121   |   35150|     583.518|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 121   |      10|       3.667|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 121   |    1002|       7.952|   0.1%/488|   0.2%/387|   0.2%/367|   0.2%/349 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 121   |      11|       1.056|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 121   |     801|      42.856|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 121   |     320|       6.723|   2.9%/ 23|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 121   |     207|     115.545|   4.2%/ 16|   4.2%/ 17|   4.1%/ 17|   4.1%/ 17 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 118   |     446|     100.805|   0.8%/ 87|   0.8%/ 82|   0.9%/ 81|   0.9%/ 80 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 119   |     329|      50.388|   3.3%/ 21|   2.3%/ 29|   2.1%/ 33|   1.9%/ 37 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 119   |      31|      16.342|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 121   |      48|       6.976|   2.7%/ 26|   3.4%/ 20|   3.6%/ 19|   3.8%/ 18 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 118   |      79|      17.634|   0.6%/124|   0.1%/ ***|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 120   |      71|      10.312|   3.9%/ 18|   4.5%/ 15|   4.7%/ 15|   4.9%/ 14 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 121   |      80|      28.729|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  75   |     104|       3.974|   5.4%/ 13|   5.4%/ 13|   5.5%/ 13|   5.5%/ 12 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 121   |     124|       3.790|   0.1%/630|   0.1%/604|   0.1%/597|   0.1%/591 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 121   |     124|       6.128|   0.2%/404|   0.2%/381|   0.2%/374|   0.2%/367 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 121   |     159|      39.056|   0.3%/254|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 121   |   46390|     366.491|   1.5%/ 47|   1.4%/ 50|   1.3%/ 51|   1.3%/ 52 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 121   |     770|     287.009|   1.0%/ 69|   1.0%/ 72|   1.0%/ 72|   1.0%/ 73 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 121   |     325|       9.047|   1.9%/ 36|   2.3%/ 30|   2.4%/ 29|   2.5%/ 28 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  67   |      11|       0.369|   1.3%/ 53|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  21   |      10|       4.067|  10.3%/  7|   4.4%/ 16|   5.2%/ 13|   7.2%/  9 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  76   |      51|       1.684|   2.0%/ 35|   2.7%/ 25|   2.9%/ 24|   3.1%/ 22 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 121   |    6163|     353.034|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 121   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 121   |     116|      17.951|   1.3%/ 51|   1.4%/ 48|   1.5%/ 47|   1.5%/ 46 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 121   |      69|       3.102|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 121   |     892|       4.328|   1.0%/ 71|   0.8%/ 86|   0.8%/ 91|   0.7%/ 96 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 121   |     487|     234.368|   1.3%/ 55|   1.1%/ 60|   1.1%/ 62|   1.1%/ 64 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 121   |     256|      47.647|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 121   |     427|      91.609|   2.7%/ 25|   2.6%/ 27|   2.6%/ 27|   2.5%/ 27 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 121   |    6006|      27.383|   0.6%/119|   0.4%/189|   0.3%/221|   0.3%/266 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 121   |    1428|     338.589|   2.3%/ 29|   2.2%/ 32|   2.1%/ 33|   2.1%/ 34 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 121   |      48|       6.758|   3.7%/ 18|   4.0%/ 17|   4.1%/ 17|   4.1%/ 17 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 121   |   19583|     609.454|   1.2%/ 55|   1.1%/ 61|   1.1%/ 63|   1.1%/ 65 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 121   |    2028|      18.685|   0.8%/ 83|   0.7%/ 92|   0.7%/ 95|   0.7%/ 99 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 121   |    1702|      44.340|   0.4%/157|   0.4%/160|   0.4%/160|   0.4%/161 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 121   |    1733|     168.639|   0.2%/325|   0.2%/405|   0.2%/431|   0.2%/461 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 121   |     172|      62.505|   0.8%/ 90|   0.6%/120|   0.5%/130|   0.5%/142 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 121   |    2288|     117.905|   1.1%/ 62|   1.1%/ 61|   1.1%/ 60|   1.2%/ 60 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 121   |   13874|      94.544|   1.1%/ 65|   0.9%/ 74|   0.9%/ 76|   0.9%/ 78 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  62   |       5|       0.404|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 121   |    2893|      84.544|   1.3%/ 52|   1.1%/ 62|   1.1%/ 65|   1.0%/ 69 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 121   |     204|      12.577|   1.9%/ 37|   1.9%/ 36|   1.9%/ 35|   2.0%/ 35 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 121   |     583|      83.718|   1.9%/ 37|   1.5%/ 46|   1.4%/ 49|   1.3%/ 53 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  99   |      67|       8.474|   0.3%/264|   0.2%/352|   0.2%/388|   0.2%/431 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 121   |      27|       4.770|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 121   |      28|       5.132|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 121   |     117|      55.953|   0.2%/287|   0.3%/218|   0.3%/206|   0.4%/195 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 114   |      93|       5.858|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 121   |    7800|     132.707|   3.6%/ 19|   3.7%/ 19|   3.7%/ 19|   3.7%/ 19 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 121   |   28442|     603.863|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 121   |      11|       0.505|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 121   |     736|      17.341|   0.6%/122|   0.5%/148|   0.4%/157|   0.4%/167 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 121   |    5748|     555.956|   0.2%/381|   0.2%/454|   0.1%/478|   0.1%/506 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 121   |    1979|     230.061|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 121   |      46|       2.622|   4.1%/ 17|   3.6%/ 19|   1.7%/ 40|   0.8%/ 84 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 121   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 121   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 121   |      18|       2.375|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 121   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 121   |      50|       4.265|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 121   |    5685|      68.366|   0.3%/225|   0.3%/242|   0.3%/246|   0.3%/251 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 121   |  151004|     458.220|   0.7%/103|   0.7%/ 95|   0.7%/ 93|   0.8%/ 91 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 121   |    1695|      40.466|   1.1%/ 66|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 121   |     349|      35.241|   0.3%/263|   0.2%/287|   0.2%/292|   0.2%/297 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 121   |   46115|     694.127|   0.1%/486|   0.1%/520|   0.1%/528|   0.1%/537 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 121   |      36|      10.131|   0.7%/ 93|   0.6%/116|   0.6%/124|   0.5%/133 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 121   |     141|       4.120|   4.4%/ 16|   3.7%/ 19|   3.5%/ 19|   3.4%/ 20 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 121   |     162|       5.025|   3.2%/ 21|   3.0%/ 23|   2.9%/ 24|   2.8%/ 24 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 120   |     185|      10.316|   6.1%/ 11|   3.9%/ 18|   3.2%/ 21|   2.5%/ 27 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 121   |      43|       2.808|   6.2%/ 11|   5.6%/ 12|   5.5%/ 12|   5.4%/ 13 |

