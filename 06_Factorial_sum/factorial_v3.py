import math
 
n = int(input("Enter a number: "))
try:
    print(f"The factorial is {math.factorial(n)}")
except ValueError:
    print("Invalid Input: Please enter a non-negative integer.")