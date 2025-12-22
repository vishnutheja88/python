def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even."
    else:
        return f"{num} is Odd."
user_input = int(input("Enter a number: "))

result = check_even_odd(user_input)

print(result)