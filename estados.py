import random

def jogar():

    print("*******************************************")
    print("*** Bem vindo ao jogo forca de Estados! ***")
    print("*******************************************")

    with open("estados.txt", "r", encoding="utf8") as nomes:
        estados = []

        # para valor dentro da lista
        for nome in nomes:
            estados.append(nome.strip())

    nomes.close()

    numero_aleatorio = random.randrange(0, len(estados))
    palavra_secreta = estados[numero_aleatorio].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 7

    print("A palavra secreta tem {} letras.".format(len(palavra_secreta)))
    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual letra você deseja chutar?")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros -= 1
            desenha_forca(erros)
            print("Ops, você errou! Faltam {} tentativas.".format(erros))

        enforcou = erros == 0
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("PARABÉNS!! Você acertou!! A palavra secreta é {}.".format(palavra_secreta))
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    else:
        print("Que pena, você foi enforcado!")
        print("A palavra secreta era {}".format(palavra_secreta))
        print("███████████████████████████")
        print("███████▀▀▀░░░░░░░▀▀▀███████")
        print("████▀░░░░░░░░░░░░░░░░░▀████")
        print("███│░░░░░░░░░░░░░░░░░░░│███")
        print("██▌│░░░░░░░░░░░░░░░░░░░│▐██")
        print("██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
        print("██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
        print("██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
        print("██▌░│██████▌░░░▐██████│░▐██")
        print("███░│▐███▀▀░░▄░░▀▀███▌│░███")
        print("██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
        print("██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
        print("████▄─┘██▌░░░░░░░▐██└─▄████")
        print("█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
        print("████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
        print("█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
        print("███████▄░░░░░░░░░░░▄███████")
        print("██████████▄▄▄▄▄▄▄██████████")
        print("██████████████████████████")

    print("Fim do jogo")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogar()