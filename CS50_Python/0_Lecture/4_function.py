# part 4

# def hello(to="world"):
#   print("hello,", to)
  
# hello()
# name = input("What's your name? ").strip()  
# hello(name)
# # print(name)

def main():
  name = input("What's your name? ").strip()
  hello(name)
  # print(name)

  x = int(input("What's x? "))
  print(x , "squared is" , square(x))

def square(n):
  # return n * n 
  # return n ** 2 
  return pow(n, 2)

def hello(to = "world"):
  print("hello,", to)


main()

# learnt about scope ,defining function,return values

# def hello(to="world"):
#   print("hello,", to)
  