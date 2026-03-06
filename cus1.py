# cus1.py

from utils import is_walkable

def iddfs(start, goals, rows, cols, walls):
    def is_valid_move(pos):
        return is_walkable(pos[0], pos[1], rows, cols, walls)
    
    def dls(node, goals, depth_limit, path, visited, visited_order):
        if node in goals: # Goal found
            return path

        # depth limit reached, end search on this branch
        if depth_limit == 0:
            return None

        # up, left, down, right
        for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            new_pos = (node[0] + dx, node[1] + dy)
            if new_pos not in visited and is_valid_move(new_pos):
                visited.add(new_pos)
                visited_order.append(new_pos)
                result = dls(new_pos, goals, depth_limit - 1, path + [new_pos], visited, visited_order)
                if result is not None:
                    return result
        return None

    depth = 0
    # increase depth limit until goal is found
    while True:
        # Reset visited for each new iteration 
        visited = set([start])
        visited_order = [start]
        path = dls(start, goals, depth, [start], visited, visited_order)
        
        # If a solution is found, return the path 
        if path is not None:
            nodes_created = len(visited)
            goal_found = path[-1]
            return path, goal_found, nodes_created, list(visited), visited_order

        if depth > rows * cols:
            return None, None, len(visited), list(visited), visited_order # No path found
        
        depth += 1
