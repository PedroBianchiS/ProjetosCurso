#atributos de personagem; físicos e mentais

atributosFis = {
    'força': 0,
    'destreza': 0,
    'percepção': 0,
    'constituição': 0,
}
atributosMen = {
    'presenca': 0,
    'labia': 0,
    'inteligencia': 0,
    'espirito': 0,
}

#Definição de Atributos

print('Posicione os numeros 6, 5, 5, 4, 4, 3, 3 e 2 entre os Atributos como desejar.')
atributosFis['força'] = int(input('Força: '))
print(atributosFis['força'])
atributosFis['desrteza'] = int(input('Destreza: '))
print(atributosFis['desrteza'])
atributosFis['percepção'] = int(input('Percepção: '))
print(atributosFis['percepção'])
atributosFis['constituição'] = int(input('constituição: '))
print(atributosFis['constituição'])