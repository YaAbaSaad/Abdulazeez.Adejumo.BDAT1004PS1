#!/usr/bin/env python
# coding: utf-8

# # Question 1
# 
# What data type is each of the following (evaluate where necessary)?

# # Answer
# 
# 5 - **Integer** <br>
# 5.0 - **Float** <br>
# 5 > 1 - **Boolean (True)** <br>
# '5' - **String** <br>
# 5 * 2 - **Integer** <br>
# '5' * 2 - **String ('52' - string concatenation)** <br>
# '5' + '2' - **String ('52' - string concatenation)** <br>
# 5 / 2 - **Float (division results in a float)** <br>
# 5 % 2 - **Integer (modulo operation results in an integer){5, 2, 1} - Set** <br>
# 5 == 3 - **Boolean (False)** <br>
# Pi (the number) – **Float** <br>

# # Question 2a.
# 
# How many letters are there in 'Supercalifragilisticexpialidocious'?
# 

# In[3]:


word = "Supercalifragilisticexpialidocious"
number_of_letters = len(word)
print("Number of letters is:", number_of_letters)


# # Question 2b.
# 
# Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring?
# 

# In[4]:


word= "Supercalifragilisticexpialidocious"
substring = 'ice' in word
print("The word contains 'ice' as a substring:", substring)


# # Question 2c.
# 
# Which of the following words is the longest:
# Supercalifragilisticexpialidocious, Honorificabilitudinitatibus, or
# Bababadalgharaghtakamminarronnkonn?
# 

# In[5]:


words = ['Supercalifragilisticexpialidocious', 'Honorificabilitudinitatibus',
'Bababadalgharaghtakamminarronnkonn']
longest_word = max(words, key=len)
print("Longest word:", longest_word)


# # Question 2d.
# 
# Which composer comes first in the dictionary: 'Berlioz', 'Borodin', 'Brian',
# 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'. Which one comes last?

# In[6]:


composers = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
composers.sort()
first_composer = composers[0]
last_composer = composers[-1]
print("First composer:", first_composer)
print("Last composer:", last_composer)


# # Question 3
# Implement function triangleArea(a,b,c) that takes as input the lengths of the 3
# sides of a triangle and returns the area of the triangle. By Heron's formula, the area
# of a triangle with side lengths a, b, and c is
# s(s - a)(s -b)(s -c), where
# s = (a +b + c) /2.

# In[10]:


import math

def triangleArea(a, b, c):
    # Calculate the semi-perimeter 's'
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Test the function
result = triangleArea(2, 2, 2)
print(result)


# # Question 4
# Write a program in python to separate odd and even integers in separate arrays. Go
# to the editor
# Test Data :
# Input the number of elements to be stored in the array :5
# Input 5 elements in the array :
# element - 0 : 25
# element - 1 : 47
# element - 2 : 42
# element - 3 : 56
# element - 4 : 32
# Expected Output:
# The Even elements are:
# 42 56 32
# The Odd elements are :
# 25 47

# In[12]:


# Input the number of elements
number_of_elements = int(input("Input the number of elements: "))

# Initialize empty lists for even and odd elements
even_numbers = []
odd_numbers = []

# Input elements and categorize them
for i in range(number_of_elements):
    element = int(input(f"Enter element {i + 1}: "))
    if element % 2 == 0:
        even_numbers.append(element)
    else:
        odd_numbers.append(element)

# Output the even and odd elements
print("The Even numbers are:", even_numbers)
print("The Odd numbers are:", odd_numbers)


# # Question 5a.
# Write a function inside(x,y,x1,y1,x2,y2) that returns True or False depending on whether the point (x,y) lies in the rectangle with lower left corner (x1,y1) and upper right corner (x2,y2).
# 
# inside(1,1,0,0,2,3) <br>
# True <br>
# inside(-1,-1,0,0,2,3) <br>
# False <br>

# In[45]:


def inside(x, y, x1, y1, x2, y2):
    return x1 <= x <= x2 and y1 <= y <= y2

print(inside(1, 1, 0, 0, 2, 2))  # This should return True because (1,1) is inside the rectangle defined by (0,0) and (2,2)
print(inside(-1, -1, 0, 0, 2, 3))  # This should return False


# # Question 5b.
# 
# Use function inside() from part a. to write an expression that tests whether the point (1,1) lies in both of the following rectangles: one with lower left corner (0.3, 0.5) and upper right corner (1.1, 0.7) and the other with lower left corner (0.5, 0.2) and upper right corner (1.1, 2).

# In[18]:


# Define the function to check if a point is inside a rectangle
def inside(x, y, x1, y1, x2, y2):
    return x1 <= x <= x2 and y1 <= y <= y2

# Define the coordinates of the point (1, 1)
x = 1
y = 1

# Define the coordinates of the rectangles
rectangle1 = (0.3, 0.5, 1.1, 0.7)
rectangle2 = (0.5, 0.2, 1.1, 2)

# Test if the point (1, 1) is inside both rectangles
is_inside_rectangle1 = inside(x, y, rectangle1[0], rectangle1[1], rectangle1[2], rectangle1[3])
is_inside_rectangle2 = inside(x, y, rectangle2[0], rectangle2[1], rectangle2[2], rectangle2[3])

# Check the results
if is_inside_rectangle1 and is_inside_rectangle2:
    print("The point (1, 1) lies in both rectangles.")
else:
    print("The point (1, 1) does not lie in both rectangles.")


# # Question 6
# 16. You can turn a word into pig-Latin using the following two rules (simplified):
# • If the word starts with a consonant, move that letter to the end and append 'ay'. For example, 'happy' becomes 'appyhay' and 'pencil' becomes 'encilpay'.
# • If the word starts with a vowel, simply append 'way' to the end of the word. For example, 'enter' becomes 'enterway' and 'other' becomes 'otherway' . For our purposes, there are 5 vowels: a, e, i, o, u (so we count y as a consonant).
# Write a function pig() that takes a word (i.e., a string) as input and returns its pig-Latin form. Your function should still work if the input word contains upper case characters. Your output should always be lower case however.

# In[22]:


def pig(word):
    # Convert the word to lowercase to handle uppercase characters
    word = word.lower()
    
    # Check if the word starts with a vowel
    vowels = "aeiou"
    if word[0] in vowels:
        return word + "way"
    else:
        # Find the index of the first vowel in the word
        index = 0
        for i, letter in enumerate(word):
            if letter in vowels:
                index = i
                break
        # Rearrange the word according to the rules
        pig_latin = word[index:] + word[:index] + "ay"
        return pig_latin

# Test the function
print(pig('happy'))  # Output: 'appyhay'
print(pig('Enter'))  # Output: 'enterway'


# # Question 7
# File bloodtype1.txt records blood-types of patients (A, B, AB, O or OO) at a clinic. Write a function bldcount() that reads the file with name name and reports (i.e., prints) how many patients there are in each bloodtype.

# In[32]:


# Reading the contents of the file to inspect its structure
with open("C:\\Users\\AbuSaad\\Documents\\Big Data Analytics\\BDAT1004 - Data Programming\\bloodtype1.txt", "r") as file:
    blood_data = file.read()

def bldcount(filename):
    # Open and read the file
    with open(filename, "r") as file:
        blood_types = file.read().split()  # Splitting the content based on spaces
    
    # Counting the occurrences of each blood type
    blood_counts = {
        'A': blood_types.count('A'),
        'B': blood_types.count('B'),
        'AB': blood_types.count('AB'),
        'O': blood_types.count('O'),
        'OO': blood_types.count('OO')
    }
    
    # Printing the results
    for blood_type, count in blood_counts.items():
        if count == 0:
            print(f"There are no patients of blood type {blood_type}.")
        elif count == 1:
            print(f"There is one patient of blood type {blood_type}.")
        else:
            print(f"There are {count} patients of blood type {blood_type}.")

# Call the function to get and print the blood type counts
bldcount("C:\\Users\\AbuSaad\\Documents\\Big Data Analytics\\BDAT1004 - Data Programming\\bloodtype1.txt")


# # Question 8
# Write a function curconv() that takes as input:
# 1. a currency represented using a string (e.g., 'JPY' for the Japanese Yen or 'EUR' for the Euro)
# 2. an amount
# and then converts and returns the amount in US dollars.

# In[37]:


# Reading the contents of the file to inspect its structure
with open("C:\\Users\\AbuSaad\\Documents\\Big Data Analytics\\BDAT1004 - Data Programming\\currencies.txt", "r") as file:
    currency_data = file.readlines()

def curconv(currency, amount):
    # Dictionary to store currency conversion rates
    conversion_rates = {}
    
    # Reading the file and populating the conversion_rates dictionary
    with open("C:\\Users\\AbuSaad\\Documents\\Big Data Analytics\\BDAT1004 - Data Programming\\currencies.txt", "r") as file:
        for line in file:
            data = line.split("\t")
            conversion_rates[data[0]] = float(data[1])
    
    # Convert the amount using the appropriate conversion rate
    if currency in conversion_rates:
        return amount * conversion_rates[currency]
    else:
        raise ValueError(f"Unknown currency code: {currency}")

# Testing the function
test_results = {
    'EUR': curconv('EUR', 100),
    'JPY': curconv('JPY', 100)
}
print(test_results)



# # Question 9
# Each of the following will cause an exception (an error). Identify what type of exception each will cause.

# # Answer
# 1. Trying to add incompatible variables, as in adding 6 + 'a':
# **Type Error:** This will result in a TypeError because you cannot perform addition between
# an integer and a string.
# 2. Referring to the 12th item of a list that has only 10 items:
# **IndexError:** This will result in an IndexError because you are trying to access an index
# that is out of the range of the list.
# 3. Using a value that is out of range for a function's input, such as calling math.sqrt(1.0):
# **ValueError** (for math.sqrt): This will result in a ValueError because the math.sqrt
# function does not accept negative numbers as input. It expects a non-negative number.
# 4. Using an undeclared variable, such as print(x) when x has not been defined:
# **NameError:** This will result in a NameError because the variable 'x' has not been
# declared or defined before it is used.
# 5. Trying to open a file that does not exist, such as mistyping the file name or looking in the wrong
# directory:
# **FileNotFoundError:** This will result in a FileNotFoundError if the specified file does not
# exist in the specified location or if there is a typo in the file name.

# # Question 10
# Encryption is the process of hiding the meaning of a text by substituting letters in the message with other letters, according to some system. If the process is successful, no one but the intended recipient can understand the encrypted message. Cryptanalysis refers to attempts to undo the encryption, even if some details of the encryption are unknown (for example, if an encrypted message has been intercepted). The first step of cryptanalysis is often to build up a table of letter frequencies in the encrypted text. Assume that the string letters is already defined as 'abcdefghijklmnopqrstuvwxyz'. Write a function called frequencies() that takes a string as its only parameter, and returns a list of integers, showing the number of times each character appears in the text. Your function may ignore any characters that are not in letters.

# In[40]:


def frequencies(text):
    # Define the valid letters
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    # Initialize a list to store the frequency of each letter
    letter_frequencies = [0] * 26

    # Convert the input text to lowercase for case-insensitive counting
    text = text.lower()

    # Iterate through each character in the input text
    for char in text:
        if char in letters:
            # Increment the corresponding frequency count
            index = letters.index(char)
            letter_frequencies[index] += 1

    return letter_frequencies

# Test the function with example inputs
print(frequencies('The quick red fox got bored and went home.'))
# Expected Output: [1, 1, 1, 3, 5, 1, 1, 2, 1, 0, 1, 0, 1, 2, 4, 0, 1, 2, 0, 2, 1, 0, 1, 1, 0, 0]
print(frequencies('apple'))
# Expected Output: [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

