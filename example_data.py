# This script can generate example data for 'City' and 'InterviewSlot' models.

from models import *

applicants = [
    {'first_name': 'Alexandra', 'last_name': 'Ivan', 'city': 'Budapest', 'status': 'applied',
     'email': 'ivan.codecool@gmail.com'},
    {'first_name': 'Patrik', 'last_name': 'Blik', 'city': 'Debrecen','status': 'applied',
     'email': 'blik.codecool+a1@gmail.com'},
    {'first_name': 'David', 'last_name': 'Szilniczky', 'city': 'Eger','status': 'applied',
     'email': 'szili.codecool+a2@gmail.com'},
    {'first_name': 'Fanni', 'last_name': 'Perjesi', 'city': 'Los Angeles','status': 'applied',
     'email':'perj.codecool+a3@gmail.com'},
    ]

def add_applicants():
    for applicant in applicants:
        Applicant.create(first_name=applicant['first_name'], last_name=applicant['last_name'],
                         city=applicant['nearest city'],status=applicant['status'], email=applicant['email'])


School.create(location='Budapest')
bpschool = School.select().where(School.location =='Budapest')
School.create(location='Miskolc')
misischool = School.select().where(School.location == 'Miskolc')
School.create(location='Krakow')
krakowschool = School.select().where(School.location == 'Krakow')

cities = [
    {'name': 'Budapest', 'nearest school': 'bpschool'},
    {'name' : 'Esztergom', 'nearest school' : 'bpschool'},
    {'name' : 'Miskolc', 'nearest school' : 'misischool'},
    {'name' : 'Eger', 'nearest school' : 'misischool'},
    {'name' : 'Krakow', 'nearest school' : 'krakowschool'},
    {'name' : 'Warsaw', 'nearest school' : 'krakowschool'}
]
def add_city():
    for city in cities:
        City.create(city['name'],city['school'])

mentors = [
    {'first_name': 'Matyi', 'last_name': 'Szabó', 'school': 'Budapest', 'email': 'matyi.codecool@gmail.com'},
    {'first_name': 'Imi', 'last_name': 'Fodor', 'school': 'Budapest', 'email': 'imi.codecool@gmail.com'},
    {'first_name': 'Laci', 'last_name': 'Molnár', 'school': 'Budapest', 'email': 'laci.codecool@gmail.com'},
    {'first_name': 'Agnieszka', 'last_name': 'Koszany', 'school': 'Krakow', 'email': 'agni.codecool@gmail.com'},
    {'first_name': 'Róbert', 'last_name': 'Kohányi', 'school': 'Miskolc', 'email': 'robert.codecool@gmail.com'}
]

def add_mentors():
    for mentor in mentors:
        Mentor.create(first_name=mentor['first_name'], last_name=mentor['last_name'], email=mentor['email'],
                      school=School.select().where(School.location == mentor['school']))

interview_slots = [
    {'start': '2017-09-01 09:00:00', 'end': '2017-09-01 13:00:00', 'reserved': True, 'related mentor': ''},
    {'start': '2017-09-02 10:00:00', 'end': '2017-09-02 14:00:00', 'reserved': False, 'related mentor': ''},
    {'start': '2017-09-03 11:00:00', 'end': '2017-09-03 15:00:00', 'reserved': True, 'related mentor': ''},
    {'start': '2017-09-04 12:00:00', 'end': '2017-09-04 16:00:00', 'reserved': False, 'related mentor': ''},
    {'start': '2017-09-05 13:00:00', 'end': '2017-09-05 17:00:00', 'reserved': True, 'related mentor': ''}
]

def interview():
    for interview_slot in interview_slots:
        Interview.create(start=interview_slot['start'], end=interview_slot['end'],
                         reserved=interview_slot['reserved'])