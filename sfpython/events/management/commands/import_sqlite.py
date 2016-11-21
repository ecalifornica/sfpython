import datetime
import os
from glob import glob
import sqlite3

from django.core.management.base import BaseCommand

from events.models import Event, Attendee, Attendance

class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        parser.add_argument('location')
    
    def handle(self, *args, **options):
        location = options['location']
        databases = glob(location + "/*sqlite*")
        for db in databases[:1]:
          print db
          seconds = os.path.getmtime(db)
          dt = datetime.datetime.fromtimestamp(seconds).date()
          new_date = raw_input(dt."Date? [%s] :" % dt.strftime("%a %Y-%m-%d"))
          if new_date:
            dt = datetime.datetime.strptime(new_date, '%Y-%m-%d').date()
          title = raw_input("[Talk] night? :")
          if not title:
            title = "Talk"
          meetup_id = raw_input("Meetup ID: ").strip()
          e = Event(title=dt.strftime("%B %Y's %s Night" % title),
                    date=dt,
                    meetup_id=meetup_id)
          db = sqlite3.connect(db)
          db.row_factory = sqlite3.Row
          cur = db.cursor()
          cur.execute("select user_id, name, rsvp, present from rsvp")
          for (user_id, name, rsvp, present) in cur.fetchall():
            user = Attendee.get_or_create(meetup_id=user_id, handle=

