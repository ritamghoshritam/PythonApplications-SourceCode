import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321<>?/.,+_=-!@#$%^&*(){}[]'

length = input('password length')
length = int(length)
for p in range(3):
    password = ' '
    for c in range(length):
        password += random.choice(chars)
    print(password)
