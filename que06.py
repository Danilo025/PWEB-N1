numero = int(input("Digite um numero: "))

for i in range (1, 11):
    aux = i * numero

    print("{} X {} = {}". format(numero, i, aux))
    i = i + 1