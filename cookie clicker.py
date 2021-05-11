from pynput import keyboard
import pygame
import random
pygame.init()
running = True
Width = 1200
Height = 600
Border = 20
pygame.display.set_caption('Cookie Clicker') 

class cookie:
    radius = 100
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self, color):
        global screen
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)
    def update(self, Color):
        self.x = self.x
        self.y = self.y
        self.show(Color)

screen = pygame.display.set_mode((Width,Height))
cookie = cookie(250, 250)
cookie.show(pygame.Color('yellow'))

while running:
    cookie.update(pygame.Color("yellow"))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False