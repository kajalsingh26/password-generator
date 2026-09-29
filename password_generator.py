import random
import string

length = int(input("Enter password length: "))

if length < 4:
    print("Password length should be at least 4.")
else:
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ""

    for i in range(length):
        password = password + random.choice(characters)

    print("Generated Password:", password)