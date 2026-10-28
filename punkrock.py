perigo = 0
timer = 0
morto = False
tem_ovo = False
enfrentou_troia = False
achou_portal = False
tem_camas = False
tem_ouro = False
tem_ferro = False

print("Byte: Au! Vou conseguir esse ovo!!") #1 FASE

string_fase1 = str(input())

timer += len(string_fase1) * 5

if string_fase1.isupper():
  perigo += 30
else:
  perigo += 10

str_lower = string_fase1.lower()

if "monstros" in str_lower:
  print("Você não pode dormir agora, há monstros por perto.")
  perigo += 25
  timer += 20
  if "4" in str_lower:
    print("Byte desbloqueou a conquista: [Caçador de Monstros]")
    perigo *= 2

tem_ferro = "ferro" in str_lower
if "ferro" in str_lower:
  print("Byte desbloqueou a conquista: [A Idade do Ferro]")
  perigo -= 15
  timer += 5

if "diamante" in str_lower:
   if tem_ferro:
     print("Byte desbloqueou a conquista: [Diamantes!]")
     perigo -= 40
   else:
     timer += 15

if "ouro" in str_lower:
    if tem_ferro:
       tem_ouro = True
       timer += 10
    else:
       timer += 5

if "estrutura" in str_lower:
  estrutura = str(input()).lower()

  if "vila" in estrutura:
    tem_camas = True
    timer += 10
    print("Byte desbloqueou a conquista: [Negócio Fechado!]")

  if "portal" in estrutura:
    achou_portal = True

  if "templo" in estrutura:
    perigo += 100

  if "mansao" in estrutura:
    if perigo > 100:
      print("Byte desbloqueou a conquista: [À beira da Morte]")
    perigo -= 150
    timer += 40
    

  if  "camara" in estrutura:
    timer += 60
    perigo += 50
    print("Byte desbloqueou a conquista: [Minecraft: Jogos Vorazes]")

perigo = max(0, perigo)

if perigo > 100:
  morto = True

else:
  print(f"Byte: Ufa, finalmente acabei, demorei apenas {timer} minutos, vamos ao Nether!") 

if not morto: #2 FASE
  if not achou_portal:
    print("Byte desbloqueou a conquista: [Entrando numa fria]")
    timer += 5

  perigo += 30
  print("Byte desbloqueou a conquista: [O buraco é mais embaixo]")

  n1 = float(input())
  n2 = float(input())

  soma = n1 + n2
  if soma != int(soma):
    if tem_ouro:
      print("Byte desbloqueou a conquista: [Meu precioso!]")
      perigo += 10
    else:
      perigo += 20
      timer += 30 

  resultado_blaze = str(input())
  if resultado_blaze.isnumeric():
    blaze = int(resultado_blaze)
    if 0 < blaze <= 12:
      timer += 20

    elif blaze > 12:
      timer += 10

    else:
      timer += 30
      perigo += 40

  else:
    timer += 30
    perigo += 40


  perigo = max(0, perigo)
  if perigo > 100:
    morto = True


if not morto: #3 FASE
  perigo -= 20
  perigo = max(0, perigo)

  x = int(input())
  z = int(input())

  d = ((100 - x)**2 + (200 - z)**2)**(1/2)

  distancia = int(d)
  print(f"Byte: Estou a {distancia} blocos da Stronghold!")

  timer += distancia * 2

  perigo += 30
  
  if timer > 300:
      print("Troia desbloqueou a conquista: [Liberte o End]")
      print("Byte desbloqueou a conquista: [É o fim?]")
      tem_ovo = False
      enfrentou_troia = True
  else:
      if tem_camas:
          print("Byte desbloqueou a conquista: [É o fim?]")
          print("Byte: Como eu amo o [Design Intencional do Jogo]!")
          perigo -= 30
          perigo = max(0, perigo)
          tem_ovo = True
  

      elif 180 < timer <= 300:
          enfrentou_troia = True
          print("Troia desbloqueou a conquista: [É o fim?]")
          print("Byte desbloqueou a conquista: [É o fim?]")
          perigo += 10
          n_flechas = int(input())
          n_alvos = int(input())

          if n_alvos == 1 and n_flechas == 1:
              print("Byte: Uma flecha, Uma chance.")
          elif n_alvos == 1:
              print("Byte: Troia já destruiu todos os cristais, agora é só o Dragão...")
  
          if (n_flechas / n_alvos) == (n_flechas // n_alvos) and (n_flechas // n_alvos) > 0:
              timer += 10
              print("Byte desbloqueou a conquista: [Liberte o End]")
              tem_ovo = True

          else:
              print("Byte: Droga! Não tenha flechas suficientes, Troia vai ganhar...")
              timer += 20
              tem_ovo = False
      elif timer <= 180:
            timer += 5
            print("Byte desbloqueou a conquista: [É o fim?]")
            print("Byte desbloqueou a conquista: [Liberte o End]")
            tem_ovo = True

      perigo = max(0, perigo)
      if perigo > 100:
       morto = True
            
if tem_ovo and not morto:
  print("Byte desbloqueou a conquista: [A nova geração]")  
  print("Byte: Aauauau! O ovo é meu! que rolem os créditos!")
else:
    if morto:
        print("Byte foi morto.")
    
    print("Byte: auu.... Não consegui pegar o ovo...")

print()
print("🚨Avaliação de nível de perigo: ", end="")

if perigo == 100 or enfrentou_troia:
    print("Odisseia de Byte.")
elif perigo > 100:
    print("Letal.")
elif perigo < 30:
    print("Passeio no Parque.")
elif 30 <= perigo < 70:
    print("Jornada Complicada.")
elif 70 <= perigo < 100:
    print("Aventura Perigosa.")

print()
horas = timer // 60
minutos = timer % 60
print(f"Timer: {horas} h e {minutos} minutos")





#questão origem dos guardiões
hp_noel = 100
ataque_breu = 15
custo_total = 0.00
cabousse = False
custo_base = 10.00
continente = "" 
fator_continente = 1.00
fator_pais = 1.00
carvao = 0
presente = 0
streak_presente = 0
streak_carvao = 0
emboscada = False
pontuacao_correta = False
custo_local = 0.00
morreu_noel = False
vitoria = False
sobrecarga = False
nome_localidade = ""
crianca_ou_evento = ""
pontuacao = 0
deu_FIM = False


while(hp_noel > 0 and nome_localidade != "FIM" and not morreu_noel):
    nome_localidade = str(input())   
    custo_local = 0.00
    custo_base = 10.00
    
    
    if nome_localidade == "FIM":
        deu_FIM = True
        cabousse = True
    else:
            continente = str(input())
            if continente == "FIM":
                cabousse = True
            
            else:
                if continente == "Europa":
                    fator_continente = 1.00
                elif continente == "Oceania":
                    fator_continente = 2.00
                elif continente == "América":
                    fator_continente = 3.00
                elif continente == "África":
                    fator_continente = 4.00
                elif continente == "Ásia":
                    fator_continente = 5.00
                else:
                    fator_continente = 1.00
                pais = str(input())
                if pais == 'FIM':
                    cabousse = True
                else:
                    if pais == "Brasil":
                        fator_pais = 1.10
                    elif pais == 'EUA':
                        fator_pais = 1.15
                    elif pais == "China":
                        fator_pais = 1.20
                    elif pais == "Canadá":
                        fator_pais = 1.25
                    elif pais == "Rússia":
                        fator_pais = 1.30
                    else:
                        fator_pais = 1.00

                    
                    while(crianca_ou_evento != "FIM_LOCAL" and hp_noel > 0): 
                        crianca_ou_evento = str(input())
                        if custo_local > 100.0 and not sobrecarga:
                            print("O trenó está sobrecarregado pela magia! Custos base aumentados.")
                            sobrecarga = True
                        if crianca_ou_evento == "FIM_LOCAL":
                                cabouse = True
                        else:
                            if crianca_ou_evento != "Breu": 
                                pontuacao = int(input())
                                while(pontuacao > 100 or pontuacao < 0):
                                    print("Pontuação inválida, insira novamente.")
                                    pontuacao = int(input())
                                if sobrecarga:
                                    custo_base = 15.00
                                custo_local += custo_base * fator_pais * fator_continente
                                   
                                if pontuacao >= 70:
                                    print(f"{crianca_ou_evento} foi uma boa criança este ano e receberá um presente!")
                                    streak_presente += 1 
                                    streak_carvao = 0
                                    presente += 1
                                else:
                                    print(f"{crianca_ou_evento} não se comportou bem e receberá carvão.")
                                    streak_carvao += 1
                                    streak_presente = 0
                                    carvao += 1

                                if streak_presente == 3:
                                    print("A fé das crianças fortalece a magia! Noel recuperou 10 de HP.")
                                    hp_noel += 10 
                                    hp_noel = min(hp_noel,100)
                                    streak_presente = 0
                                elif streak_carvao == 3:
                                    ataque_breu += 5
                                    novo_dano_base_breu = ataque_breu
                                    print(f"O medo e a descrença alimentam as sombras... O dano de Breu aumentou para {novo_dano_base_breu}!")
                                    streak_carvao = 0
                            

                            else:
                                emboscada = True
                                hp_breu1 = 50
                                iniciativa = str(input())
                                if iniciativa == "Breu":
                                    print("Alerta! Breu atacou a entrega!")
                                    while(hp_breu1 > 0 and hp_noel > 0):
                                        acao = str(input())
                                        hp_noel -= ataque_breu
                                        if hp_noel > 0:
                                            acao = str(input())
                                            hp_breu1 -= 20
                                        if hp_breu1 <= 0 and hp_noel > 0:
                                            print("Noel repeliu a emboscada e as entregas continuam!") 
                                            vitoria = True
                                        elif hp_noel <= 0: 
                                            morreu_noel = True
                                else:
                                    print("Alerta! Breu atacou a entrega!")
                                    while(hp_breu1 > 0 and hp_noel > 0):
                                        acao = str(input())
                                        hp_breu1 -= 20
                                        if hp_breu1 > 0:
                                            acao = str(input())
                                            hp_noel -= ataque_breu
                                        if hp_breu1 <= 0 and hp_noel > 0:
                                            print("Noel repeliu a emboscada e as entregas continuam!")
                                            vitoria = True
                                        elif hp_noel <= 0: 
                                            morreu_noel = True
                        
                        if not morreu_noel and crianca_ou_evento == "FIM_LOCAL":
                                print(f"Localidade {nome_localidade} finalizada. Custo logístico: {custo_local:.2f}")
    crianca_ou_evento = ""                            
    custo_total += custo_local

if not morreu_noel:
    print(f"Noite concluída com sucesso! Presentes: {presente} | Carvão: {carvao}")
    print(f"Custo logístico total: {custo_total:.2f}")
    print(f"HP final do Noel: {hp_noel}")

elif morreu_noel:
    print("O HP de Noel chegou a zero! O Breu venceu a batalha... O Natal das crianças foi arruinado.")



#QUESTÃO DO MENTALISTA
smiley = False
red_john = False
achou_assinatura = False
assinatura_encontrada = False
asmiley = "Nao"
qtd_j = 0

numero_linhas_matriz_evidencia = 0
numero_colunas_matriz_evidencias = 0
matriz_evidencias = []

print('--- FASE 1: A VARREDURA ---')
print('Lisbon: Jane, focamos as buscas no quadrante delimitado.')

linhas = int(input()) 
matriz_cena = []

for i in range(linhas):
    add = input().split(', ')
    matriz_cena.append(add)

valores_coordenadas = input().split() #separarr nos espaços/receber os inteiros

#converter os pedaços para inteiros
l_inicio = int(valores_coordenadas[0])
l_fim = int(valores_coordenadas[1])
coluna_inicio = int(valores_coordenadas[2])
coluna_fim = int(valores_coordenadas[3])

sub_matriz = []
for i in range(l_inicio, l_fim):
    linha_cortada = matriz_cena[i][coluna_inicio:coluna_fim]
    sub_matriz.append(linha_cortada)

qtd_sangue = 0
qtd_arma = 0
for i in sub_matriz:
    print(i)
    for elemento in i:
        if elemento == "Sangue":
            qtd_sangue += 1
        if  elemento == "Arma":
            qtd_arma += 1
        if elemento == "Smiley":
            smiley = True
            asmiley = "Sim"
       
            
print(f'Evidencias encontradas: Sangue ({qtd_sangue}), Arma ({qtd_arma}). Smiley ({asmiley})')
print()


print('--- FASE 2: A MATRIZ DE EVIDÊNCIAS ---')
print('Patrick Jane: Às vezes, a verdade está escondida bem diante dos nossos olhos.')

ij = input().split()
numero_linhas_matriz_evidencias = (int(ij[0]))
numero_colunas_matriz_evidencias = (int(ij[1]))


for i in range(numero_linhas_matriz_evidencias):
    valores_texto = input().split() #receber a linha com os valores em str
    linha_convertida = [] #para converter em int

    for valor in valores_texto:
        numero = int(valor) #converto
        linha_convertida.append(numero)

    matriz_evidencias.append(linha_convertida) #add

t = int(input())

for i in range(numero_linhas_matriz_evidencias):
    for j in range(numero_colunas_matriz_evidencias):
        if matriz_evidencias[i][j] >= t:
            matriz_evidencias[i][j] = 1

        else:
            matriz_evidencias[i][j] = 0

for linha in matriz_evidencias:
    print(*linha)

#a caça da assinatura p fase 2
assinatura_rj = [
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

#fase 2
for i in range(numero_linhas_matriz_evidencias - 3 + 1): #assinatura ocupa 3 linhas e range exclusivo   
    for j in range(numero_colunas_matriz_evidencias - 5 + 1):
        achou_assinatura = True
        for linha_mini in range(3):
            for coluna_mini in range(5):
                if achou_assinatura == True: #meu Deus do céu
                    
                    elemento_assinatura = assinatura_rj[linha_mini][coluna_mini]
                    elemento_matriz = matriz_evidencias[i + linha_mini][j + coluna_mini]

                    if elemento_matriz != elemento_assinatura:
                        achou_assinatura = False

        if achou_assinatura == True:
            linha_rj = i
            coluna_rj = j
            assinatura_encontrada = True

if assinatura_encontrada:
    print('Patrick Jane: Eu conheço esse sorriso.')
    print('RED JOHN DEIXOU UMA ASSINATURA!')
    print(f'ASSINATURA ENCONTRADA EM [{linha_rj}][{coluna_rj}]')
    print()
else:
    print('Patrick Jane: Nada aqui parece familiar.')
    print()

if smiley or assinatura_encontrada:
    red_john = True

#3 fase

if red_john: #com rj
    indice = 0

    alfabeto = "abcdefghijklmnopqrstuvwxyz "

    numeros = [int(x) for x in input().split()]

    lista_letras = [alfabeto[(num // 2) % 27] if num % 2 == 0 else alfabeto[(num * 3 + 1) % 27] for num in numeros]

    mensagem = "".join(lista_letras)

    print('--- FASE 3: A MENSAGEM ---')
    print(f'Mensagem decodificada: "{mensagem}"')
    print('Jane: Ele acha que é mais esperto que eu. Nós vamos pegá-lo.')
    

else: #sem rj
    nota_cifrada = str(input())
    texto_invertido = nota_cifrada[::-1]#pegar tudin e inverter

    fatiamento = texto_invertido[::2] #fatiar nos pares

    mensagem_decodificada = ''
    for letra in fatiamento:
        if letra.isupper():
            mensagem_decodificada += letra.lower() #salvar minuscula
        elif letra.islower():
            mensagem_decodificada += letra.upper() # salvar a maiuscula
        else:
            mensagem_decodificada += letra #se for espaço ou simbolo

        if letra == "j" or letra == "J":
            qtd_j += 1

    

    print('--- FASE 3: O CÓDIGO ---')
    print('Patrick Jane: Vamos ver o que ele quis dizer dessa vez.')
    print('MENSAGEM DECODIFICADA!')
    print(f"Patrick Jane: '{mensagem_decodificada}'...")
    print('Patrick Jane: Esse caso acabou de dar uma reviravolta interessante.')
    print(f'Grau de Obsessão: {qtd_j} aparição(ões) da letra J na mensagem.')
    print('--- CASO ENCERRADO (por enquanto...) ---')

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