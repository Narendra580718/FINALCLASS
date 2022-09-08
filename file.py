import random
winning_number = random.randint(0,100)

print(winning_number)

user_provided_number = int(input("Enter your number: "))

def guessing_function(user_provided_number):
    game_over = False
    guess_counter = 1
    while not game_over:
        if winning_number == user_provided_number:
            print(f"Correct answer in {guess_counter} {'st guess' if guess_counter==1 else 'times'}")
            game_over = True
        else:
            if user_provided_number > winning_number:
                print("Your number is too high.")
            else:
                print("Your number is too low.")
            guess_counter += 1
            user_provided_number = int(input("Try again:"))
            
guessing_function(user_provided_number)
