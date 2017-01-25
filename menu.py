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
    print(" 1.Interviews", "\n", "2.Applicants", "\n", "0.Back")
    try:
        choice = int(input("Choose 1, 2 or 0 to go back:"))
        if not (0 <= choice <= 2):
            raise ValueError()
    except ValueError:
        print("Invalid Option, you needed to type a 1, 2 or 0.")
    options=[Menu(), Interview.list_of_interviews(), Applicant.applicants()]
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
    options=[Menu(), Interviews.list_interviews(), Applicant.new_applications()]
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
    options=[Menu(), Applicant.find_application(), Interview.find_interview(), new_applicants.new_application()]
    option[choice]
else:
    pass
