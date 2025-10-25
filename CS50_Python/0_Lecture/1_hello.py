# Lecture 0 part 1


print("hello , world")
# code hello.py   used to make that particular file 
# python hello.py  used to run that file  (i can only run the files in a terminal window )

#ask user for their name
# print("What's your name? ")
# input()

# combining these 2 for better structure
# input("What's your name?")

name = input("What's your name?")


# special method of comment 
"""
this is a comment
"""

# say hello to user 
# 1st way - print("hello, ",name)
# 2nd way - print("hello,", name)
# 3rd way - print("hello, " + name)

# Documentation of Python for print function
# print(*objects, sep=' ', end='\n' , file = sys.stdout, flush= False)
print("hello, ", end="")
print(name)
print("hello,",name , sep="?")

# 1st way 
print('hello, "friend"')
# 2nd way
print("hello , \"friend\"")
# 3rd way
# tells python to format stuff in the string in special way
print(f"hello, {name}")

#Documentation of string functions

#Remove whitespace from left and right str
#this is a type of method
# name = name.strip()

# Capitalize user's name 
# name = name.capitalize()

#Capitalize the first letter of every word
# name = ()
#say hello to user

#Remove whitespace from str and capitalize user's name
# name = name.strip().title()

# name = input("What's your name? ")
name = input("What's your name? ").strip().title() 

#Split user's name into first name and last name
first, middle , last = name.split(" ")

print(f"hello, {first}")
print(f"hello, {middle}")
print(f"hello, {last}")

# learnt about interactive mode of python 
