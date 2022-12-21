PATH = __file__.replace("constants.py", "")
INPUTDIR = PATH + "/input/"


def open_file(a, debug):
    if debug:
        file = open(INPUTDIR + "input" + str(a) + "_mock.txt")
    else:
        file = open(INPUTDIR + "input" + str(a) + ".txt")
    return file


def sanitize(a: str) -> str:
    return a.replace('\n', '')


def sanitize_list_str_to_int(a: list[str]) -> list[int]:
    return list(map(int, a))


def parse_int(a: str):
    temp = a.split("\n")
    for i in temp:
        i = list(sanitize(i))
    return temp


def find_char(c: str, text, debug=True):
    for idx, r in enumerate(text):
        i = r.find(c)
        if i != -1:
            if debug: print("found {} in: {}, position {}".format(c, text.index(r), i))
            return idx, i
    

def get_neighbors(a: list[list], r_idx, c_idx, zero_as_bounds=True):
    """
    return 3x3 2d list for given index r, c
    :param zero_as_bounds:
    :param a:
    :param r_idx:
    :param c_idx:
    :return:
    """
    temp = []
    for r_jdx, r in enumerate(range(r_idx - 1, r_idx + 2)):
        temp.append([])
        for c_jdx, c in enumerate(range(c_idx - 1, c_idx + 2)):
            if zero_as_bounds and (r < 0 or c < 0):
                temp[r_jdx].append(0)
            else:
                temp[r_jdx].append(a[r][c])
    return temp


# unused but interesting https://en.m.wikipedia.org/wiki/Karatsuba_algorithm#Pseudocode
def karatsuba(x, y):
    # catch small integers
    if x < 10 or y < 10:
        return x * y
    
    # calculate size of numbers
    m = max(len(str(x)), len(str(y)))
    m2 = m // 2
    
    # calculate parts
    a = x // 10 ** m2
    b = x % 10 ** m2
    c = y // 10 ** m2
    d = y % 10 ** m2
    
    # recursive calls
    z0 = karatsuba(b, d)
    z1 = karatsuba((a + b), (c + d))
    z2 = karatsuba(a, c)
    
    # return
    return (z2 * 10 ** (2 * m2)) + ((z1 - z2 - z0) * 10 ** m2) + z0


if __name__ == '__main__':
    print(PATH)
