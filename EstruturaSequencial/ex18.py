""" Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

tamanho_arquivo = int(input('Digite o tamanho do arquivo para download em MB:'))
velocidade = int(input('Digite a velocidade de um link de internet em Mbps: '))
tempo_em_minutos= (tamanho_arquivo / velocidade) / 60
print(f'O arquivo de {tamanho_arquivo} Mb com link de dowload de {velocidade} Mbps levara aproximadamente {tempo_em_minutos} minutos')
