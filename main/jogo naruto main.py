import random
from time import sleep

# personagens
personagens = ['NARUTO', 'SASUKE', 'KAKASHI', 'TOBIRAMA']
forma = print('Escolha seu personagem, digite:\n[1] Para jogar com o NARUTO.\n[2] Para jogar com o SASUKE.\n[3] Para jogar com o KAKASHI.\n[4] Para jogar com o TOBIRAMA.')
usuario = input('')

vida_pc = 100
vida_usuario = 100

if usuario == '1':
    print(f'Seu personagem escolhido foi o NARUTO.')
    personagens.remove('NARUTO')
    usuario = 'NARUTO'
elif usuario == '2':
    print(f'Seu personagem escolhido foi o SASUKE.')
    personagens.remove('SASUKE')
    usuario = 'SASUKE'
elif usuario == '3':
    print(f'Seu personagem escolhido foi o KAKASHI.')
    personagens.remove('KAKASHI')
    usuario = 'KAKASHI'
elif usuario == '4':
    print(f'Seu personagem escolhido foi o TOBIRAMA.')
    personagens.remove('TOBIRAMA')
    usuario = 'TOBIRAMA'

computador = random.choice(personagens)
print(f'Agora o computador irá escolher um personagem para lhe enfrentar.')
print('Escolhendo...')
sleep (2)
print ('3')
sleep (1)
print('2')
sleep (1)
print('1')
sleep (1)
print(f'O personagem escolhido pelo computador foi o {computador}.')
sleep (1)
print(f'Batalha do dia: {usuario} vs {computador}!')
sleep (2)

# ataques do usuário
while vida_pc > 0 and vida_usuario > 0:
    if vida_pc <= 0 or vida_usuario <= 0:
        break
    if usuario == 'NARUTO':
        print('Escolha um ATAQUE, digite:\n[1] Para usar o RASENGAN.\n[2] Para usar os CLONES DA SOMBRA + TAIJUTSU.\n[3] Para usar a PALMA VENDAVAL.\n[4] Para usar o MIL ANOS DE MORTE.\n[5] Para se regenerar.')
        ataque = input('')
        if ataque == '1':
            print(f'NARUTO usou o RASENGAN.')
            sleep (1)
            if computador == 'SASUKE':
                vida_pc -= 20
                print(f'SASUKE sofreu com os ferimentos causados pelo RASENGAN, agora ele está com {vida_pc} de vida.')
            elif computador == 'KAKASHI':
                vida_pc -= 30
                print(f'KAKASHI sofreu com os ferimentos causados pelo RASENGAN, agora ele está com {vida_pc} de vida.')
            elif computador == 'TOBIRAMA':
                vida_pc -= 30
                print(f'TOBIRAMA sofreu com os ferimentos causados pelo RASENGAN, agora ele está com {vida_pc} de vida.')
        elif ataque == '2':
            print(f'NARUTO usou os CLONES DA SOMBRA + TAIJUTSU.')
            sleep (1)
            if computador == 'SASUKE':
                vida_pc -= 15
                print(f'SASUKE sofreu com os ferimentos causados pelos CLONES DA SOMBRA, agora ele está com {vida_pc} de vida.')
            elif computador == 'KAKASHI':
                vida_pc -= 15
                print(f'KAKASHI sofreu com os ferimentos causados pelo CLONES DA SOMBRA, agora ele está com {vida_pc} de vida.')
            elif computador == 'TOBIRAMA':
                vida_pc -= 15
                print(f'TOBIRAMA sofreu com os ferimentos causados pelo CLONES DA SOMBRA, agora ele está com {vida_pc} de vida.')
        elif ataque == '3':
            print(f'NARUTO usou a PALMA VENDAVAL.')
            sleep (1)
            if computador == 'SASUKE':
                vida_pc -= 30
                print(f'SASUKE sofreu com os ferimentos causados pela PALMA VENDAVAL, agora ele está com {vida_pc} de vida.')
            elif computador == 'KAKASHI':
                vida_pc -= 20
                print(f'KAKASHI sofreu com os ferimentos causados pela PALMA VENDAVAL, agora ele está com {vida_pc} de vida.')
            elif computador == 'TOBIRAMA':
                vida_pc -= 15
                print(f'TOBIRAMA sofreu com os ferimentos causados pela PALMA VENDAVAL, agora ele está com {vida_pc} de vida.')
        elif ataque == '4':
            print(f'NARUTO usou o JUTSU MIL ANOS DE MORTE.')
            sleep (1)
            if computador == 'SASUKE':
                vida_pc -= 10
                print(f'SASUKE sofreu com os ferimentos causados pelo MIL ANOS DE MORTE, agora ele está com {vida_pc} de vida.')
            elif computador == 'KAKASHI':
                vida_pc -= 0
                print(f'KAKASHI sofreu com os ferimentos causados pelo MIL ANOS DE MORTE, agora ele está com {vida_pc} de vida.')
            elif computador == 'TOBIRAMA':
                vida_pc -= 10
                print(f'TOBIRAMA sofreu com os ferimentos causados pelo MIL ANOS DE MORTE, agora ele está com {vida_pc} de vida.')
        elif ataque == '5':
            print(f'NARUTO se REGENEROU (+20hp).')
            sleep (1)
            vida_usuario += 20
            print(f'Sua vida agora é {vida_usuario}.')

    # ataques do sasuke
    if usuario == 'SASUKE':
        print('Escolha um ATAQUE, digite:\n[1] Para usar o CHIDORI.\n[2] Para usar o JUTSU BOLA DE FOGO.\n[3] Para usar o AMATERASU.\n[4] Para usar o COMBO DO LEÃO (TAIJUTSU).\n[5] Para se regenerar.')
        ataque = input('')
        if ataque == '1':
            print(f'SASUKE usou o CHIDORI.')
            sleep (1)
            if computador == 'NARUTO':
                vida_pc -= 20
                print(f'NARUTO sofreu com os ferimentos causados pelo CHIDORI, agora ele está com {vida_pc} de vida.')
            elif computador == 'KAKASHI':
                vida_pc -= 10
                print(f'KAKASHI sofreu com os ferimentos causados pelo CHIDORI, agora ele está com {vida_pc} de vida.')
            elif computador == 'TOBIRAMA':
                vida_pc -= 30
                print(f'TOBIRAMA sofreu com os ferimentos causados pelo CHIDORI, agora ele está com {vida_pc} de vida.')
        elif ataque == '2':
            print(f'SASUKE usou o JUTSU BOLA DE FOGO.')
            sleep (1)
            if computador == 'NARUTO':
                vida_pc -= 20
                print(f'NARUTO sofreu com os ferimentos causados pelo JUTSU BOLA DE FOGO, agora ele está com {vida_pc} de vida.')
            elif computador == 'KAKASHI':
                vida_pc -= 25
                print(f'KAKASHI sofreu com os ferimentos causados pelo JUTSU BOLA DE FOGO, agora ele está com {vida_pc} de vida.')
            elif computador == 'TOBIRAMA':
                vida_pc -= 15
                print(f'TOBIRAMA sofreu com os ferimentos causados pelo JUTSU BOLA DE FOGO, agora ele está com {vida_pc} de vida.')
        elif ataque == '3':
            print(f'SASUKE usou o AMATERASU.')
            sleep (1)
            if computador == 'NARUTO':
                vida_pc -= 20
                print(f'NARUTO sofreu com os ferimentos causados pelo AMATERASU, agora ele está com {vida_pc} de vida.')
            elif computador == 'KAKASHI':
                vida_pc -= 30
                print(f'KAKASHI sofreu com os ferimentos causados pelo AMATERASU, agora ele está com {vida_pc} de vida.')
            elif computador == 'TOBIRAMA':
                vida_pc -= 30
                print(f'TOBIRAMA sofreu com os ferimentos causados pelo AMATERASU, agora ele está com {vida_pc} de vida.')
        elif ataque == '4':
            print(f'SASUKE usou o COMBO DO LEÃO.')
            sleep (1)
            if computador == 'NARUTO':
                vida_pc -= 15
                print(f'NARUTO sofreu com os ferimentos causados pelo COMBO DO LEÃO, agora ele está com {vida_pc} de vida.')
            elif computador == 'KAKASHI':
                vida_pc -= 5
                print(f'KAKASHI sofreu com os ferimentos causados pelo COMBO DO LEÃO, agora ele está com {vida_pc} de vida.')
            elif computador == 'TOBIRAMA':
                vida_pc -= 15
                print(f'TOBIRAMA sofreu com os ferimentos causados pelo COMBO DO LEÃO, agora ele está com {vida_pc} de vida.')
        elif ataque == '5':
            print(f'SASUKE se REGENEROU (+20hp).')
            sleep (1)
            vida_pc += 20
            print(f'Sua vida agora é {vida_pc}.')

    # ataques do kakashi
    if usuario == 'KAKASHI':
        print('Escolha um ATAQUE, digite:\n[1] Para usar o CHIDORI.\n[2] Para usar o RASENGAN.\n[3] Para atacar no KAMUI.\n[4] Para usar o RAIKIRI.\n[5] Para se regenerar.')
        ataque = input('')
        if ataque == '1':
            print(f'KAKASHI usou o CHIDORI.')
            sleep (1)
            if computador == 'NARUTO':
                vida_pc -= 20
                print(f'NARUTO sofreu com os ferimentos causados pelo CHIDORI, agora ele está com {vida_pc} de vida.')
            elif computador == 'SASUKE':
                vida_pc -= 10
                print(f'SASUKE sofreu com os ferimentos causados pelo CHIDORI, agora ele está com {vida_pc} de vida.')
            elif computador == 'TOBIRAMA':
                vida_pc -= 30
                print(f'TOBIRAMA sofreu com os ferimentos causados pelo CHIDORI, agora ele está com {vida_pc} de vida.')
        elif ataque == '2':
            print(f'KAKASHI usou o RASENGAN.')
            sleep (1)
            if computador == 'NARUTO':
                vida_pc -= 10
                print(f'NARUTO sofreu com os ferimentos causados pelo RASENGAN, agora ele está com {vida_pc} de vida.')
            elif computador == 'SASUKE':
                vida_pc -= 20
                print(f'SASUKE sofreu com os ferimentos causados pelo RASENGAN, agora ele está com {vida_pc} de vida.')
            elif computador == 'TOBIRAMA':
                vida_pc -= 30
                print(f'TOBIRAMA sofreu com os ferimentos causados pelo RASENGAN, agora ele está com {vida_pc} de vida.')
        elif ataque == '3':
            print(f'KAKASHI levou o {computador} para o KAMUI e o atacou.')
            sleep (1)
            if computador == 'NARUTO':
                vida_pc -= 25
                print(f'NARUTO sofreu com os ferimentos causados no KAMUI, agora ele está com {vida_pc} de vida.')
            elif computador == 'SASUKE':
                vida_pc -= 20
                print(f'SASUKE sofreu com os ferimentos causados no KAMUI, agora ele está com {vida_pc} de vida.')
            elif computador == 'TOBIRAMA':
                vida_pc -= 25
                print(f'TOBIRAMA sofreu com os ferimentos causados no KAMUI, agora ele está com {vida_pc} de vida.')
        elif ataque == '4':
            print(f'KAKASHI usou o RAIKIRI.')
            sleep (1)
            if computador == 'NARUTO':
                vida_pc -= 20
                print(f'NARUTO sofreu com os ferimentos causados pelo RAIKIRI, agora ele está com {vida_pc} de vida.')
            elif computador == 'SASUKE':
                vida_pc -= 15
                print(f'SASUKE sofreu com os ferimentos causados pelo RAIKIRI, agora ele está com {vida_pc} de vida.')
            elif computador == 'TOBIRAMA':
                vida_pc -= 20
                print(f'TOBIRAMA sofreu com os ferimentos causados pelo RAIKIRI, agora ele está com {vida_pc} de vida.')
        elif ataque == '5':
            print(f'KAKASHI se REGENEROU (+20hp).')
            sleep (1)
            vida_pc += 20
            print(f'Sua vida agora é {vida_pc}.')

    # ataques do tobirama
    if usuario == 'TOBIRAMA':
        print('Escolha um ATAQUE, digite:\n[1] Para usar os CLONES DA SOMBRA + TAIJUTSU.\n[2] Para usar o CORTE DO RAIJIN VOADOR.\n[3] Para usar o DRAGÃO DE ÁGUA.\n[4] Para usar o TSUNAMI DE TUBARÕES.\n[5] Para se regenerar.')
        ataque = input('')
        if ataque == '1':
            print(f'TOBIRAMA usou os CLONES DA SOMBRA + TAIJUTSU.')
            sleep (1)
            if computador == 'NARUTO':
                vida_pc -= 15
                print(f'NARUTO sofreu com os ferimentos causados pelos CLONES DA SOMBRA, agora ele está com {vida_pc} de vida.')
            elif computador == 'KAKASHI':
                vida_pc -= 10
                print(f'KAKASHI sofreu com os ferimentos causados pelos CLONES DA SOMBRA, agora ele está com {vida_pc} de vida.')
            elif computador == 'SASUKE':
                vida_pc -= 15
                print(f'SASUKE sofreu com os ferimentos causados pelos CLONES DA SOMBRA, agora ele está com {vida_pc} de vida.')
        elif ataque == '2':
            print(f'TOBIRAMA usou o CORTE DO RAIJIN VOADOR.')
            sleep (1)
            if computador == 'NARUTO':
                vida_pc -= 25
                print(f'NARUTO sofreu com os ferimentos causados pelo CORTE DO RAIJIN VOADOR, agora ele está com {vida_pc} de vida.')
            elif computador == 'KAKASHI':
                vida_pc -= 20
                print(f'KAKASHI sofreu com os ferimentos causados pelo CORTE DO RAIJIN VOADOR, agora ele está com {vida_pc} de vida.')
            elif computador == 'SASUKE':
                vida_pc -= 20
                print(f'SASUKE sofreu com os ferimentos causados pelo CORTE DO RAIJIN VOADOR, agora ele está com {vida_pc} de vida.')
        elif ataque == '3':
            print(f'TOBIRAMA usou o DRAGÃO DE ÁGUA.')
            sleep (1)
            if computador == 'NARUTO':
                vida_pc -= 20
                print(f'NARUTO sofreu com os ferimentos causados pelo DRAGÃO DE ÁGUA, agora ele está com {vida_pc} de vida.')
            elif computador == 'KAKASHI':
                vida_pc -= 30
                print(f'KAKASHI sofreu com os ferimentos causados pelo DRAGÃO DE ÁGUA, agora ele está com {vida_pc} de vida.')
            elif computador == 'SASUKE':
                vida_pc -= 30
                print(f'SASUKE sofreu com os ferimentos causados pelo DRAGÃO DE ÁGUA, agora ele está com {vida_pc} de vida.')
        elif ataque == '4':
            print(f'TOBIRAMA usou o TSUNAMI DE TUBARÕES.')
            sleep (1)
            if computador == 'NARUTO':
                vida_pc -= 20
                print(f'NARUTO sofreu com os ferimentos causados pelo TSUNAMI DE TUBARÕES, agora ele está com {vida_pc} de vida.')
            elif computador == 'KAKASHI':
                vida_pc -= 25
                print(f'KAKASHI sofreu com os ferimentos causados pelo TSUNAMI DE TUBARÕES, agora ele está com {vida_pc} de vida.')
            elif computador == 'SASUKE':
                vida_pc -= 25
                print(f'SASUKE sofreu com os ferimentos causados pelo TSUNAMI DE TUBARÕES, agora ele está com {vida_pc} de vida.')
        elif ataque == '5':
            print(f'TOBIRAMA se REGENEROU (+20hp).')
            sleep (1)
            vida_pc += 20
            print(f'Sua vida agora é {vida_pc}.')
    sleep (1)

    if vida_pc <= 0 or vida_usuario <= 0:
        break

    atqnaruto = ['o RASENGAN', 'o CLONES DA SOMBRA + TAIJUTSU', 'a PALMA VENDAVAL', 'o MIL ANOS DE MORTE', 'se REGENERAR']
    atqsasuke = ['o CHIDORI', 'o JUTSU BOLA DE FOGO', 'o AMATERASU', 'o COMBO DO LEÃO (TAIJUTSU)', 'se REGENERAR']
    atqkakashi = ['o CHIDORI', 'o RASENGAN', 'atacar no KAMUI', 'o RAIKIRI', 'se REGENERAR']
    atqtobirama = ['o CLONES DA SOMBRA + TAIJUTSU', 'o CORTE DO RAIJIN VOADOR', 'o DRAGÃO DE ÁGUA', 'o TSUNAMI DE TUBARÕES', 'se REGENERAR']
    print(F'Agora é a vez do {computador} atacar!')
    if computador == 'NARUTO':
        ataquepc = random.choice(atqnaruto)
    if computador == 'SASUKE':
        ataquepc = random.choice(atqsasuke)
    if computador == 'KAKASHI':
        ataquepc = random.choice(atqkakashi)
    if computador == 'TOBIRAMA':
        ataquepc = random.choice(atqtobirama)
    print('Escolhendo...')
    print ('3')
    sleep (2)
    print('2')
    sleep (1)
    print('1')
    print(f'O {computador} usou {ataquepc}.')
    sleep (1)
    if ataquepc == 'se REGENERAR':
        print(f'{computador} se REGENEROU (+20hp).')
        sleep (1)
        vida_pc += 20
        print(f'Sua vida agora é {vida_pc}.')
        sleep (1)

    elif usuario == 'NARUTO':
        danos = [15, 20, 25, 30]
        dano = random.choice(danos)
        vida_usuario -= dano
        print(f'O {usuario} sofreu com os danos causados pelo {ataquepc} e ficou com {vida_usuario} de vida.')
        sleep (1)
    elif usuario == 'SASUKE':
        danos = [15, 20, 25, 30]
        dano = random.choice(danos)
        vida_usuario -= dano
        print(f'O {usuario} sofreu com os danos causados pelo {ataquepc} e ficou com {vida_usuario} de vida.')
        sleep (1)
    elif usuario == 'KAKASHI':
        danos = [15, 20, 25, 30]
        dano = random.choice(danos)
        vida_usuario -= dano
        print(f'O {usuario} sofreu com os danos causados pelo {ataquepc} e ficou com {vida_usuario} de vida.')
        sleep (1)
    elif usuario == 'TOBIRAMA':
        danos = [15, 20, 25, 30]
        dano = random.choice(danos)
        vida_usuario -= dano
        print(f'O {usuario} sofreu com os danos causados pelo {ataquepc} e ficou com {vida_usuario} de vida.')
        sleep (1)

if vida_pc <= 0:
    print(f'Parabéns {usuario}, você venceu a batalha contra o {computador}!')
elif vida_usuario <= 0:
    print(f'Você perdeu, o {computador} foi o vencedor dessa batalha!')