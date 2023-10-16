import requests
import json
import os
from datetime import date
from dotenv import load_dotenv

class Routes_query:
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
    routes {
    shortName
  }
}
    '''

  def print_routes(self):
    response = requests.post(url=self.url, headers = self.hdr, json={"query": self.body})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        parsed_response = json.loads(response.content)
        print("response : ", json.dumps(parsed_response, indent = 4))
    else:
        print("There was a problem retrieving the data, do you have an active API key in a .env file?")

query=Routes_query()
query.print_routes()