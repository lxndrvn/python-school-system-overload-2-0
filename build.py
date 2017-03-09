from models import *
import database

db = database.database()

db.connect()
db.drop_tables([School, City, Applicant, Mentor, InterviewSlot, Interview, Question, Admin], safe=True, cascade=True)
db.create_tables([School, City, Applicant, Mentor, InterviewSlot, Interview, Question, Admin], safe=True)

bpschool = School.create(location='Budapest')
misischool = School.create(location='Miskolc')
krakowschool = School.create(location='Krakow')

cities = [{'name': 'Budapest', 'school': bpschool},
                  {'name': 'Szekesfehervar', 'school': bpschool},
                  {'name': 'Miskolc', 'school': misischool},
                  {'name': 'Eger', 'school': misischool},
                  {'name': 'Krakow', 'school': krakowschool},
                  {'name': 'Warsaw', 'school': krakowschool}]

admins = [{'email': 'admin@codefool.com', 'password': '0'}]

mentors=[{'first_name': 'Matyi', 'last_name': 'Szabo', 'school': 'Budapest', 'email': 'matyi@gmail.com','password':'a'},
         {'first_name': 'Imi', 'last_name': 'Fodor', 'school': 'Budapest', 'email': 'imi@gmail.com','password':'a'},
         {'first_name': 'Laci', 'last_name': 'Molnar', 'school': 'Budapest', 'email': 'laci@gmail.com','password':'a'},
         {'first_name': 'Agnieszka', 'last_name': 'Koszany', 'school': 'Krakow', 'email': 'agni@gmail.com','password':'a'},
         {'first_name': 'Robert', 'last_name': 'Kohanyi', 'school': 'Miskolc', 'email': 'robert@gmail.com','password':'a'}]

applicants=[{'first_name': 'Alexandra', 'last_name': 'Ivan', 'gender': 'female', 'city': 'Budapest',
             'email': 'ivan@gmail.com','status': 'NEW','password':'a'},
            {'first_name': 'Patrik', 'last_name': 'Blik', 'gender': 'male', 'city': 'Szekesfehervar',
             'email': 'blik@gmail.com','status': 'NEW','password':'a'},
            {'first_name': 'David', 'last_name': 'Szilniczky', 'gender': 'male','city': 'Krakow',
             'email': 'szili@gmail.com','status': 'NEW','password':'a'},
            {'first_name': 'Fanni', 'last_name': 'Perjesi', 'gender': 'female','city': 'Eger',
             'email': 'perj@gmail.com','status': 'NEW','password':'a'}]

interview_slots=[{'start': '2017-09-01 09:00:00', 'end': '2017-09-01 13:00:00', 'mentor': 'Matyi'},
                 {'start': '2017-09-02 10:00:00', 'end': '2017-09-02 14:00:00', 'mentor': 'Laci'},
                 {'start': '2017-09-03 11:00:00', 'end': '2017-09-03 15:00:00', 'mentor': 'Imi'},
                 {'start': '2017-09-04 12:00:00', 'end': '2017-09-04 16:00:00', 'mentor': 'Robert'},
                 {'start': '2017-09-05 13:00:00', 'end': '2017-09-05 17:00:00', 'mentor': 'Agnieszka'}]

questions = [{'question': 'Could you give me a (KOA)Laptop?', 'applicant': 'David',
              'date': '2017-09-05 17:00:00' }]

for city in cities:
    City.create(name=city['name'],school=city['school'])

for admin in admins:
    Admin.create(email=admin['email'], password=admin['password'])

for mentor in mentors:
    Mentor.create(first_name=mentor['first_name'], last_name=mentor['last_name'], email=mentor['email'],password=mentor['password'],school=School.select().where(School.location == mentor['school']).get())

for applicant in applicants:
    Applicant.create(status=applicant['status'], application_code=None, first_name=applicant['first_name'],
                     last_name=applicant['last_name'], email=applicant['email'], password=applicant['password'], gender=applicant['gender'],
                     city=City.select().where(City.name==applicant['city']).get(), school=None)

for interview_slot in interview_slots:
    InterviewSlot.create(start=interview_slot['start'], end=interview_slot['end'],
                         mentor=Mentor.select().where(Mentor.first_name == interview_slot['mentor']).get())

for question in questions:
    Question.create(applicant=Applicant.select().where(Applicant.first_name==question['applicant']).get(),question=question['question'], date=question['date'])

