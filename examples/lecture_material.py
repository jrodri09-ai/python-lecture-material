# print("hello world")
# ex_var = 5

# ex_var = 7

# int_1 = 10

# float_1 = 2.5

# bool_1 = True

# int_1 = 9


# print (int_1)

# print (float_1)

# var_sum = 5 + 10

# print(var_sum)

# var_diff = 10 - 5

# print(var_diff)

# var_div = 4 / 2

# print(var_div)

# var_pro = 2 * 4

# print(var_pro)

# var_raised = 3 ** 8

# print(var_raised)

# var_floor_div = 10 // 3

# print(var_floor_div)

# var_modulo = 17 % 15

# print(var_modulo)

# name = "Jessica"

# print(name)

# print("Hello Jessica")

# print((2*4)+5)

ex2 = (123 + 280) / 100

# print(ex2)

ex3 = 1.23 + 2.80
# print(round(ex3, 2))

# subtotal of shopping list

pasta = 16.68

sauce = 6.98

cloves = 16.68

seasoning = 15.26

baguettes = 3.00

meatballs = 4.39

subtotal = round((pasta + sauce + cloves + seasoning + baguettes + meatballs),2)

# print(subtotal)

string1 = 'welcome user'

# print(string1)

ex_string2 = "orange"
# print(ex_string2[2])

ex_string3 = "apple"
# print(ex_string3[3])
# print(ex_string3[:3])

ex_string4 = "apricots"

# print(ex_string4[:3])
# print(ex_string4[2:5])
# print(ex_string4[4:])

concatenated = "R2" + "-" + "D2"

# print(concatenated)
# print(concatenated[1])
# print(concatenated[0:2])

myName = "Jessica" + "Grace" + "Rodriquez"

# print(myName)

nike = "Just do it!"

# print(nike[10])
# print(nike[5:8])
# print(nike[8:11])
# print(nike[0:4])

# print("Don't " + nike[5:])

ex_1 = str(True)
ex_2 = str(29)
ex_3 = str(3.2789)

# print(type(ex_1))
# print(type(ex_2))
# print(type(ex_3))

# print("Hello\tfrom\tthe\tother\tside.")
# print("line one\nline two")
# print("\"Love is all you need.\"")

ex_4 = str(6.2389)

# print(type(ex_4))
# print(ex_4 + " is a float")
# print("\"Hello, I'm Jessica, its nice to meet you!\"")

youAreAStar = "*******\n ***** \n ***\n *"

# print(youAreAStar)


# name = input("What is your name?")
# print("Your name is " + name + ".")
# print(type(name))

# quest = input("What is your quest?")
# print("Your quest is " + quest + ".")
# print(type(quest))

# color = input("What is your favorite color?")
# print("Your favorite color is " + color + ".")
# print(type(color))

# print("So your name is " + name + "," "your quest is" + quest + "," "and your favorite color is " + color + ".")

#user_int = int(input("Please enter an integer."))
#print(user_int)
#print(type(user_int))

#user_float = float(input("Please enter a float."))
#print(user_float)
#print(type(user_float))

#user_int = int(input("Please enter a number to be added to ten"))
#print(user_int)
#print(type(user_int))

#print(user_int + 10)

#def function_name(parameter):
    #print(parameter+2)


#passing an argument
#function_name(8)

#def sentence(p1="EJ",p2="is",p3="my",p4="best",p5="friend"):
    #print(p1+p2+p3+p4+p5)


#sentence()

#def hello_world_printer():
    #print("Hello World")


#hello_world_printer()

#def name_printer(parameter):
    #print(parameter)


#name = input("Please enter your name")
#name_printer(name)

#length = int(input("enter length"))
#print(length)

#width = int(input("please enter width"))
#print(width)

#height = int(input("please enter height"))
#print(height)


#def calculate_volume_rectangular_prism(l, w, h):
    #return l * w * h


#print("The volume of the rectangular prism is" + str(calculate_volume_rectangular_prism(length, width, height)) + "cubic feet.")

# this is a generic import
import random

# print(random.randint(1,10))


# function import is when a specific function is imported from a module
from random import randint

# print(randint(10, 20))

# universal import: when you import every function from a module so that whenever you call any function from that module
# you do not need to type that modules name and a period

from random import *

# print(random())

# in python you can have a variable within a function that has the same name as a variable outside of that function. However
# despite having the same name those variables are not the same variable

example = "hello world" # global

def loc_ex():
    example = "this is a string" # local
    return example


# print(example)
# print(loc_ex())

# Understanding variable scope
# Local variables cannot be used by code in the global scope.
# Global variables can be accessed by code in a local scope.
# The local scope of one function can't use variables from another function's local scope.
# You can use the same name for different variables as long as they are in different scopes.


# Examples
# Local variables cannot be used by code in the global scope.

#def loc_ex():
    #breakfast = "waffles"
    #return breakfast

#loc_ex()
#print(breakfast)
# this cannot be printed because it is outside the local scope of the variable (global)



# Global variables can be accessed by code in the local scope.


#def print_glob():
    #loc_var = " that is very long "
    #print(glob_var + loc_var)


#glob_var = "This is a string"
#print_glob()

# The local scope of one function can't use variables
# from another function's local scope


#def first():
    #loc = 2
    #return loc


#def second():
    #return loc


#first()
#second()

# You can use the same name for different variables as long as they are in different scopes.


def loc_ex1():
    fruit = "pear"
    # print(fruit)


# def loc_ex2():
    # fruit = "bananas"
    # print(fruit)


# fruit = "apple"
# loc_ex1()
# loc_ex2()
# print(fruit)

# If you wanted to assign a global variable a new value from within a function you could do so using global statements

def loc_ex():
    global fruit
    fruit = "pear"
    # print(fruit)


fruit = 'apple'
loc_ex()
# print(fruit)


# having scope's compartmentalizes problems and helps to quickly give you a better idea of where a problem involving a
# variable is happening within your code
# Because of the way local scopes are created and destroyed in functions programmers don't need to worry about code
# within each individual local scope affecting things outside of it, weather that is code in the global scope or another
# function's local scope provided

# comparison operators
# >
# <
# >=
# <=
# !=
# ==

# print(4 > 3)   # greater than
# print(1 > 3)
# print(4 < 6)   # less than
# print(3 < 3)
# print(9 >= 9)  # greater than or equal to
# print(1 <= 2)  # less than or equal to
# print(10 != 100)  # not equal to, this can also be used to compare strings
# print(10 != 10)
# print(10 == 100)
# print(10 == 10)  # is equal to, this can also be used to compare strings

# floats and integers can be equivalent
# print(4.0 >= 4)
# print(4.0 <= 4)
# print(4.0 == 4)

# boolean operators
# and
# or
# not

# and
# print(4 > 1 and "word" == "word")  # True and True
# print(8.76 == 8.7600 and 2 != 2)   # True and False
# print("earth" == "Earth" and 6 <= 3)    # False and False
# print(10 == 5 and 10 != 5) # False and True

# or : the or boolean operator only returns false if what is to the left of it and what is to the right of it, both
# evaluate to false in any other case (if there is one true the whole thing is true)

# print(4 > 1 or "word" == "word")       # True or True
# print(8.76 == 8.7600 or 2 != 2)        # True or False
# print("earth" == "Earth" or 6 <= 3)    # False or False
# print(10 == 5 or 10 != 5)              # False or True

# print(not 6482 > 0)                    # not True
# print(not "Python" != "Python")        # not False

# if statement syntax
# if True:
#    "Do the stuff here" (indent four spaces)

# veg = input("Type the name of the vegetable.")

# if veg == "corn":
    # print("The vegetable is corn.")
# else:
    # print("The vegetable is not corn.")

# else statements : when used after if statements and other flow control statements, else statements allow programmers
# to give their programs code that will be executed if no other flow control statements have had their conditions
# evaluate to true

# if False:
#    "Do the stuff here"
# else:
#    "Do this instead"

# nested if and else statements : putting if and else statements within other if and else statements
# if you want to nest statements within other statements you need to make sure that they are indented four spaces for
# to tell Python that they are statements that are meant to be nested within other statements
# the code within these nested else statements must be indented another four spaces

# gpa = float(input("What was the applicants grade point average?"))
# inst_app = input("Is the student going to be educated at an approved institution?")

# if gpa >= 3.7:
    # if inst_app == "yes":
        # print("The applicant qualifies fot a for a low APR student loan.")
    # else:
        # print("The applicant does not qualify since they have not been accepted into an approved institution.")
# else:
    # print("The applicant did not have high enough grades to qualify.")


# elif statements
#user_num = int(input("Please enter an integer."))

#if user_num < 0:
    #print("The number you entered is less than O.")
#elif user_num == 0:
    #print("The number you entered is 0.")
#elif 0 < user_num <= 100:
    #print("The number you entered can be 1, 100, or anything in between.")
#else:
    #print("The number you entered is greater than 100.")


# Truthy and Flasey Statements
# for strings anything other than an empty string is a truthy, this is equivalent to boolean true value
# an empty string is a falsey, false boolean value
# for integers, zero is the falsey value, any integers other than zero are truthy
# for floats 0.0 is falsey, anything other than that is truthy.

# strings_example = input("Enter any string other than an empty one.")

# if strings_example != "":
    # print("Thank you for entering something.")
# else:
    # print("You did not enter a string.")

# bool() function : can tell you the equivalent boolean value of anything.





# Loops are a useful tool for when you want to have code run on every item in a piece of data that has indexes such as
# a string.

# while loops
# A while loop runs its code each time it checks is condition and it turns out to be true.
# while loop stops running its code when its condition evaluates to false.

# counter = 0

# while counter < 3: # while, a condition which evaluates to a boolean value, a colon, code that loop will run
    # print("something")
    # counter += 1

# Avoiding infinite loops : need to make sure that each while loop you create has a condition that stops it from running
# an infinite amount of times.
# a while loop that has and end caused by its condition is known as a closed loop.


# For Loops : useful because it is a type of loop that is controlled by the length of the iterable piece of data that is
# being used rather than a condition

# word = "house"

# for letter in word:
    # print(letter)

# range

# one_input = range(5)

# for num in one_input:
    # print(num)


# two_inputs = range(5, 10)

# for num in two_inputs:
    # print(num)

# for a range with three arguments the third argument is called step size and can be used to increment up or down since
# it can be positive or negative

# three_inputs = range(6, -1, -2)

# for num in three_inputs:
    # print(num)


# String Methods : functions that are built into Python, which allow you to perform useful operations such as splitting
# them or changing their case so that they can be used as part of non-case-sensitive comparisons with other strings.
# characters like spaces and punctuation are not affected by the upper and lower methods.

all_low = "there are no capitals here."
print(all_low.upper())
print(all_low)
all_up = "THIS IS SHOUTING TEXT!"
print(all_up.lower())

# .isupper() the upper method returns a boolean value of true if the letters in the string it is being used
# are all uppercase

print("Mixed Case".isupper())  # this returns false
print("ALL CAPS!".isupper())   # this returns true

# .islower() the is lower method returns a boolean value of true if the letters in the string being used are all
# lowercase

print("AAAHHH".islower())  # this returns false
print("$100 is a lot to make in an hour.".islower())  # this returns true

# While they can be used on strings that contain no spaces, punctuation and special characters such as ampersands and
# asterisks, the .isupper and .islower method's will only return true for strings that have at least one uppercase
# letter or one lowercase letter in them, respectively.

# can use multiple string methods

print("SHOUT!".lower().isupper())
print("This Is An Example Of Title Case".istitle())

print("the great gatsby".title())  # this turns a string into a title sentence

print("this is a string".startswith("this"))
print("this is a string".endswith("string"))

# the .join() method is useful then you have multiple strings that you want to combine into a single string

print("" .join(["one","two","three"]))
print(" ".join(["one", "two", "three"]))
print("," .join(["one","two","three"]))
print(", " .join(["one","two","three"]))

# the .split() method does the opposite of the joint method, meaning that when it is used on a string it splits that
# string and returns a list

print("Eggs, Milk, Waffles, Bacon".split())
print("Eggs, Milk, Waffles, Bacon".split(", "))

# .rjust() .ljust() when coupled with one argument they will return strings that have spaces added either to the left
# or right of them

print("hello world".ljust(15) + "four spaces latter.")

# you can also to this with .rjust() and .ljust(), but the second argument can only be one character long and must
# be a string

print("hello world".rjust(15, "_"))
print("hello world".ljust(15, "*"))


# .center()

print("hello world".center(15,":"))

# .strip(), .rstrip(), and .lstrip() are useful for when you want to remove characters such as white spaces from a
# string
# .strip() removes all the spaces from both sides of the string
# .rstrip() removes all the spaces from the right side of the string
# .lstrip() removes all the spaces from the left side of the string

print("I had an exciting trip!!!11111")
print("I had an exciting trip!!!11111".strip("1"))
print("I had an exciting trip!!!11111".rstrip("1"))
print("I had an exciting trip!!!11111".lstrip("1"))

print("juice, bread, cheese, beef, bread".rstrip(", bread"))

print("blueblueyellowblue".strip("eulb"))  # strip removes characters from either side of the string

# .replace() is a string method which is used to search for and replace a string, it takes two strings as arguments, the
# first is the string that will be searched for when it is called, the second is the string that will replace the first
# string

print("Good morning.".replace("morning","afternoon"))

# len()
print(len("tree"))

# .format() will allow is to put curly brackets inside of a string to mark where we want other strings to be. Less
# messy alternative to concatination

# name = input("What is the job applicant's name?")
# degree = input("What did they major in at college?")
# job = input("What is their current occupation?")
# experience = input("How many years have they been working in the field?")

#print("{} majored in {}, works as a {}, and has {} years of experience.".format(name, degree, job, experience))

# arr = [1,2,2,3,4,5,5,5,6,7,8,8,9]

# print(tuple(set([x for x in arr if arr.count(x)>1])))


# list is a data type which contains multiple values in an ordered sequence values within a list are also known as items
# a list can contain as many items as you want and can contain values of any data type, can even contain list
# which would be known as a list of lists
# can have different data types within the same list
# list() function takes an iterable data type, such as a string as an argument and converts it to a list that it then
# returns

example_list_1 = [5, 4, 3, 2, 1]

print(list("blah"))

# in and not in operators can be used to check whether a value is or isn't in a list like other operators they are used
# in expressions

checked_list = [1, 2, 3, 4]
print(8 in checked_list)
not_in_example = 8 not in checked_list  # this returns true, the not in operator would return false if it was used on a
# value which checked_list contained
print(not_in_example)

# indexes and list slicing

indexes_example = ["carpet", "hardwood", "linoleum"]
print(indexes_example[1])

indexes_example2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(indexes_example2[2][0])

# negative indexes : using -1 as the index number when accessing by index gives you the last item of the list

negative = [1, 2, 3, 4, 5]
print(negative[-1])
print(negative[-2])
print(negative[-3])
print(negative[-4])
print(negative[-5])

# items that are accessed by index from lists can also be used in expressions like mathmatical expressions and string
# concatenation, provided that the items being accessed are the correct data type.

mixed = [False, 365, 4.24, "this is the string"]
print(mixed[2] + 1.76)
print("I have used \"" + mixed[-1] + "\" as an example too many times.")

# list slicing : if you only wanted to get a specific portion of a list

sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sliced[:4])
# print(sliced[3:8])
# print(sliced[6:])


# when you do this you get a segment from a larger list
# You can reassign the items in a list

example = [2, 4, 6, 8, 0]
print(example)
example[3] = 10
example[1:4] = [3, 2, 1]
print(example)
example[4:7] = [7, 6, 5]
print(example)

# del and list methods : the methods for this lecture are specific to the list data type
# del statements allow you to delete values from a list

planets = ["pluto", "mars", "earth", "venus"]
del planets[0]
print(planets)

# .remove() method allows you to remove what you pass it as an argument from a list

# planets.remove("pluto")
# print(planets)

colors = ["blue", "red", "white", "blue", "orange", "blue"]
colors.remove("blue")
print(colors)

# in this case the .remove() would remove the first instance of blue only

# del vs. .remove() del removes an item based off index number of the item being removed.
# .remove() searches a list for whatever item you passed it as an argument and removes it from the list when it finds
# that item
# .remove() gets rid of a specific item if it finds it, regardless of where it is located in a list.
# dell just deletes an item from an index
# .append() takes an argument and adds that to the end of the list it is being used on.

pets = ["cat", "dog", "parrot"]
print(pets)
pets.append("fish")
print(pets)

# .insert() allows you to add an item anywhere in the list rather than just at its end.
# .insert() takes two arguments where the first argument is the index at which a new item will be added to a list
# and the second item is the item that will be added to the list at that index

pets.insert(1, "turtle")
print(pets)

# .sort() method can be used to sort list made up of items that are all numbers or strings (will be alphabetical)

numb_list = [2.718, 4, -19, 10000, 0]
print(numb_list)
numb_list.sort()
print(numb_list)

str_list = ["Jessica", "Shaun", "EJ", "Nathan", "Liv"]
print(str_list)
str_list.sort()
print(str_list)

# reverse=True to sort items from a list in reverse order. So for numbers this would be greatest to least and for
# strings it would be in the reverse alphabetical order
# the .sort() method cannot be used on mixed lists, it does not have a way to compare strings and numbers
# .sort() only works on lists with ints, floats, or boolean values (False = 0, True = 1)

# ASCIIbetical order uppercase letters come before lowercase letters
ASCIIbetical = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
ASCIIbetical.sort(key=str.lower)
print(ASCIIbetical)

# use key=str.lower if you want to sort a list with mixed case in alphabetical order

# .index() the index list method allows you to find out the index number of the item you pass it. When called the
# .index() method returns an index number as an integer
# if you try to use this method on an item that does not appear in the list you will get an error message

metals = ["copper", "gold", "silver", "iron"]
# print(metals.index("silver"))

numbers = [4, 3, 2, 1, 0, 1, 2, 3, 4]
print(numbers.index(3))

# when using .index() on a list where an item appears multiple times it will give you the index number of the first
# time that item appears on the list

# .pop() method removes and returns an item from a list, would use this instead of .remove() or .dell() of you wanted
# the item returned to you so you could use it in some other way.

bands = ["Queen", "Led Zeppelin", "The Beatles", "MUSE", "Radiohead"]
end = bands.pop(3)
print(bands)
print(end)

# lists = mutable
# strings = immutable


ex_1 = [1, 2, 3]
ex_1[1] = 5
print(ex_1)

ex_2 = "123"
ex_2 = "153"
print(ex_2)

# creating new strings from old strings : access by index or slicing and using those
# parts to create a new string through concatination

ex_3 = "No, you can't."
ex_4 = "Yes" + ex_3[3:11] + "!"
print(ex_4)

# references : when a list is assigned to a variable instead of the variable actually storing that list like it would
# a number or a string, it stores a reference to that list, which is a value that points to a piece of data such as a
# list. So not the list itself.

ex_5 = 3.14
ex_6 = "coconut"
ex_7 = ex_5
ex_8 = ex_6
print(ex_7)
print(ex_8)

ex_9 = [1, 2, 3, 4, 5]
ex_10 = ex_9
ex_10[2] = 4
print(ex_9)
print(ex_10)

# ex_10 and ex_9 are referencing the same list
# all mutable data types are stored as references and all immutable are stored as themselves
# doing this saves memory

# copy module and deepcopy() will allow you to create a copy of a list with its own new reference

import copy
ex_12 = [1, 2, 3, 4, 5]
ex_13 = copy.deepcopy(ex_12)
ex_13[2] = 4
print(ex_12)
print(ex_13)

# since they don't share the same reference we can modify ex_13 w/o affecting ex_12

# lists can span multiple lines of code

ex_15 = ["bush",
         "fern",
         "tree",
         "moss"]

print(ex_15)

# \ line continuation : for math make sure everything is lined up vertically to make sure code is PEP compliant
# don't have to worry about this with strings unless they are concatenated

ex_16 = 2 + \
        4 + \
        1
print(ex_16)

ex_17 = "The Emp\
ire Strikes \
Back"

print(ex_17)

ex_18 = "hello " + \
        "world"

print(ex_18)


# dictionaries : are a data type which can store a collection of values like a list, but differs in that instead of
# having to have each of its items be assigned an index number that is an integer, the items that a dictionary
# contains are assigned to keys, which can be different data types

consoles = {"nintendo": "wii", "microsoft": "xbox", "sony": "playstation"}
print(consoles["microsoft"])
val = consoles["microsoft"]
print(val)
print("The " + consoles["sony"] + " 4 is Sony's newest gaming console.")

# a key value pair consists of a key and a value separated by a colon or a space, can have multiple pairs just make
# sure to separate them with a comma and a space
# you can use keys to access values from a dictionary, like you would use index numbers access the items in a list
# values from dictionaries can also be assigned to variables and used in expressions
# keys can be integers, floats or even boolean values, can have different data types for different keys in the same,
# dictionary
# unlike lists dictionaries are unordered, lists need to have the exact same items in the exact same order in order for
# python to consider them equivalent

print([2, 4, 6] == [2, 4, 6])
print([2, 4, 6] == [6, 4, 2])

# two dictionaries being compared, both need to contain the same key value pairs in order to be considered equal but
# these pairs do not need to be in the same order

first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
second = {2: 2.3, 0: 2.1, 3: 2.4, 1: 2.2}
print(first == second)

# key error : if you tried to access a value from a key that doesn't exist within a dictionary.
# can check whether a key exists within a dictionary by using the in and not in operators

print(0 in first)
print(1 not in first)

# dictionary methods 1: .keys(), .values(), .items(), and .get()
# the .keys() method allows you to get all the keys from a dictionary

birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_years.keys())

for key in birth_years.keys():
    print(key)

# .values() is a method which allows you to get all he values from a dictionary

print(birth_years.values())

for values in birth_years.values():
    print(values)

# use .items() to get the values and the keys of a dictionary at the same time

print(birth_years.items())
for key, value in birth_years.items():
    print(key, value)

# can use in and not in on a value instead of a key

print("elizabeth" in birth_years.values())

# .get() method allows us to look for and get a key from a dictionary and return
# something other than an error message

print(birth_years.get(1975, "1975 is not a key in birth years."))

# dictionaries are an immutable data type like lists, which means variables that
# have been assigned to dictionaries also hold references to dictionaries, not
# the dictionary values themselves
# so if you try to  make a copy of a dictionary and assign it to a new variable
# any changes you make to the original would also affect the original dictionary
# because they both reference the same dictionary

print(birth_years)
people = birth_years
people[1982] = "madeline"
print(birth_years)

# can use the length value to get the length of a dictionary

print(len(birth_years))  # returns the number of key value pairs

# dictionary methods 2 : .fromkeys(), .pop(), and .popitem()
# .fromkeys() method returns a dictionary using two values that it was given as arguments, the first is the key
# the second is a value

ex_1 = {}.fromkeys(["address"], "1600 Pennsylania Ave NW")
print(ex_1)

ex_2 = {}.fromkeys("ad", "1600 Pennsylania Ave NW")
print(ex_2)

ex_2 = {"make": "Honda", "model": "civic", "year": 2016}
popped = ex_2.pop("model")
print(ex_2)
print(popped)

# .popitem() is a method which allows you to remove the last key value pair from a dictionary without having to
# specify the item
ex_3 = {"name": "bob", "age": 38, "occupation": "accountant",\
        "workplace": "H&R block"}
ex_3.popitem()
print(ex_3)

# .clear() method removes everything in a dictionary that it is called on
places_to_visit = {1: "England", 2: "Scotland", 3: "Wales", 4: "Northern Ireland"}
print(places_to_visit)
places_to_visit.clear()
print(places_to_visit)

# .copy() the copying method returns an exact copy of a dictionary that its own reference

birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_years)
people = birth_years.copy()
people[1982] = "madeline"
print(birth_years)

# .update() allows us to add key value pairs from one dictionary to another or to overwrite the values  of
# existing keys in a dictionary with values from another dictionary.
# takes one argument which is the dictionary you want to add the key value pairs from

city_info = {"country": "Canada", "providence": "Ontario", "city": "Toronto"}
population = {"population": 2930000}
city_info.update(population)
print(city_info)
print(population)   # population remains unchanged, its contents were just added to city_info

# .setdefault() if key is not found itm will add it and it's value to the dictionary, cannot change the default
# value of key this way

computers = {"Google": "Chromebook", "Apple": "MacBook", "Microsoft": "Surface Pro"}
computers.setdefault("Lenovo", "ThinkPad")
print(computers)

# dict() function is an alternate way to create a dictionary, when you create keys using the dict function, they
# must be made up of letters, underscores, and numbers
# the keys in the dict function call cannot contain punctuation, special characters, and they can't be boolean values


empty = dict()
print(empty)
with_values = dict(a=1, b=2, c=3)
print(with_values)

# tuples

tuple_1 = ("a", "b", "c", "d", "e")
tuple_2 = (2.718, False, [1, 2, 3])
tuple_3 = (1, 1, 0, 0, 0)
tuple_4 = (5, 4, 3, 2, 1)

# can also create a dictionary using a tuple using a list or string
# items in a tuple have an index number

tuple_5 = tuple([3.14, 2.205, 10])
tuple_6 = tuple("abcdefg")
print(tuple_5)
print(tuple_6)

tuple_8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_8[2])
print(tuple_8[:8])
print(tuple_8[2:8])
print(tuple_8[2:7])
print(tuple_8[3:])

# tuples are an immutable, they are useful when you have collection of data
# that you know that you will not want to change later.
# their inability to be changed will prevent unwanted changes from being
# made to them

tuple_9 = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"\
           ,"Sunday")
print(tuple_9)

# tuples take up less space in memory than other mutable date types so they
# are much faster than lists

tuple_12 = (1, 3, 5)
list_1 = [1, 3, 5]
print(tuple_12.__sizeof__())
print(tuple_1.__sizeof__())

# looping through tuples

major_cities = ("Tokyo", "London", "New York", "Shanghi", "Sydney")

for city in major_cities:
    print(city)

counter = 0

while counter < len(major_cities):
    print(major_cities[counter])
    counter += 1

backwards = len(major_cities) - 1
while backwards >= 0:
    print(major_cities[backwards])
    backwards -= 1

# tuple slicing with step

ints = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(ints[::3])    # stride length of 3
print(ints[1::2])   # evens only
print(ints[7::-1])  # backwards from 8
print(ints[8::-2])  # odds only backwards

# tuple methods

nested = (1, 2, 3, (4, 5, 6), (7, 8, 9), (10, 11, 12))
print(nested[4])
print(nested[5][1])

# the .count() method returns the number of times a value that appears
# as its argument appears in a tuple

repeat = (7, 3, 3, 3, 0, 0, 7, 0, 0)
print(repeat.count(7))
print(repeat.count(3))
print(repeat.count(0))

ints = (1, 1, 7)
print(ints.index(7))
print(ints.index(1))  # index number of the first time that value appears


# intro to sets
# sets cannot have repeating items, they get ignored
# items in a set are unordered

# set_1 = {9, 8, 7, 6}    # set literal
# set_2 = set({"a", "b", "c", "d", "e"})
# print(set_1)
# print(set_2)

# set_3 = set()   # empty set
# set_4 = set(range(1, 12, 2))
# print(set_4)

# a set hold items that are of different data types
set_5 = {"a", 3.14, 18, True}
print(set_5)

# sets cannot have their items accessed from them by index, need to use a
# for loop if you want to access individual items

set_6 = {3, 4, 5, 6, 7, 8}

for num in set_6:
    print(num)


print(6 in set_6)

# sets are useful in situations where you want a collection of items,
# but you don't want duplicate items in the collection, and you also
# don't care about the order of items that make up the collection

# set methods
# the .add() method takes an item of any data type as its arguments and
# adds that to the set it is called on.

scifi = {"star trek", "star wars", "halo"}
scifi.add("mass effect")
print(scifi)

# .remove() takes an item of any data type and removes that item from the
# set it is called on

fruits = {"apple", "orange", "banana", "tomato"}
fruits.remove("tomato")
print(fruits)
# fruits.remove("pear")

# .discard() does almost the same as remove just no error message

fruits.discard("pear")
print(fruits)

# .clear() takes no arguments and just gets rid of everything in the set it is called on

mountains = {"Everest", "Kilimanjaro", "Fuji"}
print(mountains)
mountains.clear()
print(mountains)

# The .copy() method returns a copy set that has its own place in memory
mountains = {"Everest", "Kilimanjaro", "Fuji"}
set_2 = mountains.copy()
print(set_2 is mountains)
print(set_2)

# .union() method allows you to combine all the items from two different
# sets into a single set

set_1 = {1, 2, 3, 4, 5}
set_2 = {6, 7, 8, 9, 10}
# set_3 = set_1.union(set_2)
# print(set_3)

# could also use the pipe method

set_4 = {11, 12, 13, 14}
set_5 = {15, 16, 17, 18}
set_6 = set_4 | set_5
print(set_6)

# .intersection() is a method that allows you to find out what items two sets have in common

set_7 = {4, 5, 6, 7, 8}
set_8 = {6, 7, 8, 9, 10}
# set_9 = set_7.intersection(set_8)
set_9 = set_7 & set_8
print(set_9)

# subtraction and .difference() you can subtract one set from another based on their intersection
# removes the intersection from the set being subtracted from
set_1 = {4, 5, 6, 7, 8}
set_2 = {6, 7, 8, 9, 10}
set_3 = set_1 - set_2
set_3 = set_1.difference(set_2)
print(set_3)

# set comprehensions are a third slightly more advanced way to create a set
comp_1 = {even+2 for even in range(2, 11, 2)}
print(comp_1)

comp_2 = {char.lower() for char in "ALLCAPS"}
print(comp_2)

































