n = int(input("Digite um numero: "))
ultimo = 1
penultimo = 1

if n == 1 or n == 2 :
    print ("1")
else:
    for contador in range (1, n):
        aux = ultimo + penultimo
        penultimo = ultimo
        ultimo = aux

        contador += 1

        print(aux)