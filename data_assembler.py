import os
import json
import pandas as pd
import matplotlib.pyplot as plt

class Data_assembler:

  def __init__(self) -> None:
    self.df = self.assemble_data()

  def assemble_data(self):
    df = pd.DataFrame()
    for filename in os.listdir(os.getcwd()+('\\data\\cancelled_route_data')):
      with open(os.path.join(os.getcwd()+('\\data\\cancelled_route_data\\'), filename), 'r') as f: 
        content = f.read()
        parsed_content = json.loads(content)
        data_list = parsed_content['data']['cancelledTripTimes']
        new_df =  pd.DataFrame(data_list)
        df = pd.concat([df, new_df], ignore_index=True)
    trips_df = df['trip']
    trips_df = trips_df.apply(pd.Series)
    df = pd.concat([df, trips_df], axis = 1)
    df = df.drop(['headsign', 
                  'realtimeState', 
                  'gtfsId',
                  'trip',
                  'pattern',
                  'route'
                  ], axis = 1)

    return(df)
  
  def write_to_csv(self):
    self.df.to_csv('data.csv')

  def query_route_cancelations(self, route):
    df = self.df.loc[self.df['routeShortName'] == route]
    df['date'] = pd.to_datetime(df['serviceDay'], unit='s')
    df.date = df.date + pd.Timedelta('03:00:00')
    return df

  def construct_graph(self, route):
    df = self.query_route_cancelations(route)
    
    df = df['date'].value_counts()
    print(df)
    
    df.plot()
    plt.show()
