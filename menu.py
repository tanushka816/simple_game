import pygame


class Button():
    def __init__(            
            self, x, y, w, h, name,
            font_color=(0, 0, 0),
            normal_color=BLUE,
            highlight_color = GREEN,
            active_color=BLACK,
            size=24,
            font='Arial',
            padding=5
    ):
        # Текущее состояние кнопки. Все состояния: normal'   'highlight'  'active'
        self.state = 'normal'
        # Задаем цвета кнопки в нормальном, веделенном и активном состоянии:
        self.normal_color = normal_color
        self.highlight_color = highlight_color
        self.active_color = active_color
        # Задаем название  - текст на кнопке
        self.name = name
        self.font = pygame.font.SysFont(font, size, True)
        # Создаем надпись на кнопке
        self.text = self.font.render(name, True, font_color)
        # Задаем размеры прямоугольника
        self.image = pygame.Surface([w,h])
        self.image.fill(normal_color)
        # Задаем положение верхней панели на экране
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Задаем поля - отступы от границы кнопки для текста
        self.padding = padding

    # Рисуем прямоугольник кнопки и надпись на ней
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, (self.rect.x + self.padding, self.rect.y + self.padding))


    # В методе update меняем цвет кнокпи в зависимости от состояния
    def update(self):
        if self.state == 'normal':
            self.image.fill(self.normal_color)
        elif self.state == 'highlight':
            self.image.fill(self.highlight_color)
        elif self.state == 'active':
            self.image.fill(self.active_color)


    # Обработка событий кнопки:  меняем состояние в зависимости от события
    def handle_mouse_action(self, event=None):
        # Получаем текущее положение курсора
        pos_x, pos_y = pygame.mouse.get_pos()
        # Проверяем, находится курсор над кнопкой или нет:
        check_pos = self.rect.left <= pos_x <= self.rect.right and self.rect.top <= pos_y <= self.rect.bottom
        # Курсор движется над кнопкой:
        if event == pygame.MOUSEMOTION:
            if check_pos:  self.state = 'highlight'
            else: self.state = 'normal'
        # На кнопку кликнули:
        elif event == pygame.MOUSEBUTTONDOWN:
            if check_pos: self.state = 'active'
            else: self.state = 'normal'
        # На кнопку кликнули и отпустили:
        elif event == pygame.MOUSEBUTTONUP:
            if check_pos:  self.state = 'highlight'
            else: self.state = 'normal'



class MainMenu():

    def __init__(self):
        pass

