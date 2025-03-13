import datetime as dt
import pygame as pg

from config import CLOCK_PATH, HAND_PATH, FPS, SIZE, BACKGROUND_COLOR, \
    WIDTH, HEIGHT


def blit_rotated_to_center(surface: pg.Surface, image: pg.image, angle) -> None:
    rotated = pg.transform.rotate(image, angle)
    new_rect = rotated.get_rect(center=hour_arrow_img.get_rect(center=(WIDTH//2, HEIGHT//2)).center)
    surface.blit(rotated, new_rect)


if __name__ == '__main__':
    pg.init()
    running = True

    clock = pg.time.Clock()
    screen = pg.display.set_mode(SIZE)
    clock_img = pg.transform.scale(pg.image.load(CLOCK_PATH), (WIDTH, HEIGHT))

    hour_arrow_img = pg.transform.scale(pg.image.load(HAND_PATH), (50, 200))
    minute_arrow_img = pg.transform.scale(pg.image.load(HAND_PATH), (30, 100))

    hour_angle = 180 - (dt.datetime.now().hour * 30)
    min_angle = 180 - (dt.datetime.now().minute * 6)
    ticks = dt.datetime.now().second

    while running:
        ticks += 1

        screen.fill(BACKGROUND_COLOR)
        screen.blit(clock_img, (0, 0))

        blit_rotated_to_center(screen, hour_arrow_img, hour_angle)
        blit_rotated_to_center(screen, minute_arrow_img, min_angle)

        hour_angle -= 30 if ticks == 3600 else 0
        min_angle -= 6 if ticks % 60 == 0 else 0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        clock.tick(FPS)
        pg.display.flip()

        ticks %= 3600
        print(ticks)

    pg.quit()
