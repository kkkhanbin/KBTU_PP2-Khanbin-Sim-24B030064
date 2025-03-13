import pygame as pg

from config import SIZE, BALL_PATH, BACKGROUND_COLOR


def main():
    pg.init()

    ball = pg.transform.scale(pg.image.load(BALL_PATH), (50, 50))
    x, y = SIZE[0] // 2 - ball.get_width() // 2, SIZE[1] // 2 - ball.get_height() // 2
    screen = pg.display.set_mode(SIZE)

    running = True
    speed = 10

    while running:
        screen.fill(BACKGROUND_COLOR)
        screen.blit(ball, (x, y))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if pg.key.get_pressed()[pg.K_a]:
                x -= speed if x - speed >= 0 else 0
            if pg.key.get_pressed()[pg.K_s]:
                y += speed if y + speed + ball.get_height() <= SIZE[1] else 0
            if pg.key.get_pressed()[pg.K_d]:
                x += speed if x + speed + ball.get_width() <= SIZE[0] else 0
            if pg.key.get_pressed()[pg.K_w]:
                y -= speed if y - speed >= 0 else 0
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
        
        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()
