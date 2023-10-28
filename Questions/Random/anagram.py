# 242. Valid Anagram - Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

string1 = "rat"
string2 = "car"
def isAnagram(firstWord , secondWord):
    sortedFirstWord = ''.join(sorted(firstWord))
    sortedSecondWord = ''.join(sorted(secondWord))
    if (sortedFirstWord == sortedSecondWord):
        return True
    return False

print(isAnagram(string1 , string2))