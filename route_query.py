import requests
import json
import os
from dotenv import load_dotenv

def is_valid_route(test_route):
    route_list = []

    f = open('data/route_codes.json')
 
    data = json.load(f)

    routes = data["data"]["routes"]
    for route in routes:
        route_list.append(str(route["shortName"]))
    f.close()

    if test_route in route_list:
        return True
    else:
        return False


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

    def create_routes_file(self):
        response = requests.post(url=self.url, headers = self.hdr, json={"query": self.body})
        print("response status code: ", response.status_code)
        if response.status_code == 200:
            parsed_response = json.loads(response.content)
            #print("response : ", json.dumps(parsed_response, indent = 4))
            filename = ('route_codes.json')
            path = os.getcwd()+"\\data\\"+filename
            path = os.path.join(os.getcwd(), "data", filename)
            with open(path, 'w') as file:
                file.write(json.dumps(parsed_response, indent=4))
            print("File created successfully.")
            file.close()
        else:
            print("There was a problem retrieving the data, do you have an active API key in a .env file?")


#query=Routes_query()
#query.create_routes_file()