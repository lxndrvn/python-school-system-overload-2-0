from peewee import *
from connect import create_database

db = create_database()

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db

class School(BaseModel):
    #entries should contain the existing schools of Codecool like Miskolc, Budapest, Krakow
    location = CharField()

class City(BaseModel):
    #entries should contain all the information about cities where is no Codecool School yet, so we can find easily the closest city where is a School. Example data:
    #Miskolc -> Miskolc
    #Eger -> Miskolc
    #Budapest -> Budapest
    #Székesfehérvár -> Budapest
    name = CharField()
    school = ForeignKeyField(School,related_name="school")


class Applicant(BaseModel):
    application_code = CharField()
    first_name = CharField()
    last_name = CharField()
    gender = CharField()
    email = CharField(unique=True)
    city = ForeignKeyField(City)
    school = ForeignKeyField(School)
    status = CharField()

class Mentor(BaseModel):
    #entries should contain all the information about possible interview slots of mentors with specific date/time info. Example data:
    #Start: 2016-09-01 10:00
    #End: 2016-09-01 11:00
    #Reserved: true/false
    #Mentor: related mentor object
    first_name=CharField()
    last_name=CharField()
    school=ForeignKeyField(School)
    email=CharField()

class InterviewSlot(BaseModel):
    start=CharField()
    end=CharField()
    reserved=BooleanField()
    mentor=ForeignKeyField(Mentor)

class Interview(BaseModel):
    start=ForeignKeyField(InterviewSlot)
    end=CharField()
    applicant=ForeignKeyField(Applicant)
    mentor=ForeignKeyField(Mentor)

class Question(BaseModel):
    pass

class Answer(BaseModel):
    pass