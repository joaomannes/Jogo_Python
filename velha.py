import random

class Velha:

    def __init__(self, jogador1, jogador2):
        self.__posicoes = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.__tabuleiro = ['', '', '', '', '', '', '', '', '']
        self.__jogadores = [jogador1, jogador2]
        self.__jogador_atual = self.__jogadores[random.randrange(0, 1)]

    def jogada(self, posicao):
        posicao_jogar = self.__posicoes.index(posicao)
        if self.__tabuleiro[posicao_jogar] != '':
            print('Jogada Inválida')
        else:
            self.__tabuleiro[posicao_jogar] = self.__jogador_atual.simbolo

    @property
    def jogador_atual(self):
        return self.__jogador_atual

    def verifica_vencedor(self):
        if self.__tabuleiro[0] == self.__tabuleiro[1] == self.__tabuleiro[2] != '':
            return self.busca_jogador(self.__tabuleiro[0])
        elif self.__tabuleiro[3] == self.__tabuleiro[4] == self.__tabuleiro[5] != '':
            return self.busca_jogador(self.__tabuleiro[3])
        elif self.__tabuleiro[6] == self.__tabuleiro[7] == self.__tabuleiro[8] != '':
            return self.busca_jogador(self.__tabuleiro[6])
        elif self.__tabuleiro[0] == self.__tabuleiro[3] == self.__tabuleiro[6] != '':
            return self.busca_jogador(self.__tabuleiro[0])
        elif self.__tabuleiro[1] == self.__tabuleiro[4] == self.__tabuleiro[7] != '':
            return self.busca_jogador(self.__tabuleiro[1])
        elif self.__tabuleiro[2] == self.__tabuleiro[5] == self.__tabuleiro[8] != '':
            return self.busca_jogador(self.__tabuleiro[2])
        elif self.__tabuleiro[0] == self.__tabuleiro[4] == self.__tabuleiro[8] != '':
            return self.busca_jogador(self.__tabuleiro[0])
        elif self.__tabuleiro[2] == self.__tabuleiro[4] == self.__tabuleiro[6] != '':
            return self.busca_jogador(self.__tabuleiro[2])

    def verifica_empate(self):
        return '' not in self.__tabuleiro

    def busca_jogador(self, simbolo):
        if self.__jogadores[0].simbolo == simbolo:
            return self.__jogadores[0]
        else:
            return self.__jogadores[1]

    def altera_jogador(self):
        if self.__jogador_atual == self.__jogadores[0]:
            self.__jogador_atual = self.__jogadores[1]
        else:
            self.__jogador_atual = self.__jogadores[0]

    def imprime_tabuleiro(self):
        posicao = 0
        tabuleiro = ''
        for i in range(0,3):
            tabuleiro = ''
            for n in range(0,3):
                imprimir = ''
                if self.__tabuleiro[posicao] != '':
                    imprimir = self.__tabuleiro[posicao]
                else:
                    imprimir = ' '
                tabuleiro += f'[{imprimir}]'
                posicao += 1
            print(tabuleiro)

    def imprime_exemplo(self):
        posicao = 0
        tabuleiro = ''
        for i in range(0,3):
            tabuleiro = ''
            for n in range(0,3):
                tabuleiro += f'[{self.__posicoes[posicao]}]'
                posicao += 1
            print(tabuleiro)

class Jogador:

    def __init__(self, nome, simbolo):
        self.nome = nome
        self.simbolo = simbolo



def jogar():
    nome_jogador = input('Digite o nome do Jogador 1')
    jogador1 = Jogador(nome_jogador, 'X')
    nome_jogador = input('Digite o nome do Jogador 2')
    jogador2 = Jogador(nome_jogador, 'O')
    jogo = Velha(jogador1, jogador2)
    vencedor = None
    venceu = False
    empatou = False

    while not venceu and not empatou:
        print('Tabuleiro Exemplo:')
        jogo.imprime_exemplo()
        print('\n')
        jogo.imprime_tabuleiro()
        jogada = int(input(f'{jogo.jogador_atual.nome}, Digite a posição em que deseja jogar: '))
        jogo.jogada(jogada)
        vencedor = jogo.verifica_vencedor()
        venceu = vencedor is not None
        empatou = jogo.verifica_empate()
        jogo.altera_jogador()

    jogo.imprime_tabuleiro()
    if empatou:
        print('Jogo Empatado')
    else:
        print(f'{vencedor.nome}, você ganhou!')


if __name__ == '__main__':
    jogar()
