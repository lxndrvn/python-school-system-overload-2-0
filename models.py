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
    application_code = CharField(null=True)
    first_name = CharField()
    last_name = CharField()
    gender = CharField()
    email = CharField(unique=True)
    city = ForeignKeyField(City,null=True)
    school = ForeignKeyField(School,null=True)
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