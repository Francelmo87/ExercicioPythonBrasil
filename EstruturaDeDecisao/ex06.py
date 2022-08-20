""" Faça um Programa que leia três números e mostre o maior deles."""

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro  número: '))
print(f'O maior número entre os {num1}, {num2}, {num3} é: ')
if num1 > num2:
    print(num1)
elif num2 > num3:
    print(num2)
else:
    print(num3)
