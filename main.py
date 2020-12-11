import pygame
import sys

WIDTH = 1200
HEIGHT = 800

game_over = False

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Bullet(object):

    def __init__(self, initLocation, initVelocity):
        """Class Constructor, initializes following parameters
        @param (list) initLocation: initial location of bullet
        @param (list) initVelocity: initial velocity of bullet

        bulletLoc: Location of bullet, measured in in pixels from top-left corner
        bulletVelocity: Measures speed of bullet in x,y directions
        bulletRadius: Radius of physical bullet
        bulletColor: Color of bullet, using RGB scale
        lifeSpan: Duration of bullet, measured in frames
        """
        self.bulletLoc = initLocation
        self.bulletVelocity = initVelocity
        self.bulletRadius = 10
        self.bulletColor = [0, 0, 0]
        self.lifeSpan = 10000

    def draw(self):
        """Updates the bullet location on screen. Checks to keep tank within screen boundaries."""
        # todo: implement reflection off of wall

        if self.bulletLoc[0] + self.bulletVelocity[0] > 0 and \
                self.bulletLoc[0] + self.bulletRadius + self.bulletVelocity[0] < WIDTH:
            self.bulletLoc[0] += self.bulletVelocity[0]
        if self.bulletLoc[1] + self.bulletVelocity[1] > 0 and \
                self.bulletLoc[1] + self.bulletRadius + self.bulletVelocity[1] < HEIGHT:
            self.bulletLoc[1] += self.bulletVelocity[1]
        pygame.draw.circle(screen, self.bulletColor, self.bulletLoc, self.bulletRadius)
        self.lifeSpan -= 1

class Player(object):
    """Player Class that represents the user tank."""
    def __init__(self):
        """Class Constructor, initializes following parameters
        tankLoc: Location of tank, measured in pixels from top-left corner
        tankSize: Size of tank body, measured in pixes
        tankColor: Color of tank body, using RGB scale
        tankSpeed: Moving speed of tank
        tankVelocity: Measures speed of tank in x,y directions
        bullets: List of all current bullets fired
        maxBullets: Maximum number of bullets that can be fired concurrently
        """
        self.tankLoc = [400, 300]
        self.tankSize = [50, 50]
        self.tankColor = [125, 221, 100]
        self.tankSpeed = 1
        self.tankVelocity = [0, 0]
        self.bullets = []
        self.maxBullets = 10

    def move(self, event):
        """Moves the tank in the desired position

        @param event (event): detected event (KEYUP or KEYDOWN)
        """
        if event.type == pygame.KEYDOWN:
            if event.key == ord('d'):
                self.tankVelocity[0] += self.tankSpeed
            if event.key == ord('a'):
                self.tankVelocity[0] += -self.tankSpeed
            if event.key == ord('w'):
                self.tankVelocity[1] += -self.tankSpeed
            if event.key == ord('s'):
                self.tankVelocity[1] += self.tankSpeed

        if event.type == pygame.KEYUP:
            if event.key == ord('d'):
                self.tankVelocity[0] += -self.tankSpeed
            if event.key == ord('a'):
                self.tankVelocity[0] += self.tankSpeed
            if event.key == ord('w'):
                self.tankVelocity[1] += self.tankSpeed
            if event.key == ord('s'):
                self.tankVelocity[1] += -self.tankSpeed

    def draw(self):
        """Updates tank location on screen. Checks to keep tank within screen boundaries."""
        screen.fill((255, 255, 255))

        if self.tankLoc[0] + self.tankVelocity[0] > 0 and \
                self.tankLoc[0] + self.tankSize[0] + self.tankVelocity[0] < WIDTH:
            self.tankLoc[0] += self.tankVelocity[0]
        if self.tankLoc[1] + self.tankVelocity[1] > 0 and \
                self.tankLoc[1] + self.tankSize[1] + self.tankVelocity[1] < HEIGHT:
            self.tankLoc[1] += self.tankVelocity[1]
        pygame.draw.rect(screen, self.tankColor, self.tankLoc + self.tankSize)

        for bullet in self.bullets:
            bullet.draw()
            if bullet.lifeSpan == 0:
                self.bullets.remove(bullet)

    def firebullet(self, event):
        """Fires a bullet in the direction of where the mouse is"""
        if len(self.bullets) < self.maxBullets:
            bulletXDir = event.pos[0] - self.tankLoc[0]
            bulletYDir = event.pos[1] - self.tankLoc[1]
            bulletSpeed = 2 * (bulletXDir**2 + bulletYDir**2)**0.5
            bulletVelocity = [bulletXDir/bulletSpeed, bulletYDir/bulletSpeed]
            bulletLoc = self.tankLoc[:]
            bulletLoc[0] += self.tankSize[0]/2
            bulletLoc[1] += self.tankSize[1]/2
            newBullet = Bullet(bulletLoc, bulletVelocity)
            self.bullets.append(newBullet)


def runGame():
    usr = Player()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                usr.move(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                usr.firebullet(event)

        usr.draw()
        pygame.display.update()


def main():
    runGame()


if __name__ == '__main__':
    main()
