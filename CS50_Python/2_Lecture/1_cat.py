i = 0 
while i < 3 :
    print("meow")
    # i = i-1
    i += 1  
    
print()

# for i in [0,1,2] :
#     print("meow") difficulty 

for _ in range(3) :
    print("meow")
#  by default it gives 0 ,1 ,2 

print()

print("meow\n" * 3 )

while True :
    n = int(input("Enter n : "))
    # if n < 0 :
    #     continue 
    # else :
    #     break
    if n > 0 :
        break 
    
for _ in range(n) :
    print("meow", end="\n")
    
print()

def main():
    
    n = get_number()
    meow(n)
    
def get_number() :
    while True :
        n = int(input("Enter n :"))
        if n > 0 :
            break
            # return n
    return n 

def meow(n):
    for _ in range(n):
        print("meow")
        
if __name__ == "__main__" :
    main()