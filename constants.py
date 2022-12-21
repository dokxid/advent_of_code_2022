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
    for r in text:
        i = r.find(c)
        if i != -1:
            if debug: print("found {} in: {}, position {}".format(c, text.index(r), i))
            return i


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
