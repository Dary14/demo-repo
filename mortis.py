import pygame
from random import *

pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((500, 375))
pic = ['bg', 'logo', 'm1', 'm2', 'm3', 'm4', 'm5', 'pg1', 'pg2', 'pb1', 'pb2', 'ps1', 'ps2', 'rc', 'rcb', 'zg1', 'zg2',
       'zb1', 'zb2', 'princes']
Surf = {}
rm = {}
for i in pic:
    Surf[i] = pygame.image.load(i + '.png')

# Start menu
tg = 0
menu = True
font = pygame.font.Font(None, 24)
text1 = text2 = text3 = text4 = font.render("", True, [100, 150, 100])

while menu == True:
    clock.tick(60)
    tg += 1
    sc.blit(Surf['bg'], (0, 0))
    sc.blit(Surf['logo'], (2, 0))
    for i in range(5):
        sc.blit(Surf['m' + str(i + 1)], (180, 50 + 45 * i))
    if tg % 200 > 100:
        pl = Surf['ps2']
    else:
        pl = Surf['ps1']
    sc.blit(pl, (40, 190))
    for i in range(5):
        rm['rm' + str(i + 1)] = pygame.Rect(180, 50 + 45 * i, 292, 36)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if rm['rm1'].collidepoint(x, y):
                menu = False
            if rm['rm2'].collidepoint(x, y):
                text1 = font.render("You must collect 30 crystals while avoiding the enemy.", True, [220, 220, 120])
                text2 = font.render("The enemy can also collect crystals like you,", True, [220, 220, 120])
                text3 = font.render("which means you will lose one crystal.", True, [220, 220, 120])
                text4 = font.render("If the enemy catches you, all crystals will reset to zero.", True, [220, 220, 120])
            if rm['rm3'].collidepoint(x, y):
                text1 = font.render("The character is controlled using the keyboard keys.", True, [220, 220, 120])
                text2 = font.render("Use the left and right arrows to move.", True, [220, 220, 120])
                text3 = font.render("If you go off the game area,", True, [220, 220, 120])
                text4 = font.render("the character will appear from the opposite side.", True, [220, 220, 120])
            if rm['rm4'].collidepoint(x, y):
                text1 = font.render("This game was created for educational purposes,", True, [220, 220, 120])
                text2 = font.render("to demonstrate the capabilities of the PyGame library.", True, [220, 220, 120])
                text3 = font.render("Game designer/tester: Luchnikova Irina.", True, [220, 220, 120])
                text4 = font.render("Developer: Rizvanov Rustam.", True, [220, 220, 120])
            if rm['rm5'].collidepoint(x, y):
                pygame.quit()

    textpos1 = (120, 300)
    textpos2 = (135, 315)
    textpos3 = (150, 330)
    textpos4 = (165, 345)
    sc.blit(text1, textpos1)
    sc.blit(text2, textpos2)
    sc.blit(text3, textpos3)
    sc.blit(text4, textpos4)
    pygame.display.update()

# Main game logic
x_pl = 40
x_z = 400
tg = 0
spl = 0
sz = 0
score = 0
x_cr = randint(60, 300)
z = Surf['zg1']
font = pygame.font.Font(None, 60)
nap = False
game = True

while game == True:
    tg = tg + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Restricting the game area
    if x_pl < -30:
        x_pl = 500
    if x_pl > 500:
        x_pl = -30

    # Crystal flickering effect
    if tg % 20 > 10:
        cry = Surf['rc']
    else:
        cry = Surf['rcb']

    # Player movement
    if tg % 80 > 70:
        pl = Surf['ps2']
    else:
        pl = Surf['ps1']

    key_1 = pygame.key.get_pressed()
    key_2 = pygame.key.get_pressed()
    pygame.time.delay(50)

    if key_1 == key_2:
        if key_1[pygame.K_RIGHT]:
            x_pl += 10
            pl = Surf['pg' + str(spl % 2 + 1)]
            spl += 1
        elif key_1[pygame.K_LEFT]:
            x_pl -= 10
            pl = Surf['pb' + str(spl % 2 + 1)]
            spl += 1

    if abs(x_pl - x_cr) < 10:
        score += 1
        while abs(x_pl - x_cr) < 100:
            x_cr = randint(20, 480)

    # Enemy movement
    if x_pl > x_z:
        x_z += 8
        z = Surf['zb' + str(sz % 2 + 1)]
        sz += 1
    else:
        x_z -= 8
        z = Surf['zg' + str(sz % 2 + 1)]
        sz += 1

    if abs(x_z - x_cr) < 30:
        score -= 1
        while abs(x_z - x_cr) < 100:
            x_cr = randint(20, 480)

    if abs(x_z - x_pl) < 30:
        score = 0
        x_z = 400
        x_pl = 40

    # Display score
    text = font.render("Score: " + str(score), True, [100, 150, 0])

    if score == 30:
        game = False

    # Update game screen
    sc.blit(Surf['bg'], (0, 0))
    sc.blit(cry, (x_cr, 250))
    sc.blit(pl, (x_pl, 190))
    sc.blit(z, (x_z, 175))
    textpos = (10, 10)
    sc.blit(text, textpos)
    pygame.display.update()
    clock.tick(60)

# Victory scene
tg = 0
menu = True
font = pygame.font.Font(None, 80)

while menu == True:
    tg += 1
    sc.blit(Surf['bg'], (0, 0))
    sc.blit(Surf['logo'], (2, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if tg % 200 > 100:
        pl = Surf['ps2']
    else:
        pl = Surf['ps1']

    txt = font.render("You Won!!!", True, [255, 0, 0])
    txtpos = (100, 120)
    sc.blit(txt, txtpos)
    sc.blit(Surf['princes'], (300, 180))
    sc.blit(pl, (200, 190))
    pygame.display.update()
    clock.tick(60)
