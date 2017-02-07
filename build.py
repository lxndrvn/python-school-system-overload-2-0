# This script can create the database tables based on your models
from example_data import *

db.connect()
db.drop_tables([School, City, Applicant, Mentor, InterviewSlot, Interview, Question], safe=True, cascade=True)
# List the tables here what you want to create...
db.create_tables([School, City, Applicant, Mentor, InterviewSlot, Interview, Question], safe=True)

ExampleData()