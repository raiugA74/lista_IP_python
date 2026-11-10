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
