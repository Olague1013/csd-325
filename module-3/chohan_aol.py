# Filename: chohan_aol.py
# Author: Andrew Olague
# Date: 09/28/2025
# Changes:
# 1. Input prompt changed to initials
# 2. House fee changed to 12%
# 3. Added 10 mon bonus if dice roll is 2 or 7
# 4. Added bonus notice in program intro

import random
import sys

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')

print("If you roll a 2 or 7, you get a 10 mon bonus!")

purse = 5000

while True:
    # Player places bet
    while True:
        pot = input("aol: ")
        if pot.upper() == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        elif not pot.isdecimal():
            print("Please enter a number.")
        elif int(pot) > purse:
            print("You do not have enough to make that bet.")
        else:
            pot = int(pot)
            break

    # Roll dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("The dealer lifts the cup to reveal:")
    print(dice1, dice2)

    # Determine if player won
    rollIsEven = (dice1 + dice2) % 2 == 0
    correctBet = "CHO" if rollIsEven else "HAN"
    bet = input("> ").upper()
    playerWon = bet == correctBet

    # Bonus if total roll is 2 or 7
    total_roll = dice1 + dice2
    if total_roll == 2 or total_roll == 7:
        print(f"You rolled a {total_roll}! You get a 10 mon bonus!")
        purse += 10

    # Apply win/loss and house fee
    if playerWon:
        print("You won! You take", pot, "mon.")
        purse += pot
        print("The house collects a", pot * 12 // 100, "mon fee.")
        purse -= pot * 12 // 100
    else:
        purse -= pot
        print("You lost!")

    # Check if player has run out of money
    if purse == 0:
        print("You have run out of money!")
        sys.exit()
