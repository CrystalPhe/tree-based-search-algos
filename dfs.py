# dfs.py

from utils import is_walkable

def dfs(start, goals, rows, cols, walls):
    # Stack holds current_node, path_so_far
    stack = [(start, [start])]
    visited = set()
    visited_order = [] # For visualization/debugging
    nodes_created = 0

    while stack:
        # Pop last element from stack
        current, path = stack.pop()

        # If node is already visited, skip it
        if current in visited:
            continue

        # Mark the node as visited
        visited.add(current)
        visited_order.append(current)
        nodes_created += 1

        # Check if current node is one of the goals
        if current in goals:
            return path, current, nodes_created, list(visited), visited_order

        # Explore in order: up, left, down, right.
        neighbors = []
        for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]: # Stack is LIFO, add reverse order
            neighbor = (current[0] + dx, current[1] + dy)
            # Only consider neighbor if it hasn't been visited and is walkable.
            if neighbor not in visited and is_walkable(neighbor[0], neighbor[1], rows, cols, walls):
                neighbors.append(neighbor)
        
        # Add neighbors to the stack in reverse order so that the first neighbor (up) is processed first.
        for neighbor in reversed(neighbors):
            stack.append((neighbor, path + [neighbor]))

    # If we exit the loop, no path was found.
    return None, None, nodes_created, list(visited), visited_order

