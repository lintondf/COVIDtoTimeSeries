# State and Country COVID-19 Analysis #
## Updated: at 2020-08-09 for data as of 2020-08-08 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 37.1% of deaths and 40.0% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 68.3% of deaths and 55.4% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 130   |   32791|    1685.594|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 130   |   15883|    1788.232|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 130   |   10250|     259.406|   1.5%/ 46|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 130   |    8974|     309.498|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 130   |    8721|    1254.861|   0.2%/398|   0.2%/397|   0.2%/396|   0.2%/396 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 130   |    8159|     379.866|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 130   |    7823|     617.364|   0.2%/294|   0.2%/278|   0.3%/274|   0.3%/270 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 130   |    7310|     571.009|   0.2%/357|   0.2%/371|   0.2%/374|   0.2%/377 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 130   |    6510|     651.873|   0.1%/500|   0.2%/443|   0.2%/430|   0.2%/417 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 130   |    4446|    1247.053|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 130   |  161858|     491.157|   0.8%/ 91|   0.8%/ 85|   0.8%/ 84|   0.8%/ 83 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 130   |  100935|     477.434|   1.1%/ 60|   1.1%/ 64|   1.1%/ 64|   1.1%/ 65 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 130   |   51985|     410.694|   1.4%/ 50|   1.3%/ 51|   1.3%/ 52|   1.3%/ 52 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 130   |   46656|     702.271|   0.1%/518|   0.1%/534|   0.1%/538|   0.1%/542 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 130   |   43668|      32.080|   2.3%/ 31|   2.2%/ 32|   2.2%/ 32|   2.1%/ 32 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 130   |   35203|     584.399|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 130   |   30326|     452.121|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 130   |   28494|     604.973|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 130   |   21943|     682.913|   1.1%/ 64|   1.0%/ 68|   1.0%/ 70|   1.0%/ 71 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 130   |   18623|     223.358|   1.2%/ 56|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 130   |    1778|     362.619|   1.4%/ 48|   1.3%/ 53|   1.3%/ 54|   1.2%/ 56 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 130   |      27|      36.295|   1.1%/ 60|   1.4%/ 48|   1.5%/ 46|   1.6%/ 44 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 130   |    4239|     582.387|   1.9%/ 37|   1.5%/ 45|   1.5%/ 47|   1.4%/ 50 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 130   |     529|     175.430|   2.1%/ 33|   2.2%/ 31|   2.2%/ 31|   2.3%/ 30 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 130   |   10250|     259.406|   1.5%/ 46|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 130   |    1869|     324.601|   0.3%/274|   0.2%/316|   0.2%/330|   0.2%/347 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 130   |    4446|    1247.053|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 130   |     603|     619.123|   0.1%/508|   0.1%/564|   0.1%/580|   0.1%/598 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 130   |    8159|     379.866|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 130   |    4145|     390.360|   1.4%/ 50|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 130   |      28|      19.671|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 130   |     238|     133.384|   3.0%/ 23|   3.1%/ 22|   3.2%/ 22|   3.2%/ 21 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 130   |    7823|     617.364|   0.2%/294|   0.2%/278|   0.3%/274|   0.3%/270 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 130   |    3039|     451.419|   0.3%/202|   0.3%/209|   0.3%/211|   0.3%/213 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 130   |     921|     291.896|   0.8%/ 87|   0.8%/ 83|   0.8%/ 81|   0.9%/ 80 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 130   |     384|     131.878|   0.9%/ 73|   1.0%/ 72|   1.0%/ 72|   1.0%/ 72 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 130   |     774|     173.260|   0.7%/ 99|   0.7%/106|   0.6%/108|   0.6%/110 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 130   |    4208|     905.168|   0.9%/ 78|   1.0%/ 73|   1.0%/ 71|   1.0%/ 70 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 130   |     125|      93.271|   0.3%/222|   0.3%/257|   0.3%/268|   0.2%/281 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 130   |    3573|     590.968|   0.3%/239|   0.3%/233|   0.3%/232|   0.3%/230 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 130   |    8721|    1254.861|   0.2%/398|   0.2%/397|   0.2%/396|   0.2%/396 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 130   |    6510|     651.873|   0.1%/500|   0.2%/443|   0.2%/430|   0.2%/417 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 130   |    1685|     298.810|   0.3%/201|   0.4%/194|   0.4%/191|   0.4%/189 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 130   |    1873|     629.283|   1.7%/ 41|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 130   |    1333|     217.129|   0.7%/ 95|   0.7%/ 98|   0.7%/ 99|   0.7%/100 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 130   |      73|      68.758|   3.2%/ 21|   3.2%/ 22|   3.2%/ 22|   3.2%/ 22 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 130   |     345|     178.229|   0.6%/108|   0.6%/110|   0.6%/111|   0.6%/111 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 130   |     935|     303.433|   1.9%/ 37|   2.0%/ 35|   2.0%/ 35|   2.0%/ 34 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 130   |     422|     310.582|   0.2%/313|   0.2%/407|   0.2%/444|   0.1%/489 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 130   |   15883|    1788.232|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 130   |     684|     326.293|   0.8%/ 85|   0.8%/ 90|   0.8%/ 91|   0.7%/ 93 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 130   |   32791|    1685.594|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 130   |    2174|     207.298|   1.4%/ 49|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 130   |     111|     145.790|   0.9%/ 73|   0.9%/ 74|   0.9%/ 74|   0.9%/ 74 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 130   |    3679|     314.721|   0.7%/ 93|   0.8%/ 92|   0.8%/ 92|   0.8%/ 92 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 130   |     604|     152.574|   1.5%/ 45|   1.6%/ 42|   1.7%/ 42|   1.7%/ 41 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 130   |     356|      84.344|   1.4%/ 49|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 130   |    7310|     571.009|   0.2%/357|   0.2%/371|   0.2%/374|   0.2%/377 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 130   |     255|      79.785|   2.4%/ 29|   2.8%/ 25|   2.9%/ 24|   3.0%/ 23 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 130   |    1016|     958.808|   0.1%/705|   0.1%/861|   0.1%/908|   0.1%/958 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 130   |    2080|     404.038|   2.5%/ 28|   2.2%/ 31|   2.2%/ 32|   2.1%/ 33 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 130   |     143|     161.745|   1.2%/ 56|   1.4%/ 49|   1.4%/ 48|   1.5%/ 46 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 130   |    1215|     177.781|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 130   |    8974|     309.498|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 130   |  161858|     491.157|   0.8%/ 91|   0.8%/ 85|   0.8%/ 84|   0.8%/ 83 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 130   |     342|     106.817|   1.5%/ 45|   1.4%/ 49|   1.4%/ 50|   1.4%/ 51 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 130   |      58|      92.317|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 130   |    2307|     270.307|   0.8%/ 85|   0.9%/ 73|   1.0%/ 71|   1.0%/ 68 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 130   |    1670|     219.321|   0.8%/ 84|   0.9%/ 75|   0.9%/ 73|   1.0%/ 71 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 130   |     127|      70.953|   1.5%/ 45|   1.8%/ 38|   1.9%/ 37|   1.9%/ 35 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 130   |     993|     170.564|   0.8%/ 82|   0.9%/ 76|   0.9%/ 75|   0.9%/ 74 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 118   |      28|      47.830|   0.8%/ 91|   0.8%/ 83|   0.9%/ 81|   0.9%/ 79 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 130   |    1332|      41.321|   0.4%/167|   0.1%/506|   0.1%/978|   0.0%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 130   |     197|      69.167|   2.8%/ 25|   2.7%/ 26|   2.7%/ 26|   2.6%/ 26 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 130   |    1297|      30.173|   0.9%/ 78|   0.9%/ 80|   0.9%/ 81|   0.8%/ 82 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 130   |      71|       2.276|   4.4%/ 16|   3.8%/ 18|   3.7%/ 19|   3.5%/ 20 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 130   |    4548|     101.204|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 130   |     799|     270.041|   0.8%/ 82|   0.6%/113|   0.6%/125|   0.5%/140 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 130   |     285|      11.094|   4.5%/ 15|   5.0%/ 14|   5.2%/ 13|   5.3%/ 13 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 130   |     721|      80.960|   0.1%/975|   0.1%/915|   0.1%/905|   0.1%/896 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 130   |     505|      50.145|   1.3%/ 52|   1.0%/ 68|   0.9%/ 74|   0.8%/ 82 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 130   |     161|     104.093|   1.2%/ 59|   1.1%/ 65|   1.0%/ 66|   1.0%/ 67 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 130   |    3408|      20.230|   1.2%/ 60|   1.0%/ 68|   1.0%/ 70|   0.9%/ 73 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 130   |     593|      63.045|   0.7%/ 94|   0.6%/110|   0.6%/115|   0.6%/120 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 130   |    9868|     856.253|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 125   |      39|       3.327|   0.5%/128|   0.2%/428|   0.1%/ ***|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 130   |    3652|     318.421|   2.6%/ 27|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 130   |     403|     121.962|   2.1%/ 33|   2.2%/ 32|   2.2%/ 31|   2.2%/ 31 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 130   |       1|       0.428|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 130   |  100935|     477.434|   1.1%/ 60|   1.1%/ 64|   1.1%/ 64|   1.1%/ 65 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 130   |     445|      64.051|   2.1%/ 33|   2.2%/ 32|   2.2%/ 31|   2.2%/ 31 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 130   |      54|       2.574|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 118   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 130   |     396|      14.936|   0.1%/483|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 130   |    9029|     237.620|   0.1%/990|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  78   |      59|      10.737|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 103   |      76|       4.652|   0.1%/600|   0.2%/342|   0.2%/306|   0.3%/276 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 130   |   10178|     532.692|   0.8%/ 88|   0.7%/ 97|   0.7%/ 99|   0.7%/102 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 130   |    4681|       3.338|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 130   |   12814|     259.419|   3.0%/ 23|   2.9%/ 23|   2.9%/ 24|   2.9%/ 24 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 130   |     245|      48.355|   6.3%/ 11|   5.7%/ 12|   5.5%/ 12|   5.3%/ 13 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 130   |     160|      39.199|   1.2%/ 58|   1.2%/ 59|   1.2%/ 60|   1.1%/ 60 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 130   |      88|       7.826|   0.1%/786|   0.1%/559|   0.1%/518|   0.1%/482 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 130   |     617|     106.003|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 130   |    1281|     123.639|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 130   |    5941|     340.115|   0.5%/129|   0.5%/137|   0.5%/139|   0.5%/141 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 130   |    5077|      50.629|   0.6%/108|   0.4%/155|   0.4%/174|   0.4%/197 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 130   |     540|      83.284|   2.3%/ 30|   2.1%/ 33|   2.1%/ 34|   2.0%/ 34 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 109   |      90|      66.396|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 126   |     398|       4.033|   4.5%/ 15|   4.5%/ 15|   4.5%/ 15|   4.6%/ 15 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 130   |     331|      59.824|   0.1%/ ***|   0.1%/947|   0.1%/892|   0.1%/844 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 130   |   30326|     452.121|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 130   |      52|      23.760|   0.4%/160|   0.4%/171|   0.4%/175|   0.4%/179 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 130   |      17|       7.453|   4.0%/ 17|  21.1%/  3|  10.7%/  6|   5.9%/ 12 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 127   |      17|       4.663|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 130   |    9189|     110.517|   0.1%/ ***|   0.1%/953|   0.1%/922|   0.1%/893 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 130   |     206|       6.800|   1.8%/ 39|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 130   |     212|      19.751|   0.3%/209|   0.3%/204|   0.3%/204|   0.3%/203 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 130   |    2225|     133.996|   1.9%/ 37|   1.7%/ 40|   1.7%/ 41|   1.6%/ 42 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 116   |      50|       4.112|   1.1%/ 60|   1.1%/ 62|   1.1%/ 63|   1.1%/ 63 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 105   |      28|      17.147|   0.5%/149|   0.7%/ 99|   0.8%/ 92|   0.8%/ 85 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 126   |     175|      15.157|   1.0%/ 67|   1.2%/ 59|   1.2%/ 57|   1.2%/ 56 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 130   |    1565|     170.846|   2.1%/ 32|   1.8%/ 39|   1.6%/ 42|   1.5%/ 45 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 130   |     600|      61.351|   0.1%/923|   0.1%/659|   0.1%/611|   0.1%/568 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 130   |   43668|      32.080|   2.3%/ 31|   2.2%/ 32|   2.2%/ 32|   2.1%/ 32 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 130   |    5760|      21.581|   1.4%/ 50|   1.2%/ 58|   1.1%/ 61|   1.1%/ 64 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 130   |   18623|     223.358|   1.2%/ 56|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 130   |    5396|     137.900|   1.6%/ 44|   1.3%/ 52|   1.3%/ 54|   1.2%/ 56 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 130   |    1770|     359.570|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 130   |     598|      65.046|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 130   |   35203|     584.399|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 130   |      13|       4.638|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 130   |    1034|       8.208|   0.3%/201|   0.4%/160|   0.5%/152|   0.5%/144 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 130   |      11|       1.040|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 130   |    1129|      60.411|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 130   |     430|       9.032|   2.9%/ 24|   2.8%/ 25|   2.8%/ 25|   2.7%/ 25 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 130   |     317|     176.278|   4.1%/ 17|   4.0%/ 17|   3.9%/ 17|   3.9%/ 18 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 127   |     477|     107.978|   0.7%/ 95|   0.7%/100|   0.7%/101|   0.7%/103 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 128   |    1757|     268.987|   1.3%/ 54|   0.4%/184|   0.2%/449|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 128   |      32|      16.837|   0.2%/383|   0.2%/346|   0.2%/339|   0.2%/334 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 130   |      74|      10.865|   3.0%/ 23|   3.3%/ 21|   3.4%/ 20|   3.4%/ 20 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 127   |      81|      18.055|   0.7%/105|   0.7%/100|   0.7%/ 99|   0.7%/ 98 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 129   |     111|      16.137|   4.4%/ 16|   4.6%/ 15|   4.7%/ 15|   4.7%/ 15 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 130   |      81|      28.894|   0.1%/642|   0.1%/521|   0.1%/492|   0.1%/465 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  84   |     143|       5.461|   4.2%/ 16|   3.6%/ 19|   3.4%/ 20|   3.3%/ 21 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 130   |     125|       3.831|   0.1%/857|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 130   |     125|       6.172|   0.1%/642|   0.1%/778|   0.1%/826|   0.1%/880 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 130   |     158|      38.767|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 130   |   51985|     410.694|   1.4%/ 50|   1.3%/ 51|   1.3%/ 52|   1.3%/ 52 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 130   |     844|     314.570|   1.0%/ 68|   1.0%/ 68|   1.0%/ 68|   1.0%/ 68 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 130   |     409|      11.409|   3.1%/ 22|   3.7%/ 19|   3.8%/ 18|   3.9%/ 18 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  76   |      16|       0.532|   2.8%/ 25|   3.7%/ 18|   3.9%/ 17|   4.1%/ 17 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  30   |      17|       6.767|   5.4%/ 13|   6.9%/ 10|   9.0%/  8|  11.0%/  6 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  85   |      69|       2.315|   3.4%/ 20|   4.3%/ 16|   4.5%/ 15|   4.7%/ 15 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 130   |    6175|     353.716|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 130   |      22|       4.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 130   |     125|      19.390|   0.9%/ 75|   0.8%/ 85|   0.8%/ 88|   0.8%/ 91 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 130   |      69|       3.094|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 130   |     945|       4.584|   0.8%/ 84|   0.8%/ 91|   0.7%/ 93|   0.7%/ 95 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 130   |     529|     254.899|   1.0%/ 68|   0.9%/ 77|   0.9%/ 80|   0.8%/ 83 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 130   |     256|      47.692|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 130   |     506|     108.568|   2.2%/ 31|   2.1%/ 32|   2.1%/ 33|   2.1%/ 33 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 130   |    6116|      27.886|   0.3%/211|   0.2%/326|   0.2%/376|   0.2%/442 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 130   |    1654|     392.039|   1.8%/ 39|   1.5%/ 45|   1.5%/ 47|   1.4%/ 50 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  13   |       3|       0.336|   0.0%/ --|  14.5%/  5|  14.5%/  5|  14.5%/  5 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 130   |      70|       9.745|   4.5%/ 15|   4.7%/ 14|   4.8%/ 14|   4.9%/ 14 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 130   |   21943|     682.913|   1.1%/ 64|   1.0%/ 68|   1.0%/ 70|   1.0%/ 71 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 130   |    2210|      20.369|   1.0%/ 67|   1.1%/ 64|   1.1%/ 63|   1.1%/ 62 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 130   |    1784|      46.488|   0.6%/124|   0.6%/112|   0.6%/109|   0.7%/106 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 130   |    1753|     170.613|   0.1%/467|   0.1%/594|   0.1%/638|   0.1%/690 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 130   |     183|      66.446|   0.7%/103|   0.6%/115|   0.6%/118|   0.6%/122 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 130   |    2608|     134.374|   1.5%/ 47|   1.6%/ 43|   1.7%/ 42|   1.7%/ 41 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 130   |   14908|     101.594|   0.9%/ 79|   0.8%/ 86|   0.8%/ 89|   0.8%/ 91 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  71   |       5|       0.404|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 130   |    3137|      91.679|   1.1%/ 64|   1.0%/ 70|   1.0%/ 72|   0.9%/ 73 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 130   |     231|      14.240|   1.5%/ 46|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 130   |     644|      92.529|   1.4%/ 50|   1.1%/ 60|   1.1%/ 63|   1.0%/ 66 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 108   |      68|       8.568|   0.2%/386|   0.2%/382|   0.2%/380|   0.2%/376 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 130   |      27|       4.737|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 130   |      28|       5.132|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 130   |     125|      59.744|   0.6%/113|   0.7%/ 94|   0.8%/ 90|   0.8%/ 86 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 123   |      93|       5.852|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 130   |   10332|     175.790|   3.3%/ 21|   3.2%/ 21|   3.2%/ 21|   3.2%/ 22 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 130   |   28494|     604.973|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 130   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 130   |     777|      18.317|   0.6%/121|   0.5%/132|   0.5%/135|   0.5%/138 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 130   |    5785|     559.585|   0.1%/712|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 130   |    1986|     230.835|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 130   |      53|       3.041|   2.4%/ 29|   1.5%/ 48|   1.2%/ 57|   1.0%/ 70 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 130   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 130   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 130   |      22|       2.897|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 130   |       8|       5.865|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 130   |      51|       4.353|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 130   |    5833|      70.145|   0.3%/235|   0.3%/241|   0.3%/242|   0.3%/243 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 130   |  161858|     491.157|   0.8%/ 91|   0.8%/ 85|   0.8%/ 84|   0.8%/ 83 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  16   |       6|       0.152|  26.0%/  2|   0.0%/ --|   6.3%/ 11|   6.3%/ 11 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 130   |    1880|      44.896|   1.2%/ 56|   1.3%/ 53|   1.3%/ 52|   1.4%/ 51 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 130   |     356|      36.004|   0.3%/273|   0.3%/273|   0.3%/273|   0.3%/273 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 130   |   46656|     702.271|   0.1%/518|   0.1%/534|   0.1%/538|   0.1%/542 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 130   |      37|      10.616|   0.6%/116|   0.5%/132|   0.5%/136|   0.5%/140 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 130   |     192|       5.615|   3.8%/ 18|   3.5%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 130   |     213|       6.618|   3.3%/ 21|   3.3%/ 21|   3.4%/ 21|   3.4%/ 20 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 129   |     200|      11.164|   3.1%/ 22|   3.7%/ 19|   3.8%/ 18|   3.9%/ 17 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 130   |     104|       6.850|   8.0%/  8|   8.6%/  8|   8.7%/  8|   8.9%/  8 |

