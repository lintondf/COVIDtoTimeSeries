# State and Country COVID-19 Analysis #
## Updated: at 2020-08-03 for data as of 2020-08-02 ##

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 68.7% of deaths and 55.9% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 124   |   32733|    1682.614|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 124   |   15870|    1786.709|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 124   |    9376|     237.303|   1.5%/ 47|   1.5%/ 45|   1.5%/ 45|   1.6%/ 44 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 124   |    8635|    1242.547|   0.2%/383|   0.2%/382|   0.2%/381|   0.2%/380 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 124   |    7717|     609.026|   0.2%/328|   0.2%/337|   0.2%/338|   0.2%/339 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 124   |    7238|     565.360|   0.2%/335|   0.2%/366|   0.2%/375|   0.2%/383 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 124   |    7033|     327.477|   2.7%/ 26|   2.9%/ 24|   2.9%/ 24|   3.0%/ 23 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 124   |    6991|     241.096|   3.6%/ 19|   3.8%/ 18|   3.8%/ 18|   3.8%/ 18 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 124   |    6459|     646.740|   0.1%/637|   0.1%/675|   0.1%/681|   0.1%/686 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 124   |    4439|    1245.145|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 124   |  154596|     469.120|   0.7%/ 97|   0.8%/ 90|   0.8%/ 88|   0.8%/ 87 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 124   |   94883|     448.804|   1.2%/ 56|   1.2%/ 59|   1.2%/ 60|   1.1%/ 60 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 124   |   48246|     381.156|   1.4%/ 48|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 124   |   46314|     697.123|   0.1%/473|   0.1%/483|   0.1%/484|   0.1%/486 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 124   |   38399|      28.209|   2.4%/ 29|   2.3%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 124   |   35167|     583.791|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 124   |   30282|     451.454|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 124   |   28447|     603.973|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 124   |   20246|     630.110|   1.1%/ 63|   0.9%/ 73|   0.9%/ 76|   0.9%/ 79 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 124   |   17290|     207.365|   1.4%/ 50|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 124   |    1646|     335.693|   1.6%/ 42|   1.5%/ 45|   1.5%/ 45|   1.5%/ 46 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 124   |      24|      32.139|   2.3%/ 30|   3.0%/ 23|   3.1%/ 22|   3.3%/ 21 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 124   |    3896|     535.305|   2.4%/ 28|   2.2%/ 32|   2.1%/ 33|   2.1%/ 34 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 124   |     463|     153.467|   1.9%/ 37|   2.0%/ 35|   2.0%/ 34|   2.0%/ 34 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 124   |    9376|     237.303|   1.5%/ 47|   1.5%/ 45|   1.5%/ 45|   1.6%/ 44 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 124   |    1842|     319.781|   0.4%/191|   0.4%/172|   0.4%/167|   0.4%/163 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 124   |    4439|    1245.145|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 124   |     594|     609.807|   0.2%/392|   0.2%/376|   0.2%/373|   0.2%/369 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 124   |    7033|     327.477|   2.7%/ 26|   2.9%/ 24|   2.9%/ 24|   3.0%/ 23 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 124   |    3812|     359.031|   1.3%/ 51|   1.5%/ 46|   1.6%/ 44|   1.6%/ 43 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 124   |      27|      19.113|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 124   |     179|     100.035|   3.8%/ 18|   4.4%/ 16|   4.6%/ 15|   4.7%/ 15 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 124   |    7717|     609.026|   0.2%/328|   0.2%/337|   0.2%/338|   0.2%/339 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 124   |    2979|     442.458|   0.4%/182|   0.4%/175|   0.4%/174|   0.4%/173 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 124   |     879|     278.518|   0.8%/ 92|   0.8%/ 89|   0.8%/ 89|   0.8%/ 88 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 124   |     359|     123.284|   1.1%/ 64|   1.2%/ 57|   1.3%/ 55|   1.3%/ 54 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 124   |     746|     166.866|   0.8%/ 85|   0.8%/ 87|   0.8%/ 87|   0.8%/ 87 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 124   |    3985|     857.236|   0.8%/ 83|   0.9%/ 74|   1.0%/ 72|   1.0%/ 70 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 124   |     123|      91.676|   0.4%/160|   0.4%/160|   0.4%/160|   0.4%/159 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 124   |    3512|     580.865|   0.3%/242|   0.3%/236|   0.3%/234|   0.3%/232 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 124   |    8635|    1242.547|   0.2%/383|   0.2%/382|   0.2%/381|   0.2%/380 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 124   |    6459|     646.740|   0.1%/637|   0.1%/675|   0.1%/681|   0.1%/686 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 124   |    1651|     292.744|   0.3%/212|   0.3%/212|   0.3%/212|   0.3%/212 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 124   |    1677|     563.339|   1.7%/ 40|   1.9%/ 36|   2.0%/ 35|   2.0%/ 34 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 124   |    1278|     208.258|   0.8%/ 85|   0.9%/ 78|   0.9%/ 77|   0.9%/ 75 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 124   |      61|      57.105|   3.9%/ 18|   4.3%/ 16|   4.4%/ 16|   4.5%/ 15 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 124   |     334|     172.770|   0.7%/ 98|   0.7%/ 98|   0.7%/ 98|   0.7%/ 98 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 124   |     836|     271.263|   1.8%/ 38|   1.9%/ 35|   2.0%/ 35|   2.0%/ 34 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 124   |     417|     307.004|   0.3%/212|   0.3%/207|   0.3%/207|   0.3%/206 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 124   |   15870|    1786.709|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 124   |     653|     311.551|   0.9%/ 75|   1.0%/ 71|   1.0%/ 70|   1.0%/ 70 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 124   |   32733|    1682.614|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 124   |    1991|     189.801|   1.3%/ 53|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 124   |     105|     138.257|   0.9%/ 79|   0.8%/ 82|   0.8%/ 84|   0.8%/ 85 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 124   |    3512|     300.470|   0.8%/ 86|   0.9%/ 77|   0.9%/ 75|   0.9%/ 74 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 124   |     548|     138.608|   1.4%/ 48|   1.6%/ 43|   1.6%/ 42|   1.7%/ 41 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 124   |     327|      77.464|   1.7%/ 41|   1.8%/ 38|   1.8%/ 38|   1.9%/ 37 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 124   |    7238|     565.360|   0.2%/335|   0.2%/366|   0.2%/375|   0.2%/383 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 124   |     224|      70.242|   1.8%/ 39|   2.0%/ 34|   2.1%/ 33|   2.1%/ 32 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 124   |    1011|     954.654|   0.1%/660|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 124   |    1813|     352.137|   3.0%/ 23|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 124   |     133|     150.405|   1.1%/ 65|   1.1%/ 64|   1.1%/ 63|   1.1%/ 62 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 124   |    1094|     160.063|   1.8%/ 39|   1.7%/ 41|   1.7%/ 41|   1.7%/ 42 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 124   |    6991|     241.096|   3.6%/ 19|   3.8%/ 18|   3.8%/ 18|   3.8%/ 18 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 124   |  154596|     469.120|   0.7%/ 97|   0.8%/ 90|   0.8%/ 88|   0.8%/ 87 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 124   |     314|      98.023|   1.8%/ 39|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 124   |      57|      90.714|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 124   |    2179|     255.341|   0.7%/103|   0.8%/ 87|   0.8%/ 84|   0.9%/ 80 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 124   |    1584|     208.073|   0.7%/102|   0.7%/ 95|   0.7%/ 93|   0.8%/ 92 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 124   |     114|      63.462|   1.2%/ 57|   1.5%/ 45|   1.6%/ 42|   1.7%/ 40 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 124   |     940|     161.515|   0.8%/ 84|   1.0%/ 72|   1.0%/ 70|   1.0%/ 67 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 112   |      27|      45.922|   0.5%/126|   0.3%/209|   0.3%/249|   0.2%/306 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 124   |    1333|      41.358|   0.8%/ 92|   0.3%/217|   0.2%/329|   0.1%/682 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 124   |     167|      58.719|   2.8%/ 25|   2.7%/ 25|   2.7%/ 25|   2.7%/ 26 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 124   |    1233|      28.671|   1.0%/ 72|   1.0%/ 72|   1.0%/ 72|   1.0%/ 72 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 124   |      55|       1.754|   4.6%/ 15|   5.1%/ 13|   5.2%/ 13|   5.4%/ 13 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 124   |    3743|      83.294|   3.4%/ 20|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 124   |     769|     260.016|   1.2%/ 58|   0.9%/ 74|   0.9%/ 79|   0.8%/ 85 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 124   |     194|       7.573|   4.6%/ 15|   5.6%/ 12|   5.9%/ 12|   6.2%/ 11 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 124   |     717|      80.563|   0.1%/827|   0.1%/695|   0.1%/664|   0.1%/635 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 124   |     473|      46.961|   1.8%/ 38|   1.6%/ 44|   1.5%/ 45|   1.5%/ 47 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 124   |     153|      98.876|   1.2%/ 57|   0.9%/ 75|   0.8%/ 81|   0.8%/ 89 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 124   |    3214|      19.079|   1.3%/ 51|   1.2%/ 57|   1.2%/ 59|   1.1%/ 60 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 124   |     570|      60.566|   0.9%/ 74|   0.9%/ 79|   0.9%/ 80|   0.9%/ 81 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 124   |    9846|     854.330|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 119   |      38|       3.241|   1.0%/ 70|   0.5%/153|   0.3%/218|   0.2%/381 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 124   |    3132|     273.037|   2.7%/ 25|   2.7%/ 25|   2.7%/ 25|   2.8%/ 25 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 124   |     342|     103.592|   2.1%/ 32|   2.3%/ 30|   2.3%/ 29|   2.4%/ 29 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 124   |       1|       0.428|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 124   |   94883|     448.804|   1.2%/ 56|   1.2%/ 59|   1.2%/ 60|   1.1%/ 60 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 124   |     390|      56.087|   1.8%/ 38|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 124   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 112   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 124   |     397|      14.947|   0.3%/213|   0.2%/295|   0.2%/331|   0.2%/380 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 124   |    8994|     236.689|   0.1%/854|   0.1%/940|   0.1%/960|   0.1%/979 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  72   |      60|      10.843|   0.5%/127|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  97   |      75|       4.617|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 124   |    9949|     520.701|   0.9%/ 78|   0.8%/ 87|   0.8%/ 89|   0.8%/ 91 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 124   |    4662|       3.324|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 124   |   10703|     216.681|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 124   |     179|      35.369|   7.7%/  9|   7.3%/  9|   7.1%/ 10|   7.0%/ 10 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 124   |     147|      36.097|   1.3%/ 55|   1.5%/ 48|   1.5%/ 46|   1.5%/ 45 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 124   |      87|       7.766|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 124   |     615|     105.635|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 124   |    1181|     114.014|   1.4%/ 48|   1.5%/ 47|   1.5%/ 47|   1.5%/ 46 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 124   |    5767|     330.138|   0.6%/116|   0.6%/124|   0.5%/127|   0.5%/129 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 124   |    4950|      49.368|   0.9%/ 74|   0.7%/ 99|   0.6%/108|   0.6%/118 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 124   |     480|      73.928|   2.6%/ 27|   2.3%/ 30|   2.2%/ 31|   2.2%/ 32 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 103   |      65|      47.771|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 120   |     296|       3.001|   4.4%/ 16|   4.7%/ 15|   4.8%/ 14|   4.8%/ 14 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 124   |     329|      59.519|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 124   |   30282|     451.454|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 124   |      50|      22.980|   0.4%/157|   0.5%/134|   0.5%/131|   0.5%/127 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 124   |      10|       4.147|   6.4%/ 11|   6.9%/ 10|   7.0%/ 10|   7.1%/ 10 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 121   |      17|       4.577|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 124   |    9154|     110.089|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 124   |     183|       6.054|   1.6%/ 44|   1.7%/ 41|   1.7%/ 40|   1.8%/ 39 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 124   |     207|      19.269|   0.4%/183|   0.5%/151|   0.5%/145|   0.5%/140 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 124   |    2022|     121.772|   2.2%/ 31|   1.9%/ 35|   1.9%/ 37|   1.8%/ 38 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 110   |      47|       3.862|   1.0%/ 67|   0.9%/ 76|   0.9%/ 79|   0.8%/ 82 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  99   |      26|      16.464|   0.2%/313|   0.4%/167|   0.5%/148|   0.5%/132 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 120   |     166|      14.330|   0.8%/ 91|   0.6%/117|   0.6%/124|   0.5%/133 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 124   |    1395|     152.316|   3.1%/ 22|   3.2%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 124   |     597|      61.070|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 124   |   38399|      28.209|   2.4%/ 29|   2.3%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 124   |    5375|      20.137|   1.7%/ 41|   1.5%/ 46|   1.5%/ 47|   1.4%/ 49 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 124   |   17290|     207.365|   1.4%/ 50|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 124   |    5004|     127.877|   1.9%/ 37|   1.5%/ 45|   1.4%/ 48|   1.4%/ 51 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 124   |    1767|     359.082|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 124   |     532|      57.902|   2.0%/ 35|   2.1%/ 33|   2.1%/ 33|   2.1%/ 32 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 124   |   35167|     583.791|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 124   |      10|       3.667|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 124   |    1009|       8.011|   0.2%/375|   0.2%/299|   0.2%/285|   0.3%/271 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 124   |      11|       1.055|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 124   |     873|      46.698|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 124   |     357|       7.514|   3.5%/ 20|   3.7%/ 18|   3.8%/ 18|   3.9%/ 18 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 124   |     233|     129.920|   4.1%/ 17|   4.1%/ 17|   4.0%/ 17|   4.0%/ 17 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 121   |     456|     103.196|   0.8%/ 90|   0.8%/ 88|   0.8%/ 87|   0.8%/ 87 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 122   |    1535|     234.911|   2.5%/ 27|   1.5%/ 45|   1.3%/ 53|   1.0%/ 66 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 122   |      32|      16.566|   0.3%/236|   0.4%/178|   0.4%/166|   0.4%/154 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 124   |      61|       8.954|   3.0%/ 23|   3.7%/ 19|   3.8%/ 18|   4.0%/ 17 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 121   |      80|      17.911|   0.7%/ 99|   0.6%/112|   0.6%/113|   0.6%/113 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 123   |      80|      11.711|   3.8%/ 18|   4.3%/ 16|   4.4%/ 16|   4.5%/ 15 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 124   |      80|      28.724|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  78   |     117|       4.453|   4.9%/ 14|   4.3%/ 16|   4.1%/ 17|   3.9%/ 18 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 124   |     125|       3.812|   0.2%/439|   0.2%/374|   0.2%/360|   0.2%/347 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 124   |     125|       6.148|   0.1%/530|   0.1%/585|   0.1%/605|   0.1%/629 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 124   |     159|      38.982|   0.2%/362|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 124   |   48246|     381.156|   1.4%/ 48|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 124   |     793|     295.798|   1.0%/ 68|   1.0%/ 68|   1.0%/ 68|   1.0%/ 69 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 124   |     344|       9.595|   2.3%/ 30|   2.8%/ 25|   2.9%/ 24|   3.0%/ 23 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  70   |      12|       0.388|   0.7%/100|   1.6%/ 44|   1.8%/ 37|   2.2%/ 32 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  24   |      11|       4.533|   4.6%/ 15|   7.5%/  9|   5.8%/ 12|   3.9%/ 17 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  79   |      57|       1.896|   2.7%/ 26|   3.6%/ 19|   3.8%/ 18|   4.0%/ 17 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 124   |    6166|     353.232|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 124   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 124   |     119|      18.390|   1.0%/ 71|   0.8%/ 81|   0.8%/ 85|   0.8%/ 89 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 124   |      69|       3.100|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 124   |     906|       4.396|   0.8%/ 88|   0.6%/119|   0.5%/131|   0.5%/146 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 124   |     502|     241.844|   1.2%/ 57|   1.1%/ 63|   1.1%/ 65|   1.0%/ 67 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 124   |     256|      47.611|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 124   |     450|      96.380|   2.2%/ 32|   1.8%/ 39|   1.7%/ 42|   1.6%/ 44 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 124   |    6053|      27.596|   0.5%/143|   0.3%/225|   0.3%/262|   0.2%/312 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 124   |    1509|     357.658|   2.1%/ 32|   1.9%/ 36|   1.9%/ 37|   1.8%/ 39 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 124   |      54|       7.533|   3.7%/ 18|   3.8%/ 18|   3.8%/ 18|   3.8%/ 18 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 124   |   20246|     630.110|   1.1%/ 63|   0.9%/ 73|   0.9%/ 76|   0.9%/ 79 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 124   |    2086|      19.220|   1.0%/ 72|   1.0%/ 71|   1.0%/ 70|   1.0%/ 70 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 124   |    1727|      44.994|   0.5%/148|   0.5%/145|   0.5%/143|   0.5%/142 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 124   |    1742|     169.543|   0.2%/328|   0.2%/373|   0.2%/386|   0.2%/399 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 124   |     176|      64.045|   0.9%/ 81|   0.8%/ 85|   0.8%/ 86|   0.8%/ 87 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 124   |    2381|     122.721|   1.3%/ 55|   1.4%/ 51|   1.4%/ 50|   1.4%/ 49 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 124   |   14244|      97.068|   1.0%/ 69|   0.9%/ 76|   0.9%/ 78|   0.9%/ 81 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  65   |       5|       0.404|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 124   |    2971|      86.817|   1.2%/ 60|   0.9%/ 73|   0.9%/ 77|   0.8%/ 82 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 124   |     214|      13.181|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43|   1.6%/ 43 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 124   |     604|      86.770|   1.7%/ 41|   1.3%/ 51|   1.3%/ 54|   1.2%/ 58 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 102   |      67|       8.507|   0.2%/317|   0.1%/484|   0.1%/544|   0.1%/618 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 124   |      27|       4.758|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 124   |      28|       5.132|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 124   |     119|      56.884|   0.4%/185|   0.5%/143|   0.5%/136|   0.5%/129 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 117   |      93|       5.855|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 124   |    8613|     146.541|   3.4%/ 20|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 124   |   28447|     603.973|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 124   |      11|       0.505|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 124   |     752|      17.721|   0.7%/ 98|   0.7%/ 97|   0.7%/ 97|   0.7%/ 97 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 124   |    5767|     557.806|   0.2%/445|   0.1%/570|   0.1%/614|   0.1%/665 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 124   |    1982|     230.343|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 124   |      49|       2.801|   3.6%/ 19|   2.5%/ 28|   2.2%/ 32|   1.9%/ 37 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 124   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 124   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 124   |      19|       2.519|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 124   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 124   |      50|       4.286|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 124   |    5733|      68.939|   0.3%/231|   0.3%/245|   0.3%/248|   0.3%/252 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 124   |  154596|     469.120|   0.7%/ 97|   0.8%/ 90|   0.8%/ 88|   0.8%/ 87 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  10   |       4|       0.099|  26.0%/  2|  14.5%/  5|  26.0%/  2|  26.0%/  2 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 124   |    1750|      41.782|   1.1%/ 64|   1.1%/ 65|   1.1%/ 65|   1.1%/ 65 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 124   |     351|      35.536|   0.3%/250|   0.3%/252|   0.3%/252|   0.3%/251 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 124   |   46314|     697.123|   0.1%/473|   0.1%/483|   0.1%/484|   0.1%/486 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 124   |      36|      10.241|   0.6%/118|   0.4%/167|   0.4%/187|   0.3%/213 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 124   |     156|       4.569|   4.1%/ 17|   3.7%/ 19|   3.6%/ 19|   3.4%/ 20 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 124   |     176|       5.467|   3.1%/ 22|   2.9%/ 24|   2.9%/ 24|   2.8%/ 25 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 123   |     184|      10.262|   1.0%/ 71|   2.1%/ 33|   4.2%/ 16|   4.5%/ 15 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 124   |      50|       3.272|   8.7%/  8|   9.9%/  7|  10.3%/  7|  10.7%/  6 |

