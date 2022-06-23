import pygame

class Game():
    def _init_(self):
        pygame.init()
        self.running,self.playing, = True , False
        self.UP_KEY,