# State and Country COVID-19 Analysis #
## Updated: at 2020-09-23 for data as of 2020-09-22 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.3% of deaths and 38.8% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.1% of deaths and 56.2% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 175   |   33096|    1701.299|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 175   |   16077|    1810.065|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 175   |   15519|     535.224|   0.7%/103|   0.5%/126|   0.5%/133|   0.5%/141 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 175   |   15347|     388.423|   0.6%/113|   0.5%/127|   0.5%/131|   0.5%/135 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 175   |   13612|     633.783|   0.7%/ 95|   0.7%/106|   0.6%/109|   0.6%/113 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 175   |    9327|    1342.058|   0.1%/490|   0.1%/492|   0.1%/492|   0.1%/492 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 175   |    8728|     688.741|   0.2%/281|   0.2%/284|   0.2%/284|   0.2%/285 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 175   |    7979|     623.299|   0.2%/350|   0.2%/339|   0.2%/336|   0.2%/333 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 175   |    7008|     701.694|   0.1%/533|   0.1%/567|   0.1%/576|   0.1%/586 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 175   |    6799|     640.384|   0.6%/108|   0.5%/133|   0.5%/141|   0.5%/150 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 175   |  201648|     611.900|   0.4%/185|   0.3%/198|   0.3%/202|   0.3%/206 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 175   |  139054|     657.738|   0.5%/129|   0.5%/141|   0.5%/144|   0.5%/147 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 175   |   89869|      66.021|   1.4%/ 50|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 175   |   75010|     592.600|   0.6%/121|   0.5%/135|   0.5%/139|   0.5%/143 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 175   |   41864|     630.140|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 175   |   35711|     592.830|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 175   |   31188|     464.972|   0.1%/542|   0.1%/471|   0.2%/456|   0.2%/441 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 175   |   31764|     988.557|   0.4%/196|   0.3%/233|   0.3%/244|   0.3%/257 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 175   |   30539|     648.387|   0.2%/356|   0.2%/334|   0.2%/329|   0.2%/324 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 175   |   24500|     293.843|   0.6%/111|   0.6%/108|   0.6%/107|   0.7%/106 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 175   |    2488|     507.495|   0.5%/138|   0.4%/162|   0.4%/169|   0.4%/177 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 175   |      47|      64.718|   0.5%/133|   0.4%/185|   0.3%/205|   0.3%/230 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 175   |    5547|     762.056|   0.3%/199|   0.3%/243|   0.3%/257|   0.3%/273 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 175   |    1223|     405.208|   1.0%/ 67|   0.8%/ 85|   0.8%/ 91|   0.7%/ 98 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 175   |   15347|     388.423|   0.6%/113|   0.5%/127|   0.5%/131|   0.5%/135 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 175   |    2023|     351.256|   0.2%/396|   0.2%/399|   0.2%/400|   0.2%/400 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 175   |    4494|    1260.363|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 175   |     624|     640.420|   0.2%/384|   0.2%/344|   0.2%/335|   0.2%/326 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 175   |   13612|     633.783|   0.7%/ 95|   0.7%/106|   0.6%/109|   0.6%/113 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 175   |    6799|     640.384|   0.6%/108|   0.5%/133|   0.5%/141|   0.5%/150 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 175   |     130|      91.712|   2.1%/ 33|   1.7%/ 40|   1.6%/ 43|   1.5%/ 45 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 175   |     461|     258.031|   0.9%/ 80|   0.7%/ 97|   0.7%/103|   0.6%/108 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 175   |    8728|     688.741|   0.2%/281|   0.2%/284|   0.2%/284|   0.2%/285 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 175   |    3531|     524.544|   0.3%/249|   0.3%/261|   0.3%/264|   0.3%/267 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 175   |    1299|     411.716|   0.6%/115|   0.6%/125|   0.5%/128|   0.5%/131 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 175   |     603|     207.094|   1.4%/ 48|   1.6%/ 44|   1.6%/ 44|   1.6%/ 43 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 175   |    1137|     254.465|   0.7%/ 96|   0.7%/104|   0.6%/107|   0.6%/109 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 175   |    5430|    1168.020|   0.4%/197|   0.3%/225|   0.3%/233|   0.3%/241 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 175   |     139|     103.622|   0.3%/244|   0.3%/226|   0.3%/222|   0.3%/217 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 175   |    3898|     644.708|   0.2%/450|   0.1%/484|   0.1%/493|   0.1%/503 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 175   |    9327|    1342.058|   0.1%/490|   0.1%/492|   0.1%/492|   0.1%/492 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 175   |    7008|     701.694|   0.1%/533|   0.1%/567|   0.1%/576|   0.1%/586 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 175   |    2031|     360.192|   0.4%/187|   0.4%/189|   0.4%/189|   0.4%/190 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 175   |    2878|     967.116|   0.6%/122|   0.5%/144|   0.5%/151|   0.4%/158 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 175   |    1868|     304.402|   0.7%/ 94|   0.7%/ 96|   0.7%/ 96|   0.7%/ 97 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 175   |     160|     149.728|   2.1%/ 32|   2.2%/ 31|   2.3%/ 31|   2.3%/ 30 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 175   |     455|     235.280|   0.6%/125|   0.6%/124|   0.6%/124|   0.6%/124 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 175   |    1568|     509.213|   0.7%/106|   0.6%/126|   0.5%/132|   0.5%/138 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 175   |     439|     322.700|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 175   |   16077|    1810.065|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 175   |     857|     408.930|   0.4%/173|   0.4%/186|   0.4%/190|   0.4%/193 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 175   |   33096|    1701.299|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 175   |    3311|     315.716|   0.8%/ 85|   0.8%/ 89|   0.8%/ 91|   0.8%/ 92 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 175   |     191|     251.191|   1.6%/ 44|   1.7%/ 40|   1.7%/ 40|   1.8%/ 39 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 175   |    4661|     398.720|   0.5%/140|   0.5%/144|   0.5%/144|   0.5%/145 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 175   |     973|     245.855|   0.7%/ 96|   0.6%/109|   0.6%/113|   0.6%/118 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 175   |     542|     128.454|   0.6%/117|   0.5%/140|   0.5%/147|   0.4%/155 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 175   |    7979|     623.299|   0.2%/350|   0.2%/339|   0.2%/336|   0.2%/333 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 175   |     624|     195.444|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 175   |    1094|    1032.304|   0.2%/302|   0.2%/280|   0.3%/275|   0.3%/271 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 175   |    3291|     639.281|   0.7%/100|   0.6%/116|   0.6%/121|   0.5%/126 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 175   |     199|     225.195|   1.1%/ 65|   1.2%/ 58|   1.2%/ 56|   1.3%/ 55 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 175   |    2299|     336.377|   1.0%/ 66|   1.0%/ 72|   0.9%/ 73|   0.9%/ 75 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 175   |   15519|     535.224|   0.7%/103|   0.5%/126|   0.5%/133|   0.5%/141 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 175   |  201648|     611.900|   0.4%/185|   0.3%/198|   0.3%/202|   0.3%/206 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 175   |     448|     139.788|   0.3%/251|   0.2%/357|   0.2%/398|   0.2%/451 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 175   |      58|      92.950|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 175   |    2994|     350.812|   0.8%/ 91|   0.8%/ 84|   0.8%/ 82|   0.9%/ 80 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 175   |    2061|     270.698|   0.3%/227|   0.3%/242|   0.3%/246|   0.3%/250 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 175   |     325|     181.562|   1.7%/ 40|   1.6%/ 42|   1.6%/ 42|   1.6%/ 43 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 175   |    1261|     216.491|   0.4%/161|   0.4%/175|   0.4%/179|   0.4%/183 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 163   |      49|      85.154|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 175   |    1443|      44.767|   0.1%/502|   0.1%/487|   0.1%/482|   0.1%/477 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 175   |     374|     131.277|   1.1%/ 65|   1.0%/ 72|   0.9%/ 74|   0.9%/ 76 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 175   |    1694|      39.395|   0.5%/141|   0.5%/148|   0.5%/149|   0.5%/151 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 175   |     155|       4.989|   1.7%/ 41|   1.7%/ 41|   1.7%/ 40|   1.7%/ 40 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 175   |   13901|     309.339|   2.0%/ 34|   1.9%/ 36|   1.9%/ 37|   1.8%/ 37 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 175   |     941|     318.016|   0.3%/256|   0.2%/285|   0.2%/293|   0.2%/301 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 175   |    1070|      41.651|   0.7%/ 98|   0.3%/219|   0.2%/316|   0.1%/565 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 175   |     767|      86.132|   0.2%/329|   0.2%/283|   0.3%/273|   0.3%/264 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 175   |     581|      57.699|   0.3%/201|   0.3%/211|   0.3%/214|   0.3%/217 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 175   |     225|     145.909|   0.8%/ 89|   0.8%/ 85|   0.8%/ 85|   0.8%/ 84 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 175   |    5058|      30.021|   0.7%/104|   0.6%/115|   0.6%/118|   0.6%/121 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 175   |     796|      84.595|   0.7%/106|   0.6%/111|   0.6%/112|   0.6%/113 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 175   |    9950|     863.409|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 170   |      40|       3.420|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 175   |    8090|     705.293|   0.6%/112|   0.5%/154|   0.4%/170|   0.4%/190 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 175   |     786|     238.006|   1.0%/ 67|   1.0%/ 73|   0.9%/ 74|   0.9%/ 76 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 175   |      16|       6.832|   3.9%/ 17|   3.2%/ 22|   3.0%/ 23|   2.8%/ 25 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 175   |  139054|     657.738|   0.5%/129|   0.5%/141|   0.5%/144|   0.5%/147 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 175   |     792|     113.879|   0.8%/ 87|   0.6%/107|   0.6%/113|   0.6%/120 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 175   |      56|       2.694|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 163   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 175   |     417|      15.713|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 175   |    9276|     244.115|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 123   |      62|      11.289|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 148   |      82|       5.028|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 175   |   12404|     649.193|   0.4%/178|   0.4%/189|   0.4%/193|   0.4%/196 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 175   |    4743|       3.383|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 175   |   25207|     510.317|   0.9%/ 80|   0.7%/100|   0.6%/107|   0.6%/114 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 175   |     755|     149.267|   2.6%/ 27|   2.6%/ 27|   2.6%/ 27|   2.6%/ 27 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 175   |     252|      61.890|   1.5%/ 45|   1.7%/ 41|   1.7%/ 41|   1.7%/ 40 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 175   |     116|      10.348|   1.0%/ 70|   1.1%/ 64|   1.1%/ 63|   1.1%/ 61 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 175   |     637|     109.386|   0.1%/522|   0.2%/450|   0.2%/435|   0.2%/420 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 175   |    2132|     205.857|   0.7%/ 99|   0.6%/120|   0.5%/127|   0.5%/135 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 175   |    7280|     416.774|   0.3%/223|   0.3%/262|   0.3%/275|   0.2%/289 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 175   |    5810|      57.942|   0.3%/222|   0.3%/226|   0.3%/227|   0.3%/229 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 175   |     831|     128.108|   0.5%/149|   0.3%/198|   0.3%/217|   0.3%/238 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 154   |      83|      61.107|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 171   |    1162|      11.781|   1.3%/ 55|   1.0%/ 68|   1.0%/ 73|   0.9%/ 77 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 175   |     340|      61.447|   0.1%/844|   0.1%/734|   0.1%/710|   0.1%/687 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 175   |   31188|     464.972|   0.1%/542|   0.1%/471|   0.2%/456|   0.2%/441 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 175   |      53|      24.516|   0.1%/786|   0.1%/605|   0.1%/569|   0.1%/535 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 175   |     109|      46.542|   1.3%/ 54|   0.3%/223|   0.0%/ --|   0.6%/113 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 172   |      19|       5.204|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 175   |    9397|     113.019|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 175   |     300|       9.914|   0.3%/241|   0.2%/320|   0.2%/347|   0.2%/377 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 175   |     343|      31.937|   1.3%/ 52|   1.4%/ 49|   1.4%/ 48|   1.5%/ 48 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 175   |    3145|     189.415|   0.6%/119|   0.5%/126|   0.5%/128|   0.5%/130 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 161   |      65|       5.343|   0.3%/212|   0.2%/306|   0.2%/342|   0.2%/386 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 150   |      40|      25.146|   0.1%/464|   0.1%/976|   0.0%/ ***|   0.0%/ *** |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 171   |     226|      19.479|   0.3%/218|   0.3%/261|   0.3%/276|   0.2%/294 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 175   |    2241|     244.727|   0.7%/102|   0.6%/121|   0.5%/127|   0.5%/133 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 175   |     645|      66.035|   0.7%/103|   0.8%/ 85|   0.8%/ 82|   0.9%/ 78 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 175   |   89869|      66.021|   1.4%/ 50|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 175   |    9819|      36.789|   1.3%/ 54|   1.3%/ 55|   1.3%/ 55|   1.3%/ 55 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 175   |   24500|     293.843|   0.6%/111|   0.6%/108|   0.6%/107|   0.7%/106 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 175   |    8765|     224.021|   0.9%/ 76|   0.9%/ 80|   0.9%/ 81|   0.8%/ 82 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 175   |    1791|     363.825|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 175   |    1278|     139.054|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 175   |   35711|     592.830|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 175   |      68|      24.896|   6.0%/ 11|   6.4%/ 11|   6.5%/ 10|   6.6%/ 10 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 175   |    1552|      12.326|   0.6%/107|   0.6%/125|   0.5%/130|   0.5%/136 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 175   |      32|       2.987|   4.0%/ 17|   4.3%/ 16|   4.4%/ 16|   4.5%/ 15 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 175   |    1713|      91.684|   0.3%/233|   0.2%/338|   0.2%/380|   0.2%/434 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 175   |     660|      13.872|   0.5%/133|   0.5%/152|   0.4%/157|   0.4%/162 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 175   |     495|     275.775|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 172   |     586|     132.672|   0.5%/141|   0.5%/134|   0.5%/133|   0.5%/131 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 173   |    1052|     161.037|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 173   |      36|      18.949|   0.2%/306|   0.2%/328|   0.2%/334|   0.2%/339 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 175   |     315|      46.106|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 172   |      82|      18.323|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 174   |     472|      68.719|   2.9%/ 24|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 175   |      87|      31.282|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 129   |     225|       8.580|   0.7%/ 92|   0.8%/ 92|   0.8%/ 92|   0.8%/ 91 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 175   |     130|       3.962|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 175   |     129|       6.355|   0.1%/914|   0.1%/967|   0.1%/987|   0.1%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 175   |     162|      39.653|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 175   |   75010|     592.600|   0.6%/121|   0.5%/135|   0.5%/139|   0.5%/143 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 175   |    1224|     456.339|   0.9%/ 76|   0.9%/ 75|   0.9%/ 74|   0.9%/ 74 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 175   |    1972|      54.981|   2.1%/ 33|   1.8%/ 38|   1.8%/ 39|   1.7%/ 41 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 121   |      46|       1.515|   3.2%/ 22|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  75   |     116|      47.156|   1.6%/ 43|   1.4%/ 51|   1.3%/ 53|   1.2%/ 57 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 130   |     443|      14.758|   2.6%/ 27|   2.2%/ 32|   2.1%/ 34|   2.0%/ 35 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 175   |    6329|     362.524|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 175   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 175   |     149|      23.073|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 175   |      69|       3.092|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 175   |    1112|       5.394|   0.3%/251|   0.2%/281|   0.2%/291|   0.2%/301 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 175   |     698|     336.032|   0.8%/ 86|   0.9%/ 81|   0.9%/ 80|   0.9%/ 79 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 175   |     266|      49.647|   0.1%/ ***|   0.1%/928|   0.1%/890|   0.1%/854 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 175   |     859|     184.194|   1.1%/ 61|   1.1%/ 61|   1.1%/ 60|   1.1%/ 60 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 175   |    6440|      29.364|   0.1%/850|   0.1%/970|   0.1%/ ***|   0.1%/ *** |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 175   |    2289|     542.649|   0.6%/121|   0.5%/128|   0.5%/130|   0.5%/132 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  58   |       7|       0.782|   2.5%/ 27|   3.4%/ 20|   3.7%/ 19|   4.1%/ 17 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 175   |     740|     103.388|   3.2%/ 22|   2.7%/ 25|   2.6%/ 27|   2.5%/ 28 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 175   |   31764|     988.557|   0.4%/196|   0.3%/233|   0.3%/244|   0.3%/257 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 175   |    5157|      47.523|   1.5%/ 47|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 175   |    2313|      60.273|   0.6%/124|   0.6%/123|   0.6%/123|   0.6%/123 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 175   |    1907|     185.604|   0.3%/238|   0.3%/212|   0.3%/206|   0.3%/200 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 175   |     212|      77.043|   0.3%/241|   0.3%/244|   0.3%/245|   0.3%/247 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 175   |    4565|     235.230|   0.9%/ 75|   0.8%/ 82|   0.8%/ 84|   0.8%/ 86 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 175   |   19559|     133.283|   0.6%/115|   0.6%/115|   0.6%/115|   0.6%/115 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 116   |      27|       2.179|   2.4%/ 29|   2.4%/ 28|   2.4%/ 28|   2.5%/ 28 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 175   |    4562|     133.319|   0.7%/104|   0.6%/109|   0.6%/110|   0.6%/112 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 175   |     306|      18.882|   0.2%/301|   0.1%/471|   0.1%/545|   0.1%/646 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 175   |     746|     107.130|   0.2%/441|   0.1%/547|   0.1%/580|   0.1%/617 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 153   |      73|       9.180|   0.1%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 175   |      27|       4.734|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 175   |      40|       7.320|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 175   |     139|      66.525|   0.1%/665|   0.1%/716|   0.1%/726|   0.1%/734 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 168   |      99|       6.208|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 175   |   16388|     278.827|   0.5%/148|   0.3%/201|   0.3%/220|   0.3%/243 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 175   |   30539|     648.387|   0.2%/356|   0.2%/334|   0.2%/329|   0.2%/324 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 175   |      13|       0.597|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 175   |     840|      19.796|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 175   |    5869|     567.676|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 175   |    2045|     237.681|   0.1%/828|   0.1%/749|   0.1%/731|   0.1%/713 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 175   |     188|      10.714|   1.8%/ 39|   1.5%/ 46|   1.4%/ 48|   1.4%/ 51 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 175   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 175   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 175   |      43|       5.741|   0.7%/ 93|   0.8%/ 90|   0.8%/ 89|   0.8%/ 89 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 175   |      78|      57.486|   4.3%/ 16|   3.7%/ 18|   3.6%/ 19|   3.4%/ 20 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 175   |     149|      12.674|   4.7%/ 15|   5.4%/ 13|   5.6%/ 12|   5.8%/ 12 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 175   |    7574|      91.086|   0.9%/ 79|   0.9%/ 74|   1.0%/ 73|   1.0%/ 72 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 175   |  201648|     611.900|   0.4%/185|   0.3%/198|   0.3%/202|   0.3%/206 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  61   |      65|       1.621|   2.9%/ 23|   1.4%/ 51|   1.0%/ 72|   0.6%/124 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 175   |    3740|      89.314|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 175   |     408|      41.248|   0.2%/318|   0.2%/366|   0.2%/381|   0.2%/397 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 175   |   41864|     630.140|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 175   |      46|      13.182|   0.1%/477|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 175   |     449|      13.143|   1.5%/ 47|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 175   |     569|      17.651|   1.7%/ 40|   1.7%/ 42|   1.6%/ 42|   1.6%/ 42 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  54   |      35|       0.364|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 174   |     333|      18.621|   0.4%/154|   0.4%/159|   0.4%/161|   0.4%/162 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 175   |     240|      15.843|   0.2%/326|   0.0%/ --|   0.0%/ --|   0.0%/ -- |

