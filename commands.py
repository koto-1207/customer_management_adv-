from utils import get_valid_name, get_valid_age
from config import get_all_users, create_user, find_user_by_name, delete_user


# S 全てのユーザーの情報を出力
def show_all():
    for user in get_all_users():
        print(f"Name: {user.name} Age: {user.age}")


# A 新しい ユーザーを加える
def add_user():
    name = get_valid_name()
    age = get_valid_age()
    if find_user_by_name(name):
        print(f"Duplicated user name {name}")
    else:
        create_user(name, age)
        print(f"Add new user: {name}")


# F ユーザー検索機能
def find_user():
    name = input("User name > ")
    user = find_user_by_name(name)

    if user:
        print(f"Name: {user.name} Age: {user.age}")

    else:
        print(f"Sorry, {name} is not found")


# D 削除機能
def delete_user_cmd():
    name = input("User name >")
    if delete_user(name):
        print(f"User {name} is deleted")
    else:
        print(f"Sorry, {name} is not found")


# E 編集機能
def edit_user_info():
    name = input("User name > ")
    user = find_user_by_name(name)
    if user:
        print()
        update_name = get_valid_name(current_name=user.name)
        update_age = get_valid_age(current_age=user.age)
        user.name = update_name
        user.age = update_age
        user.save()
        print(f"Update user: {user.name}")

    else:
        print(f"Sorry, {name} is not found")
