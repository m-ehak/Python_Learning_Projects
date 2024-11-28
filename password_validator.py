password = input("Enter your password: ")

if len(password) < 8:
    print("Password must be atleast 8 characters long.")
elif not any(char.isalpha() for char in password): #know more about his line
    print("Password must contain atleast 1 letter.")
elif not any(char.isdigit() for char in password):
    print("Password must contain atleast 1 digit.")
else:
    print("Password is valid.")