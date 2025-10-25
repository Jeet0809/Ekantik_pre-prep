#  match (switch)

name = input("Enter Name : \n")

match name :
  case "Harry":
    print("Jonk")
  case "Farry":
    print("Ronk")
  # case "Jerry":
  #   print("Tom")
  case "Jerry" | "Merry" | "Ferry" :
    print("Tom")  
  case _: 
    print("Who?")
  