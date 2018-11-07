a = 1
Lista = []
while(1):
	coisa = int(input('Lista Eterna de Numeros - Coisas ' + str(a) + ': '))
	a += 1
	if(coisa == -1):
		print('Até que fim')
		break
	else:
		lista.append(coisa)

print(Lista)
