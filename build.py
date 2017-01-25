# This script can create the database tables based on your models
from connect import create_database
from models import *

db.connect()
db.drop_tables([School, City, Applicant, Mentor, InterviewSlot, Interview])
# List the tables here what you want to create...
db.create_tables([School, City, Applicant, Mentor, InterviewSlot, Interview], safe=True)