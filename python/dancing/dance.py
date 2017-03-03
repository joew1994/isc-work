#question 1

"""
dance.py
========

Contains the infamous "boogie" function used to generate fantastic
fun at the disco.

"""

# Standard library imports
import time
import random

# Define some dance moves
moves = ["Mash Potato", "Hippy Hippy Shake", "Back flip", "Cha Cha Cha",
         "Mosh", "Slam Dive", "Waltz"]

def boogie(dance_moves):# we are defining the function 'boogie'
    """
    This programme dances!
    """
    these_moves = moves + dance_moves #this was some bad code I commented out
    these_moves=moves #corrected it so that the loop will play from the list 'moves'
    print 'these_moves are ', these_moves #prints the list of possible moves

    for count in range(1, 5): # start loop and define count as a variable - as its a loop it takes the first value from the range 1-5
        print count # prints this value of count
        time.sleep(3.0) #from the library 'time' it imports the sleep function that pauses the loop momentarily for a designated time - 3 seconds

    print "GO!" # prints GO
    for i in range(50): # new loop defining i as a variable in the range of 0-49
        index = random.randint(0, len(these_moves) - 1) # index is new variable and is defined as the randomly selected move (between 0 and -1 of the strings in the list) from 'these moves' via the function randint from the library random. 
        print these_moves[index] # prints this move 
        time.sleep(0.3) # again pauses the loop before it restarts again.

#question 2



