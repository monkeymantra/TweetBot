import tweepy
import logging

from modules.config.tweetbot import TweetBotConfig


class TwitterApi:

    def __init__(self, config: TweetBotConfig):
        self.config = config
        self.handler = tweepy.OAuth1UserHandler(self.config.twitter_credentials.api_key,
                                                self.config.twitter_credentials.api_key_secret,
                                                callback="http://localhost:8081/twitter_redirect")
        self.access_token, self.access_secret = None, None
        self.authorization_url = None
        self.logger = logging.getLogger("TwitterApi")

    def login_to_twitter(self):
        self.logger.warn("Attempting to log in to twitter")
        exception = None
        try:
            self.handler.get_authorization_url(signin_with_twitter=True)
        except Exception as e:
            exception = e
        finally:
            if not exception:
                self.logger.exception("Unable to log in to twitter.", exc_info=e)
            else:
                self.logger.warn("Logged in to twitter.")
