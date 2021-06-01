import pygame

WIDTH = 700
HEIGHT = 500

FPS = 60
LEVEL_SEC = 20
STORY_LINE_SEC = 1

KEYS = [0, pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]
DX = [0, 0, 0, -1, 1]
DY = [0, 1, -1, 0, 0]

STORYFILE = 'stories.txt'