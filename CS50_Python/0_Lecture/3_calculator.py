# part 3

# x = int(input("What's x? "))
x = float(input("What's x? "))
# y = input("What's y? ")
y = float(input("What's y? "))
# z = x + int(y)


# Documention of Round function
# round(number[, ndigits])
z = round(x + y)

# print(z)
# print(x + int(y))
# print(x + y)

# it looks cryptic , for showing 1,000 
print(f"{z:,}")

# z = x / y 
# z = round(x / y, 2)

# print(z)

# # another way of rounding , f string approach 
# print(f"{z:.2f}")