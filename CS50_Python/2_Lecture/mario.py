for _ in range(3) :
    print("#")
    
def main():
    blocks = int(input("No. of blocks required :\n"))
    print_column(blocks)
    print_row(3)
    print_block(3, 3)
    
    
def print_row(width):
    print("?" * width)
    
def print_column(height):
    # for _ in range(height):
    #     print("#")
    print("#\n" * height, end="")
    
def print_block(height, width):
    
    # for each brick in row
    for i in range(height) :
        
        # for each brick in column 
        # for j in range(width) :
        #     print("# " , end="")   
        # print()            
        print("# " * width)
            
        
if __name__ == "__main__" :
    main()