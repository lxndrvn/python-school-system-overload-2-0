from peewee import *
from database import *

db = create_database()

class BaseModel(Model):
    class Meta:
        database = db


class School(BaseModel):
    location = CharField()


class City(BaseModel):
    name = CharField()
    school = ForeignKeyField(School, related_name="school")


class Applicant(BaseModel):
    application_code = CharField(null=True)
    first_name = CharField()
    last_name = CharField()
    gender = CharField()
    email = CharField(unique=True)
    city = ForeignKeyField(City, null=True)
    school = ForeignKeyField(School, null=True)
    status = CharField()


class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School, related_name="mentors")
    email = CharField()


class InterviewSlot(BaseModel):
    start = CharField()
    end = CharField()
    mentor = ForeignKeyField(Mentor, related_name='interview_slots', null=True)


class Interview(BaseModel):
    applicant = ForeignKeyField(Applicant, related_name="interviews", null=True)
    interview_slot = ForeignKeyField(InterviewSlot, related_name="interviews", null=True)


class Question(BaseModel):
    question = CharField()
    status = CharField(default="NEW")
    applicant = ForeignKeyField(Applicant, related_name="questions", null=True)
    mentor = ForeignKeyField(Mentor, related_name="questions", null=True)
    date = DateTimeField()


class Answer(BaseModel):
    answer = CharField()
    question = ForeignKeyField(Question, related_name="answers")


class Admin(BaseModel):
    email = CharField()
    password = CharField()

