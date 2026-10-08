import pygame
import sys
from Cores import *
from Transformacoes import *
from Primitivas import *
from Preenchimento import *

#======================================================
#          BLOCO 13: DESENHAR SAMURAI
#======================================================

def desenhar_samurai(tela, matriz = None, frame = 0):

    if matriz is None:
        matriz = identidade()

    def transformar(pontos):
        return aplica_transformacao(matriz, pontos)

    if frame == 0:
        pontosBotaE = [
            (150, 570),
            (120, 570),
            (120, 599),
            (160, 599),
            (160, 580),
            (150, 580)
        ]

        pontosBotaD = [
            (200, 570),
            (170, 570),
            (170, 599),
            (210, 599),
            (210, 580),
            (200, 580)
        ]


    if frame == 1:
        pontosBotaE = [
            (140, 570),
            (110, 570),
            (110, 599),
            (150, 599),
            (150, 580),
            (140, 580)
        ]
        
        pontosBotaD = [
            (180, 570), 
            (210, 570), 
            (210, 580), 
            (220, 580), 
            (220, 599), 
            (180, 599)
        ]

    if frame == 0:
        pontosPerna = [
            (120, 500),
            (200, 500),
            (200, 570),
            (170, 570),
            (170, 520),
            (150, 520),
            (150, 570),
            (120, 570)
        ]

    if frame == 1:
        pontosPerna = [
            (120, 500),
            (200, 500),
            (210, 570),
            (180, 570),
            (170, 520),
            (150, 520),
            (140, 570),
            (110, 570)
        ]
    
    pontosTronco = [
        (180, 400),
        (140, 400),
        (140, 410),
        (120, 410),
        (100, 420),
        (100, 480),
        (120, 480),
        (120, 550),
        (160, 520),
        (200, 550),
        (200, 480),
        (220, 480),
        (220, 420),
        (200, 410),
        (180, 410),
    ]
    
    pontosMaoE = [
        (120, 480),
        (100, 480),
        (100, 500),
        (120, 500)
    ]
    
    pontosMaoD = [
        (220, 480),
        (200, 480),
        (200, 500),
        (220, 500)
    ]
    
    pontosCabeca = [
        (185, 330),
        (135, 330),
        (135, 335),
        (130, 335),
        (130, 395),
        (135, 395),
        (135, 400),
        (145, 400),
        (160, 415),
        (175, 400),
        (185, 400),
        (185, 395),
        (190, 395),
        (190, 335),
        (185, 335)    
    ]
    
    pontosOlhoE = [
        (155, 355),
        (148, 355),
        (148, 365),
        (155, 365)
    ]
    
    pontosOlhoD = [
        (182, 355),
        (175, 355),
        (175, 365),
        (182, 365)
    ]

    pontosBotao = [
        (158, 498),
        (162, 498),
        (162, 502),
        (158, 502)
    ]

    pontosCinto = [
        (120, 496),
        (200, 496),
        (200, 504),
        (120, 504)
    ]

    pontosCabeloH = [
        (130, 330),
        (190, 330),
        (190, 342),
        (130, 342)
    ]

    pontosCabeloV = [
        (130, 330),
        (137, 330),
        (137, 400),
        (130, 400)
    ]

    pontosChonmage = [
        (118, 326),
        (129, 326),
        (129, 341),
        (118, 341)
    ]

    pontosBoca = [
        (157, 379),
        (173, 379),
        (173, 381),
        (170, 381),
        (170, 383),
        (157, 383)
    ]

    pontosBotaE_t = transformar(pontosBotaE)
    pontosBotaD_t = transformar(pontosBotaD)
    pontosPerna_t = transformar(pontosPerna)
    pontosTronco_t = transformar(pontosTronco)
    pontosMaoE_t = transformar(pontosMaoE)
    pontosMaoD_t = transformar(pontosMaoD)
    divisoriaE = transformar([(120, 480), (120, 440)])
    divisoriaD = transformar([(200, 480), (200, 440)])
    pontosCabeca_t = transformar(pontosCabeca)
    pontosOlhoE_t = transformar(pontosOlhoE)
    pontosOlhoD_t = transformar(pontosOlhoD)
    pontosBotao_t = transformar(pontosBotao)
    pontosCinto_t = transformar(pontosCinto)
    pontosCabeloH_t = transformar(pontosCabeloH)
    pontosCabeloV_t = transformar(pontosCabeloV)
    pontosChonmage_t = transformar(pontosChonmage)
    pontosBoca_t = transformar(pontosBoca)

    scanline_fill(tela, pontosBotaD_t, PRETO)
    desenhar_poligono(tela, pontosBotaD_t, PRETO)
    scanline_fill(tela, pontosBotaE_t, PRETO)
    desenhar_poligono(tela, pontosBotaE_t, PRETO)

    scanline_fill(tela, pontosPerna_t, CINZA)
    desenhar_poligono(tela, pontosPerna_t, PRETO)

    scanline_fill(tela, pontosTronco_t, AZUL_ESCURO)
    desenhar_poligono(tela, pontosTronco_t, PRETO)

    scanline_fill(tela, pontosMaoD_t, SAMURAI_PELE)
    desenhar_poligono(tela, pontosMaoD_t, PRETO)
    scanline_fill(tela, pontosMaoE_t, SAMURAI_PELE)
    desenhar_poligono(tela, pontosMaoE_t, PRETO)

    bresenham(tela, divisoriaE[0][0], divisoriaE[0][1], divisoriaE[1][0], divisoriaE[1][1], PRETO)
    bresenham(tela, divisoriaD[0][0], divisoriaD[0][1], divisoriaD[1][0], divisoriaD[1][1], PRETO)

    scanline_fill(tela, pontosCabeca_t, SAMURAI_PELE)
    desenhar_poligono(tela, pontosCabeca_t, PRETO)

    scanline_fill(tela, pontosCinto_t, CASTANHO_ESCURO)
    desenhar_poligono(tela, pontosCinto_t, PRETO)

    scanline_fill(tela, pontosOlhoD_t, PRETO)
    scanline_fill(tela, pontosOlhoE_t, PRETO)

    scanline_fill(tela, pontosBotao_t, DOURADO)
    desenhar_poligono(tela, pontosBotao_t, PRETO)

    scanline_fill(tela, pontosCabeloH_t, PRETO)

    scanline_fill(tela, pontosCabeloV_t, PRETO)

    scanline_fill(tela, pontosChonmage_t, PRETO)

    scanline_fill(tela, pontosBoca_t, PRETO)

    pontosSamurai = (pontosBotaE_t + pontosBotaD_t + pontosPerna_t + pontosTronco_t + pontosMaoE_t + pontosMaoD_t + pontosCabeca_t)
    return pontosSamurai

#======================================================
#           BLOCO 14: DESENHAR NINJA
#======================================================

def desenhar_ninja(tela, matriz = None, frame = 0):

    if matriz is None:
        matriz = identidade()

    def transformar(pontos):
        return aplica_transformacao(matriz, pontos)

    if frame == 0:
        pontosBotaD = [
            (1170, 570),
            (1200, 570),
            (1200, 599),
            (1160, 599),
            (1160, 580),
            (1170, 580)
        ]

        pontosBotaE = [
            (1120, 570),
            (1150, 570),
            (1150, 599),
            (1110, 599),
            (1110, 580),
            (1120, 580)
        ]

    if frame == 1:
        pontosBotaD = [
            (1180, 570),
            (1210, 570),
            (1210, 599),
            (1170, 599),
            (1170, 580),
            (1180, 580)
        ]

        pontosBotaE = [
            (1110, 570),
            (1140, 570),
            (1140, 599),
            (1100, 599),
            (1100, 580),
            (1110, 580)
        ]
    if frame == 0:
        pontosPerna = [
            (1120, 500),
            (1200, 500),
            (1200, 570),
            (1170, 570),
            (1170, 520),
            (1150, 520),
            (1150, 570),
            (1120, 570)
        ]

    if frame == 1:
        pontosPerna = [
            (1120, 500),
            (1200, 500),
            (1210, 570),
            (1180, 570),
            (1170, 520),
            (1150, 520),
            (1140, 570),
            (1110, 570)
        ]

    pontosTronco = [
        (1140, 400),
        (1180, 400),
        (1180, 410),
        (1200, 410),
        (1220, 420),
        (1220, 480),
        (1200, 480),
        (1200, 500),
        (1120, 500),
        (1120, 480),
        (1100, 480),
        (1100, 420),
        (1120, 410),
        (1140, 410),
    ]

    pontosMaoD = [
        (1200, 480),
        (1220, 480),
        (1220, 500),
        (1200, 500)
    ]

    pontosMaoE = [
        (1100, 480),
        (1120, 480),
        (1120, 500),
        (1100, 500)
    ]

    pontosCabeca = [
        (1135, 330),
        (1185, 330),
        (1185, 335),
        (1190, 335),
        (1190, 395),
        (1185, 395),
        (1185, 400),
        (1135, 400),
        (1135, 395),
        (1130, 395),
        (1130, 335),
        (1135, 335)
    ]

    pontosAbertura = [
        (1135, 350),
        (1185, 350),
        (1185, 370),
        (1160, 366),
        (1135, 370)
    ]

    pontosCinto = [
        (1120, 498),
        (1200, 498),
        (1200, 502),
        (1120, 502)
    ]

    pontosFaixa = [
        (1183, 410),
        (1200, 410),
        (1138, 498),
        (1121, 498)
    ]

    pontosOlhoD = [
        (1170, 355),
        (1177, 355),
        (1177, 365),
        (1170, 365)
    ]

    pontosOlhoE = [
        (1143, 355),
        (1150, 355),
        (1150, 365),
        (1143, 365)
    ]

    pontosBotaD_t = transformar(pontosBotaD)
    pontosBotaE_t = transformar(pontosBotaE)
    pontosPerna_t = transformar(pontosPerna)
    pontosTronco_t = transformar(pontosTronco)
    pontosMaoD_t = transformar(pontosMaoD)
    pontosMaoE_t = transformar(pontosMaoE)
    divisoriaD = transformar([(1200,480),(1200,440)])
    divisoriaE = transformar([(1120,480),(1120,440)])
    pontosCabeca_t = transformar(pontosCabeca)
    pontosAbertura_t = transformar(pontosAbertura)
    pontosCinto_t = transformar(pontosCinto)
    pontosFaixa_t = transformar(pontosFaixa)
    pontosOlhoD_t = transformar(pontosOlhoD)
    pontosOlhoE_t = transformar(pontosOlhoE)

    scanline_fill(tela, pontosBotaD_t, PRETO)
    desenhar_poligono(tela, pontosBotaD_t, PRETO)
    scanline_fill(tela, pontosBotaE_t, PRETO)
    desenhar_poligono(tela, pontosBotaE_t, PRETO)

    scanline_fill(tela, pontosPerna_t, CINZA_ESCURO)
    desenhar_poligono(tela, pontosPerna_t, PRETO)

    scanline_fill(tela, pontosTronco_t, CINZA_ESCURO)
    desenhar_poligono(tela, pontosTronco_t, PRETO)

    scanline_fill(tela, pontosMaoD_t, NINJA_PELE)
    desenhar_poligono(tela, pontosMaoD_t, PRETO)
    scanline_fill(tela, pontosMaoE_t, NINJA_PELE)
    desenhar_poligono(tela, pontosMaoE_t, PRETO)

    bresenham(tela, divisoriaD[0][0], divisoriaD[0][1], divisoriaD[1][0], divisoriaD[1][1], PRETO)
    bresenham(tela, divisoriaE[0][0], divisoriaE[0][1], divisoriaE[1][0], divisoriaE[1][1], PRETO)

    scanline_fill(tela, pontosCabeca_t, CINZA_ESCURO)
    desenhar_poligono(tela, pontosCabeca_t, PRETO)

    scanline_fill(tela, pontosAbertura_t, NINJA_PELE)
    desenhar_poligono(tela, pontosAbertura_t, PRETO)

    scanline_fill(tela, pontosCinto_t, PRETO)

    scanline_fill(tela, pontosFaixa_t, VERMELHO)
    desenhar_poligono(tela, pontosFaixa_t, PRETO)

    scanline_fill(tela, pontosOlhoD_t, PRETO)
    scanline_fill(tela, pontosOlhoE_t, PRETO)

    pontosNinja = (pontosBotaE_t + pontosBotaD_t + pontosPerna_t + pontosTronco_t + pontosMaoE_t + pontosMaoD_t + pontosCabeca_t)
    return pontosNinja
