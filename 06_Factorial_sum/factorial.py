def factorial_number(n):
    if n<0:
        return "Error: Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

num = int(input("Enter a number: "))
print(f"The factorial of a {num} is {factorial_number(num)}")