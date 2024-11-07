#atributos de personagem; físicos e mentais

atributosFis = {
    'Atributo1': 'Força', 'base': 0,
    'Atributo2': 'Destreza', 'base': 0,
    'Atributo3': 'Percepção', 'base': 0,
    'Atributo4': 'Costituição', 'base': 0
}
atributosMen = {
    'presenca': 0,
    'labia': 0,
    'inteligencia': 0,
    'sabedoria': 0,
}

#Definição de Atributos
pontAtr = [6, 5, 5, 4, 4, 3, 2]
print(f'Posicione um dos numeros {pontAtr} entre os Atributos como desejar.')

def definirAtrFis():
    for atr in atributosFis:
        atributosFis['base'] = int(input(f'{atributosFis[atr]}: '))

print(definirAtrFis())