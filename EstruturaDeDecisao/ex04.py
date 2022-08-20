"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

letra = input('Digite uma letra: ').lower()
if letra == 'a' or 'e' or 'i' or 'o' or 'u':
    print('A letra digitada foi uma vogal')
else:
    print('A letra digitada foi uma Consoante')