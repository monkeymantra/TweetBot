import datetime
import openai
import os
import humanize

from dataclasses import dataclass


@dataclass
class Prompt:
    start_dt: datetime.datetime
    end_dt: datetime.datetime
    max_length: int = 160
    content: str = ""
    location: str = "Westies"
    num_responses: int = 3# "Always going to be present in the text prompt

    @staticmethod
    def _format_time(dt: datetime.datetime):
        return dt.strftime('%A %d-%m-%Y at %H:%M:%S')
    @property
    def start(self) -> str:
        return Prompt._format_time(self.start_dt)

    @property
    def end(self) -> str:
        return Prompt._format_time(self.end_dt)

    def __str__(self) -> str:
        return f"""A tweet has a maximum length of 160 characters.
        All dates and times should be precise, but natural. If the end time is the next morning, don't mention the end
        date, but do mention the end time.
        Produce a fun tweet to advertise the following event:
        {self.content} starting at {self.start} and ending at {self.end}
        """


class ChatGPTClient:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_ENGINE = "text-davinci-003"

    def __init__(self):
        pass

    def get_responses(self, prompt: Prompt):
        return openai.Completion.create(
            engine=self.MODEL_ENGINE,
            prompt=str(prompt),
            max_tokens=1024,
            n=prompt.num_responses,
            stop=None,
            temperature=0.5,
        ).choices
