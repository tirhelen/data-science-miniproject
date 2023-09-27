import requests
import os
from dotenv import load_dotenv

load_dotenv()
DIGITRANSIT_SUBSCRIPTION_KEY = os.getenv('DIGITRANSIT-SUBSCRIPTION-KEY')

url = 'https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'

hdr = {
    'Cache-Control': 'no-cache',
    'digitransit-subscription-key': DIGITRANSIT_SUBSCRIPTION_KEY,
    }

body = '''
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

response = requests.post(url=url, headers = hdr, json={"query": body})
print("response status code: ", response.status_code)
if response.status_code == 200:
    print("response : ", response.content)