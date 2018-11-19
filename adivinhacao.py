import random

def jogar():
    print('**************************************')
    print('Bem vindo ao jogo de adivinhação')
    print('**************************************')
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 3
    rodada = 1
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Escolha o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    print(numero_secreto)
    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou", chute)
        chute = int(chute)

        if (chute < 1 or chute > 100):
            print("Digite um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto

        if (numero_secreto == chute):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Você errou. Seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou. Seu chute foi menor que o número secreto.")
                pontos -= abs(numero_secreto - chute)

    print("Fim do jogo")

    print("R$ {:f}".format(1.3))
    print("R$ {:.2f}".format(1.3))
    print("R$ {:7.2f}".format(1.3))
    print("R$ {:07.2f}".format(1.3))
    print("{:07d}".format(1))

if (__name__ == "__main__"):
    jogar()