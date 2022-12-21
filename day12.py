# imports
from icecream import ic
from treelib.tree import *
from constants import *

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
        f = open_file(DAY, DEBUG_DATA)
        t = f.readlines()
        t = list(map(sanitize, t))
        return t


def part_1(f):
    
    # find S
    s = find_char('S', f, DEBUG)
    e = find_char('E', f, DEBUG)
    ic(s, e)
    
    # convert field to correct heatmap
    f[s[0]] = f[s[0]].replace('S', 'a')
    f[e[0]] = f[e[0]].replace('E', 'z')
    for line in range(len(f)):
        f[line] = list(map(ord, f[line]))
    
    # store paths
    paths = Tree()
    paths.ROOT = e
    
    # return and debug
    ic(field)
    print(paths.show())
    return 0


def part_2(f):
    
    # logic
    
    # return
    return 0
    

if __name__ == '__main__':
    
    # parse
    field = Parser.parse()
    
    # main program
    sol1 = part_1(field)
    sol2 = part_2(field)
    
    # print solution
    if DEBUG:
        ic("DEBUG")
    print("sol1: ", sol1)
    print("sol2: ", sol2)
    
    # end of program reached
    print("end of program reached")
    