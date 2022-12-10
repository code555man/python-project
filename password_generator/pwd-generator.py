import random
# import string

lenght = 8

re = list("0123456789abcdefghijklmnopqrstuvwxyz")

# letters = string.ascii_letters
# digits = string.digits
# symbols = string.punctuation

for i in range(10):
    pwd_gen = random.sample(re,lenght)
    print("Password Generator : ","".join(pwd_gen))

