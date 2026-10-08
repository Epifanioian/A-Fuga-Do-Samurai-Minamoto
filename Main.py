import pygame 
import sys 
import math
from Cores import *
from Primitivas import *
from Preenchimento import *
from Personagens import *
from Jogo1 import *
from Menus import *
 
pygame.init() 
pygame.mixer.music.load("EfeitosSonoros/bounce-bay-records-traditional-japanese-3-437933.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
 
#======================================================
#          BLOCO 1: CONFIGURAÇÃO BÁSICA
#======================================================
pygame.font.init() 
fonte = pygame.font.SysFont("Georgia", 40, bold=True) 
fonte2 = pygame.font.SysFont("Georgia", 20, bold=True)
largura = 1280 
altura = 720 
tela = pygame.display.set_mode((largura, altura)) 
pygame.display.set_caption("A Fuga do Samurai Minamoto")

#======================================================
#          BLOCO 2: LOOP PRINCIPAL
#======================================================
estado = "menu" 
rodando = True 
while rodando: 
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            rodando = False 
        elif evento.type == pygame.KEYDOWN: 
            if evento.key == pygame.K_ESCAPE: 
                if estado == "menu": 
                    rodando = False 
                elif estado == "fase1" or estado == "fase2":
                    estado = "jogar"
                else: 
                    estado = "menu" 
                
 
        elif evento.type == pygame.MOUSEBUTTONDOWN: 
            if evento.button == 1: 
                pos_x, pos_y = evento.pos 
 
                if estado == "menu": 
                    if 440 < pos_x < 840: 
                        if 190 < pos_y < 290: 
                            estado = "jogar" 
                        elif 320 < pos_y < 420: 
                            estado = "historia" 
                        elif 450 < pos_y < 550: 
                            rodando = False 
                elif(estado == "jogar"): 
                    if 440 < pos_x < 840:
                        if 190 < pos_y < 290:
                            reiniciar_fase1()
                            estado = "fase1"
                        elif 320 < pos_y < 420:
                            reiniciar_fase2()
                            estado = "fase2"
                    

    if estado == "menu": 
        desenhar_menu(tela, fonte) 
    elif estado == "historia": 
        desenhar_historia(tela) 
    elif estado == "jogar": 
        desenhar_jogar(tela, fonte, fonte2) 
    elif estado == "fase1":
        fase1(tela)
    elif estado == "fase2":
        fase2(tela)

    pygame.display.flip()
 
pygame.quit()
sys.exit()