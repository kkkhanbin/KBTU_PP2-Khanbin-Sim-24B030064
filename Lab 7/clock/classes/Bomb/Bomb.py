import pygame as pg

from constants.paths import BOMB_IMAGE_PATH, BOOM_IMAGE_PATH


class Bomb(pg.sprite.Sprite):
    def __init__(self, pos: tuple, *groups):
        super().__init__(*groups)

        self.image = pg.image.load(BOMB_IMAGE_PATH)
        self.image_boom = pg.image.load(BOOM_IMAGE_PATH)
        self.rect = self.image.get_rect()

        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, *args):
        if args and args[0].type == pg.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom