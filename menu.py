from models import *
import new_applicants
print("Welcome to Codecool.")
print("Please choose your permission.")
print(" 1.Admin", "\n","2.Mentor", "\n","3.Applicant", "\n", "0.Exit")

try:
    permission = int(input("Choose 1, 2, 3 or 0 to exit:"))
    if not (0 <= permission <= 3):
        raise ValueError()
except ValueError:
    print("Invalid Option, you needed to type a 1, 2, 3 or 0.")

if permission==0:
    exit()

if permission==1:
    try:
        choice = int(input("1: Interviews | 2: Applicants | 0: Back"))
        if not (0 <= choice <= 2):
            raise ValueError()
    except ValueError:
        print("Invalid Option, you needed to type a 1, 2 or 0.")
    options=[Interview.list_of_interviews(), Applicant.applicants()]
    options[choice]
else:
    pass

if permission==2:
    print(" 1.Interview", "\n", "2.New applicants", "\n", "0.Back")
    try:
        choice = int(input("Choose 1 or 0 to go back:"))
        if not (0 <= choice <= 1):
            raise ValueError()
    except ValueError:
        print("Invalid Option, you needed to type a 1 or 0.")
    options=[Interviews.list_interviews(), Applicant.new_applications()]
    options[choice]
else:
    pass

if permission==3:
    print(" 1.Application Details", "\n", "2.Interview Details", "\n", "3.Apply","\n", "0.Back")
    try:
        choice = int(input("Choose 1, 2 or 0 to go back:"))
        if not (0 <= choice <= 3):
            raise ValueError()
    except ValueError:
        print("Invalid Option, you needed to type a 1, 2, 3 or 0.")
    options=[new_applicants.new_application()]
    options[choice]
else:
    pass
