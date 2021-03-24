import pygame
import time
from random import *

blue =  (1,126,207)
white = (255,255,255)

pygame.init()

width = 800
height = 500
ballon_w = 50
ballon_h = 50
nuages_w = 200
nuages_h = 95

surface = pygame.display.set_mode((width,height))
pygame.display.set_caption("Ballons")
img = pygame.image.load("./sprites/ballons.png")
img_nuages01 = pygame.image.load("./sprites/nuages.png")
img_nuages02 = pygame.image.load("./sprites/nuages2.png")

def nuages(nuage_x,nuage_y,espace):
    surface.blit(img_nuages01, (nuage_x, nuage_y))
    surface.blit(img_nuages02, (nuage_x, nuage_y + nuages_h + espace))



def rejoueOuQuit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP,pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP:
            continue
        return event.key
    return None    

def creaTexteObj(texte, Police):
    texteSurface = Police.render(texte, True, white)
    return texteSurface, texteSurface.get_rect()

def message(texte):
    GOtext= pygame.font.Font('BradBunR.ttf', 150)
    petitText = pygame.font.Font('BradBunR.ttf', 20)

    GOtextSurf, GOtextRect = creaTexteObj(texte,GOtext)
    GOtextRect.center = width/2, ((height/2)-50)
    surface.blit(GOtextSurf, GOtextRect)
    
    petitTextSurf, petitTextRect = creaTexteObj("Appuyer sur une touche pour continuer", petitText)
    petitTextRect.center = width/2, ((height/2)+50)
    surface.blit(petitTextSurf, petitTextRect)

    pygame.display.update()
    time.sleep(2)
    while rejoueOuQuit() == None:
        clock.tick()
    main()    

def gameOver():
    message("Boom!")

def ballon(img_x,img_y,image):
    surface.blit(image,(img_x,img_y))

def main():
    img_x = 150
    img_y = 200
    move_y = 0
    game_over = False
    clock = pygame.time.Clock()
    nuage_x = width
    nuage_y = randint(-300,20)
    espace = ballon_h * 2
    nuages_vitesse = 6

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_y = -5
            if event.type == pygame.KEYUP:
                move_y = 5
        img_y += move_y

        surface.fill(blue)
        ballon(img_x,img_y,img)
        nuages(nuage_x,nuage_y,espace)
        nuage_x -= nuages_vitesse

        if img_y > height - 40 or img_y < -10:
            gameOver()

        if img_x + ballon_w > nuage_x:
            if img_y < nuage_y + nuages_h:
                if img_x - ballon_w < nuage_x + nuages_w:
                    gameOver()
        if img_x + ballon_w > nuage_x:
            if img_y + ballon_h > nuage_y + nuages_h + espace:
                if img_x - ballon_w < nuage_x + nuages_w:
                    gameOver()

        if nuage_x < (-1 * nuages_w):
            nuage_x = width
            nuage_y = randint(-300,20)
        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
quit()