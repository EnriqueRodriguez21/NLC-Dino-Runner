import pygame

from dino_runner.utils.constants import HEART, LIST_LIVES
from pygame.sprite import Sprite


class Lives(Sprite):
    X_POS = 900
    Y_POS = 20

    def __init__(self):
        self.image = HEART
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.lives = LIST_LIVES

    def update(self, game):
        print(game.live)
        if game.live > 0:
            game.live -= 1
            self.take_live(game.live, game)
        else:
            pygame.time.delay(600)
            game.death_count += 1
            game.playing = False

    def draw(self, screen, game):
        for live in game.live_list:
            self.rect.x = live
            screen.blit(self.image, (self.rect.x, self.rect.y))

    def take_live(self, position, game):
        if len(game.live_list) != 0:
            game.live_list.pop(position)
