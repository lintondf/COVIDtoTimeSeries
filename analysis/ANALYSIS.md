# State and Country COVID-19 Analysis #
## Updated: at 2020-07-24 for data as of 2020-07-23 ##

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 69.7% of deaths and 57.1% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 132   |   32637|    1677.707|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 136   |   15850|    1784.438|   0.2%/451|   0.1%/638|   0.1%/718|   0.1%/824 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 126   |    8498|    1222.795|   0.2%/368|   0.2%/417|   0.2%/432|   0.2%/448 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 142   |    8146|     206.157|   1.3%/ 53|   1.3%/ 51|   1.3%/ 51|   1.4%/ 51 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 129   |    7621|     601.420|   0.3%/249|   0.2%/344|   0.2%/382|   0.2%/431 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 127   |    7102|     554.773|   0.3%/271|   0.2%/293|   0.2%/300|   0.2%/306 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 127   |    6407|     641.498|   0.1%/507|   0.1%/566|   0.1%/585|   0.1%/605 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 138   |    5360|     249.563|   2.2%/ 31|   2.5%/ 28|   2.5%/ 27|   2.6%/ 26 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 129   |    4460|     153.827|   3.1%/ 22|   3.5%/ 20|   3.6%/ 19|   3.7%/ 19 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 127   |    4413|    1237.899|   0.1%/709|   0.1%/679|   0.1%/673|   0.1%/668 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 146   |  143639|     435.872|   0.6%/124|   0.6%/121|   0.6%/120|   0.6%/119 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 129   |   84463|     399.518|   1.4%/ 49|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 135   |   45715|     688.105|   0.2%/449|   0.1%/512|   0.1%/530|   0.1%/550 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 127   |   42137|     332.896|   1.6%/ 42|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 154   |   35109|     582.837|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 135   |   30343|      22.291|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 160   |   30217|     450.485|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 143   |   28435|     603.702|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 126   |   14032|     436.721|   1.5%/ 47|   1.4%/ 50|   1.3%/ 51|   1.3%/ 52 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 155   |   15035|     180.328|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 121   |    1376|     280.588|   1.8%/ 38|   1.9%/ 36|   2.0%/ 35|   2.0%/ 35 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 121   |      19|      25.591|   0.9%/ 73|   1.1%/ 64|   1.1%/ 62|   1.2%/ 60 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 125   |    3048|     418.697|   3.0%/ 23|   3.1%/ 22|   3.2%/ 22|   3.2%/ 21 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 122   |     383|     126.995|   1.6%/ 42|   1.7%/ 40|   1.8%/ 39|   1.8%/ 39 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 142   |    8146|     206.157|   1.3%/ 53|   1.3%/ 51|   1.3%/ 51|   1.4%/ 51 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 132   |    1773|     307.927|   0.3%/263|   0.3%/236|   0.3%/230|   0.3%/225 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 127   |    4413|    1237.899|   0.1%/709|   0.1%/679|   0.1%/673|   0.1%/668 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 120   |     527|     541.044|   0.2%/393|   0.2%/353|   0.2%/344|   0.2%/335 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 138   |    5360|     249.563|   2.2%/ 31|   2.5%/ 28|   2.5%/ 27|   2.6%/ 26 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 134   |    3288|     309.721|   0.9%/ 74|   1.1%/ 64|   1.1%/ 61|   1.2%/ 59 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 115   |      25|      17.910|   0.9%/ 79|   1.3%/ 53|   1.4%/ 49|   1.5%/ 46 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 120   |     128|      71.466|   2.2%/ 32|   2.7%/ 26|   2.8%/ 24|   3.0%/ 23 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 129   |    7621|     601.420|   0.3%/249|   0.2%/344|   0.2%/382|   0.2%/431 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 130   |    2867|     425.913|   0.4%/190|   0.4%/187|   0.4%/186|   0.4%/185 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 121   |     815|     258.288|   0.7%/ 96|   0.8%/ 84|   0.8%/ 82|   0.9%/ 80 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 133   |     320|     109.748|   0.7%/ 96|   0.8%/ 92|   0.8%/ 91|   0.8%/ 89 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 130   |     688|     153.954|   0.8%/ 88|   0.8%/ 92|   0.7%/ 93|   0.7%/ 95 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 132   |    3576|     769.203|   0.4%/159|   0.4%/164|   0.4%/166|   0.4%/168 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 119   |     119|      88.559|   0.5%/143|   0.4%/162|   0.4%/167|   0.4%/174 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 127   |    3417|     565.218|   0.3%/251|   0.3%/270|   0.3%/275|   0.2%/280 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 126   |    8498|    1222.795|   0.2%/368|   0.2%/417|   0.2%/432|   0.2%/448 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 127   |    6407|     641.498|   0.1%/507|   0.1%/566|   0.1%/585|   0.1%/605 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 125   |    1601|     283.884|   0.3%/214|   0.3%/226|   0.3%/229|   0.3%/233 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 127   |    1432|     481.169|   1.3%/ 52|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 127   |    1169|     190.483|   0.6%/113|   0.6%/111|   0.6%/110|   0.6%/110 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 119   |      43|      40.362|   2.6%/ 26|   3.2%/ 22|   3.3%/ 21|   3.4%/ 20 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 118   |     311|     160.979|   0.7%/ 96|   0.9%/ 79|   0.9%/ 75|   1.0%/ 72 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 130   |     694|     225.190|   1.6%/ 43|   1.8%/ 38|   1.9%/ 37|   1.9%/ 36 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 123   |     404|     296.896|   0.3%/221|   0.3%/255|   0.3%/263|   0.3%/272 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 136   |   15850|    1784.438|   0.2%/451|   0.1%/638|   0.1%/718|   0.1%/824 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 121   |     594|     283.143|   0.8%/ 82|   0.9%/ 78|   0.9%/ 76|   0.9%/ 75 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 132   |   32637|    1677.707|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 121   |    1736|     165.499|   1.2%/ 57|   1.4%/ 51|   1.4%/ 50|   1.4%/ 49 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 119   |      96|     125.469|   1.0%/ 69|   1.1%/ 61|   1.2%/ 59|   1.2%/ 57 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 126   |    3242|     277.352|   0.6%/114|   0.6%/108|   0.6%/107|   0.7%/105 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 127   |     469|     118.456|   1.1%/ 65|   1.2%/ 57|   1.2%/ 55|   1.3%/ 54 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 131   |     273|      64.819|   1.4%/ 50|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 127   |    7102|     554.773|   0.3%/271|   0.2%/293|   0.2%/300|   0.2%/306 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 125   |     185|      58.017|   1.1%/ 66|   1.2%/ 57|   1.2%/ 56|   1.3%/ 54 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 118   |    1001|     945.246|   0.2%/351|   0.2%/415|   0.2%/434|   0.2%/455 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 130   |    1273|     247.164|   2.8%/ 25|   3.1%/ 22|   3.2%/ 22|   3.3%/ 21 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 135   |     123|     138.631|   1.0%/ 66|   1.0%/ 72|   0.9%/ 74|   0.9%/ 76 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 125   |     908|     132.868|   1.9%/ 36|   2.0%/ 35|   2.0%/ 35|   2.0%/ 34 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 129   |    4460|     153.827|   3.1%/ 22|   3.5%/ 20|   3.6%/ 19|   3.7%/ 19 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 146   |  143639|     435.872|   0.6%/124|   0.6%/121|   0.6%/120|   0.6%/119 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 124   |     265|      82.625|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 126   |      56|      89.745|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 132   |    2086|     244.361|   0.5%/138|   0.4%/192|   0.3%/213|   0.3%/240 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 146   |    1478|     194.076|   0.5%/140|   0.5%/145|   0.5%/147|   0.5%/148 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 116   |     102|      56.752|   0.5%/150|   0.5%/136|   0.5%/133|   0.5%/130 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 126   |     863|     148.155|   0.5%/127|   0.6%/109|   0.7%/105|   0.7%/101 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 102   |      25|      43.945|   1.0%/ 66|   1.2%/ 58|   1.2%/ 56|   1.3%/ 55 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 124   |    1261|      39.145|   1.7%/ 40|   1.3%/ 51|   1.2%/ 55|   1.2%/ 60 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 135   |     126|      44.260|   2.7%/ 26|   2.4%/ 29|   2.3%/ 30|   2.2%/ 31 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 134   |    1118|      25.998|   0.9%/ 74|   1.0%/ 72|   1.0%/ 71|   1.0%/ 70 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 117   |      34|       1.080|   3.7%/ 19|   1.1%/ 61|   4.4%/ 16|   4.4%/ 16 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 138   |    2612|      58.130|   3.3%/ 21|   3.4%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 120   |     692|     234.063|   1.9%/ 37|   1.8%/ 38|   1.8%/ 38|   1.8%/ 39 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 145   |     125|       4.875|   1.7%/ 40|   2.2%/ 31|   2.4%/ 29|   2.5%/ 28 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 134   |     712|      79.978|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 133   |     399|      39.593|   2.4%/ 28|   2.2%/ 31|   2.2%/ 32|   2.1%/ 32 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 130   |     135|      87.315|   1.7%/ 41|   1.5%/ 45|   1.5%/ 47|   1.4%/ 48 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 128   |    2826|      16.775|   1.7%/ 41|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 115   |     522|      55.503|   1.1%/ 65|   0.9%/ 75|   0.9%/ 77|   0.9%/ 80 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 135   |    9812|     851.405|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 109   |      34|       2.917|   2.8%/ 24|   2.6%/ 27|   2.5%/ 27|   2.4%/ 28 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 117   |    2437|     212.496|   2.8%/ 25|   2.4%/ 29|   2.3%/ 30|   2.2%/ 31 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 125   |     270|      81.864|   1.9%/ 37|   2.1%/ 33|   2.1%/ 33|   2.2%/ 32 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 115   |       1|       0.428|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 129   |   84463|     399.518|   1.4%/ 49|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 135   |     324|      46.651|   1.6%/ 43|   1.7%/ 42|   1.7%/ 41|   1.7%/ 41 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 128   |      53|       2.540|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 102   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 121   |     389|      14.657|   0.6%/108|   0.6%/108|   0.6%/108|   0.6%/109 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 137   |    8946|     235.415|   0.1%/676|   0.1%/939|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  62   |      57|      10.377|   0.5%/141|   1.1%/ 63|   1.2%/ 55|   1.4%/ 49 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  87   |      75|       4.629|   0.1%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 124   |    8903|     465.974|   1.2%/ 56|   1.0%/ 67|   1.0%/ 70|   0.9%/ 73 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 135   |    4644|       3.312|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 124   |    7769|     157.288|   3.4%/ 20|   3.1%/ 22|   3.1%/ 23|   3.0%/ 23 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 127   |      76|      14.997|  36.3%/  2|  44.4%/  1|  46.4%/  1|  48.4%/  1 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 127   |     125|      30.731|   0.6%/107|   0.7%/102|   0.7%/101|   0.7%/100 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 128   |      87|       7.784|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 132   |     612|     105.127|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 129   |    1030|      99.484|   1.3%/ 54|   1.2%/ 58|   1.2%/ 59|   1.1%/ 61 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 132   |    5475|     313.402|   0.7%/ 97|   0.7%/106|   0.6%/109|   0.6%/111 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 138   |    4643|      46.301|   1.5%/ 45|   1.2%/ 58|   1.1%/ 62|   1.0%/ 66 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 115   |     374|      57.672|   3.2%/ 22|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  93   |      51|      37.548|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 110   |     191|       1.933|   3.7%/ 19|   4.3%/ 16|   4.5%/ 15|   4.6%/ 15 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 125   |     328|      59.340|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 160   |   30217|     450.485|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 126   |      47|      21.652|   0.2%/348|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 123   |       4|       1.914|   4.5%/ 15|   5.2%/ 13|   5.3%/ 13|   5.5%/ 12 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 111   |      16|       4.213|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 137   |    9118|     109.653|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 125   |     156|       5.155|   1.2%/ 57|   1.0%/ 66|   1.0%/ 68|   1.0%/ 71 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 135   |     196|      18.310|   0.3%/260|   0.4%/192|   0.4%/179|   0.4%/167 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 130   |    1687|     101.609|   2.8%/ 24|   2.4%/ 29|   2.3%/ 30|   2.2%/ 32 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 100   |      42|       3.406|   1.2%/ 60|   1.2%/ 58|   1.2%/ 57|   1.2%/ 57 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  89   |      26|      16.293|   0.2%/454|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 110   |     158|      13.655|   1.4%/ 49|   1.0%/ 68|   0.9%/ 76|   0.8%/ 86 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 120   |    1021|     111.526|   2.7%/ 26|   2.6%/ 27|   2.6%/ 27|   2.6%/ 27 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 131   |     598|      61.196|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 135   |   30343|      22.291|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 135   |    4479|      16.780|   2.1%/ 33|   2.2%/ 31|   2.2%/ 31|   2.3%/ 30 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 155   |   15035|     180.328|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 142   |    4374|     111.793|   2.7%/ 26|   2.0%/ 34|   1.9%/ 37|   1.7%/ 40 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 135   |    1757|     356.921|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 125   |     430|      46.852|   1.7%/ 41|   2.0%/ 35|   2.1%/ 33|   2.1%/ 32 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 154   |   35109|     582.837|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 127   |      10|       3.667|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 162   |     991|       7.869|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 119   |      11|       1.035|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 121   |     600|      32.107|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 120   |     260|       5.473|   3.0%/ 23|   3.3%/ 21|   3.4%/ 20|   3.5%/ 20 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 120   |     161|      89.795|   4.0%/ 17|   4.1%/ 17|   4.2%/ 16|   4.2%/ 16 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 111   |     420|      95.090|   0.7%/101|   0.6%/109|   0.6%/111|   0.6%/113 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 112   |    1309|     200.325|   5.2%/ 13|   4.5%/ 15|   4.3%/ 16|   4.2%/ 16 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 112   |      31|      16.382|   0.2%/399|   0.2%/453|   0.1%/483|   0.1%/524 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 136   |      42|       6.131|   1.1%/ 63|   1.3%/ 54|   1.3%/ 52|   1.4%/ 50 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 111   |      74|      16.589|   1.3%/ 51|   0.7%/ 95|   0.6%/125|   0.4%/184 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 113   |      55|       8.058|   3.8%/ 18|   1.4%/ 50|   3.4%/ 20|   4.6%/ 15 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 125   |      80|      28.629|   0.1%/670|   0.1%/620|   0.1%/603|   0.1%/586 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  68   |      74|       2.815|   5.6%/ 12|   5.7%/ 12|   5.6%/ 12|   5.5%/ 13 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 129   |     123|       3.755|   0.1%/681|   0.1%/562|   0.1%/539|   0.1%/518 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 117   |     123|       6.057|   0.2%/373|   0.1%/482|   0.1%/511|   0.1%/538 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 116   |     159|      39.070|   0.7%/ 96|   0.5%/135|   0.5%/151|   0.4%/171 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 127   |   42137|     332.896|   1.6%/ 42|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 128   |     723|     269.752|   1.1%/ 63|   1.0%/ 69|   1.0%/ 71|   1.0%/ 72 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 136   |     284|       7.921|   1.3%/ 55|   1.4%/ 49|   1.5%/ 47|   1.5%/ 46 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  60   |      11|       0.375|   1.8%/ 38|   2.9%/ 23|   3.2%/ 21|   3.5%/ 20 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  14   |       7|       2.847|   0.0%/ --|  51.8%/  1|  32.6%/  2|  20.5%/  3 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  69   |      42|       1.401|   1.1%/ 62|   1.1%/ 65|   1.1%/ 65|   1.1%/ 64 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 140   |    6163|     353.026|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 117   |      22|       4.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 119   |     107|      16.609|   1.5%/ 46|   1.6%/ 42|   1.7%/ 41|   1.7%/ 40 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 121   |      69|       3.101|   0.1%/766|   0.1%/882|   0.1%/919|   0.1%/962 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 123   |     839|       4.071|   1.3%/ 55|   1.0%/ 66|   1.0%/ 69|   0.9%/ 73 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 124   |     449|     216.317|   1.5%/ 46|   1.3%/ 52|   1.3%/ 53|   1.3%/ 55 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 132   |     256|      47.606|   0.1%/778|   0.1%/809|   0.1%/820|   0.1%/832 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 115   |     357|      76.476|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 127   |    5875|      26.783|   1.0%/ 72|   0.7%/ 97|   0.7%/106|   0.6%/117 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 135   |    1225|     290.343|   2.7%/ 25|   2.6%/ 26|   2.6%/ 26|   2.6%/ 27 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 125   |      35|       4.919|   4.1%/ 17|   4.9%/ 14|   5.1%/ 14|   5.3%/ 13 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 126   |   14032|     436.721|   1.5%/ 47|   1.4%/ 50|   1.3%/ 51|   1.3%/ 52 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 173   |    1865|      17.185|   0.8%/ 84|   0.8%/ 83|   0.8%/ 82|   0.8%/ 82 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 134   |    1658|      43.190|   0.4%/154|   0.4%/179|   0.4%/186|   0.4%/194 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 129   |    1713|     166.721|   0.3%/241|   0.2%/291|   0.2%/308|   0.2%/326 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 118   |     167|      60.693|   1.2%/ 57|   0.9%/ 80|   0.8%/ 89|   0.7%/100 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 124   |    2120|     109.272|   1.1%/ 65|   1.1%/ 66|   1.1%/ 66|   1.0%/ 66 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 127   |   13024|      88.753|   1.3%/ 55|   1.1%/ 62|   1.1%/ 64|   1.1%/ 66 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  55   |       5|       0.417|   3.4%/ 20|   2.5%/ 27|   2.3%/ 31|   1.9%/ 37 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 122   |    2683|      78.422|   1.7%/ 40|   1.4%/ 49|   1.3%/ 52|   1.3%/ 55 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 114   |     178|      11.007|   1.8%/ 39|   1.7%/ 41|   1.7%/ 42|   1.6%/ 42 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 126   |     525|      75.430|   2.5%/ 28|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  92   |      66|       8.382|   0.4%/178|   0.4%/162|   0.4%/159|   0.4%/155 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 125   |      27|       4.763|   0.2%/365|   0.2%/332|   0.2%/328|   0.2%/326 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 118   |      28|       5.132|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 132   |     113|      53.951|   0.3%/268|   0.4%/188|   0.4%/174|   0.4%/161 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 107   |      93|       5.872|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 119   |    5907|     100.495|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 143   |   28435|     603.702|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 118   |      11|       0.505|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 133   |     710|      16.723|   0.8%/ 88|   0.7%/ 94|   0.7%/ 95|   0.7%/ 97 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 135   |    5687|     550.077|   0.2%/298|   0.2%/342|   0.2%/354|   0.2%/367 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 141   |    1972|     229.222|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 117   |      34|       1.950|   6.0%/ 11|   7.4%/  9|   8.6%/  8|   6.5%/ 11 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 115   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 145   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 119   |      15|       2.048|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 121   |       8|       5.865|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 127   |      50|       4.265|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 129   |    5570|      66.984|   0.3%/202|   0.3%/208|   0.3%/209|   0.3%/211 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 146   |  143639|     435.872|   0.6%/124|   0.6%/121|   0.6%/120|   0.6%/119 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 133   |    1588|      37.925|   1.1%/ 60|   1.0%/ 68|   1.0%/ 70|   1.0%/ 73 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 126   |     344|      34.780|   0.3%/222|   0.3%/266|   0.2%/280|   0.2%/296 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 135   |   45715|     688.105|   0.2%/449|   0.1%/512|   0.1%/530|   0.1%/550 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 117   |      34|       9.698|   1.0%/ 68|   1.0%/ 67|   1.0%/ 67|   1.0%/ 67 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 119   |     111|       3.252|   5.6%/ 12|   4.8%/ 14|   4.6%/ 15|   4.4%/ 16 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 119   |     132|       4.107|   3.6%/ 19|   3.1%/ 22|   3.0%/ 23|   2.9%/ 24 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 113   |     152|       8.494|  37.4%/  2|   2.2%/ 32|   2.2%/ 32|   1.5%/ 45 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 123   |      33|       2.172|   6.3%/ 11|   5.3%/ 13|   4.9%/ 14|   4.6%/ 15 |

