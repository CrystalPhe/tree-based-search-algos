from collections import deque
from utils import is_walkable

def bfs(start, goals, rows, cols, walls):
    queue = deque([(start, [start])])  # FIFO queue for BFS
    visited = set([start])
    visited_order = [] # For visualization/debugging
    nodes_created = 1  # Start node is 1

    while queue:
        (x, y), path = queue.popleft()
        visited_order.append((x, y))

        if (x, y) in goals: # Goal found
            return path, (x, y), nodes_created, visited, visited_order

        for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:  # Up, Left, Down, Right
            nx, ny = x + dx, y + dy
            if is_walkable(nx, ny, rows, cols, walls) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)])) # Enqueue new path
                nodes_created += 1

    return None, None, nodes_created, visited, visited_order # No goal found
