import forca
import adivinhacao
import velha

print('**************************************')
print('Escolha seu jogo!')
print('**************************************')

print("(1) Forca (2) Adivinhação (3) Velha")

jogo = int(input("Qual jogo?"))

if (jogo == 1):
    forca.jogar()
elif(jogo == 2):
    adivinhacao.jogar()
else:
    velha.jogar()

print("Fim do jogo")