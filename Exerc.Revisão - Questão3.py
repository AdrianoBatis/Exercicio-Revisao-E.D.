pergunta1 = str(input("Telefonou para a vítima?"))
pergunta2 = str(input("Esteve no local do crime?"))
pergunta3 = str(input("Mora perto da vítima?"))
pergunta4 = str(input("Devia para a vítima?"))
pergunta5 = str(input("Já trabalhou com a vítima?"))

cont = 0

if pergunta1 == 'sim' or pergunta1 == 'nao':
  cont +=1

if pergunta2 == 'sim' or pergunta1 == 'nao':
  cont +=1

if pergunta3 == 'sim' or pergunta1 == 'nao':
  cont +=1

if pergunta4 == 'sim' or pergunta1 == 'nao':
  cont +=1

if pergunta5 == 'sim'or pergunta1 == 'nao':
  cont +=1

if cont == 2:
  print("Suspeita")

elif cont == 3 or cont == 4:
  print("Cúmplice")

elif cont == 5:
  print("Assassino")

else:
  print("Inocente")
