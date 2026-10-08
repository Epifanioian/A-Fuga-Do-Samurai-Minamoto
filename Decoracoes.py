import pygame
import sys
from Primitivas import *
from Preenchimento import *
from Cores import *

#======================================================
#             BLOCO 4: ÁRVORE SAKURA
#======================================================

def desenhar_sakura(superficie, base_x, base_y):

    tronco = [
        (base_x - 31, base_y),
        (base_x + 31, base_y),
        (base_x + 20, base_y - 184),
        (base_x - 20, base_y - 184)
    ]
    scanline_fill(superficie, tronco, MARROM)
    desenhar_poligono(superficie, tronco, MARROM_ESCURO)

    origem_x = base_x
    origem_y = base_y - 180

    
    preencher_elipse(superficie, origem_x, origem_y + 8, 20, 12, MARROM)
    desenhar_elipse(superficie, origem_x, origem_y + 8, 20, 12, MARROM_ESCURO)

    
    desenhar_galho(superficie, origem_x, origem_y + 6, origem_x, origem_y - 128, MARROM_ESCURO, 7)
    desenhar_galho(superficie, origem_x - 3, origem_y + 8, origem_x - 70, origem_y - 84, MARROM_ESCURO, 6)
    desenhar_galho(superficie, origem_x + 3, origem_y + 8, origem_x + 70, origem_y - 84, MARROM_ESCURO, 6)
    desenhar_galho(superficie, origem_x - 5, origem_y + 6, origem_x - 102, origem_y - 38, MARROM_ESCURO, 4)
    desenhar_galho(superficie, origem_x + 5, origem_y + 6, origem_x + 102, origem_y - 38, MARROM_ESCURO, 4)

    
    desenhar_galho(superficie, origem_x - 66, origem_y - 82, origem_x - 89, origem_y - 108, MARROM_ESCURO, 3)
    desenhar_galho(superficie, origem_x + 66, origem_y - 82, origem_x + 89, origem_y - 108, MARROM_ESCURO, 3)
    desenhar_galho(superficie, origem_x, origem_y - 126, origem_x - 16, origem_y - 150, MARROM_ESCURO, 3)
    desenhar_galho(superficie, origem_x, origem_y - 126, origem_x + 16, origem_y - 150, MARROM_ESCURO, 3)

    
    partes_copa = [
        (base_x - 110, base_y - 222, 54, 34, ROSA_COPA_1),
        (base_x - 56,  base_y - 238, 58, 36, ROSA_COPA_2),
        (base_x,       base_y - 246, 66, 40, ROSA_COPA_3),
        (base_x + 56,  base_y - 238, 58, 36, ROSA_COPA_2),
        (base_x + 110, base_y - 222, 54, 34, ROSA_COPA_1),

        (base_x - 74,  base_y - 292, 50, 32, ROSA_COPA_2),
        (base_x,       base_y - 302, 58, 35, ROSA_COPA_4),
        (base_x + 74,  base_y - 292, 50, 32, ROSA_COPA_2),

        (base_x - 28,  base_y - 342, 40, 25, ROSA_COPA_1),
        (base_x + 28,  base_y - 342, 40, 25, ROSA_COPA_1),
        (base_x,       base_y - 365, 42, 26, ROSA_COPA_3),
    ]

    for cx, cy, rx, ry, cor_preenchimento in partes_copa:
        preencher_elipse(superficie, cx, cy, rx, ry, cor_preenchimento)
        desenhar_elipse(superficie, cx, cy, rx, ry, ROSA_CONTORNO)

    flores = [
        (base_x - 128, base_y - 220, 0.76),
        (base_x - 98,  base_y - 234, 0.84),
        (base_x - 70,  base_y - 246, 0.88),
        (base_x - 38,  base_y - 252, 0.90),
        (base_x,       base_y - 258, 0.98),
        (base_x + 38,  base_y - 252, 0.90),
        (base_x + 70,  base_y - 246, 0.88),
        (base_x + 98,  base_y - 234, 0.84),
        (base_x + 128, base_y - 220, 0.76),

        (base_x - 84,  base_y - 294, 0.84),
        (base_x - 36,  base_y - 306, 0.90),
        (base_x,       base_y - 312, 0.96),
        (base_x + 36,  base_y - 306, 0.90),
        (base_x + 84,  base_y - 294, 0.84),

        (base_x - 34,  base_y - 345, 0.80),
        (base_x,       base_y - 356, 0.90),
        (base_x + 34,  base_y - 345, 0.80),
    ]

    for fx, fy, escala in flores:
        desenhar_flor_sakura(superficie, fx, fy, escala)

#======================================================
#           BLOCO 5: DESENHAR GALHO
#======================================================

def desenhar_galho(superficie, x0, y0, x1, y1, cor, espessura=3):
    metade = espessura // 2

    for deslocamento in range(-metade, metade + 1):
        bresenham(
            superficie,
            x0 + deslocamento,
            y0,
            x1 + deslocamento,
            y1,
            cor
        )

#======================================================
#          BLOCO 6: DESENHAR FLOR DE SAKURA
#======================================================

def desenhar_flor_sakura(superficie, cx, cy, escala=1.0):

    distancia = max(5, int(8 * escala))
    rx = max(3, int(6 * escala))
    ry = max(2, int(4 * escala))
    raio_miolo = max(2, int(3 * escala))

    for i in range(5):
        angulo = math.radians(i * 72 - 90)

        px = int(cx + math.cos(angulo) * distancia)
        py = int(cy + math.sin(angulo) * distancia)

        desenhar_elipse(
            superficie,
            px,
            py,
            rx,
            ry,
            ROSA_CONTORNO
        )

        flood_fill(
            superficie,
            px,
            py,
            ROSA_CLARO
        )

    desenhar_circulo(
        superficie,
        cx,
        cy,
        raio_miolo,
        AMARELO
    )

    flood_fill(
        superficie,
        cx,
        cy,
        AMARELO
    )
#======================================================
#         BLOCO 7: FUNÇÕES DE APOIO DA CASA
#======================================================

def desenhar_retangulo(superficie, x1, y1, x2, y2, cor_preenchimento, cor_borda):
    pontos = [
        (x1, y1),
        (x2, y1),
        (x2, y2),
        (x1, y2)
    ]
    scanline_fill(superficie, pontos, cor_preenchimento)
    desenhar_poligono(superficie, pontos, cor_borda)


def desenhar_lanterna(superficie, cx, cy, raio):

    desenhar_circulo(superficie, cx, cy, raio, VERMELHO_ESCURO)
    flood_fill(superficie, cx, cy, VERMELHO2)
    bresenham(superficie, cx, cy - raio - 8, cx, cy - raio, VERMELHO_ESCURO)
    bresenham(superficie, cx, cy + raio, cx, cy + raio + 10, VERMELHO_ESCURO)
    desenhar_circulo(superficie, cx, cy, max(1, raio // 4), AMARELO2)


def desenhar_janela_grade(superficie, x1, y1, x2, y2):

    desenhar_retangulo(superficie, x1, y1, x2, y2, CREME, VINHO)

    passo_x = max(8, (x2 - x1) // 4)
    x = x1 + passo_x
    while x < x2:
        bresenham(superficie, x, y1, x, y2, VINHO)
        x += passo_x

    passo_y = max(8, (y2 - y1) // 3)
    y = y1 + passo_y
    while y < y2:
        bresenham(superficie, x1, y, x2, y, VINHO)
        y += passo_y


def desenhar_casa_japonesa(superficie, base_x, base_y):

    def janela_preta_vermelha(x1, y1, x2, y2):
        desenhar_retangulo(
            superficie,
            x1, y1, x2, y2,
            PRETO2,
            VERMELHO_ESCURO2
        )

        largura_janela = x2 - x1
        altura_janela = y2 - y1

        for i in range(1, 4):
            x = x1 + int(largura_janela * i / 4)
            bresenham(superficie, x, y1, x, y2, VERMELHO_CLARO)

        for i in range(1, 3):
            y = y1 + int(altura_janela * i / 3)
            bresenham(superficie, x1, y, x2, y, VERMELHO_CLARO)


    desenhar_retangulo(
        superficie,
        base_x - 165, base_y - 20,
        base_x + 165, base_y + 22,
        PRETO2,
        PRETO2
    )

    degraus = [
        (base_x - 48, base_y - 5,  base_x + 48, base_y + 2),
        (base_x - 42, base_y - 14, base_x + 42, base_y - 7),
        (base_x - 36, base_y - 23, base_x + 36, base_y - 16),
        (base_x - 30, base_y - 32, base_x + 30, base_y - 25),
    ]

    for x1, y1, x2, y2 in degraus:
        desenhar_retangulo(
            superficie,
            x1, y1, x2, y2,
            VERMELHO_CLARO,
            PRETO2
        )


    desenhar_retangulo(
        superficie,
        base_x - 130, base_y - 145,
        base_x + 130, base_y - 20,
        VERMELHO3,
        PRETO2
    )

    for x in [
        base_x - 118,
        base_x - 52,
        base_x + 52,
        base_x + 118
    ]:
        desenhar_retangulo(
            superficie,
            x - 5, base_y - 145,
            x + 5, base_y - 20,
            PRETO2,
            PRETO2
        )

    desenhar_retangulo(
        superficie,
        base_x - 38, base_y - 112,
        base_x + 38, base_y - 20,
        PRETO2,
        VERMELHO_ESCURO2
    )

    bresenham(
        superficie,
        base_x, base_y - 112,
        base_x, base_y - 20,
        VERMELHO_ESCURO2
    )

    desenhar_circulo(
        superficie,
        base_x - 12, base_y - 63,
        4,
        VERMELHO_CLARO
    )

    desenhar_circulo(
        superficie,
        base_x + 12, base_y - 63,
        4,
        VERMELHO_CLARO
    )

    janela_preta_vermelha(
        base_x - 106, base_y - 112,
        base_x - 58, base_y - 66
    )

    janela_preta_vermelha(
        base_x + 58, base_y - 112,
        base_x + 106, base_y - 66
    )

    bresenham(
        superficie,
        base_x - 142, base_y - 66,
        base_x + 142, base_y - 66,
        PRETO2
    )

    bresenham(
        superficie,
        base_x - 142, base_y - 52,
        base_x + 142, base_y - 52,
        PRETO2
    )

    for x in range(base_x - 138, base_x + 139, 20):
        bresenham(
            superficie,
            x, base_y - 66,
            x, base_y - 44,
            PRETO2
        )


    corpo_telhado_1 = [
        (base_x - 168, base_y - 174),
        (base_x + 168, base_y - 174),
        (base_x + 136, base_y - 145),
        (base_x - 136, base_y - 145)
    ]

    scanline_fill(
        superficie,
        corpo_telhado_1,
        PRETO2
    )

    desenhar_poligono(
        superficie,
        corpo_telhado_1,
        VERMELHO_ESCURO2
    )

    beiral_esq_1 = [
        (base_x - 205, base_y - 192),
        (base_x - 168, base_y - 174),
        (base_x - 136, base_y - 145),
        (base_x - 174, base_y - 152)
    ]

    beiral_dir_1 = [
        (base_x + 168, base_y - 174),
        (base_x + 205, base_y - 192),
        (base_x + 174, base_y - 152),
        (base_x + 136, base_y - 145)
    ]

    for poligono in [beiral_esq_1, beiral_dir_1]:
        scanline_fill(
            superficie,
            poligono,
            PRETO2
        )

        desenhar_poligono(
            superficie,
            poligono,
            VERMELHO_ESCURO2
        )

    ponta_esq_1 = [
        (base_x - 218, base_y - 220),
        (base_x - 205, base_y - 192),
        (base_x - 174, base_y - 152),
        (base_x - 188, base_y - 165)
    ]

    ponta_dir_1 = [
        (base_x + 205, base_y - 192),
        (base_x + 218, base_y - 220),
        (base_x + 188, base_y - 165),
        (base_x + 174, base_y - 152)
    ]

    for poligono in [ponta_esq_1, ponta_dir_1]:
        scanline_fill(
            superficie,
            poligono,
            VERMELHO3
        )

        desenhar_poligono(
            superficie,
            poligono,
            PRETO2
        )

    for x in range(base_x - 150, base_x + 151, 15):
        bresenham(
            superficie,
            x, base_y - 172,
            x + 8, base_y - 147,
            VERMELHO_ESCURO2
        )


    desenhar_retangulo(
        superficie,
        base_x - 92, base_y - 262,
        base_x + 92, base_y - 174,
        VERMELHO3,
        PRETO2
    )

    for x in [
        base_x - 80,
        base_x,
        base_x + 80
    ]:
        desenhar_retangulo(
            superficie,
            x - 4, base_y - 262,
            x + 4, base_y - 174,
            PRETO2,
            PRETO2
        )

    janela_preta_vermelha(
        base_x - 64, base_y - 244,
        base_x - 18, base_y - 202
    )

    janela_preta_vermelha(
        base_x + 18, base_y - 244,
        base_x + 64, base_y - 202
    )

    bresenham(
        superficie,
        base_x - 104, base_y - 202,
        base_x + 104, base_y - 202,
        PRETO2
    )

    bresenham(
        superficie,
        base_x - 104, base_y - 188,
        base_x + 104, base_y - 188,
        PRETO2
    )

    for x in range(base_x - 100, base_x + 101, 18):
        bresenham(
            superficie,
            x, base_y - 202,
            x, base_y - 174,
            PRETO2
        )


    corpo_telhado_2 = [
        (base_x - 132, base_y - 292),
        (base_x + 132, base_y - 292),
        (base_x + 100, base_y - 262),
        (base_x - 100, base_y - 262)
    ]

    scanline_fill(
        superficie,
        corpo_telhado_2,
        PRETO2
    )

    desenhar_poligono(
        superficie,
        corpo_telhado_2,
        VERMELHO_ESCURO2
    )

    beiral_esq_2 = [
        (base_x - 164, base_y - 308),
        (base_x - 132, base_y - 292),
        (base_x - 100, base_y - 262),
        (base_x - 134, base_y - 268)
    ]

    beiral_dir_2 = [
        (base_x + 132, base_y - 292),
        (base_x + 164, base_y - 308),
        (base_x + 134, base_y - 268),
        (base_x + 100, base_y - 262)
    ]

    for poligono in [beiral_esq_2, beiral_dir_2]:
        scanline_fill(
            superficie,
            poligono,
            PRETO2
        )

        desenhar_poligono(
            superficie,
            poligono,
            VERMELHO_ESCURO2
        )

    ponta_esq_2 = [
        (base_x - 175, base_y - 334),
        (base_x - 164, base_y - 308),
        (base_x - 134, base_y - 268),
        (base_x - 146, base_y - 280)
    ]

    ponta_dir_2 = [
        (base_x + 164, base_y - 308),
        (base_x + 175, base_y - 334),
        (base_x + 146, base_y - 280),
        (base_x + 134, base_y - 268)
    ]

    for poligono in [ponta_esq_2, ponta_dir_2]:
        scanline_fill(
            superficie,
            poligono,
            VERMELHO3
        )

        desenhar_poligono(
            superficie,
            poligono,
            PRETO2
        )

    for x in range(base_x - 116, base_x + 117, 14):
        bresenham(
            superficie,
            x, base_y - 290,
            x + 7, base_y - 264,
            VERMELHO_ESCURO2
        )


    desenhar_retangulo(
        superficie,
        base_x - 16, base_y - 318,
        base_x + 16, base_y - 292,
        VERMELHO_ESCURO2,
        PRETO2
    )

    telhado_topo = [
        (base_x - 52, base_y - 342),
        (base_x + 52, base_y - 342),
        (base_x + 28, base_y - 318),
        (base_x - 28, base_y - 318)
    ]

    scanline_fill(
        superficie,
        telhado_topo,
        PRETO2
    )

    desenhar_poligono(
        superficie,
        telhado_topo,
        VERMELHO_ESCURO2
    )

    ponta_esq_topo = [
        (base_x - 64, base_y - 362),
        (base_x - 52, base_y - 342),
        (base_x - 28, base_y - 318),
        (base_x - 38, base_y - 327)
    ]

    ponta_dir_topo = [
        (base_x + 52, base_y - 342),
        (base_x + 64, base_y - 362),
        (base_x + 38, base_y - 327),
        (base_x + 28, base_y - 318)
    ]

    for poligono in [ponta_esq_topo, ponta_dir_topo]:
        scanline_fill(
            superficie,
            poligono,
            VERMELHO3
        )

        desenhar_poligono(
            superficie,
            poligono,
            PRETO2
        )

    for deslocamento in [-1, 0, 1]:
        bresenham(
            superficie,
            base_x + deslocamento, base_y - 342,
            base_x + deslocamento, base_y - 372,
            PRETO2
        )
