print(
    r'''
          ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
'''
)

# Welcome
print(
    "                    Welcome to Treasure Island\n               Your mission is to find the treasure\n"
)

# Choose left or right - Right Game over
choice1 = input("Would you like to go (L)eft or (R)ight? ").lower()

if choice1 == "l" or choice1 == "left":
    choice2 = input(
        "You've come to a lake and you can see an island. Would you like to (S)wim or (W)ait for a boat? "
    ).lower()

    if choice2 == "w" or choice2 == "wait":
        choice3 = input("Which Door (R)ed (B)lue or (Y)ellow ").lower()
        if choice3 == "R" or choice3 == "Red":
            print("Sorry, you got burned alive... GAME OVER!")
        elif choice3 == "B" or choice3 == "Blue":
            print("Sorry, you got eaten by a blue beast... GAME OVER!")
        elif choice3 == "Y" or choice3 == "Yellow":
            print("WINNER... GAME OVER!")
    else:
        print("You got eaten by a shark... GAME OVER!")
else:
    print("GAME OVER!")
