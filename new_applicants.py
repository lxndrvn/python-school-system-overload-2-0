# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!

import uuid
from models import *

def new_application():
	print("Let us know Your information to Apply!")
	first_name=input("Given Name: ")
	last_name=input("Familiy Name: ")
	gender=input("Gender: ")
	email=input("Email address: ")
	city=input("Home city: ")
	Applicant.create(application_code="",first_name=first_name,last_name=last_name,gender=gender,email=email,city=City.select().where(City.name==city).get(),school=City.select().where(City.name==city).get().school,status="NEW")

def generate_code():
    return str(uuid.uuid4())

def handle_new_applicants():
    new_applicants = Applicant.select().where(Applicant.status == "New")
    for applicant in new_applicants:
        applicant.application_code = generate_code()
        school_for_applicant = Applicant.city.school
        applicant.update(application_code=id, school=school_for_applicant)
