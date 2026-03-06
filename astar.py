# astar.py

from queue import PriorityQueue
from utils import is_walkable, heuristic

def astar(start, goals, rows, cols, walls):
    frontier = PriorityQueue()
    count = 0 # Tie-breaker
    start_h = heuristic(start, goals)
    frontier.put((start_h, count, start, 0, [start]))
    nodes_created = 1

    # cost_so_far stores the best g cost found for each node
    cost_so_far = {start: 0} 
    visited = set()
    visited_order = [] # For visualization/debugging

    while not frontier.empty():
        f, _, current, g, path = frontier.get()

        # If already explored, skip 
        if current in visited:
            continue

        # Mark the node as explored.
        visited.add(current)
        visited_order.append(current)

        # If goal found
        if current in goals:
            return path, current, nodes_created, list(visited), visited_order

        # Explore in order: up, left, down, right.
        for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if is_walkable(neighbor[0], neighbor[1], rows, cols, walls):
                new_g = g + 1  # each move costs 1
                # If neighbor is either new or we've found a better path (lower cost)
                if neighbor not in cost_so_far or new_g < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_g
                    new_f = new_g + heuristic(neighbor, goals)
                    count += 1
                    frontier.put((new_f, count, neighbor, new_g, path + [neighbor]))
                    nodes_created += 1

    return None, None, nodes_created, list(visited), visited_order # No goal found
