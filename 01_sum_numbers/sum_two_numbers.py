def getNumber(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
def add_number():
    a=getNumber("enter first number: ")
    b=getNumber("enter second number: ")
    return a+b

if __name__ == "__main__":
    result=add_number()
    print(f"Sum", result)