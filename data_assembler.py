import os
import json
import pandas as pd

class Data_assembler:

  def assemble_data(self):
    df = pd.DataFrame()
    for filename in os.listdir(os.getcwd()+('//data')):
      with open(os.path.join(os.getcwd()+('//data'), filename), 'r') as f: 
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