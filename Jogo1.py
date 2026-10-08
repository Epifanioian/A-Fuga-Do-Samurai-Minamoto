import pygame
import sys
from Cores import *
from Preenchimento import *
from Transformacoes import *
from Personagens import *
from Colisoes import *
from Primitivas import *
from Viewport import *

#======================================================
#            BLOCO 38: VARIÁVEIS GLOBAIS
#======================================================

pygame.mixer.init()
somPulo = pygame.mixer.Sound("EfeitosSonoros/dragon-studio-cartoon-jump-463196.mp3")
largura = 1280 
altura = 720 

viewport = (950, 50, 1250, 250)
janela = (0, 0, 1280, 720)


posicaoXS = 0
posicaoYS = 0

velocidadeXS1 = 11
velocidadeXN1 = 13

velocidadeXS2 = 11
velocidadeXN2 = 18

velocidadeYS = 0
gravidade = 1
forcaPulo = -26
chao = True
posicaoXN = 0

velocidadeXS = velocidadeXS1
velocidadeXN = velocidadeXN1

anguloSamurai = 0

qtdDeslocamentos = 0
limDeslocamentos = 7
direcaoDeslocamento = 1

vidas = 3
vuneravel = True

estadoJogo1 = "jogando"

cenario = False
cenarioFracionado = None
aabbSamuraiAntes = None
aabbNinjaAntes = None

frameSamurai = 0
contadorAnimacaoSamurai = 0
frameNinja = 0
contadorAnimacaoNinja = 0

cenarioViewport = False
cenarioViewportFracionado = None

aabbSamuraiViewportAntes = None
aabbNinjaViewportAntes = None

matrizMinimapa = None

vidas_anterior = -1

#======================================================
#            BLOCO 39: JOGAR NÍVEL I
#======================================================
def fase1(tela):
    global posicaoXS
    global posicaoYS
    global velocidadeYS
    global chao
    global posicaoXN
    global anguloSamurai

    global qtdDeslocamentos
    global direcaoDeslocamento

    global vidas
    global vuneravel

    global estadoJogo1

    global cenario
    global cenarioFracionado
    global aabbSamuraiAntes
    global aabbNinjaAntes

    global frameSamurai
    global contadorAnimacaoSamurai
    global frameNinja
    global contadorAnimacaoNinja

    global cenarioViewport
    global cenarioViewportFracionado

    global aabbSamuraiViewportAntes
    global aabbNinjaViewportAntes

    global matrizMinimapa

    if estadoJogo1 == "derrota":
        desenhar_tela_derrota(tela)
        return

    if estadoJogo1 == "vitoria":
        desenhar_tela_vitoria(tela)
        return

    if not cenario:
        desenhar_fase1(tela)
        cenarioFracionado = salvar_cenario(tela)
        cenario = True

    if not cenarioViewport:

        matrizMinimapa = janela_viewport(
            janela,
            viewport
        )

        definir_clip(viewport)

        desenhar_cenario_viewport(
            tela,
            matrizMinimapa
        )

        remover_clip()

        cenarioViewportFracionado = salvar_viewport(tela)

        cenarioViewport = True

        desenhar_viewport(
            tela,
            viewport
        )


    restaurar_cenario(tela, aabbSamuraiAntes, cenarioFracionado)
    restaurar_cenario(tela, aabbNinjaAntes, cenarioFracionado)
    
    teclas = pygame.key.get_pressed()
    if chao:
        if teclas[pygame.K_LEFT] or teclas[pygame.K_RIGHT]:
            contadorAnimacaoSamurai = contadorAnimacaoSamurai + 1

            if contadorAnimacaoSamurai >= 8:
                contadorAnimacaoSamurai = 0

                if frameSamurai == 0:
                    frameSamurai = 1
                else:
                    frameSamurai = 0
        else:
            frameSamurai = 0
            contadorAnimacaoSamurai = 0
    
    if teclas[pygame.K_LEFT]:
        posicaoXS = posicaoXS - velocidadeXS

    if teclas[pygame.K_RIGHT]:
        posicaoXS = posicaoXS + velocidadeXS

    if posicaoXS < -100:
        posicaoXS = -100

    if posicaoXS > 1060:
        posicaoXS = 1060

    if teclas[pygame.K_SPACE] and chao:
        velocidadeYS = forcaPulo
        anguloSamurai = 0
        chao = False
        somPulo.play()

    velocidadeYS = velocidadeYS + gravidade
    posicaoYS = posicaoYS + velocidadeYS

    if not chao:
        anguloSamurai = anguloSamurai + 0.001
        frameSamurai = 0
        contadorAnimacaoSamurai = 0

    if posicaoYS >= 0:
        posicaoYS = 0
        velocidadeYS = 0
        chao = True
        anguloSamurai = 0

    matrizN_e = identidade()
    matrizS_e = identidade()
    if qtdDeslocamentos < limDeslocamentos:
        posicaoXN = posicaoXN - (velocidadeXN * direcaoDeslocamento)
        contadorAnimacaoNinja = contadorAnimacaoNinja + 1
        if contadorAnimacaoNinja >= 8:
            contadorAnimacaoNinja = 0

            if frameNinja == 0:
                frameNinja =  1
            else:
                frameNinja = 0

        if posicaoXN <= -1100:
            qtdDeslocamentos = qtdDeslocamentos + 1
            direcaoDeslocamento = direcaoDeslocamento * -1

        if posicaoXN >= 60:
            qtdDeslocamentos = qtdDeslocamentos + 1
            direcaoDeslocamento = direcaoDeslocamento * -1

    if(direcaoDeslocamento == -1):
        matrizN_e = multiplica_matrizes(translacao(1160,0), multiplica_matrizes(escala(-1,1), translacao(-1160,0)))
        matrizS_e = multiplica_matrizes(translacao(160,0), multiplica_matrizes(escala(-1,1), translacao(-160,0)))
    if (direcaoDeslocamento == 1):
        matrizS_e = identidade()
        matrizN_e = identidade()

    matrizS_a = translacao(posicaoXS, posicaoYS)
    matrizS_r = multiplica_matrizes(translacao(160, 465), multiplica_matrizes(rotacao(anguloSamurai), translacao(-160,-465)))
    matrizN_a = translacao(posicaoXN, 0)
    matrizN_f = multiplica_matrizes(translacao(1160,599),multiplica_matrizes(escala(0.8,0.8), translacao(-1160,-599)))

    matrizS = multiplica_matrizes(matrizS_a, multiplica_matrizes(matrizS_e , matrizS_r))
    matrizN = multiplica_matrizes(matrizN_a, multiplica_matrizes(matrizN_e, matrizN_f))

    pontosSamurai = desenhar_samurai(tela, matrizS, frameSamurai)
    pontosNinja = desenhar_ninja(tela, matrizN, frameNinja)
    aabbSamurai = calcular_aabb(pontosSamurai)
    aabbNinja = calcular_aabb(pontosNinja)

    restaurar_sobreposicao_viewport(
        tela,
        aabbSamurai,
        cenarioViewportFracionado
    )

    restaurar_sobreposicao_viewport(
        tela,
        aabbNinja,
        cenarioViewportFracionado
    )

    restaurar_viewport( 
        tela, 
        aabbSamuraiViewportAntes, 
        cenarioViewportFracionado 
    ) 
 
    restaurar_viewport( 
        tela, 
        aabbNinjaViewportAntes, 
        cenarioViewportFracionado 
    )

    aabbNinjaAntes = aabbNinja
    aabbSamuraiAntes = aabbSamurai

    colisao = colisao_aabb(aabbNinja, aabbSamurai)
    

    matrizS_viewport = multiplica_matrizes(
        matrizMinimapa,
        matrizS
    )


    matrizN_viewport = multiplica_matrizes(
        matrizMinimapa,
        matrizN
    )


    definir_clip(viewport)


    pontosSamuraiViewport = desenhar_samurai(
        tela,
        matrizS_viewport,
        frameSamurai
    )


    pontosNinjaViewport = desenhar_ninja(
        tela,
        matrizN_viewport,
        frameNinja
    )


    remover_clip()

    aabbSamuraiViewportAntes = calcular_aabb(
    pontosSamuraiViewport
    )

    aabbNinjaViewportAntes = calcular_aabb(
    pontosNinjaViewport
    )

    desenhar_viewport(
        tela,
        viewport
    )

    if colisao and vuneravel:
        vidas = vidas - 1
        vuneravel = False
        print("Bateu!!")

    if not colisao:
        vuneravel = True

    desenhar_vidas(tela, vidas, cenarioFracionado)

    if vidas >= 1:
        preencher_circulo(tela, 50, 50, 25, VERMELHO)

    if vidas >= 2:
        preencher_circulo(tela, 110, 50, 25, VERMELHO)

    if vidas >= 3:
        preencher_circulo(tela, 170, 50, 25, VERMELHO)

    if vidas <= 0:
        estadoJogo1 = "derrota"

    if qtdDeslocamentos >= limDeslocamentos:
        estadoJogo1 = "vitoria"

#======================================================
#            BLOCO 40: JOGAR NÍVEL II
#======================================================
def fase2(tela):
    global velocidadeXS
    global velocidadeXN

    velocidadeXS = velocidadeXS2
    velocidadeXN = velocidadeXN2

    fase1(tela)

#======================================================
#            BLOCO 41: DESENHAR VIDAS
#======================================================

def desenhar_vidas(tela, vidas, cenarioFracionado):
    global vidas_anterior
    
    if vidas == vidas_anterior:
        return
        
    if cenarioFracionado is None:
        return

    for x in range(25, 196):
        for y in range(25, 76):
            setPixel(tela, x, y, cenarioFracionado[y][x])
        
    if vidas >= 1:
        preencher_circulo(tela, 50, 50, 25, VERMELHO)
    if vidas >= 2:
        preencher_circulo(tela, 110, 50, 25, VERMELHO)
    if vidas >= 3:
        preencher_circulo(tela, 170, 50, 25, VERMELHO)

    vidas_anterior = vidas

#======================================================
#            BLOCO 42: TELA DERROTA
#======================================================

def desenhar_tela_derrota(tela):
    fonte3 = pygame.font.SysFont("Georgia", 40, bold=True)
    fonte4 = pygame.font.SysFont("Georgia", 20, bold=True)
    desenhar_fase1(tela)
    b2 = fonte3.render("VOCÊ PERDEU!", True, (0,0,0)) 
    x2_centro = 640 - (b2.get_width() // 2) 
    y2_centro = 280 - (b2.get_height() // 2) 
    tela.blit(b2, (x2_centro, y2_centro)) 
    b3 = fonte4.render("Aperte Esc para voltar ao menu", True, (255, 255, 255))
    x3_centro = 640 - (b3.get_width() // 2)
    y3_centro = 720 - (b3.get_width() // 2)
    tela.blit(b3, (x3_centro, y3_centro))

#======================================================
#            BLOCO 43: TELA VITÓRIA
#======================================================
    
def desenhar_tela_vitoria(tela):
    fonte3 = pygame.font.SysFont("Georgia", 40, bold=True)
    fonte4 = pygame.font.SysFont("Georgia", 20, bold=True)
    desenhar_fase1(tela)
    b2 = fonte3.render("VOCÊ GANHOU!", True, (0,0,0)) 
    x2_centro = 640 - (b2.get_width() // 2) 
    y2_centro = 280 - (b2.get_height() // 2) 
    tela.blit(b2, (x2_centro, y2_centro)) 
    b3 = fonte4.render("Aperte Esc para voltar ao menu", True, (255, 255, 255))
    x3_centro = 640 - (b3.get_width() // 2)
    y3_centro = 720 - (b3.get_width() // 2)
    tela.blit(b3, (x3_centro, y3_centro))

#======================================================
#            BLOCO 44: CENÁRIO NÍVEL I
#======================================================
def desenhar_fase1(tela):

    tela.fill((173, 216, 230))


    montanha_esquerda = [
        (0, 600),
        (0, 430),
        (150, 300),
        (300, 440),
        (420, 600)
    ]

    scanline_fill(
        tela,
        montanha_esquerda,
        (95, 120, 105)
    )

    desenhar_poligono(
        tela,
        montanha_esquerda,
        (65, 85, 70)
    )


    montanha_centro = [
        (250, 600),
        (420, 400),
        (600, 250),
        (790, 420),
        (930, 600)
    ]

    scanline_fill(
        tela,
        montanha_centro,
        (110, 135, 115)
    )

    desenhar_poligono(
        tela,
        montanha_centro,
        (70, 90, 75)
    )


    montanha_direita = [
        (720, 600),
        (900, 420),
        (1050, 320),
        (1280, 470),
        (1280, 600)
    ]

    scanline_fill(
        tela,
        montanha_direita,
        (90, 115, 100)
    )

    desenhar_poligono(
        tela,
        montanha_direita,
        (60, 80, 65)
    )


    sol = [
        (1040, 100),
        (1070, 110),
        (1090, 135),
        (1090, 165),
        (1070, 190),
        (1040, 200),
        (1010, 190),
        (990, 165),
        (990, 135),
        (1010, 110)
    ]

    scanline_fill(
        tela,
        sol,
        (245, 190, 70)
    )

    desenhar_poligono(
        tela,
        sol,
        (210, 140, 40)
    )


    coluna_esquerda = [
        (865, 410),
        (890, 410),
        (890, 600),
        (865, 600)
    ]

    scanline_fill(
        tela,
        coluna_esquerda,
        (170, 35, 35)
    )

    desenhar_poligono(
        tela,
        coluna_esquerda,
        (70, 20, 20)
    )

    coluna_direita = [
        (1010, 410),
        (1035, 410),
        (1035, 600),
        (1010, 600)
    ]

    scanline_fill(
        tela,
        coluna_direita,
        (170, 35, 35)
    )

    desenhar_poligono(
        tela,
        coluna_direita,
        (70, 20, 20)
    )

    barra_central = [
        (840, 420),
        (1060, 420),
        (1060, 445),
        (840, 445)
    ]

    scanline_fill(
        tela,
        barra_central,
        (180, 40, 40)
    )

    desenhar_poligono(
        tela,
        barra_central,
        (70, 20, 20)
    )

    teto_torii = [
        (810, 385),
        (1090, 385),
        (1060, 415),
        (840, 415)
    ]

    scanline_fill(
        tela,
        teto_torii,
        (190, 45, 45)
    )

    desenhar_poligono(
        tela,
        teto_torii,
        (70, 20, 20)
    )

    arbusto_esquerdo = [
        (30, 600),
        (60, 555),
        (100, 570),
        (135, 540),
        (170, 570),
        (210, 600)
    ]

    scanline_fill(
        tela,
        arbusto_esquerdo,
        (45, 100, 55)
    )

    desenhar_poligono(
        tela,
        arbusto_esquerdo,
        (30, 70, 40)
    )


    arbusto_direito = [
        (1080, 600),
        (1110, 565),
        (1150, 575),
        (1190, 545),
        (1230, 570),
        (1280, 600)
    ]

    scanline_fill(
        tela,
        arbusto_direito,
        (45, 100, 55)
    )

    desenhar_poligono(
        tela,
        arbusto_direito,
        (30, 70, 40)
    )


    pontos_chao = [
        (0, 720),
        (1280, 720),
        (1280, 600),
        (0, 600)
    ]

    scanline_fill(
        tela,
        pontos_chao,
        (75, 120, 65)
    )
#======================================================
#            BLOCO 45: RENICIAR NÍVEL I
#======================================================

def reiniciar_fase1():
    global posicaoXS
    global posicaoYS
    global velocidadeYS
    global chao
    global posicaoXN
    
    global qtdDeslocamentos
    global direcaoDeslocamento
    
    global vidas
    global vuneravel
    
    global estadoJogo1

    global cenario
    global cenarioFracionado
    global aabbSamuraiAntes
    global aabbNinjaAntes

    global frameSamurai
    global contadorAnimacaoSamurai
    global frameNinja
    global contadorAnimacaoNinja

    global cenarioViewport
    global cenarioViewportFracionado

    global aabbSamuraiViewportAntes
    global aabbNinjaViewportAntes

    global matrizMinimapa

    global vidas_anterior

    global velocidadeXS
    global velocidadeXN

    posicaoXS = 0
    posicaoYS = 0
    velocidadeYS = 0
    chao = True
    posicaoXN = 0

    qtdDeslocamentos = 0
    direcaoDeslocamento = 1

    vidas = 3
    vuneravel = True

    estadoJogo1 = "jogando"

    cenario = False
    cenarioFracionado = None
    aabbNinjaAntes = None
    aabbSamuraiAntes = None

    frameSamurai = 0
    contadorAnimacaoSamurai = 0
    frameNinja = 0
    contadorAnimacaoNinja = 0

    cenarioViewport = False

    cenarioViewportFracionado = None

    aabbSamuraiViewportAntes = None
    aabbNinjaViewportAntes = None

    matrizMinimapa = None

    vidas_anterior = -1

    velocidadeXS = velocidadeXS1
    velocidadeXN = velocidadeXN1

#======================================================
#            BLOCO 46: FUNÇÕES AUXILIARES
#======================================================

def salvar_viewport(tela):

    pixels = []

    for y in range(50, 250):

        linha = []

        for x in range(950, 1250):

            linha.append(
                tela.get_at((x, y))
            )

        pixels.append(linha)

    return pixels

def restaurar_viewport(tela, aabb, Pixels):

    if aabb is None:
        return

    if Pixels is None:
        return

    x1, y1, x2, y2 = aabb

    margem = 10

    x1 = max(
        950,
        int(x1 - margem)
    )

    x2 = min(
        1249,
        int(x2 + margem)
    )

    y1 = max(
        50,
        int(y1 - margem)
    )

    y2 = min(
        249,
        int(y2 + margem)
    )

    for y in range(y1, y2 + 1):

        for x in range(x1, x2 + 1):

            setPixel(
                tela,
                x,
                y,
                Pixels[y - 50][x - 950]
            )

def restaurar_cenario(tela, aabb, Pixels):

    if aabb is None:
        return

    if Pixels is None:
        return
    
    x1, y1, x2, y2 = aabb

    margem = 10

    x1 = max(0, int(x1 - margem))
    x2 = min(1279, int(x2 + margem))
    y1 = max(0, int(y1 - margem))
    y2 = min(719, int(y2 + margem))

    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):

            if 950 <= x <= 1249 and 50 <= y <= 249:
                continue

            setPixel(tela, x, y, Pixels[y][x])

def salvar_cenario(tela):

    pixels = []

    for y in range(altura):
        linha = []

        for x in range(largura):
            linha.append(tela.get_at((x, y)))

        pixels.append(linha)

    return pixels

def desenhar_cenario_viewport(tela, matrizViewport):

    ceu = [
        (0, 0),
        (1280, 0),
        (1280, 720),
        (0, 720)
    ]

    pontos = aplica_transformacao(
        matrizViewport,
        ceu
    )

    scanline_fill(
        tela,
        pontos,
        (173, 216, 230)
    )

    montanha_esquerda = [
        (0, 600),
        (0, 430),
        (150, 300),
        (300, 440),
        (420, 600)
    ]

    pontos = aplica_transformacao(
        matrizViewport,
        montanha_esquerda
    )

    scanline_fill(
        tela,
        pontos,
        (95, 120, 105)
    )

    desenhar_poligono(
        tela,
        pontos,
        (65, 85, 70)
    )

    montanha_centro = [
        (250, 600),
        (420, 400),
        (600, 250),
        (790, 420),
        (930, 600)
    ]

    pontos = aplica_transformacao(
        matrizViewport,
        montanha_centro
    )

    scanline_fill(
        tela,
        pontos,
        (110, 135, 115)
    )

    desenhar_poligono(
        tela,
        pontos,
        (70, 90, 75)
    )

    montanha_direita = [
        (720, 600),
        (900, 420),
        (1050, 320),
        (1280, 470),
        (1280, 600)
    ]

    pontos = aplica_transformacao(
        matrizViewport,
        montanha_direita
    )

    scanline_fill(
        tela,
        pontos,
        (90, 115, 100)
    )

    desenhar_poligono(
        tela,
        pontos,
        (60, 80, 65)
    )

    sol = [
        (1040, 100),
        (1070, 110),
        (1090, 135),
        (1090, 165),
        (1070, 190),
        (1040, 200),
        (1010, 190),
        (990, 165),
        (990, 135),
        (1010, 110)
    ]

    pontos = aplica_transformacao(
        matrizViewport,
        sol
    )

    scanline_fill(
        tela,
        pontos,
        (245, 190, 70)
    )

    desenhar_poligono(
        tela,
        pontos,
        (210, 140, 40)
    )

    coluna_esquerda = [
        (865, 410),
        (890, 410),
        (890, 600),
        (865, 600)
    ]

    pontos = aplica_transformacao(
        matrizViewport,
        coluna_esquerda
    )

    scanline_fill(
        tela,
        pontos,
        (170, 35, 35)
    )

    desenhar_poligono(
        tela,
        pontos,
        (70, 20, 20)
    )

    coluna_direita = [
        (1010, 410),
        (1035, 410),
        (1035, 600),
        (1010, 600)
    ]

    pontos = aplica_transformacao(
        matrizViewport,
        coluna_direita
    )

    scanline_fill(
        tela,
        pontos,
        (170, 35, 35)
    )

    desenhar_poligono(
        tela,
        pontos,
        (70, 20, 20)
    )

    barra_central = [
        (840, 420),
        (1060, 420),
        (1060, 445),
        (840, 445)
    ]

    pontos = aplica_transformacao(
        matrizViewport,
        barra_central
    )

    scanline_fill(
        tela,
        pontos,
        (180, 40, 40)
    )

    desenhar_poligono(
        tela,
        pontos,
        (70, 20, 20)
    )

    teto_torii = [
        (810, 385),
        (1090, 385),
        (1060, 415),
        (840, 415)
    ]

    pontos = aplica_transformacao(
        matrizViewport,
        teto_torii
    )

    scanline_fill(
        tela,
        pontos,
        (190, 45, 45)
    )

    desenhar_poligono(
        tela,
        pontos,
        (70, 20, 20)
    )

    chao = [
        (0, 720),
        (1280, 720),
        (1280, 600),
        (0, 600)
    ]

    pontos = aplica_transformacao(
        matrizViewport,
        chao
    )

    scanline_fill(
        tela,
        pontos,
        (75, 120, 65)
    )

#======================================================
#            BLOCO 47: RENICIAR NÍVEL II
#======================================================

def reiniciar_fase2():
    global velocidadeXS
    global velocidadeXN

    reiniciar_fase1()
    velocidadeXS = velocidadeXS2
    velocidadeXN = velocidadeXN2