

listra = []
numeros = 0
x = 0

print("\nCrie um listra com 5 valores.")

for cont in range (1,6):
    numeros = int(input(f"Digite o {cont}° valor da sua listra: "))
    listra.append(numeros)

print(f"\nSua listra é {listra}.\n")

x = int(input("Digite o valor que deseja encontrar na listra: "))

if x in listra:
    print(f"\nO numero {x} está na listra.\n")
    
else:
    print("\nEsse numero não existe na listra.\n")
    


    

