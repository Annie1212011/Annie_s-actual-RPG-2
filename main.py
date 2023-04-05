import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def create_tilemap(self):
        for i, row in enumerate(TILEMAP):
            for j, col in enumerate(row):
                if col == 'B':
                    Block(self, j, i, BLUE)
                if col == 'G':
                    Block(self, j, i, GREEN)
                if col == 'P':
                    Player(self, j, i)
    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enamies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.create_tilemap()
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(Black)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
    def main(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass

game = Game()
game.intro_screen()
game.new()
while game.running:
    game.main()

    game.game_over()
pygame.quit()
sys.exit()