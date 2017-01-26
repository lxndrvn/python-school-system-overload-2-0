# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!
import random
import uuid
from models import *

def new_application():
	print("Let us know Your information to Apply!")
	first_name=input("Given Name: ")
	last_name=input("Familiy Name: ")
	gender=input("Gender: ")
	email=input("Email address: ")
	city=input("Home city: ")
	Applicant.create(status="NEW",application_code=None,first_name=first_name,last_name=last_name,gender=gender,email=email,city=City.select().where(City.name==city).get(),school=None)
	print('Application Successful! Review status in menu 1.')

def check_applications():
	for applicant in Applicant.select():
		print(applicant.status,"|",applicant.application_code,"|",applicant.first_name,"|",applicant.last_name,"|",applicant.city.name,"|",applicant.school.location if applicant.school!=None else None)
	print('There are',len([applicant for applicant in Applicant.select().where(Applicant.status=="NEW")]),'new applicants! woohoo! Accept them buddy!')

def handle_new_applicants():
	for applicant in Applicant.select().where(Applicant.status=="NEW"):
	    applicant.application_code = uuid.uuid4()
	    applicant.school=applicant.city.school
	    applicant.status = "ACCEPTED"
	    applicant.save()
	    print(applicant.first_name,"accepted")

def check_interviewslots():
	for interviewslot in InterviewSlot.select():
		print(interviewslot.id,interviewslot.start,"|",interviewslot.end,"|",interviewslot.reserved)
	print("Choose a slot when we can get to know each other!")
