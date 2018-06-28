import random

#Prints the result (if player wins, loses, or ties)
def printWinner( winner ):
    if winner == 1:
        print( "You win!" )
    elif winner == -1:
        print( "You lose!" )
    else:
        print( "Tie!" )
"""
Determines who wins based on player input and computer's choice. Returns -1 if
the player loses, 1 if the player wins, and 0 if it is a tie.
"""
def winner( player, comp ):
    playerWin = -1
    if player == comp:
        playerWin = 0
    elif player == "rock":
        if comp == "scissors":
            playerWin = 1
    elif player == "paper":
        if comp == "rock":
            playerWin = 1
    else:
        if comp == "paper":
            playerWin = 1
    printWinner( playerWin )

"""
This part of the program runs the actual game:
    The user may enter "rock", "paper", or "scissors" until they chose to quit
    by entering "Q". The computer also generates a random choice. Based on these
    choices, a winner is determined and the results are displayed.
"""
game = True
choices = ["rock", "paper", "scissors"]
print( "Rock, Paper, Scissors! Enter \"Q\" to exit the game." )
while game:
    player = input( "\nEnter rock, paper, or scissors: " ).lower()
    if player == "q":
        print( "\nThank you for playing!" )
        game = False
    elif player != "rock" and player != "paper" and player != "scissors":
        print( "Invalid input." )
    else:
        comp = choices[ int( random.random() * 100 ) % 3 ]
        print( "Computer choice:", comp )
        winner( player, comp )


"""
========
 Output
========

Rock, Paper, Scissors! Enter "Q" to exit the game.

Enter rock, paper, or scissors: rock
Computer choice: rock
Tie!

Enter rock, paper, or scissors: rock
Computer choice: paper
You lose!

Enter rock, paper, or scissors: paper
Computer choice: rock
You win!

Enter rock, paper, or scissors: scissors
Computer choice: scissors
Tie!

Enter rock, paper, or scissors: hi
Invalid input.

Enter rock, paper, or scissors: q

Thank you for playing!
"""
