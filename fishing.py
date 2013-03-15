# Copyright © 2013 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

# Simple fishing game

# Player repeatedly casts and gets fish
# with different likelihoods and point values.

import random

score_file_name = "scores.txt"

catches = [
    ("minnow", 40, 2),
    ("haddock", 10, 10),
    ("lobster", 5, 20),
    ("golden boot", 1, 100) ]

# Current fisher.
fisher = None
# Current fisher's current score.
score = 0

# All-time high score fisher.
high_score_fisher = None
# All-time high score.
high_score = 0

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

def read_score_file():
    global high_score, high_score_fisher
    try:
        score_file = open(score_file_name, "r+")
        score_entry = score_file.readline().split()
        high_score = int(score_entry[0])
        if len(score_entry) > 1:
            high_score_fisher = score_entry[1]
        score_file.close()
    except IOError:
        high_score = 0
        write_score_file()

def write_score_file():
    if fisher == None:
        return
    score_file = open(score_file_name, "w")
    score_file.write(str(high_score) + " " + fisher + "\n")
    score_file.close()

def one_cast():
    if fisher == None:
        print("Use the \"fisher\" command before fishing.")
        return
    global score, high_score
    cast_score = cast()
    score += cast_score
    if cast_score > 0:
        print("Your score is now", score)
        if score > high_score:
            print("A new high score!")
            high_score = score
            write_score_file()

def game():
    read_score_file()
    if high_score_fisher == None:
        print("High score to date:", high_score)
    else:
        print("High score to date:", high_score, "by", high_score_fisher)
    print()
    while True:
        global fisher
        if fisher == None:
            prompt = "Prepare to fish! "
        else:
            prompt = "Fish! "
        try:
            command = input(prompt).split()
        except EOFError:
            print()
            break
        if command == ["quit"]:
            break
        elif command in [["cast"], []]:
            one_cast()
        elif command[0] == "fisher":
            if len(command) == 2:
                fisher = command[1]
            else:
                print("Say \"fisher\" and your fishername. " +
                      "For example, \"fisher alice\".")
        else:
            print("I do not understand you fully.")
        print()
    print()
    print("Your final score this session:", score)
    print("Thanks for fishing!")

# Testing function
def test():
    for i in range(1000):
        cast()

game()
