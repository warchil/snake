import pygame
import random

pygame.init()

ZLUTA = (255, 255, 102)
CERNA = (0, 0, 0)
CERVENA = (213, 50, 80)
ZELENA = (0, 255, 0)
MODRA = (50, 153, 213)

sirkaObrazovky = 600
vyskaObrazovky = 400

herniObrazovka = pygame.display.set_mode((sirkaObrazovky, vyskaObrazovky))
pygame.display.set_caption('Snake game')

hodiny = pygame.time.Clock()

velikostBlokuHada = 10
rychlostHada = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def vykresliSkore(skore):
    noveSkore = score_font.render("Skore: " + str(skore), True, ZLUTA)
    herniObrazovka.blit(noveSkore, [0, 0])


def vykresliHada(velikostBlokuHada, snake_list):
    for x in snake_list:
        pygame.draw.rect(herniObrazovka, CERNA, [x[0], x[1], velikostBlokuHada, velikostBlokuHada])


def zobrazZpravu(msg, color):
    zprava = font_style.render(msg, True, color)
    herniObrazovka.blit(zprava, [sirkaObrazovky / 8, vyskaObrazovky / 3])


def gameLoop():
    hraSkoncila = False
    hadNarazil = False

    hlavaX = sirkaObrazovky / 2
    hlavaY = vyskaObrazovky / 2

    zmenaHlavaX = 0
    zmenaHlavaY = 0

    seznamHadichBloku = []
    delkaHada = 1

    # Vygenerování počátečníc náhodných souřadnic jídla
    jidloX = round(random.randrange(0, sirkaObrazovky - velikostBlokuHada) / 10.0) * 10.0
    jidloY = round(random.randrange(0, vyskaObrazovky - velikostBlokuHada) / 10.0) * 10.0

    while not hraSkoncila:

        while hadNarazil == True:
            herniObrazovka.fill(MODRA)
            zobrazZpravu("Hra skončila! [C] - nová hra / [Q] - ukončení.", CERVENA)
            vykresliSkore(delkaHada - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        hraSkoncila = True
                        hadNarazil = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hraSkoncila = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    zmenaHlavaX = -velikostBlokuHada
                    zmenaHlavaY = 0
                elif event.key == pygame.K_RIGHT:
                    zmenaHlavaX = velikostBlokuHada
                    zmenaHlavaY = 0
                elif event.key == pygame.K_UP:
                    zmenaHlavaY = -velikostBlokuHada
                    zmenaHlavaX = 0
                elif event.key == pygame.K_DOWN:
                    zmenaHlavaY = velikostBlokuHada
                    zmenaHlavaX = 0

        if hlavaX >= sirkaObrazovky or hlavaX < 0 or hlavaY >= vyskaObrazovky or hlavaY < 0:
            hadNarazil = True

        hlavaX += zmenaHlavaX
        hlavaY += zmenaHlavaY

        herniObrazovka.fill(MODRA)
        pygame.draw.rect(herniObrazovka, ZELENA, [jidloX, jidloY, velikostBlokuHada, velikostBlokuHada])

        hlavaHada = []
        hlavaHada.append(hlavaX)
        hlavaHada.append(hlavaY)

        seznamHadichBloku.append(hlavaHada)
        if len(seznamHadichBloku) > delkaHada:
            del seznamHadichBloku[0]

        for x in seznamHadichBloku[:-1]:
            if x == hlavaHada:
                hadNarazil = True

        vykresliHada(velikostBlokuHada, seznamHadichBloku)
        vykresliSkore(delkaHada - 1)

        pygame.display.update()

        if hlavaX == jidloX and hlavaY == jidloY:
            jidloX = round(random.randrange(0, sirkaObrazovky - velikostBlokuHada) / 10.0) * 10.0
            jidloY = round(random.randrange(0, vyskaObrazovky - velikostBlokuHada) / 10.0) * 10.0
            delkaHada += 1

        hodiny.tick(rychlostHada)

    pygame.quit()
    quit()


gameLoop()
