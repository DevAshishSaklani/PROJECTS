import random

# Global variables to track runs
total_run_c = 0
total_run_m = 0

def bowling(target=None):
    """Computer Bats, Player Bowls"""
    global total_run_c
    print("\nStart Bowling")
    RUNS = [1, 2, 3, 4, 5, 6]
    comp_total = 0

    while True:
        comp_run = random.choice(RUNS)
        my_bowl = int(input("Enter your bowl (1-6): "))

        if my_bowl not in RUNS:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        print(f"Computer scored: {comp_run}")

        if comp_run == my_bowl:
            print("Computer is out!")
            break
        else:
            comp_total += comp_run

        # If chasing, check if computer has reached the target
        if target is not None and comp_total > target:
            print(f"Computer chased the target successfully with {comp_total} runs!")
            total_run_c = comp_total
            return True  # Computer wins

    total_run_c = comp_total
    print(f"Computer's total score: {total_run_c}")
    return False  # Computer does not win yet

def batting(target=None):
    """Player Bats, Computer Bowls"""
    global total_run_m
    print("\nStart Batting")
    RUNS = [1, 2, 3, 4, 5, 6]
    my_total = 0

    while True:
        comp_bowl = random.choice(RUNS)
        my_run = int(input("Enter your run (1-6): "))

        if my_run not in RUNS:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        print(f"Computer bowled: {comp_bowl}")

        if my_run == comp_bowl:
            print("You are out!")
            break
        else:
            my_total += my_run

        # If chasing, check if player has reached the target
        if target is not None and my_total > target:
            print(f"You chased the target successfully with {my_total} runs! You win!")
            total_run_m = my_total
            return True  # Player wins

    total_run_m = my_total
    print(f"Your total score: {total_run_m}")
    return False  # Player does not win yet

def defend():
    """Player bats first, then the computer chases"""
    batting()
    print(f"\nComputer needs {total_run_m + 1} runs to win.")
    computer_wins = bowling(total_run_m)

    if not computer_wins:
        print("You successfully defended your total! You win!")  # If computer fails
    else:
        print("Computer won the match!")

def chasing():
    """Computer bats first, then the player chases"""
    computer_wins = bowling()
    print(f"\nYou need {total_run_c + 1} runs to win.")

    if not computer_wins:
        player_wins = batting(total_run_c)
        if player_wins:
            print("You won the match!")  # If player chases successfully
        else:
            print("Computer successfully defended its score! Computer wins!")  # If player fails

# Toss
coin = [1, 2]
coin_ans = random.choice(coin)
toss = int(input("Choose 1 for Heads and 2 for Tails: "))

if toss == coin_ans:
    print("You won the toss!")
    choice = int(input("Choose 1 to Bat or 2 to Bowl: "))

    if choice == 1:
        print("You chose to Bat first.")
        defend()
    elif choice == 2:
        print("You chose to Bowl first.")
        chasing()
    else:
        print("Invalid choice. Defaulting to Batting.")
        defend()
else:
    print("Computer won the toss.")

    comp_choice = random.choice([1, 2])
    if comp_choice == 1:
        print("Computer chose to Bat first.")
        chasing()
    else:
        print("Computer chose to Bowl first.")
        defend()
