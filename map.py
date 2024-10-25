import pygame as pg
from settings import * 

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],   
    [1, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, 1, 1, 1, 1, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, 1, _, _, 1, 1, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1, _, _, 1, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1, _, _, 1, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.tile_width = WIDTH // len(self.mini_map[0])   # Calculate tile width
        self.tile_height = HEIGHT // len(self.mini_map)    # Calculate tile height
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        for pos in self.world_map:
            pg.draw.rect(
                self.game.screen, 'darkgray',
                (pos[0] * self.tile_width, pos[1] * self.tile_height, self.tile_width, self.tile_height), 2
            )
