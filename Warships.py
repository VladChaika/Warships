import pygame
import random

from pygame.locals import *
from sys import exit
def warships(self):
    pygame.init()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREY = (200, 200, 200)
    GREEN = (0, 255, 0)
    SIZE = [800, 600]

    grid = []
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Морський бій")

    ship_n = 0
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 30)
    text_4 = font.render("4",True,BLACK)
    text_3 = font.render("3",True,BLACK)
    text_2 = font.render("2",True,BLACK)
    text_1 = font.render("1",True,BLACK)

    numb_1_1 = font.render("1",True,BLACK)
    numb_1_2 = font.render("2",True,BLACK)
    numb_1_3 = font.render("3",True,BLACK)
    numb_1_4 = font.render("4",True,BLACK)
    numb_1_5 = font.render("5", True, BLACK)
    numb_1_6 = font.render("6", True, BLACK)
    numb_1_7 = font.render("7", True, BLACK)
    numb_1_8 = font.render("8", True, BLACK)
    numb_1_9 = font.render("9",True,BLACK)
    numb_1_10 = font.render("10",True,BLACK)
    numb_2_1 = font.render("1",True,BLACK)
    numb_2_2 = font.render("2",True,BLACK)
    numb_2_3 = font.render("3",True,BLACK)
    numb_2_4 = font.render("4",True,BLACK)
    numb_2_5 = font.render("5",True,BLACK)
    numb_2_6 = font.render("6",True,BLACK)
    numb_2_7 = font.render("7",True,BLACK)
    numb_2_8 = font.render("8",True,BLACK)
    numb_2_9 = font.render("9",True,BLACK)
    numb_2_10 = font.render("10",True,BLACK)

    letter_1_1 = font.render("А",True,BLACK)
    letter_1_2 = font.render("Б",True,BLACK)
    letter_1_3 = font.render("В",True,BLACK)
    letter_1_4 = font.render("Г",True,BLACK)
    letter_1_5 = font.render("Д",True,BLACK)
    letter_1_6 = font.render("Е",True,BLACK)
    letter_1_7 = font.render("Є",True,BLACK)
    letter_1_8 = font.render("Ж",True,BLACK)
    letter_1_9 = font.render("З",True,BLACK)
    letter_1_10 = font.render("И",True,BLACK)
    letter_2_1 = font.render("А",True,BLACK)
    letter_2_2 = font.render("Б",True,BLACK)
    letter_2_3 = font.render("В",True,BLACK)
    letter_2_4 = font.render("Г",True,BLACK)
    letter_2_5 = font.render("Д",True,BLACK)
    letter_2_6 = font.render("Е",True,BLACK)
    letter_2_7 = font.render("Є",True,BLACK)
    letter_2_8 = font.render("Ж",True,BLACK)
    letter_2_9 = font.render("З",True,BLACK)
    letter_2_10 = font.render("И",True,BLACK)

    squre_1 = pygame.Surface((202,202))
    squre_1.fill((0,255,255))
    squre_2 = pygame.Surface((202,202))
    squre_2.fill((0,255,255))

    Ship_1 = pygame.Surface((21,21))
    Ship_1.fill((255,255,0))
    Ship_2 = pygame.Surface((41,21))
    Ship_2.fill((255,255,0))
    Ship_3 = pygame.Surface((61,21))
    Ship_3.fill((255,255,0))
    Ship_4 = pygame.Surface((81,21))
    Ship_4.fill((255,255,0))

    line_1 = pygame.Surface((20,2))
    line_1.fill(BLACK)
    line_2=pygame.Surface((20,2))
    line_2.fill(BLACK)
    line_3=pygame.Surface((20,2))
    line_3.fill(BLACK)
    line_4=pygame.Surface((20,2))
    line_4.fill(BLACK)

    squre=pygame.Surface((20,20))
    squre.fill((200,255,255))

    done = False
    def draw_setka_1():
        x = 0
        x_x =200
        y = 0
        y_y = 200
        for i in range(11):
            pygame.draw.line(squre_1, (BLACK), (x, y), (x, y_y), 2)
            x += 20
        x = 0
        for i2 in range(11):
            pygame.draw.line(squre_1, (BLACK), (x, y), (x_x, y), 2)
            y += 20

    def draw_setka_2():
        x = 0
        x_x =200
        y = 0
        y_y = 200
        for i in range(11):
            pygame.draw.line(squre_2, (BLACK), (x, y), (x, y_y), 2)
            x += 20
        x = 0
        for i2 in range(11):
            pygame.draw.line(squre_2, (BLACK), (x, y), (x_x, y), 2)
            y += 20

    class Ships():
        def __init__(self, xpos, ypos):
            self.xpos = xpos
            self.ypos = ypos
            self.bitmap = pygame.Surface((18,18))
            self.bitmap.fill(WHITE)
        def render(self):
            squre_1.blit(self.bitmap, (self.xpos * 20+2 ,self.ypos * 20+2 ))

    ship_1_1 = Ships(5, 3)
    ship_1_2 = Ships(1, 8)
    ship_1_3 = Ships(8, 0)
    ship_1_4 = Ships(7, 8)

    #ship_2_1 = Ships(0, 3)
    #ship_2_2 = Ships(9, 5)
    #ship_2_3 = Ships(4, 8)

    #ship_3_1 = Ships(3, 0)
    #ship_3_2 = Ships(7, 2)

    #ship_4 = Ships(3, 5)

    #----------------------------------------

    ship_2_1_1 = Ships(0, 3)
    ship_2_1_2 = Ships(0, 4)
    ship_2_2_1 = Ships(9, 5)
    ship_2_2_2 = Ships(9, 6)
    ship_2_3_1 = Ships(4, 8)
    ship_2_3_2 = Ships(4, 9)

    ship_3_1_1 = Ships(3, 0)
    ship_3_1_2 = Ships(3, 1)
    ship_3_1_3 = Ships(3, 2)
    ship_3_2_1 = Ships(7, 2)
    ship_3_2_2 = Ships(8, 2)
    ship_3_2_3 = Ships(9, 2)


    ship_4_1 = Ships(3, 5)
    ship_4_2 = Ships(4, 5)
    ship_4_3 = Ships(5, 5)
    ship_4_4 = Ships(6, 5)

    #-------------------------------------
    going = '' # для клавиш
    list_1_1 = [ship_1_1]
    list_1_2 = [ship_1_2]
    list_1_3 = [ship_1_3]
    list_1_4 = [ship_1_4]
    list_2_1 = [ship_2_1_1,ship_2_1_2]
    list_2_2 = [ship_2_2_1,ship_2_2_2]
    list_2_3 = [ship_2_3_1,ship_2_3_2]
    list_3_1 = [ship_3_1_1,ship_3_1_2,ship_3_1_3]
    list_3_2 = [ship_3_2_1,ship_3_2_2,ship_3_2_3]
    list_4 = [ship_4_1,ship_4_2,ship_4_3,ship_4_4]


    '''
    list_2_1 = [ship_2_1_1,ship_2_1_2]
    list_2_2 = [ship_2_2_1,ship_2_2_2]
    list_2_3 = [ship_2_3_1,ship_2_3_2]
    list_3_1 = [ship_3_1_1,ship_3_1_2,ship_3_1_3]
    list_3_2 = [ship_3_2_1,ship_3_2_2,ship_3_2_3]
    list_4 = [ship_4_1,ship_4_2,ship_4_3,ship_4_4]
    '''

    background = pygame.image.load("1364161083_morskoy-boy-0-409x200.jpg").convert_alpha()
    background_spip_1=pygame.image.load("1 ship.jpg").convert_alpha()
    background_spip_2=pygame.image.load("2 ship_g.jpg").convert_alpha()
    background_spip_3=pygame.image.load("3 ship_g.jpg").convert_alpha()
    background_spip_4=pygame.image.load("4 ship_g.jpg").convert_alpha()
    i=0
    j=0

    def change_grid_status(x, y):
        j = int(x / 22)
        i = int(y / 22)
        if grid[i][j]["nagata"] > 0:
            grid[i][j]["nagata"] = 0
        else:
            grid[i][j]["nagata"] = 1
    ship_1 = pygame.Surface((24, 24))
    ship_1_c = (225, 380)
    ship_2_c = (225, 430)
    ship_3_c = (225, 480)
    ship_4_c = (225, 530)

    squre_1_c = ((150, 125))
    squre_2_c = (550, 100)

    stroki_1 = 1
    stolbiki_1 = 1
    otstup = 2
    shirina_s_otstupom_1 = (SIZE[0] + otstup) / (stolbiki_1 + 46)
    shirina_uacheiki_1 = shirina_s_otstupom_1 - otstup
    visota_s_otstupom_1 = (SIZE[1] + otstup) / (stroki_1 + 26)
    visota_uacheiki_1 = visota_s_otstupom_1 - otstup
    squre_size = 250

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    i, j = event.pos
                    if (i > squre_1_c[0] and i < squre_1_c[0] + squre_size) and (
                            j > squre_1_c[1] and j < squre_1_c[1] + squre_size):
                        print(1)
                        print(i, j)
                    elif (i > squre_2_c[0] and i < squre_2_c[0] + squre_size) and (
                            j > squre_2_c[1] and j < squre_2_c[1] + squre_size):
                        print(2)
                        print(i, j)
                    else:
                        print(3)
                        print(i, j)
                        if (i > ship_1_c[0] and i < ship_1_c[0] + shirina_uacheiki_1) and (
                                j > ship_1_c[1] and j < ship_1_c[1] + visota_uacheiki_1):
                            ship_n = 1
                    if screen == ship_1_c:
                        ship_1.fill((255, 255, 255))
        for elem in range(10):
            i = random.randint(0, 10 - 1)
            j = random.randint(0, 10 - 1)


        screen.fill(GREEN)
        screen.blit(background, [0, 0])
        Ship_1.blit(background_spip_1, [0, 0])
        Ship_2.blit(background_spip_2, [0, 0])
        Ship_3.blit(background_spip_3, [0, 0])
        Ship_4.blit(background_spip_4, [0, 0])

        screen.blit(squre_1, (150, 125))
        screen.blit(squre_2, (450, 125))

        screen.blit(Ship_1, (175, 380))
        screen.blit(Ship_2, (175, 430))
        screen.blit(Ship_3, (175, 480))
        screen.blit(Ship_4, (175, 530))

        screen.blit(line_1, (210, 390))
        screen.blit(line_2, (230, 440))
        screen.blit(line_3, (250, 490))
        screen.blit(line_4, (270, 540))

        screen.blit(text_1, [240, 380])
        screen.blit(text_2, [260, 430])
        screen.blit(text_3, [280, 480])
        screen.blit(text_4, [300, 528])

        screen.blit(numb_1_1, [135, 127])
        screen.blit(numb_1_2, [135, 147])
        screen.blit(numb_1_3, [135, 167])
        screen.blit(numb_1_4, [135, 187])
        screen.blit(numb_1_5, [135, 207])
        screen.blit(numb_1_6, [135, 227])
        screen.blit(numb_1_7, [135, 247])
        screen.blit(numb_1_8, [135, 267])
        screen.blit(numb_1_9, [135, 287])
        screen.blit(numb_1_10, [125, 307])
        screen.blit(numb_2_1, [435, 127])
        screen.blit(numb_2_2, [435, 147])
        screen.blit(numb_2_3, [435, 167])
        screen.blit(numb_2_4, [435, 187])
        screen.blit(numb_2_5, [435, 207])
        screen.blit(numb_2_6, [435, 227])
        screen.blit(numb_2_7, [435, 247])
        screen.blit(numb_2_8, [435, 267])
        screen.blit(numb_2_9, [435, 287])
        screen.blit(numb_2_10, [425, 307])
        screen.blit(letter_1_1, [155, 105])
        screen.blit(letter_1_2, [175, 105])
        screen.blit(letter_1_3, [195, 105])
        screen.blit(letter_1_4, [215, 105])
        screen.blit(letter_1_5, [232, 105])
        screen.blit(letter_1_6, [255, 105])
        screen.blit(letter_1_7, [273, 105])
        screen.blit(letter_1_8, [290, 105])
        screen.blit(letter_1_9, [315, 105])
        screen.blit(letter_1_10, [335, 105])
        screen.blit(letter_2_1, [455, 105])
        screen.blit(letter_2_2, [475, 105])
        screen.blit(letter_2_3, [495, 105])
        screen.blit(letter_2_4, [515, 105])
        screen.blit(letter_2_5, [532, 105])
        screen.blit(letter_2_6, [555, 105])
        screen.blit(letter_2_7, [573, 105])
        screen.blit(letter_2_8, [590, 105])
        screen.blit(letter_2_9, [615, 105])
        screen.blit(letter_2_10, [635, 105])


        draw_setka_1()
        draw_setka_2()
        for i in list_1_1:
            i.render()
        for i in list_1_2:
            i.render()
        for i in list_1_3:
            i.render()
        for i in list_1_4:
            i.render()
        for i in list_2_1:
            i.render()
        for i in list_2_2:
            i.render()
        for i in list_2_3:
            i.render()
        for i in list_3_1:
            i.render()
        for i in list_3_2:
            i.render()
        for i in list_4:
            i.render()


        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
warships