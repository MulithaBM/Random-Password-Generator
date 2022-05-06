import random
import bcrypt

salt = bcrypt.gensalt()

def generate_password(length) :
    password = ""
    for _ in range(length) :
        password += chr(random.randint(32, 126))
    return password

def hash_password(password) :
    # convert string into corresponding array of bytes before hashing
    b_password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(b_password, salt)
    return hashed_password

def verify_password(password, hashed_password) :
    b_password = password.encode('utf-8')
    return bcrypt.checkpw(b_password, hashed_password)

length = int(input("Length : ") or 10)

password = generate_password(length)
hashed_password = hash_password(password)

# verify passwords
verification = bcrypt.checkpw(password, hashed_password)
