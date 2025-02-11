import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def log(*x):
    print(" == ", x, file=sys.stderr, flush=True)

class Tree:
    def __init__(self, start):
        self.start = start
        self.next = {}
        self.nodes = 1

    def add_num(self, number):
        if len(number) > 1:
            follow = number[1]
            if follow not in self.next:
                self.next[follow] = Tree(follow)
                self.next[follow].add_num(number[1:])
                self.nodes += self.next[follow].nodes
            else:
                self.next[follow].add_num(number[1:])
                self.nodes = 1
                for i in self.next:
                    self.nodes += self.next[i].nodes


trees = {}

telephone = []
n = int(input())
for i in range(n):
    telephone.append(input())

log(telephone)

for num in telephone:
    indice = num[0]
    if indice not in trees:
        trees[indice] = Tree(indice)
    trees[indice].add_num(num)

tot = 0
for tree in trees:
    tot += trees[tree].nodes

print(tot)

# The number of elements (referencing a number) stored in the structure.
