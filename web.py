# pip3 install flask ics

import os

from flask import Flask, render_template, make_response

from functools import lru_cache
import time

import sys
import converter
import api
from converter import createICSFile, createCalendar

from datetime import datetime, timedelta

sys.path.append('.') # so we can import api below
from api import get_user as _get_user, get_syllabi as _get_syllabi, get_syllabus as _get_syllabus

def cached(f, ttl=60):
    """
    decorator
    Cache function calls with a TTL
    """
    @lru_cache()
    def expensive(*args, ttl_hash=None, **kwargs):
        del ttl_hash
        return f(*args, **kwargs)

    def _f(*args, **kwargs):
        return expensive(*args, ttl_hash=round(time.time() / ttl), **kwargs)
    return _f

get_user = cached(_get_user)
get_syllabi = cached(_get_syllabi)
get_syllabus = cached(_get_syllabus)


def filterDate(x, d1, d2):
    if (x['event_date'] < d2 and x['event_date'] > d1):
        return True
    return False

app = Flask('syllabusapp', root_path=os.getcwd())

@app.template_filter()
def date(value, format="%Y-%m-%d"):
    return value.strftime(format)

@app.route('/')
def index():
    _, user = get_user()
    _, syllabi = get_syllabi()
    syllabi = syllabi['syllabi']
    print(syllabi)
    return render_template('index.html', user=user, syllabi=syllabi)

@app.route('/syllabus/<syl_id>')
def syllabus_detail(syl_id):
    _, syllabus = get_syllabus(syl_id)
    _, user = get_user()

    # Fetch events sort them into two groups: future and past events 
    events = syllabus['events']
    for event in events:        
        if(type(event['event_date']) is str):
            datestr = str(event['event_date'])
            event['event_date'] = datetime.strptime(datestr, "%Y-%m-%d")

    eventDates = [x['event_date'] for x in events]

    lastDate = max(eventDates) + timedelta(days=1)
    pastDate = min(eventDates) - timedelta(days=1)
    
    currentDate = datetime.combine(datetime.today(), datetime.min.time())

    # print(lastDate, pastDate, currentDate)

    future = list(filter(lambda x: filterDate(x, currentDate, lastDate), events))
    past = list(filter(lambda x: filterDate(x, pastDate, currentDate), events))
    today = list(filter(lambda x: filterDate(x, currentDate-timedelta(days=1), currentDate+timedelta(days=1)), events))
    
    return render_template('syllabus.html', user=user, syllabus=syllabus, id=syl_id, currentDate=currentDate, past=past, future=future, today=today, events=events)


@app.route('/download/<syl_id>')
def download_ics(syl_id):
    _, syllabus = get_syllabus(syl_id)
    c = createCalendar(syllabus['events'])
    return make_response((c.serialize(), 200, {
        'Content-Disposition': 'attachment; filename=calendar{}.ics'.format(syl_id),
        'Content-Type': 'text/calendar'
    }))

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(debug=True)


