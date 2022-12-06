import random
import copy
import pygame

class MazeCreator():
    def __init__(self):
        pass

    def create_empty_maze(self):
        #initialize variable for the creation
        self.move_stack = []
        self.maze_data = []
        for i in range(0, self.num_of_case):
            line = []
            for i in range(0, self.num_of_case):
                line.append(0)
            self.maze_data.append(line)
        self.maze_data[1][1] = 1
        self.maze_data[1][0] = 2
        self.maze_data[self.num_of_case - 2][self.num_of_case - 1] = 2
        #initialize position
        self.x = 1
        self.y = 1

    def create_maze(self, num_of_case, case_size):
        #case of the screen
        self.num_of_case = num_of_case
        self.case_size = case_size

        self.create_empty_maze()
        load_maze = True

        while load_maze:
            possibility = []
            #see possibility of deplacement
            if self.x-2 > 0 and self.maze_data[self.y][self.x-2] == 0:
                possibility.append("west")
            if self.x+2 < num_of_case - 1:
                if self.maze_data[self.y][self.x+2] == 0:
                    possibility.append("east")
            if self.y-2 > 0 and self.maze_data[self.y-2][self.x] == 0:
                possibility.append("north")
            if self.y+2 < num_of_case - 1:
                if self.maze_data[self.y+2][self.x] == 0:
                    possibility.append("south")

            if possibility:
                move = random.choice(possibility)
                if move == "west":
                    self.maze_data[self.y][self.x-1] = 1
                    self.maze_data[self.y][self.x-2] = 1
                    self.x -= 2
                if move == "east":
                    self.maze_data[self.y][self.x+1] = 1
                    self.maze_data[self.y][self.x+2] = 1
                    self.x += 2
                if move == "north":
                    self.maze_data[self.y-1][self.x] = 1
                    self.maze_data[self.y-2][self.x] = 1
                    self.y -= 2
                if move == "south":
                    self.maze_data[self.y+1][self.x] = 1
                    self.maze_data[self.y+2][self.x] = 1
                    self.y += 2
                self.move_stack.append((copy.deepcopy(self.x), copy.deepcopy(self.y)))
            else:
                if self.move_stack:
                    self.x, self.y = self.move_stack.pop()
                else:
                    load_maze = False
        return self.maze_data, (self.num_of_case - 2,self.num_of_case - 1)