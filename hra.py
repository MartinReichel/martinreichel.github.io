import pygame
import time
import random

# Inicializace knihovny Pygame
pygame.init()

# Nastavení rozměrů okna
sirka = 800
vyska = 600

# Barvy
cerna = (0, 0, 0)
bila = (255, 255, 255)
cervena = (255, 0, 0)
zelena = (0, 255, 0)

# Velikost jednotlivých částí hada a jeho rychlost
velikost_bunky = 20
rychlost_hada = 15

# Font pro zobrazení textu
font = pygame.font.SysFont(None, 30)

# Funkce pro vykreslení hada
def vykreslit_hada(velikost_bunky, had):
    for x in had:
        pygame.draw.rect(okno, zelena, [x[0], x[1], velikost_bunky, velikost_bunky])

# Funkce pro hlavní smyčku hry
def hra():
    konec_hry = False
    game_over = False

    # Pozice hada
    x = sirka / 2
    y = vyska / 2

    # Změna pozice hada
    dx = 0
    dy = 0

    had = []
    delka_hada = 1

    # Náhodné umístění jídla
    jidlo_x = round(random.randrange(0, sirka - velikost_bunky) / 20.0) * 20.0
    jidlo_y = round(random.randrange(0, vyska - velikost_bunky) / 20.0) * 20.0

    while not konec_hry:
        while game_over == True:
            okno.fill(bila)
            text = font.render("Pro hraní znovu stiskněte R, nebo Q pro ukončení.", True, cerna)
            text_rect = text.get_rect(center=(sirka / 2, vyska / 2))
            okno.blit(text, text_rect)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        konec_hry = True
                        game_over = False
                    if event.key == pygame.K_r:
                        hra()

        # Zachycení událostí
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                konec_hry = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -velikost_bunky
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = velikost_bunky
                    dy = 0
                elif event.key == pygame.K_UP:
                    dx = 0
                    dy = -velikost_bunky
                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = velikost_bunky

        # Nastavení hracího pole
        if x >= sirka or x < 0 or y >= vyska or y < 0:
            game_over = True

        # Pohyb hada
        x += dx
        y += dy

        # Vykreslení okna
        okno.fill(bila)
        pygame.draw.rect(okno, cervena, [jidlo_x, jidlo_y, velikost_bunky, velikost_bunky])

        had_hlava = []
        had_hlava.append(x)
        had_hlava.append(y)
        had.append(had_hlava)
        if len(had) > delka_hada:
            del had[0]

        for cast in had[:-1]:
            if cast == had_hlava:
                game_over = True

        vykreslit_hada(velikost_bunky, had)
        pygame.display.update()

        # Podmínka pro sežrání jídla
        if x == jidlo_x and y == jidlo_y:
            jidlo_x = round(random.randrange(0, sirka - velikost_bunky) / 20.0) * 20.0
            jidlo_y = round(random.randrange(0, vyska - velikost_bunky) / 20.0) * 20.0
            delka_hada += 1

        # Rychlost hada
        cas
