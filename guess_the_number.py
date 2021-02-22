import random

def guess_number(winning_answer):
  lose = True

  while lose == True:
    users_guess = int(input("Guess a number between 1 and 100:\n"))

    if users_guess > winning_answer:
      print("Try again! You guessed too high!")
    elif users_guess < winning_answer:
      print("Try again! You guessed too low!")
    else:
      print(f"You got it! The answer was {winning_answer}")
      lose = False


winning_answer = random.randint(1, 101)
guess_number(winning_answer)