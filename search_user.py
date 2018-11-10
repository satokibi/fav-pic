# -*- coding: utf-8 -*-

import config
import json
from requests_oauthlib import OAuth1Session


def create_oauth_session( key_dict ):
    oauth = OAuth1Session(
            key_dict["consumer_key"],
            key_dict["consumer_secret"],
            key_dict["access_token"],
            key_dict["access_token_secret"],
            )
    return oauth


def search_user( str, key_dict ):
    url = "https://api.twitter.com/1.1/users/show.json?"
    params = {
            "screen_name" : str,
            "include_entities" : False,
            }

    twitter = create_oauth_session( key_dict )
    response = twitter.get( url, params = params )
    if response.status_code == 200:
        user = json.loads( response.text )
        return user
    else:
        return None


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

    user = search_user( input_str, oauth_key_dict ) 
    if user is not None:
        # print( user )
        print( "     id: {}".format( user["screen_name"] ) )
        print( "   name: {}".format( user["name"] ) )
        print( "img_url: {}".format( user["profile_image_url"] ) )

