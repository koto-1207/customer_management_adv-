import os
from dotenv import load_dotenv
from playhouse.db_url import connect
from peewee import Model, IntegerField, CharField

load_dotenv(override=True)
DATABASE_URL = os.getenv("DATABASE_URL")
db = connect(DATABASE_URL)


class User(Model):
    name = CharField(unique=True, max_length=20)
    age = IntegerField()

    class Meta:
        database = db
        table_name = "users"


def init_db():
    db.connect()
    db.create_tables([User], safe=True)


def get_all_users():
    return list(User.select)


def add_user(name, age):
    return User.create(name=name, age=age)


def find_user_by_name(name):
    return User.get_or_none(User.name == name)


def delete_user(name):
    user = find_user_by_name(name)
    if user:
        user.delete_instance()
        return True
    return False


users = [User("Bob", 15), User("Tom", 57), User("Ken", 73)]
