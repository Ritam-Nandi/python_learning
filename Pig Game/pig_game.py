import random

player1_score = 0 #player 1 is +1
player2_score = 0 #player 2 is -1
winning_score = 50
current_player= 1 # start with player 1

while player1_score < 50 or player2_score < 50 :
    if current_player == 1:
        print("Its Player 1's turn")
    else:
        print("Its Player 2's turn")

    throw=input("Press r to roll the dice or q to skip your turn ")

    if throw=="q":
        print("You have skipped your turn")
        current_player = current_player * -1
    
    else:
        val=random.randrange(1,6)
        print("Dice roll has given score: ", val)

        if val==1:
            current_player = current_player * -1
        else:
            if current_player == 1:
                player1_score += val
            else:
                player2_score += val
                

if player1_score > player2_score:
    print("Player 1 wins")
else:
    print("Player 2 wins")