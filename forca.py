import estados
import frutas
import países
import carros

def jogar():

    print("*******************************************")
    print("*** Bem vindo ao jogo de Forca! ***")
    print("*******************************************")

    print("*** Escolha qual tema você deseja jogar ***")

    jogo = int(input("(1) Frutas (2) Estados (3) Países (4) Carros"))

    if(jogo == 1):
        print("Você escolheu o tema Frutas")
        frutas.jogar()

    elif( jogo == 2):
        print("Você escolheu o tema Estados")
        estados.jogar()

    elif( jogo == 3):
        print("Você escolheu o tema Países")
        países.jogar()

    elif( jogo == 4):
        print("Você escolheu o tema Carros")
        carros.jogar()


if (__name__ == "__main__"):
    jogar()
