REQUIRED_LENGTH = 6


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Enter password: ")
    while len(password) < REQUIRED_LENGTH:
        print("Password too short")
        password = input("Enter password: ")
    return password


main()
