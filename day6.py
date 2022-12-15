# imports
from icecream import ic
import constants

# constants
DAY = 6
PART = 2
DEBUG_DATA = False
DEBUG = False
if not DEBUG:
    ic.disable()

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
    if PART == 1:
        for line in range(line_count):
            for char in range(text[line].__len__() - 4 + 1):
                temp = text[line][char:char + 4]
                j = 0
                ic(char + 4, temp)
                for i in range(4):
                    ic(temp.rfind(temp[i]) == temp.find(temp[i]) and temp.find(temp[i]) != -1)
                    if temp.rfind(temp[i]) == temp.find(temp[i]) and temp.find(temp[i]) != -1:
                        j += 1
                        ic("only 1 found", j)
                    else:
                        ic("DUPLICATE", j)
                if j == 4:
                    ic("MARKER FOUND", char + 4)
                    sol1 = char + 4
                    break
    
    # main program part 2
    if PART == 2:
        for line in range(line_count):
            for char in range(text[line].__len__() - 14 + 1):
                temp = text[line][char:char + 14]
                j = 0
                ic(char + 14, temp)
                for i in range(14):
                    ic(temp.rfind(temp[i]) == temp.find(temp[i]) and temp.find(temp[i]) != -1)
                    if temp.rfind(temp[i]) == temp.find(temp[i]) and temp.find(temp[i]) != -1:
                        j += 1
                        ic("only 1 found", j)
                    else:
                        ic("DUPLICATE", j)
                if j == 14:
                    ic("MARKER FOUND", char + 14)
                    sol1 = char + 14
                    break
    
    # print solution
    if DEBUG:
        ic("DEBUG")
        ic(data)
    print("sol1: ", sol1)
    print("sol2: ", sol2)
    
    # end of program reached
    print("end of program reached")
