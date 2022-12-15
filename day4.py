# imports
from icecream import ic
import constants

# constants
DAY = 4
DEBUG_DATA = False
DEBUG = False
if not DEBUG:
    ic.disable()

# open file
file = constants.open_file(DAY, DEBUG_DATA)
text = file.readlines()
line_count = text.__len__()


# def
def fully_contained(a):
    ic(int(a[0]), int(a[1]), int(a[2]), int(a[3]))
    ic(int(a[0]) <= int(a[2]) and int(a[1]) >= int(a[3]))
    ic(int(a[0]) <= int(a[2]))
    ic(int(a[1]) >= int(a[3]))
    ic(int(a[2]) <= int(a[0]) and int(a[3]) >= int(a[1]))
    ic(int(a[2]) <= int(a[0]))
    ic(int(a[3]) >= int(a[1]))
    if int(a[0]) <= int(a[2]) and int(a[1]) >= int(a[3]):
        return True
    if int(a[2]) <= int(a[0]) and int(a[3]) >= int(a[1]):
        return True


def overlap(a):
    ic(int(a[0]), int(a[1]), int(a[2]), int(a[3]))
    ic(int(a[1]) >= int(a[2]) and int(a[3]) >= int(a[0]))
    ic(int(a[1]) >= int(a[2]) and int(a[3]) >= int(a[0]))
    if int(a[1]) >= int(a[2]) and int(a[3]) >= int(a[0]):
        return True


# var
data = {}
sol1 = 0
sol2 = 0

if __name__ == '__main__':
    
    # main program part 1
    for line in range(line_count):
        san = text[line].replace('\n', '')
        spl = san.split(',')
        spl2 = spl[0].split('-')
        spl3 = spl[1].split('-')
        data.update({line: [spl2[0], spl2[1], spl3[0], spl3[1]]})
        if fully_contained(data[line]):
            sol1 += 1
    
    # main program part 2
    for line in range(line_count):
        if overlap(data[line]):
            sol2 += 1
    
    # print solution
    if DEBUG:
        ic("DEBUG")
        # ic(data)
    print("sol1: ", sol1)
    print("sol2: ", sol2)
    
    # end of program reached
    print("end of program reached")
