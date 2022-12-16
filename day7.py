# imports
from dataclasses import dataclass

from icecream import ic
import constants
from constants import sanitize

# constants
DAY = 7
PART = 1
DEBUG_DATA = False
DEBUG = True
if not DEBUG:
    ic.disable()

# open file
file = constants.open_file(DAY, DEBUG_DATA)
text = file.readlines()
line_count = text.__len__()

# var
sol1 = 0
sol2 = 0
data = {}


class Directory:
    
    def __init__(self, name, files=None, dirs=None, parent=None, size=0):
        self.size = size
        if files is None:
            files = []
        if dirs is None:
            dirs = []
        if parent is None:
            parent = 0
        self.name = name
        self.files = files
        self.dirs = dirs
        self.parent = parent
        data.update({self.__str__(): self})  # put into hashmap
        
    def get_size(self) -> int:
        temp_size = 0
        for i in self.dirs:
            temp_size += i.get_size()
        return self.size + temp_size
        
    def add_file(self, file_name):
        self.files.append(file_name)
        self.size += file_name.size
        
    def add_dir(self, dir_name: str):
        self.dirs.append(Directory(dir_name, parent=self))
        
    def __str__(self):
        if self.parent == 0:
            return "/"
        else:
            return self.parent.__str__() + self.name + "/"
        
    def __repr__(self):
        return "(" + str(self.get_size()) + ", " + str(self.get_size() < 100000) + ")"
        

@dataclass
class File:
    name: str
    size: int


if __name__ == '__main__':
    
    # main program part 1
    master = Directory("/")
    current_dir = master
    ic(master)
    
    # parse text into directories
    for line in range(1, line_count):
        ic("PROCESSING LINE", sanitize(text[line]))
        if text[line][0] == "$":
            san = sanitize(text[line][2:text[line].__len__()])
            ic(line, "$ found", san)
            match san[0:2]:
                case "ls":
                    ic("ls found")
                    for l_ls in range(line+1, line_count):
                        if not text[l_ls].startswith("$"):
                            if text[l_ls].startswith("dir"):
                                temp_dir_name = sanitize(text[l_ls][4:text[l_ls].__len__()])
                                ic(temp_dir_name)
                                current_dir.add_dir(temp_dir_name)
                            else:
                                temp_file_name = sanitize(text[l_ls][0:text[l_ls].__len__()])
                                ic(temp_file_name)
                                spl = temp_file_name.split(" ")
                                current_dir.add_file(File(spl[1], int(spl[0])))
                        else:
                            break
                case "cd":
                    ic("cd found", san[3:san.__len__()])
                    if san.find("..") != -1:
                        ic("switching to", current_dir.parent)
                        current_dir = current_dir.parent
                    else:
                        ic("switching to", san[3:san.__len__()])
                        ic(current_dir.__str__() + san[3:san.__len__()])
                        current_dir = data.get(current_dir.__str__() + san[3:san.__len__()] + "/")
    
    # calculate total size
    for directory in data:
        if data.get(directory).get_size() < 100000:
            ic("adding", data.get(directory).name, data.get(directory).get_size())
            sol1 += data.get(directory).get_size()
        # else:
            # ic("NOT adding", data.get(directory).name, data.get(directory).get_size())
            
            
    
    # main program part 2
    for line in range(line_count):
        sol2 += 1  # TODO
    
    # print solution
    if DEBUG:
        ic("DEBUG")
        ic(data)
    print("sol1: ", sol1)
    print("sol2: ", sol2)
    
    # end of program reached
    print("end of program reached")
