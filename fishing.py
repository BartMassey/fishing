# Copyright © 2013 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

# Simple fishing game

# Player repeatedly casts and gets fish
# with different likelihoods and point values.

import random

catches = [
    ("minnow", 40, 2),
    ("haddock", 10, 10),
    ("lobster", 5, 20),
    ("golden boot", 1, 100) ]

def cast():
    selection = random.randrange(100)
    for c in catches:
        if selection < c[1]:
            print("You reel in a", c[0],
                  "for", c[2], "points!")
            return c[2]
        selection -= c[1]
    print("After a while, you reel in, empty-handed.")
    return 0

score_file_name = "scores.txt"

def read_score_file():
    try:
        score_file = open(score_file_name, "r+")
        high_score = int(score_file.readline())
        score_file.close()
    except IOError:
        high_score = 0
        write_score_file(high_score)
    return high_score

def write_score_file(high_score):
    score_file = open(score_file_name, "w")
    score_file.write(str(high_score) + "\n")
    score_file.close()

def game():
    score = 0
    high_score = read_score_file()
    print("High score to date: ", high_score)
    while True:
        command = input("Fish! ")
        if command == "quit":
            break
        elif command in ["cast", ""]:
            cast_score = cast()
            score += cast_score
            if cast_score > 0:
                print("Your score is now", score)
            if score > high_score:
                print("A new high score!")
                high_score = score
                write_score_file(high_score)
        else:
            print("I do not understand you fully.")
        print()

# Testing function
def test():
    for i in range(1000):
        cast()

game()
