from models import *
import new_applicants

class Menu():
    def __init__(self):
        permission = int(input("Welcome to Codecool.\n\
        Please choose your permission.\n\
        1.Applicant | 2.Mentor | 3.Admin | 0.Exit\n"))
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
        choice = int(input("1: Interviews | 2: Applicants | 0: Back\n"))
        if choice==0:
            Menu()
        if choice==1:
            Interview.list_of_interviews()
        if choice==2:
            Applicant.applicants()
        options[choice]
        if not (0 <= choice <= 2):
            raise ValueError()
            print("Invalid Option, you needed to type a 1, 2 or 0.\n")

    def ApplicantMenu(self):
        choice = int(input("1.Interview 2.New applicants 0.Back\n"))
        if choice==0:
            Menu()
        if choice==1:
            Interviews.list_interviews()
        if choice==2:
            Applicant.new_applications()
        if not (0 <= choice <= 1):
                raise ValueError()
                print("Invalid Option, you needed to type a 1 or 0.\n")
    
    def ApplicantMenu(self):
        choice = int(input("1.Application Details 2.Interview Details 3.Apply 0.Back\n"))
        if choice==0:
            Menu()
        if choice==1:
            Interviews.list_interviews()
        if choice==2:
            Applicant.new_applications()
        if choice==3:
            new_applicants.new_application()
            if not (0 <= choice <= 3):
                raise ValueError()
                print("Invalid Option, you needed to type a 1, 2, 3 or 0.\n")
Menu()