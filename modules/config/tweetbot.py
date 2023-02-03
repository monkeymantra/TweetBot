import os
import json
import yaml

from dataclasses import dataclass


@dataclass
class GoogleCredentials:
    credentials_path: str
    calendar_email_address: str


class TwitterCredentials:
    def __init__(self, credentials_path: str = "./sample_config/twitter/credentials.json"):
        self. credentials_path = credentials_path
        self._creds_dict: dict = None
        self._creds_dict = self.parse_creds()
        self._api_key: str = None
        self._api_key_secret: str = None

    def parse_creds(self) -> dict:
        if not self._creds_dict:
            with open(self.credentials_path, 'r') as twitter_creds:
                return json.loads(twitter_creds.read())

    @property
    def credentials(self) -> dict:
        return self._creds_dict

    @property
    def api_key(self) -> str:
        if not self._api_key:
            self._api_key = self.credentials.get("api_key")
        return self._api_key

    @property
    def api_key_secret(self) -> str:
        if not self._api_key_secret:
            self._api_key_secret = self.credentials.get("api_key_secret")
        return self._api_key_secret


@dataclass
class TweetBotConfig:
    name: str
    owner_email: str
    # google_credentials: GoogleCredentials
    twitter_credentials: TwitterCredentials = None

    @staticmethod
    def configFromYaml(path: str):
        with open(path, 'r') as config:
            config_dict = yaml.safe_load(config)
            return TweetBotConfig(
                name=config_dict['name'],
                owner_email=config_dict['owner']['email'],
                twitter_credentials=TwitterCredentials()
            )
