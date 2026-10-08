import pygame
import sys
from Preenchimento import *
from Primitivas import *
from Cores import *
from Personagens import *
from Decoracoes import *
from EfeitosGraficos import *

#======================================================
#          BLOCO 31: FONTE JAPONESA
#======================================================
def obter_fonte_japonesa(tamanho, bold=True):
    for nome in ["Yu Gothic UI", "Yu Gothic", "MS Gothic", "Noto Sans CJK JP", "Arial Unicode MS", "Arial"]:
        try:
            return pygame.font.SysFont(nome, tamanho, bold=bold)
        except:
            pass
    return pygame.font.SysFont(None, tamanho, bold=bold)

#======================================================
#          BLOCO 32: DESENHAR ESCUDO PAZ
#======================================================
def desenhar_escudo_paz(superficie, cx, cy):
    dourado = (214, 177, 88)
    dourado_escuro = (124, 86, 27)
    vinho = (101, 26, 26)
    creme = (245, 235, 215)

    escudo = [
        (cx - 34, cy - 42),
        (cx + 34, cy - 42),
        (cx + 40, cy - 12),
        (cx + 28, cy + 28),
        (cx, cy + 54),
        (cx - 28, cy + 28),
        (cx - 40, cy - 12)
    ]

    scanline_fill(superficie, escudo, dourado)
    desenhar_poligono(superficie, escudo, dourado_escuro)

    faixa = [
        (cx - 25, cy - 10),
        (cx + 25, cy - 10),
        (cx + 20, cy + 18),
        (cx - 20, cy + 18)
    ]
    scanline_fill(superficie, faixa, vinho)
    desenhar_poligono(superficie, faixa, dourado_escuro)

    fonte_jp = obter_fonte_japonesa(25, True)
    texto = fonte_jp.render("平和", True, creme)
    superficie.blit(texto, (cx - texto.get_width() // 2, cy - texto.get_height() // 2 + 3))

#======================================================
#          BLOCO 33: DESENHAR TÍTULO
#======================================================
def desenhar_titulo(superficie):
    fonte = pygame.font.SysFont("Georgia", 51, bold=True)
    titulo = "A Fuga do Samurai Minamoto"

    sombra = fonte.render(titulo, True, (79, 48, 31))
    texto = fonte.render(titulo, True, (245, 235, 218))

    x = 640 - texto.get_width() // 2 + 34
    superficie.blit(sombra, (x + 3, 48))
    superficie.blit(texto, (x, 43))
    desenhar_escudo_paz(superficie, x - 62, 74)

#======================================================
#          BLOCO 34: DESENHAR BOTÃO
#======================================================
def desenhar_botao(superficie, fonte, texto, x1, y1, x2, y2):
    creme = (241, 216, 168)
    creme_claro = (249, 233, 198)
    marrom = (74, 43, 27)
    sombra = (136, 88, 48)
    vermelho = (155, 57, 43)

    sombra_pts = [(x1 + 7, y1 + 8), (x2 + 7, y1 + 8), (x2 + 7, y2 + 8), (x1 + 7, y2 + 8)]
    scanline_fill(superficie, sombra_pts, sombra)

    pontos = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
    scanline_fill(superficie, pontos, creme)
    desenhar_poligono(superficie, pontos, marrom)

    for y in range(y1 + 8, y2 - 4, 9):
        bresenham(superficie, x1 + 15, y, x2 - 15, y, (224, 191, 133))

    bresenham(superficie, x1 + 15, y1 + 12, x1 + 15, y2 - 12, vermelho)
    bresenham(superficie, x2 - 15, y1 + 12, x2 - 15, y2 - 12, vermelho)

    brilho = [(x1 + 3, y1 + 3), (x2 - 3, y1 + 3), (x2 - 3, y1 + 17), (x1 + 3, y1 + 17)]
    scanline_fill(superficie, brilho, creme_claro)

    txt = fonte.render(texto, True, (22, 16, 12))
    tx = (x1 + x2) // 2 - txt.get_width() // 2
    ty = (y1 + y2) // 2 - txt.get_height() // 2
    superficie.blit(txt, (tx, ty))

#======================================================
#            BLOCO 35: DESENHAR MENU
#======================================================

def desenhar_menu(tela, fonte):
    desenhar_ceu_gradiente(tela, 0, 599, (241, 226, 214), (170, 199, 229))

    desenhar_sol_com_clipping(
        tela,
        1160, 115, 38,
        (900, 18, 1260, 250),
        cor_sol=(194, 69, 52),
        cor_raio=(196, 120, 82)
    )

    pontos_chao = [(0, 720), (1280, 720), (1280, 600), (0, 600)]
    scanline_fill(tela, pontos_chao, (116, 145, 98))

    for x in range(0, 1280, 18):
        bresenham(tela, x, 720, x - 13, 607, (100, 126, 84))
    for x in range(8, 1280, 29):
        bresenham(tela, x, 720, x + 7, 620, (137, 163, 116))

    desenhar_titulo(tela)

    desenhar_sakura(tela, 180, 600)
    desenhar_casa_japonesa(tela, 1055, 600)

    aplicar_textura_telhado(tela, 1055, 600)

    desenhar_botao(tela, fonte, "Jogar", 440, 190, 840, 290)
    desenhar_botao(tela, fonte, "História", 440, 320, 840, 420)
    desenhar_botao(tela, fonte, "Sair", 440, 450, 840, 550)


#======================================================
#          BLOCO 36: DESENHAR HISTÓRIA
#======================================================

def desenhar_historia(tela):
    desenhar_ceu_gradiente(tela, 0, 719, (240, 223, 210), (176, 205, 232))

    fonte_titulo = pygame.font.SysFont("Georgia", 40, bold=True)
    fonte_historia = pygame.font.SysFont("Georgia", 24, bold=True)
    fonte_voltar = pygame.font.SysFont("Georgia", 20, bold=True)

    titulo = fonte_titulo.render("A Fuga do Samurai Minamoto", True, (0, 0, 0))
    x_titulo = 640 - titulo.get_width() // 2
    tela.blit(titulo, (x_titulo, 55))

    caixa_historia = [(150, 130), (1130, 130), (1130, 610), (150, 610)]
    scanline_fill(tela, caixa_historia, (255, 165, 0))
    desenhar_poligono(tela, caixa_historia, (0, 0, 0))

    linhas = [
        "Em uma época marcada por guerras entre clãs,",
        "um jovem samurai do poderoso Clã Minamoto",
        "recebe uma missão que pode decidir o futuro de seu povo.",
        "",
        "Durante sua jornada, ele descobre que foi cercado",
        "por ninjas inimigos enviados para impedir sua fuga.",
        "Sem tempo para enfrentar todos eles, resta apenas correr.",
        "",
        "Agora, o samurai precisa atravessar caminhos perigosos,",
        "superar obstáculos e manter distância dos perseguidores.",
        "A cada passo, os ninjas se aproximam.",
        "",
        "Seu objetivo é simples: sobreviver à perseguição,",
        "escapar dos ninjas e levar sua missão até o fim.",
        "",
        "Corra. Desvie. Não deixe que eles alcancem você."
    ]

    y_texto = 165
    for linha in linhas:
        if linha == "":
            y_texto += 15
            continue
        texto = fonte_historia.render(linha, True, (0, 0, 0))
        tela.blit(texto, (640 - texto.get_width() // 2, y_texto))
        y_texto += 31

    voltar = fonte_voltar.render("Aperte ESC para voltar ao menu", True, (0, 0, 0))
    tela.blit(voltar, (640 - voltar.get_width() // 2, 640))

#======================================================
#            BLOCO 37: DESENHAR JOGAR
#======================================================

def desenhar_jogar(tela, fonte, fonte2):
    desenhar_ceu_gradiente(tela, 0, 599, (230, 240, 252), (130, 180, 225))

    pontos_chao = [(0, 720), (1280, 720), (1280, 600), (0, 600)]
    scanline_fill(tela, pontos_chao, (0, 128, 0))

    desenhar_botao(tela, fonte, "Nível I", 440, 190, 840, 290)
    desenhar_botao(tela, fonte, "Nível II", 440, 320, 840, 420)

    b3 = fonte2.render("Aperte ESC para voltar ao menu", True, (255, 255, 255))
    tela.blit(b3, (640 - b3.get_width() // 2, 680))

    desenhar_ninja(tela)
    desenhar_samurai(tela)