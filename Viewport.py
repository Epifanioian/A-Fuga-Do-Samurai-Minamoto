from Transformacoes import *
from Primitivas import *
from Cores import *
from Preenchimento import *

#======================================================
#          BLOCO 29: JANELA -> VIEWPORT
#======================================================

def janela_viewport(janela, viewport):

    Wxmin, Wymin, Wxmax, Wymax = janela
    Vxmin, Vymin, Vxmax, Vymax = viewport

    sx = (
        (Vxmax - Vxmin)
        / (Wxmax - Wxmin)
    )

    sy = (
        (Vymax - Vymin)
        / (Wymax - Wymin)
    )

    M = identidade()

    M = multiplica_matrizes(
        translacao(
            -Wxmin,
            -Wymin
        ),
        M
    )

    M = multiplica_matrizes(
        escala(
            sx,
            sy
        ),
        M
    )

    M = multiplica_matrizes(
        translacao(
            Vxmin,
            Vymin
        ),
        M
    )

    return M

#======================================================
#      BLOCO 30: FUNÇÕES AUXILIARES PARA VIEWPORT
#======================================================
def desenhar_viewport(tela, viewport):
    xmin, ymin, xmax, ymax = viewport
    pontosViewport = [
        (xmin, ymin),
        (xmax, ymin),
        (xmax, ymax),
        (xmin, ymax)
    ]

    desenhar_poligono(tela, pontosViewport, PRETO)

def desenhar_poligono_viewport(
    tela,
    pontos,
    matrizViewport,
    corPreenchimento,
    corBorda
):

    pontos_view = aplica_transformacao(
        matrizViewport,
        pontos
    )

    scanline_fill(
        tela,
        pontos_view,
        corPreenchimento
    )

    desenhar_poligono(
        tela,
        pontos_view,
        corBorda
    )

def restaurar_sobreposicao_viewport(tela, aabb, Pixels):
    if aabb is None:
        return

    if Pixels is None:
        return

    x1, y1, x2, y2 = aabb

    margem = 5

    x1 = max(950, int(x1 - margem))
    x2 = min(1249, int(x2 + margem))
    y1 = max(50, int(y1 - margem))
    y2 = min(249, int(y2 + margem))

    if x1 > x2 or y1 > y2:
        return

    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            setPixel(tela, x, y, Pixels[y - 50][x - 950])