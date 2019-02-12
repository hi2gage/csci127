import random
import string
def password(num):
    pass_string = ""
    for i in range(int(num)):
        pass_string = pass_string + random.choice(string.ascii_letters)
    return pass_string

print(password(25))
