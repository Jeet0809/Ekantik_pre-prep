def main():
    inverseStar(5)
    
    
def inverseStar(n) :
    for i in range(n) :
        print("*" * (n - i) )
        
if __name__ == "__main__" :
    main()