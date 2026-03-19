UGV Pathfinding Simulation (A* Search)
======================================

This file contains information about a Python simulation of an Unmanned Ground Vehicle (UGV) navigating a 70x70 km battlefield grid. The UGV utilizes the A* (A-Star) search algorithm to calculate the most optimal, shortest-distance path from a starting position to a user-specified goal while avoiding obstacles.

This project was developed as part of an Artificial Intelligence course assignment to demonstrate search algorithms and measure their computational effectiveness.

PROBLEM STATEMENT
-----------------
An Unmanned Ground Vehicle (UGV) must find the optimal path from a start node to a goal node on a 70x70 map of a small battlefield area. Obstacles are known a-priori, and the density of these obstacles is generated randomly across three different levels (Low, Medium, High). The algorithm must navigate the UGV through this grid space, avoiding all known obstacles, to reach the goal by the shortest distance. The path must be traced along with specific Measures of Effectiveness.

FEATURES & IMPLEMENTATION DETAILS
---------------------------------
- Algorithm: A* Search Algorithm.
- Heuristic: Euclidean Distance (allowing for 8-way movement including diagonals).
- Grid Environment: 70x70 coordinate system.
- Obstacle Densities:
    - Low (10% obstacle coverage)
    - Medium (25% obstacle coverage)
    - High (40% obstacle coverage)
- Measures of Effectiveness (MoE):
    - Path Length: Total Euclidean distance traveled.
    - Nodes Expanded: The number of grid cells evaluated during the search (efficiency metric).
    - Execution Time: The time taken by the algorithm to compute the path.
    - Steps in Path: The total number of discrete movements made.

REQUIREMENTS
------------
This script relies purely on Python standard libraries. No external packages are required.
- Python 3.x
- heapq
- random
- time
- math

HOW TO RUN
----------
Execute the Python script from your terminal or command prompt:

python program.py

The script will automatically run the simulation for all three density levels (Low, Medium, High) and output the Measures of Effectiveness for each scenario directly to the console.

