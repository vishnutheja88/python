def check_palindrome(s):
    s = s.lower().replace(" ","")
    left, right=0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
user_string=input("Enter a word or a string: ")

if check_palindrome(user_string):
    print(f" '{user_string}' is a Palindrome. ")
else:
    print(f" '{user_string}' is NOT a Palindrome.")