# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!
import random

from models import *


class Interface(object):
    def __init__(self,user=None):
        self.applicants = Applicant.select()
        self.mentors = Mentor.select()
        self.user=user

    @property
    def new_applicants(self):
        return self.applicants.where(Applicant.status == "NEW")

    def generate_unique_code(self):
        codes = [applicant.application_code for applicant in self.applicants.where(Applicant.status == "ACCEPTED")]
        new_code = str(random.randint(100, 999))
        if new_code in codes:
            self.generate_unique_code()
        else:
            return new_code

    def check_applications(self):
        Applicant.print_table()
        print('There are',len(Applicant.select().where(Applicant.status=="NEW")),
            'new applicants! woohoo! Accept them buddy!')

    def accept_new_applicants(self):
        for applicant in self.new_applicants:
            applicant.application_code = self.generate_unique_code()
            applicant.school = applicant.city.school
            applicant.status = "ACCEPTED"
            applicant.save()
            print(applicant.first_name, "accepted")

    def apply(self):
        print("Let us know Your information to Apply!")
        first_name = input("Given Name: ")
        last_name = input("Family Name: ")
        gender = input("Gender: ")
        email = input("Email address: ")
        city = input("Home city: ")
        while city not in [city.name for city in City.select()]:
            print("Sorry, application is not available in Your city Yet. Please select another one.")
            city = input("Home city: ")
        print('Application Successful! Review status in menu 1.')
        user = Applicant.create(
            status="NEW", application_code=None, first_name=first_name, last_name=last_name,
            gender=gender, email=email, city=City.select().where(City.name == city).get(), school=None
        )
        return user

    def show_application(self):
        Applicant.print_table(Applicant.application_code==self.user.application_code)

    def subscribe_to_interview(self):
        InterviewSlot.update(mentor=Mentor.select().where(Mentor.school == self.user.school).count()).execute()
        InterviewSlot.print_table()
        interviewid = int(input("Choose a slot when we can get to know each other! "))
        if interviewid==0:return
        if InterviewSlot.select().where(InterviewSlot.id == interviewid).get().mentor == 0:
            while InterviewSlot.select().where(InterviewSlot.id == interviewid).get().mentor == 0:
                interviewid = int(input("Sorry, we're all busy that time already, could we arrange an other time? "))
        interviewslot=InterviewSlot.select().where(InterviewSlot.id == interviewid).get()
        if interviewslot.start in [interview.interview_slot.start for interview in Interview.select()]:
            busymentors = [interview.mentor for interview in Interview.select().where(Interview.interview_slot == interviewslot)]
            yourmentor = random.choice([mentor for mentor in Mentor.select() if mentor not in busymentors])
        else:
            yourmentor = [mentor for mentor in Mentor.select()][0]
        Interview.create(interview_slot=interviewslot,applicant=self.user, mentor=yourmentor)

    def interview_duty(self):
        mentoremail = input("Sign in with Your mentor email address (0 to cancel): ")
        if mentoremail == "0":
            return
        teacher = Mentor.select().where(Mentor.email == mentoremail).get()
        Interview.print_table(Interview.mentor == teacher)

    def check_interviews(self):
        Interview.print_table()

        filter = input("FILTER: 1.By School 2.By Applicant 3.By Mentor 4.By date EXIT: 0. ")

        if filter == "0":
            return
        if filter == "1":
            self.filter_by_school()

        if filter == "2":
            self.filter_by_applicant()

        if filter == "3":
            self.filter_by_mentor()

        if filter == "4":
            self.filter_by_date()

    def filter_by_school(self):
        school = input("Applications to School: ")
        schools = [school.location for school in School.select()]
        if school not in schools:
            while school not in schools:
                if school == "0": return
                school = input("No school there (0 to cancel): ")
        Interview.print_table(Interview.mentor in [mentor for mentor in Mentor.select().where(Mentor.school in [cool for cool in School.select().where(School.location==school)])])

    def filter_by_applicant(self):
        code = input("Applicant code: ")
        codes = [applicant.application_code for applicant in Applicant.select()]
        if code not in codes:
            while code not in codes:
                if code == "0": return
                code = input("No such application (0 to cancel): ")
        Interview.print_table(Interview.applicant == Applicant.select().where(Applicant.application_code==code))

    def filter_by_mentor(self):
        name = input("Mentor's first name: ")
        names = [mentor.first_name for mentor in Mentor.select()]
        if name not in names:
            while name not in names:
                if name == "0": return
                name = input("No such mentor (0 to cancel): ")
        Interview.print_table(Interview.mentor == Mentor.select().where(Mentor.first_name==name))

    def filter_by_date(self):
        date = input("Interview start time: ")
        dates = [interviewslot.start for interviewslot in InterviewSlot.select()]
        if date not in dates:
            while date not in dates:
                if date == "0": return
                date = input("No such mentor (0 to cancel): ")
        Interview.print_table(Interview.interview_slot.start == date)

