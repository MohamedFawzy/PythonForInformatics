# Suppose you are given a string and you want to count how many times each letter appears
def histogram(string):
    my_dictionary = dict()
    for character in string:
        if character not in my_dictionary:
            my_dictionary[character] = 1
        else:
            my_dictionary[character] += 1
    return my_dictionary
user_string = raw_input("Enter your string: ")
print histogram(user_string)
