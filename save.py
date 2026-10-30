def combinacoes(n, k):
    # casos basee 
    if k == 0 or k == n: 
        return 1 #combinação para k=0 será 1, mesma coisa para k=n, ideia do triangulo de pascal, por isso suas pontas são 1, de inicio (n 0) 
    elif k > n or k < 0: 
        return 0 #combinação para qualquer k>0 ou k sendo negativo...será 0 o resultado
    else:
    # relação recursiva de Stifel
        return combinacoes(n - 1, k - 1) + combinacoes(n - 1, k)

qtd_setores = int(input()) #leitura
minimo_possibilidades = int(input())
resultados = []

for _ in range(qtd_setores): #leitura dos setores e processamemnto
    n = int(input())
    k = int(input())

    possibilidades = combinacoes(n, k) #fzr a combinação, conjuntos, tanto que no texto fala que a ordem não importa, estrela e sino = sino e estrela
    resultados.append(possibilidades)   

print("Relatório dos escudos de Norte:")
aprovados = 0

for i in range(len(resultados)): #percorrer a lista de resultados p acompanhar o numero do setor
    possibilidades = resultados[i]
    numero_setor = i + 1

    if possibilidades >= minimo_possibilidades:
        print(f"Setor {numero_setor}: {possibilidades} possibilidade(s). Variedade suficiente!")
        aprovados += 1
    else:
        print(f"Setor {numero_setor}: {possibilidades} possibilidade(s). Precisa de mais alternativas!")

#resumo final
print(f'Setores que atingiram a meta: {aprovados} de {qtd_setores}.')
if aprovados == qtd_setores:
    print('Tudo pronto! O planejamento dos escudos foi aprovado!')
else:
    print('Norte precisa revisar o planejamento!')