if __name__ == '__main__':
    
    # constants
    DEBUG = False
    DAY = 3
    
    # open file
    if DEBUG:
        file = open("input" + str(DAY) + "_mock.txt")
    else:
        file = open("input" + str(DAY) + ".txt")
    text = file.readlines()
    line_count = text.__len__()
    
    # def
    def str_compare(a: str, b: str) -> [str, int]:
        """
        returns an array with [the shared characters, their point number]
        
        :param a: str 1
        :param b: str 2
        :return: [str, int]
        """
        
        same_chars = ""
        for char in a:
            if char in b:
                same_chars += char
                break
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
        
    # var
    rucksack = []
    chars = []
    points = 0
    sol = 0
    
    # main program here
    for line in range(line_count):
        c_size = int((text[line].__len__() - 1) / 2)
        temp = text[line].__len__() - 1
        rucksack.append([text[line][0:c_size], text[line][c_size:text[line].__len__()-1]])
        chars.append(str_compare(rucksack[line][0], rucksack[line][1]))
    sol = sum_second_index(chars)
        
    # print solution
    print(rucksack)
    for row in range(chars.__len__()):
        print(chars[row])
    print("sol: ", sol)
    
    # end of program reached
    print("end of program reached")
