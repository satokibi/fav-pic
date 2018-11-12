# -*- coding:utf-8 -*-
import json
import config
from lib import *


def get_fav_tweets( screen_name, key_dict ):
    url = "https://api.twitter.com/1.1/favorites/list.json"
    params = {
            "screen_name" : screen_name,
            "include_entities" : False,
            "count": 200,
            }

    twitter = create_oauth_session( key_dict )
    response = twitter.get( url, params = params )
    return response


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

    response = get_fav_tweets( input_str, oauth_key_dict ) 
    if response.status_code == 200:
        limit = response.headers['x-rate-limit-remaining']
        reset = response.headers['x-rate-limit-reset']

        print("API remain: {}".format( limit ) )
        print("API  reset: {}".format( reset ) )

        tweets = json.loads( response.text )
        for tweet in tweets:
            try:
                image_list = tweet['extended_entities']['media']
                for image in image_list:
                    url = image['media_url']
                    url_large = url + ':large'
                    print( url_large )
                    
            except KeyError:
                print("画像を含んでいないツイート")
    else:
        print("##ERROR## status_code: {}".format( response.status_code ) )

