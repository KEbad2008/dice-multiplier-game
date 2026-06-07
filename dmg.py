# Name: @ebaduk117 on hackclub
# Date: 2026-06-05 to 07
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


# Define display_prizes(), which prints the prizes the user can buy, and how much of that prize (upon function being called).
def display_prizes(points):
    print()
    print("---------Available Prizes-----")
    print("[1] Candy Bar - 10 points | Max: ", points // 10)
    print("[2] Juice Box - 25 points | Max: ", points // 25)
    print("[3] Pencil Crayon Pack - 35 points | Max: ", points // 35)
    print("[4] Phone Case - 50 points | Max: ", points // 50)
    print("[5] Earplugs - 75 points | Max: ", points // 75)
    print("[6] Jumbo Size Stuff Toy - 200 points | Max: ", points // 200)
    print("Your current amount of points: ", points)
    print()
    time.sleep(0.5)
# Define pick_prizes(), which lets user choose prize, and deducts points based on prize bought.
def pick_prizes(points):
    stop_shopping = 0
    out_of_money = 1
    while points >= 10 and stop_shopping != 1:
        display_prizes(points)
        print("Which Prize Would You Like To Buy?")
        prize_choice = input("Enter The Prize Number, or 'done' to stop!: ")

        while prize_choice not in ['1', '2', '3', '4', '5', '6', 'done', 'Done', 'DONE', 'quit', '0']:
            print("Please enter an option from the menu!")
            prize_choice = input("Which Prize Would You Like To Buy? Enter The Prize Number, or 'done' to stop!: ")

        if prize_choice == "1" and points >= 10:
            points -= 10
            print("You Bought A Candy Bar!")
        elif prize_choice == "2" and points >= 25:
            points -= 25
            print("You Bought A Juice Box!")
        elif prize_choice == "3" and points >= 35:
            points -= 35
            print("You Bought A Pencil Crayon Pack!")
        elif prize_choice == "4" and points >= 50:
            points -= 50
            print("You bought a Phone Case!")
        elif prize_choice == "5" and points >= 75:
            points -= 75
            print("You bought Earplugs!")
        elif prize_choice == "6" and points >= 200:
            points -= 200
            print("You bought a Jumbo Stuff Toy!")
        elif prize_choice == "done" or prize_choice == "Done" or prize_choice == "DONE" or prize_choice == "quit" or prize_choice == "0":
            print("Thank you for checking out the prizes!")
            stop_shopping = 1
        else:
            print("Sorry, but you can't afford that prize, Thank You!")
            print()

        if points < 10:
            print()
            print("You no longer have enough points to purchase prizes.")
            out_of_money = 1
    if points < 10 and out_of_money == 0:
        print("You dont have enough points to shop!")
        
    print("Your remaining points: ", points)

    return points

# Output - Print Graph and statistics to the user.
def print_graph(roll_sums):
    sum_frequency = [0] * 16 
   
    for roll_sum in roll_sums:
        if 2 <= roll_sum <= 15:
            sum_frequency[roll_sum] += 1
    print()
    print("-----Frequency of Roll Sums-------")
    
    for roll_sum in range(2, 16): 
        stars = '*' * sum_frequency[roll_sum]  
        print(roll_sum, ":", stars)  
