required_length = 6
password = input("Enter password: ")
while len(password) < 6:
    print("Password too short")
    password = input("Enter password: ")

print("*" * len(password))

