# Copyright © 2013 Bart Massey
# Simple fishing game

# Player repeatedly casts and gets fish
# with different likelihoods and point values

import random

catches = [
    ("minnow", 40, 2),
    ("haddock", 10, 10),
    ("lobster", 5, 20),
    ("golden boot", 1, 100) ]

def cast():
    selection = random.randrange(100)
    cumulative = 0
    for c in catches:
        if c[1] + cumulative > selection:
            print("You reel in a", c[0],
                  "for", c[2], "points!")
            return c[2]
        cumulative += c[1]
    print("After a while, you reel in, empty-handed.")
    return 0

def game():
    # The current score of the currently-playing player.
    score = 0
    while True:
        command = input("Fish! ")
        if command == "quit":
            break
        elif command in ["cast", ""]:
            cast_score = cast()
            score += cast_score
            if cast_score > 0:
                print("Your score is now", score)
        else:
            print("I do not understand you fully.")
        print()

# Testing function
def test():
    for i in range(1000):
        cast()

game()
