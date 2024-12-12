def even_or_odd(number):
    if (number % 2) == 0:
        return ('Even')
    else:
        return ('Odd')
    return even_or_odd
# EVEN OR ODD NUMBER CHECKER ^^^


def number_to_string(num):
    str_num = str(num)
    return (str_num)
#Convert Interger into String 


def get_count(sentence):
    vowel = ['a','e','i','o','u']
    vow_count = 0
    for letter in sentence:
        if letter in vowel:
            vow_count += 1
    return vow_count
#Vowel Count Assignment 


