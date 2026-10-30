#questão de FUNÇÕES ZAGREW
print('O portão se abre diante de você, revelando o caminho para o Submundo. Uma nova tentativa começa agora.\n')
inventário_bencaos = []


def bencaos(lista_bencaos_atual):
    
    combinadas = []
    deuses = ['AFRODITE' ,'ARES','ARTEMIS','ATENA','DEMETER','DIONISIO','HERMES','POSEIDON','ZEUS']
    cabousse = False
    while (not cabousse): 
      deus = input()
      if deus.lower() == 'parar':
        cabousse = True
        print()
      elif deus == 'COMBINADA':
        combinada1 = input()
        combinada2 = input()
        if combinada1 not in deuses or combinada2 not in deuses: 
            print('Zagreu: Uma Bênção Combinada assim? Acho que você está brincando comigo.')

        elif combinada1 not in lista_bencaos_atual or combinada2 not in lista_bencaos_atual:
            print('Zagreu: Eu ainda não tenho nenhuma Bênção desse(a) Deus(a), não posso combiná-la')

        elif combinada1 == combinada2:
            print('Zagreu: Os dois Deuses precisam diferentes para realizar uma Bênção Combinada...')

        elif combinada1.lower() == 'hermes' or combinada2.lower() == 'hermes':
            print('Zagreu: Uma Bênção Combinada com Hermes? Acho que ele é competitivo demais pra cooperar com os outros.')

        else:
            print(f'Zagreu foi abençoado por uma Bênção Combinada de {combinada1} e {combinada2}.')
            lista_bencaos_atual.append('combinada') #para adicionar na quantidade no len
        
        
      else:
        if deus in deuses:
            print(f'Zagreu obteve uma Bênção de {deus}.')
            lista_bencaos_atual.append(deus)
        else:
            print(f'Zagreu: Ah, claro. A Bênção de {deus}. Como pude esquecer? Tenho certeza de que meu pai também deve ter esquecido de mencioná-lo(a)... Você está brincando comigo não é?.')
       
        
    qtd_bencaos = len(lista_bencaos_atual)

    return qtd_bencaos, lista_bencaos_atual


def tartaro(inventario):
 
 prisioneiros = input().split(', ')
 tamanho = len(prisioneiros)
 #burocracia/bubblesort
 for i in range(tamanho):
        for j in range(tamanho - 1):
            if prisioneiros[j] > prisioneiros[j + 1]:
                # p trocar de lugar
                prisioneiros[j], prisioneiros[j + 1] = prisioneiros[j + 1], prisioneiros[j]

    # print do evento especial formatado
 lista_formatada = ", ".join(prisioneiros)
 print(f'Zagreu: Aqui está sua papelada: {lista_formatada}\n')
         
 
 
 qtd_bencaos, inventario = bencaos(inventario) #bençãos
 if qtd_bencaos >= 3:
   venceu1 = True


 else:
   venceu1 = False 
   print('Zagreu cai, derrotado mais uma vez. Seu corpo se desfaz, retornando ao lugar que conhece tão bem.')


 return venceu1, inventario

def asfodelo(inventario):
    matriz1 = []
    matriz2 = []
    matriz3 = []
    venceu2 = False
       #receber 2 matrizes
    for n in range(3):
         linha = []
         elementos_texto = input().split() #p receber os dados
         for texto in elementos_texto:
             num = int(texto)
             linha.append(num)

         matriz1.append(linha)

    for n in range(3):
          linha1 = []
          elementos_texto = input().split()
          for texto in elementos_texto:
              num = int(texto)
              linha1.append(num)
          matriz2.append(linha1)
       
    for i in range(3):
        matriz3.append([0, 0, 0])

    for i in range(3): #linhas da matriz1
        for j in range(3): #colunas da matriz2
            soma = 0
            for k in range(3): #multiplicação
                r = matriz1[i][k] * matriz2[k][j]
                soma += r
           
            matriz3[i][j] = soma

    maior_valor = matriz3[0][0]
    linha_maior = 0
    coluna_maior = 0
    for i in range(3):
        for j in range(3):
            if matriz3[i][j] > maior_valor:
                maior_valor = matriz3[i][j]
                linha_maior = i
                coluna_maior = j

    print(f'Zagreu: devo lançar minha vara de pesca nesse ponto: ({linha_maior}, {coluna_maior})\n')

    qtd_bencaos, inventario = bencaos(inventario) #bençãos
    if qtd_bencaos >= 6:
       venceu2 = True
    else:
        venceu2 = False
        print('Zagreu cai, derrotado mais uma vez. Seu corpo se desfaz, retornando ao lugar que conhece tão bem.')

    return venceu2, inventario


def elisio(inventario):
    legado = 0
    qtd_legado = 0
    while legado < 200:
       receber_legado_titulo = input().split(' O ')
       nome_heroi = receber_legado_titulo[0]
       titulo = receber_legado_titulo[1]

       if 'Hércules' == nome_heroi:
        qtd_legado = 50
       elif 'Aquiles' == nome_heroi:
        qtd_legado = 40
       elif 'Odisseu' == nome_heroi:
        qtd_legado = 35
       else:
        qtd_legado = 20
       

       if 'Imortal' == titulo:
            qtd_legado *= 1.5
       elif 'Forte' == titulo:
            qtd_legado *= 1.2
       elif 'Grande' == titulo:
            qtd_legado += 15
       else:
            qtd_legado += 10

       print(f'O Herói: {nome_heroi} O {titulo} adicionou {qtd_legado} pontos de Legado.')
       legado += qtd_legado     

    print('Zagreu: Acho que já fizemos história o suficiente por hoje.\n')

    qtd_bencaos, inventario = bencaos(inventario) #bençãos
    if qtd_bencaos >= 9:
        venceu3 = True

    else:
      venceu3 = False
      print('Zagreu cai, derrotado mais uma vez. Seu corpo se desfaz, retornando ao lugar que conhece tão bem.')
    return venceu3, inventario


def estige():
 fase2 = False
 print('O Templo de Estige... o último obstáculo entre você e a superfície.\n')
 hp_zagreu = 100
 atq_zagreu = 20
 atq_especial_zagreu = 40


 hp_hades = 200
 atq_hades = 15
 seq_ataques = 0
 atq_especial_hades = 50
 
 while hp_hades > 0 and hp_zagreu > 0:
     if seq_ataques == 2: #seria depois do 2 e antes do 3
            print("Zagreu: Meu pai parece estar carregando um forte ataque, é melhor desviar!")

     acao = input()

     #TURNO ZAGREW
     if acao == 'ATACAR':
         print(f"Zagreu golpeia Hades, causando {atq_zagreu} de dano.")
         hp_hades -= atq_zagreu

        
     elif acao == 'ATAQUE ESPECIAL':
         print(f"Zagreu golpeia Hades com um ataque especial, causando {atq_especial_zagreu} de dano.")
         hp_hades -= atq_especial_zagreu

         
     elif acao == 'ESQUIVA':
         print("Zagreu esquiva do ataque de Hades, evitando o dano.")

#turno HADES
     if hp_hades <= 100 and not fase2 and hp_hades > 0:
            fase2 = True
            print("\nHades: Chega! Isso acaba agora!\n")
            atq_hades = 25 #para mudar o ataque do hades e não precisar criar outra variavel p o ataque v2
            atq_especial_hades = 100    

     if hp_hades > 0:
            seq_ataques += 1
            
            if seq_ataques == 3:
                # ataque Fortalecido
                if acao != 'ESQUIVA':
                    print("Hades: Desapareça!")
                    print(f"Hades causou {atq_especial_hades} de dano em Zagreu.")
                    hp_zagreu -= atq_especial_hades  # subtrai o HP de Zagreu
                seq_ataques = 0
            else:
                # ataque Normal
                if acao != 'ESQUIVA':
                    print(f"Hades causou {atq_hades} de dano em Zagreu.")
                    hp_zagreu -= atq_hades  # subtrai o HP de Zagreu
                    
         
         
     if seq_ataques == 3:
         seq_ataques = 0

 print()
 if hp_zagreu > 0:
     print('O senhor do Submundo cai diante de Zagreu. Pela primeira vez, não há nada entre ele e a superfície.')
     print('O portão se abre diante de você.')
     print('Zagreu finalmente deixa o Submundo para trás e sente o calor do sol tocar seu rosto. Pela primeira vez, a superfície está diante de seus olhos.')
     print('Você conseguiu escapar. A tentativa foi concluída.')

     venceu4 = True    

 else:
     print('Zagreu: Me desculpe, mãe. Foi tão perto...')
     venceu4 = False
 
 return venceu4


venceu1 = False
venceu2 = False
venceu3 = False
venceu4 = False

# COMEÇA O JOGO
inventario_bencaos = []

# TÁRTARO
venceu1, inventario_bencaos = tartaro(inventario_bencaos)

if venceu1:
    # ASFÓDELO 
    venceu2, inventario_bencaos = asfodelo(inventario_bencaos) 
    
    if venceu2:
        # ELÍSIO
        venceu3, inventario_bencaos = elisio(inventario_bencaos)
        
        if venceu3:
            #  ESTIGE (CHEFÃO)
            # estige não tem bênçãos, então não precisa do inventário
            venceu4 = estige()