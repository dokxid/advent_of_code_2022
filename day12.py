# imports
import math
import traceback
from queue import PriorityQueue

from icecream import ic
from treelib.tree import *
from constants import *

# constants
DAY = 12
DEBUG_DATA = False
DEBUG = True
if not DEBUG:
    ic.disable()

# var
sol1 = 0
sol2 = 0
field = []
tree = Tree()


class Parser:
    
    def __init__(self, text_parse: list[str]):
        self.text_parse = text_parse
        self.len = text_parse.__len__()
    
    @staticmethod
    def parse():
        # open file
        f = open_file(DAY, DEBUG_DATA)
        t = f.readlines()
        t = list(map(sanitize, t))
        return t


def eval_elevation(f: list[list[int]], debug=True):
    evaluation = {"up": abs(f[1][1] - f[1 - 1][1]) <= 1,
                  "down": abs(f[1][1] - f[1 + 1][1]) <= 1,
                  "left": abs(f[1][1] - f[1][1 - 1]) <= 1,
                  "right": abs(f[1][1] - f[1][1 + 1]) <= 1}
    if debug: print("+ can move up? {}\n"
                    "+ can move down? {}\n"
                    "+ can move left? {}\n"
                    "+ can move right? {}\n".format(evaluation["up"],
                                                    evaluation["down"],
                                                    evaluation["left"],
                                                    evaluation["right"]))
    return evaluation


def create_path(t: Tree, pos_old, pos_new, direction):
    t.create_node(pos_new, pos_new, parent=pos_old)


def eval_create_path(f):
    g = {}
    for r_idx, r in enumerate(f):
        for c_idx, c in enumerate(r):
            temp_graph = []
            elev = eval_elevation(get_neighbors(f, r_idx, c_idx), debug=False)
            if elev["up"]:
                temp_graph.append((r_idx - 1, c_idx))
            if elev["down"]:
                temp_graph.append((r_idx + 1, c_idx))
            if elev["left"]:
                temp_graph.append((r_idx, c_idx - 1))
            if elev["right"]:
                temp_graph.append((r_idx, c_idx + 1))
            g.update({(r_idx, c_idx): temp_graph})
    return g


def dijk(g: dict, s, e):
    # initialize distance dict
    dist = {}
    for key in g.keys():
        if key == s:
            dist.update({key: 0})
        else:
            dist.update({key: math.inf})
    
    # dijkstra time
    priority = 0
    pq = PriorityQueue()
    jobs = {0: s}
    pq.put(0)
    while not pq.empty():
        old = jobs[pq.get()]
        new = g[old]
        for p in new:
            if p == "END":
                break
            if dist[p] > dist[old] + 1:
                dist[p] = dist[old] + 1
                priority += 1
                pq.put(priority)
                jobs.update({priority: p})
    
    # return
    return dist


def ord_new(a):
    return ord(a) - 96


def part_1(f):
    # var
    graph = {}
    
    # find S
    s = find_char('S', f, DEBUG)
    e = find_char('E', f, DEBUG)
    ic(s, e)
    
    # convert field to correct heatmap
    f[s[0]] = f[s[0]].replace('S', 'a')
    f[e[0]] = f[e[0]].replace('E', 'z')
    for line in range(len(f)):
        f[line] = list(map(ord_new, f[line]))
    
    # store paths
    tree.create_node("START" + s.__str__(), s)
    graph = eval_create_path(f)
    graph.update({e: ["END"]})
    distance = dijk(graph, s, e)
    distance_field = []
    for r in range(len(f)):
        distance_field.append([])
        for c in range(len(f[0])):
            distance_field[r].append(distance[(r, c)])
    ic(distance[e])
    ic(distance_field)
    ic(f)
    
    # return and debug
    return 0


def part_2(f):
    # logic
    
    # return
    return 0


if __name__ == '__main__':
    
    # parse
    field = Parser.parse()
    
    # main program
    sol1 = part_1(field)
    sol2 = part_2(field)
    
    # print solution
    if DEBUG:
        ic("DEBUG")
    print("sol1: ", sol1)
    print("sol2: ", sol2)
    
    # end of program reached
    print("end of program reached")
