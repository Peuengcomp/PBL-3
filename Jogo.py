import os
import csv
import datetime
import random as rd

vermelho = '\033[91m'
azul = '\033[94m'
verde = '\033[92m'
reset = '\033[0m'

############################################################################################################

def limpar_tela():
    sistema_operacional = os.name

    if sistema_operacional == 'nt':  # Linux e macOS
        os.system('cls')
    else:
        os.system('clear')

def retornar():
    sair = int(input("Digite zero para retornar ao menu principal: "))
    while sair != 0:
        limpar_tela()
        sair = int(input("Digite zero para retornar ao menu principal: "))

# Este bloco de funções é responsável por imprimir o menu e retornar os valores correspondentes ás opções

def menu1():
    print("1 - Novo jogo\n", end='')
    print("2 - Continuar\n", end='')
    print("3 - Ranking\n", end='')
    print("4 - Sair do jogo\n", end='')
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

##################################################################################################################################

def sorteio(jogador):
    global verde, azul, vermelho, reset
    if jogador == 1:
        cor = azul
    else:
        cor = vermelho
    
    print(verde + f"Jogador {jogador}:\n" + reset)
    print(verde + f"Digite o nome do jogador {jogador}: " + reset, end='')
    nome = input()
    print("\n")
    objetivo = rd.randint(1,4)
    if objetivo == 1:
        print(cor + "Seu objetivo é formar uma sequência numérica ascendente. Ex: 1,2,3 ou 7,8,9\n" + reset)
    elif objetivo == 2:
        print(cor + "Seu objetivo é formar uma sequência numérica descendente. Ex: 3,2,1 ou 9,8,7\n" + reset)
    elif objetivo == 3:
        print(cor + "Seu objetivo é formar uma sequência numérica par. Ex: 2,4,6 ou 8,6,4\n" + reset)
    else:
        print(cor + "Seu objetivo é formar uma sequência numérica ímpar. Ex: 1,3,5 ou 9,7,5\n" + reset)
    
    print(verde + f"Digite {jogador} para prosseguir: " + reset, end='')
    aux = int(input())
    while aux != jogador:
        aux = int(input(f"Digite {jogador} para prosseguir: "))
    return (objetivo,nome,jogador)

def gerar_numeros_possiveis(tamanho):
    numeros = []
    for n in range(1, tamanho**2 + 1):
        numeros.append(n)
    return numeros

def jogada(dicionario, jogador, numeros, nome1, nome2):
    global azul, vermelho, reset
    if jogador == 1:
        cor = azul
        nome = nome1
    else:
        cor = vermelho
        nome = nome2
    print(cor + f"Faça sua jogada, jogador {nome}" + reset)
    linha = int(input("Digite a linha\n"))
    coluna = int(input("Digite a coluna\n"))
    if dicionario.get((linha,coluna), False) == "x":
        jogada = int(input("Digite seu número\n"))
        if jogada in numeros:
            dicionario[(linha,coluna)] = str(cor + str(jogada) + reset)
            return dicionario, jogada, linha, coluna
        else:
            return None
    else:
        return None
    
##################################################################################################################################

def verificar_lista(lista, objetivo):
    if objetivo == 1:
        razao = 1
    elif objetivo == 2:
        razao = -1
    else:
        razao = 2
    
    for k in range(len(lista) - 1):
        if lista[k+1] - lista[k] != razao:
            resultado = False
            break
        else:
            resultado = True
    if resultado == True:
        return resultado
    
def verificar_par_impar_descendencia(lista):
    for k in range(len(lista) - 1):
        if lista[k+1] - lista[k] != -2:
            resultado = False
            break
        else:
            resultado = True
    if resultado == True:
        return resultado

def verificar_linha_coluna_diagonal(dicionario, tamanho, objetivo, nome, jogador):
    for i in range(1, tamanho + 1):
        linha = []
        coluna = []
        principal = []
        secundaria = []

        for j in range(1, tamanho + 1):
            linha.append(dicionario[(i,j)])
            coluna.append(dicionario[(j,i)])
            principal.append(dicionario[(j,j)])
            secundaria.append(dicionario[(tamanho + 1 - j,j)])

        if objetivo == 1:
            resultado_linha = verificar_lista(linha, objetivo)
            resultado_coluna = verificar_lista(coluna, objetivo)
            resultado_principal = verificar_lista(principal, objetivo)
            resultado_secundaria = verificar_lista(secundaria, objetivo)
            if resultado_linha == True or resultado_coluna == True or resultado_principal == True or resultado_secundaria == True:
                return (True,nome,jogador)
            else:
                valor = (False,nome,jogador)
        elif objetivo == 2:
            resultado_linha = verificar_lista(linha, objetivo)
            resultado_coluna = verificar_lista(coluna, objetivo)
            resultado_principal = verificar_lista(principal, objetivo)
            resultado_secundaria = verificar_lista(secundaria, objetivo)
            if resultado_linha == True or resultado_coluna == True or resultado_principal == True or resultado_secundaria == True:
                return (True,nome,jogador)
            else:
                valor = (False,nome,jogador)
        elif objetivo == 3:
            if linha[0] % 2 == 0 or coluna[0] % 2 == 0 or principal[0] % 2 == 0 or secundaria[0] % 2 == 0:
                resultado_linha = verificar_lista(linha, objetivo)
                resultado_coluna = verificar_lista(coluna, objetivo)
                resultado_principal = verificar_lista(principal, objetivo)
                resultado_secundaria = verificar_lista(secundaria, objetivo)
                
                linha_descendente = verificar_par_impar_descendencia(linha)
                coluna_descendente = verificar_par_impar_descendencia(coluna)
                principal_descendente = verificar_par_impar_descendencia(principal)
                secundaria_descendente = verificar_par_impar_descendencia(secundaria)
                if resultado_linha == True or resultado_coluna == True or resultado_principal == True or resultado_secundaria == True:
                    return (True,nome,jogador)
                elif linha_descendente == True or coluna_descendente == True or principal_descendente == True or secundaria_descendente == True:
                    return (True,nome,jogador)
                else:
                    valor = (False,nome,jogador)
        else:
            if linha[0] % 2 != 0 or coluna[0] % 2 != 0 or principal[0] % 2 != 0 or secundaria[0] % 2 != 0:
                resultado_linha = verificar_lista(linha, objetivo)
                resultado_coluna = verificar_lista(coluna, objetivo)
                resultado_principal = verificar_lista(principal, objetivo)
                resultado_secundaria = verificar_lista(secundaria, objetivo)

                linha_descendente = verificar_par_impar_descendencia(linha)
                coluna_descendente = verificar_par_impar_descendencia(coluna)
                principal_descendente = verificar_par_impar_descendencia(principal)
                secundaria_descendente = verificar_par_impar_descendencia(secundaria)
                if resultado_linha == True or resultado_coluna == True or resultado_principal == True or resultado_secundaria == True:
                    return (True,nome,jogador)
                elif linha_descendente == True or coluna_descendente == True or principal_descendente == True or secundaria_descendente == True:
                    return (True,nome,jogador)
                else:
                    valor = (False,nome,jogador)
    return valor

##################################################################################################################################

def data_atual():
    hoje = datetime.date.today()
    data_formatada = hoje.strftime('%d/%m/%Y')
    return data_formatada

def ranking(nome, nivel, data):
    pontuaçao = []
    pontos = 10*nivel
    pontuaçao.append(nome)
    pontuaçao.append(str(pontos) + "pts.")
    pontuaçao.append(data)
    try:
        with open('ranking', 'a', newline='', encoding='utf-8') as rank:
            escritor = csv.writer(rank)
            escritor.writerow(pontuaçao)
    except FileNotFoundError:
        with open("ranking", 'a', newline='', encoding='utf-8') as rank:
            escritor = csv.writer(rank)
            escritor.writerow(['nome', 'pontos', 'data'])
            escritor.writerow(pontuaçao)

##################################################################################################################################
start = True
while start:
    limpar_tela()
    escolha = menu1()
    limpar_tela()
    if escolha == 1:
        opcao = menu2()
        rodar = True
        limpar_tela()
        tupla_1 = sorteio(1)
        limpar_tela()
        tupla_2 = sorteio(2)
        limpar_tela()
        jogador = rd.randint(1,2)
        matriz_visual, matriz_de_jogadas, tamanho = nivel(opcao)
        imprimir_tela(formatar_tela(tamanho, matriz_visual))
        numeros = gerar_numeros_possiveis(tamanho)
        while rodar:
            valor = jogada(matriz_visual, jogador, numeros, tupla_1[1], tupla_2[1])
            resultado = False
            if valor == None:
                limpar_tela()
                imprimir_tela(formatar_tela(tamanho, matriz_visual)) 
                print("Não é possível fazer essa jogada\n")       
            else:
                matriz_visual, lance, linha, coluna = valor
                matriz_de_jogadas[(linha,coluna)] = lance
                numeros.remove(lance)

                resultado_1 = verificar_linha_coluna_diagonal(matriz_de_jogadas, tamanho, tupla_1[0], tupla_1[1], tupla_1[2])
                valor_1 = resultado_1[0]
                resultado_2 = verificar_linha_coluna_diagonal(matriz_de_jogadas, tamanho, tupla_2[0], tupla_2[1], tupla_2[2])
                valor_2 = resultado_2[0]
                if valor_1 == True or valor_2 == True:
                    if valor_1 == True and valor_2 == True:
                        if jogador == 1:
                            nome = tupla_1[1]
                        else:
                            nome = tupla_2[1]
                    elif valor_1 == True:
                        nome = tupla_1[1]
                        jogador = tupla_1[2]
                    else:
                        nome = tupla_2[1]
                        jogador = tupla_2[2]
                    
                    resultado = True

                else:
                    None

                if resultado == True:
                    limpar_tela()
                    imprimir_tela(formatar_tela(tamanho, matriz_visual))
                    print(f"O vencedor foi o jogador {jogador}, {nome}\n")
                    data = data_atual()
                    ranking(nome, opcao, data)
                    retornar()
                    rodar = False
                
                elif len(numeros) == 0:
                    limpar_tela()
                    imprimir_tela(formatar_tela(tamanho, matriz_visual))
                    print("Empate\n")
                    retornar()
                    rodar = False

                else:
                    limpar_tela()
                    imprimir_tela(formatar_tela(tamanho, matriz_visual))
                    if jogador == 1:
                        jogador = 2
                    else:
                        jogador = 1
                
    elif escolha == 2:
        print("Continuar jogo")
    
    elif escolha == 3:
        limpar_tela()
        try:
            with open('ranking', 'r', newline='', encoding='utf-8') as rank:
                leitor = csv.reader(rank)
                for item in leitor:
                    for campos in item:
                        print(f"{(verde + str(campos) + reset)}", end='\t')
                    print("\n")
            retornar()
            
        except FileNotFoundError:
            print("Não há ranking disponível\n")
            retornar()
    
    elif escolha == 4:
        limpar_tela()
        start = False
    else:
        print("DIgite valores válidos\n")
