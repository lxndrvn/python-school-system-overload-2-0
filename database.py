from peewee import *


class Database:
    def read_name():
        try:
            return open('database.txt', "r").readline().strip()
        except:
            print(
                "You need to create a database and store its name in a file named 'database.txt'. For more info, head over to the README")
    database = PostgresqlDatabase(read_name())
