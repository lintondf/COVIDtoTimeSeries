# State and Country COVID-19 Analysis #
## Updated: at 2020-09-09 for data as of 2020-09-08 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.3% of deaths and 39.5% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.8% of deaths and 57.2% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 161   |   33015|    1697.120|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 161   |   15986|    1799.766|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 161   |   14107|     357.018|   0.8%/ 87|   0.7%/ 99|   0.7%/103|   0.6%/107 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 161   |   14226|     490.613|   1.1%/ 66|   0.9%/ 80|   0.8%/ 85|   0.8%/ 91 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 161   |   12324|     573.802|   0.8%/ 82|   0.6%/109|   0.6%/118|   0.5%/130 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 161   |    9159|    1317.978|   0.1%/486|   0.1%/514|   0.1%/522|   0.1%/531 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 161   |    8422|     664.611|   0.2%/283|   0.2%/281|   0.2%/281|   0.2%/281 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 161   |    7794|     608.835|   0.2%/391|   0.2%/421|   0.2%/429|   0.2%/437 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 161   |    6832|     684.110|   0.1%/490|   0.1%/512|   0.1%/519|   0.1%/526 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 161   |    6216|     585.425|   1.1%/ 65|   1.0%/ 71|   1.0%/ 72|   0.9%/ 74 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 161   |  191422|     580.870|   0.4%/159|   0.4%/176|   0.4%/181|   0.4%/187 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 161   |  129279|     611.505|   0.7%/106|   0.6%/119|   0.6%/122|   0.5%/126 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 161   |   74565|      54.778|   1.6%/ 44|   1.5%/ 47|   1.5%/ 47|   1.4%/ 48 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 161   |   69122|     546.085|   0.7%/ 94|   0.7%/104|   0.6%/107|   0.6%/110 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 161   |   41096|     618.587|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 161   |   35570|     590.494|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 161   |   30766|     458.675|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 161   |   30872|     960.805|   0.5%/127|   0.5%/142|   0.5%/146|   0.5%/150 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 161   |   29441|     625.067|   0.2%/448|   0.2%/388|   0.2%/376|   0.2%/364 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 161   |   22666|     271.846|   0.5%/128|   0.5%/144|   0.5%/148|   0.5%/152 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 161   |    2320|     473.081|   0.7%/ 94|   0.7%/101|   0.7%/103|   0.7%/105 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 161   |      44|      59.603|   1.6%/ 44|   1.6%/ 42|   1.7%/ 41|   1.7%/ 41 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 161   |    5328|     731.986|   0.6%/123|   0.5%/154|   0.4%/164|   0.4%/175 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 161   |     928|     307.441|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 161   |   14107|     357.018|   0.8%/ 87|   0.7%/ 99|   0.7%/103|   0.6%/107 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 161   |    1976|     343.087|   0.2%/366|   0.2%/368|   0.2%/368|   0.2%/369 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 161   |    4472|    1254.353|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 161   |     610|     626.730|   0.1%/691|   0.1%/741|   0.1%/756|   0.1%/771 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 161   |   12324|     573.802|   0.8%/ 82|   0.6%/109|   0.6%/118|   0.5%/130 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 161   |    6216|     585.425|   1.1%/ 65|   1.0%/ 71|   1.0%/ 72|   0.9%/ 74 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 161   |      90|      63.486|   3.6%/ 19|   3.8%/ 18|   3.9%/ 18|   3.9%/ 18 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 161   |     410|     229.372|   1.3%/ 55|   1.0%/ 69|   0.9%/ 74|   0.9%/ 79 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 161   |    8422|     664.611|   0.2%/283|   0.2%/281|   0.2%/281|   0.2%/281 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 161   |    3393|     503.985|   0.3%/231|   0.3%/251|   0.3%/257|   0.3%/263 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 161   |    1191|     377.516|   0.8%/ 91|   0.7%/ 95|   0.7%/ 96|   0.7%/ 97 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 161   |     486|     166.837|   0.8%/ 90|   0.8%/ 90|   0.8%/ 90|   0.8%/ 89 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 161   |    1013|     226.750|   0.9%/ 80|   0.8%/ 82|   0.8%/ 82|   0.8%/ 83 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 161   |    5186|    1115.458|   0.5%/141|   0.4%/166|   0.4%/174|   0.4%/183 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 161   |     135|     100.411|   0.2%/348|   0.2%/401|   0.2%/418|   0.2%/438 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 161   |    3816|     631.157|   0.2%/360|   0.2%/376|   0.2%/380|   0.2%/384 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 161   |    9159|    1317.978|   0.1%/486|   0.1%/514|   0.1%/522|   0.1%/531 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 161   |    6832|     684.110|   0.1%/490|   0.1%/512|   0.1%/519|   0.1%/526 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 161   |    1930|     342.221|   0.3%/199|   0.3%/224|   0.3%/231|   0.3%/240 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 161   |    2670|     896.965|   0.8%/ 87|   0.7%/105|   0.6%/111|   0.6%/118 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 161   |    1664|     271.181|   1.0%/ 69|   1.1%/ 62|   1.1%/ 60|   1.2%/ 59 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 161   |     120|     112.513|   1.7%/ 42|   1.7%/ 42|   1.7%/ 42|   1.7%/ 42 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 161   |     412|     212.918|   0.4%/170|   0.3%/206|   0.3%/218|   0.3%/232 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 161   |    1449|     470.509|   0.9%/ 74|   0.7%/ 92|   0.7%/ 98|   0.7%/106 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 161   |     435|     319.807|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 161   |   15986|    1799.766|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 161   |     814|     388.039|   0.5%/136|   0.5%/145|   0.5%/147|   0.5%/150 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 161   |   33015|    1697.120|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 161   |    2941|     280.459|   0.9%/ 76|   0.9%/ 79|   0.9%/ 80|   0.9%/ 81 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 161   |     158|     206.769|   1.0%/ 68|   1.0%/ 71|   1.0%/ 71|   1.0%/ 72 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 161   |    4321|     369.660|   0.5%/150|   0.4%/162|   0.4%/165|   0.4%/169 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 161   |     883|     223.204|   1.0%/ 70|   0.9%/ 80|   0.8%/ 83|   0.8%/ 86 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 161   |     495|     117.441|   0.9%/ 80|   0.8%/ 90|   0.7%/ 93|   0.7%/ 96 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 161   |    7794|     608.835|   0.2%/391|   0.2%/421|   0.2%/429|   0.2%/437 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 161   |     497|     155.721|   1.5%/ 47|   1.3%/ 55|   1.2%/ 57|   1.2%/ 60 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 161   |    1060|    1000.844|   0.1%/499|   0.1%/516|   0.1%/522|   0.1%/529 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 161   |    2988|     580.348|   1.0%/ 72|   0.8%/ 84|   0.8%/ 88|   0.8%/ 92 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 161   |     175|     197.902|   0.5%/134|   0.5%/150|   0.4%/155|   0.4%/160 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 161   |    1967|     287.799|   1.2%/ 60|   1.0%/ 71|   0.9%/ 74|   0.9%/ 78 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 161   |   14226|     490.613|   1.1%/ 66|   0.9%/ 80|   0.8%/ 85|   0.8%/ 91 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 161   |  191422|     580.870|   0.4%/159|   0.4%/176|   0.4%/181|   0.4%/187 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 161   |     431|     134.586|   0.5%/126|   0.4%/157|   0.4%/167|   0.4%/179 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 161   |      58|      92.966|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 161   |    2705|     316.901|   0.5%/128|   0.5%/126|   0.6%/126|   0.6%/125 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 161   |    1990|     261.278|   0.3%/228|   0.2%/337|   0.2%/383|   0.2%/444 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 161   |     258|     144.115|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 161   |    1179|     202.469|   0.5%/135|   0.5%/141|   0.5%/143|   0.5%/145 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 149   |      43|      74.605|   0.2%/327|   0.1%/492|   0.1%/550|   0.1%/617 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 161   |    1424|      44.176|   0.1%/686|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 161   |     325|     114.165|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 161   |    1581|      36.773|   0.6%/125|   0.5%/136|   0.5%/139|   0.5%/142 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 161   |     123|       3.965|   1.4%/ 49|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 161   |   10695|     237.999|   2.3%/ 29|   2.1%/ 32|   2.1%/ 33|   2.0%/ 34 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 161   |     908|     307.024|   0.4%/187|   0.3%/210|   0.3%/216|   0.3%/223 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 161   |     836|      32.533|   2.2%/ 32|   1.8%/ 39|   1.7%/ 41|   1.6%/ 44 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 161   |     738|      82.891|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 161   |     551|      54.745|   0.4%/172|   0.4%/169|   0.4%/169|   0.4%/168 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 161   |     201|     130.394|   0.6%/108|   0.6%/116|   0.6%/118|   0.6%/119 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 161   |    4603|      27.323|   0.9%/ 79|   0.8%/ 84|   0.8%/ 86|   0.8%/ 88 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 161   |     721|      76.600|   0.7%/ 93|   0.8%/ 91|   0.8%/ 90|   0.8%/ 90 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 161   |    9902|     859.222|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 156   |      40|       3.441|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 161   |    5659|     493.396|   1.3%/ 52|   1.3%/ 55|   1.2%/ 56|   1.2%/ 56 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 161   |     687|     208.008|   1.3%/ 52|   1.2%/ 57|   1.2%/ 59|   1.1%/ 60 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 161   |       8|       3.370|   7.5%/  9|   8.7%/  8|   9.1%/  7|   9.4%/  7 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 161   |  129279|     611.505|   0.7%/106|   0.6%/119|   0.6%/122|   0.5%/126 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 161   |     700|     100.737|   1.3%/ 53|   1.2%/ 55|   1.2%/ 56|   1.2%/ 57 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 161   |      55|       2.655|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 149   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 161   |     417|      15.723|   0.1%/707|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 161   |    9214|     242.475|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 109   |      62|      11.313|   0.1%/659|   0.1%/592|   0.1%/587|   0.1%/586 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 134   |      78|       4.803|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 161   |   11726|     613.703|   0.5%/147|   0.5%/153|   0.4%/155|   0.4%/156 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 161   |    4735|       3.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 161   |   22360|     452.681|   1.4%/ 48|   1.2%/ 55|   1.2%/ 58|   1.2%/ 60 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 161   |     527|     104.146|   2.1%/ 33|   1.9%/ 37|   1.8%/ 38|   1.7%/ 40 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 161   |     200|      49.141|   1.0%/ 67|   1.1%/ 62|   1.1%/ 60|   1.2%/ 59 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 161   |      96|       8.581|   0.7%/ 99|   0.8%/ 83|   0.9%/ 80|   0.9%/ 77 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 161   |     628|     107.773|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 161   |    1890|     182.463|   1.2%/ 60|   1.1%/ 61|   1.1%/ 62|   1.1%/ 62 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 161   |    6819|     390.356|   0.5%/143|   0.5%/144|   0.5%/144|   0.5%/144 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 161   |    5566|      55.512|   0.3%/209|   0.3%/212|   0.3%/213|   0.3%/214 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 161   |     781|     120.398|   0.9%/ 78|   0.8%/ 91|   0.7%/ 95|   0.7%/ 99 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 140   |      83|      61.107|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 157   |     992|      10.051|   2.2%/ 32|   1.9%/ 37|   1.8%/ 39|   1.7%/ 41 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 161   |     337|      60.883|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 161   |   30766|     458.675|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 161   |      53|      24.589|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 161   |     122|      51.891|   0.3%/200|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 158   |      20|       5.239|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 161   |    9342|     112.356|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 161   |     295|       9.732|   0.5%/143|   0.2%/294|   0.2%/400|   0.1%/622 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 161   |     290|      27.039|   1.1%/ 63|   1.2%/ 60|   1.2%/ 59|   1.2%/ 59 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 161   |    2945|     177.351|   0.7%/102|   0.5%/127|   0.5%/135|   0.5%/145 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 147   |      63|       5.167|   0.8%/ 84|   0.8%/ 86|   0.8%/ 86|   0.8%/ 87 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 136   |      37|      23.293|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 157   |     213|      18.397|   0.5%/132|   0.5%/126|   0.6%/124|   0.6%/122 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 161   |    2051|     223.933|   1.2%/ 59|   1.2%/ 57|   1.2%/ 56|   1.2%/ 56 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 161   |     624|      63.818|   0.2%/460|   0.2%/413|   0.2%/402|   0.2%/391 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 161   |   74565|      54.778|   1.6%/ 44|   1.5%/ 47|   1.5%/ 47|   1.4%/ 48 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 161   |    8215|      30.777|   1.3%/ 53|   1.3%/ 52|   1.3%/ 51|   1.4%/ 51 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 161   |   22666|     271.846|   0.5%/128|   0.5%/144|   0.5%/148|   0.5%/152 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 161   |    7723|     197.368|   1.1%/ 63|   1.1%/ 66|   1.0%/ 66|   1.0%/ 67 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 161   |    1778|     361.303|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 161   |    1081|     117.669|   1.4%/ 50|   1.3%/ 53|   1.3%/ 54|   1.3%/ 55 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 161   |   35570|     590.494|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 161   |      25|       9.181|   3.6%/ 19|   4.1%/ 17|   4.2%/ 16|   4.4%/ 16 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 161   |    1401|      11.122|   1.0%/ 70|   1.0%/ 69|   1.0%/ 69|   1.0%/ 69 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 161   |      17|       1.577|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 161   |    1677|      89.734|   0.7%/105|   0.5%/142|   0.4%/156|   0.4%/174 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 161   |     625|      13.135|   0.7%/105|   0.4%/180|   0.3%/220|   0.2%/280 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 161   |     530|     295.023|   0.3%/236|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 158   |     549|     124.153|   0.4%/181|   0.4%/194|   0.4%/197|   0.3%/201 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 159   |     975|     149.261|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 159   |      35|      18.377|   0.4%/184|   0.4%/168|   0.4%/165|   0.4%/161 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 161   |     210|      30.727|   3.0%/ 23|   2.9%/ 24|   2.9%/ 24|   2.8%/ 24 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 158   |      82|      18.373|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 160   |     305|      44.425|   2.7%/ 26|   2.4%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 161   |      87|      31.211|   0.1%/465|   0.1%/624|   0.1%/694|   0.1%/787 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 115   |     205|       7.809|   0.8%/ 84|   0.8%/ 85|   0.8%/ 86|   0.8%/ 87 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 161   |     128|       3.905|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 161   |     127|       6.252|   0.1%/722|   0.1%/595|   0.1%/570|   0.1%/545 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 161   |     160|      39.259|   0.1%/783|   0.1%/704|   0.1%/688|   0.1%/673 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 161   |   69122|     546.085|   0.7%/ 94|   0.7%/104|   0.6%/107|   0.6%/110 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 161   |    1077|     401.720|   0.9%/ 79|   0.9%/ 76|   0.9%/ 75|   0.9%/ 74 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 161   |    1536|      42.806|   3.1%/ 23|   2.8%/ 24|   2.8%/ 25|   2.7%/ 26 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 107   |      28|       0.922|   2.1%/ 33|   2.4%/ 28|   2.5%/ 27|   2.6%/ 27 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  61   |      94|      38.322|   4.1%/ 17|   2.0%/ 35|   1.4%/ 48|   0.9%/ 78 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 116   |     325|      10.821|   4.5%/ 15|   4.0%/ 17|   3.9%/ 18|   3.8%/ 18 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 161   |    6285|     360.043|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 161   |      22|       4.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 161   |     144|      22.224|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 161   |      69|       3.092|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 161   |    1060|       5.141|   0.4%/171|   0.4%/165|   0.4%/163|   0.4%/161 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 161   |     628|     302.535|   0.6%/109|   0.6%/108|   0.6%/108|   0.6%/108 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 161   |     265|      49.430|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 161   |     743|     159.306|   1.1%/ 63|   1.1%/ 65|   1.0%/ 66|   1.0%/ 67 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 161   |    6371|      29.049|   0.1%/609|   0.1%/711|   0.1%/741|   0.1%/773 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 161   |    2134|     505.946|   0.7%/103|   0.6%/119|   0.6%/124|   0.5%/129 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  44   |       5|       0.560|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 161   |     508|      71.080|   5.2%/ 13|   4.9%/ 14|   4.8%/ 14|   4.7%/ 14 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 161   |   30872|     960.805|   0.5%/127|   0.5%/142|   0.5%/146|   0.5%/150 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 161   |    4042|      37.251|   1.6%/ 42|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 161   |    2145|      55.898|   0.5%/127|   0.5%/131|   0.5%/132|   0.5%/133 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 161   |    1846|     179.650|   0.2%/421|   0.2%/426|   0.2%/427|   0.2%/428 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 161   |     203|      74.007|   0.3%/201|   0.4%/190|   0.4%/186|   0.4%/182 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 161   |    4013|     206.811|   1.2%/ 58|   1.1%/ 62|   1.1%/ 62|   1.1%/ 63 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 161   |   18008|     122.716|   0.6%/121|   0.5%/126|   0.5%/127|   0.5%/129 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 102   |      20|       1.625|   2.0%/ 34|   1.8%/ 38|   1.8%/ 38|   3.6%/ 19 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 161   |    4173|     121.961|   0.8%/ 88|   0.7%/ 96|   0.7%/ 98|   0.7%/100 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 161   |     299|      18.433|   0.5%/144|   0.3%/210|   0.3%/238|   0.3%/274 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 161   |     734|     105.437|   0.2%/289|   0.1%/470|   0.1%/554|   0.1%/672 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 139   |      71|       9.034|   0.2%/349|   0.2%/296|   0.2%/286|   0.3%/277 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 161   |      27|       4.734|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 161   |      37|       6.804|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 161   |     136|      64.748|   0.2%/416|   0.1%/479|   0.1%/497|   0.1%/516 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 154   |      98|       6.172|   0.1%/650|   0.1%/786|   0.1%/852|   0.1%/939 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 161   |   15461|     263.060|   0.9%/ 80|   0.7%/104|   0.6%/113|   0.6%/122 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 161   |   29441|     625.067|   0.2%/448|   0.2%/388|   0.2%/376|   0.2%/364 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 161   |      12|       0.562|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 161   |     836|      19.710|   0.1%/483|   0.1%/672|   0.1%/740|   0.1%/820 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 161   |    5841|     564.937|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 161   |    2016|     234.333|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 161   |     147|       8.387|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 161   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 161   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 161   |      32|       4.208|   0.9%/ 75|   1.2%/ 59|   1.2%/ 56|   1.3%/ 53 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 161   |      37|      27.371|   6.8%/ 10|   7.4%/  9|   7.6%/  9|   7.8%/  9 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 161   |      90|       7.647|   2.2%/ 32|   2.5%/ 28|   2.6%/ 27|   2.6%/ 26 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 161   |    6504|      78.215|   0.7%/102|   0.8%/ 90|   0.8%/ 88|   0.8%/ 85 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 161   |  191422|     580.870|   0.4%/159|   0.4%/176|   0.4%/181|   0.4%/187 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  47   |      46|       1.140|   3.2%/ 21|   6.0%/ 11|   6.7%/ 10|   7.6%/  9 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 161   |    2960|      70.673|   1.6%/ 43|   1.7%/ 41|   1.7%/ 40|   1.7%/ 40 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 161   |     393|      39.693|   0.3%/240|   0.3%/257|   0.3%/262|   0.3%/268 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 161   |   41096|     618.587|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 161   |      46|      13.113|   0.5%/140|   0.4%/182|   0.4%/197|   0.3%/216 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 161   |     369|      10.820|   1.7%/ 41|   1.4%/ 48|   1.4%/ 50|   1.3%/ 52 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 161   |     455|      14.109|   1.8%/ 38|   1.6%/ 43|   1.5%/ 45|   1.5%/ 46 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  40   |      35|       0.365|   1.8%/ 38|   0.4%/184|   0.1%/821|   0.0%/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 160   |     305|      17.027|   0.4%/171|   0.3%/224|   0.3%/242|   0.3%/264 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 161   |     232|      15.296|   1.0%/ 68|   0.3%/255|   0.1%/796|   0.0%/ -- |

