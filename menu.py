import pygame

class Menu():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 500))
        self.font = pygame.font.SysFont("Impact", 50, italic=True)
        self.restart()
        self.max_velocity_btn = 20
        self.velocity_cooldown = 2
        self.maze_txt = self.font.render("Maze", True, (255,255,255))
        self.maze_txt_rect = self.maze_txt.get_rect()
        self.maze_txt_rect.center = (400, 500 // self.num_of_button - 40)
    
    def update(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(self.maze_txt, self.maze_txt_rect)
        if not self.maze_level:
            for btn in self.all_btn:
                if not btn[2] >= self.max_velocity_btn: btn[3] += 1
                if btn[3] >= self.velocity_cooldown:
                    btn[3] = 0
                    btn[2] += 1
                if btn[0].update(400 - btn[1]): self.maze_level = btn[4]
                if not btn[1] <= 0: btn[1] -= btn[2]
                elif btn[1] < 0:
                    btn[1] = 0
                    btn[2] = 0
                    btn[3] = 0
            return False
        else:
            return self.maze_level

    def restart(self):
        pygame.display.set_caption("Maze - Menu")
        pygame.display.set_icon(pygame.image.load("icon.png"))
        self.screen = pygame.display.set_mode((800, 500))
        #num + 1
        self.num_of_button = 6
        #500 // num_of_button * (nb du btn)
        self.all_btn = [
            [Button(self.screen, "Très facile", 500 // self.num_of_button * 1 + 20), 400, 0, 0, (21, 28)],
            [Button(self.screen, "Facile", 500 // self.num_of_button * 2 + 20), 500, 0, 0, (31, 20)],
            [Button(self.screen, "Moyen", 500 // self.num_of_button * 3 + 20), 600, 0, 0, (41, 14)],
            [Button(self.screen, "Difficile", 500 // self.num_of_button * 4 + 20), 700, 0, 0, (51, 13)],
            [Button(self.screen, "Impossible", 500 // self.num_of_button * 5 + 20), 800, 0, 0, (71, 10)]
        ]
        self.maze_level = False

class GameOver():
    def __init__(self, case_size, num_of_case, screen, maze_data):
        self.screen = screen
        self.case_size = case_size
        self.num_of_case = num_of_case
        self.iteration = 0
        self.maze_data = maze_data
        self.cooldown = 1
        self.counter_size = 1

    def update(self):
        self.iteration += 1
        if self.iteration >= self.cooldown:
            self.iteration = 0
            self.counter_size += 1
        line = 0
        for line_case in self.maze_data:
            row = 0
            for row_case in line_case:
                if not row_case:
                    rect = pygame.Rect(0, 0, self.case_size + self.counter_size, self.case_size + self.counter_size)
                    rect.center = (row * self.case_size + self.case_size // 2, line * self.case_size + self.case_size // 2)
                    pygame.draw.rect(self.screen, (0,0,0), rect)
                row += 1
            line += 1
        if self.counter_size >= self.case_size:
            return True
        return False

class Button():
    def __init__(self, screen, text, y):
        self.screen = screen
        self.color = (180,180,180)
        self.text = text
        self.font = pygame.font.SysFont("Impact", 32)
        self.y = y
    
    def update(self, x, clickable = True):
        self.button = self.font.render(self.text, True, self.color)
        self.rect = self.button.get_rect()
        self.rect.center = (x, self.y)
        self.screen.blit(self.button, self.rect)
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]) and clickable:
            self.color = (255,255,255)
            if pygame.mouse.get_pressed()[0]:
                return True
        else: self.color = (180,180,180)
        return False