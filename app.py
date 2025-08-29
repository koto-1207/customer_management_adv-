from config import init_db
from commands import show_all, add_user, find_user, delete_user_cmd, edit_user_info
from utils import show_menu


def main():
    init_db()
    show_menu()
    while True:
        print()
        command = input("Your command > ").strip().upper()

        if command == "Q":
            print("Bye!")
            break

        elif command == "S":
            show_all()

        elif command == "A":
            add_user()

        elif command == "F":
            find_user()

        elif command == "D":
            delete_user_cmd()

        elif command == "E":
            edit_user_info()

        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
