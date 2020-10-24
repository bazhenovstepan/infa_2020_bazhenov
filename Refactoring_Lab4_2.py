#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pygame
import pygame.gfxdraw
from pygame.draw import*
import numpy

pygame.init()

WHITE = (255,255,255) # Белый цвет
BLACK = (0,0,0) # Чёрный цвет
BLUE = (180,210,245) # Голубой цвет
GRAY = (180,180,180) # Серый цвет
LIME = (160,255,130) # Цвет зелёной поляны (оттенок зеленого)
GREEN = (140,235,70) # Цвет зеленых кустов (оттенок зеленого)
YELLOW = (255,255,0) # Жёлтый цвет
PURPLE = (230, 130, 200) # Фиолетовый цвет
RED = (255,0,0) # Красный цвет

sc = pygame.display.set_mode((620, 760))

# sc - главная плоскость, голубого цвета (задаёт цвет небу на рисунке)

sc.fill(BLUE)

# Рисуем серые горы

polygon(sc, GRAY, [(0,280), (80,80),(150,220), (230, 120), (370,360), (480, 100), (520, 140), (620, 20), (620, 430), (0,430), (0,280)], 0)
aalines(sc, BLACK, False, [(0,280), (80,80),(150,220), (230, 120), (370,360), (480, 100), (520, 140), (620, 20)])

back = pygame.Surface((620, 760))
back.fill(GRAY)
sc.blit(back, (0,430))

# Рисуем зеленую поляну

polygon(sc, LIME, [(0,455), (30,445), (60,440), (76,440), (136, 435), (300, 435), (307, 437), (310, 436), (312,440), (316,443), (316,460), (318,462), (318, 500), (325,502),(330,504),(620,504), (620,760), (0,760),(0,455)], 0)
aalines(sc, BLACK, False, [(0,455), (30,445), (60,440), (76,440), (136, 435), (300, 435), (307, 437), (310, 436), (312,440), (316,443), (316,460), (318,462), (318, 500), (325,502),(330,504),(620,504)])

flower = pygame.Surface((620,760))
flower.fill(RED)
flower.set_colorkey(RED)
circle(flower, GREEN, (520, 640), 90)

k = pygame.Surface((400,400))
k.fill(RED)
k.set_colorkey(RED)

a = 200
b = 200

d = a 
t = b - 35
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)
    
d = a + 55
t = b - 20
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)
    
d = a - 55
t = b - 25
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)
    
pygame.gfxdraw.filled_ellipse(k,a,b,50,20,YELLOW)
    
d = a - 90
t = b + 5
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)

pygame.gfxdraw.filled_ellipse(k,a,b,50,20,YELLOW)

d = a + 80
t = b
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)
      
d = a - 40
t = b + 20
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)
    
d = a + 40
t = b + 25
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)

flower1 = pygame.transform.scale(k, (k.get_width()//4,k.get_height()//4))
flower2 = pygame.transform.scale(k, (k.get_width()//5,k.get_height()//5))

def flower_1(x,y,g):
    '''
    Функция рисует большие цветки на зеленом кусте
    flower1 - объект pygame.Surface
    x,y - координаты левого верхнего угла изображения
    g - угол поворота плоскости изображения
    
    '''
    flower.blit(pygame.transform.rotate(flower1, g), (x,y)) 

flower_1(420,530,20)
flower_1(490,630,-10)

def flower_2(x,y,g):
    '''
    Функция рисует маленькие цветки на зеленом кусте
    flower2 - объект pygame.Surface
    x,y - координаты левого верхнего угла изоображения
    g - угол поворота плоскости изображения
    
    '''
    flower.blit(pygame.transform.rotate(flower2, g), (x,y))
    
flower_2(510,550, -30)
flower_2(430,600,20)
flower_2(500,590,-40)

animal = pygame.Surface((620,760))
animal.fill(RED)
animal.set_colorkey(RED)

telo = pygame.Surface((620,760))
telo.fill(RED)
telo.set_colorkey(RED)

def risuem_telo(surface,x,y,width,height,color):
    '''
    Функция рисует тело животного
    surface - объект pygame.Surface
    x,y - координаты левого верхнего угла изображения
    width,height - ширина и высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    
    '''
    pygame.gfxdraw.filled_ellipse(surface,x,y,width,height,color)

risuem_telo(telo,180,580,60,25,WHITE)

neck = pygame.Surface((500,500))
neck.fill(GREEN)
neck.set_colorkey(GREEN)

def risuem_sheyu(surface,x,y,width,height,color):
    '''
    Функция рисует шею животного
    surface - объект pygame.Surface
    x,y - координаты левого верхнего угла изображения
    width,height - ширина и высота изображения
    color - цвет, заданный в форматe, подходящем для pygame.Color
    
    '''
    pygame.gfxdraw.filled_ellipse(surface,x,y,width,height,color)

risuem_sheyu(neck,122,130,50,18,WHITE)

sheya = pygame.transform.rotate(neck,90)

roga = pygame.Surface((60,80))
roga.set_colorkey(BLACK)
horn1  = pygame.Surface((600,600))
horn1.fill(GREEN)
horn1.set_colorkey(GREEN)
polygon(horn1, WHITE, [(50,50),(54,58),(60,62),(68,64),(74,74),(70,74),(60,68),(56,64),(54,60),(52,56),(50,50)],0)
horn2 = horn1.copy()

def risuem_rog(surface, x,y):
    '''
    Функция рисует рог животного
    surface - объект pygame.Surface
    x,y - координаты левого верхнего угла изображения
    
    '''
    roga.blit(surface, (x,y))

risuem_rog(horn1,-30,-30)
risuem_rog(horn2, -40, -25)

golova = pygame.Surface((500,500))
golova.fill(GREEN)
golova.set_colorkey(GREEN)

def risuem_golovu(surface,x,y,width,height,color):
    '''
    Функция рисует голову животного
    surface - объект pygame.Surface
    x,y - координаты левого верхнего угла изображения
    width,heigth - ширина и высота изображения
    color - цвет, заданный в форматe, подходящем для pygame.Color
    
    '''
    pygame.gfxdraw.filled_ellipse(surface,x,y,width,height,color)
    
risuem_golovu(golova,142,319,22,14,WHITE)

def risuem_glaz(surface,x,y,radius,color):
    '''
    Функция рисует глаз животного
    surface - объект pygame.Surface
    x,y - координаты левого верхнего угла изображения
    radius - радиус окружности
    color - цвет, заданный в форматe, подходящем для pygame.Color
    
    '''
    pygame.gfxdraw.filled_circle(surface,x,y,radius,color)

risuem_glaz(golova,140,317,9,PURPLE)
risuem_glaz(golova,143,316,4,BLACK)

eye = pygame.Surface((1200,700))
eye.fill(GREEN)
eye.set_colorkey(GREEN)
pygame.gfxdraw.filled_ellipse(eye,885,665,70,30,WHITE)
eyeball = pygame.transform.scale(eye, (eye.get_width()//16,eye.get_height()//16))

glazok = pygame.transform.rotate(eyeball,-30)

leg = pygame.Surface((600,600))
leg.fill(GREEN)
leg.set_colorkey(GREEN)

def risuem_nogu(surface,x,y,width,height,color):
    '''
    Функция рисует ногу животного
    surface - объект pygame.Surface
    x,y - координаты левого верхнего угла изображения
    width,height - ширина и высота изображения
    color - цвет, заданный в форматe, подходящем для pygame.Color
    
    '''
    pygame.gfxdraw.filled_ellipse(surface,x,y,width,height,color)

risuem_nogu(leg,88,63,24,10,WHITE)
risuem_nogu(leg,107,37,24,10,WHITE)
risuem_nogu(leg,88,120,24,10,WHITE)
risuem_nogu(leg,107,100,24,10,WHITE)

risuem_nogu(leg,46,63,20,10,WHITE)
risuem_nogu(leg,65,37,20,10,WHITE)
risuem_nogu(leg,46,120,20,10,WHITE)
risuem_nogu(leg,65,100,20,10,WHITE)

noga = pygame.transform.rotate(leg, 90)

stupnya = pygame.Surface((600,600))
stupnya.fill(GREEN)
stupnya.set_colorkey(GREEN)

def risuem_stupnyu(surface,x,y,width,height,color):
    '''
    Функция рисует ступню ноги животного
    surface - объект pygame.Surface
    x,y - координаты левого верхнего угла изображения
    width,height - ширина и высота изображения
    color - цвет, заданный в форматe, подходящем для pygame.Color
    
    '''
    pygame.gfxdraw.filled_ellipse(surface,x,y,width,height,color)
    
risuem_stupnyu(stupnya,21,160,10,7,WHITE)
risuem_stupnyu(stupnya,84,160,10,7,WHITE)
risuem_stupnyu(stupnya,47,179,10,7,WHITE)
risuem_stupnyu(stupnya,104,179,10,7,WHITE)

def risuem_zhivotnoe(surface, x,y):
    '''
    Функция рисует животное
    surface - объект pygame.Surface
    x,y - координаты левого верхнего угла изображения
    
    '''
    animal.blit(surface, (x,y))

risuem_zhivotnoe(roga,199,421)
risuem_zhivotnoe(sheya,100,150)
risuem_zhivotnoe(golova, 100,150)
risuem_zhivotnoe(glazok,190,400)
risuem_zhivotnoe(noga,100,100)
risuem_zhivotnoe(stupnya, 120,500)
risuem_zhivotnoe(telo, 0,0)

# Копируем изображения животных, отражаем их относительно вертикали и изменяем их размер

animal1 = pygame.transform.scale(animal, (animal.get_width()*2, animal.get_height()*2))
animal2 = pygame.transform.scale(animal, (animal.get_width()//2, animal.get_height()//2))
animal3 = pygame.transform.scale(animal, (animal.get_width()//2, animal.get_height()//2))
animal4 = pygame.transform.scale(animal, (animal.get_width()//2, animal.get_height()//2))
animal5 = pygame.transform.scale(animal, (720,860))
animal6 = pygame.transform.flip(animal5,True,False)
animal7 = pygame.transform.flip(animal4,True,False)

# Копируем изображения зеленых кустов и изменяем их размер

bush1 = pygame.transform.scale(flower, (flower.get_width()//3, flower.get_height()//3))
bush2 = pygame.transform.scale(flower, (flower.get_width()//3, flower.get_height()//3))
bush3 = pygame.transform.scale(flower, (flower.get_width()//3, flower.get_height()//3))
bush4 = pygame.transform.scale(flower, (360,450))
bush5 = pygame.transform.scale(flower, (280, 350))
bush6 = pygame.transform.scale(flower, (420, 560))

def kust(surface,x,y):
    '''
    Функция отображает на плоскости "sc" изображение зеленого куста с цветами
    surface - объект pygame.Surface
    x,y - координаты левого верхнего угла изображения
    
    '''
    sc.blit(surface, (x,y))
    
kust(bush1, -152,261)
kust(bush2, 270,323)
kust(bush3, 450,520)
kust(bush4, 180,300)
kust(bush5, 360,200)
kust(bush6, 260,150)

def zhivotnoe(surface,x,y):
    '''
    Функция оторажает на плоскости "sc" изображение животного
    surface - объект pygame.Surface
    x,y - координаты левого верхнего угла изображения
    
    '''
    sc.blit(surface, (x,y))
    
zhivotnoe(animal1, -400,-350)
zhivotnoe(animal2, 160,130)
zhivotnoe(animal3, 80,220)
zhivotnoe(animal6, 115,-52)
zhivotnoe(animal7, 80,270)

help(flower_1)
help(flower_2)
help(risuem_telo)
help(risuem_sheyu)
help(risuem_rog)
help(risuem_golovu)
help(risuem_glaz)
help(risuem_nogu)
help(risuem_stupnyu)
help(risuem_zhivotnoe)
help(kust)
help(zhivotnoe)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()


# In[ ]:





# In[ ]:




