# State and Country COVID-19 Analysis #
## Updated: at 2020-07-25 for data as of 2020-07-24 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 35.3% of deaths and 39.7% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 69.5% of deaths and 56.9% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 133   |   32641|    1677.899|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 137   |   15854|    1784.918|   0.1%/495|   0.1%/756|   0.1%/879|   0.1%/ *** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 127   |    8511|    1224.687|   0.2%/371|   0.2%/416|   0.2%/430|   0.2%/444 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 143   |    8267|     209.235|   1.4%/ 51|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 130   |    7632|     602.257|   0.3%/259|   0.2%/359|   0.2%/399|   0.2%/448 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 128   |    7120|     556.185|   0.3%/268|   0.2%/284|   0.2%/289|   0.2%/293 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 128   |    6413|     642.172|   0.1%/528|   0.1%/602|   0.1%/626|   0.1%/652 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 139   |    5507|     256.391|   2.3%/ 30|   2.6%/ 27|   2.6%/ 26|   2.7%/ 26 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 130   |    4637|     159.907|   3.3%/ 21|   3.7%/ 19|   3.8%/ 18|   3.9%/ 18 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 128   |    4417|    1238.938|   0.1%/734|   0.1%/722|   0.1%/722|   0.1%/724 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 147   |  144594|     438.768|   0.6%/118|   0.6%/113|   0.6%/112|   0.6%/111 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 130   |   85580|     404.803|   1.4%/ 49|   1.3%/ 51|   1.3%/ 52|   1.3%/ 52 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 136   |   45787|     689.191|   0.2%/444|   0.1%/492|   0.1%/506|   0.1%/520 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 128   |   42818|     338.278|   1.7%/ 42|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 155   |   35119|     582.992|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 136   |   31132|      22.870|   2.5%/ 27|   2.6%/ 27|   2.6%/ 27|   2.6%/ 27 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 161   |   30228|     450.653|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 144   |   28437|     603.744|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 127   |   14240|     443.194|   1.4%/ 48|   1.3%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 156   |   15259|     183.008|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 122   |    1408|     287.210|   2.0%/ 35|   2.2%/ 32|   2.2%/ 31|   2.3%/ 30 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 122   |      19|      25.816|   1.1%/ 65|   1.3%/ 53|   1.4%/ 51|   1.4%/ 48 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 126   |    3141|     431.571|   2.9%/ 24|   3.1%/ 23|   3.1%/ 22|   3.1%/ 22 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 123   |     390|     129.333|   1.7%/ 41|   1.7%/ 40|   1.8%/ 39|   1.8%/ 39 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 143   |    8267|     209.235|   1.4%/ 51|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 133   |    1780|     309.080|   0.3%/239|   0.3%/209|   0.3%/203|   0.4%/197 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 128   |    4417|    1238.938|   0.1%/734|   0.1%/722|   0.1%/722|   0.1%/724 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 121   |     531|     545.544|   0.2%/383|   0.2%/342|   0.2%/333|   0.2%/323 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 139   |    5507|     256.391|   2.3%/ 30|   2.6%/ 27|   2.6%/ 26|   2.7%/ 26 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 135   |    3336|     314.170|   1.0%/ 67|   1.2%/ 56|   1.3%/ 54|   1.3%/ 52 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 116   |      26|      18.248|   1.4%/ 51|   2.0%/ 35|   2.1%/ 32|   2.3%/ 30 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 121   |     131|      73.212|   3.1%/ 22|   3.9%/ 18|   4.1%/ 17|   4.3%/ 16 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 130   |    7632|     602.257|   0.3%/259|   0.2%/359|   0.2%/399|   0.2%/448 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 131   |    2878|     427.526|   0.4%/186|   0.4%/181|   0.4%/180|   0.4%/178 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 122   |     822|     260.551|   0.7%/ 94|   0.8%/ 83|   0.9%/ 81|   0.9%/ 79 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 134   |     323|     110.884|   0.8%/ 87|   0.9%/ 80|   0.9%/ 78|   0.9%/ 76 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 131   |     693|     155.145|   0.8%/ 88|   0.8%/ 91|   0.7%/ 92|   0.7%/ 94 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 133   |    3598|     773.986|   0.4%/162|   0.4%/169|   0.4%/172|   0.4%/174 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 120   |     119|      88.792|   0.4%/160|   0.3%/201|   0.3%/214|   0.3%/231 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 128   |    3426|     566.674|   0.3%/259|   0.2%/281|   0.2%/287|   0.2%/293 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 127   |    8511|    1224.687|   0.2%/371|   0.2%/416|   0.2%/430|   0.2%/444 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 128   |    6413|     642.172|   0.1%/528|   0.1%/602|   0.1%/626|   0.1%/652 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 126   |    1606|     284.808|   0.3%/211|   0.3%/218|   0.3%/220|   0.3%/222 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 128   |    1453|     488.208|   1.4%/ 50|   1.4%/ 48|   1.5%/ 47|   1.5%/ 47 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 128   |    1179|     192.144|   0.7%/101|   0.7%/ 94|   0.7%/ 92|   0.8%/ 90 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 120   |      45|      41.927|   3.0%/ 23|   3.5%/ 19|   3.7%/ 19|   3.8%/ 18 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 119   |     314|     162.458|   0.7%/ 96|   0.9%/ 80|   0.9%/ 77|   0.9%/ 74 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 131   |     708|     229.772|   1.7%/ 41|   1.9%/ 36|   2.0%/ 35|   2.0%/ 34 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 124   |     405|     298.093|   0.3%/206|   0.3%/217|   0.3%/219|   0.3%/220 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 137   |   15854|    1784.918|   0.1%/495|   0.1%/756|   0.1%/879|   0.1%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 122   |     599|     285.669|   0.8%/ 83|   0.9%/ 79|   0.9%/ 78|   0.9%/ 78 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 133   |   32641|    1677.899|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 122   |    1763|     168.086|   1.3%/ 55|   1.4%/ 49|   1.5%/ 48|   1.5%/ 46 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 120   |      97|     127.198|   1.1%/ 64|   1.2%/ 56|   1.3%/ 54|   1.3%/ 52 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 127   |    3267|     279.485|   0.6%/110|   0.7%/103|   0.7%/102|   0.7%/100 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 128   |     475|     120.048|   1.1%/ 61|   1.3%/ 53|   1.4%/ 51|   1.4%/ 49 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 132   |     278|      65.864|   1.4%/ 49|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 128   |    7120|     556.185|   0.3%/268|   0.2%/284|   0.2%/289|   0.2%/293 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 126   |     188|      58.873|   1.2%/ 60|   1.3%/ 51|   1.4%/ 50|   1.4%/ 48 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 119   |    1003|     946.794|   0.2%/354|   0.2%/411|   0.2%/428|   0.2%/445 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 131   |    1319|     256.169|   3.0%/ 23|   3.4%/ 20|   3.5%/ 20|   3.6%/ 19 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 136   |     124|     139.944|   1.0%/ 66|   1.0%/ 72|   0.9%/ 73|   0.9%/ 75 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 126   |     928|     135.759|   2.0%/ 35|   2.1%/ 33|   2.1%/ 33|   2.1%/ 33 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 130   |    4637|     159.907|   3.3%/ 21|   3.7%/ 19|   3.8%/ 18|   3.9%/ 18 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 147   |  144594|     438.768|   0.6%/118|   0.6%/113|   0.6%/112|   0.6%/111 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 125   |     271|      84.395|   2.0%/ 34|   2.1%/ 34|   2.1%/ 33|   2.1%/ 33 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 127   |      56|      89.745|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 133   |    2091|     245.002|   0.5%/147|   0.3%/209|   0.3%/234|   0.3%/266 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 147   |    1485|     195.076|   0.5%/135|   0.5%/137|   0.5%/138|   0.5%/138 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 117   |     102|      57.120|   0.5%/143|   0.5%/129|   0.5%/126|   0.6%/124 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 127   |     869|     149.237|   0.6%/121|   0.7%/104|   0.7%/101|   0.7%/ 97 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 103   |      26|      44.335|   0.9%/ 73|   1.0%/ 71|   1.0%/ 71|   1.0%/ 71 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 125   |    1274|      39.521|   1.6%/ 43|   1.2%/ 56|   1.1%/ 61|   1.0%/ 67 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 136   |     129|      45.446|   2.7%/ 26|   2.4%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 135   |    1129|      26.265|   1.0%/ 73|   1.0%/ 70|   1.0%/ 69|   1.0%/ 69 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 118   |      35|       1.113|   2.4%/ 29|   4.4%/ 16|   4.4%/ 16|   5.3%/ 13 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 139   |    2711|      60.324|   3.4%/ 20|   3.6%/ 19|   3.6%/ 19|   3.7%/ 19 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 121   |     703|     237.662|   1.8%/ 37|   1.8%/ 39|   1.7%/ 40|   1.7%/ 40 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 146   |     127|       4.943|   2.0%/ 35|   2.5%/ 27|   2.7%/ 26|   2.8%/ 24 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 135   |     712|      79.989|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 134   |     407|      40.399|   2.4%/ 29|   2.2%/ 32|   2.1%/ 32|   2.1%/ 33 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 131   |     137|      88.818|   1.7%/ 40|   1.6%/ 44|   1.5%/ 45|   1.5%/ 47 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 129   |    2865|      17.008|   1.6%/ 42|   1.5%/ 46|   1.5%/ 47|   1.4%/ 49 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 116   |     527|      56.035|   1.1%/ 66|   0.9%/ 74|   0.9%/ 76|   0.9%/ 79 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 136   |    9815|     851.658|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 110   |      35|       2.982|   2.8%/ 25|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 118   |    2495|     217.531|   2.8%/ 25|   2.5%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 126   |     276|      83.651|   1.9%/ 36|   2.1%/ 33|   2.1%/ 33|   2.2%/ 32 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 116   |       1|       0.428|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 130   |   85580|     404.803|   1.4%/ 49|   1.3%/ 51|   1.3%/ 52|   1.3%/ 52 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 136   |     331|      47.552|   1.7%/ 40|   1.8%/ 39|   1.8%/ 38|   1.8%/ 38 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 129   |      53|       2.540|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 103   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 122   |     390|      14.709|   0.6%/116|   0.6%/122|   0.6%/123|   0.6%/124 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 138   |    8950|     235.524|   0.1%/726|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  63   |      58|      10.584|   0.6%/108|   1.4%/ 48|   1.6%/ 42|   1.8%/ 38 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  88   |      75|       4.628|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 125   |    9064|     474.364|   1.2%/ 59|   1.0%/ 70|   0.9%/ 74|   0.9%/ 77 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 136   |    4645|       3.312|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 125   |    8017|     162.299|   3.4%/ 20|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 128   |      83|      16.380|  38.4%/  2|  46.4%/  1|  48.4%/  1|  50.4%/  1 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 128   |     126|      31.006|   0.7%/ 95|   0.8%/ 87|   0.8%/ 85|   0.8%/ 83 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 129   |      87|       7.784|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 133   |     612|     105.185|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 130   |    1043|     100.694|   1.3%/ 55|   1.2%/ 59|   1.1%/ 60|   1.1%/ 62 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 133   |    5506|     315.201|   0.7%/ 99|   0.6%/108|   0.6%/111|   0.6%/113 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 139   |    4684|      46.708|   1.4%/ 48|   1.1%/ 62|   1.0%/ 67|   1.0%/ 73 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 116   |     385|      59.318|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23|   2.9%/ 23 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  94   |      51|      37.548|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 111   |     199|       2.013|   3.7%/ 19|   4.3%/ 16|   4.4%/ 16|   4.6%/ 15 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 126   |     328|      59.356|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 161   |   30228|     450.653|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 127   |      47|      21.809|   0.3%/269|   0.1%/560|   0.1%/719|   0.1%/962 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 124   |       5|       2.076|   5.5%/ 12|   6.7%/ 10|   7.0%/ 10|   7.3%/  9 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 112   |      16|       4.245|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 138   |    9121|     109.698|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 126   |     158|       5.233|   1.3%/ 55|   1.1%/ 60|   1.1%/ 62|   1.1%/ 63 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 136   |     198|      18.418|   0.3%/215|   0.4%/158|   0.5%/148|   0.5%/138 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 131   |    1724|     103.834|   2.8%/ 25|   2.4%/ 28|   2.3%/ 30|   2.2%/ 31 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 101   |      42|       3.442|   1.1%/ 61|   1.1%/ 61|   1.1%/ 61|   1.1%/ 61 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  90   |      26|      16.268|   0.1%/584|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 111   |     159|      13.745|   1.3%/ 51|   1.0%/ 71|   0.9%/ 79|   0.8%/ 88 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 121   |    1049|     114.528|   2.7%/ 26|   2.6%/ 27|   2.6%/ 27|   2.5%/ 27 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 132   |     598|      61.200|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 136   |   31132|      22.870|   2.5%/ 27|   2.6%/ 27|   2.6%/ 27|   2.6%/ 27 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 136   |    4584|      17.175|   2.2%/ 32|   2.3%/ 30|   2.3%/ 30|   2.4%/ 29 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 156   |   15259|     183.008|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 143   |    4444|     113.578|   2.6%/ 27|   1.9%/ 35|   1.8%/ 38|   1.6%/ 42 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 136   |    1758|     357.301|   0.1%/975|   0.1%/849|   0.1%/820|   0.1%/791 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 126   |     440|      47.878|   1.7%/ 40|   2.0%/ 35|   2.1%/ 33|   2.1%/ 32 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 155   |   35119|     582.992|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 128   |      10|       3.667|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 163   |     992|       7.876|   0.1%/960|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 120   |      11|       1.043|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 122   |     616|      32.972|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 121   |     269|       5.662|   3.0%/ 23|   3.3%/ 21|   3.4%/ 20|   3.5%/ 20 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 121   |     167|      93.109|   4.4%/ 16|   4.6%/ 15|   4.6%/ 15|   4.6%/ 15 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 112   |     424|      95.827|   0.7%/ 96|   0.7%/ 99|   0.7%/100|   0.7%/100 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 113   |     268|      41.092|   5.0%/ 14|   4.4%/ 16|   4.2%/ 16|   4.1%/ 17 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 113   |      31|      16.391|   0.2%/445|   0.1%/614|   0.1%/708|   0.1%/852 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 137   |      43|       6.235|   1.3%/ 53|   1.6%/ 44|   1.7%/ 42|   1.7%/ 40 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 112   |      75|      16.842|   1.2%/ 60|   0.5%/134|   0.3%/201|   0.2%/406 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 114   |      57|       8.278|   3.7%/ 18|   3.4%/ 20|   4.6%/ 15|   4.5%/ 15 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 126   |      80|      28.653|   0.1%/742|   0.1%/709|   0.1%/696|   0.1%/683 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  69   |      78|       2.956|   5.8%/ 12|   5.4%/ 13|   5.3%/ 13|   5.1%/ 14 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 130   |     123|       3.758|   0.1%/745|   0.1%/652|   0.1%/634|   0.1%/618 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 118   |     123|       6.065|   0.2%/360|   0.2%/412|   0.2%/419|   0.2%/424 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 117   |     160|      39.162|   0.6%/107|   0.4%/164|   0.4%/191|   0.3%/229 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 128   |   42818|     338.278|   1.7%/ 42|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 129   |     730|     272.236|   1.1%/ 64|   1.0%/ 71|   1.0%/ 73|   0.9%/ 74 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 137   |     289|       8.043|   1.4%/ 51|   1.5%/ 45|   1.6%/ 43|   1.6%/ 42 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  61   |      11|       0.380|   2.1%/ 32|   2.3%/ 30|   2.2%/ 31|   2.2%/ 32 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  15   |       7|       2.847|   0.0%/ --|  32.6%/  2|  20.5%/  3|   0.0%/ -- |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  70   |      43|       1.431|   1.1%/ 60|   1.6%/ 44|   1.7%/ 40|   1.9%/ 37 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 141   |    6162|     353.009|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 118   |      22|       4.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 120   |     109|      16.805|   1.4%/ 51|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 122   |      69|       3.102|   0.1%/857|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 124   |     850|       4.121|   1.3%/ 55|   1.1%/ 63|   1.1%/ 66|   1.0%/ 69 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 125   |     455|     218.984|   1.5%/ 47|   1.3%/ 51|   1.3%/ 52|   1.3%/ 54 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 133   |     256|      47.632|   0.1%/863|   0.1%/958|   0.1%/992|   0.1%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 116   |     366|      78.440|   2.9%/ 23|   2.9%/ 24|   2.8%/ 24|   2.8%/ 24 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 128   |    5913|      26.959|   0.9%/ 76|   0.7%/104|   0.6%/114|   0.5%/127 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 136   |    1257|     298.067|   2.7%/ 26|   2.6%/ 26|   2.6%/ 27|   2.6%/ 27 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 126   |      37|       5.159|   4.1%/ 17|   4.7%/ 15|   4.9%/ 14|   5.0%/ 14 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 127   |   14240|     443.194|   1.4%/ 48|   1.3%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 174   |    1897|      17.480|   0.8%/ 85|   0.8%/ 83|   0.8%/ 83|   0.8%/ 83 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 135   |    1663|      43.337|   0.4%/158|   0.4%/183|   0.4%/190|   0.3%/198 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 130   |    1717|     167.086|   0.3%/245|   0.2%/294|   0.2%/310|   0.2%/327 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 119   |     168|      60.996|   1.1%/ 61|   0.8%/ 85|   0.7%/ 94|   0.7%/106 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 125   |    2144|     110.485|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 128   |   13169|      89.740|   1.2%/ 56|   1.1%/ 62|   1.1%/ 64|   1.0%/ 66 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  56   |       5|       0.424|   3.3%/ 21|   1.8%/ 38|   1.3%/ 54|   0.7%/106 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 123   |    2716|      79.371|   1.7%/ 42|   1.4%/ 50|   1.3%/ 53|   1.2%/ 55 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 115   |     181|      11.192|   1.7%/ 40|   1.6%/ 42|   1.6%/ 42|   1.6%/ 43 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 127   |     536|      76.974|   2.4%/ 28|   2.3%/ 30|   2.3%/ 30|   2.2%/ 31 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  93   |      66|       8.404|   0.4%/193|   0.4%/194|   0.4%/195|   0.4%/197 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 126   |      27|       4.770|   0.2%/403|   0.2%/403|   0.2%/410|   0.2%/420 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 119   |      28|       5.132|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 133   |     114|      54.233|   0.3%/257|   0.4%/182|   0.4%/169|   0.4%/157 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 108   |      93|       5.872|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 120   |    6156|     104.746|   3.8%/ 18|   3.9%/ 17|   4.0%/ 17|   4.0%/ 17 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 144   |   28437|     603.744|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 119   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 134   |     715|      16.849|   0.8%/ 86|   0.8%/ 89|   0.8%/ 89|   0.8%/ 90 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 136   |    5701|     551.405|   0.2%/291|   0.2%/321|   0.2%/329|   0.2%/337 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 142   |    1973|     229.348|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 118   |      36|       2.057|   4.4%/ 16|   8.6%/  8|   6.5%/ 11|   4.1%/ 17 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 116   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 146   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 120   |      16|       2.077|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 122   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 128   |      50|       4.265|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 130   |    5588|      67.197|   0.3%/204|   0.3%/210|   0.3%/212|   0.3%/214 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 147   |  144594|     438.768|   0.6%/118|   0.6%/113|   0.6%/112|   0.6%/111 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 134   |    1604|      38.296|   1.1%/ 61|   1.0%/ 68|   1.0%/ 70|   1.0%/ 72 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 127   |     345|      34.849|   0.3%/233|   0.2%/285|   0.2%/302|   0.2%/321 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 136   |   45787|     689.191|   0.2%/444|   0.1%/492|   0.1%/506|   0.1%/520 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 118   |      34|       9.777|   1.0%/ 68|   1.0%/ 68|   1.0%/ 68|   1.0%/ 68 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 120   |     116|       3.384|   5.3%/ 13|   4.4%/ 15|   4.2%/ 16|   4.0%/ 17 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 120   |     137|       4.242|   3.6%/ 19|   3.1%/ 22|   3.0%/ 23|   2.9%/ 23 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 114   |     160|       8.940|  10.1%/  7|  11.7%/  6|  12.1%/  6|  12.3%/  5 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 124   |      34|       2.252|   6.2%/ 11|   5.1%/ 13|   4.8%/ 14|   4.4%/ 15 |

