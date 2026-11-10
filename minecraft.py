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