import tweepy
from .sharedutils import errlog

def twitternotify(config, group, title) -> None :
    '''
    Posting message to Twitter
    '''
    try:
        client = tweepy.Client(
             consumer_key=config['consumer_key'], consumer_secret=config['consumer_secret'],
             access_token=config['access_token'], access_token_secret=config['access_token_secret']
        )
        client.create_tweet(
    except:
        errlog('Can not tweet :(')

