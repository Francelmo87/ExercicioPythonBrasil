# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.


C = int(input('Digite qual é valor em Célsius:  '))
F = (C*9/5) + 32
print(f'o valor de {C} graus célsius em graus fahrenheigt é {F:.1f}')