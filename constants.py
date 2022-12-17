INPUTDIR = "input/"


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
