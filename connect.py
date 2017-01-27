from peewee import PostgresqlDatabase


def create_database():
    with open("connection.txt", "r") as f:
        data_lines = f.readlines()
        db_name = data_lines[0].replace("\n", "").split(":", 1)[1]
        username = data_lines[1].replace("\n", "").split(":", 1)[1]
        return PostgresqlDatabase(db_name, user=username)
