import sys, pygame, random
pygame.init()

size = width, height = 1024, 768
black = 0, 0, 0
clock = pygame.time.Clock

screen = pygame.display.set_mode(size)

numberOfBalls = 1
maxVal = 10
balls = []

pygame.font.init()

class Ball:

    ballTile = pygame.image.load("intro_ball.gif")
    speed = [0.5, 1]
    ballrect = ballTile.get_rect()

    def __init__(self, speed, scale):
        if speed is not None:
            self.speed = speed
        w, h = self.ballTile.get_size()
        self.ballTile = pygame.transform.scale(self.ballTile, (int(w * scale), int(h * scale)))
        self.ballrect = self.ballTile.get_rect()

    def update(self):
        self.ballrect = self.ballrect.move(self.speed)
        if self.ballrect.left < 0 or self.ballrect.right > width:
            self.speed[0] = -self.speed[0]
            return
        if self.ballrect.top < 0 or self.ballrect.bottom > height:
            self.speed[1] = -self.speed[1]
            return

        for ball in balls:
            collisionDetected = False
            if ball is not self and not collisionDetected :

                # top
                x = self.ballrect[0] + self.ballrect[2]/2
                y = self.ballrect[1]
                if self.isPointInsideRect(x, y, ball.ballrect):
                    self.speed[0] = -self.speed[0]
                    ball.speed[0] = -ball.speed[0]
                    return

                # right
                x = self.ballrect[0] + self.ballrect[2]
                y = self.ballrect[1] + self.ballrect[3]/2
                if self.isPointInsideRect(x, y, ball.ballrect):
                    self.speed[0] = -self.speed[0]
                    ball.speed[0] = -ball.speed[0]
                    return

                # left
                x = self.ballrect[0]
                y = self.ballrect[1] + self.ballrect[3] / 2
                if self.isPointInsideRect(x, y, ball.ballrect):
                    self.speed[1] = -self.speed[1]
                    ball.speed[1] = -ball.speed[1]
                    return

                #bottom
                x = self.ballrect[0] + self.ballrect[2] / 2
                y = self.ballrect[1] + self.ballrect[3]
                if self.isPointInsideRect(x, y, ball.ballrect):
                    self.speed[1] = -self.speed[1]
                    ball.speed[1] = -ball.speed[1]
                    return

        screen.blit(self.ballTile, self.ballrect)

    def isPointInsideRect(self, x, y, rect):
        if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
            return True
        else:
            return False

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',48)
    label = largeText.render(text, 1, (255,255,255))
    screen.blit(label, (100,100))
    # pygame.display.flip()


for _ in range(numberOfBalls):
    balls.append(Ball([random.randrange(1, maxVal, 1), random.randrange(1, maxVal, 1)], scale = random.uniform(0.5, 1.5)))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                balls.append(Ball([random.randrange(random.randrange(-1, 1, 1), maxVal, 1), random.randrange(1, maxVal, 1)],scale=random.uniform(0.5, 1.5)))
            # if event.key == pygame.K_DOWN:
            #     balls.pop(balls.__len__() - 1)

    # ball.update()
    screen.fill(black)

    for ball in balls:
        ball.update()

    message_display("Balls:" + str(balls.__len__()))

    pygame.display.update()

    # ball2.update()
    pygame.time.delay(5)

