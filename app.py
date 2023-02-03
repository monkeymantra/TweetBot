from logging import getLogger
from flask import Flask, request

from modules.config.tweetbot import TweetBotConfig
from modules.twitter.client import TwitterApi
from typed_dataclass import typed_dataclass

logger = getLogger("TweetBot HTTP Server initializing...")
config = TweetBotConfig.configFromYaml("./sample_config/config.yaml")
twitter_api = TwitterApi(config)
app = Flask(__name__)


@typed_dataclass
class TwitterSession:
    oauth_token: str = ""
    oauth_verifier: str = ""
    access_token: str = ""
    access_secret: str = ""


global twitter_session


@app.route('/twitter_redirect', methods=['GET', 'POST'])
def twitter_login_handler():
    logger.warning(f"Login handler received request: {request}")
    logger.warning(f"Args: {request.args}")
    oauth_token = request.args.get("oauth_token")
    oauth_verifier = request.args.get("oauth_verifier")
    access_token, access_secret = twitter_api.handler.get_access_token(verifier=oauth_verifier)
    twitter_session = TwitterSession(oauth_token,
                                     oauth_verifier,
                                     access_token,
                                     access_secret)
    logger.warning(f"Got a token! {twitter_session.access_token}")
    return "Got your token!"


@app.route('/twitter_login', methods=['GET'])
def twitter_login():
    twitter_api.login_to_twitter()
    return "Logging into twitter..."

@app.route('/', methods=['GET'])
def dummy():
    return "Hello World!"


if __name__ == '__main__':
    context = ('/etc/ssl/localhost/localhost.crt', '/etc/ssl/localhost/localhost.key')#certificate and key files
    app.run(debug=True, ssl_context=context, host="0.0.0.0", port=8001)
