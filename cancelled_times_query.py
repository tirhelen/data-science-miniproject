import requests
import json
import os
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
        print(response.content)
        parsed_response = json.loads(response.content)
        print("response : ", json.dumps(parsed_response, indent = 4))
  
  def write(self):
     
    response = requests.post(url=self.url, headers = self.hdr, json={"query": self.body})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
      parsed_response = json.loads(response.content)
      file = open('cancelled-trip-times-data.json', 'w')
      file.write(json.dumps(parsed_response, indent = 4))
      file.close()
      print("data succesfully written to cancelled-trip-times-data.json")

  
  