from models import *
import user_interfaces
import os


class Menu():
    def __init__(self):
        permission = int(input("Welcome to Codecool.\nPlease choose your permission.\n1.Applicant | 2.Mentor | 3.Admin | 0.Exit\n"))
        if permission == 0:
            exit()
        elif permission == 1:
            self.ApplicantMenu()
        elif permission == 2:
            self.MentorMenu()
        elif permission == 3:
            self.AdminMenu()
        if not (0 <= permission <= 3):
            print("Invalid Option, you needed to type a 1, 2, 3 or 0.")
            Menu()

    def ApplicantMenu(self):
        choice = int(input("1.Apply | 2.Interview Subscription | 3.My Application 0.Back\n"))
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice == 0:
            Menu()
        if choice == 1:
            global user
            user = user_interfaces.new_application()
            self.ApplicantMenu()
        if choice == 2:
            user_interfaces.interview_subscription()
            self.ApplicantMenu()
        if choice == 3:
            if 'user' in globals():
                user_interfaces.my_application(user)
            else:
                user = Applicant.select().where(Applicant.application_code == input("Select your application code (0 to cancel): "))
                if user == "0":
                    self.ApplicantMenu()
                else:
                    user_interfaces.my_application(user)
            self.ApplicantMenu()
        if not (0 <= choice <= 3):
            print("Invalid Option, you needed to type a 1, 2, 3 or 0.\n")
            self.ApplicantMenu()

    def MentorMenu(self):
        choice = int(input("1: Interviews | 2: Applicants | 0: Back\n"))
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice == 0:
            Menu()
        if choice == 1:
            user_interfaces.interview_duty()
            self.MentorMenu()
        if choice == 2:
            self.MentorMenu()
        if not (0 <= choice <= 2):
            print("Invalid Option, you needed to type a 1, 2 or 0.\n")
            self.MentorMenu()

    def AdminMenu(self):
        choice = int(input("1.Review Applications | 2.Accept New Applicants | 3.Check on Interviews | 0.Back\n"))
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice == 0:
            Menu()
        if choice == 1:
            user_interfaces.check_applications()
            self.AdminMenu()
        if choice == 2:
            user_interfaces.accept_new_applicants()
            self.AdminMenu()
        if choice == 3:
            user_interfaces.check_interviews()
            self.AdminMenu()
        if not (0 <= choice <= 2):
            print("Invalid Option, you needed to type a 1, 2 or 0.\n")
            self.AdminMenu()
