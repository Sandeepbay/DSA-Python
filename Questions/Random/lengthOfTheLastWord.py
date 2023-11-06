# 58. Length of Last Word - Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

string = "luffy is still joyboy"

def lengthOfTheLastWord(string):
    word = string.split()
    last_word = word[-1]
    return len(last_word)


print(lengthOfTheLastWord(string))