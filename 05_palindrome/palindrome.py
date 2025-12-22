def is_palindrome(text):
    clean_text=text.replace(" ","").lower()

    return clean_text == clean_text[::-1]

user_string=input("Enter the word or a phase: ")
if is_palindrome(user_string):
    print(f"'{user_string}' is a Palindrome.")
else:
    print(f" '{user_string}' is NOT a Palindrome.")