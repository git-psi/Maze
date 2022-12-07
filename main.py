import pygame
import maze_creator as maze_creator_py
import player as player_py
import menu as menu_py

clock = pygame.time.Clock()
fps = 60

#initialize menu
menu = menu_py.Menu()
in_menu = True


def start(num_of_case, case_size):
    #initialize screen
    screen_width =  num_of_case * case_size
    screen_height = num_of_case * case_size
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Maze - Game")

    #create maze
    maze_creator = maze_creator_py.MazeCreator()
    maze_data, arrivate = maze_creator.create_maze(num_of_case, case_size)

    #initialize game_over
    game_over = menu_py.GameOver(case_size, num_of_case, screen, maze_data)

    #initialize player
    player = player_py.Player(0, 1, arrivate, maze_data, case_size, screen)
    return screen, game_over, player, maze_data, screen_width, screen_height

def draw_maze(maze_data, case_size):
    line = 0
    for line_case in maze_data:
        row = 0
        for row_case in line_case:
            if row_case:
                rect = pygame.Rect(0, 0, case_size, case_size)
                rect.center = (row * case_size + case_size // 2, line * case_size + case_size // 2)
            if row_case == 1:
                pygame.draw.rect(screen, (255, 255, 255), rect)
            if row_case == 2:
                pygame.draw.rect(screen, (180, 180, 180), rect)
            row += 1
        line += 1


run = True
while run:
    #fps
    clock.tick(fps)

    if in_menu:
        menu_response = menu.update()
        if menu_response:
            in_menu = False
            num_of_case = menu_response[0]
            case_size = menu_response[1]
            screen, game_over, player, maze_data, screen_width, screen_height = start(num_of_case, case_size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if not in_menu:
        #draw background
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_width, screen_height))
        #draw maze
        draw_maze(maze_data, case_size)

        #update player
        response = player.update()
        if response == True:
            response = game_over.update()
            if response:
                menu.restart()
                in_menu = True

    pygame.display.update()

pygame.quit()