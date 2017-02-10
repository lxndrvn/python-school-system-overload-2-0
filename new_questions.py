# New questions (from random applicants) created into your project database by this script.
# You can run it anytime to generate new questions!
from models import *
import time
import random

class QuestionInterface:
    def __init__(self):
        self.questions=Question.select()

    def new_question(question=None,user=None):
        if user not in [applicant.application_code for applicant in Applicant.select()]:
            print("That application code doesn't exist. Please check your application code again. ")
        else:
            question = input("What is your question?")
            Question.create(question = question, date = time.strftime("%Y-%m-%d %I:%M:%S"),
                            applicant=Applicant.select().where(Applicant.application_code==user).get())

    def accept_new_questions(self):
        for question in Question.select().where(Question.status == 'NEW'):
            question.status = "waiting for answer"
            question.mentor = random.choice(Mentor.select().where(question.applicant.school == Mentor.school).get())
            question.save()
            print("Question", question.id, "was assigned to", question.mentor)

    def check_questions(self):
        condition=Question.status=="NEW"
        Question.print_table(condition)
        print('There are',len(Question.select().where(condition)),'new questions! woohoo! Send to mentors to answer them!')

    def reply(self):
        mentoremail=input("email: ")
        mentor=Mentor.select().where(Mentor.email == mentoremail).get()
        Question.print_table(Question.mentor==mentor)

