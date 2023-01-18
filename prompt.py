from api import *
import pick

# IF get_syllabi() returns more than one course - let user choose ?

# Mock response - more than one course
syllabi= [{'course_name': 'Projects in Computer Science',
               'course_semester': 'Spring',
               'course_year': 2023,
               'created_at': '2023-01-07T05:02:29.000000Z',
               'discord_channel': '1060282877230723077',
               'end_date': '2023-05-09',
               'id': 1,
               'start_date': '2023-01-17',
               'updated_at': '2023-01-07T06:44:34.000000Z'},

               {'course_name': 'Software Design',
               'course_semester': 'Fall',
               'course_year': 2022,
               'created_at': '2022-01-07T05:02:29.000000Z',
               'discord_channel': '1060282877230723077',
               'end_date': '2022-05-09',
               'id': 2,
               'start_date': '2022-01-17',
               'updated_at': '2023-01-07T06:44:34.000000Z'}
               ]


# grab course names 
courses = [x['course_name'] for x in syllabi]

# prompt user
title = 'What syllabus would you like a calendar for? '
options = courses
option, index = pick.pick(options, title, indicator='>', default_index=0)

# based on user selection grab the ID 
def getID(x):
    return x['course_name'] == option

optionID = list(filter(getID, syllabi))
print("ID:", optionID[0]['id'])

