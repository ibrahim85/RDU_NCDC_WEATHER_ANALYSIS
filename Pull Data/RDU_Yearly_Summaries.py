####Python Script to pull Daily Summaries for RDU ####
#Author - Andrew Kramer#

import json
import requests
import pandas as pd

#Call the Dataset
#url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=GHCND:USW00013722&startdate=2010-01-01&enddate=2016-01-01&limit=100'

url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=GHCND:USW00013722&startdate=2006-01-01&enddate=2016-01-01&limit=100&datatypeid=PRCP&datatypeid=TAVG' #Avg Temp and Precipitation per month at rdu
headers = {'token': 'dKuJxEKlhIJuoZSjvKULivIPXWsRqspt' }

#Execute call and parse response
response = requests.get(url, headers=headers)
parsed=json.loads(response.text)

year=[]
PRCP=[]
TAVG=[]
for year in parsed['results']:
	print(year)

