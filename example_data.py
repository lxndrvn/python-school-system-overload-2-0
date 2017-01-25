# This script can generate example data for "City" and "InterviewSlot" models.

from models import *
School.create(location="Budapest")
bpschool=School.select().where(School.location="Budapest")
School.create(location="Miskolc")
misischool=School.select().where(School.location="Miskolc")
School.create(location="Krakow")
krakowschool=School.select().where(School.location="Krakow")

cities=[{"name"="Budapest","school"="bpschool"},
        {"name"="Esztergom","school"="bpschool"},
        {"name"="Miskolc","school"="misischool"},
        {"name"="Eger","school"="misischool"},
        {"name"="Krakow","school"="krakowschool"},
        {"name"="Warsaw","school"="krakowschool"}]

for city in cities:
    City.create(city["name"],city["school"])
