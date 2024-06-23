import os
import random as rd

vermelho = '\033[91m'
azul = '\033[94m'
verde = '\033[92m'
reset = '\033[0m'

# Este bloco de funções é responsável por imprimir o menu e retornar os valores correspondentes às opções

def menu1():
    print("1 - Novo jogo\n", end='')
    print("2 - Continuar\n", end='')
    print("3 - Sair do jogo\n", end='')
    escolha = int(input("Selecionar: "))
    return escolha

def menu2():
    print("Selecione o tipo de dificuldade:\n")
    print("1 - Fácil\n", end='')
    print("2 - Normal\n", end='')
    print("3 - Difícil\n", end='')
    escolha = int(input("Nível: "))
    return escolha

# Este blogo é responsável por gerar o jogo conforme o seu tamanho. Ela cria duas matrizes esparsas, uma para verificação, outra para visualização

def gerar_jogo(tamanho):
    matriz_de_jogo = {}
    matriz_de_jogadas = {}
    for i in range(1, tamanho + 1):
        for j in range(1, tamanho + 1):
            matriz_de_jogo[(i,j)] = "x"
            matriz_de_jogadas[(i,j)] = -100
    return matriz_de_jogo, matriz_de_jogadas

def nivel(opcao):
    if opcao == 1:
        tamanho = 3
        matriz_de_jogo, matriz_de_jogadas = gerar_jogo(tamanho)
    elif opcao == 2:
        tamanho = 4
        matriz_de_jogo, matriz_de_jogadas = gerar_jogo(tamanho)
    else:
        tamanho = 5
        matriz_de_jogo, matriz_de_jogadas = gerar_jogo(tamanho)
    return matriz_de_jogo, matriz_de_jogadas, tamanho

def formatar_tela(tamanho, dicionario):
    global verde, reset
    matriz = []
    for i in range(1, tamanho + 1):
        lista = []
        for j in range(1, tamanho + 1):
            lista.append(dicionario[(i,j)])
        matriz.append(lista)
    indice = []
    for indice_coluna in range(1, len(matriz) + 1):
        indice_coluna = verde + ("C" + str(indice_coluna)) + reset
        indice.append(indice_coluna)
    indice.insert(0, verde + "I" + reset)
    matriz.insert(0, indice)
    for indice_linha in range(1, len(matriz)):
        elemento = matriz[indice_linha]
        elemento.insert(0,verde + ("L" + str(indice_linha)) + reset)
        matriz[indice_linha] = elemento
    return matriz

def imprimir_tela(matriz):
    for lista in matriz:
        for elemento in lista:
            print(f"|{elemento}|", end='\t')
        print("\n")

def sorteio(jogador):
    print(f"Jogador {jogador}:\n")
    nome = input(f"Digite o nome do jogador {jogador}: ")
    objetivo = rd.randint(1,4)
    if objetivo == 1:
        print("Seu objetivo é formar uma sequência numérica ascendente\n")
    elif objetivo == 2:
        print("Seu objetivo é formar uma sequência numérica descendente\n")
    elif objetivo == 3:
        print("Seu objetivo é formar uma sequência numérica par\n")
    else:
        print("Seu objetivo é formar uma sequência numérica ímpar\n")
    aux = int(input(f"Digite {jogador} para prosseguir: "))
    while aux != jogador:
        aux = int(input(f"Digite {jogador} para prosseguir: "))
    return (objetivo,nome,jogador)

def jogada(dicionario, jogador):
    global azul, vermelho, reset
    if jogador == 1:
        cor = azul
    else:
        cor = vermelho
    print(cor + f"Faça sua jogada, jogador {jogador}" + reset)
    linha = int(input("Digite a linha\n"))
    coluna = int(input("Digite a coluna\n"))
    if dicionario.get((linha,coluna), False) == "x":
        jogada = int(input("Digite seu número\n"))
        dicionario[(linha,coluna)] = str(cor + str(jogada) + reset)
        return dicionario, jogador, jogada, linha, coluna
    else:
        return None
    
def razao_numerica(objetivo):
    if objetivo == 1:
        return 1
    elif objetivo == 2:
        return -1
    else:
        return 2

def verificar_lista(lista, objetivo):
    for k in range(len(lista) - 1):
        if lista[k+1] - lista[k] != razao_numerica(objetivo):
            resultado = False
            break
        else:
            resultado = True
    if resultado == True:
        return resultado
    

def verificar_linha_coluna(dicionario, tamanho, objetivo, nome, jogador):
    for i in range(1, tamanho + 1):
        linha = []
        coluna = []
        for j in range(1, tamanho + 1):
            linha.append(dicionario[(i,j)])
            coluna.append(dicionario[(j,i)])
        if objetivo == 1:
            resultado_linha = verificar_lista(linha, objetivo)
            resultado_coluna = verificar_lista(coluna, objetivo)
            if resultado_linha == True or resultado_coluna == True:
                return (True,nome,jogador)
            else:
                return (False,nome,jogador)
        elif objetivo == 2:
            resultado_linha = verificar_lista(linha, objetivo)
            resultado_coluna = verificar_lista(coluna, objetivo)
            if resultado_linha == True or resultado_coluna == True:
                return (True,nome,jogador)
            else:
                return (False,nome,jogador)
        elif objetivo == 3:
            if linha[0] % 2 == 0 or coluna[0] % 2 == 0:
                resultado_linha = verificar_lista(linha, objetivo)
                resultado_coluna = verificar_lista(coluna, objetivo)
                if resultado_linha == True or resultado_coluna == True:
                    return (True,nome,jogador)
                else:
                    return (False,nome,jogador)
        else:
            if linha[0] % 2 != 0 or coluna[0] % 2 != 0:
                resultado_linha = verificar_lista(linha, objetivo)
                resultado_coluna = verificar_lista(coluna, objetivo)
                if resultado_linha == True or resultado_coluna == True:
                    return (True,nome,jogador)
                else:
                    return (False,nome,jogador)

start = True
while start:
    escolha = menu1()
    os.system('clear')
    if escolha == 1:
        opcao = menu2()
        rodar = True
        os.system('clear')
        tupla_1 = sorteio(1)
        os.system('clear')
        tupla_2 = sorteio(2)
        os.system('clear')
        jogador = rd.randint(1,2)
        matriz_visual, matriz_de_jogadas, tamanho = nivel(opcao)
        imprimir_tela(formatar_tela(tamanho, matriz_visual))
        while rodar:
            valor = jogada(matriz_visual, jogador)
            resultado = False
            if valor == None:
                print("Não é possível fazer essa jogada\n")         
            else:
                matriz_visual, jogador, lance, linha, coluna = valor
                matriz_de_jogadas[(linha,coluna)] = lance

                resultado_1 = verificar_linha_coluna(matriz_de_jogadas, tamanho, tupla_1[0], tupla_1[1], tupla_1[2])
                valor_1 = resultado_1[0]
                resultado_2 = verificar_linha_coluna(matriz_de_jogadas, tamanho, tupla_2[0], tupla_2[1], tupla_2[2])
                valor_2 = resultado_2[0]
                if valor_1 == True or valor_2 == True:
                    if valor_1 == True and valor_2 == True:
                        resultado = True
                    elif valor_1 == True:
                        jogador = tupla_1[2]
                        resultado = True
                    else:
                        jogador = tupla_2[2]
                        resultado = True
                else:
                    None

                if resultado == True:
                    os.system('clear')
                    imprimir_tela(formatar_tela(tamanho, matriz_visual))
                    print(f"O vencedor foi o jogador {jogador}\n")
                    rodar = False
                
                else:
                    os.system('clear')
                    imprimir_tela(formatar_tela(tamanho, matriz_visual))
                    if jogador == 1:
                        jogador = 2
                    else:
                        jogador = 1
    elif escolha == 2:
        print("Continuar jogo")
    
    elif escolha == 3:
        start = False
    
    else:
        print("DIgite valores válidos\n")