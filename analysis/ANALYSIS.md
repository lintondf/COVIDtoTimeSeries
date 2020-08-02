# State and Country COVID-19 Analysis #
## Updated: at 2020-08-02 for data as of 2020-08-01 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 36.2% of deaths and 40.0% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 68.8% of deaths and 56.0% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 123   |   32721|    1681.988|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 123   |   15864|    1786.002|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 123   |    9244|     233.955|   1.5%/ 47|   1.5%/ 45|   1.6%/ 44|   1.6%/ 43 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 123   |    8619|    1240.266|   0.2%/392|   0.2%/401|   0.2%/403|   0.2%/405 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 123   |    7702|     607.787|   0.2%/326|   0.2%/339|   0.2%/342|   0.2%/344 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 123   |    7225|     564.371|   0.2%/321|   0.2%/346|   0.2%/352|   0.2%/358 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 123   |    6847|     318.799|   2.7%/ 26|   2.9%/ 24|   3.0%/ 23|   3.1%/ 23 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 123   |    6761|     233.161|   3.8%/ 18|   4.0%/ 17|   4.1%/ 17|   4.2%/ 17 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 123   |    6452|     646.092|   0.1%/614|   0.1%/648|   0.1%/654|   0.1%/658 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 123   |    4438|    1244.664|   0.1%/976|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 123   |  153503|     465.804|   0.7%/ 97|   0.8%/ 88|   0.8%/ 87|   0.8%/ 85 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 123   |   93843|     443.889|   1.3%/ 55|   1.2%/ 57|   1.2%/ 58|   1.2%/ 58 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 123   |   47640|     376.373|   1.5%/ 48|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 123   |   46252|     696.198|   0.1%/472|   0.1%/485|   0.1%/488|   0.1%/490 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 123   |   37554|      27.589|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 123   |   35161|     583.688|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 123   |   30275|     451.347|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 123   |   28446|     603.942|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 123   |   20106|     625.754|   1.1%/ 65|   0.9%/ 79|   0.8%/ 84|   0.8%/ 89 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 123   |   17066|     204.680|   1.4%/ 50|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 123   |    1622|     330.711|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 123   |      23|      31.378|   2.2%/ 32|   2.8%/ 25|   3.0%/ 23|   3.1%/ 22 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 123   |    3822|     525.025|   2.6%/ 27|   2.4%/ 29|   2.4%/ 29|   2.3%/ 30 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 123   |     455|     150.671|   1.9%/ 36|   2.0%/ 34|   2.1%/ 33|   2.1%/ 33 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 123   |    9244|     233.955|   1.5%/ 47|   1.5%/ 45|   1.6%/ 44|   1.6%/ 43 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 123   |    1835|     318.637|   0.4%/195|   0.4%/175|   0.4%/170|   0.4%/166 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 123   |    4438|    1244.664|   0.1%/976|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 123   |     591|     606.962|   0.2%/408|   0.2%/396|   0.2%/394|   0.2%/392 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 123   |    6847|     318.799|   2.7%/ 26|   2.9%/ 24|   3.0%/ 23|   3.1%/ 23 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 123   |    3760|     354.111|   1.3%/ 53|   1.5%/ 46|   1.5%/ 45|   1.6%/ 44 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 123   |      27|      19.114|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 123   |     174|      97.163|   3.9%/ 18|   4.6%/ 15|   4.8%/ 14|   5.0%/ 14 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 123   |    7702|     607.787|   0.2%/326|   0.2%/339|   0.2%/342|   0.2%/344 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 123   |    2968|     440.923|   0.4%/180|   0.4%/172|   0.4%/170|   0.4%/168 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 123   |     873|     276.543|   0.8%/ 89|   0.8%/ 84|   0.8%/ 83|   0.8%/ 82 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 123   |     355|     121.828|   1.1%/ 61|   1.3%/ 52|   1.4%/ 50|   1.4%/ 48 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 123   |     740|     165.661|   0.8%/ 82|   0.8%/ 82|   0.9%/ 81|   0.9%/ 81 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 123   |    3948|     849.304|   0.9%/ 80|   1.0%/ 70|   1.0%/ 68|   1.0%/ 66 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 123   |     123|      91.332|   0.4%/155|   0.5%/153|   0.5%/152|   0.5%/151 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 123   |    3501|     579.132|   0.3%/241|   0.3%/234|   0.3%/232|   0.3%/229 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 123   |    8619|    1240.266|   0.2%/392|   0.2%/401|   0.2%/403|   0.2%/405 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 123   |    6452|     646.092|   0.1%/614|   0.1%/648|   0.1%/654|   0.1%/658 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 123   |    1645|     291.707|   0.3%/217|   0.3%/221|   0.3%/222|   0.3%/222 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 123   |    1643|     552.000|   1.7%/ 41|   1.9%/ 37|   1.9%/ 36|   2.0%/ 35 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 123   |    1269|     206.686|   0.8%/ 83|   0.9%/ 75|   0.9%/ 73|   1.0%/ 71 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 123   |      59|      55.204|   3.9%/ 18|   4.4%/ 16|   4.5%/ 15|   4.7%/ 15 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 123   |     332|     171.816|   0.7%/ 93|   0.8%/ 90|   0.8%/ 89|   0.8%/ 88 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 123   |     822|     266.966|   1.9%/ 37|   2.1%/ 34|   2.1%/ 33|   2.2%/ 32 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 123   |     416|     306.057|   0.3%/203|   0.4%/193|   0.4%/191|   0.4%/189 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 123   |   15864|    1786.002|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 123   |     647|     308.679|   0.9%/ 75|   1.0%/ 72|   1.0%/ 71|   1.0%/ 70 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 123   |   32721|    1681.988|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 123   |    1967|     187.547|   1.3%/ 52|   1.4%/ 50|   1.4%/ 50|   1.4%/ 49 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 123   |     104|     137.071|   0.9%/ 76|   0.9%/ 78|   0.9%/ 79|   0.9%/ 80 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 123   |    3483|     297.974|   0.8%/ 88|   0.9%/ 78|   0.9%/ 76|   0.9%/ 74 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 123   |     541|     136.621|   1.5%/ 46|   1.7%/ 41|   1.7%/ 40|   1.8%/ 38 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 123   |     322|      76.251|   1.8%/ 39|   1.9%/ 36|   2.0%/ 35|   2.0%/ 34 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 123   |    7225|     564.371|   0.2%/321|   0.2%/346|   0.2%/352|   0.2%/358 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 123   |     220|      68.817|   1.7%/ 42|   1.9%/ 37|   1.9%/ 36|   2.0%/ 35 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 123   |    1011|     954.188|   0.1%/581|   0.1%/832|   0.1%/934|   0.1%/ *** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 123   |    1764|     342.676|   3.1%/ 22|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 123   |     131|     148.508|   1.0%/ 69|   1.0%/ 70|   1.0%/ 70|   1.0%/ 70 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 123   |    1077|     157.678|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 123   |    6761|     233.161|   3.8%/ 18|   4.0%/ 17|   4.1%/ 17|   4.2%/ 17 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 123   |  153503|     465.804|   0.7%/ 97|   0.8%/ 88|   0.8%/ 87|   0.8%/ 85 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 123   |     309|      96.501|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 123   |      56|      90.465|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 123   |    2160|     253.031|   0.6%/118|   0.7%/105|   0.7%/101|   0.7%/ 98 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 123   |    1571|     206.356|   0.7%/103|   0.7%/ 96|   0.7%/ 94|   0.8%/ 92 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 123   |     112|      62.325|   1.2%/ 59|   1.5%/ 46|   1.6%/ 44|   1.7%/ 41 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 123   |     932|     160.079|   0.8%/ 88|   0.9%/ 75|   1.0%/ 72|   1.0%/ 70 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 111   |      27|      45.820|   0.6%/110|   0.5%/154|   0.4%/171|   0.4%/191 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 123   |    1329|      41.237|   0.8%/ 83|   0.4%/175|   0.3%/244|   0.2%/402 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 123   |     163|      57.147|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25|   2.8%/ 25 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 123   |    1222|      28.410|   1.0%/ 72|   1.0%/ 70|   1.0%/ 70|   1.0%/ 70 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 123   |      52|       1.677|   4.7%/ 15|   5.4%/ 13|   5.6%/ 12|   5.8%/ 12 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 123   |    3634|      80.860|   3.5%/ 20|   3.6%/ 19|   3.7%/ 19|   3.7%/ 19 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 123   |     762|     257.613|   1.2%/ 57|   0.9%/ 73|   0.9%/ 79|   0.8%/ 86 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 123   |     189|       7.371|   4.3%/ 16|   5.4%/ 13|   5.6%/ 12|   5.9%/ 12 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 123   |     717|      80.488|   0.1%/764|   0.1%/618|   0.1%/586|   0.1%/556 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 123   |     466|      46.255|   1.9%/ 37|   1.6%/ 43|   1.6%/ 44|   1.5%/ 46 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 123   |     152|      98.166|   1.3%/ 52|   1.1%/ 63|   1.0%/ 66|   1.0%/ 70 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 123   |    3179|      18.871|   1.4%/ 49|   1.3%/ 53|   1.3%/ 54|   1.2%/ 55 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 123   |     565|      60.051|   0.9%/ 73|   0.9%/ 78|   0.9%/ 79|   0.9%/ 80 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 123   |    9843|     854.068|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 118   |      38|       3.240|   1.3%/ 54|   0.8%/ 83|   0.7%/ 95|   0.6%/112 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 123   |    3045|     265.502|   2.7%/ 25|   2.7%/ 26|   2.7%/ 26|   2.7%/ 26 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 123   |     331|     100.184|   2.1%/ 33|   2.3%/ 31|   2.3%/ 30|   2.3%/ 30 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 123   |       1|       0.428|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 123   |   93843|     443.889|   1.3%/ 55|   1.2%/ 57|   1.2%/ 58|   1.2%/ 58 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 123   |     384|      55.173|   1.9%/ 37|   2.0%/ 34|   2.0%/ 34|   2.1%/ 33 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 123   |      53|       2.540|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 111   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 123   |     396|      14.929|   0.4%/188|   0.3%/229|   0.3%/245|   0.3%/264 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 123   |    8987|     236.512|   0.1%/826|   0.1%/909|   0.1%/928|   0.1%/947 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  71   |      60|      10.855|   0.6%/107|   0.1%/922|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  96   |      75|       4.617|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 123   |    9880|     517.102|   0.9%/ 77|   0.8%/ 86|   0.8%/ 89|   0.8%/ 91 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 123   |    4661|       3.324|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 123   |   10366|     209.860|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 123   |     168|      33.192|   8.0%/  9|   7.8%/  9|   7.7%/  9|   7.7%/  9 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 123   |     145|      35.551|   1.3%/ 55|   1.5%/ 47|   1.5%/ 45|   1.6%/ 43 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 123   |      87|       7.767|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 123   |     615|     105.588|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 123   |    1165|     112.511|   1.5%/ 46|   1.6%/ 45|   1.6%/ 44|   1.6%/ 44 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 123   |    5738|     328.483|   0.6%/113|   0.6%/120|   0.6%/121|   0.6%/123 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 123   |    4915|      49.015|   1.0%/ 70|   0.7%/ 93|   0.7%/101|   0.6%/110 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 123   |     469|      72.338|   2.6%/ 26|   2.4%/ 29|   2.4%/ 29|   2.3%/ 30 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 102   |      51|      37.548|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 119   |     282|       2.853|   4.2%/ 16|   4.5%/ 15|   4.5%/ 15|   4.6%/ 15 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 123   |     329|      59.510|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 123   |   30275|     451.347|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 123   |      50|      22.862|   0.4%/172|   0.5%/149|   0.5%/144|   0.5%/141 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 123   |       9|       3.955|   6.6%/ 10|   7.3%/  9|   7.5%/  9|   7.7%/  9 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 120   |      17|       4.542|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 123   |    9150|     110.037|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 123   |     181|       5.971|   1.6%/ 43|   1.7%/ 40|   1.8%/ 39|   1.8%/ 38 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 123   |     206|      19.174|   0.3%/216|   0.4%/181|   0.4%/175|   0.4%/169 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 123   |    1982|     119.369|   2.2%/ 31|   1.9%/ 36|   1.9%/ 37|   1.8%/ 39 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 109   |      47|       3.835|   1.2%/ 59|   1.1%/ 60|   1.1%/ 61|   1.1%/ 61 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  98   |      26|      16.338|   0.1%/668|   0.2%/325|   0.2%/285|   0.3%/253 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 119   |     165|      14.229|   0.8%/ 91|   0.5%/127|   0.5%/139|   0.4%/154 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 123   |    1358|     148.249|   3.2%/ 22|   3.4%/ 20|   3.5%/ 20|   3.5%/ 19 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 123   |     597|      61.057|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 123   |   37554|      27.589|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 123   |    5297|      19.844|   1.7%/ 40|   1.6%/ 43|   1.6%/ 44|   1.5%/ 45 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 123   |   17066|     204.680|   1.4%/ 50|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 123   |    4929|     125.974|   1.9%/ 36|   1.6%/ 43|   1.5%/ 46|   1.4%/ 48 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 123   |    1767|     359.063|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 123   |     521|      56.732|   1.9%/ 36|   2.0%/ 34|   2.1%/ 34|   2.1%/ 33 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 123   |   35161|     583.688|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 123   |      10|       3.667|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 123   |    1007|       7.993|   0.2%/390|   0.2%/306|   0.2%/290|   0.3%/275 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 123   |      11|       1.055|   0.3%/230|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 123   |     852|      45.594|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 123   |     344|       7.232|   3.3%/ 21|   3.6%/ 19|   3.6%/ 19|   3.7%/ 19 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 123   |     222|     123.381|   4.0%/ 17|   3.8%/ 18|   3.8%/ 18|   3.7%/ 19 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 120   |     452|     102.336|   0.8%/ 92|   0.8%/ 90|   0.8%/ 90|   0.8%/ 90 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 121   |    1453|     222.376|   2.7%/ 25|   1.8%/ 39|   1.5%/ 45|   1.3%/ 53 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 121   |      31|      16.498|   0.2%/330|   0.2%/280|   0.3%/266|   0.3%/252 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 123   |      59|       8.649|   3.0%/ 23|   3.7%/ 19|   3.9%/ 18|   4.1%/ 17 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 120   |      80|      17.834|   0.6%/113|   0.4%/193|   0.3%/224|   0.3%/260 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 122   |      77|      11.195|   2.3%/ 30|   4.5%/ 15|   3.4%/ 20|   1.7%/ 40 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 123   |      80|      28.727|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  77   |     113|       4.288|   5.1%/ 13|   4.7%/ 15|   4.6%/ 15|   4.5%/ 15 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 123   |     125|       3.805|   0.1%/484|   0.2%/421|   0.2%/408|   0.2%/395 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 123   |     124|       6.143|   0.1%/483|   0.1%/504|   0.1%/510|   0.1%/518 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 123   |     159|      38.969|   0.2%/306|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 123   |   47640|     376.373|   1.5%/ 48|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 123   |     786|     292.989|   1.0%/ 67|   1.0%/ 67|   1.0%/ 67|   1.0%/ 67 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 123   |     340|       9.490|   2.2%/ 32|   2.6%/ 27|   2.7%/ 26|   2.8%/ 25 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  69   |      11|       0.376|   0.7%/ 94|   0.4%/174|   0.4%/186|   0.4%/187 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  23   |      11|       4.473|   2.3%/ 30|   6.7%/ 10|   7.2%/  9|   7.4%/  9 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  78   |      55|       1.832|   2.5%/ 28|   3.6%/ 19|   3.8%/ 18|   4.1%/ 17 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 123   |    6165|     353.160|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 123   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 123   |     118|      18.273|   1.1%/ 63|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 123   |      69|       3.100|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 123   |     901|       4.372|   0.8%/ 82|   0.6%/107|   0.6%/116|   0.5%/127 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 123   |     497|     239.304|   1.2%/ 57|   1.1%/ 63|   1.1%/ 65|   1.0%/ 67 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 123   |     256|      47.617|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 123   |     443|      94.989|   2.4%/ 29|   2.1%/ 32|   2.1%/ 33|   2.0%/ 35 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 123   |    6033|      27.507|   0.5%/134|   0.3%/209|   0.3%/242|   0.2%/287 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 123   |    1482|     351.179|   2.2%/ 31|   2.0%/ 35|   1.9%/ 36|   1.9%/ 37 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 123   |      52|       7.292|   3.8%/ 18|   3.9%/ 18|   3.9%/ 17|   4.0%/ 17 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 123   |   20106|     625.754|   1.1%/ 65|   0.9%/ 79|   0.8%/ 84|   0.8%/ 89 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 123   |    2057|      18.956|   0.8%/ 86|   0.7%/ 96|   0.7%/ 99|   0.7%/102 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 123   |    1718|      44.771|   0.5%/148|   0.5%/144|   0.5%/142|   0.5%/141 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 123   |    1739|     169.252|   0.2%/326|   0.2%/379|   0.2%/394|   0.2%/411 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 123   |     174|      63.439|   0.8%/ 84|   0.7%/ 95|   0.7%/ 97|   0.7%/100 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 123   |    2348|     121.012|   1.2%/ 57|   1.3%/ 54|   1.3%/ 53|   1.3%/ 52 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 123   |   14122|      96.236|   1.0%/ 67|   0.9%/ 74|   0.9%/ 76|   0.9%/ 78 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  64   |       5|       0.404|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 123   |    2943|      86.015|   1.2%/ 57|   1.0%/ 70|   0.9%/ 74|   0.9%/ 78 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 123   |     211|      13.006|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 123   |     596|      85.594|   1.7%/ 40|   1.4%/ 50|   1.3%/ 53|   1.2%/ 57 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 101   |      67|       8.501|   0.2%/278|   0.2%/376|   0.2%/407|   0.2%/440 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 123   |      27|       4.760|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 123   |      28|       5.132|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 123   |     118|      56.583|   0.3%/216|   0.4%/167|   0.4%/158|   0.5%/150 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 116   |      93|       5.856|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 123   |    8353|     142.125|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 123   |   28446|     603.942|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 123   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 123   |     747|      17.604|   0.6%/107|   0.6%/112|   0.6%/113|   0.6%/115 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 123   |    5761|     557.269|   0.2%/402|   0.1%/480|   0.1%/505|   0.1%/532 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 123   |    1981|     230.274|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 123   |      48|       2.741|   3.9%/ 18|   2.6%/ 26|   2.3%/ 30|   2.0%/ 34 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 123   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 123   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 123   |      19|       2.484|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 123   |       8|       5.865|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 123   |      50|       4.274|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 123   |    5716|      68.738|   0.3%/231|   0.3%/247|   0.3%/251|   0.3%/255 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 123   |  153503|     465.804|   0.7%/ 97|   0.8%/ 88|   0.8%/ 87|   0.8%/ 85 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 123   |    1731|      41.340|   1.1%/ 64|   1.1%/ 65|   1.1%/ 65|   1.1%/ 65 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 123   |     351|      35.451|   0.3%/243|   0.3%/244|   0.3%/243|   0.3%/242 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 123   |   46252|     696.198|   0.1%/472|   0.1%/485|   0.1%/488|   0.1%/490 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 123   |      36|      10.173|   0.6%/121|   0.4%/189|   0.3%/220|   0.3%/265 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 123   |     150|       4.406|   4.2%/ 16|   3.7%/ 19|   3.6%/ 19|   3.5%/ 20 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 123   |     171|       5.310|   3.1%/ 22|   2.9%/ 24|   2.8%/ 25|   2.7%/ 25 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 122   |     185|      10.339|   1.2%/ 56|   2.1%/ 33|   2.1%/ 33|   4.2%/ 16 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 123   |      47|       3.092|   8.4%/  8|   9.5%/  7|   9.8%/  7|  10.1%/  7 |

