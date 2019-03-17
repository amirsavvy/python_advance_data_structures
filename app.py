"""
List / List Comprehension

List comprehension is an elegant way to define and create lists based on existing lists

List comprehensions are used for creating new list from another iterables

Common applications are to make new lists where each element is the result of some operations
applied to each member of another sequence or iterable, or to create a subsequence of those
elements that satisfy a certain condition

Example 1

"""

# You can either use loops:
squares = []

for x in range(10):
    squares.append(x ** 2)

print(squares)
print('***************')
# Or you can use list comprehensions to get the same result:
squares = [x ** 2 for x in range(10)]

print(squares)

print('***************')

"""
Multiply every part of a list by three and assign it to a new list.
"""

list1 = [3, 4, 5]

multiplied = [item * 3 for item in list1]

print(multiplied)

"""
take the first letter of each word and make a list out of it
"""

listOfWords = ["this", "is", "a", "list", "of", "words"]

items = [word[0] for word in listOfWords]

print(items)

"""
convert lower case / upper case letters
"""

lower = [x.lower() for x in ["A", "B", "C"]]
print(lower)
upper = [x.upper() for x in ["a", "b", "c"]]
print(upper)

"""
extract all the numbers from a string
"""

string = "Hello 12345 World"
numbers = [x for x in string if x.isdigit()]
print(string)
print(numbers)

"""
et specific lines out from a text file
"""

# Then create the filter by using list comprehension:

fh = open("test.txt", "r")

result = [i for i in fh if "line3" in i]

print(result)

"""
use list comprehension in functions
"""

# Create a function and name it double:


def double(x):
    return x*2

# If you now just print that function with a value in it, it should look like this:


print(double(10))

double_list = [double(x) for x in range(10)]
print(double_list)

double_list1 = [double(x) for x in range(10) if x % 2 == 0]
print(double_list1)

double_list2 = [x+y for x in [10, 30, 50] for y in [20, 40, 60]]
print(double_list2)

"""
separate the letters of the word human and add the letters as items of a list

"""


h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)

h_letters = [ letter + 'amir' for letter in 'human' ]
print( h_letters)

"""
Conditionals in List Comprehension
"""

number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

"""
if...else With List Comprehension
"""
obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(obj)

"""
Find common numbers from two list using list comprehension

"""

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common_num = [a for a in list_a for b in list_b if a == b]

print(common_num)

"""
Return numbers from the list which are not equal as tuple

"""

list_a = [1, 2, 3]
list_b = [2, 7]

different_num = [(a, b) for a in list_a for b in list_b if a != b]

print(different_num) # Output: [(1, 2), (1, 7), (2, 7), (3, 2), (3, 7)]

"""
List comprehensions can also be used to iterate over strings
"""

list_a = ["Hello", "World", "In", "Python"]

small_list_a = [str.lower() for str in list_a]

print(small_list_a) # Output: ['hello', 'world', 'in', 'python']

"""
list comprehensions can be used to produce list of list
"""

list_a = [1, 2, 3]

square_cube_list = [ [a**2, a**3] for a in list_a]

print(square_cube_list) # Output: [[1, 1], [4, 8], [9, 27]]

















