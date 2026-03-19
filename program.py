import heapq
import random
import time
import math

GRID_SIZE = 70

def generate_grid(density):
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if random.random() < density:
                grid[i][j] = 1
    return grid

def heuristic(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def get_neighbors(node):
    directions = [
        (-1,0),(1,0),(0,-1),(0,1),
        (-1,-1),(-1,1),(1,-1),(1,1)
    ]
    
    neighbors = []
    
    for d in directions:
        x = node[0] + d[0]
        y = node[1] + d[1]
        
        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
            neighbors.append((x,y))
            
    return neighbors

def astar(grid, start, goal):
    
    open_list = []
    heapq.heappush(open_list,(0,start))
    
    came_from = {}
    
    g_score = {start:0}
    
    nodes_expanded = 0
    
    while open_list:
        
        current = heapq.heappop(open_list)[1]
        nodes_expanded += 1
        
        if current == goal:
            path = []
            
            while current in came_from:
                path.append(current)
                current = came_from[current]
                
            path.append(start)
            path.reverse()
            
            return path, nodes_expanded
        
        for neighbor in get_neighbors(current):
            
            if grid[neighbor[0]][neighbor[1]] == 1:
                continue
                
            tentative_g = g_score[current] + heuristic(current,neighbor)
            
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                
                f_score = tentative_g + heuristic(neighbor,goal)
                
                heapq.heappush(open_list,(f_score,neighbor))
                
    return None, nodes_expanded


def run_simulation(density):

    grid = generate_grid(density)
    
    start = (0,0)
    goal = (69,69)
    
    grid[start[0]][start[1]] = 0
    grid[goal[0]][goal[1]] = 0
    
    start_time = time.time()
    
    path, nodes = astar(grid,start,goal)
    
    end_time = time.time()
    
    if path:
        path_length = 0
        
        for i in range(len(path)-1):
            path_length += heuristic(path[i],path[i+1])
            
        print("Path Found")
        print("Path Length:",path_length)
        print("Nodes Expanded:",nodes)
        print("Execution Time:",end_time-start_time)
        print("Steps in Path:",len(path))
        
    else:
        print("No Path Found")
        print("Nodes Expanded:",nodes)


print("LOW DENSITY")
run_simulation(0.10)

print("MEDIUM DENSITY")
run_simulation(0.25)

print("HIGH DENSITY")
run_simulation(0.40)