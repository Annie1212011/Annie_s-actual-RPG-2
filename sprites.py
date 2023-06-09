import pygame
from config import *
import math
import random

class Block(pygame.sprite.Sprite):
    def __init__ (self, game, x, y, color, is_solid = True):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)


        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.is_solid = is_solid

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.vx = 0 
        self.vy = 0

        self.width = TILESIZE
        self.height = TILESIZE

        self.facing = 'down'

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(PURPLE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()

        self.rect.x += self.vx
        self.rect.y += self.vy

        self.vx = 0
        self.vy = 0

    def new(self):
        pass

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vx -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.vx += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.vy -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.vy += PLAYER_SPEED
            self.facing = 'down'