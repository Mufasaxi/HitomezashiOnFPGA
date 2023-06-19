import pygame
import random

WIDTH = 1280
HEIGHT = 720
SIZE = 40
rowOptions = [[0,0,1,0,0,0,0,0,1,0,1,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,1,0,1,1,1,0], 
              [0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,1,0,0,0,0,1,1,1,0,0,0,1,1,0,1], 
              [1,1,0,1,0,1,0,0,0,0,1,1,1,1,0,1,0,0,1,1,1,0,0,0,0,1,0,1,1,1,1,0,1,0,1,1,0,1,1,0]]

rows = rowOptions[0]

columnOptions = [[1,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0], 
                 [0,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,0,1,1,0,0,1,0,0,0,1,1,0,1,0,0,0,0,0], 
                 [1,1,0,1,0,0,1,1,0,0,0,1,0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,0,0,1,1,0,1,0,1,0,0,1,1]]

columns = columnOptions[0]

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
            pygame.display.update()
            #print('in rect')


            
""" def randBitStream(start_state):
    state = start_state
    output = []

    for i in range(40):
        output.append(state & 1)
        bit = (state ^ (state >> 1)) & 1
        state = (state >> 1) | (bit << 5)
        
    return output """


while running:
    clock.tick(1)
    BITCHOICE = pygame.USEREVENT
    pygame.time.set_timer(BITCHOICE, 1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # creating 2 random bit streams for the rows and columns
        elif event.type == BITCHOICE:
            print("choice")
            for i in range(3):
                for j in range(3):
                    rows = rowOptions[i]
                    columns = columnOptions[j]

    win.fill((135, 80, 148))
    

    # drawing the horizontal lines
    for y in range(SIZE):
        if rows[y] == 0:
            start_pos = 0
        else:
            start_pos = 1

        for x in range(start_pos, SIZE, 2):
            rectangle(win, (162, 205, 72), multiply(x, (divide(WIDTH, SIZE))), multiply(y, (divide(WIDTH, SIZE))),
                      (divide(WIDTH, SIZE)), 3)

    # drawing the vertical lines
    for x in range(SIZE):
        if columns[x] == 0:
            start_pos = 0
        else:
            start_pos = 1

        for y in range(start_pos, SIZE, 2):
            rectangle(win, (162, 205, 72), multiply(x, (divide(WIDTH, SIZE))), multiply(y, (divide(WIDTH, SIZE))), 3,
                      (divide(WIDTH, SIZE)))

