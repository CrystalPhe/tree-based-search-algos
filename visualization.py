# visualize.py
import pygame

CELL_SIZE = 60
# colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 128, 0) 
BLUE = (0, 0, 255)
LIGHT_GRAY = (180, 180, 180)

def visualize(rows, cols, start, goals, walls, visited_order, path, method):
    WIDTH, HEIGHT = cols * CELL_SIZE, rows * CELL_SIZE
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"{method} Search Visualization") 

    clock = pygame.time.Clock()
    visited_index = 0
    path_index = 0
    step_delay = 100  # milliseconds delay, edit for test
    last_step_time = pygame.time.get_ticks()
    done_visiting = False
    running = True

    def draw_grid():
        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

    while running:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_grid() # grid lines

        # Draw walls
        for x, y, w, h in walls:
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, w * CELL_SIZE, h * CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect)

        # Draw goal cells in green.
        for gx, gy in goals:
            rect = pygame.Rect(gx * CELL_SIZE, gy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, rect)

        # Draw visited cells
        for vx, vy in visited_order[:visited_index]:
            if (vx, vy) in goals:
                continue
            rect = pygame.Rect(vx * CELL_SIZE, vy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, LIGHT_GRAY, rect)

        if not done_visiting and current_time - last_step_time > step_delay:
            if visited_index < len(visited_order):
                visited_index += 1
                last_step_time = current_time
            else:
                done_visiting = True
                last_step_time = current_time

        # Draw the path, then highlight goal in dark green
        if done_visiting and path:
            for px, py in path[:path_index]:
                rect = pygame.Rect(px * CELL_SIZE, py * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if (px, py) in goals:
                    pygame.draw.rect(screen, DARK_GREEN, rect)
                else:
                    pygame.draw.rect(screen, BLUE, rect)

            if path_index < len(path) and current_time - last_step_time > step_delay:
                path_index += 1
                last_step_time = current_time

        # Draw start cell in red
        ax, ay = start
        rect = pygame.Rect(ax * CELL_SIZE, ay * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
