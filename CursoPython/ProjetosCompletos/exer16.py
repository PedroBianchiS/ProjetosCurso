""" 16 - Faça um algoritmo que leia três valores que representam os três lados de um triângulo e verifique se são válidos, determine se o triângulo é equilátero, isósceles ou escaleno. """

def tipoTriangulo(l1, l2, l3):
    if l1 == l2 == l3:
        print('Equilátero')
    elif l1 == l2 != l3 or l1 != l2 == l3 or l1 == l3 != l2:
        print('Isósceles') 
    else:
        print('Escaleno')

l1 = int(input('1º Lado: '))
l2 = int(input('2º Lado: '))
l3 = int(input('3º Lado: '))

tipoTriangulo(l1, l2, l3)