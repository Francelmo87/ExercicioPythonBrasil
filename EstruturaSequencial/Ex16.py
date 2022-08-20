"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário
a quantidades de latas de tinta a serem compradas e o preço total."""

area = int(input('Digite a área em m² a ser Pintada: '))
litros_por_m2 = 3
litros_a_serem_usados = area /litros_por_m2
litros_por_latas = 18
numero_de_latas = litros_a_serem_usados / litros_por_latas
valor_da_lata = 80
valor_total = numero_de_latas * valor_da_lata
print(f'A quantidade de {numero_de_latas}latas de 18 litros,no valor de R$ {valor_total}')