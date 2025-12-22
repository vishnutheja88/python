def factorial_number(n):
    if n == 0  or n == 1:
        return 1
    else:
        return n*factorial_number(n-1)
    
number=int(input("Enter a number: "))
if(number<0):
    print("Factorial not defined for negative numbers. ")
else:
    print(f"Factorial is {factorial_number(number)}")