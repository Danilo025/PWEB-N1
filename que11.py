numeros = [[], []]
valor = 0

for cont in range (1, 6):
    valor =int(input(f"Digite o {cont}° numero: "))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print(f"Os numeros impares são {numeros[1]}")