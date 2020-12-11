#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 10
screen = pygame.display.set_mode((900, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
count=0
def new_ball():

    '''рисует новый шарик '''
    global x, y, r, x1, y1, r1
    x = randint(100, 500)
    y = randint(100, 500)
    r = randint(10, 80)
    x1 = randint(100, 500)
    y1 = randint(100, 500)
    r1 = randint(10, 80)
    color = COLORS[randint(0, 5)]
    color1 = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    circle(screen, color1, (x1, y1), r1)
    x_change = randint(-15, 15)
    y_change = randint(-15, 15)
    x1_change = randint(-15, 15)
    y1_change = randint(-15, 15)
    for i in range(20):
        clock.tick(15)
        pygame.display.update()
        screen.fill(BLACK)
        x+=x_change
        y+=y_change
        y1+=y1_change
        x1+=x1_change
        circle(screen, color1, (x1, y1), r1)
        circle(screen, color, (x, y), r)
        if (x+r) >= 900  or (x-r)<=0:
            x_change =0-x_change
        elif (y+r)>=700 or (y-r) <=0:
            y_change = 0-y_change
        elif (x1+r1) >= 900  or (x1-r1)<=0:
            x1_change =0-x1_change
        elif (y1+r1)>=700 or (y1-r1) <=0:
            y1_change = 0-y1_change








def click(event):
    print(x, y, r)
    global count
    a=(event.pos[0]-x)**2+(event.pos[1]-y)**2
    print(a,r**2)
    if a<=(r**2):
        print('мяч пойман')
        count += 1
    a1 = (event.pos[0] - x1) ** 2 + (event.pos[1] - y1) ** 2
    print(a1, r1 ** 2)
    if a1 <= (r1 ** 2):
        print('мяч пойман')
        count += 1

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                print('Click!')
                click(event)

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
print('Поймано мячей',count)


# In[ ]:




