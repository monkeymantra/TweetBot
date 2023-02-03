
# This is a sample Python script.
from modules.ai.client import ChatGPTClient
from modules.ai.client import Prompt
import datetime
from datetime import timedelta

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    event_start = datetime.datetime(2023, 2, 27, 22, 0, 0, 0)
    event_end = event_start + timedelta(hours=6)
    client = ChatGPTClient()
    rap_prompt = """
    You can't force it
let things run their course 
then divorce them;
The happy from sad
all the mad from glad
all the good and the bad
then enforce it
here's the task:
dry the flask
anhydrous, anoxic
and then more shit:
Keep a journal
infernal
all your faustian deals
but let's be real
cuz you'll never remember
not all of the feels
Try to write 'em in rhyme
You can't fight the crime
you're a step out of time
you're a step out of line
It's a flight-risk, that mind
so record it.
don't snort the ice
just report it to ICE
and deport it.
"""

    prompt = Prompt(start_dt=event_start, end_dt=event_end, content="Karaoke night", num_responses=3)
    print(prompt.start)
    print(prompt.end)
    responses = client.get_responses(prompt)
    for response in responses:
       print(response.text)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
