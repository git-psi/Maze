import pygame
import random
pygame.init()

clock = pygame.time.Clock()
fps = 15

#case of the screen
num_of_case = 41
case_size = 10

#initialize screen
screen_width =  num_of_case * case_size
screen_height = num_of_case * case_size
screen = pygame.display.set_mode((screen_width, screen_height))

def start():
    #initialize variable for the creation
    move_stack = []
    maze_data = []
    for i in range(0, num_of_case):
        line = []
        for i in range(0, num_of_case):
            line.append(0)
        maze_data.append(line)
    maze_data[1][1] = 1
    maze_data[1][0] = 1
    maze_data[num_of_case - 2][num_of_case - 1] = 1

    #initialize position
    x = 1
    y = 1
    return x, y, maze_data, move_stack
x, y, maze_data, move_stack = start()

def move(x, y, maze_data, move_stack):
    possibility = []
    #see possibility of deplacement
    if x-2 > 0 and maze_data[y][x-2] == 0:
        possibility.append("west")
    if x+2 < num_of_case - 1:
        if maze_data[y][x+2] == 0:
            possibility.append("east")
    if y-2 > 0 and maze_data[y-2][x] == 0:
        possibility.append("north")
    if y+2 < num_of_case - 1:
        if maze_data[y+2][x] == 0:
            possibility.append("south")

    if possibility:
        move = random.choice(possibility)
        if move == "west":
            maze_data[y][x-1] = 1
            maze_data[y][x-2] = 1
            x -= 2
        if move == "east":
            maze_data[y][x+1] = 1
            maze_data[y][x+2] = 1
            x += 2
        if move == "north":
            maze_data[y-1][x] = 1
            maze_data[y-2][x] = 1
            y -= 2
        if move == "south":
            maze_data[y+1][x] = 1
            maze_data[y+2][x] = 1
            y += 2
        move_stack.append((x, y))
    else:
        if move_stack:
            x, y = move_stack.pop()
        else:
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                x, y, maze_data, move_stack = start()

    return x, y, maze_data, move_stack

def draw_maze(maze_data, case_size):
    line = 0
    for line_case in maze_data:
        row = 0
        for row_case in line_case:
            if row_case:
                pygame.draw.rect(screen, (255, 255, 255), (row * case_size, line * case_size, case_size, case_size))
            row += 1
        line += 1

run = True
while run:
    #fps
    # clock.tick(fps)

    #draw background
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_width, screen_height))
    #move
    x, y, maze_data, move_stack = move(x, y, maze_data, move_stack)
    #draw maze
    draw_maze(maze_data, case_size)
    #draw x and y
    # pygame.draw.rect(screen, (255, 0, 0), (x * case_size, y * case_size, case_size, case_size))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()