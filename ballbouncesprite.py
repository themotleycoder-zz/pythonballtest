from pygame.locals import *
import pygame
import sys
import time
import random
import math

size = width, height = 1024, 768
black = 0, 0, 0
clock = pygame.time.Clock

screen = pygame.display.set_mode(size)
FPS = 120

numberOfBalls = 1
maxVal = 10
balls = []

pygame.font.init()

class Ball(pygame.sprite.Sprite):

    speed = [0.5, 1]

    def __init__(self, speed, scale):
        pygame.sprite.Sprite.__init__(self)
        # self.orig_image = pygame.image.load("intro_ball.gif").convert_alpha()

        self.original_image = pygame.image.load("intro_ball.gif").convert_alpha()
        w, h = self.original_image.get_size()
        self.image = pygame.transform.scale(self.original_image, (int(w * scale), int(h * scale)))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.radius = self.rect.right / 2
        self.center = (self.rect.right / 2, self.rect.bottom / 2)
        self.mass = (math.pi * (self.radius*self.radius))/2

    def move(self):

        if self.rect.right > width or self.rect.x < 0:
            self.speed[0] = -self.speed[0]

        if self.rect.bottom > height or self.rect.y < 0:
            self.speed[1] = -self.speed[1]

        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        self.center = (self.rect.x + self.radius, self.rect.y + self.radius)

    def collide(self, ball):
        if self is not ball:

            diffx = self.center[0] - ball.center[0]
            diffy = self.center[1] - ball.center[1]

            #distance between ball centers
            distance = math.sqrt((diffx*diffx) + (diffy*diffy))

            #is it less than/equal to the length of the combined radius?
            if distance <= (self.radius+ball.radius):
                collisionPointX = ((self.center[0] * ball.radius) + (ball.center[0] * self.radius)) / (self.radius + ball.radius)
                collisionPointY = ((self.center[1] * ball.radius) + (ball.center[1] * self.radius)) / (self.radius + ball.radius)

                newVelX1 = (self.speed[0] * (self.mass - ball.mass) + (2 * ball.mass * ball.speed[0])) / (self.mass + ball.mass)
                newVelY1 = (self.speed[1] * (self.mass - ball.mass) + (2 * ball.mass * ball.speed[1])) / (self.mass + ball.mass)
                newVelX2 = (ball.speed[0] * (ball.mass - self.mass) + (2 * self.mass * self.speed[0])) / (self.mass + ball.mass)
                newVelY2 = (ball.speed[1] * (ball.mass - self.mass) + (2 * self.mass * self.speed[1])) / (self.mass + ball.mass)

                self.speed = [newVelX1, newVelY1]
                ball.speed = [newVelX2, newVelY2]

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',48)
    label = largeText.render(text, 1, (255,255,255))
    screen.blit(label, (100,100))
    # pygame.display.flip()

pygame.init()

balls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

for _ in range(numberOfBalls):
    ball = Ball([random.randrange(1, maxVal, 1), random.randrange(1, maxVal, 1)], scale = random.uniform(0.5, 1.5))
    balls.add(ball)

while True:

    clock().tick(FPS)

    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                balls.add(Ball([random.randrange(random.randrange(-1, 1, 1), maxVal, 1), random.randrange(1, maxVal, 1)],scale=random.uniform(0.1, 1.0)))
            # if event.key == pygame.K_DOWN:
            #     balls.pop(balls.__len__() - 1)

    # ball.update()
    screen.fill(black)

    for ball in balls:
        for ball2 in balls:
            ball.collide(ball2)
        ball.move()

    balls.draw(screen)

    message_display("Balls:" + str(balls.__len__()))

    pygame.display.update()

    # screen.blit(background, (0, 0))


