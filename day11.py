#
from dataclasses import dataclass

# imports
from icecream import ic
import constants

# constants
DAY = 11
PART = 1
DEBUG_DATA = False
DEBUG = True
if not DEBUG:
    ic.disable()

# open file
file = constants.open_file(DAY, DEBUG_DATA)
text = file.readlines()
text = list(map(constants.sanitize, text))
line_count = text.__len__()

# var
sol1 = 0
sol2 = 0
rounds = 20
data = {}
monkeys = []


@dataclass
class Operation:
    op: str
    operand: str | int
    
    
# monkey
class Monkey:
    
    def __init__(self, items=None,
                 operation=Operation(operand=0, op="+"),
                 test=2,
                 monkey_true=0,
                 monkey_false=0):
        if items is None:
            items = []
        self.items = items
        self.operation = operation
        self.test = test
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
        self.count = 0

    def __repr__(self) -> str:
        return "Monkey(" + \
            "items: " + self.items.__repr__() + ", " + \
            "operation: " + self.operation.__repr__() + ", " + \
            "test: " + self.test.__repr__() + ", " + \
            "count: " + self.count.__repr__() + ", " + \
            "monkey_true: " + self.monkey_true.__repr__() + ", " + \
            "monkey_false: " + self.monkey_false.__repr__() + ")"
    
    def throw(self, target):
        print("+ Item with worry level {} is thrown to monkey #{}.".format(self.items[0], monkeys.index(target)))
        target.items.append(self.items.pop(0))
        
    def div_test(self):
        if self.items[0].__class__ == int:
            if self.items[0] % self.test == 0:
                # case true
                print("+ Current worry level is divisible by {}.".format(self.test))
                self.throw(monkeys[self.monkey_true])
            else:
                # case false
                print("+ Current worry level is not divisible by {}.".format(self.test))
                self.throw(monkeys[self.monkey_false])
        
    def evaluate(self):
        match self.operation.op:
            case "*":
                if not self.operation.operand.isdigit():
                    self.items[0] = self.items[0] * self.items[0]
                else:
                    self.items[0] = self.items[0] * int(self.operation.operand)
            case "+":
                if not self.operation.operand.isdigit():
                    self.items[0] = self.items[0] + self.items[0]
                else:
                    self.items[0] = self.items[0] + int(self.operation.operand)
                
    def relief(self):
        if self.items[0].__class__ == int:
            self.items[0] = self.items[0] // 3
    
    def action(self):
        print("+++ " + self.__repr__())
        while len(self.items) != 0:
            print("++ Monkey inspects an item with a worry level of {}.".format(self.items[0]))
            self.evaluate()
            print("+ Worry level has increased to {}".format(self.items[0]))
            self.relief()
            print("+ Monkey gets bored with item. Worry level is divided by 3 to {}.".format(self.items[0]))
            self.div_test()
            self.count += 1
            

class Parser:
    
    def __init__(self, text_parse: list[str]):
        self.text_parse = text_parse
        self.len = text_parse.__len__()
        
    def parse(self):
        for i in range(0, self.len, 7):
            
            # parse items
            colon_split = self.text_parse[i+1].split(":")
            items_list = colon_split[1].split(",")
            items_list = list(map(int, items_list))

            # parse op
            colon_split = self.text_parse[i+2].split(":")
            op_temp = colon_split[1].replace("new = old ", "")
            op = op_temp.split(" ")

            # parse test
            colon_split = self.text_parse[i+3].split(":")
            test = colon_split[1].replace("divisible by ", "")
            test = int(test)

            # parse monkey_true
            colon_split = self.text_parse[i+4].split(":")
            monkey_true = colon_split[1].replace("throw to monkey ", "")
            monkey_true = int(monkey_true)

            # parse monkey_false
            colon_split = self.text_parse[i+5].split(":")
            monkey_false = colon_split[1].replace("throw to monkey ", "")
            monkey_false = int(monkey_false)
            
            # create monkey
            monkeys.append(Monkey(
                items=items_list,
                operation=Operation(operand=op[2], op=op[1]),
                test=test,
                monkey_true=monkey_true,
                monkey_false=monkey_false,
            ))


def part_1():
    
    # monkey business be like
    for r in range(rounds):
        print("\n\nROUND #" + str(r+1))
        s = 0
        for mon in monkeys:
            print("\nMONKEY #" + str(s))
            mon.action()
            s += 1

    # store monkey business score
    temp = []
    for mon in monkeys:
        temp += [mon.count]
    temp.sort(reverse=True)
    return temp[0] * temp[1]
    

if __name__ == '__main__':
    
    # parse
    p = Parser(text)
    p.parse()
    
    # main program part 1
    sol1 = part_1()
    
    # main program part 2
    
    # print solution
    if DEBUG:
        ic("DEBUG")
        ic(data)
        ic(monkeys)
    print("sol1: ", sol1)
    print("sol2: ", sol2)
    
    # end of program reached
    print("end of program reached")