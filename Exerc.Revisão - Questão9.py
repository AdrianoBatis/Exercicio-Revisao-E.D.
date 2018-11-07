nomeVeiculo = []
kms = []
km = 0
for c in range(5):
    print(f"\nVeiculo {c + 1}")
    nomeVeiculo.append(input("Nome do veiculo: "))
    km = float(input("KMs por litro: "))
    kms.append(km)

print("\nRelatorio Final")
menor = 0
nme = ' '
for c,d in enumerate(nomeVeiculo):
    print(f"{c + 1}\t -\t{d}\t - \t{kms[c]} -\t{1000 / kms[c]:.2f}\t -\t{1000 / kms[c] * 2.25:.2f}")
    if kms[c] > menor:
        menor = kms[c]
        nme = nomeVeiculo[c]

print(f"\nO menor consumo e do {nme}\n")
