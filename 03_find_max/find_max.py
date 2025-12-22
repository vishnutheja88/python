def find_maximum(number_list):
    if not number_list:
        return None
    return max(number_list)

try: 
    total_number = int(input("How many numbers would you like to enter: "))

    numbers=[]
    for i in range(total_number):
        val = float(input(f"Enter number {i+1}: "))
        numbers.append(val)
    result = find_maximum(numbers)


    if result is not None:
        print(f"The maximum number is: {result}")
    else:
        print(f"The numbers were entered.")
    
except ValueError:
    print("Invalid input. Please enter numberic value..")