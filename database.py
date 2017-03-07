from peewee import PostgresqlDatabase

def database():
    try:
        credentials = open("database.txt", "r").readlines()
    except:
        print("Provide your database and user name in 'database.txt', colon-separated.")
    database = credentials[0].replace("\n", "").split(":", 1)[1]
    username = credentials[1].replace("\n", "").split(":", 1)[1]
    return PostgresqlDatabase(database, user=username)