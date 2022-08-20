""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""

import math
valor_da_hora = int(input('Digite o valor da hora trabalhada:'))
hora = int(input('Digite quantas horas você trabalha por mês:'))
salario_bruto= valor_da_hora * hora
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindical = salario_bruto * 0.05
salario_liquido_sem_ir = salario_bruto - desconto_inss - desconto_sindical
salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindical

print(f'A. O salario bruto foi R$ {salario_bruto}')
print(f'B. Foi pago ao INSS R$ {desconto_inss}')
print(f'C. Foi pago ao Sindicato R$ {desconto_sindical}')
print(f'D. O salario líquido sem Imposto retido na fonte foi R$ {salario_liquido_sem_ir}')
print(f'E.  + Salário Bruto : R${salario_bruto}\n'
      f'    - IR (11%) : R${desconto_ir}\n'
      f'    - INSS (8%) : R${desconto_inss}\n'
      f'    - Sindicato ( 5%) : R${desconto_sindical}\n'
      f'    = Salário Liquido : R${salario_liquido}'
      )
