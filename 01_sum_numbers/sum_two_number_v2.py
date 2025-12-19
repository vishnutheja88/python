def get_number(prompt: str) -> float:
    """ Get a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter the valid input: ")

def add_two_number() -> None:
    """Add two numbers provided by user input"""
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second Number: ")
    result = num1 + num2
    print(f"Result: ", result)

if __name__=="__main__":
    add_two_number()