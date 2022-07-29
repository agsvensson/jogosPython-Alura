import adivinhacao
import forca

print("*********************************")
print("        Escolha seu jogo:        ")
print("*********************************")
print("")

print("Digite 1 para Forca OU 2 para Adivinhação)")
jogo = int(input("Qual jogo? "))

if jogo == 1:
    print("Jogando Forca")
    forca.jogar()
elif jogo == 2:
    print("Jogando Adivinhação")
    adivinhacao.jogar()

print("")
print("*********************************")