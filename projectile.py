import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self,x,y,direction): 
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = pygame.image.load('assets/basicAttack.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
    def update(self):
        if self.direction == 'right':
            self.rect.x += (self.direction * self.speed)
        if not pygame.display.get_surface().get_rect().contains(self.rect):
            self.kill()

    #def update(self,events,dt):
        
        




