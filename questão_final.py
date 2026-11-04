def calcular_determinante(matriz): #teorema de LAPLACE
    tamanho = len(matriz)

    if tamanho == 1: #caso base 1x1
        return matriz[0][0] #o unico elemento da matriz 
    
    if tamanho == 2: # outro caso base 2x2
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    determinante_total = 0 #caso recursivo /// 3x3 ou mais

    for c in range(tamanho): #caminhar pelas colunas da 1 linha
        valor_escolhido = matriz[0][c]

        if c % 2 == 0: #alternancia dos sinais de laplaca
            sinal = 1
        else:
            sinal = -1

        matriz_menor = [] #submatriz menor, remove a linha 0 e a coluna c
        for i in range(1, tamanho): 
            linha_menor = []
            for j in range(tamanho):
                if j != c:
                    linha_menor.append(matriz[i][j])
            matriz_menor.append(linha_menor)

        det_menor = calcular_determinante(matriz_menor) #recursão p submatriz

        parcela = valor_escolhido * sinal * det_menor #calculo da parcela atual 
        determinante_total += parcela #acumulo no determinante total

    return determinante_total
    
print('🎄 O Natal chegou na Cozinha! Vamos preparar um Biscoito digno do Papai Noel!') #start da parada

dimensoes = input().split() #qtd de linhas e colunas
qtd_linhas = int(dimensoes[0])
qtd_colunas = int(dimensoes[1])

while(qtd_linhas != qtd_colunas) or qtd_linhas <= 0: #em qlqr um dos cenários da bronca
    print("Esse Biscoito não cabe na Receita! Precisamos de um Quadrado com dimensões positivas!")
    dimensoes = input().split()
    qtd_linhas = int(dimensoes[0]) #novos valores até...receber corretamente, com a dimensão quadrada
    qtd_colunas = int(dimensoes[1])

print("🍪 Hora de preparar a Massa! Qual a Gostosura de cada pedaço?")
matriz_inicial = []
for i in range(qtd_linhas):
    linha_str = input().split() #recebo em str com split
    linha_num = []
    for item in linha_str: #cada numero em str dentro da linha, eu vou adicionar na lista transformando em inteiro
        linha_num.append(int(item)) #coloco em int
    matriz_inicial.append(linha_num) #add na matriz, lista maior

print('Vamos dar um toque de Magia! Onde colocaremos os Enfeites Natalinos?')
mapa_enfeites = []
for i in range(qtd_linhas): #onde receberei os simbolos/enfeites
    linha = input().split()
    mapa_enfeites.append(linha)

matriz_final = []
qtd_E = 0 #qtd de cada um na parada
qtd_F = 0
qtd_P = 0
qtd_A = 0
total_enfeites = 0
for r in range(qtd_linhas): #vasculhar nas matrizes
    linha_transformada = []
    for c in range(qtd_colunas):
        val = matriz_inicial[r][c]
        sym = mapa_enfeites[r][c] #simbolos do mapa de enfeites
        if sym == 'E': #estrela
            valor_transf = val * 2  #multiplica por 2
            qtd_E += 1
            total_enfeites += 1
        elif sym == 'F': #floco
            valor_transf = -val  #inverte sinal
            qtd_F += 1
            total_enfeites += 1
        elif sym == 'P': #presente
            valor_transf = val + 5 #soma 5
            qtd_P += 1
            total_enfeites += 1
        elif sym == 'A': #arvore
            valor_transf = val ** 2 #era elevado a 2 mds do ceu
            qtd_A += 1
            total_enfeites += 1
        else: #peste nenhuma
            valor_transf = val #mantém

        linha_transformada.append(valor_transf) #pegando a linha
    matriz_final.append(linha_transformada) #colocando na matriz final

gostosura = calcular_determinante(matriz_final)

print('Vamos a Análise Final!\n') #final da questãaaaaaaaaaao(final, mas foi a 1 coisa q eu fiz)
print(f'Gostosura: {gostosura}') 

if gostosura < 0:
    print('Nem o Grinch teria Coragem de provar esse Biscoito!')
elif gostosura == 0:
    if total_enfeites == 0:
        print('A Magia do Biscoito se Anulou.')
    else:
        print('Tanta Decoração para nada! A Magia do Biscoito se Anulou.')
else:
    #gostosura positiva
    if qtd_P > 0 and qtd_F > 0 and qtd_E > 0 and qtd_A > 0:
        print('Um Pedaço de cada Encanto Natalino! Esse vai para o Papai Noel! 🎅')
    elif qtd_F > (qtd_P + qtd_E + qtd_A):
        print('Gostoso e Congelante! Sirva com uma Caneca de Chocolate Quente! ❄️')
    elif qtd_A > 0 and qtd_F == 0:
        print('Uma Floresta de gostosura! As Renas vão Adorar! 🎄')
    else:
        print('Receita Aprovada! Já pode colocar ao lado do Copo de Leite! 🥛')