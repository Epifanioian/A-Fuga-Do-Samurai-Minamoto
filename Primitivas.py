import pygame
import sys
import math

clip_atual = None
#======================================================
#              BLOCO 20: SET PIXEL
#======================================================

def setPixel(superficie, x, y, cor):

    global clip_atual

    x = int(x)
    y = int(y)

    if not (
        0 <= x < superficie.get_width()
        and
        0 <= y < superficie.get_height()
    ):
        return

    if clip_atual is not None:

        xmin, ymin, xmax, ymax = clip_atual

        if (
            x < xmin
            or x > xmax
            or y < ymin
            or y > ymax
        ):
            return

    superficie.set_at(
        (x, y),
        cor
    )
#======================================================
#          BLOCO 21: ALGORITMO DE BRESENHAM
#======================================================

def bresenham(superficie, x0, y0, x1, y1, cor): 
 
    x0 = int(x0) 
    y0 = int(y0) 
    x1 = int(x1) 
    y1 = int(y1) 
 
    steep = abs(y1 - y0) > abs(x1 - x0) 
 
    if steep: 
        x0, y0 = y0, x0 
        x1, y1 = y1, x1 
 
    if x0 > x1: 
        x0, x1 = x1, x0 
        y0, y1 = y1, y0 
 
    dx = x1 - x0 
    dy = abs(y1 - y0) 
 
    ystep = 1 if y0 < y1 else -1 
 
    d = 2 * dy - dx 
    y = y0 
 
    for x in range(x0, x1 + 1): 
 
        if steep: 
            setPixel(superficie, y, x, cor) 
        else: 
            setPixel(superficie, x, y,cor) 
 
        if d > 0: 
            y += ystep 
            d -= 2 * dx 
        d += 2 * dy 

#======================================================
#          BLOCO 22: DESENHAR POLÍGONO
#======================================================

def desenhar_poligono(superficie, pontos, cor): 
 
    n = len(pontos) 
 
    for i in range(n): 
 
        x0, y0 = pontos[i] 
        x1, y1 = pontos[(i + 1) % n] 
 
        bresenham(superficie, x0, y0, x1, y1,cor) 

#======================================================
#          BLOCO 23: CIRCUNFERÊNCIA
#======================================================

def desenhar_circulo(superficie, xc, yc, raio, cor):
    x = 0
    y = raio
    d = 1 - raio

    while x <= y:
        pontos = [
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x)
        ]

        for px, py in pontos:
            if 0 <= px < superficie.get_width() and 0 <= py < superficie.get_height():
                setPixel(superficie, px, py, cor)

        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1

        x += 1

#======================================================
#                BLOCO 24: ELIPSE
#======================================================

def desenhar_elipse(superficie, xc, yc, rx, ry, cor):
    x = 0
    y = ry

    rx2 = rx * rx
    ry2 = ry * ry

    dx = 2 * ry2 * x
    dy = 2 * rx2 * y

    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)

    while dx < dy:
        pontos = [
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y)
        ]

        for px, py in pontos:
            if 0 <= px < superficie.get_width() and 0 <= py < superficie.get_height():
                setPixel(superficie, int(px), int(py), cor)

        if p1 < 0:
            x += 1
            dx = 2 * ry2 * x
            p1 += dx + ry2
        else:
            x += 1
            y -= 1
            dx = 2 * ry2 * x
            dy = 2 * rx2 * y
            p1 += dx - dy + ry2

    p2 = (
        ry2 * (x + 0.5) * (x + 0.5)
        + rx2 * (y - 1) * (y - 1)
        - rx2 * ry2
    )

    while y >= 0:
        pontos = [
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y)
        ]

        for px, py in pontos:
            if 0 <= px < superficie.get_width() and 0 <= py < superficie.get_height():
                setPixel(superficie, int(px), int(py), cor)

        if p2 > 0:
            y -= 1
            dy = 2 * rx2 * y
            p2 += rx2 - dy
        else:
            y -= 1
            x += 1
            dx = 2 * ry2 * x
            dy = 2 * rx2 * y
            p2 += dx - dy + rx2

#======================================================
#          BLOCO 25: PREENCHER CIRCULO
#======================================================
def preencher_circulo(superficie, xc, yc, raio, cor):

    for y in range(-raio, raio + 1):

        distancia = int(math.sqrt(raio * raio - y * y))

        for x in range(xc - distancia, xc + distancia + 1):

            if 0 <= x < superficie.get_width() and 0 <= yc + y < superficie.get_height():
                setPixel(superficie, x, yc + y, cor)

#======================================================
#      BLOCO 26: FUNÇÕES AUXILIARES PARA CLIPPING
#======================================================
def definir_clip(viewport):
    global clip_atual
    clip_atual = viewport


def remover_clip():
    global clip_atual
    clip_atual = None