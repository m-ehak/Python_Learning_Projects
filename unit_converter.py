print("Welcome to the Unit Converter!")
print("What type of conversion do you want to perform?")
print("1. Kilometers to Miles")
print("2. Celsius to Fahrenheit")
choice = int(input("Enter your choice: "))

if choice == 1:
    km = float(input("Enter your distance in Kilometers: "))
    miles = km * 0.621371
    print(f"{km} km equals {miles} miles")
elif choice == 2:
    celsius = float(input("Enter your temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} celsius equals {fahrenheit} fahrenheit")
    
    