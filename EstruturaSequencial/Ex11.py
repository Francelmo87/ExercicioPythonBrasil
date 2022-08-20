""" Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo."""


num1 = int(input('Digite um número inteiro:'))
num2 = int(input('Digite um outro numero inteiro: '))
num3 = float(input('Digite um número real: '))
a = (2 * num1) * (num2 / 2)
b = (3 * num1) + num3
c = num3 ** 3
print(f'A. O produto do dobro do primeiro com metade do segundo é {a}')
print(f'B. A soma do triplo do primeiro com o terceiro é {b}')
print(f'C. O terceiro elevado ao cubo é {c}')
