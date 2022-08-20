"""  Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""

F = int(input('Digite qual é valor em fahrenheigt:  '))
C = 5 * ((F-32) / 9)
print(f'o valor de {F} em fahrenheigt em graus celsius é {C:.2f}')
