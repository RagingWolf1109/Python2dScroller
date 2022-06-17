from subprocess import STARTF_USESHOWWINDOW
import pygame
import random

#Import my projectile module 
from projectile import Projectile

pygame.init()

#creating the screen
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Side Scroller')


def menu():
    image = pygame.image.load('assets\menu.png')
    image = pygame.transform.scale(image,(640,480))    
    while True:
        screen.blit(image,(0,0))
        pygame.draw.rect(screen,(255,255,255),(250,200,100,50)) #make this an image eventually (x,y,width,height)
        #press enter to start
        pygame.display.update()
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
              print('Quitting')
              pygame.display.quit()
              exit()
           if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game()

def game():
    image = pygame.image.load('assets\level1.png')
    image = pygame.transform.scale(image,(640,480))    
    bgx = 0

    player = pygame.image.load('assets\player.png')
    player = pygame.transform.rotozoom(player,0,0.2)
    player_y = 325

    gravity = 1
    jump = 0
    jumpcount = 0

    crate = pygame.image.load('assets\crate.png')
    crate = pygame.transform.rotozoom(crate,0,0.8)
    crate_x = 760
    crate_speed = 2

    #basic attacks
    basicAttack_group = pygame.sprite.Group()
    shoot = False

    while True:
        screen.blit(image,(bgx-640,0))
        screen.blit(image,(bgx,0))
        screen.blit(image,(bgx+640,0))
        
        bgx = bgx - 1
        if bgx <= -640:
            bgx = 0

        p_rect = screen.blit(player,(50,player_y))
        if player_y < 325:
            player_y = player_y + gravity
            #go back to the og tutorial and recheck this 
        if jump == 1:
            player_y = player_y - 4
            jumpcount += 1
            if jumpcount > 40:
                jump = 0
                jumpcount = 0    
        c_rect = screen.blit(crate,(crate_x,360))
        crate_x = crate_x - crate_speed
        if crate_x < -50:
            crate_x = random.randint(760,800)
            crate_speed = random.randint(2,4)

        if p_rect.colliderect(c_rect):
            print('Collision')
            return

        jumping = False

        basicAttack_group.update()
        basicAttack_group.draw(screen)

        pygame.display.update()
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
              print('Quitting')
              pygame.display.quit()
              exit()
           if event.type == pygame.KEYDOWN:
                #to fix jumping i will need to add a box and do a collision check
                if event.key == pygame.K_SPACE:
                     if jumping == False:
                        jumping = True
                        print('Jump')
                        jump = 1
                if event.key == pygame.K_q: #basic attack
                    shoot = True
                    if shoot == True:
                      bullet = Projectile(50,player_y,0)
                      basicAttack_group.add(bullet)
           if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    shoot = False
                if event.key == pygame.K_SPACE:
                    jumping = False       
def main():
    menu()

main()