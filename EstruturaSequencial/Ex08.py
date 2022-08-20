""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês."""

salario = float(input('Qual é o valor da hora trabalhada: '))
horas = int(input('Quantas hora você trabalha mensalmente: '))
result = salario * horas
print(f'você ganha {result :.2f} por {horas} horas trabalhada')
