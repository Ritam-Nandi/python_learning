import random

print ("Press r for Rock, s for Scissor, p for Paper. To quit game press q")
choice=input("Type any of the above and press enter: ")

computer_won=0
player_won=0

while choice != "q":
    computer=random.choice(["r","p","s"])
    
    if choice==computer:
        print("No one won this round. Try Again")
    elif choice == "r":
        if computer == "p":
            computer_won = computer_won + 1
        else:
            player_won = player_won + 1
    elif choice == "p":
        if computer == "s":
            computer_won = computer_won + 1
        else:
            player_won = player_won + 1
    else:
        if computer == "r":
            computer_won = computer_won + 1
        else:
            player_won = player_won + 1
    
    if computer == "r":
        print ("Computers choice: Rock ")
    elif computer == "p":
        print ("Computers choice: Paper ")
    else:
        print ("Computers choice: Scissor ")

    print ("Player Won : %d times and Computer Won: %d times" % (player_won,computer_won) )

    print ("\nPress r for Rock, s for Scissor, p for Paper. To quit game press q")
    choice=input("Type any of the above and press enter: ")

