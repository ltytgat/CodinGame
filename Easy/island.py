import sys
import math


def log(*x):
    print(" == ", x, file=sys.stderr, flush=True)

def explore(island, start, n):
    val = island[start]
    log(start, island[start])
    if val == 0:
        return True
    else:
        up=start-n
        down=start+n
        left=start-1
        right=start+1
        log(start, up, right, down, left)
        log(island[start], island[up], island[right], island[down], island[left])
        if abs(val-island[up]) <=1:
            island[start] = 50
            if explore(island,up, n):
                return True
        if abs(val-island[down]) <=1:
            island[start] = 50
            if explore(island,down, n):
                return True
        if abs(val-island[right]) <=1:
            island[start] = 50
            if explore(island,right, n):
                return True
        if abs(val-island[left]) <=1:
            island[start] = 50
            if explore(island,left, n):
                return True
    return False

elevation = []
n = int(input())
for i in range(n):
    for j in input().split():
        elevation.append(int(j))

start = int(math.floor((len(elevation)/2)))

if explore(elevation, start, n):
    print("yes")
else:
    print("no")
