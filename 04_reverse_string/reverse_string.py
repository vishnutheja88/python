def reverse_string(num):
    return num[::-1]

original_text=input("Enter a string to reverse: ")

reverse_text = reverse_string(original_text)

print(f"Original: {original_text}")
print(f"Reversed: {reverse_text}")