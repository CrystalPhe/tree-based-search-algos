# search.py 
import pygame
import sys
import time
from visualization import visualize  

from dfs import dfs
from bfs import bfs
from astar import astar
from gbfs import gbfs
from cus1 import iddfs
from cus2 import idastar

# Read map file 
def load_map(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    rows, cols = eval(lines[0])
    start = eval(lines[1])
    goal_line = lines[2].split('|')
    goals = [eval(g.strip()) for g in goal_line]
    walls = [eval(w) for w in lines[3:]]

    return rows, cols, start, goals, walls


# Path
def path_to_directions(path):
    directions = []
    for (x1, y1), (x2, y2) in zip(path, path[1:]):
        dx, dy = x2 - x1, y2 - y1
        if dx == 1: directions.append("right")
        elif dx == -1: directions.append("left")
        elif dy == 1: directions.append("down")
        elif dy == -1: directions.append("up")
    return directions



# --MAIN--
if len(sys.argv) < 3:
    print("Usage: python search.py <mapfile.txt> <method> [visualization]")
    sys.exit(1)

map_file = sys.argv[1]
method = sys.argv[2].upper()
visualize_flag = len(sys.argv) > 3 and sys.argv[3].lower() == "visualization"

# Load map
try:
    ROWS, COLS, agent_pos, goals, walls = load_map(map_file)
except Exception as e:
    print(f"Error reading map file: {e}")
    sys.exit(1)

# Run search
path, goal, nodes_created = None, None, 0
start_time = time.perf_counter() # Timer for testing speed

if method == "DFS":
    path, goal, nodes_created, visited, visited_order = dfs(agent_pos, goals, ROWS, COLS, walls)
elif method == "BFS":
    path, goal, nodes_created, visited, visited_order = bfs(agent_pos, goals, ROWS, COLS, walls)
elif method == "ASTAR":
    path, goal, nodes_created, visited, visited_order = astar(agent_pos, goals, ROWS, COLS, walls)
elif method == "GBFS":
    path, goal, nodes_created, visited, visited_order = gbfs(agent_pos, goals, ROWS, COLS, walls)
elif method == "CUS1":
    path, goal, nodes_created, visited, visited_order = iddfs(agent_pos, goals, ROWS, COLS, walls)
elif method == "CUS2":
    path, goal, nodes_created, visited, visited_order = idastar(agent_pos, goals, ROWS, COLS, walls)
else:
    print(f"Unknown search method: {method}")
    sys.exit(1)

end_time = time.perf_counter()  # End timer
speed_time = (end_time - start_time) * 1000

# visited nodes for debugging

# print("Visited nodes in order:")
# print(', '.join(str(node) for node in visited_order))

# Print Result to Terminal
print("-----------RESULT-----------")
# print(f"Time took: {speed_time:.2f} ms") #uncomment to test speed
print(f"{map_file}; Method: {method}")
if path:
    directions = path_to_directions(path)
    print(f"{goal} {nodes_created}")
    print(', '.join(directions))
else:
    print(f"No goal is reachable; {nodes_created}")

# Optional Visualization 
if visualize_flag:
    visualize(ROWS, COLS, agent_pos, goals, walls, visited_order, path, method)

sys.exit()
