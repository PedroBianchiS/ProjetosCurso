""" Francisco tem 1,50m e cresce 2 centímetros por ano, enquanto Sara tem 1,10m e cresce 3 centímetros por ano. 
Faça um algoritmo que calcule e imprima na tela em quantos anos serão necessários para que Sara seja maior que Francisco """

fran = 1.50
sara = 1.10
anos = []

for i in range(1, 81):
    anos.append(i)
    i += 1

for ano in anos:
    fran += 0.02
    sara += 0.03
    if sara > fran:
        break

print(f'Sara será maior que Franciso em {ano} anos, quando ela terá {sara:.2f} e Francisco terá {fran:.2f}')