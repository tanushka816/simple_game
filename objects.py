import pygame
import random
from constants import *

class Artifact(pygame.sprite.Sprite):
    
    def __init__(self, born_time):
        super().__init__()
		# self.image = pygame.Surface((10, 10))
        img = random.choice(['a_d.png', 'a_d2.png'])
        self.type = 1
        if img == 'a_d2.png':
            self.type = 2
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, WIDTH - 50)
        self.rect.y = random.randint(50, HEIGHT - 50)
        self.born_time = born_time
        self.ttl = random.randint(500, 7000)
		# self.type_a = type_a # live, shield, many_coins
		# self.coins = pygame.sprite.Group()