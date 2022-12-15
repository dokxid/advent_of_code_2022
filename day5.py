# imports
from icecream import ic
import constants
from constants import sanitize

# constants
DAY = 5
PART = 2
DEBUG_DATA = False
DEBUG = True
if not DEBUG:
    ic.disable()

# open file
file = constants.open_file(DAY, DEBUG_DATA)
text = file.readlines()
line_count = text.__len__()

# var
sol1 = 0
data = {}


def stack_amount(t: list[str]):
    return t[stack_line(t)][t[stack_line(t)].__len__()-2]


def stack_line(t: list[str]):
    for li in range(line_count):
        for ch in range(t[li].__len__()):
            if t[li][ch].isdigit():
                return li
            
            
def extract_col_to_data(t: list[str]):
    col_data = []
    for li in range(stack_line(t)):
        for ch in range(t[li].__len__()):
            if t[li][ch].isalpha():
                col_data.append([li, ch, t[li][ch]])
    return col_data
    
    
def take_col_element(list_elements):
    return list_elements[1]
    

def calc_stack(a: int):
    return int((a - 1) / 4) + 1


def col_to_stack(a):
    data_col = {}
    a.sort(key=take_col_element)
    for i in range(a.__len__()):
        if data_col.get(calc_stack(a[i][1])) is None:
            data_col.update({calc_stack(a[i][1]): [a[i][2]]})
        else:
            data_col.get(calc_stack(a[i][1])).append(a[i][2])
    return data_col


if __name__ == '__main__':
    
    # parse data
    ic(extract_col_to_data(text))
    
    # main program part 1
    if PART == 1:
        move_cmd, from_cmd, to_cmd = 0, 0, 0
        stacks = col_to_stack(extract_col_to_data(text))
        temp_line = 1 + stack_line(text)
        ic(temp_line)
        ic(stacks)
        for i in range(line_count - temp_line - 1):
            san = sanitize(text[i+temp_line+1])
            # ic(san[5:san.find("from")-1])
            # ic(san[san.find("from")+5:san.find("to")-1])
            # ic(san[san.find("to")+3:san.__len__()])
            move_cmd = int(san[5:san.find("from")-1])
            from_cmd = int(san[san.find("from")+5:san.find("to")-1])
            to_cmd = int(san[san.find("to")+3:san.__len__()])
            data.update({i: [move_cmd, from_cmd, to_cmd]})
        for i in data:
            ic(data[i][0], data[i][1], data[i][2])
            for j in range(data[i][0]):
                if stacks.get(data[i][1]).__len__() != 0:
                    stacks.get(data[i][2]).insert(0, stacks.get(data[i][1]).pop(0))
            ic(stacks)
        
    # main program part 2
    if PART == 2:
        move_cmd, from_cmd, to_cmd = 0, 0, 0
        stacks = col_to_stack(extract_col_to_data(text))
        temp_line = 1 + stack_line(text)
        ic(temp_line)
        ic(stacks)
        for i in range(line_count - temp_line - 1):
            san = sanitize(text[i+temp_line+1])
            # ic(san[5:san.find("from")-1])
            # ic(san[san.find("from")+5:san.find("to")-1])
            # ic(san[san.find("to")+3:san.__len__()])
            move_cmd = int(san[5:san.find("from")-1])
            from_cmd = int(san[san.find("from")+5:san.find("to")-1])
            to_cmd = int(san[san.find("to")+3:san.__len__()])
            data.update({i: [move_cmd, from_cmd, to_cmd]})
        for i in data:
            ic(data[i][0], data[i][1], data[i][2])
            temp = []
            for j in range(data[i][0]):
                if stacks.get(data[i][1]).__len__() != 0:
                    temp.insert(0, stacks.get(data[i][1]).pop(0))
            for k in range(temp.__len__()):
                stacks.get(data[i][2]).insert(0, temp[k])
            ic(stacks)
    
    # print solution
    if DEBUG:
        ic("SOLUTION DEBUG")
        ic(data)
        ic(stacks)
    print("sol1: ", sol1)
    
    # end of program reached
    print("end of program reached")
