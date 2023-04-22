numeros = []
valor = 0

for cont in range (1, 6):
    valor = int(input(f"Didite o {cont}° valor da listra: "))
    numeros.append(valor)

soma = sum(numeros)

print(f"\nOs numeros da sua listra são: {numeros}\n")
print(f"A soma da listra é ingual a: {soma}\n")