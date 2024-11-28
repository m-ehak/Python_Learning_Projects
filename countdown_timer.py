import time

start = int(input("Enter the starting time: "))
while start != 0:
    print(start, end = "\r")#needs fixing
    time.sleep(1)
    start -=1
    
print("Time's Up!")    