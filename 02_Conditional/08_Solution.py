password = input('Enter a password:')
count = len(password)

if count < 6:
    print("Weak Password")
elif count <= 10:
    print("Medium Password")
else:
    print("Strong Password")