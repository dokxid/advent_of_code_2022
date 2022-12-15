INPUTDIR = "input/"


def open_file(a, debug):
    if debug:
        file = open(INPUTDIR + "input" + str(a) + "_mock.txt")
    else:
        file = open(INPUTDIR + "input" + str(a) + ".txt")
    return file
