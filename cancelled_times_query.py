import requests
import json
import os
from datetime import date
from dotenv import load_dotenv

class Cancelled_times_query:
  
  def __init__(self):
     
    load_dotenv()
    DIGITRANSIT_SUBSCRIPTION_KEY = os.getenv('DIGITRANSIT-SUBSCRIPTION-KEY')
    self.url = 'https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'
    self.hdr = {
      'Cache-Control': 'no-cache',
      'digitransit-subscription-key': DIGITRANSIT_SUBSCRIPTION_KEY,
      }
    self.body = '''
    {
      cancelledTripTimes(
        feeds: ["HSL"]
      ) {
        scheduledDeparture
        serviceDay
        trip {
          gtfsId
          tripHeadsign
          routeShortName
          directionId
          pattern {
            code
            name
          }
          route {
            gtfsId
            longName
          }
        }
        realtimeState
        headsign
      }
    }
    '''

  def print(self):
    response = requests.post(url=self.url, headers = self.hdr, json={"query": self.body})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        parsed_response = json.loads(response.content)
        print("response : ", json.dumps(parsed_response, indent = 4))
    else:
      print("There was a problem retrieving the data, do you have an active API key in a .env file?")
  
  def write(self):
     
    response = requests.post(url=self.url, headers = self.hdr, json={"query": self.body})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
      parsed_response = json.loads(response.content)
      today=date.today()
      current_date = today.strftime("%d.%m.%Y")
      
      filename = (current_date + ' cancelled-trip-times-data')
      path = os.getcwd()+"\\data\\"+filename
      file = open('%s.json' % path, 'w')
      file.write(json.dumps(parsed_response, indent = 4))
      file.close()
      print("data succesfully written to " + filename + '.json in the data folder')

  
  