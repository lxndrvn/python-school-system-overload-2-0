# This script can create the database tables based on your models
from example_data import *

db.connect()
db.drop_tables([School, City, Applicant, Mentor, InterviewSlot, Interview], safe=True,	cascade=True)
# List the tables here what you want to create...
db.create_tables([School, City, Applicant, Mentor, InterviewSlot, Interview], safe=True)

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

for mentor in mentors:
    Mentor.create(first_name= mentor['first_name'], last_name=mentor['last_name'], email=mentor['email'],school=School.select().where(School.location == mentor['school']).get())

for applicant in applicants:
    Applicant.create(status=applicant['status'], application_code=None, first_name=applicant['first_name'],
                     last_name=applicant['last_name'], email=applicant['email'], gender=applicant['gender'],
                     city=City.select().where(City.name==applicant['city']).get(), school=None)

for interview_slot in interview_slots:
    InterviewSlot.create(start=interview_slot['start'], end=interview_slot['end'],
                         availability=Mentor.select().where(Mentor.school==bpschool).count())