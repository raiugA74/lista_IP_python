print('========================================')
print('GDA - HERO DISPATCH SYSTEM')
print('========================================')
print('[ROBOT] Sistema de despacho iniciado.')
cabousse = False
#herois
qtd_herois = 0
heroi = []
nome_heroi = []
força = []
resistencia = []
velocidade = []
inteligencia = []
experiencia = []

#ameaças
ameaca = []
nome_ameaca = []
dificuldade = []
atributo_p = []


#cadastro herois
while(not cabousse):
    entrada = input() #[FIM] é diferente de 'FIM', separo no split depois
    if entrada == 'FIM': 
        cabousse = True
    else:#fazer a soma dos pontos e ordenar no bubblesort
        heroi = entrada.split(' - ')
        qtd_herois += 1
        nome_heroi.append(str(heroi[0]))
        força.append(int(heroi[1]))
        resistencia.append(int(heroi[2]))
        velocidade.append(int(heroi[3]))
        inteligencia.append(int(heroi[4]))
        experiencia.append(int(heroi[5]))


print(f'[ROBOT] {qtd_herois} heróis disponíveis.')


N = int(input())

while(N > 0):
    N -= 1
    print('========================================')
    print("NOVA AMEAÇA DETECTADA")
    print('========================================')

    ameaca = input().split(' - ')

    nome_ameaca = (str(ameaca[0]))
    dificuldade = (int(ameaca[1]))
    atributo_p = (str(ameaca[2]))

    print(f'AMEAÇA: {nome_ameaca}')
    print(f'NÍVEL DE DIFICULDADE: {dificuldade}')
    print(f'PRIORIDADE: {atributo_p}')
    
    nomes_rodada = []
    pontos_rodada = []
    prio_rodada = []
    id_rodada = [] #desempate

    for i in range(qtd_herois): #analisando cada heroi
        valor_prioridade = 0
        if atributo_p == 'Força':
            valor_prioridade = força[i]
        elif atributo_p == 'Resistência':
            valor_prioridade = resistencia[i]
        elif atributo_p == 'Velocidade':
            valor_prioridade = velocidade[i]
        elif atributo_p == 'Inteligência':
            valor_prioridade = inteligencia[i]
        elif atributo_p == 'Experiência':
            valor_prioridade = experiencia[i]

        soma_atributos = força[i] + resistencia[i] + velocidade[i] + inteligencia[i] + experiencia[i]
        pontuacao_final = soma_atributos + valor_prioridade

        nomes_rodada.append(nome_heroi[i])
        pontos_rodada.append(pontuacao_final)
        prio_rodada.append(valor_prioridade)
        id_rodada.append(i) #desempate


    print('[ROBOT] Analisando heróis disponíveis...')#alinhados com for para não repetir esses prints em cada heroi
    print('[ROBOT] Calculando compatibilidade...')
    print('[ROBOT] Análise concluída.')



    print('========================================')
    print('RANKING DE HERÓIS')
    print('========================================')
    #Jesus
    tamanho = len(pontos_rodada)

    for i in range(tamanho):
        for j in range(tamanho - 1 - i):
            precisa_trocar = False

            if pontos_rodada[j] < pontos_rodada[j+1]: #qm tem menos pontos vai p trás
                precisa_trocar = True

            elif pontos_rodada[j] == pontos_rodada[j+1]: #se empatar nos pontos tem a prioridade
                if prio_rodada[j] < prio_rodada[j+1]:
                    precisa_trocar = True

                elif prio_rodada[j] == prio_rodada[j+1]:#se empatar nos pontos vai p id
                        if id_rodada[j] > id_rodada[j+1]: # Maior ID significa que chegou depois, então vai pra trás
                            precisa_trocar = True

            
            if precisa_trocar == True: #a humilde troca

                tp1 = pontos_rodada[j]
                pontos_rodada[j] = pontos_rodada[j+1]
                pontos_rodada[j+1] = tp1

                tp2 = prio_rodada[j]
                prio_rodada[j] = prio_rodada[j+1]
                prio_rodada[j+1] = tp2

                tp3 = id_rodada[j]
                id_rodada[j] = id_rodada[j+1]
                id_rodada[j+1] = tp3

                tp4 = nomes_rodada[j]
                nomes_rodada[j] = nomes_rodada[j+1]
                nomes_rodada[j+1] = tp4


    for i in range(tamanho): #ranking
            print(f'{i+1}. {nomes_rodada[i]} - {pontos_rodada[i]} pontos')

    print('----------------------------------------')
    if dificuldade <= 30:
        classe_ameaca = 'SIMPLES'
        qtd_necessaria = 1

    elif dificuldade <= 70:
        classe_ameaca = 'MODERADA'
        qtd_necessaria = 2

    else:
        classe_ameaca = 'CRÍTICA'
        qtd_necessaria = 3

    print(f'[ROBOT] Ameaça {classe_ameaca}.')
    print(f'[ROBOT] {qtd_necessaria} herói(s) serão despachados.')

    if qtd_necessaria > qtd_herois:
        print('[ROBOT] ALERTA!')
        print(f'[ROBOT] São necessários {qtd_necessaria} heróis,')
        print(f'[ROBOT] mas apenas {qtd_herois} estão disponíveis.')
        print('[ROBOT] Despachando todos os heróis disponíveis.')
        qtd_enviada = qtd_herois

    else:
        print('[CECIL] Equipe selecionada para a missão.')
        qtd_enviada = qtd_necessaria

    print('EQUIPE DESPACHADA:')
    for i in range(qtd_enviada):
        print(f'> {nomes_rodada[i]}')
                    
    print('========================================')
