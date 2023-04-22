listranum = []

for numero in range (1, 6):
    listranum.append(int(input(f"Digite o {numero}° valor da sua listra: ")))

soma = sum(listranum)

media = soma / numero


print(f"\nOs numeros digitados foi: {listranum}")
print(f"\nA soma da sua listra é {soma}")
print(f"\nA media da sua listra é {media}")
