# gbfs.py

from queue import PriorityQueue
from utils import is_walkable, manhattan

def gbfs(start, goals, rows, cols, walls):
    frontier = PriorityQueue() # Priority queue sorted by heuristic
    frontier.put((0, start))
    came_from = {start: None}
    visited = set()
    visited_order = [] # For visualization/debugging

    while not frontier.empty():
        _, current = frontier.get()
        visited.add(current)
        visited_order.append(current)

        if current in goals: # Goal found
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path, path[-1], len(visited), visited, visited_order

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:  # priority: up, left, down, right
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)
            if is_walkable(nx, ny, rows, cols, walls) and neighbor not in visited:
                # Greedy uses heuristic only 
                priority = min(manhattan(neighbor, goal) for goal in goals)
                frontier.put((priority, neighbor))
                if neighbor not in came_from:
                    came_from[neighbor] = current

    return None, None, len(visited), visited, visited_order # No goal found
