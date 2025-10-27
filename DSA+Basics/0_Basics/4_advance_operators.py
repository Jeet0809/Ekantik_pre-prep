# Identity operators: is, is not
# Membership operators: in, not in

# Identity
x = [1, 2, 3]
y = [1, 2, 3]
z = x


print(f"x is y: {x is y}")  # False (different objects)
print(f"x is z: {x is z}")  # True (same object)
print(f"x == y: {x == y}")  # True (same values)

# Membership
fruits = ["apple", "banana", "cherry"]

print(f"'apple' in fruits: {'apple' in fruits}")      # True
print(f"'mango' in fruits: {'mango' in fruits}")      # False
print(f"'mango' not in fruits: {'mango' not in fruits}")  # True