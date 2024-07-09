import pygame
from pygame.math import Vector2
from pygame.draw import rect

class GameState():

    def __init__(self):
        self.worldSize = Vector2(5,5)
        self.tankPos = Vector2(2,2)

    def update(self,moveTankCommand):
        self.tankPos += moveTankCommand
    
class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tank_pyGame")
        pygame.display.set_icon(pygame.image.load("dice.png"))
        self.gamestate = GameState()
        self.unitTexture = pygame.image.load("Asset.png")
        self.cellSize = Vector2(64,64)
        self.windowSize = self.cellSize * self.gamestate.worldSize.elementwise()
        self.window = pygame.display.set_mode((int(self.windowSize.x), int(self.windowSize.y)))
        self.moveTankCommand = Vector2(0,0)

        self.running = True
        self.clock = pygame.time.Clock()

    def input_process(self):
        self.moveTankCommand = Vector2(0,0)

        eventlist = pygame.event.get()
        for event in eventlist:
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_a:
                    self.moveTankCommand.x = -1
                elif event.key == pygame.K_d:
                    self.moveTankCommand.x = 1
                elif event.key == pygame.K_s:
                    self.moveTankCommand.y = 1
                elif event.key == pygame.K_w:
                    self.moveTankCommand.y = -1

    def update(self):
        self.gamestate.update(self.moveTankCommand)

    def render(self):
        self.window.fill((0,0,0))

        spritePoint = self.gamestate.tankPos.elementwise()*self.cellSize

        #Texture
        texturePoint = Vector2(0,1).elementwise()*self.cellSize  
        textureRect = pygame.Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x),int(self.cellSize.y))
        self.window.blit(self.unitTexture,spritePoint,textureRect)

        pygame.display.update()  

    def runGame(self):
        while self.running: 
            self.input_process()
            self.update()
            self.render()

            self.clock.tick(60)

game = Game()
game.runGame()
pygame.quit()

