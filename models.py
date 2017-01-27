from peewee import *
from connect import create_database

db = create_database()


class BaseModel(Model):
    class Meta:
        database = db


class School(BaseModel):
    location = CharField()


class City(BaseModel):
    name = CharField()
    school = ForeignKeyField(School,related_name="school")


class Applicant(BaseModel):
    application_code = CharField(null=True)
    first_name = CharField()
    last_name = CharField()
    gender = CharField()
    email = CharField(unique = True)
    city = ForeignKeyField(City,null=True)
    school = ForeignKeyField(School,null=True)
    status = CharField()


class Mentor(BaseModel):
    first_name=CharField()
    last_name=CharField()
    school=ForeignKeyField(School)
    email=CharField()


class InterviewSlot(BaseModel):
    start=CharField()
    end=CharField()
    availability=ForeignKeyField(Mentor,null=True)


class Interview(BaseModel):
    start=CharField()
    end=CharField()
    applicant=ForeignKeyField(Applicant,null=True)
    mentor=ForeignKeyField(Mentor,null=True)


class Question(BaseModel):
    pass


class Answer(BaseModel):
    pass