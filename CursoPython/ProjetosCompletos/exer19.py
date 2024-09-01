tabuadas = []

for i in range(1, 11):
    tabuadas.append(i)

for num in tabuadas:
    print(f'Tabuada do {num}:')
    for tabuada in tabuadas:
        print(num * tabuada)