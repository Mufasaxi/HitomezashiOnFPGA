import pygame
import random

WIDTH = 1280
HEIGHT = 720
SIZE = 40

win = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
clock = pygame.time.Clock()


def divide(num1, num2):
    result = 0

    while (num1 >= num2):
        num1 = num1 - num2
        result += 1

    return result


def multiply(n1, n2):
    result = 0
    for i in range(n2):
        result += n1
    return result


while running:
    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((135, 80, 148))

    rows = []
    columns = []

    # creating 2 random bit streams for the rows and columns
    for i in range(SIZE):
        rows.append(random.randint(0, 1))
        columns.append(random.randint(0, 1))

    # drawing the horizontal lines
    for y in range(SIZE):
        if rows[y] == 0:
            start_pos = 0
        else:
            start_pos = 1

        for x in range(start_pos, SIZE, 2):
            pygame.draw.rect(win, (162, 205, 72),
                             [multiply(x, (divide(WIDTH, SIZE))), multiply(y, (divide(WIDTH, SIZE))),
                              (divide(WIDTH, SIZE)), 3])

    # drawing the vertical lines
    for x in range(SIZE):
        if columns[x] == 0:
            start_pos = 0
        else:
            start_pos = 1

        for y in range(start_pos, SIZE, 2):
            pygame.draw.rect(win, (162, 205, 72),
                             [multiply(x, (divide(WIDTH, SIZE))), multiply(y, (divide(WIDTH, SIZE))), 3,
                              (divide(WIDTH, SIZE))])

    pygame.display.update()
