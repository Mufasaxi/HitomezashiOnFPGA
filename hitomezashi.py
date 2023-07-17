#!/usr/bin/env python3
import pygame
import random

WIDTH = 1280
HEIGHT = 720
SIZE = 32
rows = [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1,
        1, 1, 0]

columns = [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1,
           0, 0, 0, 0]

count = 0

win = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
clock = pygame.time.Clock()


def divide(num1, num2):
    result = 0

    while (num1 >= num2):
        num1 = num1 - num2
        result += 1

    return result


def multiply(num1, num2):
    result = 0

    for i in range(num2):
        result += num1

    return result


def pixel(surface, colour, pos):
    surface.set_at(pos, colour)


def rectangle(surface, colour, x, y, width, height):
    for i in range(x, x + width):
        for j in range(y, y + height):
            pixel(surface, colour, (i, j))
            # pygame.display.update()
            # print('in rect')


""" def randBitStream(start_state):
    state = start_state
    output = []

    for i in range(40):
        output.append(state & 1)
        bit = (state ^ (state >> 1)) & 1
        state = (state >> 1) | (bit << 5)

    return output """

frame = 0

while running:
    clock.tick(6000)
    frame += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # creating 2 random bit streams for the rows and columns

    win.fill((135, 80, 148))

    # drawing the horizontal lines
    for y in range(720):
        yCell = y // 32
        if rows[yCell] == 0:
            start_pos = 0
        else:
            start_pos = 1

        for x in range(0, 1280):
            if (y % 32) >= 0 and (y % 32) <= 3 and frame > yCell:
                xCell = x // 32
                if ((xCell % 2) ^ start_pos) > 0 and x < frame:# * 10:
                    pixel(win, (162, 205, 72), (x, y))

    # drawing the vertical lines
    for x in range(1280):
        xCell = x // 32
        if columns[xCell] == 0:
            start_pos = 0
        else:
            start_pos = 1

        for y in range(720):
            if(x % 32) >= 0 and (x % 32) <=3 and frame > xCell:
                yCell = y // 32
                if ((yCell % 2) ^ start_pos) > 0 and y < frame :#* 10:
                    pixel(win, (162, 205, 72), (x, y))



    pygame.display.update()