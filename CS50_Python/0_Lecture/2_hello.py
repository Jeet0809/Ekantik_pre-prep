# Part 2 

"""
Write code to ask for a full name and print "Hello, [LAST NAME], [First name] , [Middle name]" (last name in caps, first name normal case).
"""
name = input("What's your name? ").strip()
first , middle , last = name.split()
print(f"Hello, {last.upper()} {first.capitalize()} {middle.capitalize()}" )