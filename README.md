# COVIDtoTimeSeries

Extracts the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

Writes a by-country and a by-state csv file containing the time series.

## To Use ##

Install Python and the pip install pandas

git clone the JHU CSSE repository

Edit the Main.py module and update the pathToRepository string to point to the checkout path.

Run:

python src/Main.py

