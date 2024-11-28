operator = input("Choose an Operator (+ , - , * , /): ")

a = float(input("Enter Your First Number: "))
b = float(input("Enter Your Second Number: "))

if (operator == "+"):
    print(round((a + b) , 3))   
elif (operator == "-"):
    print(round((a - b) , 3))
elif (operator == "*"):
    print(round((a * b) , 3))      
elif (operator == "/"):
    print(round((a / b) , 3))     
else:
    print("Invalid Operator")