class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


users = [User("Bob", 15), User("Tom", 57), User("Ken", 73)]


def show_menu():
    with open("menu.txt", "r") as f:
        menu = f.read()
        print(menu)


def get_valid_name(current_name=None):
    while True:
        prompt = f"New user name ({current_name}) > " if current_name else "New user name > "
        name = input(prompt).strip()

        if not name:
            print("Useer name can't be blank")
            continue
        if len(name) > 20:
            print("User name is too long(maximun is 20 characters)")
            continue

        return name


def get_valid_age(current_age=None):
    while True:
        prompt = f"New user age ({current_age}) > " if current_age is not None else "New user age > "
        age_input = input(prompt).strip()

        if not age_input:
            print("age can't be blank")
            continue

        try:
            age = int(age_input)

        except ValueError:
            print("Age is not positive integer")
            continue

        if age < 0 or age > 120:
            print("Age is grater than 120")
            continue

        return age


def main():
    show_menu()
    while True:
        print()
        command = input("Your command > ").strip().upper()

        # Q Byeを表示
        if command == "Q":
            print("Bye!")
            break

        # S 全てのユーザーの情報を出力
        elif command == "S":
            for user in users:
                print(f"Name: {user.name} Age: {user.age}")

        # A 新しい ユーザーを加える
        elif command == "A":
            name = get_valid_name()
            age = get_valid_age()

            if any(user.name == name for user in users):
                print(f"Duplicated user name {name}")

            else:
                users.append(User(name, age))
                print(f"Add new user: {name}")

        # F ユーザー検索機能
        elif command == "F":
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
        elif command == "D":
            del_user = input("User name >")
            found = False
            for i, user in enumerate(users):
                if user.name == del_user:
                    del users[i]
                    print(f"User {del_user} is deleted")
                    found = True
                    break

            if not found:
                print(f"Sorry, {del_user} is not found")

        # E 編集機能 途中！
        elif command == "E":
            edit_user = input("User name > ")
            found = False

            for user in users:
                if user.name == edit_user:
                    found = True
                    print()

                    update_name = get_valid_name(current_name=user.name)
                    update_age = get_valid_age(current_age=user.age)

                    user.name = update_name
                    user.age = update_age
                    print(f"Update user: {user.name}")
                    break

            if not found:
                print(f"Sorry, {edit_user} is not found")

        # 他のコマンドではみつからないと設定
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
