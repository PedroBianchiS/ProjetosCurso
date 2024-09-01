valor = int(input('Digite o valor para saber sua tabuada: '))
tabuada = []

for i in range(1, 11):
    tabuada.append(i)

for num in tabuada:
    print(valor * num)