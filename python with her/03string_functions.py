# Strings
# The string is a data type in Python.

# A string is a sequence of characters enclosed in quotes.

# We can primarily write a string in three ways, as we discussed yesterday:

# Single quoted strings : a = ‘wolf’
# Double quoted strings : b = “second wolf”
# Triple quoted strings : c = ‘’’ i am the third wolf ‘’’
# String Slicing:
# A string in Python can be sliced for getting a part of the string.

# Consider the following string:

name = "wolfie"
# indexing in python
# the above string has 6 alphabets, and indexing start with zero(0,1,2,3,4,5)
# w being the first element is on index zero, o at 1 and so on to the lengt
#  of the string-1
# so the index in a string starts from 0 to (length-1) in Python.
# negative indicing
# here in the above string a length is , so first elementis at index -6
#  and last on -1 
# Negative Indices: -1 corresponds to the (length-1) index.
# To slice a string, we use the following syntax:
a = "Aaina_Sharma"
print(a[1])
print(a[5])
print(len(a))
print(a[0:5])
print(a[0:144])
print(a[-12])
print(a[-1:-14:-1])




# Slicing with skip value

# We can provide a skip value as a part of our slice like this:

word = "amazing"

print(word[1:6:2])          # It will return ’mzn’

 
# Other advanced slicing techniques

word = "amazing"

print(word[:7])
# or 
print(word[0:7])     #It will return ‘amazing’

print(word[0:]) 
# or 
print(word[0:7])     #It will return ‘amazing’

# String Functions
# Some of the most used functions to perform operations on or manipulate 
# strings are:

# len() function : It returns the length of the string.
x = "wolfiewolfiewolfie"
print(len(x))             #Returns 18


#  endswith(“fie”) : 
''' This function tells whether the variable string ends
  with the string “fie” or not. If string is “wolfie”, it returns true for 
  “fie” since wolfie ends with fie.'''

print(x.endswith("fie"))   #  returns True

#   count()
'''count("c") : It counts the total number of occurrences of any character.'''
print(x.count("wolfiie")) # returns number of "i" in x

# capitalize() : This function capitalizes the first character of a given 
# string.
# print(x.capitalize)

''' find(word) : This function finds a word and returns the index of first 
occurrence of that word in the string.'''
print(x.find("w"))

''' replace(oldword, newword) : This function replaces the old word with the
 new word in the entire string.'''
x = x.replace("wol", "dol")
print(x)
# Escape Sequence Characters:
# Sequence of characters after backslash ‘\’ [Escape Sequence Characters]

''' Escape Sequence Characters comprises of more than one character but
 represents one character when used within the string.'''

# Examples: \n (new line), \t (tab), \’ (single quote), \\ (backslash), etc.
print("aaai\\naa")