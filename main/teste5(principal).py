import pygame
import random
import sys
from time import sleep

pygame.init()

WIDTH, HEIGHT = 1280, 720
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Naruto - Jogo de Luta")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (50, 50, 255)
GRAY = (220, 220, 220)

font = pygame.font.SysFont('arial', 24)

vida_usuario = 100
vida_pc = 100
usuario = ''
computador = ''
personagens = ['NARUTO', 'SASUKE', 'KAKASHI', 'TOBIRAMA']
fase = "escolha"

ataques_dict = {
    "NARUTO": ["RASENGAN", "CLONES", "PALMA", "MIL ANOS", "REGENERA"],
    "SASUKE": ["CHIDORI", "BOLA DE FOGO", "AMATERASU", "COMBO DO LEAO", "REGENERA"],
    "KAKASHI": ["CHIDORI", "RASENGAN", "KAMUI", "RAIKIRI", "REGENERA"],
    "TOBIRAMA": ["CLONES", "RAIJIN", "DRAGAO", "TSUNAMI", "REGENERA"]
}

ataques_dano = {
    "RASENGAN": 30,
    "CLONES": 15,
    "PALMA": 25,
    "MIL ANOS": 10,
    "CHIDORI": 25,
    "BOLA DE FOGO": 20,
    "AMATERASU": 30,
    "COMBO DO LEAO": 15,
    "KAMUI": 25,
    "RAIKIRI": 20,
    "RAIJIN": 25,
    "DRAGAO": 30,
    "TSUNAMI": 25,
    "REGENERA": -20
}

mensagem = ""
# Sons
pygame.mixer.music.load("audio/musicabatalha.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)
somrasengan = pygame.mixer.Sound("audio/somrasengan.mp3")
somrasengan.set_volume(0.15)
somchidori = pygame.mixer.Sound("audio/somchidori.mp3")
somchidori.set_volume(0.15)
somboladefogo = pygame.mixer.Sound("audio/somboladefogo.mp3")
somboladefogo.set_volume(0.15)
somamaterasu = pygame.mixer.Sound("audio/somamaterasu.mp3")
somamaterasu.set_volume(0.2)
somcombodoleao = pygame.mixer.Sound("audio/somcombodoleao.MP3")
somcombodoleao.set_volume(0.15)
somclones = pygame.mixer.Sound("audio/somclones.mp3")
somclones.set_volume(0.15)
sommilanosdemorte = pygame.mixer.Sound("audio/sommilanosdemorte.MP3")
sommilanosdemorte.set_volume(0.3)
sompalma = pygame.mixer.Sound("audio/sompalma.MP3")
sompalma.set_volume(0.15)
somregenera = pygame.mixer.Sound("audio/somregenera.mp3")
somregenera.set_volume(1)
somkamui = pygame.mixer.Sound("audio/somkamui.mp3")
somkamui.set_volume(0.15)
somraikiri = pygame.mixer.Sound("audio/somraikiri.mp3")
somraikiri.set_volume(0.15)
somraijin = pygame.mixer.Sound("audio/somraijin.MP3")
somraijin.set_volume(0.15)
somdragao = pygame.mixer.Sound("audio/somdragao.mp3")
somdragao.set_volume(0.15)
somtsunami = pygame.mixer.Sound("audio/somtsunami.mp3")
somtsunami.set_volume(0.15)


# Carregar imagens (certifique-se de ter esses arquivos na pasta do jogo)
background = pygame.image.load("fundo/fundo.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
sprite_usuario = None
sprite_pc = None

angulo_usuario = 90
angulo_pc = -90

def carregar_sprite(nome, lado='esquerdo'):
    caminho = f"sprites/{nome.lower()}.png"
    sprite = pygame.image.load(caminho).convert_alpha()
    sprite = pygame.transform.scale(sprite, (240, 240))
    if lado == 'direito':
        sprite = pygame.transform.flip(sprite, True, False)
    return sprite

def desenhar_texto(texto, x, y, cor=BLACK):
    render = font.render(texto, True, cor)
    win.blit(render, (x, y))

def desenhar_luta():
    win.blit(background, (0, 0))

    # Desenhar personagens apenas se estiverem vivos
    if vida_usuario > 0:
        win.blit(sprite_usuario, (100, 400))
    if vida_pc > 0:
        win.blit(sprite_pc, (WIDTH - 340, 400))

    # Barras de vida
    pygame.draw.rect(win, RED, (100, 90, 300, 30))
    pygame.draw.rect(win, GREEN, (100, 90, max(0, 3 * vida_usuario), 30))

    pygame.draw.rect(win, RED, (WIDTH - 400, 90, 300, 30))
    pygame.draw.rect(win, GREEN, (WIDTH - 400, 90, max(0, 3 * vida_pc), 30))

def atacar(jogador, alvo, ataque):
    global vida_usuario, vida_pc, mensagem
    dano = ataques_dano.get(ataque, 0)
    if ataque == "REGENERA":
        if jogador == "usuario":
            vida_usuario = min(100, vida_usuario - dano)
        else:
            vida_pc = min(100, vida_pc - dano)
        mensagem = f"{'Você' if jogador == 'usuario' else computador} se regenerou ({abs(dano)} de vida)!"
    else:
        if alvo == "pc":
            vida_pc = max(0, vida_pc - dano)
        else:
            vida_usuario = max(0, vida_usuario - dano)
        mensagem = f"{'Você' if jogador == 'usuario' else computador} usou {ataque} causando {dano} de dano!"

botao_rects = []

def desenhar_botoes(ataques):
    botao_rects.clear()
    for i, ataque in enumerate(ataques):
        rect = pygame.Rect(600, 70 + i*40, 200, 30)
        pygame.draw.rect(win, GRAY, rect)
        desenhar_texto(ataque, 610, 75 + i*40)
        botao_rects.append((rect, ataque))

clock = pygame.time.Clock()
turno = "usuario"


carregamento = pygame.image.load("fundo/carregamento.jpg")
carregamento = pygame.transform.scale(carregamento, (WIDTH, HEIGHT))


running = True
while running:
    clock.tick(60)
    win.blit(carregamento, (0, 0))

    if fase == "escolha":
        desenhar_texto("Escolha seu personagem:", 50, 50)
        for i, p in enumerate(personagens):
            desenhar_texto(f"[{i+1}] {p}", 50, 100 + i*40)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.unicode in "1234":
                usuario = personagens[int(event.unicode)-1]
                personagens.remove(usuario)
                computador = random.choice(personagens)
                sprite_usuario = carregar_sprite(usuario)
                sprite_pc = carregar_sprite(computador, lado='direito')
                fase = "batalha"
                mensagem = f"Você escolheu {usuario}. Computador escolheu {computador}."

    elif fase == "batalha":
        desenhar_luta()
        desenhar_texto(f"{usuario} (Você)", 100, 50)
        desenhar_texto(f"{computador} (PC)", WIDTH - 400, 50)
        desenhar_texto(mensagem, 50, 200)

        if vida_pc <= 0:
            desenhar_texto("Parabéns! Você venceu!", 535, 350, BLUE)
            pc_derrotado = pygame.transform.rotate(sprite_pc, angulo_pc)
            win.blit(pc_derrotado, (WIDTH - 290, 450))
        elif vida_usuario <= 0:
            desenhar_texto("Você perdeu! Fim de jogo!", 535, 350, RED)
            usuario_derrotado = pygame.transform.rotate(sprite_usuario, angulo_usuario)
            win.blit(usuario_derrotado, (50, 450))
        elif turno == "usuario":
            desenhar_texto("Seu turno: escolha um ataque", 600, 40)
            desenhar_botoes(ataques_dict[usuario])
            if ataques_dano == "RASENGAN":
                somrasengan.play()
            sleep(1)
        else:
            ataque_pc = random.choice(ataques_dict[computador])
            atacar("pc", "usuario", ataque_pc)
            turno = "usuario"
            pygame.time.delay(1000)
            sleep(2)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if turno == "usuario" and event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for rect, ataque in botao_rects:
                    if rect.collidepoint(pos):
                        if ataque == "RASENGAN":
                            somrasengan.play()
                        elif ataque == "CHIDORI":
                            somchidori.play()
                        elif ataque == "BOLA DE FOGO":
                            somboladefogo.play()
                        elif ataque == "AMATERASU":
                            somamaterasu.play()
                        elif ataque == "COMBO DO LEAO":
                            somcombodoleao.play()
                        elif ataque == "CLONES":
                            somclones.play()
                        elif ataque == "MIL ANOS":
                            sommilanosdemorte.play()
                        elif ataque == "PALMA":
                            sompalma.play()
                        elif ataque == "REGENERA":
                            somregenera.play()
                        elif ataque == "KAMUI":
                            somkamui.play()
                        elif ataque == "RAIKIRI":
                            somraikiri.play()
                        elif ataque == "RAIJIN":
                            somraijin.play()
                        elif ataque == "DRAGAO":
                            somdragao.play()
                        elif ataque == "TSUNAMI":
                            somtsunami.play()
                        atacar("usuario", "pc", ataque)
                        turno = "pc"
                        break

pygame.quit()
sys.exit()