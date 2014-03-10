# Copyright (c) 2011 Bart Massey
# A Fishing Game
# This work is available under the "MIT License". Please see the
# file COPYING in this distribution for license details.

import random
import shelve
from sys import exit

# Initialize the PRNG
random.seed()

# The scorefile is kept as a dictionary mapping
# username to score, stored in a "shelf".
user_scores = shelve.open("fishing")

def register(username):
    "Register a new, legal username."
    for c in username:
        if not (c.isalpha() or c.isdigit() or c in "_-"):
            print("illegal character in username " + \
                  "(legal are A-Za-z0-9_-)")
            return
    if username in user_scores:
        print("username already registered")
        return
    user_scores[username] = 0
    user_scores.sync()

# The username of the current fisher
fisher = None

def fish(username):
    "Set the fisher to an existing username."
    global fisher
    if not (username in user_scores):
        print("username unknown")
        return
    fisher = username

def fisher_score():
    global fisher
    print("Your current score is " + str(user_scores[fisher]))

# Dictionary of fishes keyed by fish and contents
# a two-tuple indicating the percent probability and
# the score of that fish.
fishes = (
    (None, 20, 0),
    ("Minnow", 20, 10),
    ("Bluegill", 30, 30),
    ("Bass", 15, 100),
    ("Trout", 10, 200),
    ("Salmon", 4, 500),
    ("Gold Boot", 1, 5000) )

def cast_result():
    """
    Get the result of a cast. Returns a tuple of fish
    description and cast score.
    """
    catch = random.randrange(100)
    for (fish, percent, score) in fishes:
        catch -= percent
        if catch < 0:
            return (fish, score)
    assert False

def fish_name(fish):
    "Return canonical name of a fish."
    if fish == None:
        return "nothing"
    return "a " + fish

def cast():
    "Cast the fisher's rod."
    global fisher
    if fisher == None:
        print('Use the "fish" command to choose a fisher.')
        return
    (fish, score) = cast_result()
    print("You have caught ", end="")
    if fish == None:
        print(fish_name(fish) + ".")
        return
    print("a " + fish_name(fish) + "!")
    print("It is worth " + str(score) + " points.")
    user_scores[fisher] += score
    user_scores.sync()
    fisher_score()

def scores():
    "Show everyone's score."
    global fisher
    if fisher != None:
        fisher_score()
        print("")
    print("All scores:")
    for u in user_scores:
        print(u + ": " + str(user_scores[u]))

def quit():
    "Quit the game."
    scores()
    user_scores.close()
    exit()

def help():
    "Show help."
    print("""
    register <username>: Register a new fisher named username
    fish <username>: Start username fishing
    cast: Try to catch a fish
    scores: Find out everyone's score
    quit: Quit the game
    help: This help
    """)

def test():
    "Test the fishing algorithm."
    counts = {}
    for (fish, _, _) in fishes:
        counts[fish] = 0
    for i in range(10000):
        (fish, _) = cast_result()
        counts[fish] += 1
    for fish in counts:
        print(fish_name(fish) + ": " + str(counts[fish]))

# Fishing commands. Each command comes with its argument
# count and its function.
commands = { "register" : (1, register),
             "fish" : (1, fish),
             "cast" : (0, cast),
             "scores" : (0, scores),
             "quit" : (0, quit),
             "help" : (0, help),
             "test" : (0, test) }

# The main loop
print('Fishing! Please enter fishing commands. "help" for help.')
while True:
    words = []
    while words == []:
        try:
            cmd = input("> ")
        except EOFError:
            print("quit")
            cmd = "quit"
        words = cmd.split()
    if words[0] in commands:
        (nargs, cmd_fun) = commands[words[0]]
        if len(words) - 1 != nargs:
            print("Wrong number of arguments to command. Please try again")
            continue
        if nargs == 0:
            cmd_fun()
        elif nargs == 1:
            cmd_fun(words[1])
        else:
            assert False
        continue
    print("Unknown fishing command. Please try again.")
