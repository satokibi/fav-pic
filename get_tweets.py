
import json
import config
from lib import *


def get_tweets( screen_name, key_dict ):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params = {
            "screen_name" : screen_name,
            "include_entities" : False,
            # "count": 10,
            "exclude_replies": True,
            "contributor_details": True,
            "include_rts": True,
            }

    twitter = create_oauth_session( key_dict )
    response = twitter.get( url, params = params )

    return response


def sort_by_fav( tweets ):
    return sorted( tweets, key = lambda x: x['favorite_count'], reverse = True )

if __name__ == "__main__":
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET

    oauth_key_dict = {
            "consumer_key": CK,
            "consumer_secret": CS,
            "access_token": AT,
            "access_token_secret": ATS,
            }

    print("検索したいid を入力してください")
    print(">> ", end="")
    input_str = input()

    response = get_tweets( input_str, oauth_key_dict ) 
    if response.status_code == 200:
        tweets = json.loads( response.text )
        tweets = sort_by_fav( tweets )
        # print( tweets )
        for tweet in tweets:
            print(tweet['user']['name']+'::'+tweet['text'])
            print(tweet['favorite_count'])
            print(tweet['created_at'])
            print('*******************************************')
    else:
        print("##ERROR## status_code: {}".format( response.status_code ) )
