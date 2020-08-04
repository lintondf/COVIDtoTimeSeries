# State and Country COVID-19 Analysis #
## Updated: at 2020-08-04 for data as of 2020-08-03 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 36.2% of deaths and 39.9% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 68.6% of deaths and 55.8% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 125   |   32743|    1683.134|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 125   |   15872|    1786.983|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 125   |    9495|     240.316|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48|   1.5%/ 47 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 125   |    8650|    1244.651|   0.2%/388|   0.2%/388|   0.2%/388|   0.2%/387 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 125   |    7731|     610.106|   0.2%/338|   0.2%/349|   0.2%/352|   0.2%/354 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 125   |    7247|     566.105|   0.2%/358|   0.2%/405|   0.2%/419|   0.2%/433 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 125   |    7203|     335.357|   2.6%/ 27|   2.7%/ 26|   2.7%/ 25|   2.8%/ 25 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 125   |    7227|     249.258|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 125   |    6465|     647.395|   0.1%/650|   0.1%/681|   0.1%/685|   0.1%/689 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 125   |    4441|    1245.610|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 125   |  155646|     472.306|   0.7%/ 99|   0.7%/ 94|   0.7%/ 93|   0.8%/ 92 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 125   |   95802|     453.153|   1.2%/ 58|   1.1%/ 62|   1.1%/ 64|   1.1%/ 65 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 125   |   48771|     385.305|   1.4%/ 50|   1.3%/ 54|   1.2%/ 56|   1.2%/ 57 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 125   |   46364|     697.877|   0.1%/499|   0.1%/523|   0.1%/529|   0.1%/535 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 125   |   39239|      28.826|   2.3%/ 29|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 125   |   35173|     583.890|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 125   |   30286|     451.511|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 125   |   28453|     604.096|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 125   |   20439|     636.105|   1.1%/ 61|   1.0%/ 68|   1.0%/ 70|   1.0%/ 72 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 125   |   17508|     209.988|   1.4%/ 51|   1.3%/ 53|   1.3%/ 53|   1.3%/ 54 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 125   |    1667|     339.968|   1.6%/ 44|   1.5%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 125   |      24|      33.116|   2.3%/ 30|   2.9%/ 24|   3.0%/ 23|   3.1%/ 22 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 125   |    3961|     544.148|   2.2%/ 31|   1.9%/ 36|   1.8%/ 38|   1.7%/ 40 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 125   |     472|     156.563|   1.9%/ 37|   1.9%/ 36|   2.0%/ 35|   2.0%/ 35 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 125   |    9495|     240.316|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48|   1.5%/ 47 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 125   |    1847|     320.785|   0.3%/201|   0.4%/188|   0.4%/185|   0.4%/182 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 125   |    4441|    1245.610|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 125   |     597|     612.731|   0.2%/436|   0.2%/447|   0.2%/451|   0.2%/454 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 125   |    7203|     335.357|   2.6%/ 27|   2.7%/ 26|   2.7%/ 25|   2.8%/ 25 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 125   |    3859|     363.465|   1.3%/ 53|   1.4%/ 48|   1.5%/ 47|   1.5%/ 46 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 125   |      27|      19.064|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 125   |     199|     111.175|   3.9%/ 18|   4.5%/ 15|   4.7%/ 15|   4.8%/ 14 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 125   |    7731|     610.106|   0.2%/338|   0.2%/349|   0.2%/352|   0.2%/354 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 125   |    2988|     443.895|   0.4%/191|   0.4%/190|   0.4%/190|   0.4%/191 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 125   |     885|     280.497|   0.7%/ 96|   0.7%/ 95|   0.7%/ 95|   0.7%/ 95 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 125   |     364|     124.973|   1.0%/ 66|   1.1%/ 61|   1.2%/ 59|   1.2%/ 58 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 125   |     750|     167.931|   0.8%/ 90|   0.7%/ 94|   0.7%/ 95|   0.7%/ 96 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 125   |    4020|     864.764|   0.8%/ 86|   0.9%/ 78|   0.9%/ 77|   0.9%/ 75 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 125   |     124|      92.080|   0.4%/166|   0.4%/168|   0.4%/168|   0.4%/168 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 125   |    3522|     582.560|   0.3%/241|   0.3%/234|   0.3%/232|   0.3%/231 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 125   |    8650|    1244.651|   0.2%/388|   0.2%/388|   0.2%/388|   0.2%/387 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 125   |    6465|     647.395|   0.1%/650|   0.1%/681|   0.1%/685|   0.1%/689 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 125   |    1656|     293.656|   0.3%/212|   0.3%/212|   0.3%/212|   0.3%/212 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 125   |    1705|     573.029|   1.7%/ 41|   1.8%/ 38|   1.9%/ 37|   1.9%/ 36 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 125   |    1287|     209.746|   0.8%/ 89|   0.8%/ 85|   0.8%/ 84|   0.8%/ 83 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 125   |      63|      59.282|   3.7%/ 18|   4.1%/ 17|   4.1%/ 17|   4.2%/ 16 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 125   |     335|     173.187|   0.6%/115|   0.5%/131|   0.5%/136|   0.5%/141 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 125   |     850|     275.905|   1.7%/ 41|   1.8%/ 39|   1.8%/ 39|   1.8%/ 38 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 125   |     419|     307.811|   0.3%/221|   0.3%/224|   0.3%/225|   0.3%/226 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 125   |   15872|    1786.983|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 125   |     659|     314.117|   0.9%/ 76|   0.9%/ 74|   0.9%/ 73|   0.9%/ 73 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 125   |   32743|    1683.134|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 125   |    2021|     192.707|   1.3%/ 52|   1.4%/ 50|   1.4%/ 50|   1.4%/ 49 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 125   |     106|     139.244|   0.9%/ 81|   0.8%/ 87|   0.8%/ 89|   0.8%/ 91 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 125   |    3540|     302.861|   0.8%/ 88|   0.9%/ 81|   0.9%/ 80|   0.9%/ 78 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 125   |     555|     140.355|   1.4%/ 50|   1.5%/ 47|   1.5%/ 47|   1.5%/ 46 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 125   |     332|      78.602|   1.6%/ 44|   1.6%/ 42|   1.6%/ 42|   1.6%/ 42 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 125   |    7247|     566.105|   0.2%/358|   0.2%/405|   0.2%/419|   0.2%/433 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 125   |     229|      71.597|   1.8%/ 39|   2.0%/ 35|   2.0%/ 34|   2.1%/ 33 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 125   |    1012|     955.283|   0.1%/686|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 125   |    1863|     361.753|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24|   2.8%/ 24 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 125   |     134|     151.925|   1.1%/ 64|   1.1%/ 61|   1.2%/ 60|   1.2%/ 59 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 125   |    1110|     162.425|   1.7%/ 41|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 125   |    7227|     249.258|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 125   |  155646|     472.306|   0.7%/ 99|   0.7%/ 94|   0.7%/ 93|   0.8%/ 92 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 125   |     319|      99.427|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43|   1.6%/ 43 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 125   |      57|      90.940|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 125   |    2197|     257.425|   0.7%/101|   0.8%/ 86|   0.8%/ 83|   0.9%/ 79 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 125   |    1597|     209.748|   0.7%/100|   0.7%/ 93|   0.8%/ 91|   0.8%/ 89 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 125   |     116|      64.479|   1.2%/ 59|   1.4%/ 48|   1.5%/ 46|   1.6%/ 44 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 125   |     948|     162.880|   0.8%/ 85|   0.9%/ 75|   0.9%/ 73|   1.0%/ 71 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 113   |      27|      46.229|   0.6%/116|   0.4%/156|   0.4%/169|   0.4%/184 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 125   |    1332|      41.343|   0.7%/102|   0.3%/258|   0.2%/419|   0.1%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 125   |     172|      60.427|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25|   2.8%/ 25 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 125   |    1244|      28.925|   0.9%/ 74|   0.9%/ 74|   0.9%/ 74|   0.9%/ 74 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 125   |      57|       1.842|   6.4%/ 11|   4.0%/ 17|   2.5%/ 27|   3.7%/ 19 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 125   |    3862|      85.945|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 125   |     775|     262.030|   1.2%/ 60|   0.9%/ 75|   0.9%/ 80|   0.8%/ 86 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 125   |     224|       8.715|   4.5%/ 15|   5.4%/ 13|   5.7%/ 12|   5.9%/ 12 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 125   |     718|      80.630|   0.1%/906|   0.1%/793|   0.1%/765|   0.1%/738 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 125   |     479|      47.595|   1.8%/ 39|   1.5%/ 45|   1.5%/ 47|   1.4%/ 49 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 125   |     154|      99.546|   1.1%/ 61|   0.8%/ 83|   0.8%/ 92|   0.7%/102 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 125   |    3246|      19.265|   1.3%/ 54|   1.1%/ 61|   1.1%/ 64|   1.0%/ 66 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 125   |     574|      61.046|   0.9%/ 76|   0.8%/ 81|   0.8%/ 83|   0.8%/ 84 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 125   |    9849|     854.639|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 120   |      38|       3.248|   0.8%/ 85|   0.3%/277|   0.1%/635|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 125   |    3218|     280.554|   2.7%/ 25|   2.8%/ 25|   2.8%/ 25|   2.8%/ 25 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 125   |     354|     107.089|   2.1%/ 32|   2.3%/ 30|   2.3%/ 30|   2.3%/ 29 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 125   |       1|       0.428|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 125   |   95802|     453.153|   1.2%/ 58|   1.1%/ 62|   1.1%/ 64|   1.1%/ 65 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 125   |     398|      57.294|   1.8%/ 38|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 125   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 113   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 125   |     397|      14.951|   0.3%/245|   0.2%/402|   0.1%/489|   0.1%/629 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 125   |    9000|     236.840|   0.1%/885|   0.1%/974|   0.1%/996|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  73   |      59|      10.808|   0.4%/157|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  98   |      75|       4.617|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 125   |    9994|     523.071|   0.9%/ 79|   0.8%/ 86|   0.8%/ 88|   0.8%/ 90 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 125   |    4663|       3.325|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 125   |   11053|     223.765|   3.3%/ 21|   3.2%/ 21|   3.2%/ 21|   3.2%/ 21 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 125   |     190|      37.492|   7.3%/  9|   6.7%/ 10|   6.5%/ 11|   6.3%/ 11 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 125   |     150|      36.741|   1.3%/ 52|   1.5%/ 45|   1.6%/ 43|   1.6%/ 42 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 125   |      87|       7.764|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 125   |     616|     105.708|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 125   |    1195|     115.352|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 125   |    5794|     331.682|   0.6%/121|   0.5%/132|   0.5%/135|   0.5%/138 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 125   |    4975|      49.613|   0.9%/ 79|   0.7%/106|   0.6%/115|   0.5%/127 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 125   |     489|      75.416|   2.5%/ 28|   2.2%/ 31|   2.2%/ 32|   2.1%/ 33 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 104   |      72|      53.007|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 121   |     314|       3.179|   4.6%/ 15|   5.1%/ 14|   5.2%/ 13|   5.3%/ 13 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 125   |     329|      59.532|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 125   |   30286|     451.511|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 125   |      50|      23.177|   0.5%/128|   0.7%/106|   0.7%/102|   0.7%/ 98 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 125   |      10|       4.338|   5.9%/ 12|   5.9%/ 12|   5.8%/ 12|   5.8%/ 12 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 122   |      17|       4.605|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 125   |    9157|     110.132|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 125   |     187|       6.179|   1.6%/ 43|   1.7%/ 40|   1.7%/ 40|   1.8%/ 39 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 125   |     208|      19.377|   0.4%/176|   0.5%/148|   0.5%/142|   0.5%/137 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 125   |    2054|     123.733|   2.1%/ 33|   1.9%/ 37|   1.8%/ 38|   1.8%/ 39 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 111   |      47|       3.881|   0.9%/ 77|   0.7%/ 96|   0.7%/104|   0.6%/113 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 100   |      27|      16.566|   0.3%/206|   0.6%/113|   0.7%/101|   0.8%/ 91 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 121   |     167|      14.409|   0.8%/ 89|   0.7%/103|   0.7%/106|   0.6%/110 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 125   |    1430|     156.131|   2.9%/ 24|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 125   |     597|      61.074|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 125   |   39239|      28.826|   2.3%/ 29|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 125   |    5446|      20.405|   1.6%/ 43|   1.4%/ 49|   1.3%/ 51|   1.3%/ 53 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 125   |   17508|     209.988|   1.4%/ 51|   1.3%/ 53|   1.3%/ 53|   1.3%/ 54 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 125   |    5066|     129.475|   1.8%/ 39|   1.5%/ 47|   1.4%/ 50|   1.3%/ 53 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 125   |    1767|     359.071|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 125   |     543|      59.124|   2.0%/ 35|   2.1%/ 33|   2.1%/ 32|   2.1%/ 32 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 125   |   35173|     583.890|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 125   |      10|       3.667|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 125   |    1012|       8.036|   0.2%/341|   0.3%/271|   0.3%/258|   0.3%/246 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 125   |      11|       1.053|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 125   |     889|      47.577|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 125   |     372|       7.812|   3.5%/ 20|   3.8%/ 18|   3.9%/ 18|   4.0%/ 17 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 125   |     245|     136.659|   4.3%/ 16|   4.4%/ 15|   4.5%/ 15|   4.5%/ 15 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 122   |     460|     104.078|   0.8%/ 87|   0.8%/ 83|   0.8%/ 83|   0.8%/ 82 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 123   |    1592|     243.708|   2.3%/ 30|   1.3%/ 52|   1.1%/ 64|   0.8%/ 83 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 123   |      32|      16.628|   0.3%/253|   0.3%/201|   0.4%/189|   0.4%/177 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 125   |      63|       9.291|   3.0%/ 23|   3.6%/ 19|   3.7%/ 19|   3.8%/ 18 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 122   |      81|      17.999|   0.8%/ 91|   0.8%/ 86|   0.8%/ 84|   0.9%/ 81 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 124   |      85|      12.367|   4.2%/ 16|   5.0%/ 14|   5.2%/ 13|   5.4%/ 13 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 125   |      80|      28.718|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  79   |     121|       4.611|   4.7%/ 14|   4.0%/ 17|   3.8%/ 18|   3.6%/ 19 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 125   |     125|       3.817|   0.1%/479|   0.2%/429|   0.2%/418|   0.2%/407 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 125   |     125|       6.152|   0.1%/586|   0.1%/699|   0.1%/744|   0.1%/800 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 125   |     159|      38.936|   0.2%/431|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 125   |   48771|     385.305|   1.4%/ 50|   1.3%/ 54|   1.2%/ 56|   1.2%/ 57 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 125   |     801|     298.701|   1.0%/ 68|   1.0%/ 69|   1.0%/ 69|   1.0%/ 69 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 125   |     354|       9.861|   2.5%/ 28|   2.9%/ 23|   3.1%/ 23|   3.2%/ 22 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  71   |      12|       0.412|   1.2%/ 56|   3.2%/ 22|   3.7%/ 19|   4.3%/ 16 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  25   |      12|       4.830|   4.4%/ 16|   6.1%/ 11|   5.5%/ 12|   5.1%/ 14 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  80   |      58|       1.937|   2.7%/ 26|   3.2%/ 22|   3.3%/ 21|   3.4%/ 21 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 125   |    6168|     353.302|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 125   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 125   |     119|      18.475|   0.9%/ 80|   0.7%/101|   0.6%/109|   0.6%/118 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 125   |      69|       3.098|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 125   |     910|       4.416|   0.8%/ 91|   0.6%/123|   0.5%/135|   0.5%/149 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 125   |     507|     244.039|   1.2%/ 59|   1.0%/ 66|   1.0%/ 68|   1.0%/ 70 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 125   |     256|      47.627|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 125   |     454|      97.368|   1.9%/ 36|   1.4%/ 49|   1.3%/ 54|   1.1%/ 61 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 125   |    6065|      27.652|   0.4%/154|   0.3%/244|   0.2%/284|   0.2%/340 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 125   |    1534|     363.592|   2.1%/ 33|   1.8%/ 37|   1.8%/ 39|   1.7%/ 40 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 125   |      56|       7.804|   3.8%/ 18|   3.8%/ 18|   3.8%/ 18|   3.8%/ 18 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 125   |   20439|     636.105|   1.1%/ 61|   1.0%/ 68|   1.0%/ 70|   1.0%/ 72 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 125   |    2109|      19.437|   1.0%/ 69|   1.0%/ 66|   1.1%/ 66|   1.1%/ 65 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 125   |    1734|      45.185|   0.5%/153|   0.5%/151|   0.5%/150|   0.5%/150 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 125   |    1744|     169.751|   0.2%/355|   0.2%/420|   0.2%/440|   0.2%/461 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 125   |     177|      64.516|   0.8%/ 83|   0.8%/ 87|   0.8%/ 88|   0.8%/ 89 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 125   |    2415|     124.457|   1.3%/ 55|   1.4%/ 51|   1.4%/ 50|   1.4%/ 49 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 125   |   14349|      97.784|   1.0%/ 72|   0.8%/ 82|   0.8%/ 84|   0.8%/ 87 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  66   |       5|       0.404|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 125   |    2995|      87.527|   1.1%/ 62|   0.9%/ 75|   0.9%/ 80|   0.8%/ 85 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 125   |     216|      13.348|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 125   |     611|      87.708|   1.6%/ 43|   1.3%/ 52|   1.3%/ 55|   1.2%/ 58 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 103   |      67|       8.512|   0.2%/363|   0.1%/624|   0.1%/742|   0.1%/910 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 125   |      27|       4.753|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 125   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 125   |     120|      57.264|   0.4%/160|   0.6%/124|   0.6%/117|   0.6%/111 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 118   |      93|       5.853|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 125   |    8868|     150.889|   3.2%/ 21|   3.1%/ 22|   3.1%/ 22|   3.1%/ 23 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 125   |   28453|     604.096|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 125   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 125   |     756|      17.814|   0.7%/104|   0.6%/107|   0.6%/107|   0.6%/108 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 125   |    5770|     558.130|   0.1%/500|   0.1%/704|   0.1%/785|   0.1%/888 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 125   |    1982|     230.407|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 125   |      50|       2.849|   3.6%/ 19|   2.4%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 125   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 125   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 125   |      19|       2.555|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 125   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 125   |      50|       4.302|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 125   |    5749|      69.137|   0.3%/230|   0.3%/241|   0.3%/243|   0.3%/246 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 125   |  155646|     472.306|   0.7%/ 99|   0.7%/ 94|   0.7%/ 93|   0.8%/ 92 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  11   |       5|       0.124|  26.0%/  2|  26.0%/  2|  26.0%/  2|  18.6%/  4 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 125   |    1767|      42.197|   1.1%/ 65|   1.0%/ 66|   1.0%/ 66|   1.0%/ 67 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 125   |     352|      35.603|   0.3%/274|   0.2%/290|   0.2%/293|   0.2%/297 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 125   |   46364|     697.877|   0.1%/499|   0.1%/523|   0.1%/529|   0.1%/535 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 125   |      36|      10.287|   0.6%/114|   0.5%/147|   0.4%/158|   0.4%/172 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 125   |     161|       4.723|   4.1%/ 17|   3.7%/ 19|   3.6%/ 19|   3.5%/ 20 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 125   |     181|       5.625|   3.1%/ 22|   2.9%/ 23|   2.9%/ 24|   2.9%/ 24 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 124   |     187|      10.469|   0.7%/ 97|   4.2%/ 16|   4.5%/ 15|   4.2%/ 16 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 125   |      67|       4.396|   8.6%/  8|   9.8%/  7|  10.1%/  7|  10.5%/  6 |

