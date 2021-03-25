import pygame
import time
from random import *

blue =  (20.6,42.4,67.5)
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
    police = pygame.font.Font('BradBunR.ttf', 20)
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
    petitText = pygame.font.Font('BradBunR.ttf', 50)

    GOtextSurf, GOtextRect = creaTexteObj(texte,GOtext)
    GOtextRect.center = width/2, ((height/2)-50)
    surface.blit(GOtextSurf, GOtextRect)

    petitTextSurf, petitTextRect = creaTexteObj("Appuyez sur une touche pour continuer", petitText)
    petitTextRect.center = width/2, ((height/2)+50)
    surface.blit(petitTextSurf, petitTextRect)

    pygame.display.update()
    time.sleep(2)
    while rejoueOuQuit() == None:
        clock.tick()
    main()    

def gameOver():
    message("Boom !!!")

def ballon(perso_posx,perso_posy,image):
    surface.blit(image,(perso_posx,perso_posy))

def main():
    perso_posx = 150
    perso_posy = 200
    perso_movey = 0
    game_over = False
    clock = pygame.time.Clock()
    nuage_x = width
    nuage_y = randint(-291,20)
    espace = ballon_h * 1.5
    nuages_vitesse = 7
    score_actuel = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    perso_movey = -5
            if event.type == pygame.KEYUP:
                perso_movey = 5
        perso_posy += perso_movey

        surface.fill(blue)
        ballon(perso_posx,perso_posy,img)
        nuages(nuage_x,nuage_y,espace)
        score(score_actuel)

        nuage_x -= nuages_vitesse

        if perso_posy > height - 40 or perso_posy < -10:
            gameOver()

        if 2 <= score_actuel > 4:
            nuages_vitesse = 9
            espace = ballon_h*1.4
        if 5 <= score_actuel > 7:
            nuages_vitesse = 10
            espace = ballon_h*1.3     
        if 8 <= score_actuel > 9:
            nuages_vitesse = 11
            espace = ballon_h*1.2 
        if 10 <= score_actuel > 12:
            nuages_vitesse = 12
            espace = ballon_h*1.1 
        if score_actuel > 12:
            nuages_vitesse = 15
            espace = ballon_h*1.1             

        if perso_posx + ballon_w > nuage_x + 50:
            if perso_posy < nuage_y + nuages_h - 50:
                if perso_posx - ballon_w < nuage_x + nuages_w - 50:
                    gameOver()
        if perso_posx + ballon_w > nuage_x + 50:
            if perso_posy + ballon_h > nuage_y + nuages_h + espace + 50:
                if perso_posx - ballon_w < nuage_x + nuages_w - 50:
                    gameOver()

        if nuage_x < (-1 * nuages_w):
            nuage_x = width
            nuage_y = randint(-291,20)

        if nuage_x < (perso_posx - nuages_w) < nuage_x + nuages_vitesse:
            score_actuel += 1

        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
quit()