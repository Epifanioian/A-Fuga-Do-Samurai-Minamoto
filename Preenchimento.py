import pygame
import sys
from Primitivas import *

#======================================================
#            BLOCO 15: SCANLINE FILL
#======================================================

def scanline_fill(superficie, pontos, cor): 
 
    ys = [p[1] for p in pontos] 
 
    y_min = max( 
        0, 
        int(min(ys)) 
    ) 
 
    y_max = min( 
        superficie.get_height() - 1, 
        int(max(ys)) 
    ) 
 
    n = len(pontos) 
 
    for y in range(y_min, y_max + 1): 
 
        intersecoes = [] 
 
        for i in range(n): 
 
            x0, y0 = pontos[i] 
            x1, y1 = pontos[(i + 1) % n] 
 
            if y0 == y1: 
                continue 
 
            if y0 > y1: 
                x0, y0, x1, y1 = ( 
                    x1, y1, 
                    x0, y0 
                ) 
 
            if y < y0 or y >= y1: 
                continue 
 
            x = ( 
                x0 
                + (y - y0) 
                * (x1 - x0) 
                / (y1 - y0) 
            ) 
 
            intersecoes.append(x) 
 
        intersecoes.sort() 
 
        for i in range( 
            0, 
            len(intersecoes), 
            2 
        ): 
 
            if i + 1 < len(intersecoes): 
 
                x_inicio = int( 
                    intersecoes[i] 
                ) 
 
                x_fim = int( 
                    intersecoes[i + 1] 
                ) 
 
                for x in range( 
                    x_inicio, 
                    x_fim + 1 
                ): 
 
                    setPixel( 
                        superficie, 
                        x, 
                        y, 
                        cor 
                    )

#======================================================
#          BLOCO 16: CÉU EM GRADIENTE
#======================================================

def desenhar_ceu_gradiente(superficie, y_inicio, y_fim, cor_topo, cor_base):
    largura = superficie.get_width()

    if y_fim <= y_inicio:
        return

    altura_gradiente = y_fim - y_inicio

    for y in range(y_inicio, y_fim + 1):
        t = (y - y_inicio) / altura_gradiente

        r = int(cor_topo[0] * (1 - t) + cor_base[0] * t)
        g = int(cor_topo[1] * (1 - t) + cor_base[1] * t)
        b = int(cor_topo[2] * (1 - t) + cor_base[2] * t)

        for x in range(largura):
            setPixel(superficie, x, y, (r, g, b))

#======================================================
#             BLOCO 17: FLOOD FILL
#======================================================

def flood_fill(superficie, x, y, cor_nova):
    largura_superficie = superficie.get_width()
    altura_superficie = superficie.get_height()

    if x < 0 or x >= largura_superficie or y < 0 or y >= altura_superficie:
        return

    cor_antiga = tuple(superficie.get_at((x, y))[:3])

    if cor_antiga == cor_nova:
        return

    pilha = [(x, y)]

    while pilha:
        px, py = pilha.pop()

        if px < 0 or px >= largura_superficie or py < 0 or py >= altura_superficie:
            continue

        cor_atual = tuple(superficie.get_at((px, py))[:3])

        if cor_atual != cor_antiga:
            continue

        setPixel(superficie, px, py, cor_nova)

        pilha.append((px + 1, py))
        pilha.append((px - 1, py))
        pilha.append((px, py + 1))
        pilha.append((px, py - 1))

#======================================================
#          BLOCO 18: PREENCHIMENTO DA ELIPSE
#======================================================

def preencher_elipse(superficie, xc, yc, rx, ry, cor):
    for y in range(-ry, ry + 1):
        termo = 1 - (y * y) / (ry * ry)

        if termo < 0:
            termo = 0

        limite_x = int(rx * math.sqrt(termo))

        for x in range(-limite_x, limite_x + 1):
            px = xc + x
            py = yc + y

            if 0 <= px < superficie.get_width() and 0 <= py < superficie.get_height():
                setPixel(superficie, px, py, cor)

#======================================================
#          BLOCO 19: DESENHAR RETÂNGULO
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