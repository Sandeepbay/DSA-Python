# 9. Palindrome Number - Given an integer x, return true if x is a palindrome, and false otherwise.


x = 121


def isPalindrome(value):
    value1 = str(value)
    reverseNumber = ''.join(reversed(value1))
    if value == reverseNumber:
        return True
    return False


print(isPalindrome(x))