# Fishing
Copyright &copy; 2014 Bart Massey  
2014-03-10

This is a very simple little fishing game that I wrote as a
class demo with my Intro Programming in Python class in
2011.

Invoke the game with "python3 fishing.py". When it tells you
to "Prepare to fish!", say "fisher" and your fisher name,
for example "fisher Alice".

When the game tells you to "Fish!", you can hit return or
say "cast" to cast, or you can say "quit" to quit. Your high
score is tracked.

  * When the user starts up the program, it reads commands
    from the user and then executes them.

  * The available commands are:

                register <username>
                    Register a new user named <username>.
                    Usernames should include only letters,
                    numbers, and the characters '-' and '_'.
                fish <username>
                    Starts fishing as user <username>
                cast
                    The current user tries to catch a fish,
                    as detailed below.  The "cast" command
                    refuses to work if there is no current
                    fisher.
                scores
                    List the user's score, then
                    the scores of all registered users.
                quit
                    Quit the program. The program should
                    run the "scores" command on the way out.
                help
                    List the fishing commands and their effects.

    If the user "ends input" (`input()` raises an
    `EOFError`) this is treated as a quit command. If the user
    enters an empty command (blank line) it is ignored.
    Otherwise, an error is given for any input that is not a
    valid command, and the user is allowed to continue fishing.

  * When the "cast" command is issued, the program decides
    what is caught and how it is scored based on the
    following table:

    > <table><tr><th>Fish</th><th>Chance</th><th>Score</th></tr>
    > <tr><td>Nothing</td><td>20%</td><td>0</td></tr>
    > <tr><td>Minnow</td><td>20%</td><td>10</td></tr>
    > <tr><td>Bluegill</td><td>30%</td><td>30</td></tr>
    > <tr><td>Bass</td><td>15%</td><td>100</td></tr>
    > <tr><td>Trout</td><td>10%</td><td>200</td></tr>
    > <tr><td>Salmon</td><td>4%</td><td>500</td></tr>
    > <tr><td>Gold Boot</td><td>1%</td><td>5000</td></tr></table>

    The program responds to the cast command by
    showing what is caught, how much it is worth, and
    the user's current score.

  * The program saves the scores on disk. The scores are
    loaded and saved using "shelving" of scores keyed by
    username. A shelf with the filename "fishing" is used.
    The score shelf file is always current.

  * Each command is implemented as a separate function that
    is called from the main loop.

A testing command is included; it casts 10000 times and
reports the percentages of fish caught. This convinced me my
catch algorithm was working.

-----

Future work:

  * Add some other fish and adjust the probabilities. Be
    creative.

  * Randomize the catch text to add interest. Make the catch
    text dependent on the type and score of the fish caught
    in interesting ways.

  * Implement the *achievement* "Caught the Gold Boot", and
    any other achievements you can think of. My achievement
    idea: "'One Fish, Two Fish, Red Fish, Blue Fish': Caught
    a Salmon followed by two Bluegill". OFTFRFBF is
    completed only 9% of the time after you have caught a
    Salmon, and catching a Salmon is only 4%, making this
    achievement pretty unlikely.

-----

Fishing is available under the "MIT License". Please see the
file COPYING in this distribution for license details.
