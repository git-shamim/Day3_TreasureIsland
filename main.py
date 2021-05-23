
print("Welcome to the Treasure Island")
print("Your mission is to find the treasure")

choice1 = input("You\'re at a crossroad. Where do you want to go ? Type 'left' or 'right': \n").lower()

if choice1 == "left":
    choice2 = input("You\'ve come to a lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
    if choice2 == "wait":
        choice3 = input("There is a house with three doors, red, yellow, blue. Which color you choose ? \n").lower()
        if choice3 == "yellow":
            print("You found the treasure, You win!!")
        elif choice3 == "red":
            print("You entered a room full of fire, Game Over!")
        elif choice3 == "blue":
            print("You went to a room full of beasts, Game Over!")
        else:
            print("You did not choose a right option, Game Over!")
    else:
        print("You got attacked, Game Over!")
else:
    print("You fell into a hole, Game Over!")