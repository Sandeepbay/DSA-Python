# 125. Valid Palindrome - A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

string = "race a car"

# def isPalindrome(value):
#     cleaned_string = ""
#     for char in value:
#         if char.isalnum():
#             cleaned_string += char
#     new_string = cleaned_string.lower()
#     reverseString = ''.join(reversed(new_string))
#     if new_string == reverseString:
#         return True
#     return False

def isPalindrome(value):
        cleaned_string = ""
        for char in value:
            if char.isalnum():
                cleaned_string = char + cleaned_string
        proper_string = cleaned_string.lower()
        reverse_string = ''.join(reversed(proper_string))
        if reverse_string == proper_string:
            return True
        return False

print(isPalindrome(string))