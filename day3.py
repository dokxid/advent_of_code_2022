from icecream import ic

import collections
import operator

# constants
DEBUG_DATA = False
DEBUG = False
DAY = 3

# open file
if DEBUG_DATA:
    file = open("input" + str(DAY) + "_mock.txt")
else:
    file = open("input" + str(DAY) + ".txt")
text = file.readlines()
line_count = text.__len__()


def str_compare(a: str, b: str) -> [str, int]:
    """
    returns an array with [the shared characters, their point number]

    :param a: str 1
    :param b: str 2
    :return: [str, int]
    """
    same_chars = "???"
    for char in a:
        if char in b and char != "\n":
            same_chars = char
    return [same_chars, priorities(same_chars)]


def str_compare_3(a: str, b: str, c: str) -> [str, int]:
    """
    returns an array with [the shared characters, their point number]

    :param a: str 1
    :param b: str 2
    :param c: str 3
    :return: [str, int]
    """
    same_chars = "???"
    for char in a:
        if char in b and char != "\n":
            if char in c and char != "\n":
                same_chars = char
    return [same_chars, priorities(same_chars)]


def priorities(a: str) -> int:
    """
    returns an integer value for alphabets:

    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.

    :param a: str with len(1)
    :return: int
    """
    if a.__len__() == 1:
        if ord(a) > 96:
            return ord(a) - 96
        else:
            return ord(a) - 64 + 26
    else:
        return 0


def sum_second_index(a: list) -> int:
    """
    returns sum of 2nd col of lists

    :param a: list with 2nd col int
    :return: int
    """
    temp_sum = 0
    for i in range(a.__len__()):
        temp_sum += a[i][1]
    return temp_sum


def count_chars(a: list):
    temp_char_count = {}
    for i in a:
        for j in i:
            if temp_char_count.get(j) is not None:
                temp_char_count[j] += 1
            else:
                temp_char_count.update({j: 1})
    return collections.OrderedDict(sorted(temp_char_count.items(), key=operator.itemgetter(1)))
    
    
def find_matching_token(text_to_search: list):
    res = {}
    for i in range(0, line_count, 3):
        a = text_to_search[i]
        b = text_to_search[i+1]
        c = text_to_search[i+2]
        temp_compare_str = ""
        temp_compare = str_compare_3(a, b, c)
        if res.get(temp_compare[0][0]) is not None:
            res[temp_compare[0][0]] += 1
        else:
            res.update({temp_compare[0][0]: 1})
    return res
    

# var
rucksack = []
chars = []
sol1 = 0
sol2 = 0


if __name__ == '__main__':
    
    # main program part 1
    for line in range(line_count):
        c_size = int((text[line].__len__() - 1) / 2)
        temp = text[line].__len__() - 1
        rucksack.append([text[line][0:c_size], text[line][c_size:text[line].__len__() - 1]])
        chars.append(str_compare(rucksack[line][0], rucksack[line][1]))
    sol1 = sum_second_index(chars)
    
    # main program part 2
    token = find_matching_token(text)
    for char in token.keys():
        sol2 += priorities(char) * token[char]
    
    # print solution
    if DEBUG:
        ic(rucksack)
        ic(chars)
        ic(count_chars(text))
        ic(token)
        ic(sum(token.values()))
    ic(sol1)
    ic(sol2)
    
    # end of program reached
    print("end of program reached")
