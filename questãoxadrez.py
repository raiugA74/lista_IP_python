def jogar_turno(jogador_da_vez, tabuleiro, historico, jogadas_validas):
    jogada = input()
    jogador_que_jogou = jogada[0]#pega a primeira letra da string N ou C

    partes = jogada.replace('(', '').replace(')', '').replace(',', '').split() # limpar a string: "N (6, 4) (4, 4)" q vira "N 6 4 4 4" e dps quebra numa lista
    lo = int(partes[1]) #linha de origem//// garantir que cada posição seja um inteiro
    co = int(partes[2]) #coluna de origem
    ld = int(partes[3]) #linha de destino
    cd = int(partes[4]) #coluna de destino

    if jogador_que_jogou != jogador_da_vez: #caso base 1, jogar fora da vez
        if jogador_que_jogou == 'N':
            nome_insistente = "Papai Noel" #ver o nome de quem errou
        else:
            nome_insistente = nome

        print(f'{nome_insistente} insistiu em jogar fora da vez! A partida foi encerrada.')

        #add a jogada errada antes de fechar
        numero = len(historico) + 1
        historico.append(f"{numero}. {nome_insistente}: {lo} {co} -> {ld} {cd} [FORA DA VEZ]")

        if jogador_que_jogou == 'N': #ver quem ganha, quem não insistiu
            vencedor = 'C'
        else:
            vencedor = 'N'
        return vencedor #caso base do jogador insistindo jogada, o que acaba a partida  
    
    nome_jogador = "Papai Noel" if jogador_da_vez == 'N' else nome

    # valida a jogada
    if not eh_jogada_valida(lo, co, ld, cd, jogador_da_vez, tabuleiro):
        print("Jogada errada, perdeu a vez!")
        numero = len(historico) + 1 #printar com o numero
        historico.append(f"{numero}. {nome_jogador}: {lo} {co} -> {ld} {cd} [ERRADA]")
    else:
        # guarda a peça do destino antes de mover (para saber se é o rei)
        peca_capturada = ""
        if (ld, cd) in tabuleiro:
            peca_capturada = tabuleiro[(ld, cd)]
            
        # move a peça: cria a chave no destino e apaga (.pop) a da origem
        tabuleiro[(ld, cd)] = tabuleiro.pop((lo, co))
        
        # registra no histórico
        numero = len(historico) + 1
        historico.append(f"{numero}. {nome_jogador}: {lo} {co} -> {ld} {cd} [VÁLIDA]")
        
        # guarda a jogada válida exata para verificar as aberturas famosas depois
        jogadas_validas.append(f"{jogador_da_vez} ({lo}, {co}) ({ld}, {cd})")

        #verificar aberturas famosas comparando a lista inteira
        if jogadas_validas == ['N (6, 4) (4, 4)', 'C (1, 2) (3, 2)']:
            print(f"Muito bem, {nome_jogador} utilizou a Defesa Siciliana!")
        elif jogadas_validas == ['N (6, 4) (4, 4)', 'C (1, 3) (3, 3)']:
            print(f"Muito bem, {nome_jogador} utilizou a Defesa Escandinava!") #coloquei nome jogador porque aí pega o nome de quem tiver jogando e fizer essa jogada
        elif jogadas_validas == ['N (6, 3) (4, 3)', 'C (1, 3) (3, 3)', 'N (6, 2) (4, 2)']:
            print(f"Muito bem, {nome_jogador} utilizou o Gambito da Rainha!")

        #caso base 2: Captura do Rei
        if peca_capturada.lower() == 'r':
            print(f"O rei foi capturado! {nome_jogador} venceu a partida!")
            return jogador_da_vez # termina recursão e retorna quem ganhou

    if jogador_da_vez == 'N': 
        proximo = 'C'
    else:
        proximo = 'N' #Noel e Criança/ INVERTER A VEZ
    return jogar_turno(proximo, tabuleiro, historico, jogadas_validas)

def eh_jogada_valida(lo, co, ld, cd, jogador, tabuleiro): #retorna sim ou não p peça poder se movimentar
    if lo > 7 or lo < 0 or ld > 7 or ld < 0 or co > 7 or co < 0 or cd > 7 or cd < 0:
        return False
    if (lo, co) == (ld, cd):#origem e destino tem que ser diferentes
        return False 
    elif (lo, co) not in tabuleiro: #tem que existir uma peça na casa de origem
        return False
   
    peca_origem = tabuleiro[(lo, co)] #a peça tem q ser do jogador da vez
    if jogador == 'N':
        if peca_origem.islower(): #se Noel tentar mover peça minúscula, é falso
            return False
    else: # jogador == 'C'
        if peca_origem.isupper(): #se Criança tentar mover peça Maiúscula, é falso
            return False

    if (ld, cd) in tabuleiro: #o destino não pode ter a peça do próprio jogador(meu Deus do Céu), FOGO AMIGO
        peca_destino = tabuleiro[(ld, cd)]
        if jogador == 'N' and peca_destino.isupper(): #NOEL NÃO PODE SE ENCONTRAR COM UPPER(PEÇAS DELE)
            return False
        if jogador == 'C' and peca_destino.islower(): #CRIANCA NÃO PODE SE ENCONTRAR COM LOWER(PEÇAS DELA)
            return False
        
    tipo = peca_origem.lower() #'R' ou 'r' viram 'r', facilita os IFs
    #regras específicas de movimento de cada peça, se INFRINGIR invalida o movimento

    if tipo == 'r': #rei: avança 1 casa em qualquer direção
        if abs(lo - ld) > 1 or abs(co - cd) > 1:
            return False
    elif tipo == 'c': #cavalo: move em L (2 em um eixo e 1 no outro)
        dist_linha = abs(lo - ld)
        dist_coluna = abs(co - cd) #abs para pegar o valor absoluto
        #se não for (2 e 1) e também não for (1 e 2), o movimento é inválido       
        if not ((dist_linha == 2 and dist_coluna == 1) or (dist_linha == 1 and dist_coluna == 2)): #pegando a diferença para ver se encaixa no 1 e 2 ou 2 e 1
            return False 
        
    elif tipo == 'b':# o bispo precisa ser a mesma diferença, ja que ele anda em diagonal///2 colunas e 2 linhas...3 e 3... 5 e 5
        if abs(lo - ld) != abs(co - cd):
            return False
        if not caminho_livre(lo, co, ld, cd, tabuleiro): #andam muito e depende do caminho livre
            return False
        
    elif tipo == 't': #torre
        if lo != ld and co != cd: #se n for reto...n é torre, só movimenta coluna ou linha
            return False
        if not caminho_livre(lo, co, ld, cd, tabuleiro): #depende do caminho livre
            return False
        
    elif tipo == 'd': #se não for diagonal q nem o bispo e nem reto que nem uma torre...ta errado///logo não é dama
        if abs(lo - ld) != abs(co - cd) and (lo != ld and co != cd): 
            return False
        if not caminho_livre(lo, co, ld, cd, tabuleiro):#depende do caminho livre
            return False
        
    elif tipo == 'p': #peão
        if jogador == 'N': #Noel (sobe no tabuleiro, linha diminui)
            #movimento reto (sem capturar)
            if co == cd:
                if ld == lo - 1: #tenta andar 1 casa
                    if (ld, cd) in tabuleiro: #se tiver alguém na frente, ele trava
                        return False
                elif ld == lo - 2 and lo == 6: #tenta andar 2 casas (só se estiver na casa inicial) linha 6
                    if (ld, cd) in tabuleiro or (lo - 1, co) in tabuleiro: # Caminho tem que estar livre
                        return False
                else:
                    return False #qualquer outro movimento reto é proibido
                    
            #movimento diagonal (APENAS p capturar)
            elif abs(co - cd) == 1 and ld == lo - 1:
                if (ld, cd) not in tabuleiro: # Se NÃO tiver ninguém lá, ele não pode andar na diagonal
                    return False
            else:
                return False # Qualquer outro movimento louco é proibido
        else:#jogador == 'C', Criança
            #movimento reto (sem capturar)
            if co == cd:
                if ld == lo + 1: #tenta andar 1 casa
                    if (ld, cd) in tabuleiro:
                        return False
                elif ld == lo + 2 and lo == 1: #tenta andar 2 casas (só se estiver na casa inicial) linha 1
                    if (ld, cd) in tabuleiro or (lo + 1, co) in tabuleiro:
                        return False
                else:
                    return False
            #movimento diagonal (APENAS capturar)
            elif abs(co - cd) == 1 and ld == lo + 1:
                if (ld, cd) not in tabuleiro: #obrigatoriamente tem que ter uma peça lá (a regra do fogo amigo já garantiu que é inimiga)
                    return False
            else:
                return False
    #se passou por tudo....é porque REALMENTE é true e pode fazer
    return True

def caminho_livre(linha_atual, coluna_atual, ld, cd, tabuleiro, primeiro_passo=True):
    #se já chegou no destino, o caminho tava livre
    if linha_atual == ld and coluna_atual == cd:
        return True
        
    #se não é o primeiro passo (a origem sempre tem peça) e a casa atual tem peça...lascou
    if not primeiro_passo and (linha_atual, coluna_atual) in tabuleiro:
        return False
        
    #descobre para que lado tem que andar na linha
    if ld > linha_atual:
        passo_linha = 1
    elif ld < linha_atual:
        passo_linha = -1
    else:
        passo_linha = 0
        
    #descobre para que lado tem que andar na coluna
    if cd > coluna_atual:
        passo_coluna = 1
    elif cd < coluna_atual:
        passo_coluna = -1
    else:
        passo_coluna = 0
        
    #da um passo na direção do destino e chama a função de novo
    nova_linha = linha_atual + passo_linha
    nova_coluna = coluna_atual + passo_coluna
    return caminho_livre(nova_linha, nova_coluna, ld, cd, tabuleiro, False)

tabuleiro_inicial = { #mermão que PESTE É ESSA BOY
    (0, 0): 't', (0, 1): 'c', (0, 2): 'b', (0, 3): 'd', (0, 4): 'r', (0, 5): 'b', (0, 6): 'c', (0, 7): 't', #minuscula da criança
    (1, 0): 'p', (1, 1): 'p', (1, 2): 'p', (1, 3): 'p', (1, 4): 'p', (1, 5): 'p', (1, 6): 'p', (1, 7): 'p',
    (6, 0): 'P', (6, 1): 'P', (6, 2): 'P', (6, 3): 'P', (6, 4): 'P', (6, 5): 'P', (6, 6): 'P', (6, 7): 'P', #maiuscula do noel
    (7, 0): 'T', (7, 1): 'C', (7, 2): 'B', (7, 3): 'D', (7, 4): 'R', (7, 5): 'B', (7, 6): 'C', (7, 7): 'T'
}

print('Ho ho ho! Quem ousa desafiar o Papai Noel numa partida de xadrez de Natal?')

nome = input()
if nome == 'Beth Harmon':
    print('Nossa, temos um gênio aqui')
elif nome == 'Magnus Carlsen':
    print('Essa vai ser difícil! O menino é um prodígio!')

print('Que a partida comece! O Papai Noel joga com as peças brancas.')

historico_partida = []
jogadas_validas_partida = []

vencedor_final = jogar_turno('N', tabuleiro_inicial, historico_partida, jogadas_validas_partida)
print('Histórico da partida:')
print('\n'.join(historico_partida)) #fazer os prints em cada linha

if vencedor_final == 'C':
    print(f'Parabéns, {nome}! Você venceu o Papai Noel e ganhou um presente!')

else:
    print(f'Ho ho ho! Você não foi uma criança boa durante o ano, {nome}, e por isso perdeu. Sem presente!')