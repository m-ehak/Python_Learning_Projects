import random
import string


char = string.ascii_letters
char += string.digits
char += string.punctuation

length = int(input("Enter the length of your password: "))
password = ""

for i in range(length):
   password += random.choice(char)
   
print("Your random password is: " , password)   