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
		while applicant.application_code in [accepted.application_code for accepted in Applicant.select()]:
		    applicant.application_code = "".join([str(random.randint(0,10)),str(random.randint(0,10)),str(random.randint(0,10))]) #if x not in [application.application_code for applicant in Applicant.select()]
		applicant.school=applicant.city.school
		applicant.status = "ACCEPTED"
		applicant.save()
		print(applicant.first_name,"accepted")

def interview_subscription():
	key=input("Provide Your application code to make an appointment (0 to cancel): ")
	if key==0:
		return None
	elif key not in [applicant.application_code for applicant in Applicant.select()]:
		print("No such application in our records. ")
		interview_subscription()
	applicant=Applicant.select().where(Applicant.application_code==key).get()
	InterviewSlot.update(availability=Mentor.select().where(Mentor.school==applicant.school).count()).execute()
	for interviewslot in InterviewSlot.select():
		print(interviewslot.id,interviewslot.start,"|",interviewslot.end,"|",interviewslot.availability)
	interviewid=int(input("Choose a slot when we can get to know each other! "))
	if InterviewSlot.select().where(InterviewSlot.id==interviewid).get().availability==0:
		print("Sorry, we're all busy that time already, could we arrange an other time? ")
		interview_subscription()
	else:
		if InterviewSlot.select().where(InterviewSlot.id==interviewid).get().start in [interview.start for interview in Interview.select()]:
			busymentors=[mentor for mentor in Interview.select().where(Interview.start==InterviewSlot.select().where(InterviewSlot.id==interviewid).get().start)]
			yourmentor=[mentor for mentor in Mentor if mentor not in busymentors][0]
		else:
			yourmentor=[mentor for mentor in Mentor][0]
		Interview.create(start=InterviewSlot.select().where(InterviewSlot.id==interviewid).get().start,end=InterviewSlot.select().where(InterviewSlot.id==interviewid).get().end,applicant=applicant,mentor=yourmentor)