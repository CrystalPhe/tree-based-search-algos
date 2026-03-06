# cus2.py

from utils import is_walkable, heuristic

def idastar(start, goals, rows, cols, walls):

    visited_set = set()    
    visited_order = []  # For visualization/debugging
    nodes_created = 0      

    def limited_dfs(path, g, threshold):
        nonlocal nodes_created
        node = path[-1]
        f = g + heuristic(node, goals)
        # Prune if cost exceeds the current threshold
        if f > threshold:
            return f
        if node in goals: # goal is found
            return True
        if node not in visited_set:
            visited_set.add(node)
            visited_order.append(node)
        
        minimum = float('inf')
        # Up left down right
        # Sorting neighbors by their estimated f value 
        neighbors = []
        for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:

            neighbor = (node[0] + dx, node[1] + dy)
            if neighbor in path:  # Skip if already in the current path 
                continue
            if not is_walkable(neighbor[0], neighbor[1], rows, cols, walls):
                continue
            # Calculate the f cost
            f_neighbor = g + 1 + heuristic(neighbor, goals)
            neighbors.append((f_neighbor, neighbor))
        
        # Sort neighbors in increasing order of f cost
        neighbors.sort(key=lambda x: x[0])
        
        for _, neighbor in neighbors:
            # Increase node counter for each expand 
            nodes_created += 1
            # Record neighbor in visited order 
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                visited_order.append(neighbor)
            
            path.append(neighbor)
            result = limited_dfs(path, g + 1, threshold)
            if result is True:
                return True 
            # Update the minimal f value that exceeded the threshold
            if isinstance(result, (int, float)) and result < minimum:
                minimum = result
            path.pop()
        return minimum

    # Initial threshold is the heuristic of the start node
    threshold = heuristic(start, goals)
    path = [start]
    visited_set.add(start)
    visited_order.append(start)
    
    # Iterative deepening loop: Increase threshold until a solution is found or no solution
    while True:
        result = limited_dfs(path, 0, threshold)
        if result is True:
            found_path = list(path)
            reached_goal = path[-1]
            return found_path, reached_goal, nodes_created, list(visited_set), visited_order
        if result == float('inf'):
            return None, None, nodes_created, list(visited_set), visited_order # no path found
        threshold = result  # Increase threshold to the smallest f value that exceeded the current threshold
