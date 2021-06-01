from objects import Artifact
from random import randint
import random
import pygame
from constants import *
from player import *
from enemies import *
from file_handler import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.back = pygame.image.load('paper.jpg').convert()
        self.all_sprite_list = pygame.sprite.Group()
        self.bombs_list = pygame.sprite.Group()
        self.rockets_list = pygame.sprite.Group()
        self.lines_list = pygame.sprite.Group()
        self.artifact_list = pygame.sprite.Group()
        # константы для начального экрана (выбор персонажа)
        consts =   [(330, 350, 1, 2, 20, 'r.png'), 
                    (330, 350, 3, 2, 40, 'o.png'), 
                    (330, 350, 3, 4, -60, 'y.png'), 
                    (330, 350, 5, 4, 80, 'g.png'), 
                    (330, 350, 5, 6, 60, 'b.png'), 
                    (330, 350, 9, 8, 20, 'pu.png')]  

        # вариаты персонажей (заполняются константами ↑)
        self.players_vars = pygame.sprite.Group()
        for c in consts:
            pl = FullyPlayer(*c)
            self.players_vars.add(pl)
        self.imgs = ['r.png', 'o.png', 'y.png', 'g.png', 'b.png', 'pu.png']  # картинки для создания выбранного персонажа
        self.ex_arr = []  # для учета, что на экране (список, а не группа как self.players_vars)
        for c in consts:
            pl = FullyPlayer(*c)
            self.ex_arr.append(pl)

        self.on_screen_player = pygame.sprite.Group()  # для отображения того, кто на экране сейчас
        self.on_screen_player.add(pl)  # добавляем последнего
        self.menu_on_screen_index = len(consts) - 1  # индекс последнего
        self.active_index = []

        self.state = 'INTRO'  # 'GAME'  'PAUSE', 'INTRO' 'MENU'
        self.start_t = pygame.time.get_ticks()

        # self.menu_font = pygame.font.SysFont('arial', 30)
        self.menu_font = pygame.font.Font('Socialitta.ttf', 60)
        self.menu_font_arrow = pygame.font.SysFont('arial', 60)
        self.menu_text_1 = self.menu_font.render(' For choose press UP ↑', 0, (0, 0, 0))
        self.menu_text_2 = self.menu_font.render('For play press enter', 0, (0, 0, 0))
        self.menu_text_3 = self.menu_font.render('For change press ← →', 0, (0, 0, 0))
        self.pause_text = self.menu_font.render('Pause', 0, (0, 0, 0))
        
        self.menu_text_a_r = self.menu_font_arrow.render('}', 0, (30, 180, 50))  
        # self.active_one_player = .. для одного активного для управленя
        # для экрана game over:
        self.menu_text_a_l = self.menu_font_arrow.render('{', 0, (30, 180, 50))  # 255, 0, 255
        self.go_font = pygame.font.SysFont('arial', 30)
        self.go_text1 = self.go_font.render('GAME OVER', 0, (128, 0, 128))
        self.go_text2 = self.go_font.render('You were alive for', 0, (128, 0, 128))

        self.story_font = pygame.font.Font('19689.otf', 40)  # 19510  19689.otf
        self.text_handler = FileHandlerStory(STORYFILE)
        self.text_ind = 0  # curr text
        self.story_ind = 0  # curr story
        self.text_c = 0  # frames
        self.clear_screen = False
        self.x_text = 90
        self.y_text = 10
        self.curr_text = self.story_font.render('', 0, (0, 0, 0))
        self.clear_text = self.story_font.render('Нажмите ПКМ для продолжения...', 0, (0, 0, 0))
        # print(self.text_handler)
        self.story_pics = {}
        self.load_pics()
        # print(self.story_pics)
        self.sounds = [pygame.mixer.Sound('Nature.mp3'), pygame.mixer.Sound('Sea.mp3'),
                       pygame.mixer.Sound('Fire.mp3')]
        self.sound_ind = 0
        self.sound_change_count = 0  # частное для нахождения остатка
        self.back_sound = self.sounds[self.sound_ind]

        self.intro_sound_ind = 2
        self.intro_sound = self.sounds[self.intro_sound_ind]
        # self.back_sound = pygame.mixer.Sound('Nature.mp3')
        self.last_art_create = 0
        self.artcd = 1000
        self.score_font = pygame.font.Font('19689.otf', 20)
        self.art_player_message = self.score_font.render('', 1, (0, 0, 0))

        self.your_time_f_level = 60 * LEVEL_SEC # 20c
        self.your_time_text = self.score_font.render('Your time: ' + str(self.your_time_f_level//60), 1, (0, 0, 0))


    def create_rockets(self):  # rockets должен вызываться периодически (раз в 10 кадров) ракеты должны помират 
        x = 200
        consts =   [(x + randint(-10, 100), 20, 'r3_.png', 350), 
                    (x + randint(-10, 100), 20, 'r3_.png', 340), 
                    (x + randint(-10, 100), 20, 'r3_.png', 330),
                    (x + randint(-10, 10), 50, 'r3_.png', 200), 
                    (x + randint(-10, 10), 50, 'r3_.png', 210), 
                    (x + randint(-10, 10), 50, 'r3_.png', 180), 
                    (x + randint(-10, 10), 50, 'r3_.png', 190), 
                    (x + randint(-10, 10), 70, 'r3_.png', 100), 
                    (x + randint(-10, 10), 100, 'r3_.png', 200), 
                    (x + randint(-10, 10), 100, 'r3_.png', 210), 
                    (x + randint(-10, 10), 200, 'r3_.png', 400)
                    ]
        for e in consts: 
            enemy = Rocket(*e)
            self.rockets_list.add(enemy)
            self.all_sprite_list.add(enemy)

    def create_lines(self):
        lines_c = [(400, -50, 10, 800), (-50, 300, 800, 8)]
        for pre_line in lines_c:
            line = Line(*pre_line)
            self.lines_list.add(line)
            self.all_sprite_list.add(line)

    def create_artifacts(self):
        n = random.randint(1, 5)
        t = pygame.time.get_ticks()
        for i in range(n):
            art = Artifact(t)
            self.artifact_list.add(art)
            self.all_sprite_list.add(art)


    def time_killer_artifact(self):
        for art in self.artifact_list:
            t = pygame.time.get_ticks()
            if t - art.born_time > art.ttl:
                art.kill()


    def load_pics(self):
        for name_pic in self.text_handler.pics:
            pict = pygame.image.load(name_pic).convert()
            self.story_pics[name_pic] = pict

    def handle_scene(self, e):
        if self.state == 'INTRO':
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_s:
                    self.state = 'MENU'
                    self.intro_sound.stop()
                    self.back_sound.play()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    self.clear_screen = True
                
        # create text or pict -> draw in draw_scene

        elif self.state == 'MENU':
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_s:
                    self.state = 'INTRO'


            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.active_index.append(self.menu_on_screen_index)
                elif e.key == pygame.K_LEFT:  # закольцовано
                    self.menu_on_screen_index = (self.menu_on_screen_index - 1) % len(self.players_vars)
                elif e.key == pygame.K_RIGHT:
                    self.menu_on_screen_index = (self.menu_on_screen_index + 1) % len(self.players_vars)

                self.on_screen_player = pygame.sprite.Group()
                self.on_screen_player.add(self.ex_arr[self.menu_on_screen_index])
                # print(self.on_screen_player)

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:  # enter ~ return
                    self.state = 'GAME'
                    # print('yes')
                    self.back_sound.play()
                    self.start_time = pygame.time.get_ticks()
                    #  здесь теперь должен быть список игроков
                    # self.active_players = pygame.sprite.Group()  # нужно
                    self.active_one_player = Player(350, 350, self.imgs[self.menu_on_screen_index])
                    self.all_sprite_list.add(self.active_one_player)
                    # self.create_rockets()
                    self.create_artifacts()

                        
        elif self.state == 'GAME':
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.state = 'PAUSE'
                if e.key == pygame.K_m:
                    self.back_sound.stop()
                    self.sound_change_count += 1
                    self.sound_ind = self.sound_change_count % len(self.sounds)
                    self.back_sound = self.sounds[self.sound_ind]
                    self.back_sound.play()

            self.active_one_player.go_on(e)


            # ############# if collide
            if pygame.sprite.spritecollide(self.active_one_player, self.lines_list, False):
                # pygame.sprite.spritecollide(self.active_one_player, self.rockets_list, False):
                self.state = 'GAME OVER'
                self.end_time = pygame.time.get_ticks()
                self.in_game_time = self.end_time - self.start_time
                self.time_text = self.go_font.render(str(self.in_game_time), 0, (128, 0, 128))

            art_hit_list = pygame.sprite.spritecollide(self.active_one_player, self.artifact_list, False)
            for art in art_hit_list:
                if art.type == 1:
                    self.active_one_player.art_count += 1
                else:
                    self.active_one_player.art_count += 3
                art.kill()

        elif self.state == 'PAUSE':
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.state = 'GAME'

        elif self.state == 'GAME OVER':
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.state = 'MENU'
                
    
    # прорисовка
    def draw_scene(self):
        # self.screen.blit(self.back, (0, 0))
        if self.state == 'INTRO':
            story = self.text_handler.stories['Лиссажу']
            if self.text_c > STORY_LINE_SEC * 60:
                if self.text_ind >= len(story):
                    self.story_ind += 1
                    self.text_ind = 0

                if self.story_ind >= len(story) or self.text_ind >= len(story[self.story_ind]):
                    self.state = 'MENU'
                    self.intro_sound.stop()
                    self.back_sound.play()
                    return
                if self.text_ind >= len(story[self.story_ind]):
                    self.state = 'MENU'
                    self.intro_sound.stop()
                    self.back_sound.play()
                if isinstance(story[self.story_ind][self.text_ind], str):
                    text = story[self.story_ind][self.text_ind]
                    self.curr_text = self.story_font.render(text, 1, (10, 130, 111))
                    self.text_c = 0
                    self.text_ind += 1
                    # print(self.curr_text)
                    self.screen.blit(self.curr_text, (self.x_text, self.y_text))
                    self.y_text += 30
                else:
                    pict_name = story[self.story_ind][self.text_ind][0]
                    pict_x = story[self.story_ind][self.text_ind][1]
                    pict_y = story[self.story_ind][self.text_ind][2]
                    cur_pic = self.story_pics[pict_name]
                    # print(pict_x, pict_x)
                    self.screen.blit(cur_pic, (pict_x, pict_y))
                    self.y_text = 450

            if self.y_text > 420:
                self.screen.blit(self.clear_text, (self.x_text, 450))
            
            if self.clear_screen:
                # self.screen.fill((255, 255, 255))
                self.screen.blit(self.back, (0, 0))
                self.y_text = 10
                self.clear_screen = False
                self.story_ind += 1
                self.text_ind = 0

        elif self.state == 'MENU':
            self.screen.blit(self.back, (0, 0))
            self.screen.blit(self.menu_text_1, (90, 10))
            self.screen.blit(self.menu_text_2, (90, 60))
            self.screen.blit(self.menu_text_a_l, (100, 350))  # 100 350 575 350
            self.screen.blit(self.menu_text_a_r, (575, 350))  # отписали текста
            # отрисовка текущего персонажа (активного)
            self.on_screen_player.draw(self.screen)

        elif self.state == 'GAME':
            self.screen.blit(self.back, (0, 0))
            self.screen.blit(self.art_player_message, (10, 10))
            self.screen.blit(self.your_time_text, (30, 10))
            self.all_sprite_list.draw(self.screen)

        elif self.state == 'PAUSE':
            self.screen.blit(self.back, (0, 0))
            self.screen.blit(self.pause_text, (240, 10))

        elif self.state ==  'GAME OVER':
            self.screen.blit(self.back, (0, 0))
            self.all_sprite_list.draw(self.screen)
            self.screen.blit(self.go_text1, (200, 100))
            self.screen.blit(self.go_text2, (50, 200))
            self.screen.blit(self.time_text, (250, 200))
 

    def update_scene(self):
        if self.state == 'MENU':
            t = pygame.time.get_ticks() - self.start_t
            # self.players_vars.update(t//20)
            self.on_screen_player.update(t//20)

        elif self.state == 'GAME':
            self.art_player_message = self.score_font.render(str(self.active_one_player.art_count), 1, (0, 0, 0))
            self.time_killer_artifact()
            t = pygame.time.get_ticks()
            if t - self.last_art_create > self.artcd:
                self.last_art_create = t  # комментруем, получаем liketime
                self.artcd = random.randint(1000, 3000)
                self.create_artifacts()

            self.your_time_f_level -= 1
            self.your_time_text = self.score_font.render('Your time: ' + str(self.your_time_f_level//60), 1, (0, 0, 0))
            if self.your_time_f_level <= 60:  # последняя секунда
                self.state = 'MENU'
                self.active_one_player.kill()
                self.your_time_f_level = 60*10
                # print(self.active_one_player)
            self.all_sprite_list.update()
    

    def run(self):
        self.intro_sound.play()
        self.screen.blit(self.back, (0, 0))
        while True:
            self.text_c += 1
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                self.handle_scene(e)

            self.update_scene()
            self.draw_scene()
            pygame.display.update()
            self.clock.tick(FPS)



    
game = Game()
game.run()








