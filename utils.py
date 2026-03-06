# utils.py

# Check if a cell is walkable (not outside bounds or in walls)
def is_walkable(x, y, rows, cols, walls):
    if not (0 <= x < cols and 0 <= y < rows):
        return False
    for wx, wy, w, h in walls:
        if wx <= x < wx + w and wy <= y < wy + h:
            return False
    return True

# Manhattan distance between two points
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Heuristic function: minimum Manhattan distance to any goal
def heuristic(pos, goals):
    return min(manhattan(pos, goal) for goal in goals)