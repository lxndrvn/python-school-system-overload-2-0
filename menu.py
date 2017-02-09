import user_interfaces
import os
from new_questions import *

class Menu(object):
    def __init__(self,session=True,login=False):
        self.interface = user_interfaces.Interface()
        self.session=session
        os.system('cls' if os.name == 'nt' else 'clear')

    def opt(self):
        for option in self.options:
            index=self.options.index(option)
            function=option.__name__.translate({ord("_"):" ",})
            print(index,function,end=" ")
        self.option = int(input())
        if self.option not in range(len(self.options)):
            while self.option not in range(len(self.options)):
                self.option=int(input("Invalid Option, choose up to",len(self.options)-1))
        self.options[self.option]()

    def exit(self):
        self.session=False

    def logout(self):
        self.login=False


class Login(Menu):
    def __init__(self):
        super().__init__()
        self.options = [self.exit,Applicant,Mentor,Admin]
        print("Welcome to Codecool! \nChoose user to log in: ")
        self.opt()


class Applicant(Menu):
    def __init__(self,login=True,user=None):
        super().__init__()
        self.login=login
        self.options = [self.logout,self.interface.apply,self.interface.subscribe_to_interview,self.interface.show_application,QuestionInterface.new_question]
        print("logged in as",self.__class__.__name__)
        while self.login==True:
            self.opt()


class Mentor(Menu):
    def __init__(self,login=True,user=None):
        super().__init__()
        email=input()
        emails=[mentor.email for mentor in self.interface.mentors]
        if email not in emails:
            while email not in emails:
                if email == "0": return
                email=input("Invalid email, try again ")
        self.login=True
        self.options = [self.logout,self.interface.interview_duty,QuestionInterface.reply]
        print("logged in as",self.interface.mentors.where(Mentor.email==email))
        while self.login==True:
            self.opt()


class Admin(Menu):
    def __init__(self,login=False,user=None):
        super().__init__()
        self.login=True
        self.options = [self.logout,self.interface.check_applications,self.interface.accept_new_applicants,self.interface.check_interviews,QuestionInterface.check_questions]
        print("logged in as",self.__class__.__name__)
        while self.login==True:
            self.opt()
