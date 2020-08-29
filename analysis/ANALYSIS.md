# State and Country COVID-19 Analysis #
## Updated: at 2020-08-29 for data as of 2020-08-28 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.1% of deaths and 40.0% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.2% of deaths and 58.0% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 150   |   32933|    1692.920|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 150   |   15955|    1796.236|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 150   |   12903|     326.557|   1.1%/ 64|   1.0%/ 68|   1.0%/ 70|   1.0%/ 71 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 150   |   13058|     450.351|   1.6%/ 43|   1.4%/ 48|   1.4%/ 50|   1.4%/ 51 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 150   |   11314|     526.789|   1.4%/ 50|   1.2%/ 60|   1.1%/ 63|   1.0%/ 67 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 150   |    9011|    1296.640|   0.2%/388|   0.2%/375|   0.2%/372|   0.2%/368 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 150   |    8190|     646.307|   0.3%/277|   0.3%/264|   0.3%/261|   0.3%/258 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 150   |    7644|     597.071|   0.2%/312|   0.2%/309|   0.2%/309|   0.2%/309 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 150   |    6709|     671.745|   0.2%/446|   0.2%/429|   0.2%/425|   0.2%/421 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 150   |    5489|     516.990|   1.3%/ 53|   1.3%/ 54|   1.3%/ 54|   1.3%/ 55 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 150   |  182354|     553.353|   0.6%/123|   0.5%/130|   0.5%/131|   0.5%/133 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 150   |  120218|     568.643|   0.9%/ 81|   0.8%/ 85|   0.8%/ 87|   0.8%/ 88 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 150   |   63882|     504.686|   0.9%/ 75|   0.8%/ 84|   0.8%/ 87|   0.8%/ 90 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 150   |   63363|      46.548|   1.8%/ 39|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 150   |   41072|     618.226|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 150   |   35503|     589.370|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 150   |   30578|     455.872|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 150   |   28969|     615.043|   0.1%/778|   0.1%/666|   0.1%/642|   0.1%/620 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 150   |   29678|     923.655|   0.7%/ 98|   0.6%/112|   0.6%/116|   0.6%/120 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 150   |   21532|     258.249|   0.7%/100|   0.6%/117|   0.6%/123|   0.5%/128 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 150   |    2118|     431.943|   0.8%/ 89|   0.7%/106|   0.6%/112|   0.6%/118 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 150   |      35|      47.566|   1.1%/ 61|   1.1%/ 64|   1.1%/ 65|   1.1%/ 66 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 150   |    5032|     691.372|   0.9%/ 78|   0.8%/ 92|   0.7%/ 96|   0.7%/100 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 150   |     749|     248.310|   1.8%/ 38|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 150   |   12903|     326.557|   1.1%/ 64|   1.0%/ 68|   1.0%/ 70|   1.0%/ 71 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 150   |    1937|     336.336|   0.2%/368|   0.2%/382|   0.2%/385|   0.2%/389 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 150   |    4467|    1252.959|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 150   |     604|     620.360|   0.1%/494|   0.1%/464|   0.2%/456|   0.2%/449 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 150   |   11314|     526.789|   1.4%/ 50|   1.2%/ 60|   1.1%/ 63|   1.0%/ 67 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 150   |    5489|     516.990|   1.3%/ 53|   1.3%/ 54|   1.3%/ 54|   1.3%/ 55 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 150   |      55|      38.941|   2.7%/ 25|   2.9%/ 23|   3.0%/ 23|   3.1%/ 23 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 150   |     350|     195.695|   2.2%/ 31|   2.2%/ 31|   2.2%/ 31|   2.2%/ 31 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 150   |    8190|     646.307|   0.3%/277|   0.3%/264|   0.3%/261|   0.3%/258 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 150   |    3283|     487.630|   0.4%/182|   0.4%/182|   0.4%/182|   0.4%/182 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 150   |    1089|     345.199|   0.9%/ 74|   1.0%/ 70|   1.0%/ 69|   1.0%/ 68 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 150   |     446|     153.051|   0.8%/ 86|   0.8%/ 87|   0.8%/ 87|   0.8%/ 87 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 150   |     912|     204.198|   0.9%/ 74|   1.0%/ 68|   1.0%/ 67|   1.0%/ 66 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 150   |    4927|    1059.740|   0.8%/ 92|   0.7%/ 95|   0.7%/ 96|   0.7%/ 97 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 150   |     132|      98.126|   0.3%/214|   0.3%/198|   0.4%/194|   0.4%/190 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 150   |    3734|     617.558|   0.2%/335|   0.2%/361|   0.2%/367|   0.2%/374 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 150   |    9011|    1296.640|   0.2%/388|   0.2%/375|   0.2%/372|   0.2%/368 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 150   |    6709|     671.745|   0.2%/446|   0.2%/429|   0.2%/425|   0.2%/421 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 150   |    1855|     328.883|   0.5%/136|   0.5%/129|   0.5%/127|   0.5%/126 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 150   |    2423|     814.088|   1.3%/ 54|   1.2%/ 57|   1.2%/ 57|   1.2%/ 58 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 150   |    1502|     244.772|   0.6%/115|   0.6%/117|   0.6%/118|   0.6%/119 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 150   |     101|      94.423|   1.6%/ 43|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 150   |     392|     202.608|   0.6%/107|   0.6%/107|   0.6%/107|   0.6%/107 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 150   |    1303|     422.952|   1.5%/ 45|   1.5%/ 48|   1.4%/ 48|   1.4%/ 49 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 150   |     432|     317.348|   0.1%/490|   0.1%/490|   0.1%/490|   0.1%/490 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 150   |   15955|    1796.236|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 150   |     769|     366.673|   0.6%/118|   0.6%/124|   0.6%/125|   0.5%/127 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 150   |   32933|    1692.920|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 150   |    2667|     254.313|   1.0%/ 70|   0.9%/ 74|   0.9%/ 75|   0.9%/ 76 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 150   |     143|     187.273|   1.0%/ 67|   1.0%/ 72|   0.9%/ 74|   0.9%/ 75 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 150   |    4098|     350.592|   0.6%/121|   0.6%/124|   0.6%/124|   0.6%/125 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 150   |     781|     197.363|   1.4%/ 49|   1.5%/ 47|   1.5%/ 47|   1.5%/ 46 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 150   |     446|     105.836|   1.1%/ 62|   1.1%/ 65|   1.1%/ 66|   1.0%/ 66 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 150   |    7644|     597.071|   0.2%/312|   0.2%/309|   0.2%/309|   0.2%/309 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 150   |     433|     135.593|   2.1%/ 33|   2.0%/ 35|   2.0%/ 35|   1.9%/ 36 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 150   |    1041|     982.372|   0.2%/385|   0.2%/328|   0.2%/316|   0.2%/304 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 150   |    2695|     523.514|   1.3%/ 52|   1.2%/ 60|   1.1%/ 62|   1.1%/ 64 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 150   |     166|     187.742|   0.6%/114|   0.5%/140|   0.5%/148|   0.4%/158 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 150   |    1706|     249.709|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 150   |   13058|     450.351|   1.6%/ 43|   1.4%/ 48|   1.4%/ 50|   1.4%/ 51 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 150   |  182354|     553.353|   0.6%/123|   0.5%/130|   0.5%/131|   0.5%/133 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 150   |     409|     127.597|   0.9%/ 74|   0.9%/ 81|   0.8%/ 82|   0.8%/ 84 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 150   |      58|      93.250|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 150   |    2531|     296.552|   0.5%/136|   0.5%/137|   0.5%/136|   0.5%/135 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 150   |    1924|     252.663|   0.6%/121|   0.5%/137|   0.5%/142|   0.5%/148 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 150   |     199|     111.118|   2.0%/ 35|   2.0%/ 35|   2.0%/ 35|   2.0%/ 34 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 150   |    1115|     191.581|   0.6%/117|   0.6%/122|   0.6%/123|   0.6%/124 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 138   |      38|      66.255|   0.5%/131|   0.4%/188|   0.3%/213|   0.3%/245 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 150   |    1416|      43.942|   0.3%/260|   0.2%/334|   0.2%/361|   0.2%/394 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 150   |     275|      96.551|   1.6%/ 43|   1.4%/ 48|   1.4%/ 50|   1.3%/ 51 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 150   |    1490|      34.641|   0.7%/103|   0.6%/108|   0.6%/110|   0.6%/112 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 150   |     111|       3.565|   1.8%/ 39|   1.4%/ 49|   1.3%/ 52|   1.2%/ 56 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 150   |    8289|     184.445|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 150   |     874|     295.539|   0.5%/149|   0.4%/172|   0.4%/178|   0.4%/185 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 150   |     629|      24.489|   3.3%/ 21|   3.0%/ 23|   2.9%/ 24|   2.8%/ 25 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 150   |     735|      82.537|   0.1%/926|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 150   |     531|      52.717|   0.3%/213|   0.2%/344|   0.2%/401|   0.1%/480 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 150   |     192|     124.108|   0.8%/ 87|   0.7%/ 97|   0.7%/100|   0.7%/103 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 150   |    4162|      24.703|   1.1%/ 64|   1.1%/ 63|   1.1%/ 63|   1.1%/ 62 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 150   |     662|      70.342|   0.7%/ 98|   0.8%/ 92|   0.8%/ 90|   0.8%/ 89 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 150   |   10028|     870.136|   0.1%/895|   0.1%/859|   0.1%/853|   0.1%/848 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 145   |      40|       3.400|   0.3%/241|   0.3%/212|   0.3%/205|   0.4%/197 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 150   |    4903|     427.438|   1.5%/ 47|   1.3%/ 51|   1.3%/ 53|   1.3%/ 54 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 150   |     598|     181.291|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 150   |       3|       1.426|   1.2%/ 57|   0.6%/109|   0.5%/147|   0.3%/228 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 150   |  120218|     568.643|   0.9%/ 81|   0.8%/ 85|   0.8%/ 87|   0.8%/ 88 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 150   |     602|      86.607|   1.5%/ 45|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 150   |      55|       2.650|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 138   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 150   |     413|      15.543|   0.2%/355|   0.2%/368|   0.2%/373|   0.2%/379 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 150   |    9153|     240.886|   0.1%/967|   0.1%/954|   0.1%/950|   0.1%/947 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  98   |      61|      11.110|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 123   |      77|       4.721|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 150   |   11151|     583.589|   0.5%/134|   0.5%/143|   0.5%/145|   0.5%/147 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 150   |    4725|       3.369|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 150   |   19191|     388.517|   1.9%/ 36|   1.7%/ 40|   1.7%/ 42|   1.6%/ 43 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 150   |     426|      84.164|   2.7%/ 25|   2.3%/ 30|   2.1%/ 32|   2.0%/ 34 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 150   |     178|      43.715|   0.7%/105|   0.6%/108|   0.6%/108|   0.6%/109 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 150   |      91|       8.118|   0.3%/246|   0.4%/193|   0.4%/183|   0.4%/173 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 150   |     624|     107.180|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 150   |    1670|     161.176|   1.2%/ 59|   1.1%/ 65|   1.0%/ 67|   1.0%/ 68 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 150   |    6449|     369.198|   0.5%/132|   0.6%/123|   0.6%/120|   0.6%/118 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 150   |    5369|      53.545|   0.3%/211|   0.3%/236|   0.3%/243|   0.3%/250 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 150   |     717|     110.583|   1.2%/ 56|   1.0%/ 67|   1.0%/ 71|   0.9%/ 75 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 129   |      83|      61.135|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 146   |     798|       8.091|   3.1%/ 22|   2.8%/ 25|   2.7%/ 25|   2.7%/ 26 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 150   |     336|      60.703|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 150   |   30578|     455.872|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 150   |      53|      24.624|   0.1%/566|   0.1%/829|   0.1%/943|   0.1%/ *** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 150   |     145|      61.810|   2.9%/ 23|   2.2%/ 31|   2.2%/ 31|   2.2%/ 32 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 147   |      18|       4.864|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 150   |    9298|     111.822|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 150   |     282|       9.319|   1.2%/ 58|   1.0%/ 69|   0.9%/ 73|   0.9%/ 78 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 150   |     251|      23.419|   0.9%/ 75|   1.0%/ 68|   1.0%/ 66|   1.1%/ 65 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 150   |    2740|     165.036|   1.1%/ 65|   1.0%/ 72|   0.9%/ 73|   0.9%/ 75 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 136   |      57|       4.661|   1.1%/ 65|   1.3%/ 54|   1.3%/ 52|   1.4%/ 49 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 125   |      35|      21.725|   0.4%/161|   0.4%/188|   0.4%/194|   0.3%/200 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 146   |     205|      17.664|   0.4%/177|   0.2%/417|   0.1%/635|   0.1%/ *** |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 150   |    1771|     193.321|   1.1%/ 63|   1.1%/ 61|   1.2%/ 60|   1.2%/ 59 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 150   |     615|      62.969|   0.1%/714|   0.1%/774|   0.1%/792|   0.1%/811 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 150   |   63363|      46.548|   1.8%/ 39|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 150   |    7088|      26.555|   1.2%/ 56|   1.3%/ 55|   1.3%/ 54|   1.3%/ 54 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 150   |   21532|     258.249|   0.7%/100|   0.6%/117|   0.6%/123|   0.5%/128 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 150   |    6856|     175.220|   1.2%/ 56|   1.2%/ 58|   1.2%/ 58|   1.2%/ 59 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 150   |    1779|     361.482|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 150   |     910|      99.067|   1.6%/ 43|   1.5%/ 45|   1.5%/ 46|   1.5%/ 46 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 150   |   35503|     589.370|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 150   |      17|       6.230|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 150   |    1239|       9.840|   1.0%/ 69|   1.1%/ 62|   1.2%/ 60|   1.2%/ 58 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 150   |      11|       1.032|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 150   |    1619|      86.654|   1.4%/ 50|   1.5%/ 45|   1.6%/ 44|   1.6%/ 44 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 150   |     591|      12.423|   1.4%/ 48|   1.2%/ 57|   1.2%/ 60|   1.1%/ 63 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 150   |     520|     289.478|   2.0%/ 34|   1.6%/ 42|   1.5%/ 45|   1.5%/ 47 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 147   |     529|     119.715|   0.4%/158|   0.4%/187|   0.4%/197|   0.3%/207 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 148   |    1068|     163.398|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 148   |      33|      17.539|   0.3%/222|   0.4%/181|   0.4%/172|   0.4%/165 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 150   |     149|      21.765|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 147   |      83|      18.603|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 149   |     230|      33.545|   3.5%/ 20|   3.3%/ 21|   3.3%/ 21|   3.2%/ 21 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 150   |      85|      30.347|   0.4%/195|   0.4%/156|   0.5%/149|   0.5%/142 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 104   |     188|       7.157|   1.0%/ 72|   0.5%/141|   0.4%/183|   0.3%/255 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 150   |     125|       3.817|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 150   |     126|       6.203|   0.1%/970|   0.1%/820|   0.1%/784|   0.1%/749 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 150   |     158|      38.774|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 150   |   63882|     504.686|   0.9%/ 75|   0.8%/ 84|   0.8%/ 87|   0.8%/ 90 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 150   |     983|     366.555|   0.8%/ 89|   0.8%/ 92|   0.7%/ 93|   0.7%/ 94 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 150   |    1066|      29.714|   4.3%/ 16|   4.5%/ 15|   4.5%/ 15|   4.5%/ 15 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  96   |      21|       0.712|   1.0%/ 67|   0.7%/105|   0.6%/120|   0.5%/138 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  50   |      66|      26.724|   6.1%/ 11|   5.3%/ 13|   4.8%/ 14|   4.2%/ 16 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 105   |     192|       6.385|   5.1%/ 13|   5.3%/ 13|   5.4%/ 13|   5.4%/ 13 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 150   |    6240|     357.434|   0.1%/ ***|   0.1%/895|   0.1%/863|   0.1%/832 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 150   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 150   |     138|      21.388|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 150   |      69|       3.092|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 150   |    1024|       4.968|   0.3%/209|   0.2%/287|   0.2%/317|   0.2%/352 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 150   |     585|     281.463|   0.6%/108|   0.6%/108|   0.6%/107|   0.6%/107 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 150   |     265|      49.461|   0.1%/809|   0.1%/803|   0.1%/807|   0.1%/813 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 150   |     674|     144.570|   1.2%/ 58|   1.1%/ 66|   1.0%/ 68|   1.0%/ 71 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 150   |    6301|      28.727|   0.2%/443|   0.1%/537|   0.1%/566|   0.1%/598 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 150   |    1998|     473.555|   0.9%/ 78|   0.7%/ 94|   0.7%/ 99|   0.7%/105 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  33   |       4|       0.448|   6.5%/ 11|   1.3%/ 53|   3.0%/ 23|   4.8%/ 14 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 150   |     285|      39.845|   6.2%/ 11|   6.4%/ 11|   6.5%/ 11|   6.5%/ 10 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 150   |   29678|     923.655|   0.7%/ 98|   0.6%/112|   0.6%/116|   0.6%/120 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 150   |    3280|      30.226|   2.0%/ 34|   2.2%/ 32|   2.2%/ 31|   2.2%/ 31 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 150   |    2016|      52.525|   0.6%/113|   0.6%/111|   0.6%/110|   0.6%/110 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 150   |    1813|     176.455|   0.2%/401|   0.2%/398|   0.2%/398|   0.2%/397 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 150   |     198|      72.183|   0.2%/316|   0.1%/861|   0.0%/ ***|   0.0%/ *** |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 150   |    3525|     181.642|   1.4%/ 50|   1.3%/ 51|   1.3%/ 52|   1.3%/ 52 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 150   |   16913|     115.256|   0.6%/110|   0.6%/116|   0.6%/118|   0.6%/120 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  91   |      16|       1.304|   5.3%/ 13|   5.7%/ 12|   5.8%/ 12|   5.8%/ 12 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 150   |    3841|     112.257|   1.0%/ 71|   0.9%/ 73|   0.9%/ 74|   0.9%/ 75 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 150   |     284|      17.510|   0.9%/ 76|   0.8%/ 89|   0.7%/ 93|   0.7%/ 97 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 150   |     724|     103.913|   0.5%/146|   0.3%/226|   0.3%/261|   0.2%/308 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 128   |      70|       8.811|   0.1%/659|   0.1%/802|   0.1%/835|   0.1%/862 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 150   |      27|       4.734|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 150   |      34|       6.152|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 150   |     134|      63.927|   0.2%/289|   0.2%/409|   0.2%/451|   0.1%/502 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 143   |      94|       5.920|   0.2%/435|   0.2%/311|   0.2%/289|   0.3%/269 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 150   |   14378|     244.630|   1.3%/ 51|   1.0%/ 70|   0.9%/ 77|   0.8%/ 86 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 150   |   28969|     615.043|   0.1%/778|   0.1%/666|   0.1%/642|   0.1%/620 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 150   |      12|       0.545|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 150   |     830|      19.569|   0.3%/267|   0.2%/364|   0.2%/401|   0.2%/446 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 150   |    5825|     563.423|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 150   |    2004|     232.953|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 150   |     104|       5.918|   3.0%/ 23|   3.1%/ 22|   3.2%/ 22|   3.2%/ 21 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 150   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 150   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 150   |      29|       3.856|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 150   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 150   |      74|       6.315|   1.1%/ 61|   1.3%/ 52|   1.4%/ 50|   1.4%/ 48 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 150   |    6221|      74.817|   0.3%/198|   0.4%/189|   0.4%/187|   0.4%/185 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 150   |  182354|     553.353|   0.6%/123|   0.5%/130|   0.5%/131|   0.5%/133 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  36   |      29|       0.723|   6.4%/ 11|   6.7%/ 10|   6.8%/ 10|   6.8%/ 10 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 150   |    2469|      58.947|   1.4%/ 50|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 150   |     379|      38.309|   0.4%/197|   0.4%/182|   0.4%/178|   0.4%/175 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 150   |   41072|     618.226|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 150   |      43|      12.325|   0.8%/ 82|   0.9%/ 76|   0.9%/ 74|   0.9%/ 73 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 150   |     311|       9.106|   2.3%/ 30|   2.1%/ 34|   2.0%/ 35|   1.9%/ 36 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 150   |     382|      11.851|   2.4%/ 28|   2.1%/ 32|   2.0%/ 34|   2.0%/ 35 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  29   |      31|       0.317|   1.3%/ 54|   3.0%/ 23|   3.4%/ 20|   3.8%/ 18 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 149   |     310|      17.336|   0.4%/179|   0.3%/263|   0.2%/299|   0.2%/347 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 150   |     196|      12.918|   3.1%/ 22|   2.6%/ 27|   2.4%/ 28|   2.3%/ 30 |

