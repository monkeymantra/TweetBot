import tweepy
import logging

from modules.config.tweetbot import TweetBotConfig

import logging
from tweepy import API, Client

from tweet_bot_config import TweetBotConfig


class TwitterApi:
    def __init__(self, config: TweetBotConfig, api: API, client: Client) -> None:
        self.config: TweetBotConfig = config
        self.logger: logging.Logger = logging.getLogger("TwitterApi")
        self.api: API = api
        self.client: Client = client

    def get_followers(self) -> list:
        self.logger.warning("Getting Followers")
        return self.api.get_followers()

    def get_me(self) -> dict:
        return self.client.get_me()

    def create_tweet(self, tweet: str) -> dict:
        return self.client.create_tweet(text=tweet)

    def login_to_twitter(self) -> None:
        self.logger.warning("Attempting to log in to twitter")
        try:
            self.api.verify_credentials()
        except Exception as e:
            self.report_an_exception(e)
        else:
            self.logger.warning("Logged in to twitter.")

    def report_an_exception(self, e: Exception) -> None:
        # Do something with the exception
        pass