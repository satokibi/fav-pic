# -*- coding:utf-8 -*-
import config #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session
import json
import os
import sys
import urllib

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理

save_path = os.path.abspath('./test')

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
        "include_entities" : 1     #ツイートのメタデータ取得。これしないと複数枚の画像に対応できない。
    }
    # oath = create_oath_session(oath_key_dict)
    responce = twitter.get(url, params = params)

    if responce.status_code != 200:
        print("Error code: {0}".format(responce.status_code))
        return None

    tweets = json.loads(responce.text)
    return tweets


def image_saver(tweets):
    global image_number 
    for tweet in tweets:
        try:
            image_list = tweet["extended_entities"]["media"]

            for image_dict in image_list:
                url = image_dict["media_url"]
                url_large = url + ":large"
                with open(save_path+ "/" + str(image_number) + "_" + os.path.basename(url), 'wb') as f:
                    img = urllib.request.urlopen(url_large, timeout = 5).read()
                    f.write(img)
                print("done!")
                image_number += 1

        except KeyError:
            print("KeyError:画像を含んでいないツイートです。")
        except:
            print("Unexpected error:", sys.exc_info()[0])

if __name__ == "__main__":
    for i in range(1, get_pages):
        tweets = fav_tweets_get(i)
        image_saver(tweets)

