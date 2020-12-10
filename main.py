import pygame
import sys

WIDTH = 1200
HEIGHT = 800

game_over = False

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Player(object):
    def __init__(self):
        self.tankPos = [400, 300]
        self.tankSize = [50, 50]
        self.tankColor = [125, 221, 100]
        self.tankSpeed = 0.5
        self.tankVelocity = [0, 0]

    def move(self, event):
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
        screen.fill((255, 255, 255))
        if self.tankPos[0] + self.tankVelocity[0] > 0 and \
                self.tankPos[0] + self.tankSize[0] + self.tankVelocity[0] < WIDTH:
            self.tankPos[0] += self.tankVelocity[0]
        if self.tankPos[1] + self.tankVelocity[1] > 0 and \
                self.tankPos[1] + self.tankSize[1] + self.tankVelocity[1] < HEIGHT:
            self.tankPos[1] += self.tankVelocity[1]
        pygame.draw.rect(screen, self.tankColor, self.tankPos + self.tankSize)


def runGame():
    usr = Player()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                usr.move(event)

        usr.draw()
        pygame.display.update()


def main():
    runGame()


if __name__ == '__main__':
    main()
