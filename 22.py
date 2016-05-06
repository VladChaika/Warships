import pygame
import random

from pygame.locals import *
from sys import exit

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (200, 200, 200)
GREEN = (0, 255, 0)
# Set the height and width of the screen
# -----------------------------------
stroki = 10
stolbiki = 20
shirina_uacheiki = 20
visota_uacheiki = 20
otstup = 3
shirina_s_otstupom = shirina_uacheiki + otstup
visota_s_otstupom = visota_uacheiki + otstup

squre = [shirina_s_otstupom*stolbiki+otstup, visota_s_otstupom*stroki+otstup]
SIZE = [1000, 600]
# -----------------------------------
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Kyrsovaya")

clock = pygame.time.Clock()

ship_n = 0

squre_size = 250
squre_1 = pygame.Surface((squre_size,squre_size))
squre_1.fill((0,255,255))
squre_2 = pygame.Surface((squre_size,squre_size))
squre_2.fill((0,255,255))

ship_1 = pygame.Surface((24,24))
ship_1.fill((255,255,0))
ship_2 = pygame.Surface((48,24))
ship_2.fill((255,255,0))
ship_3 = pygame.Surface((72,24))
ship_3.fill((255,255,0))
ship_4 = pygame.Surface((96,24))
ship_4.fill((255,255,0))

# gm = 3
# gw = 25
# gh = 25
# i = 10
# j = 10
#
# grid = []
# for ii in range(i):
#     grid.append([])
#     for jj in range(j):
#         grid[ii].append(0)
# Loop until the user clicks the close button.
done = False

#-------------------------------------------------
stroki = 10
stolbiki = 10
otstup = 2
shirina_s_otstupom = (SIZE[0]-otstup)/(stolbiki+30)
shirina_uacheiki = shirina_s_otstupom - otstup
visota_s_otstupom = (SIZE[1]-otstup)/(stroki+14)
visota_uacheiki = visota_s_otstupom - otstup
#-------------------------------------------------

stroki_1 = 1
stolbiki_1 = 1
otstup = 2
shirina_s_otstupom_1 = (SIZE[0]+otstup)/(stolbiki_1+46)
shirina_uacheiki_1 = shirina_s_otstupom_1-otstup
visota_s_otstupom_1 = (SIZE[1]+otstup)/(stroki_1+26)
visota_uacheiki_1 = visota_s_otstupom_1 - otstup


background=pygame.image.load("1364161083_morskoy-boy-0-409x200.jpg").convert_alpha()
grid = []
for stroka in range(stroki):
    grid.append([])
    for stolbik in range(stolbiki):
        grid[stroka].append(0)
print(grid)
def change_color(x, y):
    j = int(x/shirina_s_otstupom)
    i = int(y/visota_s_otstupom)
    grid[i][j]=1






color_cell = GREY

ship_1_c=(225, 380)
ship_2_c=(225, 430)
ship_3_c=(225, 480)
ship_4_c=(225, 530)

squre_1_c=(200, 100)
squre_2_c=(550, 100)
while not done:
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                i, j = event.pos
                if (i > squre_1_c[0] and i<squre_1_c[0]+squre_size) and (j>squre_1_c[1]and j<squre_1_c[1]+squre_size):
                    print(1)
                    print(i,j)
                elif (i > squre_2_c[0] and i<squre_2_c[0]+squre_size) and (j>squre_2_c[1]and j<squre_2_c[1]+squre_size):
                    print(2)
                    print(i, j)
                else:
                    print(3)
                    print(i, j)
                    if (i>ship_1_c[0] and i<ship_1_c[0]+shirina_uacheiki_1) and (j>ship_1_c[1] and j<ship_1_c[1]+visota_uacheiki_1 ):
                        ship_n=1
                if screen==ship_1_c:
                    ship_1.fill((255,255,255))


# draw_stick_figure(screen, x, y)
    # Set the screen background
    screen.fill(GREEN)
    # screen.blit(background_image, [0, 0])
    screen.blit(background, [0, 0])
    screen.blit(squre_1, squre_1_c)
    screen.blit(squre_2, squre_2_c)
    screen.blit(ship_1, ship_1_c)
    screen.blit(ship_2, ship_2_c)
    screen.blit(ship_3, ship_3_c)
    screen.blit(ship_4, ship_4_c)
    x = 0
    y = 0
    #pygame.draw.line(squre_1,GREEN,[x, y], [x, SIZE[1]], otstup)
    #pygame.draw.line(squre_1,GREEN,[x, y], [SIZE[0], y], otstup)
    #pygame.draw.line(squre_1,GREEN,[SIZE[0], y], [SIZE[0], SIZE[1]], otstup)
    #pygame.draw.line(squre_1,GREEN,[SIZE[0], SIZE[1]], [x, SIZE[1]], otstup)
    for stroka in range(stroki):
        y = stroka*visota_s_otstupom + otstup
        for stolbik in range(stolbiki):
            x = stolbik*shirina_s_otstupom + otstup

            pygame.draw.rect(squre_1,color_cell,[x , y, shirina_uacheiki, visota_uacheiki])
            pygame.draw.rect(squre_2, color_cell, [x, y, shirina_uacheiki, visota_uacheiki])
            pygame.draw.rect(ship_1, color_cell, [x, y, shirina_uacheiki_1, visota_uacheiki_1])
            pygame.draw.rect(ship_2, color_cell, [x, y, shirina_uacheiki_1, visota_uacheiki_1])
            pygame.draw.rect(ship_3, color_cell, [x, y, shirina_uacheiki_1, visota_uacheiki_1])
            pygame.draw.rect(ship_4, color_cell, [x, y, shirina_uacheiki_1, visota_uacheiki_1])

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(60)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

