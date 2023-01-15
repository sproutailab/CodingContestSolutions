#!/usr/bin/env python
# coding: utf-8
import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().split()))
cgrid = sys.stdin.read().split("\n")
grid = [list(row) for row in cgrid]
# Mark cameras, empties and start
MAX_STEPS = 10000
cameras = []
empties = []
for y in range(N):
    for x in range(M):
        if grid[y][x]=='S':
            sx = x
            sy = y
        if grid[y][x]=='C':
            cameras.append([x, y])
        if grid[y][x]=='.':
            empties.append([x, y])

#Create a matrix to keep the steps needed
steps = [[0 for i in range(M)] for j in range(N)]

def get_char(x, y):
    return grid[y][x]

def get_steps(x, y):
    return steps[y][x]

def set_grid(x, y, v):
    grid[y][x] = v
    
def set_step(x, y, v):
    steps[y][x] = v    
        

def mark_seen_by_camera(x, y):
    '''
    input:
        x, y : position of camera
    '''
    cx = x
    cy = y
    while True:
        cy -= 1
        if grid[cy][cx] in ['.', 'S']:  # Empty cell caught by camera
            set_step(cx, cy, -1)
            set_grid(cx, cy, "W")
        elif grid[cy][cx]=='W': # Camera cannot see through walls
            break
    
    cx = x
    cy = y
    while True:
        cy += 1
        if grid[cy][cx] in ['.', 'S']:  # Empty cell caught by camera
            set_step(cx, cy, -1)
            set_grid(cx, cy, "W")
        elif grid[cy][cx]=='W': # Camera cannot see through walls
            break
    
    cx = x
    cy = y
    while True:
        cx -= 1
        if grid[cy][cx] in ['.', 'S']:  # Empty cell caught by camera
            set_step(cx, cy, -1)
            set_grid(cx, cy, "W")
        elif grid[cy][cx]=='W': # Camera cannot see through walls
            break

    cx = x
    cy = y    
    
    while True:
        cx += 1
        if grid[cy][cx] in ['.', 'S']:  # Empty cell caught by camera
            set_step(cx, cy, -1)
            set_grid(cx, cy, "W")
        elif grid[cy][cx]=='W': # Camera cannot see through walls
            break


for x, y in cameras:
    mark_seen_by_camera(x, y)

if steps[sy][sx] == -1: # Starting point caught by camera the print all -1
    for x, y in empties:
        print(-1)
    exit()


def bfs(x, y):
    q = deque()
    q.append((x, y, 0)) # Push staring point to the queue. x, y are positions, 0 is steps
    while q:
        cx, cy, csteps = q.popleft()
        char = get_char(cx, cy)
        if char in ("W", "C"):
            continue
        set_grid(cx, cy, "W")
        set_step(cx, cy, csteps)
        if char in ["S", "."]:
            q.append((cx - 1, cy, csteps + 1))
            q.append((cx + 1, cy, csteps + 1))
            q.append((cx, cy + 1, csteps + 1))
            q.append((cx, cy - 1, csteps + 1))
        elif char == "L":
            q.append((cx - 1, cy, csteps))
        elif char == "R":
            q.append((cx + 1, cy, csteps))
        elif char == "U":
            q.append((cx, cy - 1, csteps))
        elif char == "D":
            q.append((cx, cy + 1, csteps))
        

bfs(sx, sy)

for x, y in empties:
    csteps = get_steps(x, y)
    csteps = -1 if csteps==0 else csteps
    print(csteps)