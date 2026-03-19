import heapq
import random
import math

GRID = 70

def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def neighbors(node):
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    result=[]
    
    for d in dirs:
        x=node[0]+d[0]
        y=node[1]+d[1]
        
        if 0<=x<GRID and 0<=y<GRID:
            result.append((x,y))
            
    return result


def astar(grid,start,goal):

    openlist=[]
    heapq.heappush(openlist,(0,start))
    
    parent={}
    g={start:0}

    while openlist:

        current=heapq.heappop(openlist)[1]

        if current==goal:
            
            path=[]
            
            while current in parent:
                path.append(current)
                current=parent[current]
            
            path.append(start)
            path.reverse()
            
            return path

        for n in neighbors(current):

            if grid[n[0]][n[1]]==1:
                continue

            newg=g[current]+1

            if n not in g or newg<g[n]:

                g[n]=newg
                f=newg+heuristic(n,goal)
                
                heapq.heappush(openlist,(f,n))
                parent[n]=current

    return None


grid=[[0]*GRID for _ in range(GRID)]

start=(0,0)
goal=(69,69)

current=start

while current!=goal:

    path=astar(grid,current,goal)

    if not path:
        print("Goal unreachable")
        break

    next_step=path[1]

    if random.random()<0.1:
        x=random.randint(0,69)
        y=random.randint(0,69)
        grid[x][y]=1

    if grid[next_step[0]][next_step[1]]==1:
        continue

    current=next_step
    print("UGV moved to",current)

print("Goal reached")