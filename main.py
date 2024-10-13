import sys
import pygame
from constants import *
from player import *
from circleshape import *
from asteroid  import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    global CURRENT_SCORE
    
    #Player
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    
    #Asteroid
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    #Shot
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for update in updatable:
            update.update(dt)
        for asteroid in asteroids:
            if player.detect_collisions(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.detect_collisions(asteroid):
                    asteroid.split()
                    shot.kill()
                    CURRENT_SCORE += SCORE_IMPLEMENT
        screen.fill((0,0,0))
        
        #Display score
        pygame.font.init()
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {CURRENT_SCORE}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        for draw in drawable:
            draw.draw(screen)  
        pygame.display.flip()
        dt = clock.tick(60) / 1000 
        

if __name__ == "__main__":
    main()