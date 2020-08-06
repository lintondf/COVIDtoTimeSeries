# State and Country COVID-19 Analysis #
## Updated: at 2020-08-06 for data as of 2020-08-05 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 36.6% of deaths and 40.0% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 68.5% of deaths and 55.6% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 127   |   32764|    1684.193|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 127   |   15876|    1787.439|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 127   |    9782|     247.578|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 127   |    8675|    1248.302|   0.2%/421|   0.2%/440|   0.2%/444|   0.2%/450 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 127   |    7764|     612.662|   0.2%/336|   0.2%/341|   0.2%/342|   0.2%/343 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 127   |    7756|     267.498|   3.3%/ 21|   3.3%/ 21|   3.2%/ 21|   3.2%/ 21 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 127   |    7591|     353.439|   2.4%/ 28|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 127   |    7269|     567.827|   0.2%/385|   0.2%/442|   0.2%/459|   0.1%/478 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 127   |    6478|     648.668|   0.1%/670|   0.1%/693|   0.1%/697|   0.1%/701 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 127   |    4443|    1246.212|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 127   |  157949|     479.296|   0.7%/101|   0.7%/ 98|   0.7%/ 97|   0.7%/ 96 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 127   |   97752|     462.377|   1.1%/ 61|   1.0%/ 66|   1.0%/ 68|   1.0%/ 69 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 127   |   49950|     394.616|   1.3%/ 52|   1.2%/ 57|   1.2%/ 58|   1.2%/ 60 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 127   |   46436|     698.962|   0.1%/606|   0.1%/716|   0.1%/751|   0.1%/791 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 127   |   40962|      30.092|   2.3%/ 30|   2.2%/ 31|   2.2%/ 31|   2.2%/ 31 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 127   |   35184|     584.085|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 127   |   30300|     451.728|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 127   |   28472|     604.491|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 127   |   20970|     652.633|   1.2%/ 59|   1.1%/ 63|   1.1%/ 64|   1.1%/ 65 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 127   |   17943|     215.203|   1.3%/ 52|   1.3%/ 55|   1.2%/ 55|   1.2%/ 56 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 127   |    1712|     349.118|   1.5%/ 46|   1.4%/ 50|   1.3%/ 52|   1.3%/ 53 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 127   |      25|      34.680|   2.6%/ 27|   3.1%/ 22|   3.3%/ 21|   3.4%/ 20 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 127   |    4068|     558.895|   2.0%/ 35|   1.6%/ 44|   1.5%/ 47|   1.4%/ 50 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 127   |     495|     163.981|   2.0%/ 34|   2.2%/ 32|   2.2%/ 31|   2.2%/ 31 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 127   |    9782|     247.578|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 127   |    1858|     322.624|   0.3%/229|   0.3%/231|   0.3%/233|   0.3%/234 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 127   |    4443|    1246.212|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 127   |     601|     616.972|   0.1%/466|   0.1%/493|   0.1%/501|   0.1%/510 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 127   |    7591|     353.439|   2.4%/ 28|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 127   |    3968|     373.753|   1.3%/ 54|   1.3%/ 52|   1.4%/ 51|   1.4%/ 50 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 127   |      27|      19.209|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 127   |     216|     120.793|   2.9%/ 24|   3.2%/ 22|   3.3%/ 21|   3.3%/ 21 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 127   |    7764|     612.662|   0.2%/336|   0.2%/341|   0.2%/342|   0.2%/343 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 127   |    3010|     447.047|   0.4%/196|   0.3%/198|   0.3%/199|   0.3%/201 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 127   |     898|     284.544|   0.7%/ 97|   0.7%/ 97|   0.7%/ 97|   0.7%/ 97 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 127   |     372|     127.845|   1.0%/ 69|   1.1%/ 65|   1.1%/ 64|   1.1%/ 63 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 127   |     760|     170.014|   0.7%/ 98|   0.7%/106|   0.6%/109|   0.6%/112 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 127   |    4090|     879.804|   0.8%/ 88|   0.8%/ 81|   0.9%/ 80|   0.9%/ 79 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 127   |     124|      92.578|   0.4%/189|   0.3%/204|   0.3%/208|   0.3%/213 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 127   |    3541|     585.692|   0.3%/252|   0.3%/251|   0.3%/251|   0.3%/251 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 127   |    8675|    1248.302|   0.2%/421|   0.2%/440|   0.2%/444|   0.2%/450 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 127   |    6478|     648.668|   0.1%/670|   0.1%/693|   0.1%/697|   0.1%/701 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 127   |    1667|     295.567|   0.3%/215|   0.3%/216|   0.3%/216|   0.3%/216 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 127   |    1773|     595.858|   1.7%/ 42|   1.8%/ 39|   1.8%/ 38|   1.8%/ 38 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 127   |    1306|     212.715|   0.7%/ 96|   0.7%/ 96|   0.7%/ 97|   0.7%/ 97 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 127   |      67|      62.745|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 127   |     338|     174.921|   0.5%/127|   0.5%/150|   0.4%/157|   0.4%/166 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 127   |     882|     286.295|   1.7%/ 40|   1.8%/ 39|   1.8%/ 39|   1.8%/ 38 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 127   |     420|     309.196|   0.3%/251|   0.3%/275|   0.2%/283|   0.2%/292 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 127   |   15876|    1787.439|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 127   |     669|     319.134|   0.8%/ 82|   0.8%/ 83|   0.8%/ 84|   0.8%/ 85 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 127   |   32764|    1684.193|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 127   |    2079|     198.233|   1.4%/ 50|   1.4%/ 48|   1.4%/ 48|   1.5%/ 47 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 127   |     108|     141.744|   0.9%/ 78|   0.9%/ 81|   0.8%/ 81|   0.8%/ 82 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 127   |    3597|     307.759|   0.8%/ 92|   0.8%/ 88|   0.8%/ 87|   0.8%/ 86 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 127   |     574|     145.126|   1.4%/ 49|   1.5%/ 47|   1.5%/ 46|   1.5%/ 45 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 127   |     341|      80.905|   1.4%/ 49|   1.4%/ 50|   1.4%/ 51|   1.4%/ 51 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 127   |    7269|     567.827|   0.2%/385|   0.2%/442|   0.2%/459|   0.1%/478 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 127   |     239|      74.811|   1.8%/ 37|   2.0%/ 34|   2.1%/ 33|   2.2%/ 32 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 127   |    1013|     956.584|   0.1%/663|   0.1%/869|   0.1%/941|   0.1%/ *** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 127   |    1954|     379.453|   2.7%/ 26|   2.5%/ 27|   2.5%/ 28|   2.4%/ 28 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 127   |     137|     154.920|   1.0%/ 70|   1.0%/ 70|   1.0%/ 69|   1.0%/ 69 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 127   |    1146|     167.755|   1.7%/ 41|   1.6%/ 43|   1.6%/ 43|   1.6%/ 44 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 127   |    7756|     267.498|   3.3%/ 21|   3.3%/ 21|   3.2%/ 21|   3.2%/ 21 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 127   |  157949|     479.296|   0.7%/101|   0.7%/ 98|   0.7%/ 97|   0.7%/ 96 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 127   |     329|     102.538|   1.6%/ 42|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 127   |      57|      91.287|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 127   |    2239|     262.374|   0.7%/100|   0.8%/ 87|   0.8%/ 84|   0.9%/ 81 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 127   |    1623|     213.183|   0.7%/103|   0.7%/ 98|   0.7%/ 97|   0.7%/ 96 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 127   |     120|      67.087|   1.4%/ 49|   1.7%/ 40|   1.8%/ 38|   1.9%/ 36 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 127   |     966|     165.924|   0.8%/ 87|   0.9%/ 80|   0.9%/ 79|   0.9%/ 78 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 115   |      27|      46.699|   0.7%/ 97|   0.7%/100|   0.7%/ 99|   0.7%/ 99 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 127   |    1329|      41.251|   0.5%/131|   0.1%/484|   0.0%/ ***|   0.0%/ -- |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 127   |     182|      63.923|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 127   |    1265|      29.421|   0.9%/ 77|   0.9%/ 79|   0.9%/ 79|   0.9%/ 80 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 127   |      63|       2.010|   4.4%/ 15|   4.7%/ 15|   4.8%/ 14|   4.8%/ 14 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 127   |    4124|      91.779|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 127   |     786|     265.605|   1.0%/ 66|   0.8%/ 84|   0.8%/ 91|   0.7%/ 98 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 127   |     245|       9.535|   4.6%/ 15|   5.4%/ 13|   5.6%/ 12|   5.8%/ 12 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 127   |     719|      80.772|   0.1%/965|   0.1%/879|   0.1%/860|   0.1%/841 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 127   |     491|      48.746|   1.6%/ 43|   1.4%/ 51|   1.3%/ 53|   1.2%/ 56 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 127   |     156|     100.934|   1.1%/ 63|   0.9%/ 81|   0.8%/ 87|   0.7%/ 94 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 127   |    3311|      19.654|   1.2%/ 56|   1.1%/ 64|   1.0%/ 66|   1.0%/ 69 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 127   |     583|      61.920|   0.8%/ 82|   0.8%/ 90|   0.8%/ 92|   0.7%/ 94 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 127   |    9856|     855.267|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 122   |      39|       3.288|   0.6%/120|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 127   |    3396|     296.054|   2.7%/ 25|   2.7%/ 25|   2.7%/ 25|   2.7%/ 25 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 127   |     375|     113.745|   2.3%/ 30|   2.5%/ 27|   2.6%/ 27|   2.6%/ 26 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 127   |       1|       0.428|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 127   |   97752|     462.377|   1.1%/ 61|   1.0%/ 66|   1.0%/ 68|   1.0%/ 69 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 127   |     417|      59.951|   2.0%/ 34|   2.2%/ 32|   2.2%/ 31|   2.3%/ 31 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 127   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 115   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 127   |     397|      14.943|   0.2%/331|   0.1%/877|   0.0%/ ***|   0.0%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 127   |    9012|     237.176|   0.1%/908|   0.1%/977|   0.1%/994|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  75   |      59|      10.756|   0.3%/275|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 100   |      75|       4.617|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 127   |   10055|     526.253|   0.8%/ 83|   0.8%/ 91|   0.7%/ 93|   0.7%/ 96 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 127   |    4647|       3.314|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 127   |   11756|     237.997|   3.2%/ 21|   3.2%/ 22|   3.2%/ 22|   3.1%/ 22 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 127   |     211|      41.620|   6.9%/ 10|   6.1%/ 11|   5.8%/ 12|   5.6%/ 12 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 127   |     155|      37.908|   1.4%/ 49|   1.6%/ 43|   1.6%/ 42|   1.7%/ 41 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 127   |      87|       7.789|   0.1%/ ***|   0.1%/780|   0.1%/717|   0.1%/661 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 127   |     616|     105.821|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 127   |    1227|     118.491|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 127   |    5853|     335.089|   0.6%/124|   0.5%/134|   0.5%/137|   0.5%/139 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 127   |    5018|      50.043|   0.8%/ 89|   0.6%/124|   0.5%/137|   0.5%/152 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 127   |     508|      78.335|   2.4%/ 29|   2.1%/ 33|   2.0%/ 34|   1.9%/ 35 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 106   |      82|      60.407|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 123   |     348|       3.530|   4.9%/ 14|   5.3%/ 13|   5.4%/ 13|   5.6%/ 12 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 127   |     330|      59.666|   0.0%/ ***|   0.1%/987|   0.1%/914|   0.1%/851 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 127   |   30300|     451.728|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 127   |      51|      23.490|   0.6%/119|   0.7%/102|   0.7%/ 99|   0.7%/ 96 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 127   |      13|       5.463|   8.2%/  8|   9.3%/  7|   9.6%/  7|   9.8%/  7 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 124   |      17|       4.641|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 127   |    9168|     110.265|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 127   |     195|       6.425|   1.8%/ 39|   1.9%/ 36|   1.9%/ 35|   2.0%/ 35 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 127   |     210|      19.558|   0.4%/172|   0.5%/150|   0.5%/145|   0.5%/141 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 127   |    2117|     127.474|   1.9%/ 36|   1.7%/ 42|   1.6%/ 43|   1.5%/ 45 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 113   |      49|       3.978|   1.1%/ 65|   1.0%/ 69|   1.0%/ 71|   1.0%/ 72 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 102   |      27|      16.749|   0.3%/219|   0.5%/141|   0.5%/128|   0.6%/118 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 123   |     169|      14.612|   0.8%/ 91|   0.7%/100|   0.7%/102|   0.7%/104 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 127   |    1492|     162.867|   2.5%/ 27|   2.4%/ 29|   2.3%/ 30|   2.2%/ 31 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 127   |     597|      61.136|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 127   |   40962|      30.092|   2.3%/ 30|   2.2%/ 31|   2.2%/ 31|   2.2%/ 31 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 127   |    5574|      20.882|   1.5%/ 46|   1.3%/ 53|   1.2%/ 55|   1.2%/ 58 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 127   |   17943|     215.203|   1.3%/ 52|   1.3%/ 55|   1.2%/ 55|   1.2%/ 56 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 127   |    5194|     132.747|   1.7%/ 41|   1.4%/ 50|   1.3%/ 52|   1.3%/ 55 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 127   |    1767|     358.985|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 127   |     566|      61.620|   2.0%/ 34|   2.1%/ 33|   2.1%/ 33|   2.1%/ 33 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 127   |   35184|     584.085|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 127   |      10|       3.667|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 127   |    1020|       8.096|   0.3%/274|   0.3%/217|   0.3%/206|   0.4%/196 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 127   |      11|       1.047|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 127   |    1016|      54.394|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 127   |     396|       8.328|   3.3%/ 21|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 127   |     276|     153.544|   4.6%/ 15|   4.8%/ 14|   4.9%/ 14|   5.0%/ 14 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 124   |     468|     105.823|   0.8%/ 85|   0.8%/ 82|   0.8%/ 82|   0.9%/ 81 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 125   |    1673|     256.100|   1.8%/ 37|   0.9%/ 80|   0.6%/112|   0.4%/189 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 125   |      32|      16.731|   0.2%/294|   0.3%/242|   0.3%/230|   0.3%/218 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 127   |      67|       9.886|   2.9%/ 23|   3.3%/ 21|   3.4%/ 20|   3.5%/ 20 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 124   |      81|      18.168|   0.8%/ 86|   0.9%/ 76|   0.9%/ 73|   1.0%/ 70 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 126   |      95|      13.785|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.5%/ 20 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 127   |      80|      28.760|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  81   |     130|       4.946|   4.6%/ 15|   3.9%/ 18|   3.7%/ 19|   3.5%/ 20 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 127   |     125|       3.825|   0.1%/592|   0.1%/599|   0.1%/602|   0.1%/606 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 127   |     125|       6.156|   0.1%/742|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 127   |     158|      38.851|   0.1%/635|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 127   |   49950|     394.616|   1.3%/ 52|   1.2%/ 57|   1.2%/ 58|   1.2%/ 60 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 127   |     818|     305.207|   1.0%/ 67|   1.0%/ 66|   1.0%/ 66|   1.0%/ 66 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 127   |     372|      10.363|   2.9%/ 23|   3.5%/ 19|   3.7%/ 19|   3.9%/ 18 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  73   |      14|       0.476|   2.2%/ 31|   5.1%/ 14|   5.8%/ 12|   6.7%/ 10 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  27   |      12|       4.947|   6.4%/ 11|   4.4%/ 16|   3.7%/ 19|   2.9%/ 24 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  82   |      61|       2.026|   2.6%/ 27|   2.4%/ 29|   2.3%/ 29|   2.3%/ 31 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 127   |    6170|     353.465|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 127   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 127   |     122|      18.941|   1.0%/ 66|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 127   |      69|       3.096|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 127   |     924|       4.482|   0.8%/ 85|   0.7%/ 99|   0.7%/103|   0.6%/108 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 127   |     516|     248.415|   1.1%/ 63|   1.0%/ 72|   0.9%/ 74|   0.9%/ 77 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 127   |     256|      47.654|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 127   |     471|     100.958|   1.8%/ 39|   1.3%/ 53|   1.2%/ 58|   1.1%/ 65 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 127   |    6083|      27.732|   0.4%/179|   0.2%/292|   0.2%/346|   0.2%/423 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 127   |    1583|     375.175|   2.0%/ 35|   1.7%/ 40|   1.7%/ 41|   1.6%/ 43 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  10   |       2|       0.224|  26.0%/  2|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 127   |      61|       8.464|   4.0%/ 17|   4.0%/ 17|   4.0%/ 17|   4.0%/ 17 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 127   |   20970|     652.633|   1.2%/ 59|   1.1%/ 63|   1.1%/ 64|   1.1%/ 65 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 127   |    2149|      19.801|   1.0%/ 67|   1.1%/ 64|   1.1%/ 63|   1.1%/ 62 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 127   |    1750|      45.606|   0.4%/155|   0.4%/154|   0.4%/154|   0.4%/154 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 127   |    1748|     170.079|   0.2%/430|   0.1%/570|   0.1%/621|   0.1%/683 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 127   |     179|      65.304|   0.7%/ 92|   0.7%/101|   0.7%/104|   0.7%/106 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 127   |    2488|     128.199|   1.3%/ 53|   1.4%/ 49|   1.4%/ 48|   1.5%/ 47 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 127   |   14567|      99.268|   0.9%/ 76|   0.8%/ 86|   0.8%/ 89|   0.7%/ 92 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  68   |       5|       0.404|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 127   |    3047|      89.041|   1.1%/ 63|   0.9%/ 75|   0.9%/ 78|   0.8%/ 82 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 127   |     222|      13.681|   1.5%/ 46|   1.3%/ 52|   1.3%/ 53|   1.2%/ 55 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 127   |     624|      89.600|   1.5%/ 45|   1.3%/ 54|   1.2%/ 57|   1.1%/ 60 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 105   |      67|       8.519|   0.1%/491|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 127   |      27|       4.744|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 127   |      28|       5.132|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 127   |     122|      58.219|   0.6%/119|   0.7%/ 93|   0.8%/ 88|   0.8%/ 83 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 120   |      93|       5.852|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 127   |    9421|     160.290|   3.2%/ 21|   3.1%/ 22|   3.1%/ 22|   3.0%/ 23 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 127   |   28472|     604.491|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 127   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 127   |     765|      18.037|   0.6%/110|   0.6%/116|   0.6%/117|   0.6%/118 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 127   |    5777|     558.748|   0.1%/589|   0.1%/900|   0.1%/ ***|   0.1%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 127   |    1984|     230.551|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 127   |      51|       2.930|   0.8%/ 84|   2.3%/ 30|   2.3%/ 30|   2.9%/ 23 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 127   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 127   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 127   |      20|       2.651|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 127   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 127   |      51|       4.329|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 127   |    5783|      69.545|   0.3%/228|   0.3%/234|   0.3%/236|   0.3%/237 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 127   |  157949|     479.296|   0.7%/101|   0.7%/ 98|   0.7%/ 97|   0.7%/ 96 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  13   |       5|       0.124|   0.0%/ --|  18.6%/  4|   7.7%/  9|   7.7%/  9 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 127   |    1807|      43.141|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 127   |     353|      35.733|   0.2%/313|   0.2%/351|   0.2%/362|   0.2%/374 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 127   |   46436|     698.962|   0.1%/606|   0.1%/716|   0.1%/751|   0.1%/791 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 127   |      37|      10.450|   0.7%/ 96|   0.7%/102|   0.7%/103|   0.7%/104 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 127   |     173|       5.073|   4.0%/ 17|   3.7%/ 18|   3.6%/ 19|   3.6%/ 19 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 127   |     193|       5.990|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 126   |     184|      10.297|   1.7%/ 42|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 127   |      82|       5.389|   8.2%/  8|   9.1%/  7|   9.3%/  7|   9.6%/  7 |

