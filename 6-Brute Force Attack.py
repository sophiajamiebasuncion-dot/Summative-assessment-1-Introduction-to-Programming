correct_password = "12345"

while True:
    password_attempt = int(input("Enter the password: "))
    if correct_password == password_attempt:
        print("You are now granted access")
        break
    else:
        print("Wrong password, retry")
