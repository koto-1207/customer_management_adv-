from utils import get_valid_name, get_valid_age
from config import users, User


# S 全てのユーザーの情報を出力
def show_all():
    for user in users:
        print(f"Name: {user.name} Age: {user.age}")


# A 新しい ユーザーを加える
def add_user():
    name = get_valid_name()
    age = get_valid_age()
    if any(user.name == name for user in users):
        print(f"Duplicated user name {name}")
    else:
        users.append(User(name, age))
        print(f"Add new user: {name}")


# F ユーザー検索機能
def find_user():
    find_user = input("User name > ")
    found = False
    for user in users:
        if user.name == find_user:
            print(f"Name: {user.name} Age: {user.age}")
            found = True
            break
    if not found:
        print(f"Sorry, {find_user} is not found")


# D 削除機能
def delete_user_cmd():
    del_user = input("User name >")
    user_to_delete = next((u for u in users if u.name == del_user), None)
    if user_to_delete:
        users.remove(user_to_delete)
        print(f"User {del_user} is deleted")
    else:
        print(f"Sorry, {del_user} is not found")


# E 編集機能 途中！
def edit_user_info():
    edit_user = input("User name > ")
    user_to_edit = next((u for u in users if u.name == edit_user), None)
    if user_to_edit:
        update_name = get_valid_name(current_name=user_to_edit.name)
        update_age = get_valid_age(current_age=user_to_edit.age)
        user_to_edit.name = update_name
        user_to_edit.age = update_age
        print(f"Update user: {user_to_edit.name}")

    else:
        print(f"Sorry, {edit_user} is not found")
