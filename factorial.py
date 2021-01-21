import math
import time
num = int(input("Enter the number \n"))

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial*i

    b = 1
    for b in range(0, 100):
        b = b+1
        while not(math.floor(num/(5**b) == 0)):
            zero = (math.floor(num / (5 ** b)))
            zero = zero+(math.floor(num / (5 ** b)))
            print(
                f"pls wait,printing no. of zeroes at the end of {num} factorial ")
            time.sleep(2)
            d = math.floor(zero/2)

            print(d)
            print("Done!,you can now exit the program")
            time.sleep(10000)
