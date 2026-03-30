name = input("What is your full name? ")
hometown = input("What is your hometown? ")
age = input("What is your age? ")

biography = {
    "insert name": name,
    "insert hometown": hometown,
    "insert age": age
}

print(biography["insert name"], biography["insert hometown"], biography["insert age"], sep="\n")