####Python Script to pull Daily Summaries for RDU ####
#Author - Andrew Kramer#

import json
import requests
import pandas as pd

#Call the Dataset
url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&stationid=GHCND:USW00013722&startdate=2013-01-01&enddate=2013-02-01'

headers = {'token': 'dKuJxEKlhIJuoZSjvKULivIPXWsRqspt' }

#Execute call and parse response
response = requests.get(url, headers=headers)
#parsed=json.loads(response.text)

print(response.text)