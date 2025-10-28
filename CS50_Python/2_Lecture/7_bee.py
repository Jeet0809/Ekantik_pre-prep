WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}



def main():
    global WORDS 
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")
    total_points = 0
    for word, points in WORDS.items():  # keys , value
        print(f"{word} is worth {points} points")
    
    print()
    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: \n")
        
        if guess == "GRAPHIC":
            WORDS.clear()
            print("You've won!")
        if guess in WORDS.keys():
            point = WORDS.pop(guess)
            # print(f"Good job! You scored {WORDS[guess]} points.")
            print(f"Good job! You scored {point} points.")
            # total_points += WORDS[guess] 
            total_points += point
            
            
        
    
        # TODO: Check is guess in Dictionary
        
    print("That's the game")
    print(f"Total points scored by you are {total_points}")
    
main()