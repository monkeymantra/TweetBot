import datetime
from dataclasses import dataclass

import openai
import os

@dataclass
class Prompt:
    start_dt: datetime.datetime
    end_dt: datetime.datetime
    max_length: int = 160
    content:    str = ""
    location:   str = "Westies" # "Always going to be present in the text prompt

    def to_prompt(self) -> str:
        return f"""A tweet has a maximum length of 160 characters. Produce a fun tweet to advertise the following event,
        targeting a college-aged demographic:
        {self.content}
        """

class ChatGPTClient:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_ENGINE="text-davinci-003"

    def __init__(self):
        pass

    def get_response(self, prompt: Prompt):
        completion = openai.Completion.create(
            engine=self.MODEL_ENGINE,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )


class EventToTweet:

    def __init__(self):
        pass


    def convert_to_tweet(self, start_time: datetime.datetime, end_time: datetime.datetime, summary: str) -> str:
        # AI magic box called here
        pass
