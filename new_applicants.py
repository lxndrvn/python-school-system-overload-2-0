# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!

import uuid
from models import *

def new_application():
	first_name=input("Name: ")
	last_name=input("Last name: ")

	Applicant.create(first_name,last_name)

def handle_new_applicants():
    new_applicants = Applicant.select().where(Applicant.application_code == None)
    for applicant in new_applicants:
        id = generate_id()
        school_for_applicant = Applicant.city.school
        applicant.update(application_code=id, school=school_for_applicant)

def generate_id():
    return str(uuid.uuid4())