
# This is a sample Python script.
from ai_client import ChatGPTClient
from event_calendar import WestiesCalendar
from ai_client import Prompt
import datetime
from datetime import timedelta

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    event_start = datetime.datetime(2023, 2, 27, 22, 0, 0, 0)
    event_end = event_start + timedelta(hours=6)
    client = ChatGPTClient()
    prompt = Prompt(start_dt=event_start, end_dt=event_end, content="Karaoke night", num_responses=3)
    print(prompt.start)
    print(prompt.end)
    responses = client.get_responses(prompt)
    for response in responses:
       print(response.text)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
