#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pygame
from pygame.draw import *
from random import randint
import math
pygame.init()
FPS = 3
screen = pygame.display.set_mode((1200, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Target:
    '''задает параметры начальной мишени'''
    def __init__(self):
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(15, 50)
        self.color = COLORS[randint(0, 5)]
        circle(screen, self.color, (self.x, self.y),self.r )

    def new_target(self):
        """Координаты мишени"""
        circle(screen,(0,0,0), (self.x, self.y), self.r)
        x = self.x = randint(600, 780)
        y = self.y = randint(300, 550)
        r = self.r =  randint(15,50)
        color=self.color = COLORS[randint(0, 5)]
        circle(screen,color,(x,y),r)
        pygame.display.update()

class Ball:
    '''задает параметры шара'''
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.r = 10
        self.color=COLORS[randint(0, 5)]
        circle(screen,self.color,(self.x,self.y),self.r)
        pygame.display.update()
    def move(self,x_change,y_change):
        '''задает движение шара'''
        circle(screen,(0,0,0),(self.x,self.y),self.r)
        self.x+=x_change
        self.y+=y_change
        circle(screen, self.color, (self.x, self.y), self.r)
        pygame.display.update()
class Gun:
    '''Задает параметры пушки'''
    def __init__(self,x=40,y=460,x1=70,w=10):
        self.x = x
        self.y = y
        self.w = w
        self.x1 = x1
        self.y1 = y
        self.color = COLORS[randint(0, 5)]
        line(screen,self.color,(self.x,self.y),(self.x1,self.y1),self.w)
        pygame.display.update()
    def Gun_aim(self,x,y):
        '''движение пушки'''
        line(screen, (0,0,0), (self.x, self.y), (self.x1, self.y1), self.w)
        self.y1 = y
        self.x1 = x
        line(screen, self.color, (self.x, self.y), (self.x1,self.y1), self.w)
        pygame.display.update()

pygame.display.update()
clock = pygame.time.Clock()
finished = False
screen.fill(BLACK)
New_target=Target()
new_gun=Gun()
count=0

while finished == False:
    strike = False
    click = False
    clock.tick(FPS)
    h=30
    while strike == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Пушка попала',str(count),'раза')
                #pygame.quit()
                finished = True
                strike = True
            elif event.type == pygame.MOUSEMOTION:
                x2 = event.pos[0]
                y2 = event.pos[1]
                tg_angle = (460-y2)/(x2-40)
                alpha = math.atan(tg_angle)
                coordinate_Gun_x= int(40+h*math.cos(alpha))
                coordinate_Gun_y= int(460-h * math.sin(alpha))
                new_gun.Gun_aim(coordinate_Gun_x,coordinate_Gun_y)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x = event.pos[0]
                    y = event.pos[1]
                    tg_angle = (460 - y) / (x - 40)
                    alpha = math.atan(tg_angle)
                if  event.button == 3:
                    coordinate_Gun_x = int(40 + h * math.cos(alpha))
                    coordinate_Gun_y = int(460 - h * math.sin(alpha))
                    new_gun.Gun_aim(coordinate_Gun_x, coordinate_Gun_y)
                    if h<=50:
                        h+=5

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    coordinate_ball_x = int(40 + h * math.cos(alpha))
                    coordinate_ball_y = int(460 - h * math.sin(alpha))
                    New_ball = Ball(coordinate_ball_x,coordinate_ball_y)
                    x_change=int(h*math.cos(alpha))
                    y_change=-int(20 * math.sin(alpha))
                    while New_ball.y<=600 and New_ball.x<=1200 and ((New_target.x-New_ball.x)**2 + (New_target.y-New_ball.y)**2) > ((New_target.r+New_ball.r)**2):
                        clock.tick(40)
                        New_ball.move(x_change,y_change)
                        y_change+=1
                        if ((New_target.x-New_ball.x)**2 + (New_target.y-New_ball.y)**2) < ((New_target.r+New_ball.r)**2):
                            count+=1
                    else:
                        while New_ball.y <= 600 and New_ball.x <= 1200:
                            clock.tick(40)
                            New_ball.move(x_change, y_change)
                            y_change += 1
                        circle(screen,(0,0,0),(New_ball.x,New_ball.y),10)
                    strike=True
    New_target.new_target()

pygame.quit()


# In[ ]:





# In[ ]:




