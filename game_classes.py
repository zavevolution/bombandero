import pygame


class Mob:
    def __init__(self) -> None:
        self.image = pygame.Surface((20,20)).convert_alpha()
        self.image.fill((255, 0, 0))
        self.rec = self.image.get_rect()

    def blitme(self, surface: pygame.Surface, x: int=0, y: int=0) -> None:
        self.rec.x = x
        self.rec.y = y
        surface.blit(self.image, self.rec)


class Aereo:
    def __init__(self) -> None:
        self.image = pygame.Surface((60, 20)).convert_alpha()
        self.image.fill((0, 0, 255))
        self.rec = self.image.get_rect()

    def blitme(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rec)

    def move(self, speed: int) -> None:
        self.rec.x += speed
        if self.rec.x > 1600:
            self.rec.x = -60
            self.rec.y += 20


class Bomb:
    def __init__(self, x: int, y: int) -> None:
        self.image = pygame.Surface((5, 10)).convert_alpha()
        self.image.fill((0, 0, 0))
        self.rec = self.image.get_rect()
        self.rec.x = x
        self.rec.y = y

    def blitme(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rec)

    def move(self, speed: int) -> None:
        self.rec.y += speed