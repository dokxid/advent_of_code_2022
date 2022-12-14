if __name__ == '__main__':
    
    # constants
    DEBUG = True
    DAY = 3
    
    # open file
    if DEBUG:
        file = open("input" + str(DAY) + "_mock.txt")
    else:
        file = open("input" + str(DAY) + "txt")
    text = file.readlines()
    line_count = text.__len__()
    
    # main program here
    
    
    # end of program reached
    print("end of program reached")
