import pygame
import copy
import numpy

class Player():
    def __init__(self, x, y, xy_arrivate, maze_data, case_size, screen):
        self.screen = screen
        self.move_x = 0
        self.move_y = 0
        self.x = x * case_size
        self.y = y * case_size
        self.case_size = case_size
        self.arrivate = xy_arrivate
        self.maze_data = maze_data
        self.velocity = 0
        self.max_velocity = 20
        self.direction = 0
        self.actual_direction = 0
        self.animation = []
        self.color = [0, 0, 255]
        self.color_animation = 0

    def update(self):
        self.change_color()
        self.animation_fun()
        if (self.y//self.case_size, self.x//self.case_size) == self.arrivate:
            print(1111)
        elif not self.move_x and not self.move_y:
            if not self.test_key():
                self.velocity = 0
        else:
            if not self.direction == self.actual_direction:
                self.velocity = 0
            self.actual_direction = copy.deepcopy(self.direction)
            if abs(self.velocity) != self.max_velocity:
                if self.move_x < 0 or self.move_y < 0: self.velocity -= 3
                elif self.move_x > 0 or self.move_y > 0: self.velocity += 3
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
        self.draw()
    
    def draw(self):
        rect = pygame.Rect(0, 0, self.case_size - self.case_size // 5, self.case_size - self.case_size // 5)
        rect.center = (self.x + self.case_size//2, self.y + self.case_size//2)
        pygame.draw.rect(self.screen, self.color, rect, border_radius=2)

    def test_key(self):
        x = copy.deepcopy(self.x)//self.case_size
        y = copy.deepcopy(self.y)//self.case_size
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.maze_data[y][x + 1]:
            self.move_x += self.case_size
            self.direction = 1
            self.animation.append([x, y, copy.deepcopy(self.case_size)])
            return True
        elif keys[pygame.K_LEFT] and self.maze_data[y][x - 1] and x > 0:
            self.move_x -= self.case_size
            self.direction = 2
            self.animation.append([x, y, copy.deepcopy(self.case_size)])
            return True
        elif keys[pygame.K_UP] and self.maze_data[y - 1][x] and y > 0:
            self.move_y -= self.case_size
            self.direction = 3
            self.animation.append([x, y, copy.deepcopy(self.case_size)])
            return True
        elif keys[pygame.K_DOWN] and self.maze_data[y + 1][x]:
            self.move_y += self.case_size
            self.direction = 4
            self.animation.append([x, y, copy.deepcopy(self.case_size)])
            return True
        else: 
            return False

    def animation_fun(self):
        for i in self.animation:
            if i[2] > 0:
                color = copy.deepcopy(self.color)
                for rgb in range(0, len(color)):
                    if color[rgb] < 255:
                        color[rgb] += 255-(255//self.case_size*i[2])
                        if color[rgb] > 255: color[rgb] = 255
                i[2] -= numpy.divide(self.case_size,25)
                size = self.case_size - (self.case_size-i[2])
                rect = pygame.Rect(0, 0, size, size)
                rect.center = (i[0]*self.case_size + self.case_size//2, i[1]*self.case_size + self.case_size//2)
                pygame.draw.rect(self.screen, color, rect, border_radius=2)
            else: self.animation.remove(i)

    def change_color(self):
        self.color[self.color_animation] += 2
        self.color[self.color_animation - 1] -= 2
        if self.color[self.color_animation] >= 255:
            for rgb in range(0, len(self.color)):
                if self.color[rgb] > 255:
                    self.color[rgb] = 255
                elif self.color[rgb] < 0:
                    self.color[rgb] = 0
            self.color_animation += 1
            if self.color_animation > len(self.color) - 1:
                self.color_animation = 0