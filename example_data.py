# This script can generate example data for 'City' and 'InterviewSlot' models.

from models import *

mentors=[{'first_name': 'Matyi', 'last_name': 'Szabó', 'school': 'Budapest', 'email': 'matyi.codecool@gmail.com'},
         {'first_name': 'Imi', 'last_name': 'Fodor', 'school': 'Budapest', 'email': 'imi.codecool@gmail.com'},
         {'first_name': 'Laci', 'last_name': 'Molnár', 'school': 'Budapest', 'email': 'laci.codecool@gmail.com'},
         {'first_name': 'Agnieszka', 'last_name': 'Koszany', 'school': 'Krakow', 'email': 'agni.codecool@gmail.com'},
         {'first_name': 'Róbert', 'last_name': 'Kohányi', 'school': 'Miskolc', 'email': 'robert.codecool@gmail.com'}]


applicants=[{'first_name': 'Alexandra', 'last_name': 'Ivan', 'gender': 'female', 'city': 'Budapest',
             'email': 'ivan.codecool@gmail.com','status': 'NEW'},
            {'first_name': 'Patrik', 'last_name': 'Blik', 'gender': 'male', 'city': 'Székesfehérvár',
             'email': 'blik.codecool@gmail.com','status': 'NEW'},
            {'first_name': 'David', 'last_name': 'Szilniczky', 'gender': 'male','city': 'Krakow',
             'email': 'szili.codecool@gmail.com','status': 'NEW'},
            {'first_name': 'Fanni', 'last_name': 'Perjesi', 'gender': 'female','city': 'Eger',
             'email': 'perj.codecool@gmail.com','status': 'NEW'}]



interview_slots=[{'start': '2017-09-01 09:00:00', 'end': '2017-09-01 13:00:00'},
                 {'start': '2017-09-02 10:00:00', 'end': '2017-09-02 14:00:00'},
                 {'start': '2017-09-03 11:00:00', 'end': '2017-09-03 15:00:00'},
                 {'start': '2017-09-04 12:00:00', 'end': '2017-09-04 16:00:00'},
                 {'start': '2017-09-05 13:00:00', 'end': '2017-09-05 17:00:00'}]


