import pygame as pg
import os

from config import SONGS_PATH, PLAYER_PATH, SIZE

pg.init()
pg.mixer.init()

cur_track = 0
playing = False


def main():
    songs = os.listdir(SONGS_PATH)
    cur_track = 0
    running = True

    pg.mixer.music.load(os.path.join(SONGS_PATH, os.listdir(SONGS_PATH)[0]))
    pg.mixer.music.play()
    print("Music Player: Space=Play/Pause, S=Stop, Right Arrow=Next, Left Arrow=Previous, Escape=Exit")

    image = pg.transform.scale(pg.image.load(PLAYER_PATH), SIZE)
    screen = pg.display.set_mode(SIZE)

    while running:
        screen.blit(image, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if pg.mixer.music.get_busy():
                        pg.mixer.music.pause()
                    else:
                        pg.mixer.music.unpause()
                elif event.key == pg.K_s:
                    pg.mixer.music.stop()
                elif event.key == pg.K_RIGHT:
                    cur_track = (cur_track + 1) % len(songs)
                    pg.mixer.music.load(os.path.join(SONGS_PATH, os.listdir(SONGS_PATH)[cur_track]))
                    pg.mixer.music.play()
                elif event.key == pg.K_LEFT:
                    cur_track = (cur_track - 1) % len(songs)
                    pg.mixer.music.load(os.path.join(SONGS_PATH, os.listdir(SONGS_PATH)[cur_track]))
                    pg.mixer.music.play()
                elif event.key == pg.K_ESCAPE:
                    running = False
        
        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()
