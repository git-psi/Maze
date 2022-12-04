import pygame
import maze_creator as maze_creator_py
import player as player_py
pygame.init()

clock = pygame.time.Clock()
fps = 60

#case of the screen
num_of_case = 51
case_size = 15

#initialize screen
screen_width =  num_of_case * case_size
screen_height = num_of_case * case_size
screen = pygame.display.set_mode((screen_width, screen_height))

#create maze
maze_creator = maze_creator_py.MazeCreator()
maze_data = maze_creator.create_maze(num_of_case, case_size)

def draw_maze(maze_data, case_size):
    line = 0
    for line_case in maze_data:
        row = 0
        for row_case in line_case:
            if row_case == 1:
                pygame.draw.rect(screen, (255, 255, 255), (row * case_size, line * case_size, case_size, case_size))
            if row_case == 2:
                pygame.draw.rect(screen, (0, 255, 0), (row * case_size, line * case_size, case_size, case_size))
            row += 1
        line += 1

#initialize player
player = player_py.Player(0, 1, num_of_case, num_of_case, maze_data, case_size, screen)

run = True
while run:
    #fps
    clock.tick(fps)

    #draw background
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_width, screen_height))
    #draw maze
    draw_maze(maze_data, case_size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update player
    player.update()

    pygame.display.update()

pygame.quit()