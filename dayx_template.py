# imports
from icecream import ic
import constants

# constants
DEBUG_DATA = True
DEBUG = True
DAY = 0

# open file
file = constants.open_file(DAY, DEBUG_DATA)
text = file.readlines()
line_count = text.__len__()

# var
sol1 = 0
sol2 = 0
data = {}


if __name__ == '__main__':
    
    # main program part 1
    for line in range(line_count):
        sol1 = 0  # TODO
    
    # main program part 2
    for line in range(line_count):
        sol2 = 0  # TODO
    
    # print solution
    if DEBUG:
        ic("DEBUG")
        ic(data)
    ic(sol1)
    ic(sol2)
    
    # end of program reached
    print("end of program reached")
