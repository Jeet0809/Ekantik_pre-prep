def main():
    rect(2,4)
    
def rect(row, col):
    for i in range(row):
        print("*\t" * col)
    
if __name__ == "__main__":
    main()