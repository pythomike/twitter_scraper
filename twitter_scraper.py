import twitter
import json
import pandas as pd
from env import gear

##########################################
#  YOU'VE INVALIDATED ALL THE AUTH JUNK  #
##########################################

api = twitter.Api(consumer_key=gear['api_key'],
                  consumer_secret=gear['api_secret'],
                  access_token_key=gear['access_token'],
                  access_token_secret=gear['access_token_secret']
                  )


def favourite_parser(fav):
    global df, tweet_id, batch_length
    json_boye.append(fav)

    for i in fav:
        test = pd.DataFrame.from_dict({
                                    'text': [i['text']],
                                    'user': [i['user']['name']],
                                    'created_at': [i['created_at']],
                                    'id': [i['id']],
                                    # 'entities':i['entities']
                                    }, orient='columns')
        df = pd.concat([df, test], axis=0).reset_index(drop=True)
    batch_length = len(fav)
    print("Batch Length: ", batch_length)
    tweet_id = df.iloc[-1]['id']
    print("Tweet ID: ", tweet_id)


def favourite_iterator(maxId):
    while batch_length > 1:
        fav = api.GetFavorites(screen_name='mjmorganti', count=200, return_json=True, max_id=maxId)
        favourite_parser(fav)
        maxId = tweet_id


# Final DataFrame
df = pd.DataFrame(columns=['text', 'user', 'created_at', 'id'])
tweet_id = 0
batch_length = 2
running = True
json_boye = []

# RUNNER CODE
fav = api.GetFavorites(screen_name='mjmorganti', count=200, return_json=True)
favourite_parser(fav)
favourite_iterator(tweet_id)

# WRITER CODE
# df.to_csv('faves.csv')
with open('favourites_json.json', 'w') as file:
    json.dump(json_boye, file)