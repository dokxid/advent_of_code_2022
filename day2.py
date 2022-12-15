from enum import Enum

if __name__ == '__main__':

    # file = open("input2_mock.txt")
    file = open("input/input2.txt")
    text = file.readlines()
    line_count = text.__len__()
    
    class Bonus(Enum):
        ROCK = 1        # rock
        PAPER = 2       # paper
        SCISSORS = 3    # scissors
    
    class Result(Enum):
        LOSE = 0        # lose
        DRAW = 3        # draw
        WIN = 6         # win
    
    # deprecated and unused
    # comment of shame
    class Strategy(Enum):
        E_ROCK = "A"
        E_PAPER = "B"
        E_SCISSORS = "C"
        ROCK = "X"
        PAPER = "Y"
        SCISSORS = "Z"
    
    points_1 = 0
    points_2 = 0
    
    # part 1
    for cur in range(line_count):
        if text[cur][0] == "A":
            if text[cur][2] == "X":
                points_1 += Result.DRAW.value
                points_1 += Bonus.ROCK.value
            if text[cur][2] == "Y":
                points_1 += Result.WIN.value
                points_1 += Bonus.PAPER.value
            if text[cur][2] == "Z":
                points_1 += Result.LOSE.value
                points_1 += Bonus.SCISSORS.value
        if text[cur][0] == "B":
            if text[cur][2] == "X":
                points_1 += Result.LOSE.value
                points_1 += Bonus.ROCK.value
            if text[cur][2] == "Y":
                points_1 += Result.DRAW.value
                points_1 += Bonus.PAPER.value
            if text[cur][2] == "Z":
                points_1 += Result.WIN.value
                points_1 += Bonus.SCISSORS.value
        if text[cur][0] == "C":
            if text[cur][2] == "X":
                points_1 += Result.WIN.value
                points_1 += Bonus.ROCK.value
            if text[cur][2] == "Y":
                points_1 += Result.LOSE.value
                points_1 += Bonus.PAPER.value
            if text[cur][2] == "Z":
                points_1 += Result.DRAW.value
                points_1 += Bonus.SCISSORS.value
    print("part 1: ", points_1)

    # part 2
    for cur in range(line_count):
        if text[cur][0] == "A":
            if text[cur][2] == "Y":
                points_2 += Result.DRAW.value
                points_2 += Bonus.ROCK.value
            if text[cur][2] == "Z":
                points_2 += Result.WIN.value
                points_2 += Bonus.PAPER.value
            if text[cur][2] == "X":
                points_2 += Result.LOSE.value
                points_2 += Bonus.SCISSORS.value
        if text[cur][0] == "B":
            if text[cur][2] == "X":
                points_2 += Result.LOSE.value
                points_2 += Bonus.ROCK.value
            if text[cur][2] == "Y":
                points_2 += Result.DRAW.value
                points_2 += Bonus.PAPER.value
            if text[cur][2] == "Z":
                points_2 += Result.WIN.value
                points_2 += Bonus.SCISSORS.value
        if text[cur][0] == "C":
            if text[cur][2] == "Z":
                points_2 += Result.WIN.value
                points_2 += Bonus.ROCK.value
            if text[cur][2] == "X":
                points_2 += Result.LOSE.value
                points_2 += Bonus.PAPER.value
            if text[cur][2] == "Y":
                points_2 += Result.DRAW.value
                points_2 += Bonus.SCISSORS.value
    print("part 2: ", points_2)
    
    print("end of program reached")
    