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

# Define active_round(), which plays 1 round of the game, upon being called.
def active_round(account_balance, round_number, roll_sums):
    round_points = 0
    double_six_count = 0
    
    rolling = True 
    print("----Round:", round_number,"----")
    time.sleep(1)

    while rolling:
        roll_sum, die1, die2 = user_roll_dice()  
        roll_sums.append(roll_sum)
        round_points += roll_sum  

        # Apply Punishments from the apply_punishments() function if user rolls a punishment.
        account_balance, round_points = apply_punishments(die1, die2, round_points, account_balance)

        if die1 == 6 and die2 == 6:
            double_six_count += 1

        print("Your current points for this round: ", round_points)
        print("Your account balance: ", account_balance)
        time.sleep(0.5)

        rolling_input_valid = False  
        while not rolling_input_valid:
            try:
                print()
                rolling_input = int(input("Enter [1] to roll again | Or [0] to bank your points (save round points & end round): "))
                if rolling_input == 1:
                    rolling = True  
                    rolling_input_valid = True
                elif rolling_input == 0:
                    rolling = False  
                    print("You have chosen to bank your points this round. Your total points: ", round_points)
                    account_balance += round_points

                    # Apply incentives from the apply_incentives function, when they meet incentive requirement upon roll.
                    account_balance = apply_incentives(round_points, account_balance, double_six_count)
                    rolling_input_valid = True
                # Let user know if they entered an invalid input, either strings or numbers not 0 or 1.
                else:
                    print("Invalid input. Please enter 1 for Yes or 0 for No.")
            except ValueError:
                print("Invalid input. Please enter a valid number (1 for Yes or 0 for No).")

    return round_points, account_balance

# Define apply_incentives(), which sets up all the incentives, and their reward's.
def apply_incentives(round_points, account_balance, double_six_count):
    if double_six_count >= 5:
        account_balance *= 20
        print("You rolled Double 6's at least 5 times, therefore, your account balance has been multiplied by 20!")
        print("Your updated account balance is: ", account_balance)
    
    elif 50 <= round_points < 75:
        account_balance += round_points * 2
        print("Your points have been doubled to: ", account_balance)
        
    elif 75 <= round_points < 100:
        account_balance += round_points * 3
        print("Your points have been tripled to: ", account_balance)
        
    elif round_points >= 100:
        account_balance += round_points * 4
        print("Your points have been quadrupled to: ", account_balance)

    return account_balance

# Define apply_punishments(), which deducts points based on the punishment-qualified roll they rolled.
def apply_punishments(die1, die2, round_points, account_balance):
    if die1 == 1 or die2 == 1:
        print("You rolled a 1! Therefore, your points for this round have been reset to zero.")
        round_points = 0
        
    if die1 == 1 and die2 == 1:
        print("Snake Eyes! Your round points and account balance have been reset to zero!")
        account_balance = 0 
        round_points = 0    
        
    if die1 + die2 == 7:
        round_points = (round_points + 1) // 2
        print("Your rolls equal 7! Therefore, your round points have been halved to: ", round_points)

    return account_balance, round_points


