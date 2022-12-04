import pygame
import copy

class Player():
    def __init__(self, x, y, x_arrivate, y_arrivate, maze_data, case_size, screen):
        self.screen = screen
        self.move_x = 0
        self.move_y = 0
        self.x = x * case_size
        self.y = y * case_size
        self.case_size = case_size
        self.arrivate = (x_arrivate, y_arrivate)
        self.maze_data = maze_data
        self.velocity = 0
        self.max_velocity = 10

    def update(self):
        if not self.move_x and not self.move_y:
            if not self.test_key():
                self.velocity = 0
        else:
            sign_velocity = abs(self.velocity) == self.velocity
            sign_move = abs(self.move_x) == self.move_x or abs(self.move_x) == self.move_x
            if not sign_velocity == sign_move: self.velocity = 0
            if abs(self.velocity) != self.max_velocity:
                if self.move_x < 0 or self.move_y < 0: self.velocity -= 2
                elif self.move_x > 0 or self.move_y > 0: self.velocity += 2
            if abs(self.move_x) > 0:
                if not abs(self.move_x) - abs(self.velocity) <= 0:
                    self.move_x -= self.velocity
                    self.x += self.velocity
                else:
                    self.x += self.move_x
                    self.move_x = 0
            if abs(self.move_y) > 0:
                if not abs(self.move_y) - abs(self.velocity) <= 0:
                    self.move_y -= self.velocity
                    self.y += self.velocity
                else:
                    self.y += self.move_y
                    self.move_y = 0
        print(self.velocity)
        self.draw()
    
    def draw(self):
        rect = pygame.Rect(0, 0, self.case_size - 5, self.case_size - 5)
        rect.center = (self.x + self.case_size//2, self.y + self.case_size//2)
        pygame.draw.rect(self.screen, (255, 0, 0), rect, border_radius=3)

    def test_key(self):
        x = copy.deepcopy(self.x)//self.case_size
        y = copy.deepcopy(self.y)//self.case_size
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.maze_data[y][x + 1]:
            self.move_x += self.case_size
            return True
        elif keys[pygame.K_LEFT] and self.maze_data[y][x - 1]:
            self.move_x -= self.case_size
            return True
        elif keys[pygame.K_UP] and self.maze_data[y - 1][x]:
            self.move_y -= self.case_size
            return True
        elif keys[pygame.K_DOWN] and self.maze_data[y + 1][x]:
            self.move_y += self.case_size
            return True
        else: return False