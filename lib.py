# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session

def create_oauth_session( key_dict ):
    oauth = OAuth1Session(
            key_dict["consumer_key"],
            key_dict["consumer_secret"],
            key_dict["access_token"],
            key_dict["access_token_secret"],
            )
    return oauth
