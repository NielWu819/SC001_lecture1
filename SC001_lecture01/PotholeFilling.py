"""
File: PotholeFilling.py
Name: Niel wu
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def put_99_beepers():
    """ Karel put 99 beepers """
    i = 0
    while i < 99:
        put_beeper()
        i = i + 1

def go_in():
    """
    pre-condition:Karel is at the upper left of the pathole, facing East
    post-condition:Karel is in the pathole, facing South
    """
    move()
    turn_right()
    move()

def go_out():
    """
    pre-condition:Karel is in the pathole, facing South
    post-condition:Karel is at the upper left of the pathole, facing East
    """
    turn_around()
    move()
    turn_right()
    move()


def main():
    """
    Karel put beepers in the pothole
    """
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
