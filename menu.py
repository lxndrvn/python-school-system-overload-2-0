import user_interfaces
import os
from new_questions import *

class Menu(object):
    def __init__(self,session=True,user=None,options=[],interface=None):
        self.session=session
        self.interface=user_interfaces.Interface()
        self.user=user

    def opt(self):
        for option in self.options:
            index=self.options.index(option)
            function=option.__name__.translate({ord("_"):" ",})
            print(index,function,end=" ")
        self.option = int(input())
        if self.option not in range(len(self.options)):
            while self.option not in range(len(self.options)):
                self.option=int(input("Invalid Option, choose up to",len(self.options)-1))
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            self.options[self.option](self.user)
        except:
            self.options[self.option]()

    def login(self):
        self.options=[self.exit,self.applicant,self.mentor,self.admin]
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to Codecool! \nChoose user to log in: ")
        self.opt()

    def applicant(self):
        application_code=input("Enter application code (N to apply): ")
        if application_code=="N": 
            self.interface.apply()
            return
        application_codes=[applicant.application_code for applicant in Applicant.select()]
        if application_code not in application_codes:
            while application_code not in application_codes:
                if application_code == "0": return
                application_code=input("Invalid application code, try again (0 to cancel): ")
        self.user=self.interface.applicants.where(Applicant.application_code==application_code).get()
        self.interface = user_interfaces.Interface(self.user)
        self.options = [self.logout,self.interface.subscribe_to_interview,self.interface.show_application,QuestionInterface.new_question]
        print("logged in as",self.user.first_name)
        while self.user!=None:
            self.opt()

    def mentor(self):
        email=input("email: ")
        emails=[mentor.email for mentor in self.interface.mentors]
        if email not in emails:
            while email not in emails:
                if email == "0": return
                email=input("Invalid email, try again (0 to cancel): ")
        self.user=self.interface.mentors.where(Mentor.email==email).get()
        self.options = [self.logout,self.interface.interview_duty,QuestionInterface.reply]
        print("logged in as",self.user.first_name)
        while self.user!=None:
            self.opt()

    def admin(self):
        self.user="admin"
        self.options = [self.logout,self.interface.check_applications,self.interface.accept_new_applicants,self.interface.check_interviews,QuestionInterface.check_questions,QuestionInterface.accept_new_questions]
        print("logged in as",self.user)
        while self.user!=None:
            self.opt()

    def logout(self):
        self.user=None

    def exit(self):
        self.session=False

