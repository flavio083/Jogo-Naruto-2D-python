
import pygame
import random
import sys
from time import sleep
import sqlite3


pygame.init()


WIDTH, HEIGHT = 1280, 720
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Naruto - Jogo de Luta")

#cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (50, 50, 255)
GRAY = (220, 220, 220)
YELLOW = (255, 255, 0)


# Conexão com o banco de dados
conn = sqlite3.connect("ranking_naruto.db")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS ranking (
    jogador TEXT PRIMARY KEY,
    vitorias INTEGER DEFAULT 0,
    derrotas INTEGER DEFAULT 0,
    pontos INTEGER DEFAULT 0
)
''')
conn.commit()


def registrar_resultado(vencedor, perdedor, dificuldade):
    pontos_vencedor = 0
    if dificuldade == 1:  # Fácil
        pontos_vencedor = 10
    elif dificuldade == 2:  # Médio
        pontos_vencedor = 13
    elif dificuldade == 3:  # Difícil
        pontos_vencedor = 15
   
    # Atualiza o vencedor
    cursor.execute("SELECT vitorias FROM ranking WHERE jogador = ?", (vencedor,))
    resultado = cursor.fetchone()
   
    if resultado:
        cursor.execute("UPDATE ranking SET vitorias = vitorias + 1, pontos = pontos + ? WHERE jogador = ?",
                      (pontos_vencedor, vencedor))
    else:
        cursor.execute("INSERT INTO ranking (jogador, vitorias, pontos) VALUES (?, 1, ?)",
                      (vencedor, pontos_vencedor))
   
    # Atualiza o perdedor (5 pontos independente da dificuldade)
    cursor.execute("SELECT derrotas FROM ranking WHERE jogador = ?", (perdedor,))
    resultado = cursor.fetchone()
   
    if resultado:
        cursor.execute("UPDATE ranking SET derrotas = derrotas + 1, pontos = pontos + 5 WHERE jogador = ?",
                      (perdedor,))
    else:
        cursor.execute("INSERT INTO ranking (jogador, derrotas, pontos) VALUES (?, 1, 5)",
                      (perdedor,))
   
    conn.commit()


def mostrar_ranking_tela():
    win.fill(BLACK)
    desenhar_texto("RANKING DE PONTOS", WIDTH//2 - 215, 50, YELLOW, font_grande)
   
    cursor.execute("SELECT jogador, vitorias, derrotas, pontos FROM ranking ORDER BY pontos DESC LIMIT 10")
    resultados = cursor.fetchall()
   
    if not resultados:
        desenhar_texto("Nenhum jogador registrado ainda", WIDTH//2 - 200, 150, WHITE, font_media)
    else:
        for i, (jogador, vitorias, derrotas, pontos) in enumerate(resultados, 1):
            texto = f"{i}. {jogador} - {pontos} pts (V: {vitorias} | D: {derrotas})"
            desenhar_texto(texto, WIDTH//2 - 250, 150 + i*50, WHITE, font_media)
   
    desenhar_texto("Pressione qualquer tecla para continuar...", WIDTH//2 - 250, HEIGHT - 100, WHITE, font_media)
    pygame.display.update()
   
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                esperando = False


# Fontes
font_pequena = pygame.font.Font("fontes/njnaruto.ttf", 18)
font_media = pygame.font.Font("fontes/njnaruto.ttf", 24)
font_grande = pygame.font.Font("fontes/njnaruto.ttf", 48)


def desenhar_texto(texto, x, y, cor=BLACK, fonte=font_pequena):
    render = fonte.render(texto, True, cor)
    win.blit(render, (x, y))


def obter_nome_jogador():
    nome = ""
    input_ativo = True
    clock = pygame.time.Clock()
   
    while input_ativo:
        win.fill(BLACK)
        desenhar_texto("Digite seu nome e pressione ENTER:", WIDTH//2 - 425, HEIGHT//2 - 50, WHITE, font_grande)
        desenhar_texto(nome, WIDTH//2 - 220, HEIGHT//2 + 20, WHITE, font_grande)
        pygame.display.update()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if nome.strip() != "":
                        input_ativo = False
                elif event.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]
                else:
                    if len(nome) < 15:  # Limite de caracteres
                        nome += event.unicode
       
        clock.tick(30)
   
    return nome.strip()


carregamento = pygame.image.load("fundo/carregamento.jpg")
carregamento = pygame.transform.scale(carregamento, (WIDTH, HEIGHT))


# Variáveis de jogo
nome_jogador = ""
dificuldade = 0
vida_pc = 100
dificuldade_max = 100
dificuldade_escolhida = False
vida_usuario = 100
usuario = ''
computador = ''
personagens = ['NARUTO', 'SASUKE', 'KAKASHI', 'TOBIRAMA']
fase = "nome_jogador"  


# Ataques 
ataques_dict = {
    "NARUTO": ["RASENGAN", "CLONES", "PALMA", "MIL ANOS", "REGENERA"],
    "SASUKE": ["CHIDORI", "BOLA DE FOGO", "AMATERASU", "COMBO DO LEAO", "REGENERA"],
    "KAKASHI": ["CHIDORI", "RASENGAN", "KAMUI", "RAIKIRI", "REGENERA"],
    "TOBIRAMA": ["COMBO DO LEAO", "RAIJIN", "DRAGAO", "TSUNAMI", "REGENERA"]
}


ataques_dano = {
    "RASENGAN": 30, "CLONES": 15, "PALMA": 25, "MIL ANOS": 10,
    "CHIDORI": 25, "BOLA DE FOGO": 20, "AMATERASU": 30, "COMBO DO LEAO": 15,
    "KAMUI": 25, "RAIKIRI": 20, "RAIJIN": 25, "DRAGAO": 30, "TSUNAMI": 25,
    "REGENERA": -20
}


mensagem = ""


# Sons 
pygame.mixer.music.load("audio/musicabatalha.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)


somrasengan = pygame.mixer.Sound("audio/somrasengan.mp3"); somrasengan.set_volume(0.15)
somchidori = pygame.mixer.Sound("audio/somchidori.mp3"); somchidori.set_volume(0.15)
somboladefogo = pygame.mixer.Sound("audio/somboladefogo.mp3"); somboladefogo.set_volume(0.15)
somamaterasu = pygame.mixer.Sound("audio/somamaterasu.mp3"); somamaterasu.set_volume(0.2)
somcombodoleao = pygame.mixer.Sound("audio/somcombodoleao.MP3"); somcombodoleao.set_volume(0.15)
somclones = pygame.mixer.Sound("audio/somclones.mp3"); somclones.set_volume(0.15)
sommilanosdemorte = pygame.mixer.Sound("audio/sommilanosdemorte.MP3"); sommilanosdemorte.set_volume(0.3)
sompalma = pygame.mixer.Sound("audio/sompalma.MP3"); sompalma.set_volume(0.15)
somregenera = pygame.mixer.Sound("audio/somregenera.mp3"); somregenera.set_volume(1)
somkamui = pygame.mixer.Sound("audio/somkamui.mp3"); somkamui.set_volume(0.15)
somraikiri = pygame.mixer.Sound("audio/somraikiri.mp3"); somraikiri.set_volume(0.15)
somraijin = pygame.mixer.Sound("audio/somraijin.MP3"); somraijin.set_volume(0.15)
somdragao = pygame.mixer.Sound("audio/somdragao.mp3"); somdragao.set_volume(0.15)
somtsunami = pygame.mixer.Sound("audio/somtsunami.mp3"); somtsunami.set_volume(0.15)


# Imagens 
background = pygame.image.load("fundo/fundo.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
sprite_usuario = None
sprite_pc = None


angulo_usuario = 90
angulo_pc = -90


frame_count = 0
letra_index = 0
ultima_mensagem = ""


def carregar_sprite(nome, lado='esquerdo'):
    caminho = f"sprites/{nome.lower()}.png"
    sprite = pygame.image.load(caminho).convert_alpha()
    sprite = pygame.transform.scale(sprite, (240, 240))
    if lado == 'direito':
        sprite = pygame.transform.flip(sprite, True, False)
    return sprite


def atacar(jogador, alvo, ataque):
    global vida_usuario, vida_pc, mensagem
    dano = ataques_dano.get(ataque, 0)
    if ataque == "REGENERA":
        if jogador == "usuario":
            trocar_sprite_dano("usuario", tipo="cura")
            vida_usuario = min(100, vida_usuario - dano)
        else:
            trocar_sprite_dano("pc", tipo="cura")
            vida_pc = min(dificuldade_max, vida_pc - dano)
        mensagem = f"{nome_jogador if jogador == 'usuario' else computador} se regenerou ({abs(dano)} de vida)!"
    else:
        if alvo == "pc":
            vida_pc = max(0, vida_pc - dano)          
        else:
            vida_usuario = max(0, vida_usuario - dano)
        mensagem = f"{nome_jogador if jogador == 'usuario' else computador} usou {ataque} causando {dano} de dano!"


def desenhar_texto_animado(texto, x, y, cor=BLACK, fonte=font_grande):
    global letra_index, ultima_mensagem
    if texto != ultima_mensagem:
        letra_index = 0
        ultima_mensagem = texto
    letra_index = min(letra_index + 1, len(texto))
    render = fonte.render(texto[:letra_index], True, cor)
    win.blit(render, (x, y))


def desenhar_luta():
    win.blit(background, (0, 0))
    if vida_usuario > 0:
        win.blit(sprite_usuario, (100, 400))
    if vida_pc > 0:
        win.blit(sprite_pc, (WIDTH - 340, 400))
    pygame.draw.rect(win, RED, (100, 90, 300, 30))
    pygame.draw.rect(win, GREEN, (100, 90, max(0, 300 * (vida_usuario / 100)), 30))
    desenhar_texto(f"Vida: {vida_usuario}/100", 100, 65, fonte=font_pequena)
    pygame.draw.rect(win, RED, (WIDTH - 400, 90, 300, 30))
    pygame.draw.rect(win, GREEN, (WIDTH - 400, 90, max(0, 300 * (vida_pc / dificuldade_max)), 30))
    desenhar_texto(f"Vida: {vida_pc}/{dificuldade_max}", WIDTH - 400, 65, fonte=font_pequena)


def atualizar_barras():
    pygame.draw.rect(win, RED, (100, 90, 300, 30))
    pygame.draw.rect(win, GREEN, (100, 90, max(0, 300 * (vida_usuario / 100)), 30))
    desenhar_texto(f"Vida: {vida_usuario}/100", 100, 65, fonte=font_pequena)
    pygame.draw.rect(win, RED, (WIDTH - 400, 90, 300, 30))
    pygame.draw.rect(win, GREEN, (WIDTH - 400, 90, max(0, 300 * (vida_pc / dificuldade_max)), 30))
    desenhar_texto(f"Vida: {vida_pc}/{dificuldade_max}", WIDTH - 400, 65, fonte=font_pequena)


def trocar_sprite_dano(jogador, tipo='dano'):
    global sprite_usuario, sprite_pc


    if jogador == "usuario":
        if tipo == 'cura':
            sprite_usuario = carregar_sprite(usuario.lower() + "cura")
        else:
            if vida_usuario <= 0: return
            sprite_usuario = carregar_sprite(usuario.lower() + "dano")


        desenhar_luta()
        desenhar_texto(f"{usuario} ({nome_jogador})", 100, 35, fonte=font_media)
        desenhar_texto(f"{computador} (PC)", WIDTH - 400, 35, fonte=font_media)
        desenhar_texto(mensagem, 50, 200, fonte=font_pequena)
        pygame.display.update()
        pygame.time.delay(1000)
        sprite_usuario = carregar_sprite(usuario)


    else:
        if tipo == 'cura':
            sprite_pc = carregar_sprite(computador.lower() + "cura")
            sprite_pc = pygame.transform.flip(sprite_pc, True, False)
        else:
            if vida_pc <= 0: return
            sprite_pc = carregar_sprite(computador.lower() + "dano", lado='direito')


        desenhar_luta()
        desenhar_texto(f"{usuario} ({nome_jogador})", 100, 35, fonte=font_media)
        desenhar_texto(f"{computador} (PC)", WIDTH - 400, 35, fonte=font_media)
        desenhar_texto(mensagem, 50, 200, fonte=font_pequena)
        pygame.display.update()
        pygame.time.delay(1000)
        sprite_pc = carregar_sprite(computador, lado='direito')


def animar_ataque(origem, destino, ataque, lado):
    passos = 20
    imagem = pygame.image.load(f"ataques/{ataque.lower().replace(' ', '')}.png").convert_alpha()
    imagem = pygame.transform.scale(imagem, (80, 80))
    if lado == 'pc':
        imagem = pygame.transform.flip(imagem, True, False)


    for i in range(passos):
        t = i / passos
        x = int(origem[0] * (1 - t) + destino[0] * t)
        y = int(origem[1] * (1 - t) + destino[1] * t)
        desenhar_luta()
        desenhar_texto(f"{usuario} ({nome_jogador})", 100, 35, fonte=font_media)
        desenhar_texto(f"{computador} (PC)", WIDTH - 400, 35, fonte=font_media)
        desenhar_texto(mensagem, 50, 200, fonte=font_pequena)
        win.blit(imagem, (x, y))
        pygame.display.update()
        pygame.time.delay(35)
    if ataque != "REGENERA":
        trocar_sprite_dano('usuario' if lado == 'pc' else 'pc')


    passos = 20
    for i in range(passos):
        t = i / passos
        x = int(origem[0] * (1 - t) + destino[0] * t)
        y = int(origem[1] * (1 - t) + destino[1] * t)
        desenhar_luta()
        desenhar_texto(f"{usuario} ({nome_jogador})", 100, 35, fonte=font_media)
        desenhar_texto(f"{computador} (PC)", WIDTH - 400, 35, fonte=font_media)
        desenhar_texto(mensagem, 50, 200, fonte=font_pequena)
        pygame.display.update()
        pygame.time.delay(35)


def desenhar_botoes(ataques):
    botao_rects.clear()
    for i, ataque in enumerate(ataques):
        rect = pygame.Rect(600, 70 + i*40, 200, 30)
        pygame.draw.rect(win, GRAY, rect)
        desenhar_texto(ataque, 610, 75 + i*40, fonte=font_pequena)
        botao_rects.append((rect, ataque))


running = True


def reiniciar_ou_sair():
    texto_reiniciar = font_media.render("Reiniciar", True, (255, 255, 255))
    texto_sair = font_media.render("Sair", True, (255, 255, 255))


    pos_reiniciar = texto_reiniciar.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    pos_sair = texto_sair.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))


    while True:
        win.fill((0, 0, 0))
        win.blit(texto_reiniciar, pos_reiniciar)
        win.blit(texto_sair, pos_sair)
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos_reiniciar.collidepoint(event.pos):
                    return 'reiniciar'
                elif pos_sair.collidepoint(event.pos):
                    return 'sair'


clock = pygame.time.Clock()
turno = "usuario"
botao_rects = []


while running:
    clock.tick(60)
    frame_count += 1
    win.blit(carregamento, (0, 0))


    if fase == "nome_jogador":
        nome_jogador = obter_nome_jogador()
        fase = "dificuldade"
   
    elif fase == "dificuldade":
        win.blit(carregamento, (0, 0))
        desenhar_texto(f"Bem-vindo, {nome_jogador}!", 50, 50, fonte=font_grande)
        desenhar_texto("Selecione o nivel de dificuldade:", 50, 120, fonte=font_media)
        desenhar_texto("[1] FACIL", 50, 170, fonte=font_media)
        desenhar_texto("[2] MEDIO", 50, 220, fonte=font_media)
        desenhar_texto("[3] DIFICIL", 50, 270, fonte=font_media)
        pygame.display.update()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    vida_pc = 75
                    dificuldade_max = 75
                    dificuldade = 1
                    dificuldade_escolhida = True
                    fase = "escolha"
                elif event.key == pygame.K_2:
                    vida_pc = 100
                    dificuldade_max = 100
                    dificuldade = 2
                    dificuldade_escolhida = True
                    fase = "escolha"
                elif event.key == pygame.K_3:
                    vida_pc = 125
                    dificuldade_max = 125
                    dificuldade = 3
                    dificuldade_escolhida = True
                    fase = "escolha"


    elif fase == "escolha":
        desenhar_texto(f"{nome_jogador}, escolha seu personagem:", 50, 50, fonte=font_grande)
        for i, p in enumerate(personagens):
            desenhar_texto(f"[{i+1}] {p}", 50, 125 + i*40, fonte=font_media)
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
                mensagem = f"{nome_jogador} escolheu {usuario}.\nComputador escolheu {computador}."


    elif fase == "batalha":
        desenhar_luta()
        desenhar_texto(f"{usuario} ({nome_jogador})", 100, 40, fonte=font_media)
        desenhar_texto(f"{computador} (PC)", WIDTH - 400, 40, fonte=font_media)
        desenhar_texto(mensagem, 50, 200, fonte=font_pequena)


        if vida_pc <= 0:
            desenhar_texto(f"Parabens {nome_jogador}! Voce venceu!", 310, 330, BLUE, fonte=font_grande)
            pc_derrotado = pygame.transform.rotate(sprite_pc, angulo_pc)
            win.blit(pc_derrotado, (WIDTH - 290, 500))
            registrar_resultado(nome_jogador, computador, dificuldade)
            pygame.display.update()
            pygame.time.delay(3000)
            mostrar_ranking_tela()
            resultado = reiniciar_ou_sair()
            if resultado == 'reiniciar':
                vida_usuario = 100
                vida_pc = 100
                dificuldade_max = 100
                dificuldade_escolhida = False
                usuario = ''
                computador = ''
                personagens = ['NARUTO', 'SASUKE', 'KAKASHI', 'TOBIRAMA']
                fase = "dificuldade"
                mensagem = ""
                turno = "usuario"
                continue
            else:
                running = False
        elif vida_usuario <= 0:
            desenhar_texto(f"{nome_jogador} perdeu! Fim de jogo!", 310, 330, RED, fonte=font_grande)
            usuario_derrotado = pygame.transform.rotate(sprite_usuario, angulo_usuario)
            win.blit(usuario_derrotado, (50, 500))
            registrar_resultado(computador, nome_jogador, dificuldade)
            pygame.display.update()
            pygame.time.delay(3000)
            mostrar_ranking_tela()
            resultado = reiniciar_ou_sair()
            if resultado == 'reiniciar':
                vida_usuario = 100
                vida_pc = 100
                dificuldade_max = 100
                dificuldade_escolhida = False
                usuario = ''
                computador = ''
                personagens = ['NARUTO', 'SASUKE', 'KAKASHI', 'TOBIRAMA']
                fase = "dificuldade"
                mensagem = ""
                turno = "usuario"
                continue
            else:
                running = False
        elif turno == "usuario":
            desenhar_texto(f"{nome_jogador}, escolha um ataque:", 600, 40, fonte=font_pequena)
            desenhar_botoes(ataques_dict[usuario])
        else:
            ataque_pc = random.choice(ataques_dict[computador])
            if ataque_pc == "REGENERA":
                trocar_sprite_dano("pc", tipo="cura")
                somregenera.play()
            elif ataque_pc == "RASENGAN": somrasengan.play()
            elif ataque_pc == "CHIDORI": somchidori.play()
            elif ataque_pc == "BOLA DE FOGO": somboladefogo.play()
            elif ataque_pc == "AMATERASU": somamaterasu.play()
            elif ataque_pc == "COMBO DO LEAO": somcombodoleao.play()
            elif ataque_pc == "CLONES": somclones.play()
            elif ataque_pc == "MIL ANOS": sommilanosdemorte.play()
            elif ataque_pc == "PALMA": sompalma.play()
            elif ataque_pc == "REGENERA":
                trocar_sprite_dano("pc", tipo="cura")
                somregenera.play()
            elif ataque_pc == "KAMUI": somkamui.play()
            elif ataque_pc == "RAIKIRI": somraikiri.play()
            elif ataque_pc == "RAIJIN": somraijin.play()
            elif ataque_pc == "DRAGAO": somdragao.play()
            elif ataque_pc == "TSUNAMI": somtsunami.play()
            animar_ataque((WIDTH - 250, 450), (220, 450), ataque_pc, 'pc')
            atacar("pc", "usuario", ataque_pc)
            atualizar_barras()
            pygame.display.update()
            turno = "usuario"
            pygame.time.delay(1000)


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if turno == "usuario" and event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for rect, ataque in botao_rects:
                    if rect.collidepoint(pos):
                        if ataque == "REGENERA":
                            trocar_sprite_dano("usuario", tipo="cura")
                            somregenera.play()
                            atacar("usuario", "pc", ataque)
                            atualizar_barras()
                            pygame.display.update()
                            while pygame.mixer.get_busy():
                                pygame.time.wait(100)
                            turno = "pc"
                            break
                        if ataque == "RASENGAN": somrasengan.play()
                        elif ataque == "CHIDORI": somchidori.play()
                        elif ataque == "BOLA DE FOGO": somboladefogo.play()
                        elif ataque == "AMATERASU": somamaterasu.play()
                        elif ataque == "COMBO DO LEAO": somcombodoleao.play()
                        elif ataque == "CLONES": somclones.play()
                        elif ataque == "MIL ANOS": sommilanosdemorte.play()
                        elif ataque == "PALMA": sompalma.play()
                        elif ataque == "REGENERA":
                            trocar_sprite_dano("usuario", tipo="cura")
                            somregenera.play()
                        elif ataque == "KAMUI": somkamui.play()
                        elif ataque == "RAIKIRI": somraikiri.play()
                        elif ataque == "RAIJIN": somraijin.play()
                        elif ataque == "DRAGAO": somdragao.play()
                        elif ataque == "TSUNAMI": somtsunami.play()
                        animar_ataque((220, 450), (WIDTH - 250, 450), ataque, 'usuario')
                        atacar("usuario", "pc", ataque)
                        atualizar_barras()
                        pygame.display.update()
                        while pygame.mixer.get_busy():
                            pygame.time.wait(100)
                        turno = "pc"
                        break


pygame.quit()
sys.exit()



