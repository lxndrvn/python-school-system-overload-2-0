from peewee import *
from connect import create_database

db = create_database()


class BaseModel(Model):
    class Meta:
        database = db

    @classmethod
    def print_table(cls,query):
        cls.query=query
        records=[record for record in query]
        fields=sorted(list(records[0].__dict__['_data'].keys()))
        print(" "*(sum([max([len(str(column.__dict__['_data'][field])) for column in records]+[len(str(field))])+3 for field in fields])//2)+cls.__name__)
        print(" /"+"-"*(sum([max([len(str(column.__dict__['_data'][field])) for column in records]+[len(str(field))])+3 for field in fields])-1)+"\\")
        for field in fields:
            fieldspan=max([len(str(column.__dict__['_data'][field])) for column in records]+[len(str(field))])
            justify=" "*(fieldspan-len(field))
            print(" | "+field.upper()+justify,end="")
        print(" |")
        for record in records:
            for field in fields:
                value=str(record.__dict__['_data'][field])
                fieldspan=max([len(str(column.__dict__['_data'][field])) for column in records]+[len(str(field))])
                justify=" "*(fieldspan-len(value))
                print(" | "+value+justify,end="")
        print(" |")
        print(" \\"+"-"*(sum([max([len(str(column.__dict__['_data'][field])) for column in records]+[len(str(field))])+3 for field in fields])-1)+"/")


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
    mentor = ForeignKeyField(Mentor, null=True)


class Interview(BaseModel):
    applicant = ForeignKeyField(Applicant, related_name="interviews", null=True)
    interview_slot = ForeignKeyField(InterviewSlot, related_name="interviews", null=True)


class Question(BaseModel):
    question = CharField()
    status = CharField(default="NEW")
    applicant_code = ForeignKeyField(Applicant, related_name="questions", null=True )
    mentor = ForeignKeyField(Mentor, related_name="questions", null=True)
    date = DateTimeField()


class Answer(BaseModel):
    answer = CharField()
    question = ForeignKeyField(Question, related_name="answers")

