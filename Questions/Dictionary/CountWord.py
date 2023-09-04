#Count Word Frequency - Define a function to count the frequency of words in a given list of words.

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple' , 'apple'] 

def count_word_frequency(words):
    my_dict = {}
    for i in words:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] = my_dict[i] + 1
    print(my_dict)
count_word_frequency(words)