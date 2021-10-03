import pygame

from game_functions import drow_window, is_destroed, update_game, check_event, init_game, is_destroed
       

pygame.init()
window = pygame.display.set_mode((1600, 800))
pygame.display.set_caption('Geometry')
clock = pygame.time.Clock()
FPS = 30
background = pygame.image.load('869.jpg').convert()
font = pygame.font.SysFont(None, 32)


game_level = 1
build_level_start = 5
build_level_end = 10

building, player, bombs = init_game(build_level_start, build_level_end)

while True:
    check_event(player, bombs)

    clock.tick(FPS)

    if is_destroed(building):
        game_level += 1
        build_level_start += 5
        build_level_end += 5
        building, player, bombs = init_game(build_level_start, build_level_end)
    
    update_game(player, building, bombs)

    drow_window(window, background, player, building, bombs)
    text_level = font.render(f'Level: {game_level}', True, (0, 155, 80, 0)).convert_alpha()
    window.blit(text_level, (20, 10))
    pygame.display.update()
