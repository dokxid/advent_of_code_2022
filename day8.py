# task: https://adventofcode.com/2022/day/8

# imports
from icecream import ic
import constants

# constants
DAY = 8
PART = 2
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


# ignores outer trees
def visible_trees(a: list) -> list[bool]:
    temp_highest = -1
    j = []
    for i in range(a.__len__()):
        if int(a[i]) > temp_highest:
            temp_highest = int(a[i])
            j.append(True)
        else:
            j.append(False)
    return j


def distance_trees(a: list) -> int:
    
    # sanitize list[str] to list[int]
    if a[0].__class__ == str:
        a = list(map(int, a))
    
    # catch edge
    if a.__len__() == 1:
        return 0
    
    start_point = a[0]
    trees = a[1:]
    distance = 0
    highest = -1
    # ic(start_point, trees)
    
    if start_point >= trees[0]:
        for i in trees:
            if i >= highest:
                highest = i
                distance += 1
        if highest == trees[0]:
            return trees.__len__()
    else:
        for i in trees:
            if i >= highest:
                highest = i
                distance += 1
        if highest == trees[0]:
            return 1
    
    return distance


def mark(op: list[bool], mut: list[list[bool]], index, col=False, rev=False) -> None:
    assert op.__len__() == mut[index].__len__()
    # TODO: implement index, col
    if rev:
        op.reverse()
    for i in range(op.__len__()):
        if op[i] is True:
            if col:
                mut[i][index] = True
            else:
                mut[index][i] = True
            
            
def count_true(a: list) -> int:
    two_arr = []
    if not a[0].__class__ == list:
        two_arr.append(a)
    else:
        two_arr = a
    k = 0
    for i in two_arr:
        for j in i:
            if j:
                k += 1
    return k


def part2(data_temp, direction=""):
    sol_temp = 0
    data_score = []
    for i in range(data_temp.__len__()):
        data_score.append([0] * data_temp.__len__())
    for i, row in enumerate(data_temp):
        for j, col in enumerate(data_temp[i]):
            
            cardinal = []
            points_north = 1
            points_south = 1
            points_east = 1
            points_west = 1
            # ic("row: ", i + 1)
            # ic("col: ", j + 1)
            
            # get array north
            if direction != "E" and direction != "S" and direction != "W":
                cardinal.clear()
                cardinal_bool = [False] * (i + 1)
                for k in range(i + 1):
                    cardinal_vert = [item[j] for item in data_temp]
                    cardinal.append(cardinal_vert[i - k])
                # ic("north", cardinal)
                points_north = distance_trees(cardinal)
            
            # get array south
            if direction != "E" and direction != "N" and direction != "W":
                cardinal.clear()
                cardinal_bool = [False] * (data_temp.__len__() - j)
                for k in range(i, data_temp.__len__()):
                    cardinal_vert = [item[j] for item in data_temp]
                    cardinal.append(cardinal_vert[k])
                # ic("south", cardinal)
                points_south = distance_trees(cardinal)
            
            # get array east
            if direction != "N" and direction != "N" and direction != "W":
                cardinal.clear()
                cardinal_bool = [False] * (data_temp.__len__() - j)
                for k in range(j, data_temp.__len__()):
                    cardinal.append(row[k])
                # ic("east", cardinal)
                points_east = distance_trees(cardinal)
            
            # get array west
            if direction != "E" and direction != "N" and direction != "N":
                cardinal.clear()
                cardinal_bool = [False] * (j + 1)
                for k in range(j + 1):
                    cardinal.append(row[j - k])
                cardinal.reverse()
                # ic("west", cardinal)
                points_west = distance_trees(cardinal)
            
            # ic(points_north, points_east, points_south, points_west)
            data_score[i][j] = points_north * points_west * points_east * points_south
    for i in data_score:
        if max(i) > sol_temp:
            sol_temp = max(i)
    ic(data_score)
    return sol_temp, data_score
    

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
        if i == 0:
            for j in range(data[i].__len__()):
                vert = [k[j] for k in data]
                temp_vert = vert[:]
                temp_vert.reverse()
                mark(visible_trees(vert), data_bool, j, col=True)
                mark(visible_trees(temp_vert), data_bool, j, col=True, rev=True)
        temp = data[i][:]
        temp.reverse()
        mark(visible_trees(data[i]), data_bool, i)
        mark(visible_trees(temp), data_bool, i, rev=True)
    sol1 = count_true(data_bool)
    
    # main program part 2
    sol2 = part2(data)[0]
    
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
