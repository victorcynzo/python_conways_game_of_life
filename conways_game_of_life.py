import pygame
import random

pygame.init()

#constants
BLACK = (0, 0, 0) #RGB colour codes
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def gen(num):
    return set([(random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH)) for _ in range(num)])

#drawing the grid, positions are live cells
def draw_grid(positions):
    for position in positions:
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE))

    #all positions of alive cells, rather than every possible grid position (incl empty)
    for row in range (GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE),)

    for col in range (GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))


def adjust_grid(positions):
    all_neighbors = set()
    new_positions = set()

    for position in positions:
        neighbors = get_neighbors(position)
        all_neighbors.update(neighbors) #passed into set, no dupes

        #check if they're alive
        neighbors = list(filter(lambda x: x in position, neighbors))

        if len(neighbors) in [2, 3]:
            new_positions.add(position)

    #cells need to become alive
    for position in all_neighbors:
        neighbors = get_neighbors(positions)
        neighbors = list(filter(lambda x: x in position, neighbors))

        if len(neighbors) == 3: #three live neighbors cell becomes alive
            new_positions.add(position)

    return new_positions

def get_neighbors(pos):
    # 8 possible neighbor saround 1 cell
    x, y = pos
    neighbors = []
    for dx in [-1, 0, 1]: #displacement in x, iterate around cell
        if x + dx < 0 or x + dx > GRID_WIDTH: #not off screen
            continue
        for dy in [-1, 0 ,1]: #displayement in y, iterate around cell
            if y + dy < 0 or y + dy >GRID_HEIGHT: #not off screen
                continue
            if dx == 0 and dy == 0: #current pos, not iterate cell itself
                continue

            neighbors.append((x + dx, y +dy))

    return neighbors

#main loop
def main():
    running = True
    playing = False

    positions = set()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (col, row)

                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing

                if event.key == pygame.K_c:
                    positions = set()
                    playing = False
                
                if event.key == pygame.K_g:
                    positions = gen(random.randrange(2, 5) * GRID_WIDTH)


        screen.fill(GREY)    
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()