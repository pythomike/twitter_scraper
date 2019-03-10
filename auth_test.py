import twitter, json
import pandas as pd
from env import gear

api = twitter.Api(consumer_key=gear['api_key'],
                  consumer_secret=gear['api_secret'],
                  access_token_key=gear['access_token'],
                  access_token_secret=gear['access_token_secret'])

fav = api.GetFavorites(screen_name='mjmorganti', count=200, return_json=True)
# fav = api.GetFavorites(screen_name='mjmorganti', count=200, return_json=True, max_id=1070350854539173888)
# fav = api.GetFavorites(screen_name='mjmorganti', count=2, return_json=True)

cols = ['text', 'user', 'created_at', 'id']
df  = pd.DataFrame(columns=cols)

for i in fav:
  fave = {
    'text':[i['text']],
    'user':[i['user']['name']],
    'created_at':[i['created_at']],
    'id': [i['id']]    
    # Need a function to parse out all hashtags and dump into a list.
    # 'entities':i['entities']
  }
  test = pd.DataFrame.from_dict(fave, orient='columns')
  df = pd.concat([df, test], axis=0).reset_index(drop=True)
  df.to_csv('faves.csv')


