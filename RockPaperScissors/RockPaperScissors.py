import random

def startGame():
    user = input(f"Choose 1: Rock (r), Paper (p) or Scissors (s)! ")
    computer = random.choice(["r", "p", "s"])

    # Testing
    print(f"Computer: {computer}; Player: {user}")

    if user == computer:
        return "It's a tie!"
    
    if is_win(user, computer) == True:
       return "The Player Won!"

    return "The Computer won!"


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r

    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

print(startGame())
  