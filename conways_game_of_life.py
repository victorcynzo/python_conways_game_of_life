import pygame

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

#drawing the grid
def draw_grid(positions):
    #all positions of alive cells, rather than every possible grid position (incl empty)
    #grid lines, rows
    for row in range (GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE),)

    for column in range (GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (column * TILE_SIZE, 0), (column * TILE_SIZE, HEIGHT))

    

#main loop
def main():
    running = True

    positions = set()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(GREY)    
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()