for _ in range(3) :
    print("#")
    
def main():
    # blocks = int(input("No. of blocks required :\n"))
    # print_column(blocks)
    # print_row(3)
    
    print_block(int(input("Height:\n")) , int(input("Width: \n")))
    
    
def print_row(width):
    print("?" * width)
    
def print_column(height):
    # for _ in range(height):
    #     print("#")
    print("#\n" * height, end="")
    
def print_block(height, width):
    
    # for each brick in row
    for i in range(height) :    # 0, 1, 2, 3 auto
        
        print("# " * width)
            
        # for each brick in column 
        # for j in range(width) :
        #     print("# " , end="")   
        # print()            
        
if __name__ == "__main__" :
    main()