# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 11:44:22 2012

@author: kunj
"""

import tweepy
import sys
import re

def main():
    i=1
    hashtag = []
    CONSUMER_KEY = "" # your consumer key here
    CONSUMER_SECRET = "" # your consumer secret here
    ACCESS_KEY = "" # your access key here
    ACCESS_SECRET = "" # your access token here
    if CONSUMER_KEY and CONSUMER_SECRET and ACCESS_KEY and ACCESS_SECRET:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        try:
            api = tweepy.API(auth)
            statuses = tweepy.Cursor(api.user_timeline).items(200)
            for status in statuses:
                #match = re.search(r'#\S+',status.text)
                #if match:
                    #x = str(match.group()[1:])
                    #for x in hashtag:
                    #    continue
                    #hashtag.append(match.group()[1:])
                print i, status.text
                i=i+1
                print " "
            #for hashtags in hashtag:
                #print hashtags + " "
        except tweepy.error.TweepError:
            print "Please check consumer key/consumer secret/access key/access secret and re-install"
            sys.exit()
    else:
        print "Please add consumer key/consumer secret/access key/access secret and re-install"
        sys.exit()
        
if __name__=='__main__':
    main()
    