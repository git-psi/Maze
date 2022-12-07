import random
import kandinsky
import time
import ion

class MazeCreator():
    def __init__(self):
        pass

    def create_empty_maze(self):
        #initialize variable for the creation
        self.move_stack = []
        self.maze_data = []
        for i in range(0, self.num_of_case[1]):
            line = []
            for i in range(0, self.num_of_case[0]):
                line.append(0)
            self.maze_data.append(line)
        self.maze_data[1][1] = 1
        self.maze_data[1][0] = 2
        self.maze_data[self.num_of_case[1] - 3][self.num_of_case[0] - 2] = 1
        self.maze_data[self.num_of_case[1] - 3][self.num_of_case[0] - 1] = 2
        #initialize position
        self.x = 1
        self.y = 1

    def create_maze(self):
        #case of the screen
        self.num_of_case = [64, 46]
        self.case_size = 5

        self.create_empty_maze()
        load_maze = True

        while load_maze:
            possibility = []
            #see possibility of deplacement
            if self.x-2 > 0 and self.maze_data[self.y][self.x-2] == 0:
                possibility.append("west")
            if self.x+2 < self.num_of_case[0] - 1:
                if self.maze_data[self.y][self.x+2] == 0:
                    possibility.append("east")
            if self.y-2 > 0 and self.maze_data[self.y-2][self.x] == 0:
                possibility.append("north")
            if self.y+2 < self.num_of_case[1] - 1:
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
                self.move_stack.append((self.x, self.y))
            else:
                if self.move_stack:
                    self.x, self.y = self.move_stack.pop()
                else:
                    load_maze = False
        return self.maze_data, (self.num_of_case[1] - 3, self.num_of_case[0] - 1)

def draw_maze(maze_data, case_size):
    kandinsky.fill_rect(0, 0, 320, 230, (0,0,0))
    line = 0
    for line_case in maze_data:
        row = 0
        for row_case in line_case:
            if row_case == 1:
                kandinsky.fill_rect(row*case_size, line*case_size, case_size, case_size, (255,255,255))
            if row_case == 2:
                kandinsky.fill_rect(row*case_size, line*case_size, case_size, case_size, (180,180,180))
            row += 1
        line += 1

def player_update(x, y, move_x, move_y):
    if move_x != 0 or move_y != 0:
        kandinsky.fill_rect(x + 1, y+1, 3, 3, (255,255,255))
        if move_x:
            if move_x > 0:
                move_x -= 1
                x += 1
            else:
                move_x += 1
                x -= 1
        if move_y:
            if move_y > 0:
                move_y -= 1
                y += 1
            else:
                move_y += 1
                y -= 1
    kandinsky.fill_rect(x + 1, y+1, 3, 3, (255,0,0))
    return x, y, move_x, move_y

kandinsky.fill_rect(0, 0, 320, 230, (0, 0, 0))

def draw_animation(color, sleep_time):
    for i in range(0, 31):
        x = 65
        kandinsky.fill_rect(x, 130-i*133//100, 10, 2, color)
        kandinsky.fill_rect(x+10, 100+i//3, 10, 1, color)
        kandinsky.fill_rect(x+20, 110+i//3, 10, 1, color)
        kandinsky.fill_rect(x+30, 100+i//3, 10, 1, color)
        kandinsky.fill_rect(x + 40, 130-i*133//100, 10, 2, color)
        x += 60
        kandinsky.fill_rect(x, 130-i, 10, 1, color)
        kandinsky.fill_rect(x + 10 + (i * 100)//150, 90, 1, 10, color)
        kandinsky.fill_rect(x + 30 - (i * 100)//150, 110, 1, 10, color)
        kandinsky.fill_rect(x + 30, 130-i, 10, 1, color)
        x += 50
        kandinsky.fill_rect(x + i, 90, 1, 10, color)
        kandinsky.fill_rect(x + i//3, 113, 1, 7, color)
        kandinsky.fill_rect(x + 10 + (i//3), 107, 1, 7, color)
        kandinsky.fill_rect(x + 30 - i//3, 100, 1, 7, color)
        kandinsky.fill_rect(x + 30 - i, 120, 1, 10, color)
        x += 40
        kandinsky.fill_rect(x + i, 90, 1, 10, color)
        kandinsky.fill_rect(x, i + 90, 10, 1, color)
        kandinsky.fill_rect(x + i*100//150, 105, 1, 10, color)
        kandinsky.fill_rect(x + 30 - i, 120, 1, 10, color)
        time.sleep(sleep_time)


def animation():
    for i in range(0, 64):
        time.sleep(0.005)
        kandinsky.fill_rect(i*5, 0, 5, 230, (255,255,255))
    draw_animation((0,0,0), 0.02)
    time.sleep(2)
    draw_animation((255,255,255), 0.01)
    for i in range(0, 64):
        time.sleep(0.005)
        kandinsky.fill_rect(i*5, 0, 5, 230, (0,0,0))
    

def start():
    animation()
    maze_data , arrivate= MazeCreator().create_maze()
    case_size = 5
    x = 0
    y = case_size
    move_x = 0
    move_y = 0
    draw_maze(maze_data, 5)
    return maze_data, arrivate, x, y, move_x, move_y, case_size

maze_data, arrivate, x, y, move_x, move_y, case_size = start()
run = True
while True:
    if move_x == 0 and move_y == 0:
        if (y//case_size, x//case_size) == arrivate:
            maze_data, arrivate, x, y, move_x, move_y, case_size = start()
        if ion.keydown(ion.KEY_LEFT) and maze_data[y//case_size][x//case_size - 1]: move_x -= case_size
        elif ion.keydown(ion.KEY_RIGHT) and maze_data[y//case_size][x//case_size + 1]: move_x += case_size
        elif ion.keydown(ion.KEY_UP) and maze_data[y//case_size - 1][x//case_size]: move_y -= case_size
        elif ion.keydown(ion.KEY_DOWN) and maze_data[y//case_size + 1][x//case_size]: move_y += case_size
    x, y, move_x, move_y = player_update(x, y, move_x, move_y)
    time.sleep(0.005)