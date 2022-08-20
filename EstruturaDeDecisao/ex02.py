""" Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""


valor = int(input('Digite um número pode ser positivo ou negativo: '))
print(f'O número {valor} que voce digitou é: ')
if valor >= 0:
    print("Positivo"),
else:
    print('negativo')
