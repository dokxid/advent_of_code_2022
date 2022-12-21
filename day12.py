# imports
from icecream import ic

import constants

# constants
DAY = 12
DEBUG_DATA = True
DEBUG = True
if not DEBUG:
    ic.disable()

# open file
file = constants.open_file(DAY, DEBUG_DATA)
text = file.readlines()
text = list(map(constants.sanitize, text))
line_count = text.__len__()

# var
sol1 = 0
sol2 = 0
data = {}
    

class Parser:
    
    def __init__(self, text_parse: list[str]):
        self.text_parse = text_parse
        self.len = text_parse.__len__()
        
    def parse(self):
        return 0


def part_1():
    return 0


def part_2():
    return 0
    

if __name__ == '__main__':
    
    # parse
    p = Parser(text)
    p.parse()
    
    # main program
    sol1 = part_1()
    sol2 = part_2()
    
    # print solution
    if DEBUG:
        ic("DEBUG")
        ic(data)
    print("sol1: ", sol1)
    print("sol2: ", sol2)
    
    # end of program reached
    print("end of program reached")
    