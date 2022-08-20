""" João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
 deve pagar uma multa de R$ 4,00 por quilo excedente.

 João precisa que você faça um programa que leia a variável peso (peso de peixes)
 e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e
  na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""

peso = float(input('Digite qual foi o peso dos peixes: '))
limite_de_peso = 50
excesso = peso - limite_de_peso
valor_da_multa = 4
multa = excesso * valor_da_multa
print(f'A quantidade pescada foi de {peso} Kg\n'
      f'excendendo em {excesso} kg o limite permitido no Estado, \n'
      f'sendo a multa por excesso no valor de R$ {multa}')

