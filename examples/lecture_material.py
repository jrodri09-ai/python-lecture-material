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

print(ex2)

ex3 = 1.23 + 2.80
print(round(ex3, 2))

# subtotal of shopping list

pasta = 16.68

sauce = 6.98

cloves = 16.68

seasoning = 15.26

baguettes = 3.00

meatballs = 4.39

subtotal = round((pasta + sauce + cloves + seasoning + baguettes + meatballs),2)

print(subtotal)

string1 = 'welcome user'

print(string1)

ex_string2 = "orange"
print(ex_string2[2])

ex_string3 = "apple"
print(ex_string3[3])
print(ex_string3[:3])

ex_string4 = "apricots"

print(ex_string4[:3])
print(ex_string4[2:5])
print(ex_string4[4:])

concatenated = "R2" + "-" + "D2"

print(concatenated)
print(concatenated[1])
print(concatenated[0:2])

myName = "Jessica" + "Grace" + "Rodriquez"

print(myName)

nike = "Just do it!"

print(nike[10])
print(nike[5:8])
print(nike[8:11])
print(nike[0:4])

print("Don't " + nike[5:])

ex_1 = str(True)
ex_2 = str(29)
ex_3 = str(3.2789)

print(type(ex_1))
print(type(ex_2))
print(type(ex_3))

print("Hello\tfrom\tthe\tother\tside.")
print("line one\nline two")
print("\"Love is all you need.\"")

ex_4 = str(6.2389)

print(type(ex_4))
print(ex_4 + " is a float")
print("\"Hello, I'm Jessica, its nice to meet you!\"")

youAreAStar = "*******\n ***** \n ***\n *"

print(youAreAStar)


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

print(random.randint(1,10))


# function import is when a specific function is imported from a module
from random import randint

print(randint(10, 20))

# universal import: when you import every function from a module so that whenever you call any function from that module
# you do not need to type that modules name and a period

from random import *

print(random())

























