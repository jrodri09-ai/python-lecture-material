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





























































































