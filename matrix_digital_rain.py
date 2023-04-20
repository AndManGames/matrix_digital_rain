import pygame
import random

# initialize pygame
pygame.init()

# set window size
window_size = (1080, 1920)
screen = pygame.display.set_mode(window_size)

# set colors
white = (255, 255, 255)
green = (0, 255, 0)

# set font
font = pygame.font.SysFont(None, 25)

# create list of characters
chars = []
for i in range(33, 127):
    chars.append(chr(i))

# create list of drops
drops = []
for i in range(100):
    drops.append([random.randint(0, window_size[0]), random.randint(0, window_size[1]), random.randint(10, 20)])

# set clock
clock = pygame.time.Clock()

# main loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # draw background
    screen.fill((0, 0, 0))

    # update drops
    for drop in drops:
        # move drop down
        drop[1] += drop[2]

        # check if drop is off screen
        if drop[1] > window_size[1]:
            # reset drop to top of screen
            drop[0] = random.randint(0, window_size[0])
            drop[1] = random.randint(-100, -10)
            drop[2] = random.randint(10, 20)

        # draw drop
        text = font.render(random.choice(chars), True, green)
        screen.blit(text, (drop[0], drop[1]))

    # update screen
    pygame.display.update()

    # set frame rate
    clock.tick(30)
