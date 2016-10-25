####Python Script to pull Daily Summaries for RDU ####
#Author - Andrew Kramer#

import json
import requests
import pandas as pd

#Call the Dataset
url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=GHCND:USW00013722&startdate=2010-01-01&enddate=2016-09-01'
#url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=PRECIP_HLY&stationid=COOP:317069&startdate=2011-01-01&enddate=2011-01-10'
headers = {'token': 'dKuJxEKlhIJuoZSjvKULivIPXWsRqspt' }

#Execute call and parse response
response = requests.get(url, headers=headers)
#parsed=json.loads(response.text)

#for year in parsed['results']:
	#print(year)
print(response.text)