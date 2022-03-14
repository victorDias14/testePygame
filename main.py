import random

import pygame
from player import Player
from asteroid import Asteroid
from shoot import Shoot

# Start PyGame and create window
pygame.init()
screen = pygame.display.set_mode((840, 480))
pygame.display.set_caption('Asteroids')

# Groups
objectGroup = pygame.sprite.Group()
asteroidGroup = pygame.sprite.Group()
shootGroup = pygame.sprite.Group()

# Background
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load('graphics/2ndtry.png')
bg.image = pygame.transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()

player = Player(objectGroup)

# Music
#pygame.mixer.music.load('sounds/the_field_of_dreams.mp3')
#pygame.mixer.music.play(-1)

# Explosion
explosion = pygame.mixer.Sound('sounds/Misc Lasers/Fire 3.mp3')

gameLoop = True
gameOver = False
timer = 20
clock = pygame.time.Clock()
if __name__ == '__main__':
    while gameLoop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gameOver:
                    explosion.play()
                    newShoot = Shoot(objectGroup, shootGroup)
                    newShoot.rect.center = player.rect.center

        # Update logic
        if not gameOver:
            objectGroup.update()

            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    newAsteroid = Asteroid(objectGroup, asteroidGroup)

            collisions = pygame.sprite.spritecollide(player, asteroidGroup, False, pygame.sprite.collide_mask)

            if collisions:
                print('Game Over')
                gameOver = True

            hits = pygame.sprite.groupcollide(shootGroup, asteroidGroup, True, True, pygame.sprite.collide_mask)

        screen.fill([46, 46, 46])
        objectGroup.draw(screen)

        pygame.display.update()
