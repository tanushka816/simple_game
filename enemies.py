import math
from sys import platform
import pygame
from random import randint


class Rocket(pygame.sprite.Sprite):

    def __init__(self, x, y, img, c):
        super().__init__()
        img = pygame.image.load(img).convert_alpha()  # или convert_alpha
        random_size = randint(10, 25)
        self.image = pygame.transform.scale(img, (random_size, random_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
        self.start_x = x
        self.start_y = y
        # self.player = player
        self.theta = randint(1, 5)
        self.c = c

    def calc_change(self):
        '''x, y player's '''
        x = self.player.rect.x
        y = self.player.rect.y
        if x < self.rect.x:
            self.rect.x -= 2
        else: 
            self.rect.x += 2
        x0 = (self.rect.x + x) / 2
        y0 = (self.rect.y + y) / 2
        r = math.sqrt((self.rect.x - x0)**2 + (self.rect.y - y0)**2)
        yz = y0 +  math.sqrt(r**2 - (self.rect.x - x0)**2)
        # print(self.rect.x, self.rect.y)
        # print(x0, y0)
        # print(r)
        # print(yz)
        self.rect.y = y0 - math.sqrt(r**2 - (self.rect.x - x0)**2)

    def stike(self):
        x = self.player.rect.x
        y = self.player.rect.y
        if x < self.rect.x:
            self.rect.x -= 1
        else: 
            self.rect.x += 1
        if y < self.rect.y:
            self.rect.y -= 1
        else: 
            self.rect.y += 1

    def arh(self):
        self.theta += 1
        b = (20 - 2) / 2 / 3.14 / 10
        self.rect.x = b*self.theta * math.cos(math.radians(self.theta)) + self.c
        self.rect.y = b*self.theta * math.sin(math.radians(self.theta)) + self.c
        
    def update(self):
        # self.change_x, self.change_y = self.calc_change(350, 250)
        # self.stike()
        self.arh()
        # self.calc_change()    

    def draw(self):
        pass



class Line(pygame.sprite.Sprite):

    def __init__(self, x1, y1, w, h, angle=None, x2=0, y2=0, ttl = 2):  # flag = horizontal/vert for update
        super().__init__()
        # rect = pygame.Surface((w, h))
        # self.image = pygame.transform.rotate(rect, 30)
        self.image = pygame.Surface((w, h))
        self.image.fill((0, 10, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
        self.ttl = ttl

    # def update(self):
    #     # check for hor/vert for change x/y
    #     self.rect.x -= 1

    # def draw(self):
    #     pass