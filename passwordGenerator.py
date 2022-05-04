import random

def generate_password(length = 8) :
    password = ""
    for _ in range(length) :
        password += chr(random.randint(32, 126))
    return password

length = int(input("Length : ") or 10)
password = generate_password(length)
