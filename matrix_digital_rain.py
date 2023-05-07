import os
import pygame as pg
from random import choice, randrange

text_colors = [
    (0, 255, 102),  # green/turkis
    (0, 204, 51),   # green
    (0, 153, 51),   # green
    (64, 64, 64),   # gray
    (200, 200, 200) # white
]

class Symbol:
    def __init__(self, x, y, speed):
        self.x, self.y = x, y
        self.speed = speed
        self.value = None
        self.interval = randrange(5, 30)

    def draw(self, column_height, index):
        frames = pg.time.get_ticks()
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE

        if not frames % self.interval:
            self.value = choice(font_color)

            # highlight first character:
            if index == 0:
                self.value = choice(font_color_highlight)

            # turn tail gray
            if index > column_height * 0.9:
                self.value = choice(font_color_gray)

        if self.value:
            surface.blit(self.value, (self.x, self.y))

class SymbolColumn:
    def __init__(self, x, y):
        self.column_height = randrange(8, 40)
        self.speed = randrange(3, 7)
        self.symbols = [Symbol(x, i, self.speed) for i in range(y, y - FONT_SIZE * self.column_height, -FONT_SIZE)]

    def draw(self):
        for index, symbol in enumerate(self.symbols):
            symbol.draw(self.column_height, index)

os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 1080, 1920
FONT_SIZE = 25

pg.init()
screen = pg.display.set_mode(RES)
surface = pg.Surface(RES)
clock = pg.time.Clock()

katakana = [chr(int('0x30a0', 16) + i) for i in range(96)]
font = pg.font.Font('font/ms_mincho.ttf', FONT_SIZE)

font_color = []
for char in katakana:
    font_color.append(font.render(char, True, pg.Color(text_colors[1])))

font_color_gray = []
for char in katakana:
    font_color_gray.append(font.render(char, True, pg.Color(text_colors[3])))

font_color_highlight = []
for char in katakana:
    font_color_highlight.append(font.render(char, True, pg.Color(text_colors[4])))

symbol_columns = [SymbolColumn(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE)]

while True:
    screen.blit(surface, (0, 0))
    surface.fill(pg.Color((0, 0, 0)))

    [symbol_column.draw() for symbol_column in symbol_columns]

    [exit() for i in pg.event.get() if i.type == pg.QUIT]
    pg.display.flip()
    clock.tick(60)