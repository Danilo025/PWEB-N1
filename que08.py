listranum = []

for numero in range (1, 6):
    listranum.append(int(input(f"Digite o {numero}° valor da sua listra: ")))

maior = max(listranum)
menor = min(listranum)

print(f"\nOs numeros digitados foi: {listranum}")
print(f"\nO maior numero da sua listra é {maior}")
print(f"\nO menor numero da sua listra é {menor}")



