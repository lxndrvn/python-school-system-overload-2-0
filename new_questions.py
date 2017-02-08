# New questions (from random applicants) created into your project database by this script.
# You can run it anytime to generate new questions!
from models import *

class QuestionInterface:

    @staticmethod
    def new_question(question):
        Question(question)


    def accept_new_questions(self):
        for question in self.new_questions:
            question.applicant.application_code = self.generate_unique_code()
            question.applicant.school = question.applicant.city.school
            question.status = "waiting for answer"
            question.mentor = question.mentor
            question.date = question.date
            question.save()
            print("New questions waiting for answer now.")


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


    def get_answer(self):
        answer = Question.select(Applicant, Question).join(Applicant).where(
            Applicant.application_code == input("Give your application code: "))
        for data in answer:
            print(data.question.questions, "|", data.question.status, "|", data.answer, "|")

