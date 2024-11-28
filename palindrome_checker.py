p = input("Enter your text: ")

p = p.replace(" ", "").lower()

if p == p[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
