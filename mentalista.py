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