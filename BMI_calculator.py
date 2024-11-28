weight = float(input("Enter Your weight (in kg): "))
height = float(input("Enter Your height (in meters): "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("You are Underweight")
elif 18.5 <= bmi < 24.9:
    print("Your weight is Normal")
elif 25 <= bmi < 29.9:
    print("You are overweight")
else:
     print("You are obese")         