"""Forest Fire Sim, modified by Andrew Olague for Module 6
Based on a program by Al Sweigart and modified by Sue Sampson.
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation
"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# --------------------------------------------------------------
# CONSTANTS
# --------------------------------------------------------------
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # New water feature, acts as a firebreak

# Probability settings (0.0 to 1.0)
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01           # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01           # Chance a tree is hit by lightning & burns.

# Simulation timing
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'], 'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    continue  # Skip already updated positions

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE

                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE

                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Fire spreads to neighboring trees, but not across water.
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY

                elif forest[(x, y)] == WATER:
                    # Water never changes - acts as a firebreak.
                    nextForest[(x, y)] = WATER

                else:
                    # Copy existing object.
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.

    # ----------------------------------------------------------
    # Added Lake Feature (Module 6 - Andrew Olague)
    # The lake acts as a firebreak that flames cannot cross.
    # ----------------------------------------------------------
    lake_width = 15
    lake_height = 5
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    for x in range(center_x - lake_width // 2, center_x + lake_width // 2):
        for y in range(center_y - lake_height // 2, center_y + lake_height // 2):
            forest[(x, y)] = WATER  # Place water in the middle

    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            space = forest[(x, y)]
            if space == TREE:
                bext.fg('green')
            elif space == FIRE:
                bext.fg('red')
            elif space == WATER:
                bext.fg('blue')
            else:
                bext.fg('black')
            print(space, end='')
        print()
    bext.fg('reset')
    print('Ctrl-C to quit.', end='')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()


