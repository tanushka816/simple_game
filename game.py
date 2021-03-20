import pygame
from constants import *
from player import *
from enemies import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.back = pygame.image.load('paper.jpg').convert()
        self.all_sprite_list = pygame.sprite.Group()
        self.bombs_list = pygame.sprite.Group()
        self.lines_list = pygame.sprite.Group()

        # self.player = Player(WIDTH//2, HEIGHT//2, 'pu.png')
        # self.all_sprite_list.add(self.player)

        # consts =   [(200, 200, 1, 2, 20, 'r.png'), 
        #             (350, 320, 3, 2, 40, 'o.png'), 
        #             (400, 250, 3, 4, 60, 'y.png'), 
        #             (200, 350, 5, 4, 40, 'g.png'), 
        #             (400, 350, 5, 6, 60, 'b.png'), 
        #             (350, 400, 9, 8, 20, 'pu.png')]
        self.name_choose_pict = 'y.png'
        consts =   [(100, 100, 1, 2, 20, 'r.png'), 
                    (400, 320, 3, 2, 40, 'o.png'), 
                    (600, 300, 3, 4, -60, 'y.png'), 
                    (200, 350, 5, 4, 80, 'g.png'), 
                    (400, 350, 5, 6, 60, 'b.png'), 
                    (350, 400, 9, 8, 20, 'pu.png')]
        self.players_vars = pygame.sprite.Group()
        for c in consts:
            pl = FullyPlayer(*c)
            self.players_vars.add(pl)

        self.lines = pygame.sprite.Group()

        self.state = 'MENU'  # 'GAME'  'PAUSE'  ''
        self.start_t = pygame.time.get_ticks()

    def create_enemies(self):  # rockets
        pass

    def create_lines(self):  # lines
        lines_c = [(400, -50, 1, 800), (-50, 300, 800, 8)]
        for pre_line in lines_c:
            line = Line(*pre_line)
            self.lines.add()
            self.all_sprite_list.add(line)
        
    def handle_scene(self, e):
        if self.state == 'MENU':
            # if e.type == pygame.MOUSEMOTION:
            for fpl in self.players_vars:
                # print(0)
                pict = fpl.check_click(e)
                if pict:
                    self.name_choose_pict = pict
                    print(pict)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:  # enter ~ return
                    self.state = 'GAME' 
                    self.player = Player(WIDTH//2, HEIGHT//2, self.name_choose_pict)
                    self.all_sprite_list.add(self.player)
            

        if self.state == 'GAME':
            # print(1)
            if e.type == pygame.KEYDOWN:
                for i in range(5):
                    if e.key == KEYS[i]:
                        self.player.dir = i
            if e.type == pygame.KEYUP:
                for i in range(5):
                    if e.key == KEYS[i]:
                        self.player.dir = 0
            self.player.go_on()

    def draw_scene(self):
        self.screen.blit(self.back, (0, 0))
        if self.state == 'MENU':
            self.players_vars.draw(self.screen)

        elif self.state == 'GAME':
            self.all_sprite_list.draw(self.screen)

    def update_scene(self):
        if self.state == 'MENU':
            t = pygame.time.get_ticks() - self.start_t
            self.players_vars.update(t//20)

        elif self.state == 'GAME':
            self.all_sprite_list.update()
    

    def run(self):
        # self.screen.fill((10, 10, 100))
        '''surf = pygame.Surface((50, 20))
        surf.fill((10, 200, 10))
        surf2 = pygame.transform.rotate(surf, 35)
        surf2.fill((200, 200, 100))'''
        self.create_lines()
        while True:
            # self.screen.blit(self.back, (0, 0))
            '''self.screen.blit(surf, (200, 200))
            self.screen.blit(surf2, (300, 200))'''
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                self.handle_scene(e)
            #     if e.type == pygame.KEYDOWN:
            #         for i in range(5):
            #             if e.key == KEYS[i]:
            #                 self.player.dir = i
            #     if e.type == pygame.KEYUP:
            #         for i in range(5):
            #             if e.key == KEYS[i]:
            #                 self.player.dir = 0
            # self.player.go_on()

            # self.all_sprite_list.update()
            # self.all_sprite_list.draw(self.screen)
            self.update_scene()
            self.draw_scene()
            pygame.display.update()
            # pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

    
game = Game()
game.run()
