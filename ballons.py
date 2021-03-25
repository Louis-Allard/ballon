import pygame
import time
from random import *

blue =  (1,126,207)
white = (255,255,255)
orange = (246,99,0)

pygame.init()

width = 1450
height = 700
ballon_w = 122
ballon_h = 291
nuages_w = 480
nuages_h = 250

surface = pygame.display.set_mode((width,height))
pygame.display.set_caption("Fly Away")
img = pygame.image.load("./sprites/perso.png")
img_nuages01 = pygame.image.load("./sprites/oiseaux.png")
img_nuages02 = pygame.image.load("./sprites/oiseaux2.png")

def score(compte):
    police = pygame.font.Font('BradBunR.ttf', 16)
    texte = police.render("Score: " + str(compte), True, white)
    surface.blit(texte, [10,0])

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
    texteSurface = Police.render(texte, True, orange)
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
        clock.tick(0)
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
    score_actuel = 0

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
        score(score_actuel)

        nuage_x -= nuages_vitesse

        if img_y > height - 40 or img_y < -10:
            gameOver()

        if 3 <= score_actuel > 5:
            nuages_vitesse = 7
            espace = ballon_h*2.8
        if score_actuel >5:
            nuages_vitesse = 8
            espace = ballon_h*2.7        

        if img_x + ballon_w > nuage_x + 20:
            if img_y < nuage_y + nuages_h - 20:
                if img_x - ballon_w < nuage_x + nuages_w - 20:
                    gameOver()
        if img_x + ballon_w > nuage_x + 20:
            if img_y + ballon_h > nuage_y + nuages_h + espace + 20:
                if img_x - ballon_w < nuage_x + nuages_w - 20:
                    gameOver()

        if nuage_x < (-1 * nuages_w):
            nuage_x = width
            nuage_y = randint(-300,20)

        if nuage_x < (img_x - nuages_w) < nuage_x + nuages_vitesse:
            score_actuel += 1

        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
quit()