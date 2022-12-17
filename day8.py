# --- Day 8: Treetop Tree House ---
#
# The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that
# a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good
# location for a tree house.
#
# First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count
# the number of trees that are visible from outside the grid when looking directly along a row or column.
#
# The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input).
# For example:
#
# 30373
# 25512
# 65332
# 33549
# 35390
#
# Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.
#
# A tree is visible if all the other trees between it and an edge of the grid are shorter than it. Only consider
# trees in the same row or column; that is, only look up, down, left, or right from any given tree.
#
# All the trees around the edge of the grid are visible - since they are already on the edge, there are no trees
# to block the view. In this example, that only leaves the interior nine trees to consider:
#
# The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of
# height 5 are in the way.) The top-middle 5 is visible from the top and right. The top-right 1 is not visible from
# any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge. The
# left-middle 5 is visible, but only from the right. The center 3 is not visible from any direction; for it to be
# visible, there would need to be only trees of at most height 2 between it and an edge. The right-middle 3 is
# visible from the right. In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
#
# With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this
# arrangement.
#
# Consider your map; how many trees are visible from outside the grid?


# imports
from icecream import ic
import constants

# constants
DAY = 8
PART = 1
DEBUG_DATA = True
DEBUG = True
if not DEBUG:
    ic.disable()

# open file
file = constants.open_file(DAY, DEBUG_DATA)
text = file.readlines()
line_count = text.__len__()

# var
OUTER_TREES_COUNT = line_count * 4 - 4  # (n * 4 - 4)
sol1 = 0
sol2 = 0
data = []
data_bool = []


def visible_trees(a: list):
    for i in range(a.__len__()-1):
        if a[i+1] <= a[i]:
            return i
    return a.__len__()


if __name__ == '__main__':
    
    # parse
    for line in range(line_count):
        data.append([])
        data_bool.append([])
        for char in constants.sanitize(text[line]):
            data[line].append(char)
            data_bool[line].append(False)
        
    # main program part 1
    for i in range(line_count):
        ic(data[i])
        ic(visible_trees(data[i]))
    
    # print solution
    if DEBUG:
        ic("DEBUG")
        ic(OUTER_TREES_COUNT)
        ic(data)
        ic(data_bool)
    print("sol1: ", sol1)
    print("sol2: ", sol2)
    
    # end of program reached
    print("end of program reached")
