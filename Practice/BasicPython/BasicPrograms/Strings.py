"""
NCERT Problems.
"""

'''
1. Write a program to input line(s) of text from the user until enter is pressed. Count the
total number of characters in the text (including white spaces),total number of alphabets,
total number of digits, total number of special symbols and total number of words in the
given text. (Assume that each word is separated by one space).
'''

'''
# We can define various functions for this task, but it will increase the time complexity of the program.
# Preferring to write without any function.

# Number of:
Characters = 0
Words = 0
Digits = 0
Letters = 0
SpecialCharacters = 0

print("Enter your string:")
InputString = input()

# For number of words:
PrevCharacter = InputString[0]
if not PrevCharacter.isspace():
    Words += 1

for Character in InputString:
    Characters += 1
    if Character.isalpha():
        Letters += 1
    elif Character.isdigit():
        Digits += 1
    elif not Character.isspace():
        SpecialCharacters += 1

    if PrevCharacter.isspace() and (not Character.isspace()):
        Words += 1
    PrevCharacter = Character

print("")
print("Number of characters =", Characters)
print("Number of")
print("\tLetters =", Letters)
print("\tDigits =", Digits)
print("\tSpecial Characters =", SpecialCharacters)
print("Number of words =", Words)
'''

# --------------------------------------------------------------------------------------------

'''
2. Write a user defined function to convert a string with more than one word into title
case string where string is passed as parameter. (Title case means that the first letter
of each word is capitalised)
'''

'''
def to_title_case(input_string):
    new_string = ""

    prev_char = input_string[0]
    if not prev_char.isspace():
        new_string += prev_char.upper()
    else:
        new_string += prev_char
    for char in input_string[1:]:
        if prev_char.isspace() and (not char.isspace()):
            new_string += char.upper()
        else:
            new_string += char
        prev_char = char

    return new_string


String = input()
print(to_title_case(String))
'''

# --------------------------------------------------------------------------------------------

'''
3. Write a function delete_char() which takes two parameters: one is a string and other is
a character. The function should create a new string after deleting all occurrences of the
character from the string and return the new string.
'''

'''
# Assuming that only one character will be given.
# If more than one character is given, will consider only the first character of the given string.
def delete_char(input_string, character):
    new_string = ""

    for char in input_string:
        if char == character[0]:
            continue
        new_string += char

    return new_string


String = input()
Char = input("Enter the character to be deleted: ")
print(delete_char(String, Char))
'''

# --------------------------------------------------------------------------------------------

'''
4. Input a string having some digits. Write a function to return the sum of digits present in
this string.
'''

'''
def digit_sum(input_string):
    string_digits_sum = 0

    for char in input_string:
        if char.isdigit():
            string_digits_sum += int(char)

    return string_digits_sum


String = input()
print(digit_sum(String))
'''

# --------------------------------------------------------------------------------------------

'''
5. Write a function that takes a sentence as an input parameter where each word in the sentence
is separated by a space. The function should replace each blank with a hyphen and then return
the modified sentence.
'''

'''
# Assuming proper input.
def replace_space_with_hyphen(input_string):
    new_string = ""
    for char in input_string:
        if char.isspace():
            new_string += '-'
        else:
            new_string += char

    return new_string


String = input()
print(replace_space_with_hyphen(String))
'''
