import math
import os
import pygame
from Primitivas import setPixel, bresenham, desenhar_circulo


#======================================================
#        BLOCO 48: CARREGAR TEXTURA TELHADO
#======================================================
_textura_telha_cache = None


def carregar_textura_telha():

    global _textura_telha_cache

    if _textura_telha_cache is None:
        caminho = os.path.join(os.path.dirname(__file__), "Textura/telha.jpg")
        _textura_telha_cache = pygame.image.load(caminho).convert()

    return _textura_telha_cache


def scanline_fill_textura_imagem(superficie, pontos, textura):
   
    if len(pontos) < 3:
        return

    xs = [p[0] for p in pontos]
    ys = [p[1] for p in pontos]

    x_min_pol = min(xs)
    x_max_pol = max(xs)
    y_min_pol = min(ys)
    y_max_pol = max(ys)

    largura_pol = max(1, x_max_pol - x_min_pol)
    altura_pol = max(1, y_max_pol - y_min_pol)

    largura_tex = textura.get_width()
    altura_tex = textura.get_height()

    y_min = max(0, int(y_min_pol))
    y_max = min(superficie.get_height() - 1, int(y_max_pol))

    n = len(pontos)

    for y in range(y_min, y_max + 1):
        intersecoes = []

        for i in range(n):
            x0, y0 = pontos[i]
            x1, y1 = pontos[(i + 1) % n]

            
            if y0 == y1:
                continue

            if y0 > y1:
                x0, y0, x1, y1 = x1, y1, x0, y0

            if y < y0 or y >= y1:
                continue

            x = x0 + (y - y0) * (x1 - x0) / (y1 - y0)
            intersecoes.append(x)

        intersecoes.sort()

        for i in range(0, len(intersecoes), 2):
            if i + 1 >= len(intersecoes):
                continue

            x_inicio = max(0, int(intersecoes[i]))
            x_fim = min(superficie.get_width() - 1, int(intersecoes[i + 1]))

            for x in range(x_inicio, x_fim + 1):
                
                u_normalizado = (x - x_min_pol) / largura_pol
                v_normalizado = (y - y_min_pol) / altura_pol

                
                u = int(u_normalizado * (largura_tex - 1))
                v = int(v_normalizado * (altura_tex - 1))

                
                u = max(0, min(largura_tex - 1, u))
                v = max(0, min(altura_tex - 1, v))

                cor = textura.get_at((u, v))
                setPixel(superficie, x, y, cor)


#======================================================
#         BLOCO 49: CLIPPING COHEN-SUTHERLAND
#======================================================
INSIDE = 0
LEFT = 1
RIGHT = 2
TOP = 4
BOTTOM = 8


def _outcode(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT

    if y < ymin:
        code |= TOP
    elif y > ymax:
        code |= BOTTOM

    return code


def linha_clipada(superficie, x1, y1, x2, y2, xmin, ymin, xmax, ymax, cor):
    
    code1 = _outcode(x1, y1, xmin, ymin, xmax, ymax)
    code2 = _outcode(x2, y2, xmin, ymin, xmax, ymax)

    while True:
        if code1 == 0 and code2 == 0:
            bresenham(superficie, int(x1), int(y1), int(x2), int(y2), cor)
            return True

        if code1 & code2:
            return False

        out = code1 if code1 != 0 else code2

        if out & TOP:
            if y2 == y1:
                return False
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin

        elif out & BOTTOM:
            if y2 == y1:
                return False
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax

        elif out & RIGHT:
            if x2 == x1:
                return False
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            x = xmax

        else:  # LEFT
            if x2 == x1:
                return False
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin

        if out == code1:
            x1, y1 = x, y
            code1 = _outcode(x1, y1, xmin, ymin, xmax, ymax)
        else:
            x2, y2 = x, y
            code2 = _outcode(x2, y2, xmin, ymin, xmax, ymax)


#======================================================
#        BLOCO 50: SOL COM RAIOS CLIPADOS
#======================================================
def desenhar_sol_com_clipping(
    superficie,
    cx,
    cy,
    raio,
    janela,
    cor_sol=(205, 70, 50),
    cor_raio=(205, 115, 75)
):
    xmin, ymin, xmax, ymax = janela


    for angulo in range(0, 360, 20):
        rad = math.radians(angulo)
        x1 = cx + math.cos(rad) * (raio + 8)
        y1 = cy + math.sin(rad) * (raio + 8)
        x2 = cx + math.cos(rad) * (raio + 65)
        y2 = cy + math.sin(rad) * (raio + 65)

        linha_clipada(
            superficie,
            x1, y1,
            x2, y2,
            xmin, ymin,
            xmax, ymax,
            cor_raio
        )

    desenhar_circulo(superficie, cx, cy, raio, cor_sol)


    r2 = raio * raio

    for y in range(cy - raio + 1, cy + raio):
        for x in range(cx - raio + 1, cx + raio):
            if (x - cx) * (x - cx) + (y - cy) * (y - cy) <= r2:
                if (
                    0 <= x < superficie.get_width()
                    and 0 <= y < superficie.get_height()
                ):
                    setPixel(superficie, x, y, cor_sol)


#======================================================
#       BLOCO 51: APLICAÇÃO TEXTURA TELHADO
#======================================================
def aplicar_textura_telhado(superficie, base_x, base_y):
   
    textura = carregar_textura_telha()

    telhado_inferior = [
        (base_x - 168, base_y - 174),
        (base_x + 168, base_y - 174),
        (base_x + 136, base_y - 145),
        (base_x - 136, base_y - 145)
    ]

    telhado_superior = [
        (base_x - 132, base_y - 292),
        (base_x + 132, base_y - 292),
        (base_x + 100, base_y - 262),
        (base_x - 100, base_y - 262)
    ]

    telhado_topo = [
        (base_x - 52, base_y - 342),
        (base_x + 52, base_y - 342),
        (base_x + 28, base_y - 318),
        (base_x - 28, base_y - 318)
    ]

    for poligono in (
        telhado_inferior,
        telhado_superior,
        telhado_topo
    ):
        scanline_fill_textura_imagem(
            superficie,
            poligono,
            textura
        )