from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import traceback
from dataclasses import dataclass
import dateutil.parser
from functools import partial
import pytz

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']



@dataclass
class Person:
    email: str
    displayName: str
    self: bool

    @staticmethod
    def from_dict(d: dict) -> 'Person':
        return Person(
            email=d.get('email', 'Unknown'),
            displayName=d.get('displayName', 'Unknown'),
            self=d.get('self', False)
        )


@dataclass
class Event:
    kind: str
    id: str
    created: str
    summary: str
    creator: Person
    organizer: Person
    originalStartTime: datetime.datetime
    start: datetime.datetime
    end: datetime.datetime
    updated: datetime.datetime
    eventType: str
    htmlLink: str

    @staticmethod
    def _parse_date(field_name=None, event_dict={}) -> datetime.datetime:
        time_field = event_dict.get(field_name)
        tz = None
        if 'date' in time_field:
            time_str = time_field.get('date')
        elif 'dateTime' in time_field:
            time_str = time_field['dateTime']
            tz = pytz.timezone(time_field['timeZone'])
        else:
            time_str = time_field
        try:
            parsed = dateutil.parser.parse(time_str)
            parsed_with_tz = parsed.replace(tzinfo=tz)
        except Exception as e:
            traceback.print_exception(e)
        return parsed_with_tz

    @staticmethod
    def from_event_dict(event_dict: dict) -> 'Event':
        parse_date = partial(Event._parse_date, event_dict=event_dict)
        return Event(
            kind=event_dict['kind'],
            start=parse_date('start'),
            end=parse_date('end'),
            created=parse_date('created'),
            updated=parse_date('updated'),
            htmlLink=event_dict.get('htmlLink'),
            id=event_dict.get('id'),
            eventType=event_dict.get('eventType'),
            originalStartTime=parse_date('originalStartTime'),
            creator=Person.from_dict(event_dict['creator']),
            organizer=Person.from_dict(event_dict['organizer']),
            summary=event_dict['summary']
        )



class WestiesCalendar(object):

    def __init__(self, max_results: int = 100, timezone: str = 'Europe/Brussels'):
        self.creds = self.get_creds()
        self.token = None
        self.max_results = max_results
        self.time_zone = pytz.timezone(timezone)

    def get_creds(self) -> Credentials:
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_sxecrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        return creds

    def get_start_and_end_time(self, start_date: datetime.datetime, end_date: datetime.datetime) -> (str, str):
        return start_date, end_date


    def get_calendar_events(self, start_time: datetime.datetime, end_time: datetime.datetime) -> list[dict]:
        events = []
        try:
            service = build('calendar', 'v3', credentials=self.creds)

            # Call the Calendar API
            now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            print(f'Getting the upcoming {self.max_results} events')
            events_result = service.events().list(calendarId='primary', timeMin=now,
                                                  maxResults=self.max_results, singleEvents=True,
                                                  orderBy='startTime').execute()
            events = [Event.from_event_dict(event_dict) for event_dict in events_result.get('items')]

            if not events:
                print('No upcoming events found.')

            # Prints the start and name of the next 10 events
            return events

        except Exception as e:
            traceback.print_exception(e)
            if not events:
                print('No upcoming events found.')
                return []
            else:
                return events


if __name__ == '__main__':
    calendar = WestiesCalendar()
    events = calendar.get_calendar_events(datetime.datetime(month=1, day=20, year=2023, minute=12, second=10), datetime.datetime(month=3, day=1, year=2023, minute=10, second= 10))
    for event in events:
        print(event)