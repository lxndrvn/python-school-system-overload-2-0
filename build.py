# This script can create the database tables based on your models
import connect
from models import *

db = connect.create_database()

db.connect()
db.drop_tables([School, City, Applicant, Mentor, InterviewSlot, Interview, Question], safe=True, cascade=True)
db.create_tables([School, City, Applicant, Mentor, InterviewSlot, Interview, Question], safe=True)

bpschool = School.create(location='Budapest')
misischool = School.create(location='Miskolc')
krakowschool = School.create(location='Krakow')

cities = [{'name': 'Budapest', 'school': bpschool},
                  {'name': 'Székesfehérvár', 'school': bpschool},
                  {'name': 'Miskolc', 'school': misischool},
                  {'name': 'Eger', 'school': misischool},
                  {'name': 'Krakow', 'school': krakowschool},
                  {'name': 'Warsaw', 'school': krakowschool}]

for city in cities:
    City.create(name=city['name'],school=city['school'])

mentors=[{'first_name': 'Matyi', 'last_name': 'Szabó', 'school': 'Budapest', 'email': 'matyi.codecool@gmail.com'},
         {'first_name': 'Imi', 'last_name': 'Fodor', 'school': 'Budapest', 'email': 'imi.codecool@gmail.com'},
         {'first_name': 'Laci', 'last_name': 'Molnár', 'school': 'Budapest', 'email': 'laci.codecool@gmail.com'},
         {'first_name': 'Agnieszka', 'last_name': 'Koszany', 'school': 'Krakow', 'email': 'agni.codecool@gmail.com'},
         {'first_name': 'Róbert', 'last_name': 'Kohányi', 'school': 'Miskolc', 'email': 'robert.codecool@gmail.com'}]

for mentor in mentors:
    Mentor.create(first_name= mentor['first_name'], last_name=mentor['last_name'], email=mentor['email'],school=School.select().where(School.location == mentor['school']).get())

applicants=[{'first_name': 'Alexandra', 'last_name': 'Ivan', 'gender': 'female', 'city': 'Budapest',
             'email': 'ivan.codecool@gmail.com','status': 'NEW'},
            {'first_name': 'Patrik', 'last_name': 'Blik', 'gender': 'male', 'city': 'Székesfehérvár',
             'email': 'blik.codecool@gmail.com','status': 'NEW'},
            {'first_name': 'David', 'last_name': 'Szilniczky', 'gender': 'male','city': 'Krakow',
             'email': 'szili.codecool@gmail.com','status': 'NEW'},
            {'first_name': 'Fanni', 'last_name': 'Perjesi', 'gender': 'female','city': 'Eger',
             'email': 'perj.codecool@gmail.com','status': 'NEW'}]

for applicant in applicants:
    Applicant.create(status=applicant['status'], application_code=None, first_name=applicant['first_name'],
                     last_name=applicant['last_name'], email=applicant['email'], gender=applicant['gender'],
                     city=City.select().where(City.name==applicant['city']).get(), school=None)

interview_slots=[{'start': '2017-09-01 09:00:00', 'end': '2017-09-01 13:00:00', 'mentor': 'Matyi'},
                 {'start': '2017-09-02 10:00:00', 'end': '2017-09-02 14:00:00', 'mentor': 'Laci'},
                 {'start': '2017-09-03 11:00:00', 'end': '2017-09-03 15:00:00', 'mentor': 'Imi'},
                 {'start': '2017-09-04 12:00:00', 'end': '2017-09-04 16:00:00', 'mentor': 'Róbert'},
                 {'start': '2017-09-05 13:00:00', 'end': '2017-09-05 17:00:00', 'mentor': 'Agnieszka'}]

for interview_slot in interview_slots:
    InterviewSlot.create(start=interview_slot['start'], end=interview_slot['end'],
                         mentor=Mentor.select().where(Mentor.first_name == interview_slot['mentor']).get())

questions = [{'question': 'Could you give me a (KOA)Laptop?', 'applicant': 'David',
              'date': '2017-09-05 17:00:00' }]

for question in questions:
    Question.create(applicant=Applicant.select().where(Applicant.first_name==question['applicant']).get(),question=question['question'], date=question['date'])
