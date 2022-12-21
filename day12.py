# imports
from icecream import ic
from treelib.tree import *

import constants

# constants
DAY = 12
DEBUG_DATA = True
DEBUG = True
if not DEBUG:
    ic.disable()

# var
sol1 = 0
sol2 = 0
data = {}
field = []


class Parser:
    
    def __init__(self, text_parse: list[str]):
        self.text_parse = text_parse
        self.len = text_parse.__len__()
        
    @staticmethod
    def parse():
        # open file
        f = constants.open_file(DAY, DEBUG_DATA)
        t = f.readlines()
        t = list(map(constants.sanitize, t))
        return t


def part_1():
    
    # find S
    for r in field:
        index = r.find("S")
        if index != -1:
            if DEBUG: print("found S in: {}, position {}".format(field.index(r), index))
            break
    
    path = Tree()
    
    # return
    return 0


def part_2():
    
    # logic
    
    # return
    return 0
    

if __name__ == '__main__':
    
    # parse
    field = Parser.parse()
    
    # main program
    sol1 = part_1()
    sol2 = part_2()
    
    # print solution
    if DEBUG:
        ic("DEBUG")
        ic(field)
    print("sol1: ", sol1)
    print("sol2: ", sol2)
    
    # end of program reached
    print("end of program reached")
    