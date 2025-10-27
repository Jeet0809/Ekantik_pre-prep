def main():

    a = float(input("Enter number: \n"))
    b = float(input("Enter number: \n"))
    c = input("Enter Operator( +, -, *, /): \n").strip()
    # z = 0
    if c not in ("+", "-", "*", "/"):
        print("Enter Valid Operator")
        return 
    
    match c :
        case "+" :
            z = a + b 
        case "-" :
            z = a - b
        case "*" :
            z = a * b 
        case "/" :
            if b == 0 :
                print("Error: Not divisible by zero!")
                return 
            z = a / b 

    
    # print(z)
    print(f"Calculation of {a} {c} {b} = {z:.2f}")
    
if __name__ == "__main__":
    main()