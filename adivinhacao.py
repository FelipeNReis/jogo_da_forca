import random

def jogar():

    # Nome do jogo
    print("************************************")
    print("* Bem vindo ao jogo de Adivinhação *")
    print("************************************")

    # Variáveis
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 5
    pontos = 1000

    # Nível do jogo
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    # Definição do nível
    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}". format( rodada, total_de_tentativas))

    # Passo a passo do chute
        chute_str = input("Escolha um número de 1 a 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número de 1 a 100!")
            continue
    # Condições
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

    # Resposta se acertou ou errou
        if (acertou):
            print("Resposta correta. Parabéns, você fez {} pontos!!!".format(pontos))
            break

        else:
            if(maior):
                print("Resposta errada! O seu chute foi maior que o número secreto. Tente novamente!")
                pontos_perdidos = abs(numero_secreto - chute)  # ex: 40-20
                pontos = pontos - pontos_perdidos
            elif(menor):
                print("Resposta errada! O seu chute foi menor que o número secreto. Tente novamente!")
                pontos_perdidos = abs(numero_secreto - chute) # ex: 40-20
                pontos = pontos - pontos_perdidos

    print("Fim do jogo!")

if(__name__== "__main__"):
    jogar()
