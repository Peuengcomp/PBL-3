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

def menu3():
    print("1 - Incluir jogada especial\n", end='')
    print("2 - Não incluir jogada especial\n", end='')
    escolha = int(input("Selecionar: "))
    while escolha != 1 and escolha != 2:
        print("1 - Incluir jogada especial\n", end='')
        print("2 - Não incluir jogada especial\n", end='')
        escolha = int(input("Selecionar: "))
    return escolha

def menu4(jogador, nome_1, nome_2):
    global azul, vermelho, reset
    if jogador == 1:
        nome = nome_1
        cor = azul
    else:
        nome = nome_2
        cor = vermelho
    
    print(cor + f"Deseja fazer a jogada especial, jogador {nome}\n" + reset, end='')
    print("1 - Sim\n", end='')
    print("2 - Não\n", end='')
    escolha = int(input("Selecionar: "))
    while escolha != 1 and escolha != 2:
        print("Deseja fazer a jogada especial\n", end='')
        print("1 - Sim\n", end='')
        print("2 - Não\n", end='')
        escolha = int(input("Selecionar: "))
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

def sorteio(jogador, especial):
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
    
    if especial == 1:
        return (objetivo,nome,jogador, 1)
    else:
        return (objetivo,nome,jogador, 0)

##################################################################################

def gerar_numeros_possiveis(tamanho):
    numeros = []
    for n in range(1, tamanho**2 + 1):
        numeros.append(n)
    return numeros

def imprimir_numeros(jogados, disponiveis):
    jogados.sort()
    disponiveis.sort()

    print("Números já jogados: ", end='')
    for elemento in jogados:
        if elemento == jogados[-1]:
            print(f"{elemento}", end='.')
        else:
            print(f"{elemento}", end=', ')
    print("\n")

    print("Números disponiveis: ", end='')
    for elemento in disponiveis:
        if elemento == disponiveis[-1]:
            print(f"{elemento}", end='.')
        else:
            print(f"{elemento}", end=', ')
    print("\n")

##################################################################################
        
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

def jogada_especial(matriz_de_jogadas, matriz_visual, tamanho, jogador, numeros_jogados, numeros):
    global azul, vermelho, reset
    if jogador == 1:
        cor = azul
    else:
        cor = vermelho

    indices = []
    for i in range(1, tamanho + 1):
        indices.append(i)
    
    print(cor + "Deseja apagar linha ou coluna?\n" + reset)
    print("1 - Linha\n", end='')
    print("2 - Coluna\n", end='')
    entrada = int(input("Selecionar: "))
    while entrada != 1 and entrada != 2:
        print(cor + "Deseja apagar linha ou coluna?\n" + reset)
        print("1 - Linha\n", end='')
        print("2 - Coluna\n", end='')
        entrada = int(input("Selecionar: "))
    
    if entrada == 1:
        print("\n")
        print("Digite o valor da linha\n", end='')
        linha_remover = int(input("Selecionar: "))
        while linha_remover not in indices:
            print("Digite valores válidos\n", end='')
            linha_remover = int(input("Selecionar: "))
        
        for j in range(1, tamanho + 1):
            valor = matriz_de_jogadas[(linha_remover,j)]
            if valor != -100:
                numeros_jogados.remove(valor)
                numeros.append(valor)
            matriz_de_jogadas[(linha_remover,j)] = -100
            matriz_visual[(linha_remover,j)] = "x"
        return matriz_de_jogadas, matriz_visual, jogador, numeros_jogados, numeros
        
    else:
        print("\n")
        print("Digite o valor da coluna\n", end='')
        coluna_remover = int(input("Selecionar: "))

        while coluna_remover not in indices:
            print("Digite valores válidos\n", end='')
            coluna_remover = int(input("Selecionar: "))
        
        for j in range(1, tamanho + 1):
            valor = matriz_de_jogadas[(j,coluna_remover)]
            if valor != -100:
                numeros_jogados.remove(valor)
                numeros.append(valor)
            matriz_de_jogadas[(j,coluna_remover)] = -100
            matriz_visual[(j,coluna_remover)] = "x"
        return matriz_de_jogadas, matriz_visual, jogador, numeros_jogados, numeros
    
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
            else:
                valor = (False,nome,jogador)
    return valor

##################################################################################################################################

def ranking(nome, nivel):
    pontuaçao = []
    pontos = 10*nivel
    pontuaçao.append(nome)
    pontuaçao.append(str(pontos) + "pts.")
    try:
        with open('ranking', 'a', newline='', encoding='utf-8') as rank:
            escritor = csv.writer(rank)
            escritor.writerow(pontuaçao)
            rank.close()
    except FileNotFoundError:
        with open("ranking", 'w', newline='', encoding='utf-8') as rank:
            escritor = csv.writer(rank)
            escritor.writerow(['nome', 'pontos'])
            escritor.writerow(pontuaçao)
            rank.close()

##################################################################################################################################
start = True
while start:
    limpar_tela()
    escolha = menu1()
    limpar_tela()
    if escolha == 1:
        opcao = menu2()
        limpar_tela()
        especial = menu3()
        rodar = True
        limpar_tela()
        tupla_1 = sorteio(1, especial)
        objetivo_1, nome_1, jogador_1, especial_1 = tupla_1[0], tupla_1[1], tupla_1[2], tupla_1[3]
        limpar_tela()
        tupla_2 = sorteio(2, especial)
        objetivo_2, nome_2, jogador_2, especial_2 = tupla_2[0], tupla_2[1], tupla_2[2], tupla_2[3]
        limpar_tela()
        jogador = rd.randint(1,2)
        matriz_visual, matriz_de_jogadas, tamanho = nivel(opcao)
        imprimir_tela(formatar_tela(tamanho, matriz_visual))
        numeros = gerar_numeros_possiveis(tamanho)
        numeros_jogados = []
        while rodar:
            if especial == 1 and (especial_1 == 1 or especial_2 == 1):
                if especial_1 == 1 and jogador == 1:
                    jogar_especial = menu4(jogador, nome_1, nome_2)
                elif especial_2 == 1 and jogador == 2:
                    jogar_especial = menu4(jogador, nome_1, nome_2)
                else:
                    pass
            else:
                jogar_especial = 0
                especial = 0

            if jogar_especial == 1:
                if (especial_1 == 1 and jogador == 1) or (especial_2 == 1 and jogador_2 == 2):
                    valor_jogada_especial = jogada_especial(matriz_de_jogadas, matriz_visual, tamanho, jogador, numeros_jogados, numeros)
                    matriz_de_jogadas, matriz_visual, jogador, numeros_jogados, numeros = valor_jogada_especial
                    if jogador == 1:
                        especial_1 = 0
                    else:
                        especial_2 = 0
                    limpar_tela()
                    imprimir_tela(formatar_tela(tamanho, matriz_visual))
                    imprimir_numeros(numeros_jogados, numeros)
            else:
                pass

            valor_jogada = jogada(matriz_visual, jogador, numeros, nome_1, nome_2)
            resultado = False
            if valor_jogada == None:
                limpar_tela()
                imprimir_tela(formatar_tela(tamanho, matriz_visual))
                imprimir_numeros(numeros_jogados, numeros)
                print("Não é possível fazer essa jogada\n")   
            else:
                matriz_visual, lance, linha, coluna = valor_jogada
                matriz_de_jogadas[(linha,coluna)] = lance
                numeros.remove(lance)
                numeros_jogados.append(lance)

                resultado_1 = verificar_linha_coluna_diagonal(matriz_de_jogadas, tamanho, objetivo_1, nome_1, jogador_1)
                valor_1 = resultado_1[0]
                resultado_2 = verificar_linha_coluna_diagonal(matriz_de_jogadas, tamanho, objetivo_2, nome_2, jogador_2)
                valor_2 = resultado_2[0]
                if valor_1 == True or valor_2 == True:
                    if valor_1 == True and valor_2 == True:
                        if jogador == 1:
                            nome = nome_1
                            jogador = jogador_1
                        else:
                            nome = nome_2
                            jogador = jogador_2
                    elif valor_1 == True:
                        nome = nome_1
                        jogador = jogador_1
                    else:
                        nome = nome_2
                        jogador = jogador_2
            
                    resultado = True

                else:
                    pass

                if resultado == True:
                    limpar_tela()
                    imprimir_tela(formatar_tela(tamanho, matriz_visual))
                    imprimir_numeros(numeros_jogados, numeros)
                    print(f"O vencedor foi o jogador {jogador}, {nome}\n")
                    ranking(nome, opcao)
                    retornar()
                    rodar = False
                
                elif len(numeros) == 0:
                    limpar_tela()
                    imprimir_tela(formatar_tela(tamanho, matriz_visual))
                    imprimir_numeros(numeros_jogados, numeros)
                    print("Empate\n")
                    retornar()
                    rodar = False

                else:
                    limpar_tela()
                    imprimir_tela(formatar_tela(tamanho, matriz_visual))
                    imprimir_numeros(numeros_jogados, numeros)
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
