numeros = []
valor = 0

for cont in range (1, 6):
    valor = int(input(f"Insira o {cont}° numero: "))

    numeros.append(valor)

print(f"\nListra em ordem crescente: {sorted(numeros)}\n")
