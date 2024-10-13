import pygame
from  circleshape import CircleShape
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white",self.triangle(),2)

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self):
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        Shot(self.position.x, self.position.y, shot_velocity)
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
    
    def update(self, dt):
        if self.shot_timer > 0:
            self.shot_timer -= dt
        keys = pygame.key.get_pressed()
        #Move up
        if keys[pygame.K_w]:
            self.move(dt)
        #Move down
        if keys[pygame.K_s]:
            self.move(-dt)
        #Rotate left
        if keys[pygame.K_a]:
            self.rotate(-dt)
        #Rotate right
        if keys[pygame.K_d]:
            self.rotate(dt)
        #Shoot
        if keys[pygame.K_SPACE]:
            if self.shot_timer <= 0:
                self.shoot()