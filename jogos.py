import forca
import adivinhacao

def escolhe_jogo():
    # Nome do jogo
    print("**********************************")
    print("* Escolha qual jogo você deseja *!")
    print("**********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Você escolheu jogar Forca")
        forca.jogar()
    elif( jogo == 2):
        print("Você escolheu jogar Adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()