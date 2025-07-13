import random

def choosing_level():
        #choosing the difficulty level
    print("Please choose the difficulty level number: "\
    "\n1-Easy (guessing range from 0 to 10, num of trials = 3)" \
    "\n2-Medium (guessing range from 0 to 100, num of trials = 7)" \
    "\n3-Hard (guessing range from 0 to 1000, num of trials = 10)")

    level = int(input(""))

    if level == 1:
        play_guessing_game(3,0,10)   
    elif level == 2:
        play_guessing_game(7,0,100)
    elif level == 3:
        play_guessing_game(10,0,1000)
    else:
        print("Please choose a number from 1 to 3.")

def play_guessing_game(n_trials,lower_num,upper_num):
    original_number = random.randint(lower_num,upper_num)
    #trials loop 
    while n_trials > 0: 
        user_guess = int(input("I have a hidden number, guess it : "))
        if user_guess == original_number:
            print(f"ohhh your guess is correct. ")
            break
        elif user_guess > original_number:
            print("No, Decrease!")
        elif user_guess < original_number:
            print("No, Increase!")
        n_trials-=1
    if n_trials == 0 and user_guess != original_number:
        print("Sorry, you lost! You've run out of trials.")
        print(f"The hidden number was: {original_number}")

choosing_level()
