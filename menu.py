from models import *
import new_applicants

class Menu():
    def __init__(self):
        permission = int(input("Welcome to Codecool.\nPlease choose your permission.\n1.Applicant | 2.Mentor | 3.Admin | 0.Exit\n"))
        if permission==0:
            exit()
        elif permission==1:
            self.ApplicantMenu()
        elif permission==2:
            self.MentorMenu()
        elif permission==3:
            self.AdminMenu()
        if not (0 <= permission <= 3):
            raise ValueError()
            print("Invalid Option, you needed to type a 1, 2, 3 or 0.")

    def ApplicantMenu(self):
        choice = int(input("1.Application Details 2.Interview Details 3.Apply 0.Back\n"))
        if choice==0:
            Menu()
        if choice==1:
            Interviews.list_interviews()
        if choice==2:
            new_applicants.my_applications()
        if choice==3:
            new_applicants.new_application()
        if not (0 <= choice <= 3):
            print("Invalid Option, you needed to type a 1, 2, 3 or 0.\n")
            self.ApplicantMenu()

    def MentorMenu(self):
        choice = int(input("1: Interviews | 2: Applicants | 0: Back\n"))
        if choice==0:
            self
        if choice==1:
            Interview.list_of_interviews()
        if choice==2:
            Applicant.applicants()
        options[choice]
        if not (0 <= choice <= 2):
            print("Invalid Option, you needed to type a 1, 2 or 0.\n")
            self.MentorMenu()

    def AdminMenu(self):
        choice = int(input("1.Interview 2.New applicants 0.Back\n"))
        if choice==0:
            Menu()
        if choice==1:
            Interviews.list_interviews()
        if choice==2:
            new_applicants.new_applications()
        if not (0 <= choice <= 1):
            print("Invalid Option, you needed to type a 1 or 0.\n")
            self.AdminMenu()    
Menu()