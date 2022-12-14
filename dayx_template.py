# constants
DEBUG = True
DAY = 0

# open file
if DEBUG:
    file = open("input" + str(DAY) + "_mock.txt")
else:
    file = open("input" + str(DAY) + ".txt")
text = file.readlines()
line_count = text.__len__()

# var


if __name__ == '__main__':
    
    # main program here
    
    # print solution
    print(sol)
    
    # end of program reached
    print("end of program reached")
