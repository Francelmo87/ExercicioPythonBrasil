""" Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
a.comprar apenas latas de 18 litros;
b.comprar apenas galões de 3,6 litros;
c.misturar latas e galões, de forma que o desperdício de tinta seja menor.
 Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

import math

# B = float(input('Digite o comprimento da área: '))
# L = float(input('Digite a largura  da área: '))
# area = B * L
area = int(input('Digite a área em m² a ser Pintada: '))
area_com_folga = area * 1.1
litros_por_m2 = 6
litros_a_serem_usados = area_com_folga /litros_por_m2

litros_por_latas = 18
numero_de_latas = math.ceil(litros_a_serem_usados / litros_por_latas)
valor_da_lata = 80
valor_com_apenas_latas = numero_de_latas * valor_da_lata
print(f'A. você devera usar {numero_de_latas} latas de 18 litros,no valor de R$ {valor_com_apenas_latas}')

litros_por_galao = 3.6
numero_de_galoes = math.ceil(litros_a_serem_usados / litros_por_galao)
valor_do_galao = 25
valor_com_apenas_galoes = numero_de_galoes * valor_do_galao
print(f'B. você devera usar {numero_de_galoes} galoes de 3,6 litros,no valor de R$ {valor_com_apenas_galoes}')

# valor da compra otimizada
numero_de_latas = math.floor(litros_a_serem_usados / litros_por_latas)
valor_da_lata = 80
valor_de_latas = numero_de_latas * valor_da_lata
litros_faltantes = litros_a_serem_usados % litros_por_latas
numero_de_galoes = math.ceil(litros_faltantes / litros_por_galao)
valor_do_galao = 25
valor_com_galoes = numero_de_galoes * valor_do_galao

valor_total = valor_de_latas + valor_com_galoes

print(f'C. você devera usar {numero_de_latas} lata(s) de 18 litros mais {numero_de_galoes} galão(s) de 3,6 litros,no valor de R$ {valor_total}')



