from db_tool import users, User
import commands


def show_menu():
    with open("menu.txt", "r") as f:
        menu = f.read()
        print(menu)


def main():
    show_menu()
    while True:
        print()
        command = input("Your command > ").strip().upper()

        if command == "Q":
            print("Bye!")
            break

        elif command == "S":
            commands.show_all()

        elif command == "A":
            commands.add_user()

        elif command == "F":
            commands.find_user()

        elif command == "D":
            commands.delete_user_cmd()

        elif command == "E":
            commands.edit_user_info()

        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
