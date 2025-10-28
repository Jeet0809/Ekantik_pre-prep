def main():
    income = int(input("Enter your income: "))
    
    if income < 500000 :
        tax = 0 
    elif 500000 <= income < 1000000 :
        tax = (income - 500000) * 0.2 
    else :
        tax = (500000 * 0.2) + ((income - 1000000) * 0.3)
    
    print(f"Income tax = {tax:.2f}")

if __name__ == "__main__" :
    main()