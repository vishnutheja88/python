def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid input: ")

def is_even(number: int) -> bool:
    """Check if a number is even"""
    return number % 2 == 0

def check_even_odd() -> None:
    """Check if the user input is Even or Odd value. """
    num = get_integer("Enter a Number: ")
    result = "Even" if is_even(num) else "Odd"
    print(f"The number {num} is: {result}")

if __name__ == "__name__":
    check_even_odd()

