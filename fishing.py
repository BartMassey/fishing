# Copyright (c) 2011 Bart Massey
# A Fishing Game

import random
import shelve
from sys import exit

# Initialize the PRNG
random.seed()

# The scorefile is kept as a dictionary mapping
# username to score, stored in a "shelf".
users = shelve.open("fishing")

# Register a new, legal username
def register(username):
    for c in username:
        if not c.isalpha() and not c.isdigit() and not c in "_-":
            print("illegal character in username")
            return
    if username in users:
        print("username already registered")
        return
    users[username] = 0
    users.sync()

# The username of the current fisher
fisher = None

# Set the fisher to an existing username
def fish(username):
    global fisher
    if not (username in users):
        print("username unknown")
        return
    fisher = username

def fisher_score():
    global fisher
    print("Your current score is " + str(users[fisher]))

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

# Get the result of a cast. Returns a tuple of fish
# description and cast score.
def cast_result():
    catch = random.randrange(100)
    for (fish, percent, score) in fishes:
        catch -= percent
        if catch < 0:
            if fish == None:
                return ("nothing", score)
            return ("a " + fish, score)
    raise AssertionError("internal error: bad fishing cast")

# Cast the fisher's rod
def cast():
    global fisher
    if fisher == None:
        print('Use the "fish" command to choose a fisher.')
        return
    (fish, score) = cast_result()
    print("You have caught ", end="")
    if fish == "nothing":
        print("nothing.")
        return
    print(fish + "!")
    print("It is worth " + str(score) + " points.")
    users[fisher] += score
    users.sync()
    fisher_score()

# Show everyone's score
def scores():
    global fisher
    if fisher != None:
        fisher_score()
        print("")
    print("All scores:")
    for u in users:
        print(u + ": " + str(users[u]))

# Quit the game
def quit():
    scores()
    users.close()
    exit()

# Show help
def help():
    print("""
    register <username>: Register a new fisher named username
    fish <username>: Start username fishing
    cast: Try to catch a fish
    scores: Find out everyone's score
    quit: Quit the game
    help: This help
    """)

# Test the fishing algorithm
def test():
    counts = {}
    for i in range(10000):
        (fish, score) = cast_result()
        if fish in counts:
            counts[fish] += 1
        else:
            counts[fish] = 0
    for fish in counts:
        print(fish + ": " + str(counts[fish]))

# Fishing commands. Each command comes with its argument
# count and its function.
commands = { "register" : (2, register),
             "fish" : (2, fish),
             "cast" : (1, cast),
             "scores" : (1, scores),
             "quit" : (1, quit),
             "help" : (1, help),
             "test" : (1, test) }

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
        if len(words) != nargs:
            print("Wrong number of arguments to command. Please try again")
            continue
        if nargs == 1:
            cmd_fun()
        elif nargs == 2:
            cmd_fun(words[1])
        else:
            raise AssertionError("internal error: bogus argument count")
        continue
    print("Unknown fishing command. Please try again.")
