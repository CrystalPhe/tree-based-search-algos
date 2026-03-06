# Tree-Based Search Algorithms (Robot Navigation)

This project implements several **search algorithms** to solve a grid-based robot navigation problem.  
The program finds a path from a **start position** to one or more **goal positions** while avoiding obstacles.

## Algorithms Implemented

- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Greedy Best-First Search (GBFS)
- A* Search
- Iterative Deepening DFS (IDDFS)
- Iterative Deepening A* (IDA*)

## Features

- Grid-based pathfinding
- Supports multiple goals and obstacles
- Command-line interface
- Optional **Pygame visualization** of search progress
- Displays visited nodes and final path

## Run the Program

      python search.py <mapfile>.txt <method>

Optional: Add "visualization" at the end to see a live grid animation.
    
      Example: python search.py map1.txt astar visualization


## Technologies

- Python
- Pygame
- Search Algorithms / AI Pathfinding

