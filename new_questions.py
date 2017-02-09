# New questions (from random applicants) created into your project database by this script.
# You can run it anytime to generate new questions!
from models import *
import time
import random

class QuestionInterface:

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
        for question in self.question:
            print(
                question.status, "|",
                question.questions, "|",
                question.answer, "|",
                question.mentor, "|",
                question.applicant, "|",
            )
        print(
            'There are',
            len(self.new_questions),
            'new questions! woohoo! Send to mentors to answer them!'
        )

    def give_answer(self):
        answer = Question.select(Applicant, Question).join(Applicant)
        for data in answer:
            print(data.question.questions, "|", data.question.status, "|", data.answer, "|")

