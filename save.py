def fatorial(n):
    if (n == 0):
        return 1
    else:
        return n * fatorial(n-1)

def mdc(a, b):
    if b == 0:
        return a #caso base
    else:             #resto
        return mdc(b, a % b) #passo recursivo, chama o mdc com (b, resto) euclides by nivan

def potencia(base, exp):
    if exp == 0:
        return 1  #caso base
    return base * potencia(base, exp - 1)  #passo recursivo

#entradas
valor_duendes = int(input())
valor_elfos = int(input())

#fatorial
prod_duendes = fatorial(valor_duendes) #produções
prod_elfos = fatorial(valor_elfos)

if prod_duendes > prod_elfos: 
    print("Os duendes se superaram dessa vez.")
elif prod_elfos > prod_duendes:
    print("É, os elfos tiveram um resultado melhor.")
else:   
    print("Ué, houve um empate.")

#MDC
tamanho_caixa = mdc(prod_duendes, prod_elfos)

if tamanho_caixa > 10:
    print("Caixas gigantes! O Papai Noel vai precisar de um guindaste para empacotar tudo.")
else:
    print("Caixas compactas e organizadas perfeitamente.")

#divisor de estabilidade
divisor_estabilidade = ((prod_duendes + prod_elfos) // 2) + tamanho_caixa

if divisor_estabilidade > 50:
    print("Atenção: O divisor de estabilidade está altíssimo!")
else:
    print("Divisor calculado com sucesso. A rampa está equilibrada.")

#verificação do lançamento
print("Calculando a inclinação geométrica do canhão...")

cateto1_sq = potencia(prod_duendes, 2)
cateto2_sq = potencia(prod_elfos, 2)
hipotenusa_geometrica = cateto1_sq + cateto2_sq

if hipotenusa_geometrica % divisor_estabilidade != 0:
    print("Lançamento autorizado!")
else:
    print("Lançamento não autorizado!")


