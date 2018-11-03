import pygame
from random import choice

from .snake import Snake
from .scoreboard import Scoreboard
from .spatial import Point, apply_scale

WHITE = 255,255,255
RED = 0xff,0x08,0x00
BLACK = 0,0,0

class Frame(object):
    def __init__(self, grid_shape=(100,50), scale=10):
        self.scale = scale
        self.snake = Snake()
        self.scoreboard = Scoreboard()
        self.grid_shape = grid_shape
        self.grid_width = grid_shape[0]
        self.grid_height = grid_shape[1]
        self.field = {Point(x,y) for x in range(1,self.grid_width) for y in range(self.grid_height-1)}
        self.display_shape = (self.grid_width*scale, self.grid_height*scale)
        self.screen = pygame.display.set_mode(self.display_shape)
        self.make_apple()

    def snake_is_out_of_bounds(self):
        return not (
            (0 < self.snake.head.x < self.grid_width)
            and
            (-1 < self.snake.head.y < self.grid_height-1)
        )

    def get_open_field(self):
        return self.field - set(self.snake.coords)

    def make_apple(self):
        self.apple = Point(*choice(list(self.get_open_field())))
        return self.apple

    def draw(self):
        self.screen.fill(WHITE)
        for point in self.snake.coords:
            point = apply_scale(point, self.scale)
            rect = pygame.Rect(
                point.x - self.scale/2, #left
                point.y + self.scale/2, #top
                self.scale, #width
                self.scale  #height
            )
            self.screen.fill(BLACK,rect)
        scaled_apple = apply_scale(self.apple, self.scale)
        rect = pygame.Rect(
            scaled_apple.x - self.scale/2, #left
            scaled_apple.y + self.scale/2, #top
            self.scale, #width
            self.scale  #height
        )
        self.screen.fill(RED,rect)

