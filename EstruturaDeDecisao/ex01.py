""" Faça um Programa que peça dois números e imprima o maior deles."""

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
print(f'O maior numero entre {num1} e {num2} é: ')
if num1 > num2:
    print(num1)
else:
    print(num2)