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
