from models import *
import new_applicants
import os
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
            print("Invalid Option, you needed to type a 1, 2, 3 or 0.")
            Menu()

    def ApplicantMenu(self):
        choice = int(input("1.Application Details 2.Interview Details 3.Apply 0.Back\n"))
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice==0:
            Menu()
        if choice==1:
            Interviews.list_interviews()
        if choice==2:
            new_applicants.my_applications()
        if choice==3:
            new_applicants.new_application()
            print('Application Successful! Review status in menu 1.')
            self.ApplicantMenu()
        if not (0 <= choice <= 3):
            print("Invalid Option, you needed to type a 1, 2, 3 or 0.\n")
            self.ApplicantMenu()

    def MentorMenu(self):
        choice = int(input("1: Interviews | 2: Applicants | 0: Back\n"))
        os.system('cls' if os.name == 'nt' else 'clear')

        if choice==0:
            self
        if choice==1:
            Interview.list_of_interviews()
            print('Application Successful! Review status in menu 1.')
            self.ApplicantMenu()
        if choice==2:
            Applicant.applicants()
            self.ApplicantMenu()
        options[choice]
        if not (0 <= choice <= 2):
            print("Invalid Option, you needed to type a 1, 2 or 0.\n")
            self.MentorMenu()

    def AdminMenu(self):
        choice = int(input("1.Review Applications 2.Accept New Applicants 0.Back\n"))
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice==0:
            Menu()
        if choice==1:
            new_applicants.check_applications()
            self.AdminMenu()
        if choice==2:
            new_applicants.handle_new_applicants()
            self.AdminMenu()
        if not (0 <= choice <= 2):
            print("Invalid Option, you needed to type a 1, 2 or 0.\n")
            self.AdminMenu()    
Menu()