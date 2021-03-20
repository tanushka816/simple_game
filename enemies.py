import pygame

class Rocket(pygame.sprite.Sprite):

    def __init__(self, x, y, img):
        super().__init__()
        self.image = pygame.image.load(img).convert()  # или convert_alpha
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0

    def calc_change(self, x, y):
        '''x, y player's '''
        pass
        
    def update(self):
        self.change_x, self.change_y = self.calc_change()
        

    def draw(self):
        pass



class Line(pygame.sprite.Sprite):

    def __init__(self, x1, y1, w, h, angle=None, x2=0, y2=0, ttl = 2):  # flag = horizontal/vert for update
        super().__init__()
        # rect = pygame.Surface((w, h))
        # self.image = pygame.transform.rotate(rect, 30)
        self.image = pygame.Surface((w, h))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
        self.ttl = ttl

    # def update(self):
    #     # check for hor/vert for change x/y
    #     self.rect.x -= 1

    # def draw(self):
    #     pass