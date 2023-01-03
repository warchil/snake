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

def vykresliHada(velikostBlokuHada, snake_list):
    for x in snake_list:
        pygame.draw.rect(herniObrazovka, CERNA, [x[0], x[1], velikostBlokuHada, velikostBlokuHada])

def hlavniHerniCyklus():
    hraSkoncila = False

    # Pocatecni souradnice hlavy hada (zaciname uprostred obrazovky)
    hlavaX = sirkaObrazovky / 2
    hlavaY = vyskaObrazovky / 2

    # Zmena souradnic hlavy hada
    zmenaHlavaX = 0
    zmenaHlavaY = 0

    # Nejdulezitejsi promenna :), ktera ma v sobe seznam (pole) bloku hada, ktere se vykresluji
    seznamHadichBloku = []
    delkaHada = 1

    # Vygenerování počátečníc náhodných souřadnic jídla
    jidloX = round(random.randrange(0, sirkaObrazovky - velikostBlokuHada) / 10.0) * 10.0
    jidloY = round(random.randrange(0, vyskaObrazovky - velikostBlokuHada) / 10.0) * 10.0

    while not hraSkoncila:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hraSkoncila = True
            # Zmena souradnic X a Y hlavy hada podle stisknute klavesy
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

        # Zkontroluj, jestli hlava hada nenarazila do okraju obrazovky
        if hlavaX >= sirkaObrazovky or hlavaX < 0 or hlavaY >= vyskaObrazovky or hlavaY < 0:
            hraSkoncila = True

        # Nastaveni novych souradnic hlavy hada
        hlavaX += zmenaHlavaX
        hlavaY += zmenaHlavaY

        # Vykresleni herniho pozadi (vyplneni cele obrazovky jednou barvou)
        herniObrazovka.fill(MODRA)

        # Vykresleni jidla
        pygame.draw.rect(herniObrazovka, ZELENA, [jidloX, jidloY, velikostBlokuHada, velikostBlokuHada])

        hlavaHada = []
        hlavaHada.append(hlavaX)
        hlavaHada.append(hlavaY)

        # Pridani novych souradnic hlavy na konec seznamu hadich bloku
        seznamHadichBloku.append(hlavaHada)

        # Odmazani posledniho bloku hada (jinak by zustavala hadi stopa)
        if len(seznamHadichBloku) > delkaHada:
            del seznamHadichBloku[0]

        # Kontrola jestli had nenarazil sam do sebe
        for blokHada in seznamHadichBloku[:-1]:
            if blokHada == hlavaHada:
                hraSkoncila = True

        vykresliHada(velikostBlokuHada, seznamHadichBloku)

        pygame.display.update()

        if hlavaX == jidloX and hlavaY == jidloY:
            jidloX = round(random.randrange(0, sirkaObrazovky - velikostBlokuHada) / 10.0) * 10.0
            jidloY = round(random.randrange(0, vyskaObrazovky - velikostBlokuHada) / 10.0) * 10.0
            delkaHada += 1

        hodiny.tick(rychlostHada)

    pygame.quit()
    quit()

hlavniHerniCyklus()
