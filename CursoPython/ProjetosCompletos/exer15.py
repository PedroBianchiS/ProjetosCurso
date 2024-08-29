""" Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na tela quantos anos, 
meses e dias essa pessoa ja viveu. Leve em consideração o ano com 365 dias e o mês com 30 dias.

(Ex: 5 anos, 2 meses e 15 dias de vida) """
from datetime import datetime

def calcularVida(anoNascimento, mesNascimento, diaNascimento):
    dataAtual = datetime.now()
    dataNascimento = datetime(anoNascimento, mesNascimento, diaNascimento)
    diasVividos = (dataAtual - dataNascimento).days
    
    anosVividos = diasVividos // 365
    diasRestantes = diasVividos % 365
    mesesVividos = (anosVividos * 12 ) - diasRestantes
    diasVividos = (anosVividos * 365) - diasRestantes
    
    return anosVividos, mesesVividos, diasVividos
    
ano_nascimento = int(input("Digite o ano de nascimento: "))
mes_nascimento = int(input("Digite o mês de nascimento (1-12): "))
dia_nascimento = int(input("Digite o dia de nascimento (1-30): "))

anos, meses, dias = calcularVida(ano_nascimento, mes_nascimento, dia_nascimento)
print(f'Você já viveu {anos} anos, {meses} meses e {dias} dias!')