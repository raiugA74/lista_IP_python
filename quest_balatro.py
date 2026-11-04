def verificar_mao(mao):
    erros = 0
    valores_retirar = []

    mao_copiada = mao.copy()

    mao_copiada.insert(0, 'x') #copiar e ajustar o indice

    piso = len(mao_copiada) // 2 #piso

    for i in range(1, piso): #1 até o piso
        if mao_copiada[i] < mao_copiada[2 * i]:
            valores_retirar.append(2 * i)
            erros += 1 #contagem de erros

        if (2 * i + 1) < len(mao_copiada):
            if mao_copiada[i] < mao_copiada[2 * i + 1]:
                valores_retirar.append(2 * i + 1)
                erros += 1

            

    mao_filtrada = []
    for i in range(1, len(mao_copiada)):
        if i not in valores_retirar:
            mao_filtrada.append(mao_copiada[i])


    return mao_filtrada, erros


def calculo_chips_mult(erros):

    if erros >= 3:
        nome_mao = 'Carta Maior'
        chips_base = 5
        mult_base = 1
    elif erros == 2:
        nome_mao = 'Dois pares'
        chips_base = 20
        mult_base = 2
    elif erros == 1:
        nome_mao = 'Três do mesmo'
        chips_base = 30
        mult_base = 3
    else:
        nome_mao = 'Full House'
        chips_base = 40
        mult_base = 4


    return nome_mao, chips_base, mult_base


def efeitos_curinga(lista_curingas, chips, mult):
    for i in range(len(lista_curingas)):
        curinga_atual = lista_curingas[i]
        
        #  Blueprint
        if curinga_atual == 'Blueprint':
            if i + 1 < len(lista_curingas) and lista_curingas[i + 1] != 'Blueprint':
                curinga_atual = lista_curingas[i + 1]
                
        
        if curinga_atual == 'Joker':
            mult+= 4
           
        elif curinga_atual == 'Space Joker':
            chips += 20
            mult += 1
            
    return chips, mult

def efeitos_arcanos(arcanos_ativados, mao_filtrada, mult):
        if 'Hierofante' in arcanos_ativados:
            for i in range(len(mao_filtrada)):
                if mao_filtrada[i] < 30:
                    mao_filtrada[i] *= 2

        if 'Justiça' in arcanos_ativados:
            for carta in mao_filtrada:
                if carta % 3 == 0:
                    mult *= 1.1

        if 'Força' in arcanos_ativados:
            for i in range(len(mao_filtrada)):
                if int(mao_filtrada[i] ** (1/2)) ** 2 == mao_filtrada[i]:
                    mao_filtrada[i] += 50

        
        return mao_filtrada, mult            

def soma_pontuacao(chips_base, mao_filtrada, mult_total):

    chips_totais = chips_base + sum(mao_filtrada)
    pontuacao_final = int(chips_totais * round(mult_total, 2))
    return chips_totais, pontuacao_final

  
#start da gameplay
meta = int(input())
print(f"Jimbo: Certo, você tem que conseguir {meta} chips. Boa sorte!")

inventario = eval(input())

curingas_possiveis = ['Joker', 'Space Joker', 'Blueprint', 'Chicot']
lista_curingas_bp = []
lista_arcanos = []

lista_curinga = []

for item in inventario:
    if item in curingas_possiveis:
        lista_curingas_bp.append(item)
    else:
        lista_arcanos.append(item)

for i in range(len(lista_curingas_bp)):
    curinga = lista_curingas_bp[i]
    if curinga == 'Blueprint':
        if (i + 1) < len(lista_curingas_bp) and lista_curingas_bp[i + 1] != 'Blueprint':
            lista_curinga.append(lista_curingas_bp[i+1])
    else:
        lista_curinga.append(curinga)

if len(lista_curingas_bp) > 0:
  print(f"Curingas: {', '.join(lista_curingas_bp)}")
else:
  print("Curingas: ")

if len(lista_arcanos) > 0:
  print(f"Arcanos: {', '.join(lista_arcanos)}")
else:
    print('Arcanos: ')

pontos_acumulados = 0
maos_jogadas = 0
trocas = 0

arcanos_ativados_na_mao = [] 
mao = eval(input())

while pontos_acumulados < meta and maos_jogadas < 4:
    acao = input()
    
    if acao == 'Trocar':
        if trocas < 4:
            mao = eval(input())
            trocas += 1
            
    elif acao == 'Arcano':
        if len(lista_arcanos) > 0:
            arcano_usado = lista_arcanos.pop(0) # Tira o primeiro arcano da lista
            
            if arcano_usado == 'Tolo':
                novo_arcano = input()
                lista_arcanos.append(novo_arcano)
            else:
                arcanos_ativados_na_mao.append(arcano_usado)
                
            print(f"Arcanos: {', '.join(lista_arcanos)}")


    elif acao == 'Jogar':   
        mao_filtrada, erros = verificar_mao(mao)
        qtd_chicot = lista_curinga.count('Chicot')

        erros -= (2 * qtd_chicot)
        if erros < 0:
            erros = 0
        # calcula chips base, multiplicador base e pega o nome da mão
        nome_mao, chips_base, mult_base = calculo_chips_mult(erros)


        chips_pos_curinga, mult_pos_curinga = efeitos_curinga(lista_curingas_bp, chips_base, mult_base) #chamar os efeitos
        mao_pos_arcano, mult_final = efeitos_arcanos(arcanos_ativados_na_mao, mao_filtrada, mult_pos_curinga) #dps das mudanças

        chips_totais, pontuacao_final = soma_pontuacao(chips_pos_curinga, mao_pos_arcano, mult_final)

        pontos_acumulados += pontuacao_final
        print(f"Classificação da mão: {nome_mao}")

        if mult_final % 1 == 0:
          print(f"{chips_totais} chips x {mult_final} = {pontuacao_final}")

        elif mult_final == 2.20:
            print(f'{chips_totais} chips x 2.2 = {pontuacao_final}')

        else:
             print(f"{chips_totais} chips x {mult_final:.2f} = {pontuacao_final}")

        print(f"Total de chips: {pontos_acumulados}")

        maos_jogadas += 1
        arcanos_ativados_na_mao = []
        if pontos_acumulados < meta and maos_jogadas < 4:
            mao = eval(input())

if pontos_acumulados >= meta:
    print("Jimbo: Impressionante, você bateu a aposta.")
    
    if maos_jogadas == 1:
        print("Jimbo: Balatro Balatrez esta a jugar balatro")

    elif maos_jogadas == 4:
        print("Jimbo: Por pouco você falha, calculou bem.")

    else:
        print("Jimbo: Ainda bem que não apostei contra você.")
else:
    qnt_faltante = meta - pontos_acumulados
    print(f"Jimbo: Mais que flop! Faltou {qnt_faltante} chips.")