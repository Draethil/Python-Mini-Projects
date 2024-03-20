import random

def guessUser(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if random_number > guess:
            print("Your number is too Low!")
        elif random_number < guess:
            print("Your number is too High!")

    print(f"You win! The Number was {random_number}!!")

def guessComputer(x):
    lowBorder = 1
    highBorder = x
    feedback = ""

    while feedback != 'c':
        takeGuess = random.randint(lowBorder, highBorder)
        feedback = input(f"Is {takeGuess} too low (l), too high (h), or correct (c)? ")
        if feedback == "l":
            lowBorder = takeGuess + 1
        elif feedback == "h":
            highBorder = takeGuess - 1
    
    print(f"Congrats, the Computer won!")

guessComputer(10)