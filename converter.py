from ics import Calendar, Event

"""
Functions for converting event information to ics data 
"""

def createCalendar(events):
    """
    Creates a Calendar object with a list of events
    """
    c = Calendar()
    for event in events:
        e = Event()
        e.name = event['event_name']
        e.begin = event['event_date']
        e.description = event['event_description']
        c.events.add(e)

    return c

def createICSFile(calendar):
    """
    Creates an ics file with a Calendar object
    """
    with open('syllabus.ics', 'w') as file:
        file.writelines(calendar.serialize_iter())


# python3 converter.py 
if __name__ == '__main__':
    from api import *

    syllabus = get_syllabus(1)
    events = syllabus[1]['events']
    c = createCalendar(events)
    createICSFile(c)