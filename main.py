# -*- coding: utf-8 -*-

import config
import json
from requests_oauthlib import OAuth1Session


def create_oauth_session(ck, cs, at, ats):
    oauth = OAuth1Session(ck, cs, at, ats)
    return oauth


#画像の通し番号をつけるための変数。お好みで。
image_number = 0
get_pages = 10
#count * get_pages　だけツイートをさかのぼってくれる。今回は2000ツイート。
count = 200

def fav_tweets_get(page):
    url = "https://api.twitter.com/1.1/favorites/list.json?"
    params = {
            "screen_name" : "y_uuqu",
            "page": page,
            "count" : count,
            "include_entities" : True,
            }
    # oath = create_oath_session(oath_key_dict)
    responce = twitter.get(url, params = params)

    if responce.status_code != 200:
        print("Error code: {0}".format(responce.status_code))
        return None

    tweets = json.loads(responce)
    return tweets


def search_user( str, twitter ):
    url = "https://api.twitter.com/1.1/users/search.json?"
    params = {
            "q" : "aaa",
            }

    response = twitter.get( url, params = params )
    print( type(response) )
    print( response.status_code )
    return json.loads( response )


if __name__ == "__main__":
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET

    twitter = create_oauth_session(CK, CS, AT, ATS)
    print( search_user( "a", twitter ) )


