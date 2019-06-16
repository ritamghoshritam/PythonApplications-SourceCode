correct_password = "python123"
firstname = input("Enter Your First Name")
lastname = input("Enter Your Last Name")
password = input("Enter password: ")

while correct_password != password:
    password = input("Wrong password! Enter again: ")

message = "Hi %s %s, you are logged in" % (firstname,lastname)
print(message)
