import os
import random
ai = 0
player2 = 0
score2 = 0
score = 0
scoreai = 0
print("Welcome to GITCommitDie")

meny = 0

while meny !=489: #fixa så att den känner igen 1 eller 2 senare
    try:
        meny = int(input("Tryck 1 för AI eller 2 för 2 spelare"))
    except: 
        print("Försök igen, 1 för AI eller 2 för 2 spelare")
    if meny == 1:
        ai = random.randint(1,3)
        print("Option 1: Sten")
        print("Option 2: Sax")
        print("Option 3: Papper")
        player = int(input("Choose an option"))
        if player == ai:
            print("Tie")
        elif player == 2 and ai == 1:
            scoreai += 1
            print("AI wins", scoreai)
        elif player == 3 and ai == 2:
            scoreai += 1
            print("AI wins", scoreai)
        elif player == 1 and ai == 3:
            scoreai += 1
            print("AI wins", scoreai)
        else: 
            score += 1
            print("Player wins", score)
        if score > 2:
            print("Player wins")
            break
        if scoreai > 2:
            print("AI wins")
            break
    if meny == 2:
        print("Option 1: Sten")
        print("Option 2: Sax")
        print("Option 3: Papper")
        player = int(input("Choose an option"))
        print("****")
        print("****")
        print("****")
        print("****")
        print("****")
        print("****")
        print("****")
        print("****")
        print("****")
        player2 = int(input("Choose an option"))

        if player == player2:
            print("Tie",)
        elif player == 2 and player2 == 1:
            score2 += 1
            print("Player 2 wins", score2)
        elif player == 3 and player2 == 2:
            score2 += 1
            print("Player 2 wins", score2)
        elif player == 1 and player2 == 3:
            score2 += 1
            print("Player 2 wins", score2)
        else:
            score += 1 
            print("Player1 wins", score)
        if score > 2:
            print("Player1 wins")
            break
        if score2 > 2:
            print("Player2 wins")
            break

    
