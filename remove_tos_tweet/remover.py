"""Remover for @tos tweets."""
from traitlets.config.configurable import Configurable
from traitlets import Unicode, Int
import tweepy
from tweepy import TooManyRequests
import time
from . import load_config


class Remover(Configurable):
    """Remover for @tos tweets."""

    api_key = Unicode(config=True)
    api_secret = Unicode(config=True)
    baerer = Unicode(config=True)
    access_token = Unicode(config=True)
    access_token_secret = Unicode(config=True)
    limit = Int(config=True)

    def remove(self):
        """Remove @tos tweets."""
        client = tweepy.Client(self.baerer,
                               consumer_key=self.api_key,
                               consumer_secret=self.api_secret,
                               access_token=self.access_token,
                               access_token_secret=self.access_token_secret)

        me = client.get_me()

        for tweet in tweepy.Paginator(
                client.get_users_tweets,
                me.data.id,
                max_results=100
        ).flatten(limit=self.limit):
            if "@tos" in tweet.text:
                print(tweet)

                for i in range(15):
                    try:
                        client.delete_tweet(tweet.id)  # 50 request / 15 min
                    except TooManyRequests:
                        print(f"Retry after 1 min: {i+1}/15")
                        time.sleep(60)
                    else:
                        break


main = Remover().remove
