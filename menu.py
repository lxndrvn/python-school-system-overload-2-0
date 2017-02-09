import user_interfaces
import os
from new_questions import *


class Menu(object):
    def __init__(self):
        self.interface = user_interfaces.Interface()

        permission = input("Welcome to Codecool.\nPlease choose your permission.\n1.Applicant | 2.Mentor | 3.Admin | 0.Exit\n")

        permission = int(permission)
        if not (0 <= permission <= 3):
            print("Invalid Option, you needed to type a 1, 2, 3 or 0.")
            Menu()

        if permission == 0:
            exit()
        elif permission == 1:
            self.ApplicantMenu()
        elif permission == 2:
            self.MentorMenu()
        elif permission == 3:
            self.AdminMenu()

        else:
            print("Invalid Option, you needed to type a 1, 2, 3 or 0.\n")
            Menu()

    def ApplicantMenu(self):
        choice = input("1.Apply | 2.Interview Subscription | 3.My Application | 4. Question | 0.Back\n")

        try:
            choice = int(choice)
            if not (0 <= choice <= 4):
                print("Invalid Option, you needed to type a 1, 2, 3, 4 or 0.\n")
                self.ApplicantMenu()

            os.system('cls' if os.name == 'nt' else 'clear')

            if choice == 0:
                Menu()
            if choice == 1:
                self.interface.apply()
                self.ApplicantMenu()
            if choice == 2:
                self.interface.subscribe_to_interview()
                self.ApplicantMenu()

            if choice == 3:
                user = Applicant.select().where(Applicant.application_code == input("Select your application code (0 to cancel): "))
                if user == "0":
                    self.ApplicantMenu()
                else:
                    self.interface.show_application(user)

            if choice == 4:
                question = input("What is your question?")
                QuestionInterface.new_question(question)
            self.ApplicantMenu()

        except:
            print("Invalid option, you needed to type a 1, 2, 3 or 0.\n")
            self.ApplicantMenu()

    def MentorMenu(self):
        choice = input("1: Interviews | 2: Questions | 0: Back\n")

        choice = int(choice)
        if not (0 <= choice <= 2):
            print("Invalid Option, you needed to type a 1, 2 or 0.\n")
            self.MentorMenu()

        os.system('cls' if os.name == 'nt' else 'clear')

        if choice == 0:
            Menu()
        elif choice == 1:
            mentoremail = input("Sign in with Your mentor email address (0 to cancel): ")
            if mentoremail == "0":
                return
            teacher = Mentor.select().where(Mentor.email == mentoremail).get()
            Interview.print_table(query=Interview.select().where(Interview.mentor == teacher))
            self.interface.interview_duty()
            self.MentorMenu()
        elif choice == 2:
            self.MentorMenu()

        else:
            print("Invalid option, you needed to type a 1, 2, 3 or 0.\n")
            self.MentorMenu()

    def AdminMenu(self):
        choice = input("1.Review Applications | 2.Accept New Applicants | 3.Check on Interviews | 4. Check new questions | 0.Back\n")


        choice = int(choice)
        if not (0 <= choice <= 4):
            print("Invalid Option, you needed to type a 1, 2, 3, 4 or 0.\n")
            self.AdminMenu()

        os.system('cls' if os.name == 'nt' else 'clear')

        if choice == 0:
            Menu()
        elif choice == 1:
            Applicant.print_table(query=Applicant.select())
            self.AdminMenu()
        elif choice == 2:
            self.interface.accept_new_applicants()
            self.AdminMenu()
        elif choice == 3:
            self.interface.check_interviews()
            self.AdminMenu()
        elif choice == 4:
            Question.print_table(query=Question.select().where(Question.status == "NEW"))
            self.AdminMenu()

        else:
            print("Invalid Option, you needed to type a 1, 2 or 3.\n")
            self.AdminMenu()
