def main():
    stars_pattern(5)
    
    
def stars_pattern(n) :
    for i in range(n) :
        print("*" * (i+1) )
        
if __name__ == "__main__" :
    main()