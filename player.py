import pygame
import math
from constants import *

class Player():
    def __init__(self):
        self.rect = pygame.Rect(100, 100, BLOCK_SIZE, BLOCK_SIZE)
        self.angle = 0
        self.img = pygame.image.load('arrow.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (BLOCK_SIZE, BLOCK_SIZE))
        self.correction_angle = 0
        self.bullets = []
        self.can_shoot = True
        self.shoot_frame = 0
        self.shoot_delay = 60
        self.ammo = 20


    def update(self):
        self.rotate()
        self.shoot()
        if pygame.time.get_ticks() > self.shoot_frame + self.shoot_delay :
            self.can_shoot = True

        for bullet in self.bullets:
            bullet.update()
            if bullet.can_delete:
                self.bullets.remove(bullet)

    def shoot(self):
        if self.can_shoot and self.ammo > 0:
            if pygame.mouse.get_pressed()[0]:
                self.bullets.append(Bullet(self.rect.x, self.rect.y, self.angle))
                self.can_shoot = False
                self.shoot_frame = pygame.time.get_ticks()
                self.ammo -= 1

    def rotate(self):
        mx, my = pygame.mouse.get_pos()
        dx, dy = mx - self.rect.centerx, my - self.rect.centery
        self.angle = math.degrees(math.atan2(-dy, dx)) - self.correction_angle
        self.rot_img = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.rot_img.get_rect(center = self.rect.center)


    def draw(self, surface):
        surface.blit(self.rot_img, (self.rect.x, self.rect.y))
        for bullet in self.bullets:
            bullet.draw(surface)
        #


class Bullet():
    def __init__(self, x, y, angle):
        print(angle)
        self.rect = pygame.Rect(100, 100, BLOCK_SIZE // 4, BLOCK_SIZE // 4)
        self.angle = angle
        self.img = pygame.image.load('arrow.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (BLOCK_SIZE // 4, BLOCK_SIZE // 4))
        self.correction_angle = 0
        self.speed = 5
        self.can_delete = False

    def update(self):

        self.rect.x = self.rect.x + (self.speed * math.cos(self.angle * math.pi / 180))
        self.rect.y = self.rect.y + (self.speed * math.cos(self.angle * math.pi / 180))
        # self.rect.x += self.speed
        if self.rect.x > 600:
            self.can_delete = True



    def draw(self, surface):
        surface.blit(self.img, (self.rect.x, self.rect.y))
