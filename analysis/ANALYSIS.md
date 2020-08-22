# State and Country COVID-19 Analysis #
## Updated: at 2020-08-22 for data as of 2020-08-21 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 37.9% of deaths and 40.3% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.6% of deaths and 58.4% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 143   |   32882|    1690.271|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 143   |   15941|    1794.706|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 143   |   12026|     304.359|   1.2%/ 56|   1.2%/ 59|   1.2%/ 59|   1.1%/ 60 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 143   |   11950|     412.127|   2.0%/ 35|   1.7%/ 41|   1.6%/ 42|   1.6%/ 44 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 143   |   10450|     486.540|   1.9%/ 37|   1.7%/ 40|   1.7%/ 41|   1.6%/ 43 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 143   |    8904|    1281.209|   0.2%/428|   0.2%/433|   0.2%/435|   0.2%/436 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 143   |    8051|     635.352|   0.2%/295|   0.2%/286|   0.2%/284|   0.2%/282 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 143   |    7528|     588.052|   0.2%/294|   0.3%/277|   0.3%/273|   0.3%/269 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 143   |    6633|     664.192|   0.1%/472|   0.2%/448|   0.2%/442|   0.2%/437 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 143   |    5009|     471.797|   1.3%/ 51|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 143   |  175798|     533.457|   0.6%/109|   0.6%/114|   0.6%/115|   0.6%/117 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 143   |  113638|     537.519|   1.0%/ 72|   0.9%/ 75|   0.9%/ 76|   0.9%/ 77 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 143   |   60295|     476.346|   1.1%/ 62|   1.0%/ 67|   1.0%/ 68|   1.0%/ 70 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 143   |   56388|      41.425|   2.0%/ 35|   1.9%/ 36|   1.9%/ 37|   1.9%/ 37 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 143   |   47137|     709.511|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 143   |   35411|     587.849|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 143   |   30466|     454.204|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 143   |   28737|     610.119|   0.1%/978|   0.1%/788|   0.1%/751|   0.1%/716 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 143   |   27541|     857.152|   0.8%/ 83|   0.7%/ 93|   0.7%/ 96|   0.7%/ 99 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 143   |   20661|     247.799|   0.9%/ 80|   0.8%/ 91|   0.7%/ 94|   0.7%/ 97 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 143   |    2026|     413.157|   1.0%/ 72|   0.8%/ 87|   0.8%/ 91|   0.7%/ 97 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 143   |      30|      40.863|   1.2%/ 56|   1.2%/ 60|   1.1%/ 60|   1.1%/ 61 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 143   |    4798|     659.126|   1.1%/ 63|   0.9%/ 77|   0.8%/ 82|   0.8%/ 87 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 143   |     663|     219.653|   1.7%/ 41|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 143   |   12026|     304.359|   1.2%/ 56|   1.2%/ 59|   1.2%/ 59|   1.1%/ 60 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 143   |    1911|     331.900|   0.2%/406|   0.1%/496|   0.1%/524|   0.1%/556 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 143   |    4461|    1251.319|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 143   |     598|     613.935|   0.1%/646|   0.1%/683|   0.1%/692|   0.1%/701 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 143   |   10450|     486.540|   1.9%/ 37|   1.7%/ 40|   1.7%/ 41|   1.6%/ 43 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 143   |    5009|     471.797|   1.3%/ 51|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 143   |      45|      31.746|   2.4%/ 29|   2.8%/ 25|   2.9%/ 24|   3.0%/ 23 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 143   |     308|     172.471|   2.2%/ 31|   2.1%/ 33|   2.1%/ 33|   2.0%/ 34 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 143   |    8051|     635.352|   0.2%/295|   0.2%/286|   0.2%/284|   0.2%/282 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 143   |    3196|     474.735|   0.4%/168|   0.4%/159|   0.4%/157|   0.4%/154 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 143   |    1024|     324.437|   0.8%/ 83|   0.9%/ 81|   0.9%/ 80|   0.9%/ 80 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 143   |     425|     146.009|   0.8%/ 86|   0.8%/ 90|   0.8%/ 92|   0.7%/ 93 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 143   |     848|     189.836|   0.9%/ 81|   0.9%/ 74|   1.0%/ 72|   1.0%/ 71 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 143   |    4686|    1008.040|   0.8%/ 84|   0.8%/ 86|   0.8%/ 86|   0.8%/ 86 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 143   |     129|      95.597|   0.2%/321|   0.2%/372|   0.2%/386|   0.2%/401 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 143   |    3685|     609.560|   0.2%/309|   0.2%/341|   0.2%/350|   0.2%/360 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 143   |    8904|    1281.209|   0.2%/428|   0.2%/433|   0.2%/435|   0.2%/436 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 143   |    6633|     664.192|   0.1%/472|   0.2%/448|   0.2%/442|   0.2%/437 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 143   |    1788|     317.104|   0.5%/134|   0.6%/121|   0.6%/118|   0.6%/115 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 143   |    2244|     753.885|   1.3%/ 51|   1.3%/ 55|   1.2%/ 56|   1.2%/ 57 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 143   |    1443|     235.183|   0.7%/100|   0.7%/ 99|   0.7%/ 98|   0.7%/ 97 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 143   |      93|      86.857|   1.6%/ 43|   1.2%/ 59|   1.1%/ 64|   1.0%/ 72 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 143   |     375|     193.963|   0.7%/103|   0.7%/101|   0.7%/100|   0.7%/100 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 143   |    1178|     382.451|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 143   |     427|     314.132|   0.2%/420|   0.2%/426|   0.2%/425|   0.2%/422 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 143   |   15941|    1794.706|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 143   |     740|     352.698|   0.7%/106|   0.6%/112|   0.6%/113|   0.6%/115 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 143   |   32882|    1690.271|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 143   |    2502|     238.525|   1.1%/ 62|   1.1%/ 66|   1.0%/ 67|   1.0%/ 68 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 143   |     132|     172.665|   1.3%/ 55|   1.4%/ 51|   1.4%/ 50|   1.4%/ 50 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 143   |    3952|     338.108|   0.6%/112|   0.6%/116|   0.6%/117|   0.6%/118 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 143   |     711|     179.729|   1.4%/ 48|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 143   |     417|      98.930|   1.3%/ 53|   1.3%/ 55|   1.3%/ 55|   1.2%/ 55 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 143   |    7528|     588.052|   0.2%/294|   0.3%/277|   0.3%/273|   0.3%/269 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 143   |     374|     117.196|   2.6%/ 27|   2.7%/ 26|   2.7%/ 25|   2.7%/ 25 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 143   |    1028|     970.009|   0.1%/604|   0.1%/552|   0.1%/539|   0.1%/526 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 143   |    2493|     484.136|   1.6%/ 44|   1.3%/ 52|   1.3%/ 55|   1.2%/ 57 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 143   |     160|     180.639|   0.8%/ 84|   0.7%/ 95|   0.7%/ 98|   0.7%/102 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 143   |    1503|     219.913|   1.8%/ 38|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 143   |   11950|     412.127|   2.0%/ 35|   1.7%/ 41|   1.6%/ 42|   1.6%/ 44 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 143   |  175798|     533.457|   0.6%/109|   0.6%/114|   0.6%/115|   0.6%/117 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 143   |     387|     120.720|   1.1%/ 66|   0.9%/ 74|   0.9%/ 76|   0.9%/ 79 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 143   |      58|      93.566|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 143   |    2457|     287.820|   0.4%/155|   0.4%/190|   0.3%/202|   0.3%/216 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 143   |    1850|     242.940|   0.8%/ 90|   0.8%/ 89|   0.8%/ 89|   0.8%/ 88 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 143   |     175|      97.464|   1.8%/ 39|   1.8%/ 39|   1.7%/ 40|   1.7%/ 40 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 143   |    1074|     184.418|   0.6%/107|   0.6%/113|   0.6%/115|   0.6%/116 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 131   |      32|      56.097|   1.0%/ 69|   1.1%/ 65|   1.1%/ 64|   1.1%/ 63 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 143   |    1396|      43.316|   0.4%/191|   0.3%/215|   0.3%/222|   0.3%/230 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 143   |     251|      88.091|   1.7%/ 40|   1.4%/ 48|   1.3%/ 51|   1.3%/ 55 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 143   |    1426|      33.155|   0.7%/ 94|   0.7%/ 99|   0.7%/100|   0.7%/102 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 143   |     102|       3.284|   2.2%/ 32|   1.7%/ 40|   1.6%/ 43|   1.5%/ 46 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 143   |    6746|     150.115|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 143   |     849|     286.958|   0.5%/129|   0.4%/158|   0.4%/167|   0.4%/177 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 143   |     525|      20.428|   3.9%/ 18|   3.6%/ 19|   3.6%/ 19|   3.5%/ 20 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 143   |     730|      82.048|   0.1%/788|   0.1%/792|   0.1%/794|   0.1%/796 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 143   |     525|      52.166|   0.4%/164|   0.2%/438|   0.1%/744|   0.0%/ *** |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 143   |     181|     117.277|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71|   1.0%/ 71 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 143   |    3862|      22.923|   1.0%/ 66|   1.0%/ 68|   1.0%/ 68|   1.0%/ 69 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 143   |     629|      66.879|   0.6%/119|   0.6%/125|   0.5%/126|   0.5%/127 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 143   |    9971|     865.162|   0.1%/849|   0.1%/726|   0.1%/700|   0.1%/676 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 138   |      40|       3.369|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 143   |    4478|     390.424|   1.6%/ 43|   1.3%/ 52|   1.3%/ 54|   1.2%/ 57 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 143   |     534|     161.913|   1.8%/ 38|   1.7%/ 40|   1.7%/ 40|   1.7%/ 41 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 143   |       3|       1.358|   2.3%/ 29|   1.8%/ 39|   1.6%/ 42|   1.5%/ 45 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 143   |  113638|     537.519|   1.0%/ 72|   0.9%/ 75|   0.9%/ 76|   0.9%/ 77 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 143   |     549|      78.987|   1.6%/ 45|   1.4%/ 49|   1.4%/ 50|   1.3%/ 51 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 143   |      55|       2.637|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 131   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 143   |     407|      15.328|   0.2%/282|   0.3%/254|   0.3%/247|   0.3%/241 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 143   |    9107|     239.668|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  91   |      61|      11.176|   0.2%/404|   0.1%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 116   |      76|       4.692|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 143   |   10778|     564.089|   0.5%/129|   0.5%/148|   0.5%/153|   0.4%/159 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 143   |    4711|       3.360|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 143   |   17069|     345.552|   2.2%/ 31|   1.9%/ 36|   1.9%/ 37|   1.8%/ 38 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 143   |     370|      73.069|   3.3%/ 21|   2.8%/ 25|   2.6%/ 26|   2.5%/ 28 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 143   |     172|      42.086|   0.6%/115|   0.4%/156|   0.4%/170|   0.4%/187 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 143   |      88|       7.890|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 143   |     622|     106.904|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 143   |    1551|     149.715|   1.4%/ 51|   1.3%/ 53|   1.3%/ 54|   1.3%/ 55 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 143   |    6217|     355.922|   0.4%/167|   0.4%/175|   0.4%/176|   0.4%/178 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 143   |    5272|      52.573|   0.3%/198|   0.3%/269|   0.2%/294|   0.2%/324 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 143   |     669|     103.134|   1.6%/ 44|   1.3%/ 53|   1.2%/ 56|   1.2%/ 59 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 122   |      85|      62.835|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 139   |     649|       6.582|   3.9%/ 18|   3.8%/ 18|   3.7%/ 18|   3.7%/ 19 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 143   |     335|      60.527|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 143   |   30466|     454.204|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 143   |      53|      24.316|   0.3%/242|   0.3%/244|   0.3%/243|   0.3%/241 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 143   |      84|      35.780|  17.8%/  4|   6.9%/ 10|   8.7%/  8|  10.1%/  7 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 140   |      17|       4.595|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 143   |    9264|     111.411|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 143   |     260|       8.571|   1.9%/ 36|   2.0%/ 34|   2.0%/ 34|   2.1%/ 33 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 143   |     235|      21.891|   0.8%/ 86|   0.9%/ 73|   1.0%/ 71|   1.0%/ 68 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 143   |    2556|     153.946|   1.2%/ 56|   1.1%/ 65|   1.0%/ 67|   1.0%/ 70 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 129   |      53|       4.339|   0.7%/105|   0.6%/110|   0.6%/110|   0.6%/110 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 118   |      34|      20.973|   0.6%/112|   0.5%/136|   0.5%/144|   0.4%/155 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 139   |     203|      17.524|   0.8%/ 88|   0.7%/105|   0.6%/112|   0.6%/119 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 143   |    1677|     183.117|   0.8%/ 89|   0.4%/171|   0.3%/220|   0.2%/304 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 143   |     611|      62.500|   0.1%/639|   0.1%/602|   0.1%/596|   0.1%/592 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 143   |   56388|      41.425|   2.0%/ 35|   1.9%/ 36|   1.9%/ 37|   1.9%/ 37 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 143   |    6515|      24.408|   1.1%/ 64|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 143   |   20661|     247.799|   0.9%/ 80|   0.8%/ 91|   0.7%/ 94|   0.7%/ 97 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 143   |    6300|     161.006|   1.3%/ 52|   1.3%/ 55|   1.2%/ 56|   1.2%/ 56 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 143   |    1777|     361.154|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 143   |     749|      81.542|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41|   1.7%/ 42 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 143   |   35411|     587.849|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 143   |      15|       5.617|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 143   |    1137|       9.031|   0.9%/ 79|   1.1%/ 65|   1.1%/ 62|   1.2%/ 60 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 143   |      11|       1.032|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 143   |    1525|      81.590|   1.7%/ 41|   2.1%/ 33|   2.2%/ 31|   2.3%/ 30 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 143   |     537|      11.281|   1.9%/ 36|   1.6%/ 42|   1.6%/ 44|   1.5%/ 46 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 143   |     459|     255.371|   2.3%/ 30|   1.7%/ 40|   1.6%/ 43|   1.4%/ 48 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 140   |     515|     116.572|   0.6%/123|   0.5%/137|   0.5%/142|   0.5%/146 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 141   |    1531|     234.266|   0.2%/397|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 141   |      33|      17.164|   0.3%/268|   0.3%/226|   0.3%/215|   0.3%/205 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 143   |     118|      17.309|   3.3%/ 21|   3.2%/ 21|   3.2%/ 21|   3.2%/ 22 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 140   |      84|      18.747|   0.3%/226|   0.1%/477|   0.1%/673|   0.1%/ *** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 142   |     187|      27.162|   3.7%/ 19|   3.5%/ 19|   3.5%/ 20|   3.5%/ 20 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 143   |      82|      29.237|   0.1%/529|   0.2%/435|   0.2%/416|   0.2%/398 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  97   |     185|       7.034|   2.0%/ 35|   1.1%/ 61|   0.9%/ 74|   0.7%/ 95 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 143   |     125|       3.822|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 143   |     125|       6.188|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 143   |     158|      38.647|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 143   |   60295|     476.346|   1.1%/ 62|   1.0%/ 67|   1.0%/ 68|   1.0%/ 70 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 143   |     936|     348.928|   0.8%/ 88|   0.7%/ 96|   0.7%/ 98|   0.7%/101 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 143   |     801|      22.321|   4.1%/ 17|   4.4%/ 16|   4.5%/ 15|   4.5%/ 15 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  89   |      20|       0.681|   1.7%/ 41|   1.0%/ 73|   0.8%/ 92|   0.5%/126 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  43   |      42|      17.152|   9.8%/  7|   4.6%/ 15|   3.4%/ 20|   2.4%/ 29 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  98   |     133|       4.442|   4.8%/ 14|   4.9%/ 14|   4.9%/ 14|   5.0%/ 14 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 143   |    6206|     355.474|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 143   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 143   |     134|      20.786|   0.6%/110|   0.6%/120|   0.6%/122|   0.6%/125 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 143   |      69|       3.092|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 143   |    1005|       4.877|   0.5%/144|   0.4%/176|   0.4%/186|   0.3%/198 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 143   |     562|     270.726|   0.5%/127|   0.4%/163|   0.4%/175|   0.4%/189 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 143   |     262|      48.889|   0.2%/424|   0.2%/330|   0.2%/312|   0.2%/296 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 143   |     632|     135.401|   1.5%/ 45|   1.4%/ 49|   1.4%/ 49|   1.4%/ 50 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 143   |    6245|      28.473|   0.2%/363|   0.1%/468|   0.1%/503|   0.1%/545 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 143   |    1896|     449.345|   1.1%/ 61|   0.9%/ 73|   0.9%/ 77|   0.9%/ 81 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  26   |       4|       0.448|   0.0%/ --|   0.0%/ --|  10.1%/  7|  10.1%/  7 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 143   |     175|      24.417|   6.7%/ 10|   7.3%/  9|   7.5%/  9|   7.6%/  9 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 143   |   27541|     857.152|   0.8%/ 83|   0.7%/ 93|   0.7%/ 96|   0.7%/ 99 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 143   |    2832|      26.102|   2.1%/ 33|   2.4%/ 28|   2.5%/ 28|   2.6%/ 27 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 143   |    1932|      50.353|   0.6%/114|   0.6%/109|   0.6%/108|   0.6%/107 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 143   |    1792|     174.344|   0.2%/413|   0.2%/411|   0.2%/411|   0.2%/411 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 143   |     197|      71.876|   0.4%/156|   0.3%/215|   0.3%/239|   0.3%/271 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 143   |    3212|     165.530|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 143   |   16239|     110.658|   0.7%/101|   0.6%/110|   0.6%/112|   0.6%/115 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  84   |      11|       0.891|   5.0%/ 14|   5.0%/ 14|   5.0%/ 14|   5.1%/ 13 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 143   |    3589|     104.872|   1.1%/ 66|   1.0%/ 67|   1.0%/ 67|   1.0%/ 67 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 143   |     268|      16.528|   1.1%/ 64|   0.9%/ 74|   0.9%/ 77|   0.9%/ 80 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 143   |     707|     101.555|   0.7%/ 94|   0.5%/129|   0.5%/143|   0.4%/159 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 121   |      70|       8.798|   0.1%/600|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 143   |      27|       4.734|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 143   |      33|       6.027|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 143   |     132|      63.085|   0.2%/292|   0.1%/543|   0.1%/707|   0.1%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 136   |      93|       5.852|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 143   |   13386|     227.752|   2.0%/ 35|   1.6%/ 43|   1.5%/ 45|   1.4%/ 48 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 143   |   28737|     610.119|   0.1%/978|   0.1%/788|   0.1%/751|   0.1%/716 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 143   |      11|       0.505|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 143   |     818|      19.285|   0.4%/173|   0.3%/201|   0.3%/209|   0.3%/219 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 143   |    5807|     561.654|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 143   |    1997|     232.079|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 143   |      76|       4.341|   1.4%/ 50|   1.1%/ 64|   1.0%/ 69|   0.9%/ 74 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 143   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 143   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 143   |      29|       3.883|   1.5%/ 47|   1.1%/ 64|   1.0%/ 70|   0.9%/ 79 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 143   |       8|       5.865|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 143   |      54|       4.602|   0.9%/ 79|   1.1%/ 61|   1.2%/ 58|   1.3%/ 55 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 143   |    6068|      72.970|   0.3%/214|   0.3%/206|   0.3%/205|   0.3%/203 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 143   |  175798|     533.457|   0.6%/109|   0.6%/114|   0.6%/115|   0.6%/117 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  29   |      19|       0.481|   9.1%/  7|   7.0%/ 10|   7.7%/  9|   8.5%/  8 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 143   |    2240|      53.498|   1.3%/ 52|   1.4%/ 51|   1.4%/ 50|   1.4%/ 50 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 143   |     368|      37.213|   0.3%/229|   0.3%/210|   0.3%/205|   0.3%/200 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 143   |   47137|     709.511|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 143   |      40|      11.450|   0.9%/ 77|   1.0%/ 66|   1.1%/ 63|   1.1%/ 61 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 143   |     269|       7.890|   2.6%/ 26|   2.3%/ 30|   2.2%/ 32|   2.1%/ 33 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 143   |     327|      10.155|   3.1%/ 22|   3.0%/ 23|   2.9%/ 24|   2.9%/ 24 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  22   |      25|       0.260|  10.1%/  7|   1.4%/ 51|   0.0%/ ***|   0.0%/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 142   |     299|      16.728|   1.4%/ 48|   1.6%/ 44|   1.6%/ 43|   1.6%/ 42 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 143   |     174|      11.475|   2.1%/ 32|   4.4%/ 16|   3.8%/ 18|   2.5%/ 27 |

