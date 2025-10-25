def main():
    print(factorial(5))
    
def factorial(n) :
    f = 1 
    for i in range(n) :
        f *= (i+1)
    return f 

        
if __name__ == "__main__" :
    main()