import math
import pygame
from constants import KEYS, DX, DY

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, img=None):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()  # или convert_alpha
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
        self.dir = 0
        self.art_count = 0

    def go_on(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.change_x = -2
            if event.key == pygame.K_RIGHT:
                self.change_x = 2
            if event.key == pygame.K_DOWN:
                self.change_y = 2
            if event.key == pygame.K_UP:
                self.change_y = -2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.change_x = 0
            if event.key == pygame.K_RIGHT:
                self.change_x = 0
            if event.key == pygame.K_DOWN:
                self.change_y = 0
            if event.key == pygame.K_UP:
                self.change_y = 0
        
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    

class FullyPlayer(pygame.sprite.Sprite):
    def __init__(self, x, y, a=1, b=2, mult=20, img=None):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()  # или convert_alpha
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self._x = x
        self._y = y
        self.change_x = 0
        self.change_y = 0

        self.liss_a = a
        self.liss_b = b
        self.sigm = math.pi / 2
        self.mult = mult

        self.name = img

    def update(self, t):
        # p.s. https://en.wikipedia.org/wiki/Lissajous_curve
        # t = pygame.time.get_ticks() - self.start_t
        self.rect.x = math.sin(math.radians(self.liss_a * t + self.sigm)) * self.mult + self._x
        self.rect.y = math.sin(math.radians(self.liss_b * t)) * self.mult + self._y

    def check_click(self, event):
        pos_x,pos_y = pygame.mouse.get_pos()
        # check_pos = self.rect.left <= pos_x <= self.rect.right and self.rect.top <= pos_y <= self.rect.bottom
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.name
            # if check_pos: self.state = 'active'
            # else: self.state = 'normal'