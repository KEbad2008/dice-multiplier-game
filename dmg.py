# Name: @ebaduk117 on hackclub
# Date: 2026-06-05
# File: dmg.py (dicemultipliergame)
# Desc: Multiplier Game | a dice game in python


# Imports 
import random
import time
from tkinter import *

# Process - Define Functions and run 5 rounds, store each rounds sum.

# Define tkinter_greet(): to send a welcome message in tkinter!
def tkinter_greet():
    window = Tk()
    window.title("Multiplier Game")
    lbl = Label(window, text="Hello There, and Welcome To The Multiplier Game! ", font=("Arial Bold", 30))
    
    lbl2 = Label(window, text="★★★★★★ Close this window to start the game! ★★★★★★", font=("Arial", 20))
    lbl.grid()
    lbl2.grid()
    window.mainloop()
    
# Define greeting(), which tells the user a little bit about the game.
def greeting():
    print("Welcome to the Multiplier Game!")
    time.sleep(2)
    print("You will be rolling dice, to try and earn as many points as you can.")
    time.sleep(2)
    print("However, there are punishments! Try not to roll 1's or a sum of 7!")
    time.sleep(2)
    print("There are also incentives, in which you can multiply your score.")
    time.sleep(2)
    print("There will be prizes at the end!")
    time.sleep(2)
    print("Enjoy!")
    time.sleep(2.5)
    print()

# Define user_roll_dice(), to generate roll 1 and 2. Then add their sum.
def user_roll_dice():
    die1 = random.randint(1, 9)
    die2 = random.randint(1, 6)

    print("You rolled a", die1, "on the first dice")
    print("You rolled a", die2, "on the second dice")
    
    roll_sum = die1 + die2
    print("Total points this roll (Sum of the rolls): ", roll_sum)
    print()
    
    return roll_sum, die1, die2


