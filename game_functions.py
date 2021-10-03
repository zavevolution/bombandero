import pygame
import random
import sys

from game_classes import Bomb, Mob, Aereo


def init_game(start, end) -> tuple:
    building = [[Mob() for m in range(random.randint(start, end))] for k in range(1600 // 20)]
    player = Aereo()
    bombs = []

    return (building, player, bombs,)


def check_event(player, bombs) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not bombs:
                    b = Bomb(player.rec.centerx, player.rec.bottom)
                    bombs.append(b)


def drow_window(window, background, player, building, bombs) -> None:
    window.blit(background, (0, 0))
    player.blitme(window)

    for index, bild in enumerate(building):
        for ind, mob in enumerate(bild):
            mob.blitme(window, index * 20, 800 - ind * 20)

    for b in bombs:
        b.blitme(window)


def update_game(player, building, bombs) -> None:
    player.move(5)
    for b in bombs:  
        b.move(9)
        for i, l in enumerate(building):
            index = b.rec.collidelist([x.rec for x in l])   
            if index != -1 or b in bombs and b.rec.y > 800:
                building[i] = []
                bombs.remove(b)


def is_destroed(building) -> bool:
    check = []
    for l in building:    
        if l:
            check.append(True)
        else:
            check.append(False)
    return not True in check
