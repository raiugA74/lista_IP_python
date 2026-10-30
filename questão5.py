def eh_primo(numero):
    primo = False
    if numero > 1:
        primo = True
        for i in range(2, numero):
            if numero % i == 0: #se ele tem divisores diferentes de 1 e ele mesmo
                primo = False

    return primo

def quad_perf(numero):
    quadrado = False
    if numero > 0:
        for i in range(1,10): #vai de 0 a 99..testar do 0 a 9 já que o 81 é o último quad perfeito 
            if i*i == numero:
                quadrado = True
    return quadrado

mago = {
	"nome": "Salazar",
	"inventario": { 
			"cajado" : {"tipo" : "arma", "poder" : 15},
			"grimorio" : {"tipo" : "utilidade", "poder" : 10},
	},
}
arma = ['cajado', 'machado grande', 'adaga', 'adaga dupla']
utilidade = ['grimorio', 'escudo de madeira', 'alaude', 'ferramentas de ladrao']
consumivel = ['pergaminho oculto', 'racao de viagem', 'pocao de cura','bomba de fumaca']

B ='Bardo'
G = 'Guerreiro'
L = 'Ladino'
M = 'Mago'

print('Boa noite a todos!! Sejam bem vindos ao reino de Cinland. A aventura será longa, mas a gloria é eterna!!')
print('Vamos as apresentações.\n')

quantidade_aventureiros = int(input())

while quantidade_aventureiros > 4 or quantidade_aventureiros < 1:
    print("Não tem toda essa gente pra jogar não.")
    quantidade_aventureiros = int(input()) #pedindo de novo no loop até acertar

#armazenar num grupo
grupo = []
qtd_av = quantidade_aventureiros
while qtd_av > 0:
    qtd_av -= 1
    dados_heroi = input().split() #ler a entrada e separar numa lista com o nome e a classe
    nome_heroi = dados_heroi[0] 
    letra_classe = dados_heroi[1]

    classe_completa = ''
    if letra_classe == 'M':
        classe_completa = M

    elif letra_classe == 'B':
        classe_completa = B

    elif letra_classe == 'L':
        classe_completa = L
    
    elif letra_classe == 'G':
        classe_completa = G

    aventureiro_atual = {
        "nome": nome_heroi,
        "classe": classe_completa,
        "inventario": {}
        }
    cabousse = False
    while not cabousse:
        entrada = input().split(' - ')
        if entrada[0] == 'pronto':
            cabousse = True
        else:#cifra de cesar
        #convertendo os números para int
            nome_criptografado = entrada[0]
            chave = int(entrada[1])
            poder = int(entrada[2])

            alfabeto = "abcdefghijklmnopqrstuvwxyz" #descriptografando a cifra
            nome_descriptografado = ""

            for letra in nome_criptografado:
                if letra == ' ':# se for espaço, adiciona o espaço direto e ignora a cifra  
                    nome_descriptografado += ' '

                else:
                    pos_atual = 0
                    for i in range(26): # alfabeto com 26 letras
                        if alfabeto[i] == letra:
                            pos_atual = i

                    
                    nova_pos = (pos_atual - chave) % 26 #subtrai a chave com o módulo 26
                    nome_descriptografado += alfabeto[nova_pos] # add a letra verdadeira na palavra final

            tipo_item = "" #descobrir o tipo do item
            if nome_descriptografado in arma:
                tipo_item = "arma"
            elif nome_descriptografado in utilidade:
                tipo_item = "utilidade"
            elif nome_descriptografado in consumivel:
                tipo_item = "consumivel"


            aventureiro_atual["inventario"][nome_descriptografado] = {"tipo": tipo_item, "poder": poder}
 # QUANDO DIGITA "pronto" SAI DO 'while not cabousse'  
    grupo.append(aventureiro_atual)
    #cabousse leitura e start da fase 1

for heroi in grupo:
    nome = heroi["nome"]
    classe = heroi["classe"]
    inventario = heroi["inventario"]

    #se o dicionario do inventario tiver sem nada
    if len(inventario) == 0:
        print(f"{nome} ({classe}): sem itens")    
    else:
        lista_formatada = []
        #se tiver itens..
        for nome_item, status in inventario.items():#.items() pega o nome do item e os status
            tipo = status['tipo']
            poder = status['poder']

            texto_item = f"{nome_item} [{tipo}, {poder}]"
            lista_formatada.append(texto_item)    

        # junta os itens tudo com vírgula e espaço
        itens_juntos = ", ".join(lista_formatada)
        print(f"{nome} ({classe}): {itens_juntos}")

print("Grupo completamente apresentado, espero que todos estejam preparados para o que estar por vir.")

#FASE 2 DUNGEON
print("\nAo passa pelo arco de pedras, vocês encontram um lugar silencioso, com um odor nada agradável e um frio sem igual. Um calafrio na espinha os chama a recuar, mas a jornada começa aqui. Bem vindos a Dungeon do Grad5.")
tamanho_matriz = int(input())
mapa = []

for _ in range(tamanho_matriz): #ler as linhas baseado no tamanho do input
    linha_str = input().split()#pegar cada numero e depois tenho que colocar em int, ja que no split vem tudo em str
    linha_int = []#fazer linha por linha direto, ja que o input vem todos os numeros da linha

    for numero in linha_str:#trasnforamr os numeros em int
        linha_int.append(int(numero))

    mapa.append(linha_int) #add a linha no mapa

# VARIÁVEIS DA DUNGEON
linha_atual = 0
coluna_atual = 0
chegou_na_saida = False
grupo_vivo = True #saber se deu game over

while not chegou_na_saida and grupo_vivo:
    valor_atual = mapa[linha_atual][coluna_atual] #posição por posição
 
    tipo_sala = "" #VERIFCAR O TIPO DA SALA ATUAL
    if valor_atual == 0:
        tipo_sala = "Entrada"
    elif valor_atual == 99:
        tipo_sala = "Saída"
    elif eh_primo(valor_atual):
        tipo_sala = "Armadilha"
    elif quad_perf(valor_atual):
        tipo_sala = "Looting"
    else:
        tipo_sala = "Sala Comum"
        
    print(f"Casa visitada: {tipo_sala}")

    # EVENTOS DAS SALAS (armadilha e loot)
    if tipo_sala == "Armadilha":
        tipo_armadilha = input().strip() # saber o tipo
        #procurar quem ta vivo no grupo e o índice
        idx_guerreiro = -1
        idx_bardo = -1
        idx_ladino = -1

        for i in range(len(grupo)): #analisar cada um
            if grupo[i]["classe"] == "Guerreiro":
                idx_guerreiro = i
            elif grupo[i]["classe"] == "Bardo":
                idx_bardo = i
            elif grupo[i]["classe"] == "Ladino":
                idx_ladino = i

        if tipo_armadilha == 'flechas': #guerreiro tá vivo(idx >= 0) e tem o escudo no inventário
            if idx_guerreiro != -1 and "escudo de madeira" in grupo[idx_guerreiro]["inventario"]:
                nome_guerreiro = grupo[idx_guerreiro]["nome"]
                print(f"O escudo de madeira de {nome_guerreiro} protegeu o grupo.")
                #tirar o escudo do inventário
                grupo[idx_guerreiro]["inventario"].pop("escudo de madeira") #usado

            else:
                morto = grupo[-1] 
                nome_morto = morto["nome"]
                print(f"{nome_morto} sacrificou-se pelo grupo.")
                foi_salvo = False # saber se foi salvo pela poção

                # se o bardo for o ultimo(o que morre e sacrifica) ele só falece mesmo, não pode SE curar
                if idx_bardo != -1 and "pocao de cura" in grupo[idx_bardo]["inventario"] and morto["classe"] != "Bardo":
                    nome_bardo = grupo[idx_bardo]["nome"]
                    print(f"{nome_bardo} usou a pocao de cura e salvou {nome_morto}.")
                    # tirar a poção
                    grupo[idx_bardo]["inventario"].pop("pocao de cura") #usado
                    foi_salvo = True

                if not foi_salvo:
                    grupo.pop() # tira o coitado da lista
                    
                    if len(grupo) == 0: # se todo mundo morreu
                        grupo_vivo = False

            #analisando SE MORREU TD MUNDO

        if tipo_armadilha == 'beholder':
            if idx_ladino != -1 and "bomba de fumaca" in grupo[idx_ladino]["inventario"]:
                nome_ladino = grupo[idx_ladino]["nome"]
                print(f'{nome_ladino} usou a bomba de fumaça e o escaparam do Beholder.') 
                grupo[idx_ladino]['inventario'].pop('bomba de fumaca') #usado, taquei a bomba

            else:
                grupo_vivo = False
                print(f'Entraram em uma sala que não deveriam. A ultima visão é tudo ficando vermelho e em um flash, tudo fica preto. Vocês tão mortos.')
                 
    if tipo_sala == 'Looting':
        print('Finalmente um descanso! Aproveitam as maravilhas presentes na sala.')

        # verifica se tem o ladino com ferramentas para ver se são 2 baús nesta sala
        tem_ladino_com_ferramentas = False
        for heroi in grupo:
            if heroi["classe"] == "Ladino" and "ferramentas de ladrao" in heroi["inventario"]:
                print(f"{heroi['nome']} arrombou o baú trancado!")
                heroi["inventario"].pop("ferramentas de ladrao")
                tem_ladino_com_ferramentas = True

        # Qtd de loots nesta sala específica
        qtd_loots = 1
        if tem_ladino_com_ferramentas:
            qtd_loots = 2

        letras_vivos = []
        for heroi in grupo:
            letras_vivos.append(heroi['classe'][0])

        letras_vivos.sort()  

        loop_loot = 0 
        while loop_loot < qtd_loots:
            entrada_loot = input().split(' - ')
            nome_item_esp = entrada_loot[0]
            cod_inv = int(entrada_loot[1]) 

            modulo = len(letras_vivos) 
            indice_sorteado = cod_inv % modulo
            letra_ganhadora = letras_vivos[indice_sorteado]

            heroi_sortudo = {}
            for heroi in grupo:
                if heroi["classe"][0] == letra_ganhadora:
                    heroi_sortudo = heroi
            print(f"{nome_item_esp} foi para {heroi_sortudo['nome']} ({heroi_sortudo['classe']}).")

            # AUMENTANDO O PODER DOS ITENS DO HERÓI SORTUDO
            classe_sortudo = heroi_sortudo['classe']
            eh_ideal = False

            if nome_item_esp == 'lira encantada' and classe_sortudo == 'Bardo':
                eh_ideal = True
            elif nome_item_esp == 'martelo do trovao' and classe_sortudo == 'Guerreiro':
                eh_ideal = True 
            elif nome_item_esp == 'olho do abismo' and classe_sortudo == 'Ladino':
                eh_ideal = True
            elif nome_item_esp == 'orbe arcano' and classe_sortudo == 'Mago':
                eh_ideal = True

            if eh_ideal:
                print("O poder que esta em suas mãos é grandioso e parece chamar-lhe a glória eterna.")
                for nome_item in heroi_sortudo["inventario"]:
                    heroi_sortudo["inventario"][nome_item]["poder"] *= 2
            else:
                print("O poder é grande demais, você não consegue extrair o máximo dele.")
                for nome_item in heroi_sortudo["inventario"]:
                    heroi_sortudo["inventario"][nome_item]["poder"] = int(heroi_sortudo["inventario"][nome_item]["poder"] * 1.25)
            
            loop_loot += 1

    if valor_atual == 99: #SE NÃO FOR SAÍDA
        chegou_na_saida = True
        print("Vocês finalmente saem das cavernas escuras e frias. Mas não parece chegar em um lugar melhor.")

    else: #limites do mapa
        limite = tamanho_matriz - 1
        maior_valor_vizinho = -1 # para mudar de lugar, ja que o menor é 0, para mudar coloco -1

        prox_linha = linha_atual
        prox_coluna = coluna_atual

        #MOVIMENTAÇÃO   
        if linha_atual > 0: #IR P CIMA, TEM Q SER MAIOR QUE 0, JA QUE POSIÇÃO INICIAL É 0
            valor_cima = mapa[linha_atual - 1][coluna_atual] #POSIÇÃO DE CIMA
            if valor_cima > maior_valor_vizinho:
                maior_valor_vizinho = valor_cima
                prox_linha = linha_atual - 1
                prox_coluna = coluna_atual 

        if  linha_atual < limite: #IR P BAIXO
            valor_baixo = mapa[linha_atual + 1][coluna_atual] #POSIÇÃO DE BAIXO, VALOR
            if valor_baixo > maior_valor_vizinho:
                maior_valor_vizinho = valor_baixo
                prox_linha = linha_atual + 1
                prox_coluna = coluna_atual

        if coluna_atual > 0: #IR P ESQUERDA, COMEÇAMOS NA PONTA ESUQERDA, NÃO TEM COMO IR MAIS P ESQUERDA SE ESTIVERMOS NO 0
            valor_esq = mapa[linha_atual][coluna_atual - 1] #POSIÇÃO DA ESQ
            if valor_esq > maior_valor_vizinho:
                maior_valor_vizinho = valor_esq
                prox_linha = linha_atual
                prox_coluna = coluna_atual - 1

        if coluna_atual < limite: #IR P DIREITA
            valor_dir = mapa[linha_atual][coluna_atual + 1] #POSIÇÃO DA DERECHA
            if valor_dir > maior_valor_vizinho:
                maior_valor_vizinho = valor_dir
                prox_linha = linha_atual
                prox_coluna = coluna_atual + 1

        mapa[linha_atual][coluna_atual] = -1
        linha_atual = prox_linha
        coluna_atual = prox_coluna

#FASE 3 MEU DEUS DO CEEEEEEEEEU
if not grupo_vivo:
    print("Os sonhos e objetivos de todos são deixados no chão do Grad5. Nenhum de vocês restou. A glória nunca será alcançada!")
else:
    print("\nO lugar é silencioso. Até que, de repente, um rugido é ouvido. Uma criatura surge das sombras: o temido TarraByte!")       
    ficha_boss = input().split() # ler ficha do boss
    hp_boss = int(ficha_boss[0])
    ca_boss = int(ficha_boss[1])

    #ler os dados dos aventureiros que sobreviveram
    for heroi in grupo:
        dados_rolagem = input().split()
        #add a rolagem no dicionario p usar na luta, meu Deus muito RPG, sou fã
        heroi["iniciativa"] = int(dados_rolagem[0])
        heroi["dado_ataque"] = int(dados_rolagem[1])
    #testar essa função lambda, pega cada heroi e organiza
    grupo.sort(key=lambda heroi: heroi["iniciativa"], reverse=True) #ordenando do maior p menor

    # Imprimir a ordem de iniciativa:
    nomes_iniciativa = []
    for heroi in grupo:
        nomes_iniciativa.append(heroi["nome"])

    ordem_str = ", ".join(nomes_iniciativa)
    print(f"Ordem de iniciativa: {ordem_str}")
    #TRETA E COMBATE PAPAE
    buff_bardo = 0 # bardo começa sem tocar música
    boss_derrotado_por = ""
    for heroi in grupo:
        # tudo só acontece SE o boss ainda tiver vivo
        if hp_boss > 0:
            nome = heroi["nome"]
            classe = heroi["classe"]
            inventario = heroi["inventario"]
            dado_ataque = heroi["dado_ataque"]
            
            # AÇÃO ESPECIAL DO BARDO
            if classe == "Bardo" and "alaude" in inventario:
                print(f"{nome} inspirou o grupo.")
                buff_bardo = 2

            else:
                # PROCURAR A ARMA MAIS FORTE E CONSUMILVEL
                poder_arma = 0
                poder_consumivel = 0
                
                for nome_item, status in inventario.items():
                    if status["tipo"] == "arma":
                        if status["poder"] > poder_arma:
                            poder_arma = status["poder"]
                            
                    elif status["tipo"] == "consumivel":
                        if classe == "Mago" and nome_item == "pergaminho oculto":
                            poder_consumivel = status["poder"]
                        elif classe == "Guerreiro" and nome_item == "racao de viagem":
                            poder_consumivel = status["poder"]

                bonus_ataque = 0
                if classe == "Guerreiro" or classe == "Ladino":
                    bonus_ataque = buff_bardo
                    
                valor_ataque_total = dado_ataque + bonus_ataque

                # acerto crítico (20 natural)
                if dado_ataque == 20:
                    dano_total = (poder_arma + poder_consumivel) * 2
                    hp_boss -= dano_total
                    print(f"{nome} acertou um critico e causou {dano_total} de dano.")
                    
                    if hp_boss <= 0 and boss_derrotado_por == "":
                        boss_morreu = True
                        boss_derrotado_por = nome

                # acerto normal na CA do boss
                elif valor_ataque_total >= ca_boss:
                    dano_total = poder_arma + poder_consumivel
                    hp_boss -= dano_total
                    print(f"{nome} acertou e causou {dano_total} de dano.")
                    
                    if hp_boss <= 0 and boss_derrotado_por == "":
                        boss_morreu = True
                        boss_derrotado_por = nome

                else:
                    print(f'{nome} errou o ataque.')

    if hp_boss <= 0:
            print(f"O TarraByte foi derrotado por {boss_derrotado_por}!")
    else:
        print(f"O TarraByte sobreviveu com {hp_boss} de HP e obliterou o grupo. Fim da aventura.")